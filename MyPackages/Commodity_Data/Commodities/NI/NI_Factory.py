# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 16:13:28 2018

@author: 李弘一萌
"""

import pandas as pd
from .NI_Base import NI_Base
from . import NI_SpotPrice, NI_Upstream, NI_Downstream, NI_Macro, NI_Others
from . import NI_Inventory, NI_Spread, NI_SupplyDemandBalance, NI_FuturesPrice
#from sqlalchemy.orm import sessionmaker
#from sqlalchemy import and_



class NI_Factory(object):
    @staticmethod
    def getobj(col):
        class_name, table_module_name = NI_Base.get_col_class_table(col)
        tmp_obj = eval(table_module_name + "." + class_name)()
        return tmp_obj

    @staticmethod
    def getBaseObj():
        return NI_Base()
        
if __name__ == "__main__":
    col_list = [u"PP拉丝价格_华东"]
    col = u"PP拉丝价格_华东"
    a = NI_Factory().getobj(col)
    print(a.col_name)
#    bbb = a.get_ts()