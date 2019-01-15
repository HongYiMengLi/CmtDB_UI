# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 16:13:28 2018

@author: 李弘一萌
"""

import pandas as pd
from .CF_Base import CF_Base
from . import CF_SpotPrice, CF_Upstream, CF_Downstream
from . import CF_Inventory, CF_Spread, CF_SupplyDemandBalance, CF_FuturesPrice
#from sqlalchemy.orm import sessionmaker
#from sqlalchemy import and_



class CF_Factory(object):
    @staticmethod
    def getobj(col):
        class_name, table_module_name = CF_Base.get_col_class_table(col)
        tmp_obj = eval(table_module_name + "." + class_name)()
        return tmp_obj

    @staticmethod
    def getBaseObj():
        return CF_Base()
        
if __name__ == "__main__":
    col_list = [u"PP拉丝价格_华东"]
    col = u"PP拉丝价格_华东"
    a = CF_Factory().getobj(col)
    print(a.col_name)
#    bbb = a.get_ts()