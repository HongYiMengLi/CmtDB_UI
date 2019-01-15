# -*- coding: utf-8 -*-
"""
Created on Tue Sep 04 08:15:15 2018

@author: Administrator
"""

import pandas as pd
import os, shutil
from datetime import datetime
from .L_Base import L_Base
from . import L_Device_SQLTable
from ....Futures_Data.DateTime.Trade_Date import Trade_Date

from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_


file_data_path = L_Base.relative_data_path + "files/Device_Files/"
#total_col_df = pd.read_excel(file_data_path + u"PE装置Field_Table.xlsx", index_col=0, encoding="gbk") 
#liscence_list_df = pd.read_excel(file_data_path + u"PE牌号.xlsx", index_col=0, encoding="gbk") 
#liscence_list_df.index = [str(x) for x in liscence_list_df.index]
#field_list_df = pd.read_excel(file_data_path + u"PE装置类别.xlsx", index_col=0, encoding="gbk") 

# 装置profile类
class total_device(object):
    file_path = file_data_path + "PE装置Field_Table.xlsx"
    
    @staticmethod
    def type_translate(ts):
        if "available_date" in ts.index:
            ts["available_date"] = ts["available_date"].to_pydatetime()   
        if "capability" in ts.index:
            ts["capability"] = float(ts["capability"])
        return ts    
    
    # 上传
    @staticmethod
    def upload_total_df():
        total_col_df = pd.read_excel(total_device.file_path, encoding="gbk", parse_dates=["available_date"])
        if len(total_col_df) == 0:
            raise("PE装置profile本地文件导入失败")
        session = sessionmaker()
        session.configure(bind=L_Base.engine)
        s = session()  
        try:
            L_Device_SQLTable.SQL_Device_Profile.__table__.drop(L_Base.engine)
            L_Device_SQLTable.SQL_Device_Profile.__table__.create(L_Base.engine)
            for i in range(len(total_col_df)):   
                tmp_ts = total_col_df.iloc[i,:].copy()
                tmp_ts = total_device.type_translate(tmp_ts)
                record = L_Device_SQLTable.SQL_Device_Profile(**dict(tmp_ts))
                s.add(record)    
            s.commit() #Attempt to commit all the records
        except Exception as e:
            print(repr(e))
            s.rollback() #Rollback the changes on error
            raise
        finally:
            s.close() #Close the connection
    
    # 提取
    @staticmethod
    def get_total_df(mode="db"):
        if mode == "local":
            total_col_df = pd.read_excel(total_device.file_path, encoding="gbk", parse_dates=["available_date"])
        elif mode == "db":
            session = sessionmaker()
            session.configure(bind=L_Base.engine)
            s = session()  
            try:
                tmp_query = s.query(L_Device_SQLTable.SQL_Device_Profile)
                total_col_df = pd.read_sql(tmp_query.statement, L_Base.engine)
            except Exception as e:
                print(repr(e))
                s.rollback() #Rollback the changes on error
                raise
            finally:
                s.close() #Close the connection
        else:
            raise("Wrong mode parameter: " + mode)
        return total_col_df


    # 提取
    @staticmethod
    def get_total_df(mode="db"):
        if mode == "local":
            total_col_df = pd.read_excel(total_device.file_path, encoding="gbk", parse_dates=["available_date"])
        elif mode == "db":
            session = sessionmaker()
            session.configure(bind=L_Base.engine)
            s = session()  
            try:
                tmp_query = s.query(L_Device_SQLTable.SQL_Device_Profile)
                total_col_df = pd.read_sql(tmp_query.statement, L_Base.engine)
            except Exception as e:
                print(repr(e))
                s.rollback() #Rollback the changes on error
                raise
            finally:
                s.close() #Close the connection
        else:
            raise("Wrong mode parameter: " + mode)
        return total_col_df
    
# 牌号类
class product_license(object):
    file_path = file_data_path + "PE牌号.xlsx"
    
    @staticmethod
    def type_translate(ts):
        if "id_" in ts.index:
            ts["id_"] = str(ts["id_"])
        return ts    
    
    
    @staticmethod
    def upload_product_license():
        liscence_list_df = pd.read_excel(product_license.file_path, index_col=0, encoding="gbk") 
        if len(liscence_list_df) == 0:
            raise("PE牌号文件本地文件导入失败")
        liscence_list_df.index = [str(x) for x in liscence_list_df.index]
        liscence_list_df = liscence_list_df.fillna("")
        liscence_list_df.index.name = "product"
        liscence_list_df = liscence_list_df.reset_index()
        session = sessionmaker()
        session.configure(bind=L_Base.engine)
        s = session()  
        try:
            L_Device_SQLTable.SQL_Product_License.__table__.drop(L_Base.engine)
            L_Device_SQLTable.SQL_Product_License.__table__.create(L_Base.engine)
            for i in range(len(liscence_list_df)):   
                tmp_ts = liscence_list_df.iloc[i, :].copy()
                tmp_ts = product_license.type_translate(tmp_ts)

                record = L_Device_SQLTable.SQL_Product_License(**dict(tmp_ts))
                s.add(record)    
            s.commit() # Attempt to commit all the records
        except Exception as e:
            print(repr(e))
            s.rollback() # Rollback the changes on error
            raise
        finally:
            s.close() # Close the connection
        
    @staticmethod
    def get_product_license(mode="db"):
        if mode == "local":
            liscence_list_df = pd.read_excel(product_license.file_path, index_col=0, encoding="gbk")
        elif mode == "db":
            session = sessionmaker()
            session.configure(bind=L_Base.engine)
            s = session()  
            try:
                tmp_query = s.query(L_Device_SQLTable.SQL_Product_License)
                liscence_list_df = pd.read_sql(tmp_query.statement, L_Base.engine)
                liscence_list_df = liscence_list_df.drop(["id"], axis=1).set_index("product")
                
            except Exception as e:
                print(repr(e))
                s.rollback() #Rollback the changes on error
                raise
            finally:
                s.close() #Close the connection
        else:
            raise("Wrong mode parameter: " + mode)
        return liscence_list_df
    
# 细分装置对应大类表
class field_list(object):
    file_path = file_data_path + "PE装置类别.xlsx"
        
    @staticmethod
    def upload_field_list():
        field_list_df = pd.read_excel(field_list.file_path, index_col=0, encoding="gbk") 
        if len(field_list_df) == 0:
            raise("PE装置类别对应大类本地文件导入失败")
        field_list_df.index.name = "product_class"
        field_list_df = field_list_df.reset_index()
        session = sessionmaker()
        session.configure(bind=L_Base.engine)
        s = session()  
        try:
            L_Device_SQLTable.SQL_Field_List.__table__.drop(L_Base.engine)
            L_Device_SQLTable.SQL_Field_List.__table__.create(L_Base.engine)
            for i in range(len(field_list_df)):   
                tmp_ts = field_list_df.iloc[i, :].copy()
