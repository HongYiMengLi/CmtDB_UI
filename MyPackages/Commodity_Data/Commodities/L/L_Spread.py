# -*- coding: utf-8 -*-
"""
Created on Mon Aug 27 08:35:42 2018

@author: 李弘一萌
"""

import pandas as pd
from datetime import datetime
from .L_Base import L_Base
from . import L_SpotPrice, L_Macro, L_Others
from ..PP import PP_SpotPrice
from ...Base.Spread_Generate import main_month_quote_2_spread_series
from ...Base.DataType_Base import Manual, Computed, WindData
from ...Base.Plot_Base import Plot_Base
from matplotlib.ticker import FuncFormatter

class spread_base(L_Base, Plot_Base):
    table_english_name = "Spread"
    table_chinese_name = u"价差"
#    original_db_filepath = data_path + u"LPP价格数据库.xlsx"
    
    def output(self):
        print("Spread")
    
    def get_relevant_df(self, col_list):
        ts_list = [eval(L_Base.get_table_class_full_variable(x))().get_ts() for x in col_list]
        tmp_table_df = pd.concat(ts_list, axis=1).dropna(how="all")
        return tmp_table_df  

###########################################################################################################################
""" 非标价差 """ 

""" 计算指标 """

class LDMoMinusLLDMo(spread_base, Computed):
    field_name = u"PEPP国内现货"
    col_name = u"LD膜-LLD膜"
    axhline = 0
    start_year = 2015
    def get_ts_whole_progress(self):
        relevant_col_list = [u"LD膜料价格_华东", u"LLD膜价格_华东(煤化工)"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"LD膜料价格_华东"] - tmp_total[u"LLD膜价格_华东(煤化工)"]
        return tmp_total
    
class HDZhuSuMinusLLDMo(spread_base, Computed):
    field_name = u"PEPP国内现货"
    col_name = u"HD注塑-LLD膜"
    axhline = 0
    start_year = 2015
    def get_ts_whole_progress(self):
        relevant_col_list = [u"HD注塑价格_华东", u"LLD膜价格_华东(煤化工)"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"HD注塑价格_华东"] - tmp_total[u"LLD膜价格_华东(煤化工)"]
        return tmp_total   
    
