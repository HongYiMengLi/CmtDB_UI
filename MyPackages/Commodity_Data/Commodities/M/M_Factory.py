# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 16:13:28 2018

@author: 李弘一萌
"""

import pandas as pd
from .M_Base import M_Base
from . import M_SpotPrice, M_Upstream, M_Downstream
from . import M_Inventory, M_Spread, M_SupplyDemandBalance, M_FuturesPrice
#from sqlalchemy.orm import sessionmaker
#from sqlalchemy import and_



class M_Factory(object):
    @staticmethod
    def getobj(col):
        class_name, table_module_name = M_Base.get_col_class_table(col)
        tmp_obj = eval(table_module_name + "." + class_name)()
        return tmp_obj


    @staticmethod
    def getBaseObj():
        return M_Base()   
     
if __name__ == "__main__":
    col_list = [u"PP拉丝价格_华东"]
    col = u"PP拉丝价格_华东"
    a = M_Factory().getobj(col)
    print(a.col_name)
#    bbb = a.get_ts()