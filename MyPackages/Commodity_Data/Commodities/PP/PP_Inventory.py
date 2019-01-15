# -*- coding: utf-8 -*-
"""
Created on Wed Aug 29 13:15:30 2018

@author: Administrator
"""

import pandas as pd
from datetime import datetime
from .PP_Base import PP_Base
from ..L import L_Inventory
from ...Base.DataType_Base import Manual, Computed, WindData
from ...Base.Plot_Base import Plot_Base
from matplotlib.ticker import FuncFormatter

class inventory_base(PP_Base, Plot_Base):
    table_english_name = "Inventory"
    table_chinese_name = u"库存"
    
    def output(self):
        print("Inventory")
    
    def get_relevant_df(self, col_list):
        local_col_name_list = inventory_base.get_all_table_classname()
        col_cls_list = []
        for x in col_list:
            col_cls_name = str(PP_Base.get_class_name(x))
            if col_cls_name not in local_col_name_list:
                col_cls_list.append(eval(PP_Base.get_table_class_full_variable(x)))
            else:
                col_cls_list.append(eval(col_cls_name))
        ts_list = [x().get_ts() for x in col_cls_list]
        tmp_table_df = pd.concat(ts_list, axis=1).dropna(how="all")
        return tmp_table_df 
    
    
################################################################################################################################    
""" 石化库存 """
""" 计算指标 """

class ZhongShiHua(inventory_base, Computed):
    field_name = u"石化库存"
    col_name = u"石化库存_中石化"
    def get_ts(self):
        tmp_ts = L_Inventory.ZhongShiHua().get_ts()
        return tmp_ts
    
class ZhongShiYou(inventory_base, Computed):
    field_name = u"石化库存"
    col_name = u"石化库存_中石油"
    def get_ts(self):
        tmp_ts = L_Inventory.ZhongShiYou().get_ts()
        return tmp_ts
    
class ShiHuaZongKuCun(inventory_base, Computed):
    field_name = u"石化库存"
    col_name = u"石化库存_总库存"
    def get_ts(self):
        tmp_ts = L_Inventory.ShiHuaZongKuCun().get_ts()
        return tmp_ts
    
################################################################################################################################    
""" 社会库存 """    
""" 计算指标 """

class PPSheHuiKuCun(inventory_base, Computed):
    field_name = u"社会库存"
    col_name = u"PP社会库存"
    axhline = 0
    start_year = 2016
    def get_ts_whole_progress(self):
        relevant_col_list = [u"石化库存_总库存", u"PP库存_煤化工", u"PP库存_港口"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = 0.372616925610075 * tmp_total[u"石化库存_总库存"] + tmp_total[u"PP库存_煤化工"] / 10000 + tmp_total[u"PP库存_港口"]
        return tmp_total

################################################################################################################################    
""" 煤化工库存 """

class MeiHuaGongPP(inventory_base, Manual):
    field_name = u"煤化工库存"
    col_name = u"PP库存_煤化工"

################################################################################################################################    
""" 港口库存 """

class PPGangKouKuCun(inventory_base, Manual):
    field_name = u"港口库存"
    col_name = u"PP库存_港口"
    axhline = 0
    start_year = 2016

################################################################################################################################
    
if __name__ == "__main__":
    aaa = PPSheHuiKuCun().get_ts()







