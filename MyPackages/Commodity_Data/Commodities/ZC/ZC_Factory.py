# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 16:13:28 2018

@author: 李弘一萌
"""

import pandas as pd
from .ZC_Base import ZC_Base
from . import ZC_SpotPrice, ZC_Midstream, ZC_Downstream, ZC_Spread, ZC_FuturesPrice
#from sqlalchemy.orm import sessionmaker
#from sqlalchemy import and_



class ZC_Factory(object):
    @staticmethod
    def getobj(col):
        class_name, table_module_name = ZC_Base.get_col_class_table(col)
        tmp_obj = eval(table_module_name + "." + class_name)()
        return tmp_obj

    @staticmethod
    def getBaseObj():
        return ZC_Base()
        
if __name__ == "__main__":
    col_list = [u"PP拉丝价格_华东"]
    col = u"PP拉丝价格_华东"
    a = ZC_Factory().getobj(col)
    print(a.col_name)
#    bbb = a.get_ts()