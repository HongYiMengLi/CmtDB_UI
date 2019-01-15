# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 16:13:28 2018

@author: 李弘一萌
"""

import pandas as pd
from .SR_Base import SR_Base
from . import SR_SpotPrice, SR_Macro, SR_Upstream, SR_Downstream
from . import SR_Inventory, SR_Spread, SR_SupplyDemandBalance, SR_FuturesPrice
#from sqlalchemy.orm import sessionmaker
#from sqlalchemy import and_



class SR_Factory(object):
    @staticmethod
    def getobj(col):
        class_name, table_module_name = SR_Base.get_col_class_table(col)
        tmp_obj = eval(table_module_name + "." + class_name)()
        return tmp_obj

    @staticmethod
    def getBaseObj():
        return SR_Base()
        
if __name__ == "__main__":
    col_list = [u"PP拉丝价格_华东"]
    col = u"PP拉丝价格_华东"
    a = MA_Factory().getobj(col)
    print(a.col_name)
#    bbb = a.get_ts()