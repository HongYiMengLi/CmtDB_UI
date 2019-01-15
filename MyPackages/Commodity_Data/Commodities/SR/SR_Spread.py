# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 10:48:24 2018

@author: 李弘一萌
"""

import pandas as pd
from datetime import datetime
from .SR_Base import SR_Base
#from . import CF_SpotPrice, CF_Upstream, CF_FuturesPrice
from ...Base.Spread_Generate import main_month_quote_2_spread_series
from ...Base.DataType_Base import Manual, Computed, WindData
from ...Base.Plot_Base import Plot_Base
from matplotlib.ticker import FuncFormatter

class spread_base(SR_Base, Plot_Base):
    table_english_name = "Spread"
    table_chinese_name = u"价差"
    
    def output(self):
        print("Spread")
    
    def get_relevant_df(self, col_list):
        ts_list = [eval(SR_Base.get_table_class_full_variable(x))().get_ts() for x in col_list]
        tmp_table_df = pd.concat(ts_list, axis=1).dropna(how="all")
        return tmp_table_df  
    

###########################################################################################################################
""" 基差(计算指标) """ 




    
if __name__ == "__main__":
    ts = CF1_5JiaCha().seasonal_plot()
    
    
    
    
    
    
    
    
    
    
    
    
    