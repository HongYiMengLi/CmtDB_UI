# -*- coding: utf-8 -*-
"""
Created on Wed Aug 29 13:36:18 2018

@author: Administrator
"""

import pandas as pd
from datetime import datetime
from .PP_Base import PP_Base
from . import PP_SpotPrice
from ..L import L_SpotPrice
from . import PP_Macro
from . import PP_Others
from ...Base.Spread_Generate import main_month_quote_2_spread_series
from ...Base.DataType_Base import Manual, Computed, WindData
from ...Base.Plot_Base import Plot_Base
from matplotlib.ticker import FuncFormatter

class spread_base(PP_Base, Plot_Base):
    table_english_name = "Spread"
    table_chinese_name = u"价差"
#    original_db_filepath = data_path + u"LPP价格数据库.xlsx"
    
    def output(self):
        print("Spread")
    
    def get_relevant_df(self, col_list):
        ts_list = [eval(PP_Base.get_table_class_full_variable(x))().get_ts() for x in col_list]
        tmp_table_df = pd.concat(ts_list, axis=1).dropna(how="all")
        return tmp_table_df  
    
###########################################################################################################################
""" 非标价差 """ 
""" 计算指标 """
    
class PPZhuSuMinusPPLaSi(spread_base, Computed):
    field_name = u"非标价差"
    col_name = u"PP注塑-PP拉丝"
    axhline = 0
    start_year = 2016
    def get_ts_whole_progress(self):
        relevant_col_list = [u"PP注塑价格_华东", u"PP拉丝价格_华东"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"PP注塑价格_华东"] - tmp_total[u"PP拉丝价格_华东"]
        return tmp_total
    
class PPDiRongGongBingMinusPPLaSi(spread_base, Computed):
    field_name = u"非标价差"
    col_name = u"PP低融共丙-PP拉丝"
    axhline = 0
    start_year = 2015
    def get_ts_whole_progress(self):
        relevant_col_list = [u"PP低融共丙_华东", u"PP拉丝价格_华东"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"PP低融共丙_华东"] - tmp_total[u"PP拉丝价格_华东"]
        return tmp_total
    
class PPLiMinusFen_HuaBei(spread_base, Computed):
    field_name = u"非标价差"
    col_name = u"PP粒-粉_华北"
    axhline = 0
    start_year = 2016
    def get_ts_whole_progress(self):
        relevant_col_list = [u"PP拉丝价格_华北", u"PP粉料价格_京博"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"PP拉丝价格_华北"] - tmp_total[u"PP粉料价格_京博"]
        return tmp_total
    
class PPLiMinusFen_HuaDong(spread_base, Computed):
    field_name = u"非标价差"
    col_name = u"PP粒-粉_华东"
    axhline = 0
    start_year = 2016
    def get_ts_whole_progress(self):
        relevant_col_list = [u"PP拉丝价格_华东", u"PP粉料价格_华东"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"PP拉丝价格_华东"] - tmp_total[u"PP粉料价格_华东"]
        return tmp_total
    
