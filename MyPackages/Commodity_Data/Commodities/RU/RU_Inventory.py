# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 10:47:54 2018

@author: 李弘一萌
"""

import pandas as pd
from datetime import datetime
from .RU_Base import RU_Base
from ...Base.DataType_Base import Manual, Computed, WindData
from ...Base.Plot_Base import Plot_Base
from matplotlib.ticker import FuncFormatter

class inventory_base(RU_Base, Plot_Base):
    table_english_name = "Inventory"
    table_chinese_name = u"库存"
    
    def output(self):
        print("Inventory")
    
    def get_relevant_df(self, col_list):
        local_col_name_list = inventory_base.get_all_table_classname()
        col_cls_list = []
        for x in col_list:
            col_cls_name = str(RU_Base.get_class_name(x))
            if col_cls_name not in local_col_name_list:
                col_cls_list.append(eval(RU_Base.get_table_class_full_variable(x)))
            else:
                col_cls_list.append(eval(col_cls_name))
        ts_list = [x().get_ts() for x in col_cls_list]
        tmp_table_df = pd.concat(ts_list, axis=1).dropna(how="all")
        return tmp_table_df 

    
###########################################################################################################################
""" 保税区库存 """    

class XiangJiaoKuCunHeJi_QingDaoBaoShuiQu(inventory_base, WindData):
    field_name = u"保税区库存"
    col_name = u"橡胶库存合计_青岛保税区"    
    wind_code = "S5016800" 

class TianRanXiangJiaoKuCun_QingDaoBaoShuiQu(inventory_base, WindData):
    field_name = u"保税区库存"
    col_name = u"天然橡胶库存_青岛保税区"    
    wind_code = "S5016797"
    
class HeChengXiangJiaoKuCun_QingDaoBaoShuiQu(inventory_base, WindData):
    field_name = u"保税区库存"
    col_name = u"合成橡胶库存_青岛保税区"    
    wind_code = "S5016798"
    
class FuHeXiangJiaoKuCun_QingDaoBaoShuiQu(inventory_base, WindData):
    field_name = u"保税区库存"
    col_name = u"复合橡胶库存_青岛保税区"    
    wind_code = "S5016799"

    
###########################################################################################################################
""" 期货库存 """    
    
class XiangJiaoQiHuoKuCun_ShangQiSuo(inventory_base, WindData):
    field_name = u"期货库存"
    col_name = u"橡胶期货库存_上期所"    
    wind_code = "S0163835"
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    