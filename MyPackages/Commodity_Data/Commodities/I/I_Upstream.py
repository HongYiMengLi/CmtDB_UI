# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 10:44:58 2018

@author: 李弘一萌
"""

import pandas as pd
from datetime import datetime
from .I_Base import I_Base
from ...Base.DataType_Base import Manual, Computed, WindData
from ...Base.Plot_Base import Plot_Base
from matplotlib.ticker import FuncFormatter

class upstream_base(I_Base, Plot_Base):
    table_english_name = "Upstream"
    table_chinese_name = u"上游"
    
    def output(self):
        print("Upstream")
    
    def get_relevant_df(self, col_list):
        local_col_name_list = upstream_base.get_all_table_classname()
        col_cls_list = []
        for x in col_list:
            col_cls_name = str(I_Base.get_class_name(x))
            if col_cls_name not in local_col_name_list:
                col_cls_list.append(eval(I_Base.get_table_class_full_variable(x)))
            else:
                col_cls_list.append(eval(col_cls_name))
        ts_list = [x().get_ts() for x in col_cls_list]
        tmp_table_df = pd.concat(ts_list, axis=1).dropna(how="all")
        return tmp_table_df
    
###########################################################################################################################
""" 海运价格 """  
     

class TieKuangShiYunJia_XiAo_QingDao_BCI_C5(upstream_base, WindData):
    field_name = u"海运价格"
    col_name = u"铁矿石运价_西澳-青岛(BCI-C5)"
    wind_code = "S0109343"
    
class TieKuangShiYunJia_BaXiTuBaLang_QingDao_BCI_C3(upstream_base, WindData):
    field_name = u"海运价格"
    col_name = u"铁矿石运价_巴西图巴郎-青岛(BCI-C3)"
    wind_code = "S0109342"
    

    
if __name__ == "__main__":
    df = PIXianHuoJiaGongFei().seasonal_plot()    
    
    
    
    
    
    
    
    
    
    
    
    
    
    