#                tmp_ts = product_license.type_translate(tmp_ts)
                record = L_Device_SQLTable.SQL_Field_List(**dict(tmp_ts))
                s.add(record)    
            s.commit() # Attempt to commit all the records
        except Exception as e:
            print(repr(e))
            s.rollback() # Rollback the changes on error
            raise
        finally:
            s.close() # Close the connection
        
        
    @staticmethod
    def get_field_list(mode="db"):
        if mode == "local":
            field_list_df = pd.read_excel(field_list.file_path, index_col=0, encoding="gbk")
        elif mode == "db":
            session = sessionmaker()
            session.configure(bind=L_Base.engine)
            s = session()  
            try:
                tmp_query = s.query(L_Device_SQLTable.SQL_Field_List)
                field_list_df = pd.read_sql(tmp_query.statement, L_Base.engine)
                field_list_df = field_list_df.set_index("product_class")
                
            except Exception as e:
                print(repr(e))
                s.rollback() #Rollback the changes on error
                raise
            finally:
                s.close() #Close the connection
        else:
            raise("Wrong mode parameter: " + mode)
        return field_list_df
    
# functions    
    
def liscence_to_specific_field(x, liscence_list_df): 
    if x in liscence_list_df.index:
        return liscence_list_df.loc[x, u"类别"]
    elif x == u"停车":
        return u"停车"
    else:
        return u"无此牌号"


def specific_field_to_field(x, field_list_df):        
    if x in field_list_df.index:
        tmp_field = field_list_df.loc[x, u"大类别"]
        return tmp_field
    elif x == u"停车":
        return u"停车"
    else:
        print(x)
        raise Exception(u"Wrong Field") 


def field_to_device_list(ts, field_list_df, field=u"all"):
    tmp_ts = ts.dropna()
    if field == u"all":
        return tmp_ts.index.tolist()
    else:
        if field not in field_list_df[u"大类别"].unique().tolist():
            print(field)
            raise Exception(u"Wrong Field")
        else:
            tmp_list = tmp_ts[tmp_ts==field].index.tolist()
            return tmp_list



###############################################################################

class L_Device_Process(object):
    @staticmethod
    def local_hist_data_process():
        local_data_path = L_Base.relative_data_path + "local/"        
        hist_table = pd.read_excel(local_data_path + u"PE装置历史数据.xlsx", encoding="gbk") 
        hist_table.iloc[:, [0, 1]] = hist_table.iloc[:, [0, 1]].ffill()
        liscence_list = []
        for i in range(len(hist_table)):
            tmp_company = hist_table.iloc[i][u"所属"]
