# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 15:36:33 2018

@author: 李弘一萌
"""

import pandas as pd
from sqlalchemy.orm import sessionmaker
from ..Base import SQL_CommonData_Base
import os, shutil
import openpyxl
from datetime import datetime
from ..Global_Factory import Global_Factory
from ..IndexTable import CmtDB_Index
import os

def type_translate(ts):
    if "value" in ts.index:
        ts["value"] = float(ts["value"])
    if "date" in ts.index:
        ts["date"] = ts["date"].to_pydatetime()      
    return ts



class CMTDB_Update(object):
    
    def __init__(self, cmt_name, update_type, spec_col=None):
        self.cmt_name = cmt_name
        self.spec_col = spec_col
        self.update_type = update_type
        self.cmt_cls = Global_Factory.getBaseObj(cmt_name)
        self.default_dstfile = self.cmt_cls.relative_data_path + "update/update_backup/" + datetime.now().strftime("%Y-%m-%d-%H_%M_%S")
    
    @staticmethod
    def drop_non_float_value(original_df):
        drop_list = []
        for i in range(len(original_df)):
            try:
                original_df.loc[i, "value"] = float(original_df.loc[i, "value"])
            except ValueError:
                print(i)
                drop_list.append(i)
                continue
        original_df.drop(drop_list, inplace=True)
        return original_df    

    def backup_original_update(self, srcfile=None, dstfile=None):
        if dstfile is None:
            dstfile = self.default_dstfile
        if not os.path.exists(dstfile):
            os.makedirs(dstfile)
        if srcfile is not None:
            try:
                shutil.copy(srcfile, dstfile) 
            except Exception as e:
                print(repr(e))
        return dstfile       
    
    def backup_update_df(self, df):
#        print("BackUp Start")
        current_dir = os.getcwd()
        backup_dir = current_dir + "\\Update_BackUp\\" + self.cmt_name + "\\" + datetime.today().strftime("%Y%m%d") + "\\" + self.update_type + "_Update"
        if not os.path.exists(backup_dir):
            os.makedirs(backup_dir)
        df.to_excel(backup_dir + "\\" + datetime.now().strftime("%H_%M_%S") + ".xlsx", encoding="gbk")
        
    
    @staticmethod
    def local_table_load(path):
        tmp_wb = openpyxl.load_workbook(path)
        sheets_name_list = tmp_wb.sheetnames
        sheet_df_list = []
        for tmp_sheet in sheets_name_list:                
            tmp_sheet_df = pd.read_excel(path, index_col=0, encoding="gbk", sheet_name=tmp_sheet, parse_dates=[0])
            sheet_df_list.append(tmp_sheet_df)
        if len(sheet_df_list) == 0:
            raise Exception("载入的excel文件无有效数据可更新")
        else:
            table = pd.concat(sheet_df_list, axis=1, sort=False)
            if len(sheet_df_list) == 0:
                raise Exception("载入的excel文件无有效数据可更新")
            return table
    
    
    
    def table_generate_from_file(self, table):
        transformed_series_list = []
        false_list = []
        tmp_log = ""
        for col in table.columns.tolist():
            if not self.cmt_cls.check_col_available(col):
                false_list.append(col)
                print("Warning：" + col + "不存在于" + self.cmt_name + "数据库中")
            else:
                print(col + u"开始转换")
                tmp_series = table[col].dropna()
                if len(tmp_series) == 0:
                    tmp_log += "%s：'%s'更新0条数据\n" % (self.cmt_name, col)
                    continue
                tmp_col_obj = Global_Factory.getobj(col, self.cmt_name)
                if hasattr(tmp_col_obj, "update_table_generate"):
                    tmp_transformed_df = tmp_col_obj.update_table_generate(tmp_series)
                    tmp_log += "%s：'%s'更新%d条数据，更新起始日期%s，截止日期%s；\n" % (self.cmt_name, col, len(tmp_transformed_df), 
                                                                  tmp_transformed_df["date"].iloc[0].to_pydatetime().strftime("%Y-%m-%d"), 
                                                                  tmp_transformed_df["date"].iloc[-1].to_pydatetime().strftime("%Y-%m-%d"))                      
                    transformed_series_list.append(tmp_transformed_df)
        transformed_df = pd.concat(transformed_series_list)
        transformed_df.reset_index(inplace=True)
        transformed_df = transformed_df.drop(["index"], axis=1)
        transformed_df = CMTDB_Update.drop_non_float_value(transformed_df)
        transformed_df.reset_index(inplace=True)
        transformed_df = transformed_df.drop(["index"], axis=1)
        return transformed_df, tmp_log, false_list
    
    @staticmethod
    def standard_local_update(update_obj_list, srcfile):
        update_df = CMTDB_Update.local_table_load(srcfile)
        log = ""
        false_set_list = []
        cmt_name_list = [x.cmt_name for x in update_obj_list]
        for update_obj in update_obj_list:
            transformed_df, new_log, false_list = update_obj.table_generate_from_file(update_df)
            log += new_log
            false_set_list.append(set(false_list))
            if len(transformed_df) != 0:
                update_obj.upload_table(transformed_df)
                update_obj.backup_update_df(transformed_df)
                index_update_df = transformed_df.groupby("col").last().drop(["value", "field", "table"], axis=1).reset_index().rename(columns={"date": "last_date"})
                index_update_df["update_date"] = datetime.today()
                index_update_df["cmt"] = update_obj.cmt_name            
                CmtDB_Index.update_sql_cmtdb_condition(index_update_df)
                log += "%s本次更新手动数据已入库！\n" % (update_obj.cmt_name)
        total_false_col_list = list(set.intersection(*false_set_list))
        if len(total_false_col_list) != 0: 
            log += ",".join(total_false_col_list) + "不存在于" + ",".join(cmt_name_list) + "数据库中, 未更新这些指标！"
        else:
            log += "本次" + ",".join(cmt_name_list) + "数据库手动更新完成！"    
        log += "\n"
        print(log)    
        return update_df, log
    
    def standard_wind_update(self, mode="merge", start_date=None):
        dstfile = self.backup_original_update()
#        wind_col_dict = self.cmt_cls.get_all_windcol_class()
#        print(wind_col_dict.keys())
        wind_df = CmtDB_Index().get_wind_index_df(self.cmt_name)
        df, log = self.wind_table_update(wind_df, dstfile, start_date)
        if df is not None:
            self.upload_table(df, mode)
            self.backup_update_df(df)
            # 更新index数据库
            index_update_df = df.groupby("col").last().drop(["value", "field", "table"], axis=1).reset_index().rename(columns={"date": "last_date"})
            index_update_df["update_date"] = datetime.today()
            index_update_df["cmt"] = self.cmt_name            
            CmtDB_Index.update_sql_cmtdb_condition(index_update_df)
            log += "%s本次更新万得数据已入库！" % (self.cmt_name)
        log += "\n"
#        print(log)   
        return df, log
    

    def wind_table_update(self, wind_df, dstfile=None, start_date=None):
        if dstfile is None:
            dstfile = self.default_dstfile
#        tm1p_log = "%s万得数据开始更新！\n" % self.cmt_name
        tmp_log = ""
        update_df_list = []
        for index, row in wind_df.iterrows():
            tmp_col_obj = Global_Factory.getobj(row["data_name"], self.cmt_name)
            tmp_update_df = tmp_col_obj.download_wind_quote(start_date=start_date)
            if (tmp_update_df is None) or (len(tmp_update_df) == 0):
                tmp_log += "%s：'%s'无新数据更新；\n" % (self.cmt_name, tmp_col_obj.col_name)
                continue        
            tmp_update_df.columns = ["value"]
            tmp_update_df["field"] = tmp_col_obj.field_name
            tmp_update_df["col"] = tmp_col_obj.col_name
            tmp_update_df["date"] = tmp_update_df.index.tolist()
            tmp_update_df["table"] = tmp_col_obj.table_chinese_name
            tmp_log += "%s：'%s'更新%d条数据，更新起始日期%s，截止日期%s；\n" % (self.cmt_name, tmp_col_obj.col_name, len(tmp_update_df), 
                                                            tmp_update_df.index[0].to_pydatetime().strftime("%Y-%m-%d"), 
                                                            tmp_update_df.index[-1].to_pydatetime().strftime("%Y-%m-%d"))    
            update_df_list.append(tmp_update_df)
        if len(update_df_list) == 0:
            print(u"本次wind全部指标无需更新")
            tmp_log += "%s本次无万得数据更新\n" % (self.cmt_name)
            return None, tmp_log
        transformed_df = pd.concat(update_df_list)
        transformed_df.reset_index(inplace=True)
        transformed_df = transformed_df.drop(["index"], axis=1)
        transformed_df = CMTDB_Update.drop_non_float_value(transformed_df)
        transformed_df.reset_index(inplace=True)
        transformed_df = transformed_df.drop(["index"], axis=1)
        transformed_df.to_excel(dstfile + "/update_transformed.xlsx", encoding="gbk")
        print(u"wind指标下载完毕")
        tmp_log += "%s本次万得数据更新完毕\n" % (self.cmt_name)
        return transformed_df, tmp_log
    
    def upload_table(self, transformed_df, mode="merge"):
        engine = self.cmt_cls.engine 
        SQL_CommonData_Base.Base.metadata.create_all(engine)
        session = sessionmaker()
        session.configure(bind=engine)
        s = session()
        class_variable = SQL_CommonData_Base.SQL_CommonData
        try:
            tmp_upload_df = transformed_df[["col", "table", "field", "date", "value"]]                
            for i in range(len(tmp_upload_df)):
                tmp_ts = tmp_upload_df.iloc[i,:].copy()
                tmp_ts = type_translate(tmp_ts)
                record = class_variable(**dict(tmp_ts))
                if mode == "merge":
                    s.merge(record)  
                elif mode == "add":
                    s.add(record)
                else:
                    raise Exception("Wrong Update Mode")
            s.commit() #Attempt to commit all the records
        except Exception as e:
            print(repr(e))
            s.rollback() #Rollback the changes on error
            raise e
        finally:
            s.close()
            
    def update_start_last_date_length(self, col=None):
        if col is None:
            col_list = []
            start_date_list = []
            last_date_list = []
            length_list = []
            col_cls_dict = self.cmt_cls.get_all_col_class()
            for col_cls in col_cls_dict.keys():
                tmp_obj = col_cls_dict[col_cls]()
                tmp_col = tmp_obj.col_name
                tmp_ts = tmp_obj.get_ts().dropna()
                if len(tmp_ts) == 0:
                    col_list.append(tmp_col)
                    start_date_list.append(None)
                    last_date_list.append(None)
                    length_list.append(0)
                else:
                    tmp_start_date = tmp_ts.index[0]
                    tmp_last_date = tmp_ts.index[-1] 
                    tmp_length = len(tmp_ts)
                    col_list.append(tmp_col)
                    start_date_list.append(tmp_start_date)
                    last_date_list.append(tmp_last_date)
                    length_list.append(tmp_length)
            update_df = pd.DataFrame([col_list, start_date_list, last_date_list, length_list], 
                                     index=["col", "start_date", "last_date", "length"]).T
            
        else:
            tmp_col_obj = Global_Factory.getobj(col, self.cmt_name)
            tmp_ts = tmp_col_obj.get_ts().dropna()
            if len(tmp_ts) == 0:
                tmp_length = 0
                tmp_start_date = None
                tmp_last_date = None
            else:
                tmp_start_date = tmp_ts.index[0]
                tmp_last_date = tmp_ts.index[-1]
                tmp_length = len(tmp_ts)
            update_df = pd.DataFrame([[col, tmp_start_date, tmp_last_date, tmp_length]], 
                                     columns=["col", "start_date", "last_date", "length"])
        if len(update_df) != 0:
            update_df["cmt"] = self.cmt_name
            CmtDB_Index.update_sql_cmtdb_condition(update_df)            
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
            
        