# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 10:47:54 2018

@author: 李弘一萌
"""

import pandas as pd
from datetime import datetime
from .AL_Base import AL_Base
from ...Base.DataType_Base import Manual, Computed, WindData
from ...Base.Plot_Base import Plot_Base
from matplotlib.ticker import FuncFormatter

class inventory_base(AL_Base, Plot_Base):
    table_english_name = "Inventory"
    table_chinese_name = u"库存"
#    original_db_filepath = data_path + u"LPP价格数据库.xlsx"
    
    def output(self):
        print("Inventory")
    
    def get_relevant_df(self, col_list):
        local_col_name_list = inventory_base.get_all_table_classname()
        col_cls_list = []
        for x in col_list:
            col_cls_name = str(AL_Base.get_class_name(x))
            if col_cls_name not in local_col_name_list:
                col_cls_list.append(eval(AL_Base.get_table_class_full_variable(x)))
            else:
                col_cls_list.append(eval(col_cls_name))
        ts_list = [x().get_ts() for x in col_cls_list]
        tmp_table_df = pd.concat(ts_list, axis=1).dropna(how="all")
        return tmp_table_df 

###########################################################################################################################
""" 电解铝库存 """    

class DianJieLvGuoNeiKuCun(inventory_base, Manual):
    field_name = u"电解铝库存"
    col_name = u"电解铝国内库存"

class LvKuCunXiaoJi_ZongJi(inventory_base, WindData):
    field_name = u"电解铝库存"
    col_name = u"铝库存小计_总计"
    wind_code = "S0049509"
    
class LvKuCunQiHuo(inventory_base, WindData):
    field_name = u"电解铝库存"
    col_name = u"铝库存期货"
    wind_code = "S0049494"
    
class DianJieLvXianHuoKuCun_HeJi(inventory_base, WindData):
    field_name = u"电解铝库存"
    col_name = u"电解铝现货库存_合计"
    wind_code = "S9900014"
    start_year = 2014
    
class LMELvZongKuCun(inventory_base, WindData):
    field_name = u"电解铝库存"
    col_name = u"LME铝总库存"
    wind_code = "S0029756"
    start_year = 2014

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    