# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 10:48:24 2018

@author: 李弘一萌
"""

import pandas as pd
from datetime import datetime
from .Y_Base import Y_Base
from . import Y_SpotPrice, Y_Upstream, Y_FuturesPrice
from ..OI import OI_FuturesPrice
from ..P import P_FuturesPrice
from ...Base.Spread_Generate import main_month_quote_2_spread_series
from ...Base.DataType_Base import Manual, Computed, WindData
from ...Base.Plot_Base import Plot_Base
from matplotlib.ticker import FuncFormatter

class spread_base(Y_Base, Plot_Base):
    table_english_name = "Spread"
    table_chinese_name = u"价差"
    
    def output(self):
        print("Spread")
    
    def get_relevant_df(self, col_list):
        ts_list = [eval(Y_Base.get_table_class_full_variable(x))().get_ts() for x in col_list]
        tmp_table_df = pd.concat(ts_list, axis=1).dropna(how="all")
        return tmp_table_df  
    

###########################################################################################################################
""" 基差(计算指标) """ 

    
class Y1YueJiCha(spread_base, Computed):
    field_name = u"基差"
    col_name = u"Y1月基差"
    axhline = 0
    def get_ts_whole_progress(self):
#        relevant_col_list = [u"中国棉花328价格指数", "Y01合约收盘价"]
#        tmp_total = self.get_relevant_df(relevant_col_list)
#        tmp_total[self.col_name] = tmp_total[u"中国棉花328价格指数"] - tmp_total[u"Y01合约收盘价"]
#        return tmp_total
        pass
    
    def seasonal_plot(self, title=None, start_year=None, axhline=None):
        tmp_df_interpolated, fig, axis = super(Y1YueJiCha, self).seasonal_plot(title=self.col_name, axhline=self.axhline, date_constraint=[1, 17])
        axis = Plot_Base.add_month_span(axis, tmp_df_interpolated, 1)
        return tmp_df_interpolated, fig, axis


class Y5YueJiCha(spread_base, Computed):
    field_name = u"基差"
    col_name = u"Y5月基差"
    axhline = 0
    def get_ts_whole_progress(self):
#        relevant_col_list = [u"中国棉花328价格指数", "Y05合约收盘价"]
#        tmp_total = self.get_relevant_df(relevant_col_list)
#        tmp_total[self.col_name] = tmp_total[u"中国棉花328价格指数"] - tmp_total[u"Y05合约收盘价"]
#        return tmp_total
        pass
    
    def seasonal_plot(self, title=None, start_year=None, axhline=None):
        tmp_df_interpolated, fig, axis = super(Y5YueJiCha, self).seasonal_plot(title=self.col_name, axhline=self.axhline, date_constraint=[5, 17])
        axis = Plot_Base.add_month_span(axis, tmp_df_interpolated, 5)
        return tmp_df_interpolated, fig, axis

    
class Y9YueJiCha(spread_base, Computed):
    field_name = u"基差"
    col_name = u"Y9月基差"
    axhline = 0
    def get_ts_whole_progress(self):
#        relevant_col_list = [u"中国棉花328价格指数", "Y09合约收盘价"]
#        tmp_total = self.get_relevant_df(relevant_col_list)
#        tmp_total[self.col_name] = tmp_total[u"中国棉花328价格指数"] - tmp_total[u"Y09合约收盘价"]
#        return tmp_total
        pass
    
    def seasonal_plot(self, title=None, start_year=None, axhline=None):
        tmp_df_interpolated, fig, axis = super(Y9YueJiCha, self).seasonal_plot(title=self.col_name, axhline=self.axhline, date_constraint=[9, 17])
        axis = Plot_Base.add_month_span(axis, tmp_df_interpolated, 9)
        return tmp_df_interpolated, fig, axis
    

###########################################################################################################################
""" 月间价差(计算指标) """ 

class Y1_5JiaCha(spread_base, Computed):
    field_name = u"月间价差"
    col_name = u"Y1-5价差"
    axhline = 0
    start_year = 2015
    def get_ts_whole_progress(self):
        month_list = ["01", "05"]
        all_main_quote_df = Y_Base.get_Y_main_month_quote_df()
        spread_series = main_month_quote_2_spread_series(month_list, all_main_quote_df)
        tmp_df = pd.DataFrame([spread_series], index=[self.col_name]).T
        return tmp_df

    def seasonal_plot(self, title=None, start_year=None, axhline=None):
        tmp_df_interpolated, fig, axis = super(Y1_5JiaCha, self).seasonal_plot(title=self.col_name, start_year = self.start_year, 
                                              axhline=self.axhline, date_constraint=[1, 17])
        axis = Plot_Base.add_month_span(axis, tmp_df_interpolated, 1)
        return tmp_df_interpolated, fig, axis
        
class Y5_9JiaCha(spread_base, Computed):
    field_name = u"月间价差"
    col_name = u"Y5-9价差"
    axhline = 0
    start_year = 2015
    def get_ts_whole_progress(self):
        month_list = ["05", "09"]
        all_main_quote_df = Y_Base.get_Y_main_month_quote_df()
        spread_series = main_month_quote_2_spread_series(month_list, all_main_quote_df)
        tmp_df = pd.DataFrame([spread_series], index=[self.col_name]).T
        return tmp_df

    def seasonal_plot(self, title=None, start_year=None, axhline=None):
        tmp_df_interpolated, fig, axis = super(Y5_9JiaCha, self).seasonal_plot(title=self.col_name, start_year = self.start_year, 
                                              axhline=self.axhline, date_constraint=[5, 17])
        axis = Plot_Base.add_month_span(axis, tmp_df_interpolated, 5)
        return tmp_df_interpolated, fig, axis    
      

class Y9_1JiaCha(spread_base, Computed):
    field_name = u"月间价差"
    col_name = u"Y9-1价差"
    axhline = 0
    start_year = 2015
    def get_ts_whole_progress(self):
        month_list = ["09", "01"]
        all_main_quote_df = Y_Base.get_Y_main_month_quote_df()
        spread_series = main_month_quote_2_spread_series(month_list, all_main_quote_df)
        tmp_df = pd.DataFrame([spread_series], index=[self.col_name]).T
        return tmp_df

    def seasonal_plot(self, title=None, start_year=None, axhline=None):
        tmp_df_interpolated, fig, axis = super(Y9_1JiaCha, self).seasonal_plot(title=self.col_name, start_year = self.start_year, 
                                              axhline=self.axhline, date_constraint=[9, 17])
        axis = Plot_Base.add_month_span(axis, tmp_df_interpolated, 9)
        return tmp_df_interpolated, fig, axis  
        
###########################################################################################################################
""" 国际价差 """ 
    
class GuoJiDouZongFOBJiaCha(spread_base, WindData):
    field_name = u"国际价差"
    col_name = u"国际豆棕FOB价差"   
    wind_code = "S5023708"

###########################################################################################################################
""" 国内盘面价差 """ 

class CaiYouDouYou1YueHeYueJiaCha(spread_base, Computed):
    field_name = u"国内盘面价差"
    col_name = u"菜油豆油1月合约价差"   
    def get_ts_whole_progress(self):
        tmp_ts = OI_FuturesPrice.OI01HeYueShouPanJia().get_ts()
        relevant_col_list = ["Y01合约收盘价"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total = pd.concat([tmp_total, tmp_ts], axis=1, sort=False)
        tmp_total[self.col_name] = tmp_total[u"OI01合约收盘价"] - tmp_total[u"Y01合约收盘价"]
        return tmp_total 

class CaiYouDouYou5YueHeYueJiaCha(spread_base, Computed):
    field_name = u"国内盘面价差"
    col_name = u"菜油豆油5月合约价差"   
    def get_ts_whole_progress(self):
        tmp_ts = OI_FuturesPrice.OI05HeYueShouPanJia().get_ts()
        relevant_col_list = ["Y05合约收盘价"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total = pd.concat([tmp_total, tmp_ts], axis=1, sort=False)
        tmp_total[self.col_name] = tmp_total[u"OI05合约收盘价"] - tmp_total[u"Y05合约收盘价"]
        return tmp_total 

class CaiYouDouYou9YueHeYueJiaCha(spread_base, Computed):
    field_name = u"国内盘面价差"
    col_name = u"菜油豆油9月合约价差"   
    def get_ts_whole_progress(self):
        tmp_ts = OI_FuturesPrice.OI09HeYueShouPanJia().get_ts()
        relevant_col_list = ["Y09合约收盘价"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total = pd.concat([tmp_total, tmp_ts], axis=1, sort=False)
        tmp_total[self.col_name] = tmp_total[u"OI09合约收盘价"] - tmp_total[u"Y09合约收盘价"]
        return tmp_total 

class DouYouZongLvYou1YueHeYueJiaCha(spread_base, Computed):
    field_name = u"国内盘面价差"
    col_name = u"豆油棕榈油1月合约价差"   
    def get_ts_whole_progress(self):
        tmp_ts = P_FuturesPrice.P01HeYueShouPanJia().get_ts()
        relevant_col_list = ["Y01合约收盘价"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total = pd.concat([tmp_total, tmp_ts], axis=1, sort=False)
        tmp_total[self.col_name] = tmp_total[u"P01合约收盘价"] - tmp_total[u"Y01合约收盘价"]
        return tmp_total 

class DouYouZongLvYou5YueHeYueJiaCha(spread_base, Computed):
    field_name = u"国内盘面价差"
    col_name = u"豆油棕榈油5月合约价差"   
    def get_ts_whole_progress(self):
        tmp_ts = P_FuturesPrice.P05HeYueShouPanJia().get_ts()
        relevant_col_list = ["Y05合约收盘价"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total = pd.concat([tmp_total, tmp_ts], axis=1, sort=False)
        tmp_total[self.col_name] = tmp_total[u"P05合约收盘价"] - tmp_total[u"Y05合约收盘价"]
        return tmp_total  

class DouYouZongLvYou9YueHeYueJiaCha(spread_base, Computed):
    field_name = u"国内盘面价差"
    col_name = u"豆油棕榈油9月合约价差"   
    def get_ts_whole_progress(self):
        tmp_ts = P_FuturesPrice.P09HeYueShouPanJia().get_ts()
        relevant_col_list = ["Y09合约收盘价"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total = pd.concat([tmp_total, tmp_ts], axis=1, sort=False)
        tmp_total[self.col_name] = tmp_total[u"P09合约收盘价"] - tmp_total[u"Y09合约收盘价"]
        return tmp_total 
    
if __name__ == "__main__":
    ts = Y1_5JiaCha().seasonal_plot()
    
    
    
    
    
    
    
    
    
    
    
    
    