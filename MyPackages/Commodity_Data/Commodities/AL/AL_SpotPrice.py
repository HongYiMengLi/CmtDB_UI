# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 16:35:12 2018

@author: 李弘一萌
"""

import pandas as pd
from datetime import datetime
from .AL_Base import AL_Base
from ...Base.DataType_Base import Manual, Computed, WindData
from ...Base.Plot_Base import Plot_Base
from matplotlib.ticker import FuncFormatter

class spot_price_base(AL_Base, Plot_Base):
    table_english_name = "SpotPrice"
    table_chinese_name = u"现货价格"
#    original_db_filepath = data_path + u"LPP价格数据库.xlsx"
    
    def output(self):
        print("SpotPrice")
    
    def get_relevant_df(self, col_list):
        local_col_name_list = spot_price_base.get_all_table_classname()
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
""" 电解铝价格 """    

class GuoChanA00Lv_PiShouHanPiao_JiaGe_NanHaiYouSe_PingJunJia_FoShan(spot_price_base, WindData):
    field_name = u"电解铝价格"
    col_name = u"国产A00铝(批售含票)价格_南海有色(灵通)_平均价_佛山"
    wind_code = "S5807011"
    
class GuoChanA00Lv_PiShouBuHanPiao_JiaGe_NanHaiYouSe_PingJunJia_FoShan(spot_price_base, WindData):
    field_name = u"电解铝价格"
    col_name = u"国产A00铝(批售不含票)价格_南海有色(灵通)_平均价_佛山"
    wind_code = "S5807012"
    
class DianJieLvJiaGe_ChangJiangYouSeShiChang_ZuiGaoJia(spot_price_base, WindData):
    field_name = u"电解铝价格"
    col_name = u"电解铝价格_长江有色市场_最高价"
    wind_code = "S0031729"
    
class DianJieLvJiaGe_ChangJiangYouSeShiChang_ZuiDiJia(spot_price_base, WindData):
    field_name = u"电解铝价格"
    col_name = u"电解铝价格_长江有色市场_最低价"
    wind_code = "S0031730"    
    
class DianJieLvJiaGe_ChangJiangYouSeShiChang_PingJunJia_A00(spot_price_base, WindData):
    field_name = u"电解铝价格"
    col_name = u"电解铝价格_长江有色市场_平均价_A00"
    wind_code = "S0182162"

    

if __name__ == "__main__":
    ts = PALXianHuoJiaGe_HuaDong().get_ts()