#            if tmp_company == u"辽通化工":
#                continue
            tmp_field = hist_table.iloc[i][u"品种"]
            tmp_cls = L_Device_Factory.get_device_cls(tmp_company, tmp_field)
            tmp_obj = tmp_cls()
            tmp_series = hist_table.iloc[i, 5:].dropna()
            tmp_liscence_df = tmp_obj.original_data_to_liscence(tmp_series)
            liscence_list.append(tmp_liscence_df)
        total_liscence_df = pd.concat(liscence_list, axis=1)
        total_liscence_df = total_liscence_df.resample("D").ffill()
        total_liscence_df = total_liscence_df.fillna(method="ffill")
        return total_liscence_df
    
    
    
    @staticmethod
    def L_Device_Update():
        dstfile = L_Base.relative_data_path + "update/update_backup/" + datetime.now().strftime("%Y-%m-%d-%H_%M_%S")
        srcfile = L_Base.relative_data_path + "update/update_source/update_source.xlsx"
        os.makedirs(dstfile)
        shutil.copy(srcfile, dstfile)
        total_liscence_df = L_Device_Process.update_data_process()
        ts, miss = L_Device_Process.liscence_df_to_field(total_liscence_df)
        if len(miss) != 0:
            print("存在无法查到的牌号")
            return miss
        else:
            transformed_df = L_Device_Process.local_table_2_sql_table(total_liscence_df)
            L_Device_Process.upload_table(transformed_df)
            transformed_df.to_excel(dstfile + "/update_transformed.xlsx", encoding="gbk")
            return None
            
            
    @staticmethod
    def update_data_process():
        local_data_path = L_Base.relative_data_path + "update/update_source/"        
        hist_table = pd.read_excel(local_data_path + u"device_update.xlsx", encoding="gbk") 
        hist_table.iloc[:, [0, 1]] = hist_table.iloc[:, [0, 1]].ffill()
        liscence_list = []
        for i in range(len(hist_table)):
            tmp_company = hist_table.iloc[i][u"所属"]
            tmp_field = hist_table.iloc[i][u"品种"]
            tmp_cls = L_Device_Factory.get_device_cls(tmp_company, tmp_field)
            tmp_obj = tmp_cls()
            tmp_series = hist_table.iloc[i, 5:].dropna()
            tmp_liscence_df = tmp_obj.original_data_to_liscence(tmp_series)
            liscence_list.append(tmp_liscence_df)
        total_liscence_df = pd.concat(liscence_list, axis=1)
        total_liscence_df = total_liscence_df.resample("D").ffill()
        total_liscence_df = total_liscence_df.fillna(method="ffill")
        return total_liscence_df
    
    @staticmethod
    def liscence_df_to_field(liscence_df): 
        total_field_list = []
        total_miss_list = []
        license_list_df = product_license.get_product_license()
        for col in liscence_df.columns:
            print(col)
            tmp_series = liscence_df[col].dropna()
            tmp_field_series = tmp_series.apply(lambda x: liscence_to_specific_field(x, license_list_df))
            tmp_miss_series = tmp_series[tmp_field_series==u"无此牌号"]
            tmp_miss_series.index = [(tmp_miss_series.name + x.strftime("%Y-%m-%d")) for x in tmp_miss_series.index]
            tmp_miss_series.name = u"无效牌照"
            total_field_list.append(tmp_field_series)
            total_miss_list.append(tmp_miss_series)
        total_field_df = pd.concat(total_field_list, axis=1)
        total_miss_ts = pd.concat(total_miss_list)
        return total_field_df, total_miss_ts

    @staticmethod
    def local_table_2_sql_table(total_liscence_df): 
        table_df_list = []
        for i in total_liscence_df.columns:
            tmp_obj = L_Device_Factory.get_device_cls_from_col(i)()
            tmp_series = total_liscence_df[i].dropna()
            tmp_df = tmp_obj.update_table_generate(tmp_series)
            table_df_list.append(tmp_df)
        total_transformed_table = pd.concat(table_df_list)
        return total_transformed_table
    
    @staticmethod
    def type_translate(ts):
        if "date" in ts.index:
            ts["date"] = ts["date"].to_pydatetime()
        if "product_yield" in ts.index:
            ts["product_yield"] = float(ts["product_yield"])     
        if "capability" in ts.index:
            ts["capability"] = float(ts["capability"])
        return ts
    
    @staticmethod
    def upload_table(tmp_table_df, chunksize=10000):
        if tmp_table_df is None:
            print(u"上传数据库失败: 无内容")
            return
        session = sessionmaker()
        session.configure(bind=L_Base.engine)
        s = session()  
        try:
            L_Device_SQLTable.SQL_Device.__table__.drop(L_Base.engine)
            L_Device_SQLTable.SQL_Device.__table__.create(L_Base.engine)
            tmp_upload_df = tmp_table_df[["date", "company", "device_name", "field", "pipeline", "product", "product_specifict_class", 
                                          "product_field", "product_yield", "capability"]]
            for chunk in range(0, len(tmp_upload_df), chunksize):
                print(chunk)
                end_point = chunk + chunksize if (chunk + chunksize) <= len(tmp_upload_df) else len(tmp_upload_df)
                tmp_df = tmp_upload_df.iloc[chunk:end_point,:]               
                for i in range(len(tmp_df)):   
                    print(chunk + i)
                    tmp_ts = tmp_df.iloc[i,:].copy()
                    tmp_ts = L_Device_Process.type_translate(tmp_ts)
                    record = L_Device_SQLTable.SQL_Device(**dict(tmp_ts))
                    s.add(record)    
                s.commit() #Attempt to commit all the records
        except Exception as e:
            print(repr(e))
            s.rollback() #Rollback the changes on error
            raise
        finally:
            s.close() #Close the connection
        return
    
    @staticmethod
    def get_product_yield(tmp_product_field=None):
        session = sessionmaker()
        session.configure(bind=L_Base.engine)
        s = session()
        try:
            class_variable = L_Device_SQLTable.SQL_Device
            if tmp_product_field is None:
                tmp_query = s.query(class_variable.date, class_variable.product_yield)
            else:
                tmp_query = s.query(class_variable.date, class_variable.product_yield).filter(class_variable.product_field == tmp_product_field)
            tmp_df = pd.read_sql(tmp_query.statement, L_Base.engine)
            sum_total_yield = tmp_df.groupby("date")["product_yield"].sum()
        except Exception as e:
            print(repr(e))
            s.rollback()
            raise e
        finally:
            s.close()
        return sum_total_yield
    
    @staticmethod
    def get_device_capability(tmp_field=None):
        session = sessionmaker()
        session.configure(bind=L_Base.engine)
        s = session()
        try:
            class_variable = L_Device_SQLTable.SQL_Device
            if tmp_field is None:
                tmp_query = s.query(class_variable.date, class_variable.capability)
            else:
                tmp_query = s.query(class_variable.date, class_variable.capability).filter(class_variable.field == tmp_field)
            tmp_df = pd.read_sql(tmp_query.statement, L_Base.engine)
            sum_total_yield = tmp_df.groupby("date")["capability"].sum()
        except Exception as e:
            print(repr(e))
            s.rollback()
            raise e
        finally:
            s.close()
        return sum_total_yield
    
    @staticmethod
    def get_product_yield_for_specific_field(field, tmp_product_field=None):
        session = sessionmaker()
        session.configure(bind=L_Base.engine)
        s = session()
        try:
            class_variable = L_Device_SQLTable.SQL_Device
            if tmp_product_field is None:
                tmp_query = s.query(class_variable.date, class_variable.product_yield).filter(class_variable.field == field)
            else:
                tmp_query = s.query(class_variable.date, class_variable.product_yield).filter(and_(class_variable.product_field 
                                   == tmp_product_field, class_variable.field == field))
            tmp_df = pd.read_sql(tmp_query.statement, L_Base.engine)
            sum_total_yield = tmp_df.groupby("date")["product_yield"].sum()
        except Exception as e:
            print(repr(e))
            s.rollback()
            raise e
        finally:
            s.close()
        return sum_total_yield

    @staticmethod
    def get_total_product_field_for_date(tmp_date, tmp_product_field=None):
        session = sessionmaker()
        session.configure(bind=L_Base.engine)
        s = session()
        try:
            class_variable = L_Device_SQLTable.SQL_Device
            if tmp_product_field is None:
                tmp_query = s.query(class_variable.company, class_variable.device_name, class_variable.pipeline, class_variable.field, 
                                    class_variable.product_field, class_variable.product_yield).filter(class_variable.date == tmp_date)
            else:
                tmp_query = s.query(class_variable.company, class_variable.device_name, class_variable.pipeline, class_variable.field, 
                                    class_variable.product_field, class_variable.product_yield).filter(and_(class_variable.date == tmp_date,
                                                                                              class_variable.product_field == tmp_product_field))
            tmp_df = pd.read_sql(tmp_query.statement, L_Base.engine)
        except Exception as e:
            print(repr(e))
            s.rollback()
            raise e
        finally:
            s.close()
        return tmp_df
###############################################################################


class L_Device_Factory(object):
    @staticmethod
    def get_device_cls(company, device, mode="db"):
        total_col_df = total_device.get_total_df(mode)
        tmp_df = total_col_df[(total_col_df["company"] == company) & (total_col_df["field"] == device)]
        if len(tmp_df) == 0:
            raise Exception(u"无该装置:" + company + u"_" + device)
        if len(tmp_df) > 1:
            raise Exception(u"装置表重复:" + company + u"_" + device)
        tmp_cls = eval(tmp_df["classname"].iloc[0])
        return tmp_cls
    
    @staticmethod
    def get_device_obj(company, device):
        tmp_cls = L_Device_Factory.get_device_cls(company, device)
        return tmp_cls()

    @staticmethod
    def get_device_cls_from_col(whole_str):
        index1 = whole_str.find(u"_")
        tmp_company = whole_str[:index1]
        index2 = whole_str[(index1+1):].find(u"_")
        if index2 == -1:
            tmp_device = whole_str[(index1+1):]
            tmp_cls = L_Device_Factory.get_device_cls(tmp_company, tmp_device)
        else:
            tmp_device = whole_str[(index1+1):(index1+1+index2)]
            base_cls = L_Device_Factory.get_device_cls(tmp_company, tmp_device)
            tmp_pipe = whole_str[(index1+index2+2):]
            tmp_cls = base_cls.get_pipe_cls(tmp_pipe)
        return tmp_cls
###############################################################################
    
def is_chinese(uchar):
        """判断一个unicode是否是汉字"""
        if uchar >= u'\u4e00' and uchar <= u'\u9fa5':
                return True
        else:
                return False


