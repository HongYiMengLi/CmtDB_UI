# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 10:48:24 2018

@author: 李弘一萌
"""

import pandas as pd
from datetime import datetime
from .HC_Base import HC_Base
from . import HC_SpotPrice, HC_Upstream, HC_FuturesPrice, HC_Macro
from ...Base.Spread_Generate import main_month_quote_2_spread_series
from ...Base.DataType_Base import Manual, Computed, WindData
from ...Base.Plot_Base import Plot_Base
from matplotlib.ticker import FuncFormatter

class spread_base(HC_Base, Plot_Base):
    table_english_name = "Spread"
    table_chinese_name = u"价差"
#    original_db_filepath = data_path + u"LPP价格数据库.xlsx"
    
    def output(self):
        print("Spread")
    
    def get_relevant_df(self, col_list):
        ts_list = [eval(HC_Base.get_table_class_full_variable(x))().get_ts() for x in col_list]
        tmp_table_df = pd.concat(ts_list, axis=1).dropna(how="all")
        return tmp_table_df  
    

    
###########################################################################################################################
""" 基差(计算指标) """ 


class ReJuanJiCha_01HeYue(spread_base, Computed):
    field_name = u"基差"
    col_name = u"热卷基差_01合约"
    axhline = 0
    def get_ts_whole_progress(self):
        relevant_col_list = [u"热卷现货价格_Q235B_4.75mm_天津", u"热卷现货价格_Q235B_4.75mm_武汉", u"热卷现货价格_Q235B_4.75mm_上海"
                             , u"热卷现货价格_Q235B_4.75mm_杭州", u"热卷现货价格_Q235B_4.75mm_广州", u"HC01合约收盘价"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[u"热卷现货价格_Q235B_4.75mm_天津"] = tmp_total[u"热卷现货价格_Q235B_4.75mm_天津"] + 90
        tmp_total[u"热卷现货价格_Q235B_4.75mm_武汉"] = tmp_total[u"热卷现货价格_Q235B_4.75mm_武汉"] + 70
        tmp_total[u"基准价"] = tmp_total[[u"热卷现货价格_Q235B_4.75mm_天津", u"热卷现货价格_Q235B_4.75mm_武汉", u"热卷现货价格_Q235B_4.75mm_上海"
                                         , u"热卷现货价格_Q235B_4.75mm_杭州", u"热卷现货价格_Q235B_4.75mm_广州"]].min(axis=1)
        tmp_total[self.col_name] = tmp_total[u"基准价"] - tmp_total[u"HC01合约收盘价"]
        return tmp_total
    
    def seasonal_plot(self, title=None, start_year=None, axhline=None):
        tmp_df_interpolated, fig, axis = super(ReJuanJiCha_01HeYue, self).seasonal_plot(title=self.col_name, axhline=self.axhline, date_constraint=[1, 17])
        axis = Plot_Base.add_month_span(axis, tmp_df_interpolated, 1)
        return tmp_df_interpolated, fig, axis
    
class ReJuanJiCha_05HeYue(spread_base, Computed):
    field_name = u"基差"
    col_name = u"热卷基差_05合约"
    axhline = 0
    def get_ts_whole_progress(self):
        relevant_col_list = [u"热卷现货价格_Q235B_4.75mm_天津", u"热卷现货价格_Q235B_4.75mm_武汉", u"热卷现货价格_Q235B_4.75mm_上海"
                             , u"热卷现货价格_Q235B_4.75mm_杭州", u"热卷现货价格_Q235B_4.75mm_广州", u"HC05合约收盘价"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[u"热卷现货价格_Q235B_4.75mm_天津"] = tmp_total[u"热卷现货价格_Q235B_4.75mm_天津"] + 90
        tmp_total[u"热卷现货价格_Q235B_4.75mm_武汉"] = tmp_total[u"热卷现货价格_Q235B_4.75mm_武汉"] + 70
        tmp_total[u"基准价"] = tmp_total[[u"热卷现货价格_Q235B_4.75mm_天津", u"热卷现货价格_Q235B_4.75mm_武汉", u"热卷现货价格_Q235B_4.75mm_上海"
                                         , u"热卷现货价格_Q235B_4.75mm_杭州", u"热卷现货价格_Q235B_4.75mm_广州"]].min(axis=1)
        tmp_total[self.col_name] = tmp_total[u"基准价"] - tmp_total[u"HC05合约收盘价"]
        return tmp_total
    
    def seasonal_plot(self, title=None, start_year=None, axhline=None):
        tmp_df_interpolated, fig, axis = super(ReJuanJiCha_05HeYue, self).seasonal_plot(title=self.col_name, axhline=self.axhline, date_constraint=[5, 17])
        axis = Plot_Base.add_month_span(axis, tmp_df_interpolated, 5)
        return tmp_df_interpolated, fig, axis

class ReJuanJiCha_10HeYue(spread_base, Computed):
    field_name = u"基差"
    col_name = u"热卷基差_10合约"
    axhline = 0
    def get_ts_whole_progress(self):
        relevant_col_list = [u"热卷现货价格_Q235B_4.75mm_天津", u"热卷现货价格_Q235B_4.75mm_武汉", u"热卷现货价格_Q235B_4.75mm_上海"
                             , u"热卷现货价格_Q235B_4.75mm_杭州", u"热卷现货价格_Q235B_4.75mm_广州", u"HC10合约收盘价"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[u"热卷现货价格_Q235B_4.75mm_天津"] = tmp_total[u"热卷现货价格_Q235B_4.75mm_天津"] + 90
        tmp_total[u"热卷现货价格_Q235B_4.75mm_武汉"] = tmp_total[u"热卷现货价格_Q235B_4.75mm_武汉"] + 70
        tmp_total[u"基准价"] = tmp_total[[u"热卷现货价格_Q235B_4.75mm_天津", u"热卷现货价格_Q235B_4.75mm_武汉", u"热卷现货价格_Q235B_4.75mm_上海"
                                         , u"热卷现货价格_Q235B_4.75mm_杭州", u"热卷现货价格_Q235B_4.75mm_广州"]].min(axis=1)
        tmp_total[self.col_name] = tmp_total[u"基准价"] - tmp_total[u"HC10合约收盘价"]
        return tmp_total
    
    def seasonal_plot(self, title=None, start_year=None, axhline=None):
        tmp_df_interpolated, fig, axis = super(ReJuanJiCha_10HeYue, self).seasonal_plot(title=self.col_name, axhline=self.axhline, date_constraint=[10, 17])
        axis = Plot_Base.add_month_span(axis, tmp_df_interpolated, 10)
        return tmp_df_interpolated, fig, axis
    
    
###########################################################################################################################
""" 月间价差(计算指标) """ 

class ReJuanHeYueJiaCha_1_5(spread_base, Computed):
    field_name = u"月间价差"
    col_name = u"热卷合约价差_1-5"
    axhline = 0
    start_year = 2015
    def get_ts_whole_progress(self):
        month_list = ["01", "05"]
        all_main_quote_df = HC_Base.get_HC_main_month_quote_df()
        spread_series = main_month_quote_2_spread_series(month_list, all_main_quote_df)
        tmp_df = pd.DataFrame([spread_series], index=[self.col_name]).T
        return tmp_df

    def seasonal_plot(self, title=None, start_year=None, axhline=None):
        tmp_df_interpolated, fig, axis = super(ReJuanHeYueJiaCha_1_5, self).seasonal_plot(title=self.col_name, start_year = self.start_year, 
                                              axhline=self.axhline, date_constraint=[1, 17])
        axis = Plot_Base.add_month_span(axis, tmp_df_interpolated, 1)
        return tmp_df_interpolated, fig, axis    
      

class ReJuanHeYueJiaCha_5_10(spread_base, Computed):
    field_name = u"月间价差"
    col_name = u"热卷合约价差_5-10"
    axhline = 0
    start_year = 2015
    def get_ts_whole_progress(self):
        month_list = ["05", "10"]
        all_main_quote_df = HC_Base.get_HC_main_month_quote_df()
        spread_series = main_month_quote_2_spread_series(month_list, all_main_quote_df)
        tmp_df = pd.DataFrame([spread_series], index=[self.col_name]).T
        return tmp_df

    def seasonal_plot(self, title=None, start_year=None, axhline=None):
        tmp_df_interpolated, fig, axis = super(ReJuanHeYueJiaCha_5_10, self).seasonal_plot(title=self.col_name, start_year = self.start_year, 
                                              axhline=self.axhline, date_constraint=[5, 17])
        axis = Plot_Base.add_month_span(axis, tmp_df_interpolated, 5)
        return tmp_df_interpolated, fig, axis   

class ReJuanHeYueJiaCha_10_1(spread_base, Computed):
    field_name = u"月间价差"
    col_name = u"热卷合约价差_10-1"
    axhline = 0
    start_year = 2015
    def get_ts_whole_progress(self):
        month_list = ["10", "01"]
        all_main_quote_df = HC_Base.get_HC_main_month_quote_df()
        spread_series = main_month_quote_2_spread_series(month_list, all_main_quote_df)
        tmp_df = pd.DataFrame([spread_series], index=[self.col_name]).T
        return tmp_df

    def seasonal_plot(self, title=None, start_year=None, axhline=None):
        tmp_df_interpolated, fig, axis = super(ReJuanHeYueJiaCha_10_1, self).seasonal_plot(title=self.col_name, start_year = self.start_year, 
                                              axhline=self.axhline, date_constraint=[10, 17])
        axis = Plot_Base.add_month_span(axis, tmp_df_interpolated, 10)
        return tmp_df_interpolated, fig, axis


###########################################################################################################################
""" 产品间价差(计算指标) """ 

class LengJuanReJuanJiaCha_ShangHai(spread_base, Computed):
    field_name = u"产品间价差"
    col_name = u"冷卷热卷价差_上海"
    axhline = 0
    def get_ts_whole_progress(self):
        relevant_col_list = [u"冷卷现货价格_1.0mm_上海", "热卷现货价格_Q235B_4.75mm_上海"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"冷卷现货价格_1.0mm_上海"] - tmp_total[u"热卷现货价格_Q235B_4.75mm_上海"]
        return tmp_total


class DuXinJuanReJuanJiaCha_ShangHai(spread_base, Computed):
    field_name = u"产品间价差"
    col_name = u"镀锌卷热卷价差_上海"
    axhline = 0
    def get_ts_whole_progress(self):
        relevant_col_list = [u"镀锌板卷现货价格_0.5mm_上海", "热卷现货价格_Q235B_4.75mm_上海"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"镀锌板卷现货价格_0.5mm_上海"] - tmp_total[u"热卷现货价格_Q235B_4.75mm_上海"]
        return tmp_total

class ReJuanLuoWenXianHuoJiaCha_ShangHai(spread_base, Computed):
    field_name = u"产品间价差"
    col_name = u"热卷螺纹现货价差_上海"
    axhline = 0
    def get_ts_whole_progress(self):
        relevant_col_list = [u"镀锌板卷现货价格_0.5mm_上海", "热卷现货价格_Q235B_4.75mm_上海"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"镀锌板卷现货价格_0.5mm_上海"] - tmp_total[u"热卷现货价格_Q235B_4.75mm_上海"]
        return tmp_total
#    
#class ReJuanLuoWenZhuLiHeYueJiaCha(spread_base, Computed):
#    field_name = u"产品间价差"
#    col_name = u"热卷螺纹主力合约价差"
#    axhline = 0
#    def get_ts_whole_progress(self):
#        relevant_col_list = [u"镀锌板卷现货价格_0.5mm_上海", "热卷现货价格_Q235B_4.75mm_上海"]
#        tmp_total = self.get_relevant_df(relevant_col_list)
#        tmp_total[self.col_name] = tmp_total[u"镀锌板卷现货价格_0.5mm_上海"] - tmp_total[u"热卷现货价格_Q235B_4.75mm_上海"]
#        return tmp_total


###########################################################################################################################
""" 地域价差(计算指标) """ 

class ReJuanXianHuoJiaCha_ShangHai_TianJin(spread_base, Computed):
    field_name = u"地域价差"
    col_name = u"热卷现货价差_上海-天津"
    axhline = 0
    def get_ts_whole_progress(self):
        relevant_col_list = [u"热卷现货价格_Q235B_4.75mm_上海", "热卷现货价格_Q235B_4.75mm_天津"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"热卷现货价格_Q235B_4.75mm_上海"] - tmp_total[u"热卷现货价格_Q235B_4.75mm_天津"]
        return tmp_total

class ReJuanXianHuoJiaCha_ShangHai_GuangZhou(spread_base, Computed):
    field_name = u"地域价差"
    col_name = u"热卷现货价差_上海-广州"
    axhline = 0 
    def get_ts_whole_progress(self):
        relevant_col_list = [u"热卷现货价格_Q235B_4.75mm_上海", "热卷现货价格_Q235B_4.75mm_广州"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"热卷现货价格_Q235B_4.75mm_上海"] - tmp_total[u"热卷现货价格_Q235B_4.75mm_广州"]
        return tmp_total








if __name__ == "__main__":
#    df = PHCSpread9_1().get_ts()
    df, fig, axis = LuoWenQiHuoJiaCha_1_5().seasonal_plot()
    
    
    
    
    
    
    
    
    
    
    
    
    
    