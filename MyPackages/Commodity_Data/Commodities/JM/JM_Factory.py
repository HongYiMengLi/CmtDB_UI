# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 16:13:28 2018

@author: 李弘一萌
"""

import pandas as pd
from .JM_Base import JM_Base
from . import JM_SpotPrice, JM_FuturesPrice, JM_Downstream
from . import JM_Inventory, JM_Spread, JM_SupplyDemandBalance
#from sqlalchemy.orm import sessionmaker
#from sqlalchemy import and_



class JM_Factory(object):
    @staticmethod
    def getobj(col):
        class_name, table_module_name = JM_Base.get_col_class_table(col)
        tmp_obj = eval(table_module_name + "." + class_name)()
        return tmp_obj

    @staticmethod
    def getBaseObj():
        return JM_Base()
        
if __name__ == "__main__":
    col_list = [u"PP拉丝价格_华东"]
    col = u"PP拉丝价格_华东"
    a = JM_Factory().getobj(col)
    print(a.col_name)
#    bbb = a.get_ts()