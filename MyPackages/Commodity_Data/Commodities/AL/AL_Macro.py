# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 10:44:58 2018

@author: 李弘一萌
"""

import pandas as pd
from datetime import datetime
from .AL_Base import AL_Base
from ...Base.DataType_Base import Manual, Computed, WindData
from ...Base.Plot_Base import Plot_Base
from matplotlib.ticker import FuncFormatter

class macro_base(AL_Base, Plot_Base):
    table_english_name = "Macro"
    table_chinese_name = u"宏观"
#    original_db_filepath = data_path + u"LPP价格数据库.xlsx"
    
    def output(self):
        print("Upstream")
    
    def get_relevant_df(self, col_list):
        local_col_name_list = macro_base.get_all_table_classname()
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
""" 汇率 """  
     
class JiQiHuiLv_MeiYuanDuiRenMinBi(macro_base, WindData):
    field_name = u"汇率"
    col_name = u"即期汇率_美元兑人民币"
    wind_code = "M0067855"
    





    
if __name__ == "__main__":
    df = PALXianHuoJiaGongFei().seasonal_plot()    
    
    
    
    
    
    
    
    
    
    
    
    
    
    