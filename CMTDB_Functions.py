# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 12:48:50 2019

@author: 李弘一萌
"""

import pandas as pd

import sys
if "..\.." not in sys.path:
    sys.path.append("..\..")
import pandas as pd
from datetime import datetime
from MyPackages.Futures_Data.Profile.CmtData import Cmt_Data
from MyPackages.Futures_Data.Profile.CntData import Cnt_Data
from MyPackages.Futures_Data.DateTime.Trade_Date import Trade_Date
from MyPackages.Futures_Data.Quote.QuoteData import QuoteData
from MyPackages.Futures_Data.Main_Cnt.MainCnt import Main_Cnt
from MyPackages.Commodity_Data.IndexTable import CmtDB_Index
from MyPackages.Commodity_Data.Commodities.BU.BU_Base import BU_Base
from MyPackages.Commodity_Data.Commodities.L.L_Device import total_device, product_license, field_list, L_Device_Process
#from MyPackages.Commodity_Data.Commodities.BU.BU_Factory import BU_Factory
#from MyPackages.Commodity_Data.Commodities.AL.AL_Factory import AL_Factory
from MyPackages.Commodity_Data.Global_Factory import Global_Factory
from MyPackages.Commodity_Data.APP_Base.Update_Base import CMTDB_Update

def update_all_cmt_start_last_length():
    cmt_list = CmtDB_Index().get_all_db_cmt_list()
    for cmt in cmt_list:
        if cmt not in ["A", "B", "M", "OI", "P", "Y", "SR"]:
            print("开始更新" + cmt)
            CMTDB_Update(cmt).update_start_last_date_length()
            print(cmt + " index列表更新完毕")
#        try:
#            CMTDB_Update(cmt).update_start_last_date_length()
#            print(cmt + "index列表更新完毕")
#        except Exception as e:
#            print(cmt + repr(e))


if __name__ == "__main__":
    update_all_cmt_start_last_length()
            
    