###############################################################################
class L_Device(object):
    @classmethod
    def get_pipe_cls(cls, pipe_name):
        sub_cls = cls.__subclasses__()
        if len(sub_cls) == 0:
            return None
        for x in sub_cls:
            if x.pipeline_name == pipe_name:
                return x
        return None

    @classmethod
    def get_all_sub_list(cls):
        sub_cls_list = cls.__subclasses__()
        total_sub_list = []
        for sub_cls in sub_cls_list:
            sub_sub_cls_list = sub_cls.__subclasses__()
            if len(sub_sub_cls_list) == 0:
                total_sub_list.append(sub_cls)
            else:
                total_sub_list.extend(sub_sub_cls_list)                
        return total_sub_list

    @classmethod
    def get_all_field_table(cls):
        all_sub_cls_list = cls.get_all_sub_list()
        field_series_list = []
        for sub_cls in all_sub_cls_list:
            tmp_series = sub_cls().get_product_field()
            field_series_list.append(tmp_series)
        total_field_df = pd.concat(field_series_list, axis=1)            
        return total_field_df

    @staticmethod
    def get_company_list_for_field(field=u"all", mode="db"):
        total_field_df = L_Device.get_all_field_table()
        field_list_df = field_list.get_field_list(mode=mode)
        tmp_ts = total_field_df.apply(lambda x: field_to_device_list(x, field_list_df, field), axis=1)
        return tmp_ts


    
    def single_sentence_liscence_withdraw(self, tmp_string):
        index = tmp_string.find(u"产")
        if index == -1:
            return u"停车"
        else:
            count = 0
            liscence = tmp_string[(index+1):]
            for c in liscence:
                if is_chinese(c) or c in [u"，", u",", u" ", u"；", u";"]:
                    break
                count += 1
            if count == 0 and liscence != u"茂金属":
                return u"停车"
            else:
                if liscence != u"茂金属":
                    liscence = liscence[:count]
                return liscence
      
        
        
    def devide_pipeline(self, tmp_string):
        if type(tmp_string) == str:                
            split_list = tmp_string.split(u"，")
            if len(split_list) == 1:
                split_list = split_list[0].split(",")
            if len(split_list) == 1:
                split_list = split_list[0].split(u"；")
            if len(split_list) == 1:
                split_list = split_list[0].split(u"；")
            return split_list
        else:
            raise Exception(str(tmp_string) + "not unicode")
        
                
    def original_data_to_liscence(self, tmp_series):
        cls = self.__class__
        sub_list = cls.__subclasses__()
        total_liscence_list = []
        for d in range(len(tmp_series)):
#            tmp_date = tmp_series.index[d].strftime("%Y-%m-%d") if isinstance(tmp_series.index[d], datetime) else tmp_series.index[d]
            tmp_date = tmp_series.index[d].strftime("%Y-%m-%d")
            print(self.company + u" " + self.device_name + u" " + tmp_date)
            tmp_string = tmp_series.iloc[d]
            if len(sub_list) != 0:
                split_str_list = self.devide_pipeline(tmp_string)
                if (len(split_str_list) != 1) and (len(split_str_list) != len(sub_list)):
                    raise Exception(self.company + u"_" + self.device_name + u" " + tmp_date + u" 文本分割数与线数不符")
                elif len(split_str_list) != 1:
                    tmp_liscence_list = []
                    for tmp_pipe_cls in sub_list:
                        tmp_pipe_name = tmp_pipe_cls.pipeline_name
                        tmp_exist_flag = False
                        for sub_str in split_str_list:
                            index = sub_str.find(tmp_pipe_name)
                            if index == -1:
                                continue
                            else:
                                tmp_exist_flag = True
                                tmp_liscence = self.single_sentence_liscence_withdraw(sub_str)
                                tmp_liscence_list.append(tmp_liscence)
                                break
                        if tmp_exist_flag == False:
                            raise Exception(self.company + u"_" + self.device_name + u" " + tmp_date + 
                                            u" 无此线: " + tmp_pipe_name)
                else:
                    tmp_liscence = self.single_sentence_liscence_withdraw(tmp_string)
                    tmp_liscence_list = [tmp_liscence] * len(sub_list)
            else:
                tmp_liscence = self.single_sentence_liscence_withdraw(tmp_string)
                tmp_liscence_list = [tmp_liscence]
            total_liscence_list.append(tmp_liscence_list)
        if len(sub_list) != 0:
            col_list = [self.company + u"_" + self.device_name + u"_" + x.pipeline_name for x in sub_list]
        else:
            col_list = [self.company + u"_" + self.device_name]
        tmp_liscence_df = pd.DataFrame(total_liscence_list, index=tmp_series.index, columns=col_list)                    
        return tmp_liscence_df
        
    
    def update_table_generate(self, tmp_series, mode="db"):
        tmp_product = tmp_series.values.tolist()
        tmp_dates = tmp_series.index.tolist()
        license_list_df = product_license.get_product_license()
        tmp_field_series = tmp_series.apply(lambda x: liscence_to_specific_field(x, license_list_df))
        tmp_df = pd.DataFrame(tmp_product,columns=["product"])
        tmp_df["date"] = tmp_dates
        tmp_df["company"] = self.company
        tmp_df["device_name"] = self.device_name
        tmp_df["field"] = self.field
        tmp_df["product_specifict_class"] = tmp_field_series.values.tolist()
        tmp_df["product_yield"] = tmp_df["product_specifict_class"].apply(lambda x:0 if x == u"停车" else self.capability)
        tmp_df["capability"] = self.capability
        field_list_df = field_list.get_field_list(mode=mode)
        tmp_df["product_field"] = tmp_field_series.apply(lambda x: specific_field_to_field(x, field_list_df)).values.tolist()
        
        if hasattr(self, "pipeline_name"):
            tmp_df["pipeline"] = self.pipeline_name
        else:
            tmp_df["pipeline"] = self.device_name
        return tmp_df

    def get_product(self):
        session = sessionmaker()
        session.configure(bind=L_Base.engine)
        s = session()
        company = self.company
        device_name = self.device_name
        try:
            class_variable = L_Device_SQLTable.SQL_Device    
            if hasattr(self, "pipeline_name"):            
                pipeline = self.pipeline_name
                tmp_query = s.query(class_variable.date, class_variable.product).filter(and_(class_variable.company==company, 
                                    class_variable.device_name==device_name, class_variable.pipeline==pipeline))
                tmp_series = pd.read_sql(tmp_query.statement, L_Base.engine, index_col="date").iloc[:,0]
                tmp_series.name = company + u"_" + device_name + u"_" + pipeline
            else:
                if len(self.__class__.__subclasses__()) > 0:
                    raise Exception(self.company + u"_" + self.device_name + u"有分线")
                tmp_query = s.query(class_variable.date, class_variable.product).filter(and_(class_variable.company==company, 
                                    class_variable.device_name==device_name))
                tmp_series = pd.read_sql(tmp_query.statement, L_Base.engine, index_col="date").iloc[:,0]
                tmp_series.name = company + u"_" + device_name
        except Exception as e:
            print(repr(e))
            s.rollback()
            raise e
        finally:
            s.close()
        return tmp_series

    def get_product_specific_field(self):
        product_ts = self.get_product()
        license_list_df = product_license.get_product_license()
        field_ts = product_ts.apply(lambda x: liscence_to_specific_field(x, license_list_df))
        return field_ts    

    def get_product_field(self, mode="db"):
        product_ts = self.get_product_specific_field()
        field_list_df = field_list.get_field_list(mode=mode)
        field_ts = product_ts.apply(lambda x: specific_field_to_field(x, field_list_df))
        return field_ts    

    
