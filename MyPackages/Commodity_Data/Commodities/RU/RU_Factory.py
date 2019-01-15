# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 16:13:28 2018

@author: 李弘一萌
"""

import pandas as pd
from .RU_Base import RU_Base
from . import RU_SpotPrice, RU_Macro, RU_Upstream, RU_Downstream
from . import RU_Inventory, RU_Spread, RU_FuturesPrice
#from sqlalchemy.orm import sessionmaker
#from sqlalchemy import and_



class RU_Factory(object):
    @staticmethod
    def getobj(col):
        class_name, table_module_name = RU_Base.get_col_class_table(col)
        tmp_obj = eval(table_module_name + "." + class_name)()
        return tmp_obj

    @staticmethod
    def getBaseObj():
        return RU_Base()
        
if __name__ == "__main__":
    col_list = [u"PP拉丝价格_华东"]
    col = u"PP拉丝价格_华东"
    a = RU_Factory().getobj(col)
    print(a.col_name)
#    bbb = a.get_ts()