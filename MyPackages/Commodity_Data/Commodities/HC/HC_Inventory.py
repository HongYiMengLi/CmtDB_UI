# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 10:47:54 2018

@author: 李弘一萌
"""

import pandas as pd
from datetime import datetime
from .HC_Base import HC_Base
from ...Base.DataType_Base import Manual, Computed, WindData
from ...Base.Plot_Base import Plot_Base
from matplotlib.ticker import FuncFormatter

class inventory_base(HC_Base, Plot_Base):
    table_english_name = "Inventory"
    table_chinese_name = u"库存"
#    original_db_filepath = data_path + u"LPP价格数据库.xlsx"
    
    def output(self):
        print("Inventory")
    
    def get_relevant_df(self, col_list):
        local_col_name_list = inventory_base.get_all_table_classname()
        col_cls_list = []
        for x in col_list:
            col_cls_name = str(HC_Base.get_class_name(x))
            if col_cls_name not in local_col_name_list:
                col_cls_list.append(eval(HC_Base.get_table_class_full_variable(x)))
            else:
                col_cls_list.append(eval(col_cls_name))
        ts_list = [x().get_ts() for x in col_cls_list]
        tmp_table_df = pd.concat(ts_list, axis=1).dropna(how="all")
        return tmp_table_df 

###########################################################################################################################
""" 钢厂库存 """    

class ReJuanGangChangKuCun(inventory_base, Manual):
    field_name = u"钢厂库存"
    col_name = u"热卷钢厂库存"

class LengJuanGangChangKuCun(inventory_base, Manual):
    field_name = u"钢厂库存"
    col_name = u"冷卷钢厂库存"


    
###########################################################################################################################
""" 社会库存 """    

class ReZhaJuanBanSheHuiKuCun(inventory_base, Manual):
    field_name = u"社会库存"
    col_name = u"热轧卷板社会库存"    

class ReZhaJuanBanSheHuiKuCun_ShangHai(inventory_base, Manual):
    field_name = u"社会库存"
    col_name = u"热轧卷板社会库存_上海"    

class ReZhaJuanBanSheHuiKuCun_GuangDongLeCong(inventory_base, Manual):
    field_name = u"社会库存"
    col_name = u"热轧卷板社会库存_广东乐从"    

class LengJuanSheHuiKuCun(inventory_base, Manual):
    field_name = u"社会库存"
    col_name = u"冷卷社会库存"  
    
###########################################################################################################################
""" 总库存 """    

    
class ReZhaJuanBanZongKuCun(inventory_base, Computed):
    field_name = u"总库存"
    col_name = u"热轧卷板总库存"
    
    def get_ts_whole_progress(self):
        relevant_col_list = [u"热轧卷板社会库存", u"热卷钢厂库存"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"热轧卷板社会库存"] + tmp_total[u"热卷钢厂库存"]
        return tmp_total   
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    