class HDZhuSUMinusPPDiRongGongBing(spread_base, Computed):
    field_name = u"PEPP国内现货"
    col_name = u"HD注塑-PP低融共丙"
    axhline = 0
    start_year = 2016
    def get_ts_whole_progress(self):
        relevant_col_list = [u"HD注塑价格_华东"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_series = PP_SpotPrice.PPDiRongGongBing().get_ts()
        tmp_total = pd.concat([tmp_total, tmp_series], axis=1)
        tmp_total[self.col_name] = tmp_total[u"HD注塑价格_华东"] - tmp_total[u"PP低融共丙_华东"]
        return tmp_total    


        
###########################################################################################################################
""" 废料价差 """     
""" 计算指标 """
 
class PE_XinLiaoMinusJiuLiao(spread_base, Computed):
    field_name = u"废料价格"
    col_name = u"PE:新料-废料"
    def get_ts_whole_progress(self):
        relevant_col_list = [u"LLD膜价格_华北", u"LDPE废料_莱州/莒县EVA"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"LLD膜价格_华北"] - tmp_total[u"LDPE废料_莱州/莒县EVA"]
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

    
class LBasis1(spread_base, Computed):
    field_name = u"基差"
    col_name = u"L1月基差"
    axhline = 0
    def get_ts_whole_progress(self):
        relevant_col_list = [u"LLD膜价格_华北"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        quote_df = L_Base.get_L_quote_df(month=1)
        quote_ts = month_quote_df_2_series(quote_df)
        quote_ts.name = u"L1月期货价格"
        tmp_total = pd.concat([tmp_total, quote_ts], axis=1)
        tmp_total[self.col_name] = tmp_total[u"LLD膜价格_华北"] - tmp_total[u"L1月期货价格"]
        return tmp_total

    def seasonal_plot(self, title=None, start_year=None, axhline=None):
        tmp_df_interpolated, fig, axis = super(LBasis1, self).seasonal_plot(title=self.col_name, axhline=self.axhline, date_constraint=[1, 17])
        axis = Plot_Base.add_month_span(axis, tmp_df_interpolated, 1)
        return tmp_df_interpolated, fig, axis

class LBasis5(spread_base, Computed):
    field_name = u"基差"
    col_name = u"L5月基差"
    axhline = 0
    def get_ts_whole_progress(self):
        relevant_col_list = [u"LLD膜价格_华北"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        quote_df = L_Base.get_L_quote_df(month=5)
        quote_ts = month_quote_df_2_series(quote_df)
        quote_ts.name = u"L5月期货价格"
        tmp_total = pd.concat([tmp_total, quote_ts], axis=1)
        tmp_total[self.col_name] = tmp_total[u"LLD膜价格_华北"] - tmp_total[u"L5月期货价格"]
        return tmp_total
    
    def seasonal_plot(self, title=None, start_year=None, axhline=None):
        tmp_df_interpolated, fig, axis = super(LBasis5, self).seasonal_plot(title=self.col_name, axhline=self.axhline, date_constraint=[5, 17])
        axis = Plot_Base.add_month_span(axis, tmp_df_interpolated, 5)
        return tmp_df_interpolated, fig, axis

class LBasis9(spread_base, Computed):
    field_name = u"基差"
    col_name = u"L9月基差"
    axhline = 0
    def get_ts_whole_progress(self):
        relevant_col_list = [u"LLD膜价格_华北"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        quote_df = L_Base.get_L_quote_df(month=9)
        quote_ts = month_quote_df_2_series(quote_df)
        quote_ts.name = u"L9月期货价格"
        tmp_total = pd.concat([tmp_total, quote_ts], axis=1)
        tmp_total[self.col_name] = tmp_total[u"LLD膜价格_华北"] - tmp_total[u"L9月期货价格"]
        return tmp_total    

    def seasonal_plot(self, title=None, start_year=None, axhline=None):
        tmp_df_interpolated, fig, axis = super(LBasis9, self).seasonal_plot(title=self.col_name, axhline=self.axhline, date_constraint=[9, 17])
        axis = Plot_Base.add_month_span(axis, tmp_df_interpolated, 9)
        return tmp_df_interpolated, fig, axis    


###########################################################################################################################
""" 月间价差(计算指标) """ 

class LSpread1_5(spread_base, Computed):
    field_name = u"月间价差"
    col_name = u"L1_5价差"
    axhline = 0
    start_year = 2015
    def get_ts_whole_progress(self):
        month_list = ["01", "05"]
        all_main_quote_df = L_Base.get_L_main_month_quote_df()
        spread_series = main_month_quote_2_spread_series(month_list, all_main_quote_df)
        tmp_df = pd.DataFrame([spread_series], index=[self.col_name]).T
        return tmp_df

    def seasonal_plot(self, title=None, start_year=None, axhline=None):
        tmp_df_interpolated, fig, axis = super(LSpread1_5, self).seasonal_plot(title=self.col_name, start_year = self.start_year, 
                                              axhline=self.axhline, date_constraint=[1, 17])
        axis = Plot_Base.add_month_span(axis, tmp_df_interpolated, 1)
        return tmp_df_interpolated, fig, axis    
      

class LSpread5_9(spread_base, Computed):
    field_name = u"月间价差"
    col_name = u"L5_9价差"
    axhline = 0
    start_year = 2015
    def get_ts_whole_progress(self):
        month_list = ["05", "09"]
        all_main_quote_df = L_Base.get_L_main_month_quote_df()
        spread_series = main_month_quote_2_spread_series(month_list, all_main_quote_df)
        tmp_df = pd.DataFrame([spread_series], index=[self.col_name]).T
        return tmp_df

    def seasonal_plot(self, title=None, start_year=None, axhline=None):
        tmp_df_interpolated, fig, axis = super(LSpread5_9, self).seasonal_plot(title=self.col_name, start_year = self.start_year, 
                                              axhline=self.axhline, date_constraint=[5, 17])
        axis = Plot_Base.add_month_span(axis, tmp_df_interpolated, 5)
        return tmp_df_interpolated, fig, axis   

class LSpread9_1(spread_base, Computed):
    field_name = u"月间价差"
    col_name = u"L9_1价差"
    axhline = 0
    start_year = 2015
    def get_ts_whole_progress(self):
        month_list = ["09", "01"]
        all_main_quote_df = L_Base.get_L_main_month_quote_df()
        spread_series = main_month_quote_2_spread_series(month_list, all_main_quote_df)
        tmp_df = pd.DataFrame([spread_series], index=[self.col_name]).T
        return tmp_df

    def seasonal_plot(self, title=None, start_year=None, axhline=None):
        tmp_df_interpolated, fig, axis = super(LSpread9_1, self).seasonal_plot(title=self.col_name, start_year = self.start_year, 
                                              axhline=self.axhline, date_constraint=[9, 17])
        axis = Plot_Base.add_month_span(axis, tmp_df_interpolated, 9)
        return tmp_df_interpolated, fig, axis       
   
  

    
if __name__ == "__main__":
#    tmp_df_interpolated, fig, axis = LBasis1().seasonal_plot()
#    tmp_df_interpolated, fig, axis = LBasis1().seasonal_plot()
    ts = LBasis1().get_ts()
#    spread_df = time_series_to_seasonal_tranform_date_constraint(ts, [1,17])
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    