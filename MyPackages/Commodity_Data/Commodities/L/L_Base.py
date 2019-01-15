# -*- coding: utf-8 -*-
"""
Created on Thu Aug 16 16:23:17 2018

@author: 李弘一萌
"""

import pandas as pd
from ...Base.CommonDataBaseClass import CommonDataBaseClass
from ...Base.CmtDB_Data_Path import CmtDB_Data_Path
from ....Futures_Data.Quote.QuoteData import QuoteData
from ....SQL.SQL_Connection import SQL_Connection


data_path = CmtDB_Data_Path.relative_local_db_path()

class L_Base(CommonDataBaseClass):
    cmt_name = "L"
    db_name = "cmt_db_" + cmt_name.lower()
    relative_data_path = data_path + cmt_name + "/"   
    engine = SQL_Connection.get_connection(db_name, charset="utf8")
    
    @staticmethod
    def get_L_quote_df(month=None):
        tmp_df = QuoteData.Daily.get_cmt_quote("close", "L.DCE", month=month)
        return tmp_df

    @staticmethod
    def get_L_main_month_quote_df():
        main_month_list = [1, 5, 9]
        df_list = []
        for x in main_month_list:
            tmp_df = QuoteData.Daily.get_cmt_quote("close", "L.DCE", month=x)
            df_list.append(tmp_df)
        total_df = pd.concat(df_list, axis=1, sort=False)
        return total_df
    
if __name__ == "__main__":
    df = L_Base.get_L_main_month_quote_df()