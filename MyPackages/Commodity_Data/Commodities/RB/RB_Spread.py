# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 10:48:24 2018

@author: 李弘一萌
"""

import pandas as pd
from datetime import datetime
from .RB_Base import RB_Base
from . import RB_SpotPrice, RB_Upstream, RB_FuturesPrice, RB_Macro
from ...Base.Spread_Generate import main_month_quote_2_spread_series
from ...Base.DataType_Base import Manual, Computed, WindData
from ...Base.Plot_Base import Plot_Base
from matplotlib.ticker import FuncFormatter

class spread_base(RB_Base, Plot_Base):
    table_english_name = "Spread"
    table_chinese_name = u"价差"
#    original_db_filepath = data_path + u"LPP价格数据库.xlsx"
    
    def output(self):
        print("Spread")
    
    def get_relevant_df(self, col_list):
        ts_list = [eval(RB_Base.get_table_class_full_variable(x))().get_ts() for x in col_list]
        tmp_table_df = pd.concat(ts_list, axis=1).dropna(how="all")
        return tmp_table_df  
    

    
###########################################################################################################################
""" 基差(计算指标) """ 


class LuoWenJiCha_01HeYue(spread_base, Computed):
    field_name = u"基差"
    col_name = u"螺纹基差_01合约"
    axhline = 0
    def get_ts_whole_progress(self):
        relevant_col_list = [u"螺纹钢现货价格_HRB400_20mm_上海", u"螺纹钢现货价格_HRB400_20mm_天津", u"螺纹钢现货价格_HRB400_20mm_杭州"
                             , u"螺纹钢现货价格_HRB400_20mm_广州", u"RB01合约收盘价"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[u"螺纹钢现货价格_HRB400_20mm_上海"] = tmp_total[u"螺纹钢现货价格_HRB400_20mm_上海"] / 0.97
        tmp_total[u"螺纹钢现货价格_HRB400_20mm_天津"] = tmp_total[u"螺纹钢现货价格_HRB400_20mm_天津"] / 0.97
        tmp_total[u"螺纹钢现货价格_HRB400_20mm_杭州"] = tmp_total[u"螺纹钢现货价格_HRB400_20mm_杭州"] / 0.97
        tmp_total[u"基准价"] = tmp_total[[u"螺纹钢现货价格_HRB400_20mm_上海", u"螺纹钢现货价格_HRB400_20mm_天津", u"螺纹钢现货价格_HRB400_20mm_杭州"
                                         , u"螺纹钢现货价格_HRB400_20mm_广州"]].min(axis=1)
        tmp_total[self.col_name] = tmp_total[u"基准价"] - tmp_total[u"RB01合约收盘价"]
        return tmp_total
    
    def seasonal_plot(self, title=None, start_year=None, axhline=None):
        tmp_df_interpolated, fig, axis = super(LuoWenJiCha_01HeYue, self).seasonal_plot(title=self.col_name, axhline=self.axhline, date_constraint=[1, 17])
        axis = Plot_Base.add_month_span(axis, tmp_df_interpolated, 1)
        return tmp_df_interpolated, fig, axis
    
class LuoWenJiCha_05HeYue(spread_base, Computed):
    field_name = u"基差"
    col_name = u"螺纹基差_05合约"
    axhline = 0
    def get_ts_whole_progress(self):
        relevant_col_list = [u"螺纹钢现货价格_HRB400_20mm_上海", u"螺纹钢现货价格_HRB400_20mm_天津", u"螺纹钢现货价格_HRB400_20mm_杭州"
                             , u"螺纹钢现货价格_HRB400_20mm_广州", u"RB05合约收盘价"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[u"螺纹钢现货价格_HRB400_20mm_上海"] = tmp_total[u"螺纹钢现货价格_HRB400_20mm_上海"] / 0.97
        tmp_total[u"螺纹钢现货价格_HRB400_20mm_天津"] = tmp_total[u"螺纹钢现货价格_HRB400_20mm_天津"] / 0.97
        tmp_total[u"螺纹钢现货价格_HRB400_20mm_杭州"] = tmp_total[u"螺纹钢现货价格_HRB400_20mm_杭州"] / 0.97
        tmp_total[u"基准价"] = tmp_total[[u"螺纹钢现货价格_HRB400_20mm_上海", u"螺纹钢现货价格_HRB400_20mm_天津", u"螺纹钢现货价格_HRB400_20mm_杭州"
                                         , u"螺纹钢现货价格_HRB400_20mm_广州"]].min(axis=1)
        tmp_total[self.col_name] = tmp_total[u"基准价"] - tmp_total[u"RB05合约收盘价"]
        return tmp_total
    
    def seasonal_plot(self, title=None, start_year=None, axhline=None):
        tmp_df_interpolated, fig, axis = super(LuoWenJiCha_05HeYue, self).seasonal_plot(title=self.col_name, axhline=self.axhline, date_constraint=[5, 17])
        axis = Plot_Base.add_month_span(axis, tmp_df_interpolated, 5)
        return tmp_df_interpolated, fig, axis

class LuoWenJiCha_10HeYue(spread_base, Computed):
    field_name = u"基差"
    col_name = u"螺纹基差_10合约"
    axhline = 0
    def get_ts_whole_progress(self):
        relevant_col_list = [u"螺纹钢现货价格_HRB400_20mm_上海", u"螺纹钢现货价格_HRB400_20mm_天津", u"螺纹钢现货价格_HRB400_20mm_杭州"
                             , u"螺纹钢现货价格_HRB400_20mm_广州", u"RB10合约收盘价"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[u"螺纹钢现货价格_HRB400_20mm_上海"] = tmp_total[u"螺纹钢现货价格_HRB400_20mm_上海"] / 0.97
        tmp_total[u"螺纹钢现货价格_HRB400_20mm_天津"] = tmp_total[u"螺纹钢现货价格_HRB400_20mm_天津"] / 0.97
        tmp_total[u"螺纹钢现货价格_HRB400_20mm_杭州"] = tmp_total[u"螺纹钢现货价格_HRB400_20mm_杭州"] / 0.97
        tmp_total[u"基准价"] = tmp_total[[u"螺纹钢现货价格_HRB400_20mm_上海", u"螺纹钢现货价格_HRB400_20mm_天津", u"螺纹钢现货价格_HRB400_20mm_杭州"
                                         , u"螺纹钢现货价格_HRB400_20mm_广州"]].min(axis=1)
        tmp_total[self.col_name] = tmp_total[u"基准价"] - tmp_total[u"RB10合约收盘价"]
        return tmp_total
    
    def seasonal_plot(self, title=None, start_year=None, axhline=None):
        tmp_df_interpolated, fig, axis = super(LuoWenJiCha_01HeYue, self).seasonal_plot(title=self.col_name, axhline=self.axhline, date_constraint=[10, 17])
        axis = Plot_Base.add_month_span(axis, tmp_df_interpolated, 1)
        return tmp_df_interpolated, fig, axis
    
    
###########################################################################################################################
""" 月间价差(计算指标) """ 

class LuoWenQiHuoJiaCha_1_5(spread_base, Computed):
    field_name = u"月间价差"
    col_name = u"螺纹期货价差_1-5"
    axhline = 0
    start_year = 2015
    def get_ts_whole_progress(self):
        month_list = ["01", "05"]
        all_main_quote_df = RB_Base.get_RB_main_month_quote_df()
        spread_series = main_month_quote_2_spread_series(month_list, all_main_quote_df)
        tmp_df = pd.DataFrame([spread_series], index=[self.col_name]).T
        return tmp_df

    def seasonal_plot(self, title=None, start_year=None, axhline=None):
        tmp_df_interpolated, fig, axis = super(LuoWenQiHuoJiaCha_1_5, self).seasonal_plot(title=self.col_name, start_year = self.start_year, 
                                              axhline=self.axhline, date_constraint=[1, 17])
        axis = Plot_Base.add_month_span(axis, tmp_df_interpolated, 1)
        return tmp_df_interpolated, fig, axis    
      

class LuoWenQiHuoJiaCha_5_10(spread_base, Computed):
    field_name = u"月间价差"
    col_name = u"螺纹期货价差_5-10"
    axhline = 0
    start_year = 2015
    def get_ts_whole_progress(self):
        month_list = ["05", "10"]
        all_main_quote_df = RB_Base.get_RB_main_month_quote_df()
        spread_series = main_month_quote_2_spread_series(month_list, all_main_quote_df)
        tmp_df = pd.DataFrame([spread_series], index=[self.col_name]).T
        return tmp_df

    def seasonal_plot(self, title=None, start_year=None, axhline=None):
        tmp_df_interpolated, fig, axis = super(LuoWenQiHuoJiaCha_5_10, self).seasonal_plot(title=self.col_name, start_year = self.start_year, 
                                              axhline=self.axhline, date_constraint=[5, 17])
        axis = Plot_Base.add_month_span(axis, tmp_df_interpolated, 5)
        return tmp_df_interpolated, fig, axis   

class LuoWenQiHuoJiaCha_10_1(spread_base, Computed):
    field_name = u"月间价差"
    col_name = u"螺纹期货价差_10-1"
    axhline = 0
    start_year = 2015
    def get_ts_whole_progress(self):
        month_list = ["10", "01"]
        all_main_quote_df = RB_Base.get_RB_main_month_quote_df()
        spread_series = main_month_quote_2_spread_series(month_list, all_main_quote_df)
        tmp_df = pd.DataFrame([spread_series], index=[self.col_name]).T
        return tmp_df

    def seasonal_plot(self, title=None, start_year=None, axhline=None):
        tmp_df_interpolated, fig, axis = super(LuoWenQiHuoJiaCha_10_1, self).seasonal_plot(title=self.col_name, start_year = self.start_year, 
                                              axhline=self.axhline, date_constraint=[10, 17])
        axis = Plot_Base.add_month_span(axis, tmp_df_interpolated, 10)
        return tmp_df_interpolated, fig, axis


###########################################################################################################################
""" 现货价差(计算指标) """ 

class LuoWenXianHuoJiaCha_ShangHaiMinusTianJin(spread_base, Computed):
    field_name = u"现货价差"
    col_name = u"螺纹现货价差_上海-天津"
    axhline = 0
    def get_ts_whole_progress(self):
        relevant_col_list = [u"螺纹钢现货价格_HRB400_20mm_上海", "螺纹钢现货价格_HRB400_20mm_天津"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = (tmp_total[u"螺纹钢现货价格_HRB400_20mm_上海"] - tmp_total[u"螺纹钢现货价格_HRB400_20mm_天津"]) / 0.97
        return tmp_total


class LuoWenXianHuoJiaCha_ShangHaiMinusGuangZhou(spread_base, Computed):
    field_name = u"现货价差"
    col_name = u"螺纹现货价差_上海-广州"
    axhline = 0
    def get_ts_whole_progress(self):
        relevant_col_list = [u"螺纹钢现货价格_HRB400_20mm_上海", "螺纹钢现货价格_HRB400_20mm_广州"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"螺纹钢现货价格_HRB400_20mm_上海"] / 0.97 - tmp_total[u"螺纹钢现货价格_HRB400_20mm_广州"]
        return tmp_total
















if __name__ == "__main__":
#    df = PRBSpread9_1().get_ts()
    df, fig, axis = LuoWenQiHuoJiaCha_1_5().seasonal_plot()
    
    
    
    
    
    
    
    
    
    
    
    
    
    