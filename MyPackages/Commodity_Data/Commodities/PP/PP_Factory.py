# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 09:12:04 2018

@author: Administrator
"""

import pandas as pd
from .PP_Base import PP_Base
from . import PP_SpotPrice, PP_FuturesPrice, PP_Macro, PP_Upstream, PP_Downstream
from . import PP_Inventory, PP_Spread, PP_Others, PP_SupplyDemandBalance
#from sqlalchemy.orm import sessionmaker
#from sqlalchemy import and_



class PP_Factory(object):
    @staticmethod
    def getobj(col):
        class_name, table_module_name = PP_Base.get_col_class_table(col)
        tmp_obj = eval(table_module_name + "." + class_name)()
        return tmp_obj

    @staticmethod
    def getBaseObj():
        return PP_Base()
        
if __name__ == "__main__":
    col_list = [u"PP拉丝价格_华东"]
    col = u"PP拉丝价格_华东"
    a = PP_Factory().getobj(col)
    print(a.col_name)
#    bbb = a.get_ts()