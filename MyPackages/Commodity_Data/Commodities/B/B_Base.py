# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 16:12:24 2018

@author: 李弘一萌
"""


import pandas as pd

from MyFutureClass.CmtDataBase.Base.CommonDataBaseClass import CommonDataBaseClass
from MyFutureClass.CmtDataBase.Base.CmtDB_Data_Path import CmtDB_Data_Path
from MyFutureClass.Data.QuoteData import QuoteData
from MyFutureClass.Contract.FuturesContract import Contracts
from MyFutureClass.SQL.SQL_Connection import SQL_Connection


data_path = CmtDB_Data_Path.relative_local_db_path()

class B_Base(CommonDataBaseClass):
    cmt_name = "B"
    db_name = "cmt_db_" + cmt_name.lower()
    relative_data_path = data_path + cmt_name + "/"   
    engine = SQL_Connection.get_connection(db_name, charset="utf8")
    
    @staticmethod
    def get_B_quote_df(month=None):
        tmp_df = QuoteData.Daily.sql_get_cmt_daily_quote("B.DCE", "close")
        if month is not None:
            cnt_obj_list = [Contracts(x) for x in tmp_df.columns]
            month_cnt_list = [x.cnt_code for x in cnt_obj_list if int(x.cnt_month) == month]
            tmp_df = tmp_df[month_cnt_list]
        return tmp_df

    @staticmethod
    def get_B_main_month_quote_df():
        main_month_list = [1, 5, 9]
        tmp_df = QuoteData.Daily.sql_get_cmt_daily_quote("B.DCE", "close")
        cnt_obj_list = [Contracts(x) for x in tmp_df.columns]
        month_cnt_list = [x.cnt_code for x in cnt_obj_list if int(x.cnt_month) in main_month_list]
        tmp_df = tmp_df[month_cnt_list]
        return tmp_df
    
if __name__ == "__main__":
    aa = B_Base.get_col_index_df()