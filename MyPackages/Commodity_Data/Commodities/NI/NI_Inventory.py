# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 10:47:54 2018

@author: 李弘一萌
"""

import pandas as pd
from datetime import datetime
from .NI_Base import NI_Base
from ...Base.DataType_Base import Manual, Computed, WindData
from ...Base.Plot_Base import Plot_Base
from matplotlib.ticker import FuncFormatter

class inventory_base(NI_Base, Plot_Base):
    table_english_name = "Inventory"
    table_chinese_name = u"库存"
#    original_db_filepath = data_path + u"LPP价格数据库.xlsx"
    
    def output(self):
        print("Inventory")
    
    def get_relevant_df(self, col_list):
        local_col_name_list = inventory_base.get_all_table_classname()
        col_cls_list = []
        for x in col_list:
            col_cls_name = str(NI_Base.get_class_name(x))
            if col_cls_name not in local_col_name_list:
                col_cls_list.append(eval(NI_Base.get_table_class_full_variable(x)))
            else:
                col_cls_list.append(eval(col_cls_name))
        ts_list = [x().get_ts() for x in col_cls_list]
        tmp_table_df = pd.concat(ts_list, axis=1).dropna(how="all")
        return tmp_table_df 

###########################################################################################################################
""" 电解镍库存 """    

class NieKuCunXiaoJi_ZongJi(inventory_base, WindData):
    field_name = u"电解镍库存"
    col_name = u"镍库存小计_总计"
    wind_code = "S0213020"
    start_year = 2014

class NieKuCunQiHuo(inventory_base, WindData):
    field_name = u"电解镍库存"
    col_name = u"镍库存期货"
    wind_code = "S0213018"
    
class LMENieZongKuCun(inventory_base, WindData):
    field_name = u"电解镍库存"
    col_name = u"LME镍总库存"
    wind_code = "S0029772"
    start_year = 2014
    
class LMENie_ZhuXiaoCangDan_HeJi_QuanQiu(inventory_base, WindData):
    field_name = u"电解镍库存"
    col_name = u"LME镍_注销仓单_合计_全球"
    wind_code = "S0165277"

    
class NieZhuXiaoCangDanKuCunBi(inventory_base, Computed):
    field_name = u"电解镍库存"
    col_name = u"镍注销仓单库存比"
    
    def get_ts_whole_progress(self):
        relevant_col_list = [u"LME镍_注销仓单_合计_全球", u"LME镍总库存"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"LME镍_注销仓单_合计_全球"] / tmp_total[u"LME镍总库存"]
        return tmp_total   
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    