# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 10:48:24 2018

@author: 李弘一萌
"""

import pandas as pd
from datetime import datetime
from .RU_Base import RU_Base
from . import RU_SpotPrice, RU_Upstream, RU_FuturesPrice, RU_Macro
from ...Base.Spread_Generate import main_month_quote_2_spread_series
from ...Base.DataType_Base import Manual, Computed, WindData
from ...Base.Plot_Base import Plot_Base
from matplotlib.ticker import FuncFormatter

class spread_base(RU_Base, Plot_Base):
    table_english_name = "Spread"
    table_chinese_name = u"价差"
#    original_db_filepath = data_path + u"LPP价格数据库.xlsx"
    
    def output(self):
        print("Spread")
    
    def get_relevant_df(self, col_list):
        ts_list = [eval(RU_Base.get_table_class_full_variable(x))().get_ts() for x in col_list]
        tmp_table_df = pd.concat(ts_list, axis=1).dropna(how="all")
        return tmp_table_df      

###########################################################################################################################
""" 合成胶价差 """ 

class QuanRu_ShunDingJiaCha(spread_base, Computed):
    field_name = u"合成胶价差"
    col_name = u"全乳_顺丁价差"
    def get_ts_whole_progress(self):
        relevant_col_list = [u"全乳胶价格_上海", "顺丁市场价格_华东"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"全乳胶价格_上海"] - tmp_total[u"顺丁市场价格_华东"]
        return tmp_total
    
class QuanRu_DingBenJiaCha(spread_base, Computed):
    field_name = u"合成胶价差"
    col_name = u"全乳_丁苯价差"
    def get_ts_whole_progress(self):
        relevant_col_list = [u"全乳胶价格_上海", "丁苯市场价格_华东"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"全乳胶价格_上海"] - tmp_total[u"丁苯市场价格_华东"]
        return tmp_total    
    
###########################################################################################################################
""" 基差(计算指标) """ 
    
class TianJiao1YueJiCha(spread_base, Computed):
    field_name = u"基差"
    col_name = u"天胶1月基差"
    axhline = 0
    def get_ts_whole_progress(self):
        relevant_col_list = [u"全乳胶价格_上海", "RU01合约收盘价"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"全乳胶价格_上海"] - tmp_total[u"RU01合约收盘价"]
        return tmp_total
    
    def seasonal_plot(self, title=None, start_year=None, axhline=None):
        tmp_df_interpolated, fig, axis = super(TianJiao1YueJiCha, self).seasonal_plot(title=self.col_name, axhline=self.axhline, date_constraint=[1, 17])
        axis = Plot_Base.add_month_span(axis, tmp_df_interpolated, 1)
        return tmp_df_interpolated, fig, axis


class TianJiao5YueJiCha(spread_base, Computed):
    field_name = u"基差"
    col_name = u"天胶5月基差"
    axhline = 0
    def get_ts_whole_progress(self):
        relevant_col_list = [u"全乳胶价格_上海", "RU05合约收盘价"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"全乳胶价格_上海"] - tmp_total[u"RU05合约收盘价"]
        return tmp_total
    
    def seasonal_plot(self, title=None, start_year=None, axhline=None):
        tmp_df_interpolated, fig, axis = super(TianJiao5YueJiCha, self).seasonal_plot(title=self.col_name, axhline=self.axhline, date_constraint=[5, 17])
        axis = Plot_Base.add_month_span(axis, tmp_df_interpolated, 5)
        return tmp_df_interpolated, fig, axis


class TianJiao9YueJiCha(spread_base, Computed):
    field_name = u"基差"
    col_name = u"天胶9月基差"
    axhline = 0
    def get_ts_whole_progress(self):
        relevant_col_list = [u"全乳胶价格_上海", "RU09合约收盘价"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"全乳胶价格_上海"] - tmp_total[u"RU09合约收盘价"]
        return tmp_total
    
    def seasonal_plot(self, title=None, start_year=None, axhline=None):
        tmp_df_interpolated, fig, axis = super(TianJiao9YueJiCha, self).seasonal_plot(title=self.col_name, axhline=self.axhline, date_constraint=[9, 17])
        axis = Plot_Base.add_month_span(axis, tmp_df_interpolated, 9)
        return tmp_df_interpolated, fig, axis
    
###########################################################################################################################
""" 美金胶价差(计算指标) """ 

class NeiWaiPanJiaCha(spread_base, Computed):
    field_name = u"美金胶价差"
    col_name = u"内外盘价差"
    def get_ts_whole_progress(self):
        relevant_col_list = [u"泰国3号烟片(RSS3)美金CIF价格", "泰国3号烟片(RSS3)保税区价格"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"泰国3号烟片(RSS3)美金CIF价格"] - tmp_total[u"泰国3号烟片(RSS3)保税区价格"]
        return tmp_total
    
###########################################################################################################################
""" 月间价差(计算指标) """ 

class TianJiao1_5JiaCha(spread_base, Computed):
    field_name = u"月间价差"
    col_name = u"天胶1_5价差"
    axhline = 0
    start_year = 2015
    def get_ts_whole_progress(self):
        month_list = ["01", "05"]
        all_main_quote_df = RU_Base.get_RU_main_month_quote_df()
        spread_series = main_month_quote_2_spread_series(month_list, all_main_quote_df)
        tmp_df = pd.DataFrame([spread_series], index=[self.col_name]).T
        return tmp_df

    def seasonal_plot(self, title=None, start_year=None, axhline=None):
        tmp_df_interpolated, fig, axis = super(TianJiao1_5JiaCha, self).seasonal_plot(title=self.col_name, start_year = self.start_year, 
                                              axhline=self.axhline, date_constraint=[1, 17])
        axis = Plot_Base.add_month_span(axis, tmp_df_interpolated, 1)
        return tmp_df_interpolated, fig, axis
        
class TianJiao5_9JiaCha(spread_base, Computed):
    field_name = u"月间价差"
    col_name = u"天胶5_9价差"
    axhline = 0
    start_year = 2015
    def get_ts_whole_progress(self):
        month_list = ["05", "09"]
        all_main_quote_df = RU_Base.get_RU_main_month_quote_df()
        spread_series = main_month_quote_2_spread_series(month_list, all_main_quote_df)
        tmp_df = pd.DataFrame([spread_series], index=[self.col_name]).T
        return tmp_df

    def seasonal_plot(self, title=None, start_year=None, axhline=None):
        tmp_df_interpolated, fig, axis = super(TianJiao5_9JiaCha, self).seasonal_plot(title=self.col_name, start_year = self.start_year, 
                                              axhline=self.axhline, date_constraint=[5, 17])
        axis = Plot_Base.add_month_span(axis, tmp_df_interpolated, 5)
        return tmp_df_interpolated, fig, axis    
      

class TianJiao9_1JiaCha(spread_base, Computed):
    field_name = u"月间价差"
    col_name = u"天胶9_1价差"
    axhline = 0
    start_year = 2015
    def get_ts_whole_progress(self):
        month_list = ["09", "01"]
        all_main_quote_df = RU_Base.get_RU_main_month_quote_df()
        spread_series = main_month_quote_2_spread_series(month_list, all_main_quote_df)
        tmp_df = pd.DataFrame([spread_series], index=[self.col_name]).T
        return tmp_df

    def seasonal_plot(self, title=None, start_year=None, axhline=None):
        tmp_df_interpolated, fig, axis = super(TianJiao9_1JiaCha, self).seasonal_plot(title=self.col_name, start_year = self.start_year, 
                                              axhline=self.axhline, date_constraint=[9, 17])
        axis = Plot_Base.add_month_span(axis, tmp_df_interpolated, 9)
        return tmp_df_interpolated, fig, axis  
        





if __name__ == "__main__":
    ts = TianJiao1_5JiaCha().seasonal_plot()
    
    
    
    
    
    
    
    
    
    
    
    
    