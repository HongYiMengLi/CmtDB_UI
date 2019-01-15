# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 16:13:28 2018

@author: 李弘一萌
"""

import pandas as pd
from .CU_Base import CU_Base
from . import CU_SpotPrice, CU_Upstream, CU_Downstream, CU_Macro, CU_Others
from . import CU_Inventory, CU_Spread, CU_SupplyDemandBalance, CU_FuturesPrice
#from sqlalchemy.orm import sessionmaker
#from sqlalchemy import and_



class CU_Factory(object):
    @staticmethod
    def getobj(col):
        class_name, table_module_name = CU_Base.get_col_class_table(col)
        tmp_obj = eval(table_module_name + "." + class_name)()
        return tmp_obj

    @staticmethod
    def getBaseObj():
        return CU_Base()
        
if __name__ == "__main__":
    col_list = [u"PP拉丝价格_华东"]
    col = u"PP拉丝价格_华东"
    a = CU_Factory().getobj(col)
    print(a.col_name)
#    bbb = a.get_ts()