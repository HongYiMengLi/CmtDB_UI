# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 16:35:12 2018

@author: 李弘一萌
"""

import pandas as pd
from datetime import datetime
from .ZN_Base import ZN_Base
from ...Base.DataType_Base import Manual, Computed, WindData
from ...Base.Plot_Base import Plot_Base
from matplotlib.ticker import FuncFormatter

class spot_price_base(ZN_Base, Plot_Base):
    table_english_name = "SpotPrice"
    table_chinese_name = u"现货价格"
    
    def output(self):
        print("SpotPrice")
    
    def get_relevant_df(self, col_list):
        local_col_name_list = spot_price_base.get_all_table_classname()
        col_cls_list = []
        for x in col_list:
            col_cls_name = str(ZN_Base.get_class_name(x))
            if col_cls_name not in local_col_name_list:
                col_cls_list.append(eval(ZN_Base.get_table_class_full_variable(x)))
            else:
                col_cls_list.append(eval(col_cls_name))
        ts_list = [x().get_ts() for x in col_cls_list]
        tmp_table_df = pd.concat(ts_list, axis=1).dropna(how="all")
        return tmp_table_df  
    
###########################################################################################################################
""" 国内现货价格 """    

class No0XinJiaGe_ChangJiangYouSe_ZuiDiJia_HanShui(spot_price_base, WindData):
    field_name = u"国内现货价格"
    col_name = u"0#锌价格_长江有色_最低价(含税)"
    wind_code = "S5810836"
    
class No1XinJiaGe_ChangJiangYouSe_ZuiDiJia_HanShui(spot_price_base, WindData):
    field_name = u"国内现货价格"
    col_name = u"1#锌价格_长江有色_最低价(含税)"
    wind_code = "S5810837"
    
class No0XinDing_GuoChanJiaGe_GuangDongNanChu_PingJunJia_FoShanCangKu(spot_price_base, WindData):
    field_name = u"国内现货价格"
    col_name = u"0#锌锭(国产)价格_广东南储_平均价_佛山仓库"
    wind_code = "S5807003"
    
class No0XinJiaGe_ChangJiangYouSeShiChang_PingJunJia(spot_price_base, WindData):
    field_name = u"国内现货价格"
    col_name = u"0#锌价格_长江有色市场_平均价"
    wind_code = "S0048087"
        



    

if __name__ == "__main__":
    ts = PZNXianHuoJiaGe_HuaDong().get_ts()