##########################################################################################################################################
""" 大庆石化 """  

""" 高压 """ 
class DaQingShiHuaGaoYa(L_Device):
    area = u"东北"
    company = u"大庆石化"
    device_name = u"高压"
    field = u"高压"
    available_date = datetime(2009, 1, 1)
    capability = 26.5

class DaQingShiHuaGaoYa_LaoGaoYa(DaQingShiHuaGaoYa):
    pipeline_name = u"老高压"
    capability = 6.5

class DaQingShiHuaGaoYa_XinGaoYa(DaQingShiHuaGaoYa):
    pipeline_name = u"新高压"
    capability = 20

""" 低压 """   
class DaQingShiHuaDiYa(L_Device):
    area = u"东北"
    company = u"大庆石化"
    device_name = u"低压"
    field = u"低压"
    available_date = datetime(2009, 1, 1)
    capability = 24

class DaQingShiHuaDiYa_AXian(DaQingShiHuaDiYa):
    pipeline_name = u"A线"
    capability = 8

class DaQingShiHuaDiYa_BXian(DaQingShiHuaDiYa):
    pipeline_name = u"B线"
    capability = 8

class DaQingShiHuaDiYa_CXian(DaQingShiHuaDiYa):
    pipeline_name = u"C线"
    capability = 8
    
""" 线性 """ 
class DaQingShiHuaXianXing(L_Device):
    area = u"东北"
    company = u"大庆石化"
    device_name = u"线性"
    field = u"线性"
    available_date = datetime(2009, 1, 1)
    capability = 6

""" 全密度二 """ 
class DaQingShiHuaQuanMiDu2(L_Device):
    area = u"东北"
    company = u"大庆石化"
    device_name = u"全密度二"
    field = u"全密度"
    available_date = datetime(2012, 12, 1)
    capability = 30

""" 全密度一 """ 
class DaQingShiHuaQuanMiDu1(L_Device):
    area = u"东北"
    company = u"大庆石化"
    device_name = u"全密度一"
    field = u"全密度"
    available_date = datetime(2012, 12, 1)
    capability = 25
    
###############################################################################    
""" 吉林石化 """  

""" 线性 """
class JiLinShiHuaXianXing(L_Device):
    area = u"东北"
    company = u"吉林石化"
    device_name = u"线性"
    field = u"线性"
    available_date = datetime(2009, 1, 1)
    capability = 27    

""" 低压 """    
class JiLinShiHuaDiYa(L_Device):
    area = u"东北"
    company = u"吉林石化"
    device_name = u"低压"
    field = u"低压"
    available_date = datetime(2009, 1, 1)
    capability = 30       
    
###############################################################################
""" 抚顺石化 """    

""" 低压 """   
class FuShunShiHuaDiYa(L_Device):
    area = u"东北"
    company = u"抚顺石化"
    device_name = u"低压"
    field = u"低压"
    available_date = datetime(2009, 1, 1)
    capability = 14

""" 新低压 """ 
class FuShunShiHuaXinDiYa(L_Device):
    area = u"东北"
    company = u"抚顺石化"
    device_name = u"新低压"
    field = u"低压"
    available_date = datetime(2012, 12, 1)
    capability = 35

""" 新线性 """ 
class FuShunShiHuaXinXianXing(L_Device):
    area = u"东北"
    company = u"抚顺石化"
    device_name = u"新线性"
    field = u"线性"
    available_date = datetime(2012, 12, 1)
    capability = 45
    
###############################################################################
""" 沈阳化工 """ 

""" 线性 """  
class ShenYangHuaGongXianXing(L_Device):
    area = u"东北"
    company = u"沈阳化工"
    device_name = u"线性"
    field = u"线性"
    available_date = datetime(2009, 1, 1)
    capability = 10 

###############################################################################
""" 辽通化工 """  

""" 低压 """     
class LiaoTongHuaGongDiYa(L_Device):
    area = u"东北"
    company = u"辽通化工"
    device_name = u"低压"
    field = u"低压"
    available_date = datetime(2009, 1, 1)
    capability = 45.4

class LiaoTongHuaGongDiYa_LaoZhuangZhiYiXian(LiaoTongHuaGongDiYa):
    pipeline_name = u"老装置一线"
    capability = 7.5
    
class LiaoTongHuaGongDiYa_LaoZhuangZhiErXian(LiaoTongHuaGongDiYa):
    pipeline_name = u"老装置二线"
    capability = 7.5
    
class LiaoTongHuaGongDiYa_XinZhuangZhi(LiaoTongHuaGongDiYa):
    pipeline_name = u"新装置"
    capability = 30.4   
        
###############################################################################
""" 兰州石化 """  

""" 高压 """ 
class LanZhouShiHuaGaoYa(L_Device):
    area = u"西北"
    company = u"兰州石化"
    device_name = u"高压"
    field = u"高压"
    available_date = datetime(2009, 1, 1)
    capability = 20

""" 低压 """ 
class LanZhouShiHuaDiYa(L_Device):
    area = u"西北"
    company = u"兰州石化"
    device_name = u"低压"
    field = u"低压"
    available_date = datetime(2009, 1, 1)
    capability = 17

class LanZhouShiHuaDiYa_LaoXian(LanZhouShiHuaDiYa):
    pipeline_name = u"老线"
    capability = 8.5
    
class LanZhouShiHuaDiYa_XinXian(LanZhouShiHuaDiYa):
    pipeline_name = u"新线"
    capability = 8.5

""" 全密度 """    
class LanZhouShiHuaQuanMiDu(L_Device):
    area = u"西北"
    company = u"兰州石化"
    device_name = u"全密度"
    field = u"全密度"
    available_date = datetime(2009, 1, 1)
    capability = 30

#########################################################################################################################################
""" 延长中煤榆林能化 """

