# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 13:43:08 2018

@author: Administrator
"""

import pandas as pd
import numpy as np
import copy
from datetime import datetime, date, timedelta
from MyFutureClass.Data.Trade_Date import Trade_Date
from MyFutureClass.Data.data_path import Data_Path
from MyFutureClass.Data.CntData import Cnt_Data
from MyFutureClass.Commodity.FuturesCommodity import Futures
from MyFutureClass.Data.QuoteData import QuoteData
from MyFutureClass.SQL.Table_Create import sql_designed_main_cnt
from sqlalchemy.orm import sessionmaker


class DesignedMainCnt(object):
    relative_db_path = Data_Path.relative_local_db_path()
    designed_cnt1_filename = relative_db_path + "main_cnt/designed_main_cnt.xlsx"
    designed_cnt2_filename = relative_db_path + "main_cnt/designed_next_cnt.xlsx"
    designed_cnt3_filename = relative_db_path + "main_cnt/designed_next2_cnt.xlsx"
   
    @staticmethod
    def sql_get_main_cnt():
        session = sessionmaker()
        session.configure(bind=sql_designed_main_cnt.engine)
        s = session()
        class_variable = sql_designed_main_cnt.SQL_Designed_Main_Cnt_Data 
        try:
            tmp_query = s.query(class_variable.cmt, class_variable.date, class_variable.cnt_1)
            tmp_df = pd.read_sql(tmp_query.statement, sql_designed_main_cnt.engine, index_col=["date", "cmt"])
            tmp_df = tmp_df.unstack()
            tmp_df.columns = [Futures(x[1]).cmt_code for x in tmp_df.columns]
        except Exception as e:
            print(repr(e))
            s.rollback()
            raise e
        finally:
            s.close()            
        return tmp_df

    @staticmethod
    def sql_get_next_cnt():
        session = sessionmaker()
        session.configure(bind=sql_designed_main_cnt.engine)
        s = session()
        class_variable = sql_designed_main_cnt.SQL_Designed_Main_Cnt_Data 
        try:
            tmp_query = s.query(class_variable.cmt, class_variable.date, class_variable.cnt_2)
            tmp_df = pd.read_sql(tmp_query.statement, sql_designed_main_cnt.engine, index_col=["date", "cmt"])
            tmp_df = tmp_df.unstack()
            tmp_df.columns = [Futures(x[1]).cmt_code for x in tmp_df.columns]
        except Exception as e:
            print(repr(e))
            s.rollback()
            raise e
        finally:
            s.close()            
        return tmp_df

    @staticmethod
    def sql_get_next2_cnt():
        session = sessionmaker()
        session.configure(bind=sql_designed_main_cnt.engine)
        s = session()
        class_variable = sql_designed_main_cnt.SQL_Designed_Main_Cnt_Data 
        try:
            tmp_query = s.query(class_variable.cmt, class_variable.date, class_variable.cnt_3)
            tmp_df = pd.read_sql(tmp_query.statement, sql_designed_main_cnt.engine, index_col=["date", "cmt"])
            tmp_df = tmp_df.unstack()
            tmp_df.columns = [Futures(x[1]).cmt_code for x in tmp_df.columns]
        except Exception as e:
            print(repr(e))
            s.rollback()
            raise e
        finally:
            s.close()            
        return tmp_df
    
    @staticmethod
    def update_all_local_main_cnt_table():
        designed_main_cnt = DesignedMainCnt.sql_get_main_cnt()
        designed_next_cnt = DesignedMainCnt.sql_get_next_cnt()
        designed_next2_cnt = DesignedMainCnt.sql_get_next2_cnt()
        
        designed_main_cnt.to_excel(DesignedMainCnt.designed_cnt1_filename)
        designed_next_cnt.to_excel(DesignedMainCnt.designed_cnt2_filename)
        designed_next2_cnt.to_excel(DesignedMainCnt.designed_cnt3_filename)
        return
    
    @staticmethod
    def get_local_designed_main_cnt(index_type="datetime"):
        tmp_df = pd.read_excel(DesignedMainCnt.designed_cnt1_filename, index_col=0, parse_dates=[0])
        if index_type=="date":
            tmp_df.index = Trade_Date.timestamp2date(tmp_df.index)
        return tmp_df   
    
    @staticmethod
    def get_local_designed_next_cnt(index_type="datetime"):
        tmp_df = pd.read_excel(DesignedMainCnt.designed_cnt2_filename, index_col=0, parse_dates=[0])
        if index_type=="date":
            tmp_df.index = Trade_Date.timestamp2date(tmp_df.index)
        return tmp_df       
    
    @staticmethod
    def get_local_designed_next2_cnt(index_type="datetime"):
        tmp_df = pd.read_excel(DesignedMainCnt.designed_cnt3_filename, index_col=0, parse_dates=[0])
        if index_type=="date":
            tmp_df.index = Trade_Date.timestamp2date(tmp_df.index)
        return tmp_df       
    
    
    
if __name__ == "__main__":
    df = DesignedMainCnt.get_local_designed_main_cnt()
    
    
    
    
    
    
    
    
    
    
    
    