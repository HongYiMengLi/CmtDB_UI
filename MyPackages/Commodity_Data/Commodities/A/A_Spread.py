# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 10:48:24 2018

@author: 李弘一萌
"""

import pandas as pd
from datetime import datetime
from .A_Base import A_Base
from . import A_SpotPrice, A_FuturesPrice
from ...Base.Spread_Generate import main_month_quote_2_spread_series
from ...Base.DataType_Base import Manual, Computed, WindData
from ...Base.Plot_Base import Plot_Base
from matplotlib.ticker import FuncFormatter

class spread_base(A_Base, Plot_Base):
    table_english_name = "Spread"
    table_chinese_name = u"价差"
    
    def output(self):
        print("Spread")
    
    def get_relevant_df(self, col_list):
        ts_list = [eval(A_Base.get_table_class_full_variable(x))().get_ts() for x in col_list]
        tmp_table_df = pd.concat(ts_list, axis=1).dropna(how="all")
        return tmp_table_df  
    

###########################################################################################################################
""" 基差(计算指标) """ 

    
#class A1YueJiCha(spread_base, Computed):
#    field_name = u"基差"
#    col_name = u"A1月基差"
#    axhline = 0
#    def get_ts_whole_progress(self):
#        relevant_col_list = [u"中国棉花328价格指数", "A01合约收盘价"]
#        tmp_total = self.get_relevant_df(relevant_col_list)
#        tmp_total[self.col_name] = tmp_total[u"中国棉花328价格指数"] - tmp_total[u"A01合约收盘价"]
#        return tmp_total
#    
#    def seasonal_plot(self, title=None, start_year=None, axhline=None):
#        tmp_df_interpolated, fig, axis = super(A1YueJiCha, self).seasonal_plot(title=self.col_name, axhline=self.axhline, date_constraint=[1, 17])
#        axis = Plot_Base.add_month_span(axis, tmp_df_interpolated, 1)
#        return tmp_df_interpolated, fig, axis
#
#
#class A5YueJiCha(spread_base, Computed):
#    field_name = u"基差"
#    col_name = u"A5月基差"
#    axhline = 0
#    def get_ts_whole_progress(self):
#        relevant_col_list = [u"中国棉花328价格指数", "A05合约收盘价"]
#        tmp_total = self.get_relevant_df(relevant_col_list)
#        tmp_total[self.col_name] = tmp_total[u"中国棉花328价格指数"] - tmp_total[u"A05合约收盘价"]
#        return tmp_total
#    
#    def seasonal_plot(self, title=None, start_year=None, axhline=None):
#        tmp_df_interpolated, fig, axis = super(A5YueJiCha, self).seasonal_plot(title=self.col_name, axhline=self.axhline, date_constraint=[5, 17])
#        axis = Plot_Base.add_month_span(axis, tmp_df_interpolated, 5)
#        return tmp_df_interpolated, fig, axis
#
#    
#class A9YueJiCha(spread_base, Computed):
#    field_name = u"基差"
#    col_name = u"A9月基差"
#    axhline = 0
#    def get_ts_whole_progress(self):
#        relevant_col_list = [u"中国棉花328价格指数", "A09合约收盘价"]
#        tmp_total = self.get_relevant_df(relevant_col_list)
#        tmp_total[self.col_name] = tmp_total[u"中国棉花328价格指数"] - tmp_total[u"A09合约收盘价"]
#        return tmp_total
#    
#    def seasonal_plot(self, title=None, start_year=None, axhline=None):
#        tmp_df_interpolated, fig, axis = super(A9YueJiCha, self).seasonal_plot(title=self.col_name, axhline=self.axhline, date_constraint=[9, 17])
#        axis = Plot_Base.add_month_span(axis, tmp_df_interpolated, 9)
#        return tmp_df_interpolated, fig, axis
    

###########################################################################################################################
""" 月间价差(计算指标) """ 

class A1_5JiaCha(spread_base, Computed):
    field_name = u"月间价差"
    col_name = u"A1-5价差"
    axhline = 0
    start_year = 2015
    def get_ts_whole_progress(self):
        month_list = ["01", "05"]
        all_main_quote_df = A_Base.get_A_main_month_quote_df()
        spread_series = main_month_quote_2_spread_series(month_list, all_main_quote_df)
        tmp_df = pd.DataFrame([spread_series], index=[self.col_name]).T
        return tmp_df

    def seasonal_plot(self, title=None, start_year=None, axhline=None):
        tmp_df_interpolated, fig, axis = super(A1_5JiaCha, self).seasonal_plot(title=self.col_name, start_year = self.start_year, 
                                              axhline=self.axhline, date_constraint=[1, 17])
        axis = Plot_Base.add_month_span(axis, tmp_df_interpolated, 1)
        return tmp_df_interpolated, fig, axis
        
class A5_9JiaCha(spread_base, Computed):
    field_name = u"月间价差"
    col_name = u"A5-9价差"
    axhline = 0
    start_year = 2015
    def get_ts_whole_progress(self):
        month_list = ["05", "09"]
        all_main_quote_df = A_Base.get_A_main_month_quote_df()
        spread_series = main_month_quote_2_spread_series(month_list, all_main_quote_df)
        tmp_df = pd.DataFrame([spread_series], index=[self.col_name]).T
        return tmp_df

    def seasonal_plot(self, title=None, start_year=None, axhline=None):
        tmp_df_interpolated, fig, axis = super(A5_9JiaCha, self).seasonal_plot(title=self.col_name, start_year = self.start_year, 
                                              axhline=self.axhline, date_constraint=[5, 17])
        axis = Plot_Base.add_month_span(axis, tmp_df_interpolated, 5)
        return tmp_df_interpolated, fig, axis    
      

class A9_1JiaCha(spread_base, Computed):
    field_name = u"月间价差"
    col_name = u"A9-1价差"
    axhline = 0
    start_year = 2015
    def get_ts_whole_progress(self):
        month_list = ["09", "01"]
        all_main_quote_df = A_Base.get_A_main_month_quote_df()
        spread_series = main_month_quote_2_spread_series(month_list, all_main_quote_df)
        tmp_df = pd.DataFrame([spread_series], index=[self.col_name]).T
        return tmp_df

    def seasonal_plot(self, title=None, start_year=None, axhline=None):
        tmp_df_interpolated, fig, axis = super(A9_1JiaCha, self).seasonal_plot(title=self.col_name, start_year = self.start_year, 
                                              axhline=self.axhline, date_constraint=[9, 17])
        axis = Plot_Base.add_month_span(axis, tmp_df_interpolated, 9)
        return tmp_df_interpolated, fig, axis  
        


    
if __name__ == "__main__":
    ts = A1_5JiaCha().seasonal_plot()
    
    
    
    
    
    
    
    
    
    
    
    
    