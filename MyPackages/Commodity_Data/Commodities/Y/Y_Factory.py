# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 16:13:28 2018

@author: 李弘一萌
"""

import pandas as pd
from .Y_Base import Y_Base
from . import Y_SpotPrice, Y_Upstream
from . import Y_Inventory, Y_Spread, Y_SupplyDemandBalance, Y_FuturesPrice
#from sqlalchemy.orm import sessionmaker
#from sqlalchemy import and_



class Y_Factory(object):
    @staticmethod
    def getobj(col):
        class_name, table_module_name = Y_Base.get_col_class_table(col)
        tmp_obj = eval(table_module_name + "." + class_name)()
        return tmp_obj

    @staticmethod
    def getBaseObj():
        return Y_Base()
        
if __name__ == "__main__":
    col_list = [u"PP拉丝价格_华东"]
    col = u"PP拉丝价格_华东"
    a = Y_Factory().getobj(col)
    print(a.col_name)
#    bbb = a.get_ts()