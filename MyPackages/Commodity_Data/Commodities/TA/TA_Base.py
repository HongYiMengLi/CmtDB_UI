# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 16:12:24 2018

@author: 李弘一萌
"""


import pandas as pd
from ...Base.CommonDataBaseClass import CommonDataBaseClass
from ...Base.CmtDB_Data_Path import CmtDB_Data_Path
from ....Futures_Data.Quote.QuoteData import QuoteData
from ....SQL.SQL_Connection import SQL_Connection


data_path = CmtDB_Data_Path.relative_local_db_path()

class TA_Base(CommonDataBaseClass):
    cmt_name = "TA"
    db_name = "cmt_db_" + cmt_name.lower()
    relative_data_path = data_path + cmt_name + "/"   
    engine = SQL_Connection.get_connection(db_name, charset="utf8")
    
    @staticmethod
    def get_TA_quote_df(month=None):
        tmp_df = QuoteData.Daily.get_cmt_quote("close", "TA.CZC", month=month)
        return tmp_df

    @staticmethod
    def get_TA_main_month_quote_df():
        main_month_list = [1, 5, 9]
        df_list = []
        for x in main_month_list:
            tmp_df = QuoteData.Daily.get_cmt_quote("close", "TA.CZC", month=x)
            df_list.append(tmp_df)
        total_df = pd.concat(df_list, axis=1, sort=False)
        return total_df
    
if __name__ == "__main__":
    
    tmp_total_ts_list = []
    for m in [1,3,5,7,9,11]:
        aa = TA_Base.get_TA_quote_df(m)
        tmp_ts_list = []
        for x in aa.columns.tolist():
            tmp_ts = aa[x].dropna()
            tmp_ts_list.append(tmp_ts)
        tmp_total_ts = pd.concat(tmp_ts_list, sort=False)
        tmp_total_ts.name = m
        tmp_total_ts_list.append(tmp_total_ts)
    total_df = pd.concat(tmp_total_ts_list, axis=1, sort=False)
            
            
            
            