""" 线性 """   
class YanChangZhongMeiYuLinNengHuaXianXing(L_Device):
    area = u"西北"
    company = u"延长中煤榆林能化"
    device_name = u"线性"
    field = u"线性"
    available_date = datetime(2014, 6, 1)
    capability = 20
    
""" 低压 """ 
class YanChangZhongMeiYuLinNengHuaDiYa(L_Device):
    area = u"西北"
    company = u"延长中煤榆林能化"
    device_name = u"低压"
    field = u"低压"
    available_date = datetime(2014, 6, 1)
    capability = 30

#########################################################################################################################################
""" 陕西延长石油延安能源化工 """
    
""" 低压 """ 
class ShanXiYanChangShiYouYanAnNengYuanHuaGong(L_Device):
    area = u"西北"
    company = u"陕西延长石油延安能源化工"
    device_name = u"低压"
    field = u"低压"
    available_date = datetime(2018, 10, 8)
    capability = 45
    
###############################################################################
""" 中煤蒙大新能源 """ 

""" 全密度 """  
class ZhongMeiMengDaXinNengYuanQuanMiDu(L_Device):
    area = u"西北"
    company = u"中煤蒙大新能源"
    device_name = u"全密度"
    field = u"全密度"
    available_date = datetime(2016, 3, 18)
    capability = 30

###############################################################################
""" 中煤榆林能化 """ 

""" 线性 """       
class ZhongMeiYuLinNengHuaXianXing(L_Device):
    area = u"西北"
    company = u"中煤榆林能化"
    device_name = u"线性"
    field = u"线性"
    available_date = datetime(2014, 7, 1)
    capability = 30

###############################################################################
""" 宁夏宝丰能源 """

""" 线性 """   
class NingXiaBaoFengNengYuanQuanMiDu(L_Device):
    area = u"西北"
    company = u"宁夏宝丰能源"
    device_name = u"全密度"
    field = u"全密度"
    available_date = datetime(2014, 11, 1)
    capability = 30

###############################################################################
""" 蒲城清洁能源化工 """

""" 全密度 """  
class PuChengQingJieNengYuanHuaGongQuanMiDu(L_Device):
    area = u"西北"
    company = u"蒲城清洁能源化工"
    device_name = u"全密度"
    field = u"全密度"
    available_date = datetime(2014, 12, 1)
    capability = 30

###############################################################################
""" 神华榆林煤化工项目 """ 

""" 高压 """   
class ShenHuaYuLinMeiHuaGongXiangMuGaoYa(L_Device):
    area = u"西北"
    company = u"神华榆林煤化工项目"
    device_name = u"高压"
    field = u"高压"
    available_date = datetime(2015, 12, 16)
    capability = 30

###############################################################################
""" 神华新疆 """  

""" 高压 """ 
class ShenHuaShenHuaXinJiangGaoYa(L_Device):
    area = u"西北"
    company = u"神华新疆"
    device_name = u"高压"
    field = u"高压"
    available_date = datetime(2016, 10, 3)
    capability = 27
    
###############################################################################
""" 中天合创 """  

""" 高压 """ 
class ZhongTianHeChuangGaoYa(L_Device):
    area = u"西北"
    company = u"中天合创"
    device_name = u"高压"
    field = u"高压"
    available_date = datetime(2016, 10, 26)
    capability = 37

class ZhongTianHeChuangGaoYa_GuanShiGaoYa(ZhongTianHeChuangGaoYa):
    pipeline_name = u"管式高压"
    capability = 25

class ZhongTianHeChuangGaoYa_FuShiGaoYa(ZhongTianHeChuangGaoYa):
    pipeline_name = u"釜式高压"
    capability = 12
    

""" 线性 """     
class ZhongTianHeChuangXianXing(L_Device):
    area = u"西北"
    company = u"中天合创"
    device_name = u"线性"
    field = u"线性"
    available_date = datetime(2017, 5, 1)
    capability = 30

    
###############################################################################
""" 神华宁煤 """

""" 全密度 """  
class ShenHuaNingMeiQuanMiDu(L_Device):
    area = u"西北"
    company = u"神华宁煤"
    device_name = u"全密度"
    field = u"全密度"
    available_date = datetime(2017, 12, 1)
    capability = 45

###############################################################################
""" 神华包头 """ 

""" 全密度 """   
class ShenHuaBaoTouQuanMiDu(L_Device):
    area = u"西北"
    company = u"神华包头"
    device_name = u"全密度"
    field = u"全密度"
    available_date = datetime(2009, 1, 1)
    capability = 30
    
###############################################################################
""" 独山子石化 """

""" 低压 """    
class DuShanZiShiHuaDiYa(L_Device):
    area = u"西北"
    company = u"独山子石化"
    device_name = u"低压"
    field = u"低压"
    available_date = datetime(2009, 1, 1)
    capability = 30    

""" 全密度一 """  
class DuShanZiShiHuaQuanMiDu1(L_Device):
    area = u"西北"
    company = u"独山子石化"
    device_name = u"全密度一"
    field = u"全密度"
    available_date = datetime(2009, 1, 1)
    capability = 22   

class DuShanZiShiHuaQuanMiDu1_YiXian(DuShanZiShiHuaQuanMiDu1):
    pipeline_name = u"一线"
    capability = 13

class DuShanZiShiHuaQuanMiDu1_ErXian(DuShanZiShiHuaQuanMiDu1):
    pipeline_name = u"二线"
    capability = 9

""" 全密度二 """     
class DuShanZiShiHuaQuanMiDu2(L_Device):
    area = u"西北"
    company = u"独山子石化"
    device_name = u"全密度二"
    field = u"全密度"
    available_date = datetime(2009, 1, 1)
    capability = 60   

class DuShanZiShiHuaQuanMiDu2_YiXian(DuShanZiShiHuaQuanMiDu2):
    pipeline_name = u"一线"
    capability = 30

class DuShanZiShiHuaQuanMiDu2_ErXian(DuShanZiShiHuaQuanMiDu2):
    pipeline_name = u"二线"
    capability = 30
    
#########################################################################################################################################
""" 武汉石化 """ 

""" 全密度 """ 
class WuHanShiHuaQuanMiDu(L_Device):
    area = u"华中"
    company = u"武汉石化"
    device_name = u"全密度"
    field = u"全密度"
    available_date = datetime(2013, 7, 13)
    capability = 30    

""" 低压 """
class WuHanShiHuaDiYa(L_Device):
    area = u"华中"
    company = u"武汉石化"
    device_name = u"低压"
    field = u"低压"
    available_date = datetime(2013, 7, 13)
    capability = 30 

###############################################################################
""" 中原乙烯 """  

""" 线性 """
class ZhongYuanYiXiXianXing(L_Device):
    area = u"华中"
    company = u"中原乙烯"
    device_name = u"线性"
    field = u"线性"
    available_date = datetime(2009, 1, 1)
    capability = 26

