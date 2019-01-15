# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 10:47:54 2018

@author: 李弘一萌
"""

import pandas as pd
from datetime import datetime
from .Y_Base import Y_Base
from ...Base.DataType_Base import Manual, Computed, WindData
from ...Base.Plot_Base import Plot_Base
from matplotlib.ticker import FuncFormatter

class inventory_base(Y_Base, Plot_Base):
    table_english_name = "Inventory"
    table_chinese_name = u"库存"
    
    def output(self):
        print("Inventory")
    
    def get_relevant_df(self, col_list):
        local_col_name_list = inventory_base.get_all_table_classname()
        col_cls_list = []
        for x in col_list:
            col_cls_name = str(Y_Base.get_class_name(x))
            if col_cls_name not in local_col_name_list:
                col_cls_list.append(eval(Y_Base.get_table_class_full_variable(x)))
            else:
                col_cls_list.append(eval(col_cls_name))
        ts_list = [x().get_ts() for x in col_cls_list]
        tmp_table_df = pd.concat(ts_list, axis=1).dropna(how="all")
        return tmp_table_df 

    
###########################################################################################################################
""" 国内未执行合同 """    

class DouYouWeiZhiXingHeTong(inventory_base, Manual):
    field_name = u"国内未执行合同"
    col_name = u"豆油未执行合同"    


    
###########################################################################################################################
""" 国内日度库存 """ 

class GuoNeiDouYouShangYeKuCun(inventory_base, Manual):
    field_name = u"国内日度库存"
    col_name = u"国内豆油商业库存"    
    
###########################################################################################################################
""" 国内周度库存 """ 

class DouYouZhouDuKuCun(inventory_base, Manual):
    field_name = u"国内周度库存"
    col_name = u"豆油周度库存"    





    
if __name__ == "__main__":
    df = MianHuaRiZongShouChuChengJiaoLiang().get_ts()  












    
    
    