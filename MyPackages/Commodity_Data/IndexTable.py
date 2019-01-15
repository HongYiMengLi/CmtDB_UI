# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 14:44:16 2018

@author: 李弘一萌
"""

from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_
import pandas as pd
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Float
from ..SQL.SQL_Connection import SQL_Connection
from ..SQL.database_dict import db_name
from ..Futures_Data.Profile.CmtData import Cmt_Data
from collections import OrderedDict

table_name = "cmtdb_index"
class_name = "CmtDB_Index"
database_name = db_name[class_name]

engine = SQL_Connection.get_connection(database_name, charset="utf8")
Base = declarative_base()
col_dict = {
        "data_field": String(100),
        "data_cmt": String(100),
        "data_name": String(100),
        "data_table": String(100),
        "data_category": String(100),
        "data_type": String(100),
        "computation_formula": String(400),
        "wind_code": String(100),
        "class_name": String(300),
        "table_name": String(300),
        "freq": String(100),
        "source": String(100),
        "length": Integer,
        "start_date": DateTime,
        "last_date": DateTime,
        "update_date": DateTime,
        "remarks": String(400)                
        }


class SQL_CMTDB_Index(Base):
    __tablename__ = table_name
    
    data_cmt = Column(col_dict["data_cmt"], primary_key=True)
    data_name = Column(col_dict["data_name"], primary_key=True)
    data_field = Column(col_dict["data_field"], nullable=False)
    data_table = Column(col_dict["data_table"], nullable=False)
    data_category = Column(col_dict["data_category"], nullable=False)
    data_type = Column(col_dict["data_type"], nullable=False)
    
    computation_formula = Column(col_dict["computation_formula"], nullable=True)
    wind_code = Column(col_dict["wind_code"], nullable=True)
    class_name = Column(col_dict["class_name"], nullable=False)
    table_name = Column(col_dict["table_name"], nullable=False)
    freq = Column(col_dict["freq"], nullable=True)
    source = Column(col_dict["source"], nullable=True)
    length = Column(col_dict["length"], nullable=True)
    start_date = Column(col_dict["start_date"], nullable=True)
    last_date = Column(col_dict["last_date"], nullable=True)
    update_date = Column(col_dict["update_date"], nullable=True)
    remarks = Column(col_dict["remarks"], nullable=True)


included_cmt_dict = OrderedDict()
included_cmt_dict["有色"] = ["CU", "AL", "ZN", "NI"]
included_cmt_dict["化工"] = ["L", "PP", "TA", "BU", "MA", "RU"]
included_cmt_dict["黑色"] = ["JM", "J", "RB", "HC", "ZC", "I"]
included_cmt_dict["农产品"] = ["A", "B", "CF", "M", "OI", "P", "SR", "Y"]

field_dict = {
           "数据名称": "data_name", 
           "数据大类": "data_table", 
           "数据小类": "data_category", 
           "数据类型": "data_type", 
           "计算公式": "computation_formula", 
           "Wind代码": "wind_code", 
           "类名": "class_name",
           "表名": "table_name",
           "频率": "freq", 
           "来源": "source", 
           "起始": "start_date",
           "更新至": "last_date", 
           "更新日期": "update_date", 
           "备注": "remarks",
           "table_name": "table_name",
           "品种": "data_cmt", 
           "所属板块": "data_field",
           "数据量": "length", 
        }

class CmtDB_Index(object):
    def __init__(self):
        self.included_cmt_dict = included_cmt_dict
        self.file_path = "../../CommodityDataBase/Commodities/"
        self.field_list = included_cmt_dict.keys()
        self.cmt_list = []
        for field, cmt_list in self.included_cmt_dict.items():
            self.cmt_list.extend(cmt_list)
    

    
    ###########################################################################
    # 提取
    
    def get_total_index_table(self):
        session = sessionmaker()
        session.configure(bind=engine)
        s = session()
        try:                       
            tmp_query = s.query(SQL_CMTDB_Index)
            tmp_df = pd.read_sql(tmp_query.statement, engine)
        except Exception as e:
            print(repr(e))
            s.rollback()
            raise e
        finally:
            s.close()
        return tmp_df

    def get_wind_index_df(self, cmt):
        session = sessionmaker()
        session.configure(bind=engine)
        s = session()
        try:                       
            tmp_query = s.query(SQL_CMTDB_Index).filter(and_(SQL_CMTDB_Index.data_cmt==cmt, SQL_CMTDB_Index.data_type=="万得数据"))
            tmp_df = pd.read_sql(tmp_query.statement, engine)
        except Exception as e:
            print(repr(e))
            s.rollback()
            raise e
        finally:
            s.close()
        return tmp_df

    def get_computed_index_df(self, cmt):
        session = sessionmaker()
        session.configure(bind=engine)
        s = session()
        try:                       
            tmp_query = s.query(SQL_CMTDB_Index).filter(and_(SQL_CMTDB_Index.data_cmt==cmt, SQL_CMTDB_Index.data_type=="计算衍生数据"))
            tmp_df = pd.read_sql(tmp_query.statement, engine)
        except Exception as e:
            print(repr(e))
            s.rollback()
            raise e
        finally:
            s.close()
        return tmp_df
    
    def get_all_db_cmt_list(self):
        session = sessionmaker()
        session.configure(bind=engine)
        s = session()
        try:                       
            tmp_query = s.query(SQL_CMTDB_Index.data_cmt)
            tmp_df = pd.read_sql(tmp_query.statement, engine)
        except Exception as e:
            print(repr(e))
            s.rollback()
            raise e
        finally:
            s.close()
        return tmp_df.iloc[:, 0].unique().tolist()
        
    def get_col_class_table_name(self, col, cmt):
        index_df = self.get_total_index_table()
        if col in index_df["data_name"].values.tolist():
            tmp_ts = index_df[(index_df["data_cmt"]==cmt) & (index_df["data_name"]==col)]
            tmp_class_name = tmp_ts["class_name"].iloc[0]
            tmp_table_name = tmp_ts["table_name"].iloc[0]
            return tmp_class_name, tmp_table_name
        else:
            print("无此数据：" + col)
            return None, None
    
    def save_index_table_for_cmt(self, cmt, path):
        total_df = self.get_total_index_table()
        tmp_df = total_df[total_df["data_cmt"]==cmt].copy()
        if len(tmp_df) == 0:
            print("商品数据库无'%s'索引" % cmt)
            return False
        else:
            tmp_df = tmp_df.rename(columns=dict(zip(field_dict.values(), field_dict.keys())))
            tmp_df = tmp_df.set_index("数据名称")
            tmp_df = tmp_df.drop("table_name", axis=1)
            tmp_df = tmp_df.sort_values(by=["数据大类", "数据小类", "数据类型", "数据名称"], ascending=[False, True, True, True])
            tmp_df.to_excel(path, encoding="gbk")
            return True 

    
    def index_df_sort(self, df):
        tmp_df = df.copy()
        tmp_df["data_field"] = tmp_df["data_field"].astype("category")
        tmp_df['data_field'].cat.set_categories(list(self.field_list), inplace=True)
        tmp_df["data_cmt"] = tmp_df["data_cmt"].astype("category")
        tmp_df['data_cmt'].cat.set_categories(list(self.cmt_list), inplace=True)
        tmp_df = tmp_df.sort_values(by=["data_field", "data_cmt", "data_table", "data_category", "data_type", "data_name"],
                                ascending=[True, True, False, True, True, True])
        return tmp_df

    def get_index_tree_dict(self):
        df = self.get_total_index_table()          
        df_sorted = self.index_df_sort(df)
        df_translated = self.translate_index_df_cmt_to_chinese(df_sorted)
        return df_translated


    # 本地生成汇总table
    def generate_all_cmt_col_index_local_df(self):
        tmp_df_list = []
        for field, cmt_list in self.included_cmt_dict.items():
            for cmt in cmt_list:
                tmp_df = pd.read_excel(self.file_path + cmt + "/files/col_index.xlsx", encoding="gbk",
                                       dtype={"更新至": datetime, "更新日期": datetime, "起始": datetime})
                tmp_table_df = pd.read_excel(self.file_path + cmt + "/files/table_index.xlsx", encoding="gbk")
                tmp_df = tmp_df.join(tmp_table_df.set_index("table"), on="数据大类")
                tmp_col_list = tmp_df.columns
                tmp_new_col = []
                for x in field_dict.keys():
                    if x in tmp_col_list:
                        tmp_new_col.append(x)
                    
                tmp_df = tmp_df[tmp_new_col]
                tmp_df.columns = [field_dict[x] for x in tmp_df.columns]
                tmp_df["data_field"] = field
                tmp_df["data_cmt"] = cmt
                tmp_df_list.append(tmp_df)
        total_df = pd.concat(tmp_df_list, sort=False)
        return total_df
    
        
    def translate_index_df_cmt_to_chinese(self, df):
        tmp_df = df.copy()
        cmt_file = Cmt_Data.get_cmt_profile()
        tmp_df["data_cmt"] = tmp_df["data_cmt"].apply(lambda x: Cmt_Data(x, cmt_file).chinese_name)        
        return tmp_df
    
    ############################################################################
    # 修改编辑
        
    @staticmethod
    def type_translate(ts):
        if "length" in ts.index:
            ts["length"] = int(ts["length"])  
        if "start_date" in ts.index:
            ts["start_date"] = ts["start_date"].to_pydatetime()
        if "last_date" in ts.index:
            ts["last_date"] = ts["last_date"].to_pydatetime()
        if "update_date" in ts.index:
            ts["update_date"] = ts["update_date"].to_pydatetime()
        return ts
    
    @staticmethod
    def update_sql_cmtdb_index_table_from_local():
        print(u"开始新建商品数据库索引列表")
        all_cnt_df = CmtDB_Index().generate_all_cmt_col_index_local_df()
        
        session = sessionmaker()
        session.configure(bind=engine)
        s = session()
        try:
            SQL_CMTDB_Index.__table__.drop(engine)
            SQL_CMTDB_Index.__table__.create(engine)
            for i in range(len(all_cnt_df)):
                tmp_ts = all_cnt_df.iloc[i,:].copy().dropna()
                tmp_ts = CmtDB_Index.type_translate(tmp_ts)
                record = SQL_CMTDB_Index(**dict(tmp_ts))
                s.add(record) #Add all the records    
            s.commit() #Attempt to commit all the records
        except Exception as e:
            print(repr(e))
            s.rollback() #Rollback the changes on error
        finally:
            s.close() #Close the connection
        print(u"全部商品数据库索引列表新建完毕")
        return

    @staticmethod
    def update_sql_cmtdb_condition(update_condition_df):
#        print(u"开始新建商品数据库索引列表")        
        session = sessionmaker()
        session.configure(bind=engine)
        s = session()
        try:
            for i in range(len(update_condition_df)):
                tmp_ts = update_condition_df.iloc[i,:].copy().dropna()
                tmp_ts = CmtDB_Index.type_translate(tmp_ts)
                tmp_query = s.query(SQL_CMTDB_Index).filter(and_(SQL_CMTDB_Index.data_cmt==tmp_ts["cmt"], SQL_CMTDB_Index.data_name==tmp_ts["col"]))
                tmp_df = pd.read_sql(tmp_query.statement, engine)
                if len(tmp_df) == 0:
                    print(tmp_ts["cmt"] + ": " + tmp_ts["col"] + " 指标名无匹配")
                tmp_query.update(dict(tmp_ts.drop(["cmt", "col"])))
            s.commit() #Attempt to commit all the records
        except Exception as e:
            print(repr(e))
            s.rollback() #Rollback the changes on error
        finally:
            s.close() #Close the connection
#        print(u"全部商品数据库索引列表新建完毕")
        return    
    
if __name__ == "__main__":
    c = CmtDB_Index()
    
#    df = c.get_all_cmt_col_index_local_df()
    
    CmtDB_Index.construct_sql_cmtdb_index_table()
     

#    df = c.get_total_index_table_from_sql()          
#    df_sorted = c.index_df_sort(df)
#    df_translated = c.translate_index_df_cmt_to_chinese(df_sorted)
#
#    for a, field_group in df_translated.groupby(by=["data_field", "data_cmt", "data_table", "data_category"], sort=False):
#        pass
#        for cmt, cmt_field in df_translated.groupby("data_cmt"):
#            for table, table_field in df_translated.groupby("data_cmt"):