#########################################################################################################################################
""" 燕山石化 """ 

""" 高压 """ 
class YanShanShiHuaGaoYa(L_Device):
    area = u"华北"
    company = u"燕山石化"
    device_name = u"高压"
    field = u"高压"
    available_date = datetime(2009, 1, 1)
    capability = 38 

class YanShanShiHuaGaoYa_LaoGaoYaYiXian(YanShanShiHuaGaoYa):
    pipeline_name = u"老高压一线"
    capability = 6
    
class YanShanShiHuaGaoYa_LaoGaoYaErXian(YanShanShiHuaGaoYa):
    pipeline_name = u"老高压二线"
    capability = 6

class YanShanShiHuaGaoYa_LaoGaoYaSanXian(YanShanShiHuaGaoYa):
    pipeline_name = u"老高压三线"
    capability = 6

class YanShanShiHuaGaoYa_XinGaoYa(YanShanShiHuaGaoYa):
    pipeline_name = u"新高压"
    capability = 20


""" 低压 """     
class YanShanShiHuaDiYa(L_Device):
    area = u"华北"
    company = u"燕山石化"
    device_name = u"低压"
    field = u"低压"
    available_date = datetime(2009, 1, 1)
    capability = 17.2

class YanShanShiHuaDiYa_YiXian(YanShanShiHuaDiYa):
    pipeline_name = u"一线"
    capability = 8.6

class YanShanShiHuaDiYa_ErXian(YanShanShiHuaDiYa):
    pipeline_name = u"二线"
    capability = 8.6
    
###############################################################################
""" 齐鲁石化 """ 

""" 高压 """  
class QiLuShiHuaGaoYa(L_Device):
    area = u"华北"
    company = u"齐鲁石化"
    device_name = u"高压"
    field = u"高压"
    available_date = datetime(2009, 1, 1)
    capability = 14 

""" 低压 """
class QiLuShiHuaDiYa(L_Device):
    area = u"华北"
    company = u"齐鲁石化"
    device_name = u"低压"
    field = u"低压"
    available_date = datetime(2009, 1, 1)
    capability = 14 

class QiLuShiHuaDiYa_YiXian(QiLuShiHuaDiYa):
    pipeline_name = u"A线"
    capability = 7

class QiLuShiHuaDiYa_ErXian(QiLuShiHuaDiYa):
    pipeline_name = u"B线"
    capability = 7

""" 全密度 """    
class QiLuShiHuaQuanMiDu(L_Device):
    area = u"华北"
    company = u"齐鲁石化"
    device_name = u"全密度装置"
    field = u"全密度"
    available_date = datetime(2013, 1, 1)
    capability = 25 

""" 全密度 """  
class QiLuShiHuaXianXing(L_Device):
    area = u"华北"
    company = u"齐鲁石化"
    device_name = u"线性"
    field = u"全密度"
    available_date = datetime(2009, 1, 1)
    capability = 12 

###############################################################################
""" 天津联化 """ 

""" 线性 """   
class TianJinLianHuaXianXing(L_Device):
    area = u"华北"
    company = u"天津联化"
    device_name = u"线性"
    field = u"线性"
    available_date = datetime(2009, 1, 1)
    capability = 12 

###############################################################################
""" 中沙天津 """  

""" 线性 """  
class ZhongShaTianJinXianXing(L_Device):
    area = u"华北"
    company = u"中沙天津"
    device_name = u"线性"
    field = u"线性"
    available_date = datetime(2010, 1, 1)
    capability = 30 

""" 低压 """  
class ZhongShaTianJinDiYa(L_Device):
    area = u"华北"
    company = u"中沙天津"
    device_name = u"低压"
    field = u"低压"
    available_date = datetime(2010, 1, 1)
    capability = 30 

#########################################################################################################################################
""" 镇海炼化 """  

""" 全密度 """ 
class ZhanHaiLianHuaQuanMiDu(L_Device):
    area = u"华东"
    company = u"镇海炼化"
    device_name = u"全密度"
    field = u"全密度"
    available_date = datetime(2010, 1, 1)
    capability = 45 

###############################################################################
""" 扬子巴斯夫 """

""" 高压 """   
class YangZiBaSiFuGaoYa(L_Device):
    area = u"华东"
    company = u"扬子巴斯夫"
    device_name = u"高压"
    field = u"高压"
    available_date = datetime(2009, 1, 1)
    capability = 20
    
###############################################################################
""" 上海某企业 """  

""" 线性 """   
class ShangHaiMouQiYeXianXing(L_Device):
    area = u"华东"
    company = u"上海某企业"
    device_name = u"线性"
    field = u"线性"
    available_date = datetime(2009, 1, 1)
    capability = 30

""" 低压 """ 
class ShangHaiMouQiYeDiYa(L_Device):
    area = u"华东"
    company = u"上海某企业"
    device_name = u"低压"
    field = u"低压"
    available_date = datetime(2009, 1, 1)
    capability = 30

###############################################################################
""" 上海金菲 """  
class ShangHaiJinFeiDiYa(L_Device):
    area = u"华东"
    company = u"上海金菲"
    device_name = u"低压"
    field = u"低压"
    available_date = datetime(2009, 1, 1)
    capability = 12.5
    
###############################################################################
""" 上海石化 """  

""" 高压 """
class ShangHaiShiHuaGaoYa(L_Device):
    area = u"华东"
    company = u"上海石化"
    device_name = u"高压"
    field = u"高压"
    available_date = datetime(2009, 1, 1)
    capability = 20

class ShangHaiShiHuaGaoYa_1PEYiXian(ShangHaiShiHuaGaoYa):
    pipeline_name = u"1PE一线"
    capability = 5
    
class ShangHaiShiHuaGaoYa_1PEErXian(ShangHaiShiHuaGaoYa):
    pipeline_name = u"1PE二线"
    capability = 5

class ShangHaiShiHuaGaoYa_2PE(ShangHaiShiHuaGaoYa):
    pipeline_name = u"2PE"
    capability = 10

""" 低压 """    
class ShangHaiShiHuaDiYa(L_Device):
    area = u"华东"
    company = u"上海石化"
    device_name = u"低压"
    field = u"低压"
    available_date = datetime(2009, 1, 1)
    capability = 25
    
###############################################################################
""" 扬子石化 """  

""" 全密度 """
class YangZiShiHuaQuanMiDu(L_Device):
    area = u"华东"
    company = u"扬子石化"
    device_name = u"全密度"
    field = u"全密度"
    available_date = datetime(2009, 1, 1)
    capability = 20    

""" 低压 """    
class YangZiShiHuaDiYa(L_Device):
    area = u"华东"
    company = u"扬子石化"
    device_name = u"低压"
    field = u"低压"
    available_date = datetime(2009, 1, 1)
    capability = 27

