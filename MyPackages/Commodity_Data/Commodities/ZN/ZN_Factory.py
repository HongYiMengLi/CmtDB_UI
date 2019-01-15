# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 16:13:28 2018

@author: 李弘一萌
"""

import pandas as pd
from .ZN_Base import ZN_Base
from . import ZN_SpotPrice, ZN_Upstream, ZN_Downstream, ZN_Macro
from . import ZN_Inventory, ZN_Spread, ZN_SupplyDemandBalance, ZN_FuturesPrice
#from sqlalchemy.orm import sessionmaker
#from sqlalchemy import and_



class ZN_Factory(object):
    @staticmethod
    def getobj(col):
        class_name, table_module_name = ZN_Base.get_col_class_table(col)
        tmp_obj = eval(table_module_name + "." + class_name)()
        return tmp_obj

    @staticmethod
    def getBaseObj():
        return ZN_Base()
        
if __name__ == "__main__":
    col_list = [u"PP拉丝价格_华东"]
    col = u"PP拉丝价格_华东"
    a = ZN_Factory().getobj(col)
    print(a.col_name)
#    bbb = a.get_ts()