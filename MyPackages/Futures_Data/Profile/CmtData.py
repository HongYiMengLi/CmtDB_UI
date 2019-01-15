# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 13:40:47 2018

@author: Administrator
"""

import pandas as pd
import numpy as np
from datetime import datetime, date
from ...Data_Path.data_path import Data_Path
from ...SQL.Table_Create import sql_cmt_profile
from sqlalchemy.orm import sessionmaker


# 获取cmt字典
def get_cmtname_exch_dict(cmt_profile):
    tmp_cmt_df = cmt_profile
    futures_cmt_code_list = tmp_cmt_df.index.tolist()
    futures_cmt_name_list = [s[:-4] for s in futures_cmt_code_list]        
    exchange_list = [s[-3:] for s in futures_cmt_code_list]
    futures_dict = dict(zip(futures_cmt_name_list, exchange_list))
    return futures_dict 
    
class Cmt_Data(object):
    relative_local_path = Data_Path.relative_local_db_path()
    class_name = "Cmt_Data"
    default_mode = "db" # "db": 从数据库提取; "local": 从本地提取


########################################################################################################################
# Cmt对象方法  

    # 构造函数
    def __init__(self, commodity_name, cmt_profile, mode=default_mode):        
        self.cmt_profile = self.get_cmt_profile(mode=mode)
        self.futures_dict = get_cmtname_exch_dict(cmt_profile)
        cmt_code = self.check_cmt_name(commodity_name)
        self._cmt_code = cmt_code
        self._profile = self.cmt_profile.loc[self._cmt_code,:].copy()        

    def check_cmt_name(self, commodity_name):
        if type(commodity_name) == str:
            commodity_name = str(commodity_name).upper()
            if commodity_name in self.cmt_profile.index:
                return str(commodity_name).upper()
            elif commodity_name in [s[:-4] for s in self.cmt_profile.index]:
                return commodity_name + "." + self.futures_dict[commodity_name]
            elif commodity_name in self.cmt_profile["chinese_name"].values.tolist():
                return self.cmt_profile[self.cmt_profile["chinese_name"]==commodity_name].index[0]
        raise Exception("No such Futures commodity: " + str(commodity_name))
        
    # getters and setters
    @property
    def cmt_code(self):
        return  self._cmt_code
    
    
    @property
    def exchange(self):
        return  self._cmt_code[-3:]
    
    @property
    def cmt_name(self):
        return self._cmt_code[:-4]
    
    @property
    def chinese_name(self):
        return self._profile["chinese_name"]

    @property
    def multiplier(self):
        return self._profile["multiplier"]

    @property
    def margin(self):
        return self._profile["margin"]

    @property
    def issue_date(self):
        return self._profile["issue_date"]

    @property
    def main_months(self):
        return self._profile["main_month"]

    @property
    def category(self):
        return self._profile["category"]

    @property
    def full_chinese_name(self):
        return self._profile["full_chinese_name"]

    @property
    def unit(self):
        return self._profile["price_unit"]

    @property
    def price_limit(self):
        return self._profile["price_limit"] / 100.0

    @property
    def min_price_chg(self):
        return self._profile["min_price_change"]

    @property
    def delivery_months(self):
        return self._profile["delivery_months"]

    @property
    def trade_hours(self):
        return self._profile["trade_hours"]

    @property
    def last_trade_date(self):
        return self._profile["last_trade_date"]
    
    #methods



    
########################################################################################################################
# 提取cmt数据   
   
    # 获取整个cmt_profile
    @staticmethod
    def get_cmt_profile(mode=default_mode, file_path=None):
        if mode == "local":
            if file_path is None:
                tmp_file_name = Cmt_Data.relative_local_path + "cmt_list\cmt_profile.csv" 
            else:
                tmp_file_name = file_path
            tmp_df = pd.read_csv(tmp_file_name, index_col=0, encoding="gbk")
        elif mode == "db":
            session = sessionmaker()
            session.configure(bind=sql_cmt_profile.engine)
            s = session()
            try:
                tmp = s.query(sql_cmt_profile.SQL_Cmt_Data)
                tmp_df = pd.read_sql(tmp.statement, sql_cmt_profile.engine, index_col="cmt")
            except Exception as e:
                print(e.message)
                raise
            finally:
                s.close()
        return tmp_df.dropna(how="all")
    
    # 获取cmt列表
    @staticmethod
    def get_cmt_list(mode=default_mode):
        tmp_cmt_df = Cmt_Data.get_cmt_profile(mode=mode)
        tmp_cmt_list = tmp_cmt_df.index.tolist()
        return tmp_cmt_list    


    
    # 获取某一cmt最小价格变动
    @staticmethod
    def get_cmt_min_price_unit(cmt, mode=default_mode):
        tmp_df = Cmt_Data.get_cmt_profile(mode=mode)
        return tmp_df.loc[cmt, "min_price_change"]
    
    # 获取某一交易所的cmt_profile
    @staticmethod
    def get_cmt_profile_given_exch(exch, mode=default_mode):
        tmp_cmt_df = Cmt_Data.get_cmt_profile(mode=mode)
        df = tmp_cmt_df[tmp_cmt_df["exchange"]==exch]
        return df
    
    # 获取某一中文名对应的品种代码
    @staticmethod
    def get_cmt_code_from_chinese(c_name, mode=default_mode):
        tmp_cmt_df = Cmt_Data.get_cmt_profile(mode=mode)
        df = tmp_cmt_df[tmp_cmt_df["chinese_name"]==c_name]
        if len(df) == 0:
            print("无此中文名对应的品种")
            return None
        else:
            return df.index[0]
    
    # 获取上市日期在某日之后的cmt_porfile
    @staticmethod
    def get_cmt_after_date(start_date, mode=default_mode):
        tmp_cmt_df = Cmt_Data.get_cmt_profile(mode=mode)
        df = tmp_cmt_df[tmp_cmt_df["issue_date"]>=start_date]
        return df
        
    # 获取自定义活跃品种的cmt_porfile
    @staticmethod
    def get_local_active_cmt_list(mode="db"):
        tmp_cmt_df = Cmt_Data.get_cmt_profile(mode=mode)
        tmp_cmt_list = tmp_cmt_df[tmp_cmt_df["active"]==1].index.tolist()
        return tmp_cmt_list  

########################################################################################################################
# 编辑或修改cmt数据   
    
    # 初始化local cmt profile
    @staticmethod
    def set_local(cmt_df, file_path=None):
        if file_path is None:
            tmp_file_name = Cmt_Data.relative_local_path + "cmt_list\cmt_profile.csv" 
        else:
            tmp_file_name = file_path
        cmt_df.to_csv(tmp_file_name, encoding="gbk")
        return 
    
    # 对local cmt profile添加active属性
    @staticmethod
    def add_local_active_cmt(active_file_path=None, profile_file_path=None):
        if active_file_path is None:            
            tmp_active_filename = Cmt_Data.relative_local_path + "cmt_list\cmt_daily_list.csv" 
        else:
            tmp_active_filename = active_file_path
        tmp_active_df = pd.read_csv(tmp_active_filename, index_col=0)
        tmp_cmt_profile = Cmt_Data.get_cmt_profile(mode="local")
        active_cnt_list = tmp_active_df.index.tolist()
        tmp_cmt_profile["active"] = 0
        tmp_cmt_profile.loc[active_cnt_list, "active"] = 1
        if profile_file_path is None:
            tmp_profile_name = Cmt_Data.relative_local_path + "cmt_list\cmt_profile.csv"
        else:
            tmp_profile_name = profile_file_path
        tmp_cmt_profile.to_csv(tmp_profile_name, encoding="gbk")
        return tmp_cmt_profile       
    
    # 上传sql前的类型转换操作
    @staticmethod
    def type_translate(ts):
        if "multiplier" in ts.index:
            ts["multiplier"] = int(ts["multiplier"])  
        if "active" in ts.index:
            ts["active"] = int(ts["active"])
        if "margin" in ts.index:
            ts["margin"] = int(ts["margin"])  
        if "price_limit" in ts.index:
            ts["price_limit"] = int(ts["price_limit"])  
        if "min_price_change" in ts.index:
            ts["min_price_change"] = int(ts["min_price_change"])              
        return ts
    
    # local cmt profile上传mysql数据库
    @staticmethod
    def upload_sql_cmt_profile():
        session = sessionmaker()
        session.configure(bind=sql_cmt_profile.engine)
        s = session()
        cmt_profile = Cmt_Data.get_cmt_profile(mode="local")
        cmt_profile.reset_index(inplace=True)
        try:    
            for i in range(len(cmt_profile)):
                tmp_ts = cmt_profile.iloc[i, :].copy()
                tmp_ts = Cmt_Data.type_translate(tmp_ts)
                record = sql_cmt_profile.SQL_Cmt_Data(**dict(tmp_ts))
                s.add(record) #Add all the records    
            s.commit() #Attempt to commit all the records
        except:
            print("Cmt Profile Upload Error")
            s.rollback() #Rollback the changes on error
        finally:
            s.close() #Close the connection
        return
    
    # 用新cmt profile替换数据库上的profile
    @staticmethod
    def replace_sql_cmt_profile(new_profile_df):
        col_dict = sql_cmt_profile.col_dict
        new_profile_df.reset_index(inplace=True)
        new_col = new_profile_df.columns.tolist()
        original_col = col_dict.keys()
        for item in new_col:
            if item not in original_col:
                raise Exception("wrong col")
        session = sessionmaker()
        session.configure(bind=sql_cmt_profile.engine)
        s = session()
        try:
            sql_cmt_profile.SQL_Cmt_Data.__table__.drop(sql_cmt_profile.engine)
            sql_cmt_profile.SQL_Cmt_Data.__table__.create(sql_cmt_profile.engine)
            for i in range(len(new_profile_df)):
                tmp_ts = new_profile_df.iloc[i, :].copy()
                tmp_ts = Cmt_Data.type_translate(tmp_ts)                
                record = sql_cmt_profile.SQL_Cmt_Data(**dict(tmp_ts))
                s.add(record) #Add all the records    
            s.commit() #Attempt to commit all the records
        except Exception as e:
            print(repr(e))
            s.rollback() #Rollback the changes on error
        finally:
            s.close() #Close the connection
        return       
    
    

    
#if __name__ == "__main__":
#    Cmt_Data.sql_upload_cmt_profile()
#    cmt_profile = Cmt_Data.get_local()
#    cmt_profile.loc["F",:] = ["F",1,1,"2018-7-10","1","1","1","1","1",1,1,"1","1","1","1",0]
#    Cmt_Data.set_local(cmt_profile)
#    Cmt_Data.sql_replace_cmt_profile(cmt_profile)
#    df = Cmt_Data.get_cmt_profile_given_exch("CZC")
#    a = Cmt_Data.get_cmt_min_price_unit("RB.SHF")
    
#    df = Cmt_Data.get_cmt_code_from_chinese("沪铜")
    
#    df = Cmt_Data.get_cmt_profile(mode="local")
    
#    df = Cmt_Data.get_cmt_after_date("2017-12-21")
    
    
    
    
    