class YangZiShiHuaDiYa_AXian(YangZiShiHuaDiYa):
    pipeline_name = u"A线"
    capability = 9

class YangZiShiHuaDiYa_BXian(YangZiShiHuaDiYa):
    pipeline_name = u"B线"
    capability = 9    

class YangZiShiHuaDiYa_CXian(YangZiShiHuaDiYa):
    pipeline_name = u"C线"
    capability = 9
    
#########################################################################################################################################
""" 茂名石化 """  

""" 高压 """
class MaoMingShiHuaGaoYa(L_Device):
    area = u"华南"
    company = u"茂名石化"
    device_name = u"高压"
    field = u"高压"
    available_date = datetime(2009, 1, 1)
    capability = 36 

class MaoMingShiHuaGaoYa_LaoGaoYa(MaoMingShiHuaGaoYa):
    pipeline_name = u"老高压"
    capability = 11

class MaoMingShiHuaGaoYa_XinGaoYa(MaoMingShiHuaGaoYa):
    pipeline_name = u"新高压"
    capability = 25

""" 低压 """    
class MaoMingShiHuaDiYa(L_Device):
    area = u"华南"
    company = u"茂名石化"
    device_name = u"低压"
    field = u"低压"
    available_date = datetime(2009, 1, 1)
    capability = 35 

""" 全密度 """
class MaoMingShiHuaQuanMiDu(L_Device):
    area = u"华南"
    company = u"茂名石化"
    device_name = u"全密度"
    field = u"全密度"
    available_date = datetime(2009, 1, 1)
    capability = 22 

###############################################################################
""" 中海油惠州 """  

""" 线性 """
class ZhongHaiYouHuiZhouXianXing(L_Device):
    area = u"华南"
    company = u"中海油惠州"
    device_name = u"线性"
    field = u"线性"
    available_date = datetime(2018, 5, 8)
    capability = 30 

""" 低压 """
class ZhongHaiYouHuiZhouDiYa(L_Device):
    area = u"华南"
    company = u"中海油惠州"
    device_name = u"低压"
    field = u"低压"
    available_date = datetime(2018, 5, 8)
    capability = 40 

###############################################################################
""" 广州石化 """  

""" 线性 """
class GuangZhouShiHuaXianXing(L_Device):
    area = u"华南"
    company = u"广州石化"
    device_name = u"线性"
    field = u"线性"
    available_date = datetime(2009, 1, 1)
    capability = 26 

###############################################################################
""" 福建炼化 """  

""" 全密度一 """
class FuJianLianHuaQuanMiDu1(L_Device):
    area = u"华南"
    company = u"福建炼化"
    device_name = u"全密度一"
    field = u"全密度"
    available_date = datetime(2009, 1, 1)
    capability = 45

""" 全密度二 """    
class FuJianLianHuaQuanMiDu2(L_Device):
    area = u"华南"
    company = u"福建炼化"
    device_name = u"全密度二"
    field = u"全密度"
    available_date = datetime(2009, 1, 1)
    capability = 45

#########################################################################################################################################
""" 四川乙烯 """  

""" 全密度 """  
class SiChuanYiXiQuanMiDu(L_Device):
    area = u"西南"
    company = u"四川乙烯"
    device_name = u"全密度"
    field = u"全密度"
    available_date = datetime(2014, 3, 1)
    capability = 30 

""" 低压 """  
class SiChuanYiXiDiYa(L_Device):
    area = u"西南"
    company = u"四川乙烯"
    device_name = u"低压"
    field = u"低压"
    available_date = datetime(2014, 3, 1)
    capability = 30 

#########################################################################################################################################



if __name__ == "__main__":
#    a = MaoMingShiHuaGaoYa_LaoGaoYa()
#    ts = a.get_product_field()
    
#    print a.capability
#    b = DaQingShiHuaGaoYa_LaoGaoYa()
#    print b.capability
    
#    a = L_Device_Factory.get_device_obj(u"大庆石化", u"低压")
#    b = a.__class__
#    c = b.__subclasses__()
#    print a.capability
#    a=0
    
#    table = L_Device_Process.local_hist_data_process()
#    ts, miss = L_Device_Process.liscence_df_to_field(table)
#
#    aaa = miss.unique()
#    
#    b = aaa[0]
#    
#    d = [miss[miss==x].index[0] for x in aaa]
#    
#    miss_unique= pd.Series(aaa, index=d)

#    table = L_Device_Process.local_hist_data_process()
#    df = L_Device_Process.local_table_2_sql_table(table)
#    L_Device_Process.upload_table(df)
    
#    aaa = L_Device_Factory.get_device_cls_from_col(u"大庆石化_高压_老高压")()
#    df = aaa.get_product()
#    print aaa.device_name
#    

#    ts = L_Device.get_company_list_for_field(u"高压")
#    ts1 = ts.apply(lambda x:",".join(x))
    
#    table1 = L_Device_Process.get_product_yield(u"线性")
#    table1 = L_Device_Process.get_product_yield(u"低压")
    
#    table1 = L_Device_Process.get_device_capability(u"低压")
#    table1 = L_Device_Process.get_product_yield_for_specific_field(u"全密度", u"线性")
#    table2 = L_Device_Process.get_product_yield_for_specific_field(u"全密度", u"低压")
#    table3 = L_Device_Process.get_product_yield_for_specific_field(u"全密度")
#    table = L_Device_Process.update_data_process()
#    ts, miss = L_Device_Process.liscence_df_to_field(table)   
    
#    miss = L_Device_Process.L_Device_Update()    
#    
    date_list = Trade_Date.get_date_list("2018-08-01", "2018-10-31")
    ts_list = []
    for tmp_date in date_list:
        tmp_date = datetime(tmp_date.year, tmp_date.month, tmp_date.day).strftime("%Y-%m-%d")
        tmp_df = L_Device_Process.get_total_product_field_for_date(tmp_date, u"线性")
        tmp_df["tmp"] = "_"
        tmp_df["name"] = tmp_df["company"] + tmp_df["tmp"]  + tmp_df["device_name"] + tmp_df["tmp"]  + tmp_df["pipeline"]
        tmp_df["daily_yield"] = tmp_df["product_yield"] / 365
        tmp_ts = pd.Series(tmp_df["daily_yield"].values.tolist(), index=tmp_df["name"], name=datetime.strptime(tmp_date, "%Y-%m-%d"))
        ts_list.append(tmp_ts)
    df = pd.concat(ts_list, axis=1, sort=False)
    df.columns = [x.strftime("%Y-%m-%d") for x in df.columns]
    df.T.to_excel("LLD2.xlsx", encoding="gbk")
    
    
    
    
    
    
    pass    