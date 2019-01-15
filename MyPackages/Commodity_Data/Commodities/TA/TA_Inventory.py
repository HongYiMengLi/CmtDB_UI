# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 10:47:54 2018

@author: 李弘一萌
"""

import pandas as pd
from datetime import datetime
from .TA_Base import TA_Base
from ...Base.DataType_Base import Manual, Computed, WindData
from ...Base.Plot_Base import Plot_Base
from matplotlib.ticker import FuncFormatter

class inventory_base(TA_Base, Plot_Base):
    table_english_name = "Inventory"
    table_chinese_name = u"库存"
    
    def output(self):
        print("Inventory")
    
    def get_relevant_df(self, col_list):
        local_col_name_list = inventory_base.get_all_table_classname()
        col_cls_list = []
        for x in col_list:
            col_cls_name = str(TA_Base.get_class_name(x))
            if col_cls_name not in local_col_name_list:
                col_cls_list.append(eval(TA_Base.get_table_class_full_variable(x)))
            else:
                col_cls_list.append(eval(col_cls_name))
        ts_list = [x().get_ts() for x in col_cls_list]
        tmp_table_df = pd.concat(ts_list, axis=1).dropna(how="all")
        return tmp_table_df 

###########################################################################################################################
""" 库存天数 """    

class PTAGongChangKuCunTianShu(inventory_base, WindData):
    field_name = u"库存天数"
    col_name = u"PTA工厂库存天数"
    wind_code = "S5446169"
    
class ChangSiPOYKuCunTianShu(inventory_base, WindData):
    field_name = u"库存天数"
    col_name = u"长丝POY库存天数"
    wind_code = "S5428996"
    start_year = 2013

class ChangSiDTYKuCunTianShu(inventory_base, WindData):
    field_name = u"库存天数"
    col_name = u"长丝DTY库存天数"
    wind_code = "S5428995"

class ChangSiFDYKuCunTianShu(inventory_base, WindData):
    field_name = u"库存天数"
    col_name = u"长丝FDY库存天数"
    wind_code = "S5428994"

class DuanXianKuCunTianShu(inventory_base, WindData):
    field_name = u"库存天数"
    col_name = u"短纤库存天数"
    wind_code = "S5448962"    
    
###########################################################################################################################
""" 仓单 """    

class PTACangDanShuLiang(inventory_base, WindData):
    field_name = u"仓单"
    col_name = u"PTA仓单数量"    
    wind_code = "S0049499" 

    
###########################################################################################################################
""" 有效预报 """    

class PTAYouXiaoYuBao(inventory_base, WindData):
    field_name = u"有效预报"
    col_name = u"PTA有效预报"    
    wind_code = "S0049521"     
    
if __name__ == "__main__":
    ts = DuanXianKuCunTianShu().get_ts()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    