# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 16:13:28 2018

@author: 李弘一萌
"""

import pandas as pd
from .OI_Base import OI_Base
from . import OI_SpotPrice, OI_Upstream
from . import OI_Inventory, OI_Spread, OI_SupplyDemandBalance, OI_FuturesPrice
#from sqlalchemy.orm import sessionmaker
#from sqlalchemy import and_



class OI_Factory(object):
    @staticmethod
    def getobj(col):
        class_name, table_module_name = OI_Base.get_col_class_table(col)
        tmp_obj = eval(table_module_name + "." + class_name)()
        return tmp_obj

    @staticmethod
    def getBaseObj():
        return OI_Base()
        
if __name__ == "__main__":
    col_list = [u"PP拉丝价格_华东"]
    col = u"PP拉丝价格_华东"
    a = OI_Factory().getobj(col)
    print(a.col_name)
#    bbb = a.get_ts()