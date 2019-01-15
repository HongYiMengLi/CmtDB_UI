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

class NI_Base(CommonDataBaseClass):
    cmt_name = "NI"
    db_name = "cmt_db_" + cmt_name.lower()
    relative_data_path = data_path + cmt_name + "/"   
    engine = SQL_Connection.get_connection(db_name, charset="utf8")
    
    @staticmethod
    def get_NI_quote_df(month=None):
        tmp_df = QuoteData.Daily.get_cmt_quote("close", "NI.SHF", month=month)
        return tmp_df


    
if __name__ == "__main__":
    aa = NI_Base.get_col_index_df()