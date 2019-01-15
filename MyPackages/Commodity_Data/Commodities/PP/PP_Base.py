# -*- coding: utf-8 -*-
"""
Created on Wed Aug 29 09:20:23 2018

@author: Administrator
"""

import pandas as pd
from ...Base.CommonDataBaseClass import CommonDataBaseClass
from ...Base.CmtDB_Data_Path import CmtDB_Data_Path
from ....Futures_Data.Quote.QuoteData import QuoteData
from ....SQL.SQL_Connection import SQL_Connection


data_path = CmtDB_Data_Path.relative_local_db_path()

class PP_Base(CommonDataBaseClass):
    cmt_name = "PP"
    db_name = "cmt_db_" + cmt_name.lower()
    relative_data_path = data_path + cmt_name + "/"   
    engine = SQL_Connection.get_connection(db_name, charset="utf8")
    
    @staticmethod
    def get_PP_quote_df(month=None):
        tmp_df = QuoteData.Daily.get_cmt_quote("close", "PP.DCE", month=month)
        return tmp_df

    @staticmethod
    def get_PP_main_month_quote_df():
        main_month_list = [1, 5, 9]
        df_list = []
        for x in main_month_list:
            tmp_df = QuoteData.Daily.get_cmt_quote("close", "PP.DCE", month=x)
            df_list.append(tmp_df)
        total_df = pd.concat(df_list, axis=1, sort=False)
        return total_df
    
if __name__ == "__main__":
    aa = PP_Base.get_col_index_df()