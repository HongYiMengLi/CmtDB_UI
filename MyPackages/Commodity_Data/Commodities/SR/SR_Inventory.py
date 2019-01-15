# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 10:47:54 2018

@author: 李弘一萌
"""

import pandas as pd
from datetime import datetime
from .SR_Base import SR_Base
from ...Base.DataType_Base import Manual, Computed, WindData
from ...Base.Plot_Base import Plot_Base
from matplotlib.ticker import FuncFormatter

class inventory_base(SR_Base, Plot_Base):
    table_english_name = "Inventory"
    table_chinese_name = u"库存"
    
    def output(self):
        print("Inventory")
    
    def get_relevant_df(self, col_list):
        local_col_name_list = inventory_base.get_all_table_classname()
        col_cls_list = []
        for x in col_list:
            col_cls_name = str(SR_Base.get_class_name(x))
            if col_cls_name not in local_col_name_list:
                col_cls_list.append(eval(SR_Base.get_table_class_full_variable(x)))
            else:
                col_cls_list.append(eval(col_cls_name))
        ts_list = [x().get_ts() for x in col_cls_list]
        tmp_table_df = pd.concat(ts_list, axis=1).dropna(how="all")
        return tmp_table_df 

    
###########################################################################################################################
""" 仓单数量 """    

class BaiTangCangDanShuLiang_ZhengZhouShangPinJiaoYiSuo(inventory_base, WindData):
    field_name = u"仓单数量"
    col_name = u"白糖仓单数量"    
    wind_code = "S0049500" 

###########################################################################################################################
""" 有效预报 """ 

class BaiTangYouXiaoYuBao_ZhengZhouShangPinJiaoYiSuo(inventory_base, WindData):
    field_name = u"有效预报"
    col_name = u"白糖有效预报"    
    wind_code = "S0049519" 


###########################################################################################################################
""" 工业库存 """ 

class MianHuaGongYeKuCun_QuanGuo(inventory_base, WindData):
    field_name = u"工业库存"
    col_name = u"棉花工业库存_全国"    








    
    
    