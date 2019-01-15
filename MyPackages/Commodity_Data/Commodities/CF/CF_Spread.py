# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 10:48:24 2018

@author: 李弘一萌
"""

import pandas as pd
from datetime import datetime
from .CF_Base import CF_Base
from . import CF_SpotPrice, CF_Upstream, CF_FuturesPrice, CF_Downstream
from ...Base.Spread_Generate import main_month_quote_2_spread_series
from ...Base.DataType_Base import Manual, Computed, WindData
from ...Base.Plot_Base import Plot_Base
from matplotlib.ticker import FuncFormatter

class spread_base(CF_Base, Plot_Base):
    table_english_name = "Spread"
    table_chinese_name = u"价差"
#    original_db_filepath = data_path + u"LPP价格数据库.xlsx"
    
    def output(self):
        print("Spread")
    
    def get_relevant_df(self, col_list):
        ts_list = [eval(CF_Base.get_table_class_full_variable(x))().get_ts() for x in col_list]
        tmp_table_df = pd.concat(ts_list, axis=1).dropna(how="all")
        return tmp_table_df  
    

###########################################################################################################################
""" 基差(计算指标) """ 

    
class CF1YueJiCha(spread_base, Computed):
    field_name = u"基差"
    col_name = u"CF1月基差"
    axhline = 0
    def get_ts_whole_progress(self):
        relevant_col_list = [u"中国棉花328价格指数", "CF01合约收盘价"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"中国棉花328价格指数"] - tmp_total[u"CF01合约收盘价"]
        return tmp_total
    
    def seasonal_plot(self, title=None, start_year=None, axhline=None):
        tmp_df_interpolated, fig, axis = super(CF1YueJiCha, self).seasonal_plot(title=self.col_name, axhline=self.axhline, date_constraint=[1, 17])
        axis = Plot_Base.add_month_span(axis, tmp_df_interpolated, 1)
        return tmp_df_interpolated, fig, axis


class CF5YueJiCha(spread_base, Computed):
    field_name = u"基差"
    col_name = u"CF5月基差"
    axhline = 0
    def get_ts_whole_progress(self):
        relevant_col_list = [u"中国棉花328价格指数", "CF05合约收盘价"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"中国棉花328价格指数"] - tmp_total[u"CF05合约收盘价"]
        return tmp_total
    
    def seasonal_plot(self, title=None, start_year=None, axhline=None):
        tmp_df_interpolated, fig, axis = super(CF5YueJiCha, self).seasonal_plot(title=self.col_name, axhline=self.axhline, date_constraint=[5, 17])
        axis = Plot_Base.add_month_span(axis, tmp_df_interpolated, 5)
        return tmp_df_interpolated, fig, axis

    
class CF9YueJiCha(spread_base, Computed):
    field_name = u"基差"
    col_name = u"CF9月基差"
    axhline = 0
    def get_ts_whole_progress(self):
        relevant_col_list = [u"中国棉花328价格指数", "CF09合约收盘价"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"中国棉花328价格指数"] - tmp_total[u"CF09合约收盘价"]
        return tmp_total
    
    def seasonal_plot(self, title=None, start_year=None, axhline=None):
        tmp_df_interpolated, fig, axis = super(CF9YueJiCha, self).seasonal_plot(title=self.col_name, axhline=self.axhline, date_constraint=[9, 17])
        axis = Plot_Base.add_month_span(axis, tmp_df_interpolated, 9)
        return tmp_df_interpolated, fig, axis
    

###########################################################################################################################
""" 月间价差(计算指标) """ 

class CF1_5JiaCha(spread_base, Computed):
    field_name = u"月间价差"
    col_name = u"CF1-5价差"
    axhline = 0
    start_year = 2015
    def get_ts_whole_progress(self):
        month_list = ["01", "05"]
        all_main_quote_df = CF_Base.get_CF_main_month_quote_df()
        spread_series = main_month_quote_2_spread_series(month_list, all_main_quote_df)
        tmp_df = pd.DataFrame([spread_series], index=[self.col_name]).T
        return tmp_df

    def seasonal_plot(self, title=None, start_year=None, axhline=None):
        tmp_df_interpolated, fig, axis = super(CF1_5JiaCha, self).seasonal_plot(title=self.col_name, start_year = self.start_year, 
                                              axhline=self.axhline, date_constraint=[1, 17])
        axis = Plot_Base.add_month_span(axis, tmp_df_interpolated, 1)
        return tmp_df_interpolated, fig, axis
        
class CF5_9JiaCha(spread_base, Computed):
    field_name = u"月间价差"
    col_name = u"CF5-9价差"
    axhline = 0
    start_year = 2015
    def get_ts_whole_progress(self):
        month_list = ["05", "09"]
        all_main_quote_df = CF_Base.get_CF_main_month_quote_df()
        spread_series = main_month_quote_2_spread_series(month_list, all_main_quote_df)
        tmp_df = pd.DataFrame([spread_series], index=[self.col_name]).T
        return tmp_df

    def seasonal_plot(self, title=None, start_year=None, axhline=None):
        tmp_df_interpolated, fig, axis = super(CF5_9JiaCha, self).seasonal_plot(title=self.col_name, start_year = self.start_year, 
                                              axhline=self.axhline, date_constraint=[5, 21])
        axis = Plot_Base.add_month_span(axis, tmp_df_interpolated, 5)
        return tmp_df_interpolated, fig, axis    
      

class CF9_1JiaCha(spread_base, Computed):
    field_name = u"月间价差"
    col_name = u"CF9-1价差"
    axhline = 0
    start_year = 2015
    def get_ts_whole_progress(self):
        month_list = ["09", "01"]
        all_main_quote_df = CF_Base.get_CF_main_month_quote_df()
        spread_series = main_month_quote_2_spread_series(month_list, all_main_quote_df)
        tmp_df = pd.DataFrame([spread_series], index=[self.col_name]).T
        return tmp_df

    def seasonal_plot(self, title=None, start_year=None, axhline=None):
        tmp_df_interpolated, fig, axis = super(CF9_1JiaCha, self).seasonal_plot(title=self.col_name, start_year = self.start_year, 
                                              axhline=self.axhline, date_constraint=[9, 17])
        axis = Plot_Base.add_month_span(axis, tmp_df_interpolated, 9)
        return tmp_df_interpolated, fig, axis  
        
###########################################################################################################################
""" 涤短棉花价差 """ 
    
class DiDuanMianHuaJiaCha(spread_base, Computed):
    field_name = u"涤短棉花价差"
    col_name = u"涤短棉花价差"   
    def get_ts_whole_progress(self):
        relevant_col_list = [u"中国棉花328价格指数", u"涤短价格_1.4D直纺涤短"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"中国棉花328价格指数"] - tmp_total[u"涤短价格_1.4D直纺涤短"]
        return tmp_total  

###########################################################################################################################
""" 进口价差 """ 
    
class NeiWaiMianShaJiaCha_YinDu(spread_base, Computed):
    field_name = u"进口价差"
    col_name = u"内外棉纱价差_印度"   
    def get_ts_whole_progress(self):
        relevant_col_list = [u"监测系统C32S指数_CF_Index", u"进口棉纱价格_印度_C32S_港口提货价"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"监测系统C32S指数_CF_Index"] - tmp_total[u"进口棉纱价格_印度_C32S_港口提货价"]
        return tmp_total  

class NeiWaiMianShaJiaCha_ZhiShu(spread_base, Computed):
    field_name = u"进口价差"
    col_name = u"内外棉纱价差_指数"   
    def get_ts_whole_progress(self):
        relevant_col_list = [u"监测系统C32S指数_CF_Index", u"进口棉纱价格指数(FCY_Index)_到港价_C32S"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"监测系统C32S指数_CF_Index"] - tmp_total[u"进口棉纱价格指数(FCY_Index)_到港价_C32S"]
        return tmp_total 
    
    
class MianHuaJinKouJiaCha(spread_base, Computed):
    field_name = u"进口价差"
    col_name = u"棉花进口价差"   
    def get_ts_whole_progress(self):
        relevant_col_list = [u"郑棉期货结算价(连续)", u"进口棉花价格指数(FC_Index)_M_滑准税提货价"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"郑棉期货结算价(连续)"] - tmp_total[u"进口棉花价格指数(FC_Index)_M_滑准税提货价"]
        return tmp_total 

###########################################################################################################################
""" CY-CF价差 """ 

class CY_CF1YueJiaCha(spread_base, Computed):
    field_name = u"CY-CF价差"
    col_name = u"CY-CF1月价差"
    axhline = 0
    def get_ts_whole_progress(self):
        relevant_col_list = [u"CY01合约收盘价", "CF01合约收盘价"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"CY01合约收盘价"] - tmp_total[u"CF01合约收盘价"]
        return tmp_total
    
    def seasonal_plot(self, title=None, start_year=None, axhline=None):
        tmp_df_interpolated, fig, axis = super(CY_CF1YueJiaCha, self).seasonal_plot(title=self.col_name, axhline=self.axhline)
        axis = Plot_Base.add_month_span(axis, tmp_df_interpolated, 1)
        return tmp_df_interpolated, fig, axis

class CY_CF5YueJiaCha(spread_base, Computed):
    field_name = u"CY-CF价差"
    col_name = u"CY-CF5月价差"
    axhline = 0
    def get_ts_whole_progress(self):
        relevant_col_list = [u"CY05合约收盘价", "CF05合约收盘价"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"CY05合约收盘价"] - tmp_total[u"CF05合约收盘价"]
        return tmp_total
    
    def seasonal_plot(self, title=None, start_year=None, axhline=None):
        tmp_df_interpolated, fig, axis = super(CY_CF5YueJiaCha, self).seasonal_plot(title=self.col_name, axhline=self.axhline)
        axis = Plot_Base.add_month_span(axis, tmp_df_interpolated, 1)
        return tmp_df_interpolated, fig, axis
    
class CY_CF9YueJiaCha(spread_base, Computed):
    field_name = u"CY-CF价差"
    col_name = u"CY-CF9月价差"
    axhline = 0
    def get_ts_whole_progress(self):
        relevant_col_list = [u"CY09合约收盘价", "CF09合约收盘价"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"CY09合约收盘价"] - tmp_total[u"CF09合约收盘价"]
        return tmp_total
    
    def seasonal_plot(self, title=None, start_year=None, axhline=None):
        tmp_df_interpolated, fig, axis = super(CY_CF9YueJiaCha, self).seasonal_plot(title=self.col_name, axhline=self.axhline)
        axis = Plot_Base.add_month_span(axis, tmp_df_interpolated, 1)
        return tmp_df_interpolated, fig, axis

    
if __name__ == "__main__":
    ts = CF1_5JiaCha().seasonal_plot()
    
    
    
    
    
    
    
    
    
    
    
    
    