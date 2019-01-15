# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 16:35:12 2018

@author: 李弘一萌
"""

import pandas as pd
from datetime import datetime
from .CU_Base import CU_Base
from ...Base.DataType_Base import Manual, Computed, WindData
from ...Base.Plot_Base import Plot_Base
from matplotlib.ticker import FuncFormatter

class spot_price_base(CU_Base, Plot_Base):
    table_english_name = "SpotPrice"
    table_chinese_name = u"现货价格"
#    original_db_filepath = data_path + u"LPP价格数据库.xlsx"
    
    def output(self):
        print("SpotPrice")
    
    def get_relevant_df(self, col_list):
        local_col_name_list = spot_price_base.get_all_table_classname()
        col_cls_list = []
        for x in col_list:
            col_cls_name = str(CU_Base.get_class_name(x))
            if col_cls_name not in local_col_name_list:
                col_cls_list.append(eval(CU_Base.get_table_class_full_variable(x)))
            else:
                col_cls_list.append(eval(col_cls_name))
        ts_list = [x().get_ts() for x in col_cls_list]
        tmp_table_df = pd.concat(ts_list, axis=1).dropna(how="all")
        return tmp_table_df  
    
###########################################################################################################################
""" 精铜现货价格 """    

class JingTongJiaGe_ZuiGaoJia_Tong_ChangJiangYouSeShiChang(spot_price_base, WindData):
    field_name = u"精铜现货价格"
    col_name = u"精铜价格_最高价_铜_长江有色市场"
    wind_code = "S0031723"
    
class JingTongJiaGe_ZuiDiJia_Tong_ChangJiangYouSeShiChang(spot_price_base, WindData):
    field_name = u"精铜现货价格"
    col_name = u"精铜价格_最低价_铜_长江有色市场"
    wind_code = "S0031724"
    
class JingTongJiaGe_PingJunJia_No1_ShangHaiJinShuWang(spot_price_base, WindData):
    field_name = u"精铜现货价格"
    col_name = u"精铜价格_平均价_1#_上海金属网"
    wind_code = "S0105511"
    
class JingTongJiaGe_PingJunJia_ShangHaiWuMao(spot_price_base, WindData):
    field_name = u"精铜现货价格"
    col_name = u"精铜价格_平均价_上海物贸"
    wind_code = "S5806983"    


if __name__ == "__main__":
    ts = PCUXianHuoJiaGe_HuaDong().get_ts()