class HDZhuSUMinusPPDiRongGongBing(spread_base, Computed):
    field_name = u"非标价差"
    col_name = u"HD注塑-PP低融共丙"
    axhline = 0
    start_year = 2016
    def get_ts_whole_progress(self):
        relevant_col_list = [u"PP低融共丙_华东"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_series = L_SpotPrice.HDZhuSu().get_ts()
        tmp_total = pd.concat([tmp_total, tmp_series], axis=1)
        tmp_total[self.col_name] = tmp_total[u"HD注塑价格_华东"] - tmp_total[u"PP低融共丙_华东"]
        return tmp_total
    
        
###########################################################################################################################
""" 废料价差 """ 
""" 计算指标 """

class PP_XinLiaoMinusJiuLiao(spread_base, Computed):
    field_name = u"废料价差"
    col_name = u"PP:新料-废料"
    def get_ts_whole_progress(self):
        relevant_col_list = [u"PP拉丝价格_华北", u"废料价格_河北文安"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"PP拉丝价格_华北"] - tmp_total[u"废料价格_河北文安"]
        return tmp_total

###########################################################################################################################
""" 基差(计算指标) """ 
def month_quote_df_2_series(df):
    ts_list = []
    for col in df.columns.tolist():
        tmp_series = df[col].dropna()
        ts_list.append(tmp_series)
    result = pd.concat(ts_list)
    result = result[~result.index.duplicated()]
    return result

class PPBasis1(spread_base, Computed):
    field_name = u"基差"
    col_name = u"PP1月基差"
    axhline = 0
    def get_ts_whole_progress(self):
        relevant_col_list = [u"PP拉丝价格_华东"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        quote_df = PP_Base.get_PP_quote_df(month=1)
        quote_ts = month_quote_df_2_series(quote_df)
        quote_ts.name = u"PP1月期货价格"
        tmp_total = pd.concat([tmp_total, quote_ts], axis=1)
        tmp_total[self.col_name] = tmp_total[u"PP拉丝价格_华东"] - tmp_total[u"PP1月期货价格"]
        return tmp_total
    
    def seasonal_plot(self, title=None, start_year=None, axhline=None):
        tmp_df_interpolated, fig, axis = super(PPBasis1, self).seasonal_plot(title=self.col_name, axhline=self.axhline, date_constraint=[1, 17])
        axis = Plot_Base.add_month_span(axis, tmp_df_interpolated, 1)
        return tmp_df_interpolated, fig, axis

class PPBasis5(spread_base, Computed):
    field_name = u"基差"
    col_name = u"PP5月基差"
    axhline = 0
    def get_ts_whole_progress(self):
        relevant_col_list = [u"PP拉丝价格_华东"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        quote_df = PP_Base.get_PP_quote_df(month=5)
        quote_ts = month_quote_df_2_series(quote_df)
        quote_ts.name = u"PP5月期货价格"
        tmp_total = pd.concat([tmp_total, quote_ts], axis=1)
        tmp_total[self.col_name] = tmp_total[u"PP拉丝价格_华东"] - tmp_total[u"PP5月期货价格"]
        return tmp_total

    def seasonal_plot(self, title=None, start_year=None, axhline=None):
        tmp_df_interpolated, fig, axis = super(PPBasis5, self).seasonal_plot(title=self.col_name, axhline=self.axhline, date_constraint=[5, 17])
        axis = Plot_Base.add_month_span(axis, tmp_df_interpolated, 5)
        return tmp_df_interpolated, fig, axis

class PPBasis9(spread_base, Computed):
    field_name = u"基差"
    col_name = u"PP9月基差"
    axhline = 0
    def get_ts_whole_progress(self):
        relevant_col_list = [u"PP拉丝价格_华东"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        quote_df = PP_Base.get_PP_quote_df(month=9)
        quote_ts = month_quote_df_2_series(quote_df)
        quote_ts.name = u"PP9月期货价格"
        tmp_total = pd.concat([tmp_total, quote_ts], axis=1)
        tmp_total[self.col_name] = tmp_total[u"PP拉丝价格_华东"] - tmp_total[u"PP9月期货价格"]
        return tmp_total

    def seasonal_plot(self, title=None, start_year=None, axhline=None):
        tmp_df_interpolated, fig, axis = super(PPBasis9, self).seasonal_plot(title=self.col_name, axhline=self.axhline, date_constraint=[9, 17])
        axis = Plot_Base.add_month_span(axis, tmp_df_interpolated, 9)
        return tmp_df_interpolated, fig, axis

###########################################################################################################################
""" 月间价差(计算指标) """ 

class PPSpread1_5(spread_base, Computed):
    field_name = u"月间价差"
    col_name = u"PP1_5价差"
    axhline = 0
    start_year = 2015
    def get_ts_whole_progress(self):
        month_list = ["01", "05"]
        all_main_quote_df = PP_Base.get_PP_main_month_quote_df()
        spread_series = main_month_quote_2_spread_series(month_list, all_main_quote_df)
        tmp_df = pd.DataFrame([spread_series], index=[self.col_name]).T
        return tmp_df

    def seasonal_plot(self, title=None, start_year=None, axhline=None):
        tmp_df_interpolated, fig, axis = super(PPSpread1_5, self).seasonal_plot(title=self.col_name, start_year = self.start_year, 
                                              axhline=self.axhline, date_constraint=[1, 17])
        axis = Plot_Base.add_month_span(axis, tmp_df_interpolated, 1)
        return tmp_df_interpolated, fig, axis    
      

class PPSpread5_9(spread_base, Computed):
    field_name = u"月间价差"
    col_name = u"PP5_9价差"
    axhline = 0
    start_year = 2015
    def get_ts_whole_progress(self):
        month_list = ["05", "09"]
        all_main_quote_df = PP_Base.get_PP_main_month_quote_df()
        spread_series = main_month_quote_2_spread_series(month_list, all_main_quote_df)
        tmp_df = pd.DataFrame([spread_series], index=[self.col_name]).T
        return tmp_df

    def seasonal_plot(self, title=None, start_year=None, axhline=None):
        tmp_df_interpolated, fig, axis = super(PPSpread5_9, self).seasonal_plot(title=self.col_name, start_year = self.start_year, 
                                              axhline=self.axhline, date_constraint=[5, 17])
        axis = Plot_Base.add_month_span(axis, tmp_df_interpolated, 5)
        return tmp_df_interpolated, fig, axis   

class PPSpread9_1(spread_base, Computed):
    field_name = u"月间价差"
    col_name = u"PP9_1价差"
    axhline = 0
    start_year = 2018
    def get_ts_whole_progress(self):
        month_list = ["09", "01"]
        all_main_quote_df = PP_Base.get_PP_main_month_quote_df()
        spread_series = main_month_quote_2_spread_series(month_list, all_main_quote_df)
        tmp_df = pd.DataFrame([spread_series], index=[self.col_name]).T
        return tmp_df

    def seasonal_plot(self, title=None, start_year=None, axhline=None):
        tmp_df_interpolated, fig, axis = super(PPSpread9_1, self).seasonal_plot(title=self.col_name, start_year = self.start_year, 
                                              axhline=self.axhline, date_constraint=[9, 17])
        axis = Plot_Base.add_month_span(axis, tmp_df_interpolated, 9)
        return tmp_df_interpolated, fig, axis



if __name__ == "__main__":
    ts = PPSpread5_9().seasonal_plot()
























