# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 16:13:28 2018

@author: 李弘一萌
"""

import pandas as pd
from .TA_Base import TA_Base
from . import TA_SpotPrice, TA_Macro, TA_Upstream, TA_Downstream
from . import TA_Inventory, TA_Spread, TA_SupplyDemandBalance, TA_FuturesPrice
#from sqlalchemy.orm import sessionmaker
#from sqlalchemy import and_



class TA_Factory(object):
    @staticmethod
    def getobj(col):
        class_name, table_module_name = TA_Base.get_col_class_table(col)
        tmp_obj = eval(table_module_name + "." + class_name)()
        return tmp_obj

    @staticmethod
    def getBaseObj():
        return TA_Base()
        
if __name__ == "__main__":
    col_list = [u"PP拉丝价格_华东"]
    col = u"PP拉丝价格_华东"
    a = TA_Factory().getobj(col)
    print(a.col_name)
#    bbb = a.get_ts()