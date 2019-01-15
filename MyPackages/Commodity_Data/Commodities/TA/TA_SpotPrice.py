# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 16:35:12 2018

@author: 李弘一萌
"""

import pandas as pd
from datetime import datetime
from .TA_Base import TA_Base
from ...Base.DataType_Base import Manual, Computed, WindData
from ...Base.Plot_Base import Plot_Base
from matplotlib.ticker import FuncFormatter

class spot_price_base(TA_Base, Plot_Base):
    table_english_name = "SpotPrice"
    table_chinese_name = u"现货价格"
    
    def output(self):
        print("SpotPrice")
    
    def get_relevant_df(self, col_list):
        local_col_name_list = spot_price_base.get_all_table_classname()
        col_cls_list = []
        for x in col_list:
            col_cls_name = str(TA_Base.get_class_name(x))
            if col_cls_name not in local_col_name_list:
                col_cls_list.append(eval(TA_Base.get_table_class_full_variable(x)))
            else:
                col_cls_list.append(eval(col_cls_name))
        ts_list = [x().get_ts() for x in col_cls_list]
        tmp_table_df = pd.concat(ts_list, axis=1).dropna(how="all")
        return tmp_table_df  
    
###########################################################################################################################
""" 国内现货价格 """    

class PTAXianHuoJiaGe_HuaNan(spot_price_base, Manual):
    field_name = u"国内现货价格"
    col_name = u"PTA现货价格_华南"

class PTAXianHuoJiaGe_HuaDong(spot_price_base, Manual):
    field_name = u"国内现货价格"
    col_name = u"PTA现货价格_华东"

###########################################################################################################################
""" 美金盘 """      

class PTAXianHuoJiaGe_WaiPan(spot_price_base, WindData):
    field_name = u"美金盘"
    col_name = u"PTA现货价格_外盘"
    wind_code = "S5435641"
    
    



if __name__ == "__main__":
    ts = PTAXianHuoJiaGe_HuaDong().get_ts()