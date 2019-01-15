# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 16:13:28 2018

@author: 李弘一萌
"""

import pandas as pd
from .BU_Base import BU_Base
from . import BU_SpotPrice, BU_FuturesPrice, BU_Macro, BU_Upstream, BU_Downstream
from . import BU_Inventory, BU_Spread, BU_SupplyDemandBalance




class BU_Factory(object):
    @staticmethod
    def getobj(col):
        class_name, table_module_name = BU_Base.get_col_class_table(col)
        tmp_obj = eval(table_module_name + "." + class_name)()
        return tmp_obj

    @staticmethod
    def getBaseObj():
        return BU_Base()
        
if __name__ == "__main__":
    col_list = [u"PP拉丝价格_华东"]
    col = u"PP拉丝价格_华东"
    a = BU_Factory().getobj(col)
    print(a.col_name)
#    bbb = a.get_ts()