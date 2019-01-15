# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 16:13:28 2018

@author: 李弘一萌
"""

import pandas as pd
from .P_Base import P_Base
from . import P_SpotPrice, P_Upstream
from . import P_Inventory, P_Spread, P_SupplyDemandBalance, P_FuturesPrice




class P_Factory(object):
    @staticmethod
    def getobj(col):
        class_name, table_module_name = P_Base.get_col_class_table(col)
        tmp_obj = eval(table_module_name + "." + class_name)()
        return tmp_obj

    @staticmethod
    def getBaseObj():
        return P_Base()
        
if __name__ == "__main__":
    col_list = [u"PP拉丝价格_华东"]
    col = u"PP拉丝价格_华东"
    a = P_Factory().getobj(col)
    print(a.col_name)
#    bbb = a.get_ts()