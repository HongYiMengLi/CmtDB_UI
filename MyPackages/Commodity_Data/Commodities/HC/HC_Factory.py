# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 16:13:28 2018

@author: 李弘一萌
"""

import pandas as pd
from .HC_Base import HC_Base
from . import HC_SpotPrice, HC_Macro, HC_Upstream, HC_Downstream
from . import HC_Inventory, HC_Spread, HC_SupplyDemandBalance, HC_FuturesPrice
#from sqlalchemy.orm import sessionmaker
#from sqlalchemy import and_



class HC_Factory(object):
    @staticmethod
    def getobj(col):
        class_name, table_module_name = HC_Base.get_col_class_table(col)
        tmp_obj = eval(table_module_name + "." + class_name)()
        return tmp_obj

    @staticmethod
    def getBaseObj():
        return HC_Base()
        
if __name__ == "__main__":
    col_list = [u"PP拉丝价格_华东"]
    col = u"PP拉丝价格_华东"
    a = HC_Factory().getobj(col)
    print(a.col_name)
#    bbb = a.get_ts()