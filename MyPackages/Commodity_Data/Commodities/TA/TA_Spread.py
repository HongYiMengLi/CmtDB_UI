# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 10:48:24 2018

@author: 李弘一萌
"""

import pandas as pd
from datetime import datetime
from .TA_Base import TA_Base
from . import TA_SpotPrice, TA_Upstream, TA_FuturesPrice, TA_Macro, TA_Downstream
from ...Base.Spread_Generate import main_month_quote_2_spread_series
from ...Base.DataType_Base import Manual, Computed, WindData
from ...Base.Plot_Base import Plot_Base
from matplotlib.ticker import FuncFormatter

class spread_base(TA_Base, Plot_Base):
    table_english_name = "Spread"
    table_chinese_name = u"价差与比价"
    
    def output(self):
        print("Spread")
    
    def get_relevant_df(self, col_list):
        ts_list = [eval(TA_Base.get_table_class_full_variable(x))().get_ts() for x in col_list]
        tmp_table_df = pd.concat(ts_list, axis=1).dropna(how="all")
        return tmp_table_df  
    
###########################################################################################################################
""" 比价 """ 
""" 计算指标 """
    
class PTA01OverBrent(spread_base, Computed):
    field_name = u"比价"
    col_name = u"PTA01/BRENT结算价"
    def get_ts_whole_progress(self):
        relevant_col_list = [u"PTA01合约收盘价", u"BRENT结算价"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"PTA01合约收盘价"] / tmp_total[u"BRENT结算价"]
        return tmp_total
    
class PTA05OverBrent(spread_base, Computed):
    field_name = u"比价"
    col_name = u"PTA05/BRENT结算价"
    def get_ts_whole_progress(self):
        relevant_col_list = [u"PTA05合约收盘价", u"BRENT结算价"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"PTA05合约收盘价"] / tmp_total[u"BRENT结算价"]
        return tmp_total
    
class PTA09OverBrent(spread_base, Computed):
    field_name = u"比价"
    col_name = u"PTA09/BRENT结算价"
    def get_ts_whole_progress(self):
        relevant_col_list = [u"PTA09合约收盘价", u"BRENT结算价"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"PTA09合约收盘价"] / tmp_total[u"BRENT结算价"]
        return tmp_total
    
class PTAZhuLiOverBrent(spread_base, Computed):
    field_name = u"比价"
    col_name = u"PTA主力/BRENT结算价"
    def get_ts_whole_progress(self):
        relevant_col_list = [u"PTA主力期价", u"BRENT结算价"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"PTA主力期价"] / tmp_total[u"BRENT结算价"]
        return tmp_total

class PTAOverSC(spread_base, Computed):
    field_name = u"比价"
    col_name = u"PTA主力/SC结算价"
    def get_ts_whole_progress(self):
        relevant_col_list = [u"PTA主力期价", u"SC原油结算价"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"PTA主力期价"] / tmp_total[u"SC原油结算价"]
        return tmp_total
    
class MianHuaHuaDongOverPTAHuaDong(spread_base, Computed):
    field_name = u"比价"
    col_name = u"棉花华东价/PTA现货比价"
    def get_ts_whole_progress(self):
        relevant_col_list = [u"棉花现货价格_华东", u"PTA现货价格_华东"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"棉花现货价格_华东"] / tmp_total[u"PTA现货价格_华东"]
        return tmp_total
    
    
    
###########################################################################################################################
""" 基差(计算指标) """ 

class PTAZhuLiJiCha(spread_base, Computed):
    field_name = u"基差"
    col_name = u"PTA主力基差"
    axhline = 0
    def get_ts_whole_progress(self):
        relevant_col_list = [u"PTA现货价格_华东", "PTA主力期价"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"PTA现货价格_华东"] - tmp_total[u"PTA主力期价"]
        return tmp_total
    
    def seasonal_plot(self, title=None, start_year=None, axhline=None):
        tmp_df_interpolated, fig, axis = super(PTAZhuLiJiCha, self).seasonal_plot(title=self.col_name, axhline=self.axhline)
        axis = Plot_Base.add_month_span(axis, tmp_df_interpolated, 1)
        return tmp_df_interpolated, fig, axis

class PTABasis1(spread_base, Computed):
    field_name = u"基差"
    col_name = u"PTA01基差"
    axhline = 0
    start_year = 2014
    def get_ts_whole_progress(self):
        relevant_col_list = [u"PTA现货价格_华东", "PTA01合约收盘价"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"PTA现货价格_华东"] - tmp_total[u"PTA01合约收盘价"]
        return tmp_total
    
    def seasonal_plot(self, title=None, start_year=None, axhline=None):
        tmp_df_interpolated, fig, axis = super(PTABasis1, self).seasonal_plot(title=self.col_name, axhline=self.axhline, date_constraint=[1, 17])
        axis = Plot_Base.add_month_span(axis, tmp_df_interpolated, 1)
        return tmp_df_interpolated, fig, axis
    
class PTABasis5(spread_base, Computed):
    field_name = u"基差"
    col_name = u"PTA05基差"
    axhline = 0
    start_year = 2014
    def get_ts_whole_progress(self):
        relevant_col_list = [u"PTA现货价格_华东", "PTA05合约收盘价"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"PTA现货价格_华东"] - tmp_total[u"PTA05合约收盘价"]
        return tmp_total

    def seasonal_plot(self, title=None, start_year=None, axhline=None):
        tmp_df_interpolated, fig, axis = super(PTABasis5, self).seasonal_plot(title=self.col_name, axhline=self.axhline, date_constraint=[5, 17])
        axis = Plot_Base.add_month_span(axis, tmp_df_interpolated, 5)
        return tmp_df_interpolated, fig, axis

class PTABasis9(spread_base, Computed):
    field_name = u"基差"
    col_name = u"PTA09基差"
    axhline = 0
    start_year = 2014
    def get_ts_whole_progress(self):
        relevant_col_list = [u"PTA现货价格_华东", "PTA09合约收盘价"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"PTA现货价格_华东"] - tmp_total[u"PTA09合约收盘价"]
        return tmp_total

    def seasonal_plot(self, title=None, start_year=None, axhline=None):
        tmp_df_interpolated, fig, axis = super(PTABasis9, self).seasonal_plot(title=self.col_name, axhline=self.axhline, date_constraint=[9, 17])
        axis = Plot_Base.add_month_span(axis, tmp_df_interpolated, 9)
        return tmp_df_interpolated, fig, axis

class PTAZhuLiMinusBrent(spread_base, Computed):
    field_name = u"基差"
    col_name = u"PTA主力-BRENT结算价"
    axhline = 0
    def get_ts_whole_progress(self):
        relevant_col_list = [u"PTA主力期价", "BRENT结算价"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"PTA主力期价"] - tmp_total[u"BRENT结算价"]
        return tmp_total

    def seasonal_plot(self, title=None, start_year=None, axhline=None):
        tmp_df_interpolated, fig, axis = super(PTAZhuLiMinusBrent, self).seasonal_plot(title=self.col_name, axhline=self.axhline)
        axis = Plot_Base.add_month_span(axis, tmp_df_interpolated, 9)
        return tmp_df_interpolated, fig, axis
    
    
###########################################################################################################################
""" 月间价差(计算指标) """ 

class PTASpread1_5(spread_base, Computed):
    field_name = u"月间价差"
    col_name = u"PTA1_5价差"
    axhline = 0
    start_year = 2015
    def get_ts_whole_progress(self):
        month_list = ["01", "05"]
        all_main_quote_df = TA_Base.get_TA_main_month_quote_df()
        spread_series = main_month_quote_2_spread_series(month_list, all_main_quote_df)
        tmp_df = pd.DataFrame([spread_series], index=[self.col_name]).T
        return tmp_df

    def seasonal_plot(self, title=None, start_year=None, axhline=None):
        tmp_df_interpolated, fig, axis = super(PTASpread1_5, self).seasonal_plot(title=self.col_name, start_year = self.start_year, 
                                              axhline=self.axhline, date_constraint=[1, 17])
        axis = Plot_Base.add_month_span(axis, tmp_df_interpolated, 1)
        return tmp_df_interpolated, fig, axis    
      

class PTASpread5_9(spread_base, Computed):
    field_name = u"月间价差"
    col_name = u"PTA5_9价差"
    axhline = 0
    start_year = 2015
    def get_ts_whole_progress(self):
        month_list = ["05", "09"]
        all_main_quote_df = TA_Base.get_TA_main_month_quote_df()
        spread_series = main_month_quote_2_spread_series(month_list, all_main_quote_df)
        tmp_df = pd.DataFrame([spread_series], index=[self.col_name]).T
        return tmp_df

    def seasonal_plot(self, title=None, start_year=None, axhline=None):
        tmp_df_interpolated, fig, axis = super(PTASpread5_9, self).seasonal_plot(title=self.col_name, start_year = self.start_year, 
                                              axhline=self.axhline, date_constraint=[5, 21])
        axis = Plot_Base.add_month_span(axis, tmp_df_interpolated, 5)
        return tmp_df_interpolated, fig, axis   

class PTASpread9_1(spread_base, Computed):
    field_name = u"月间价差"
    col_name = u"PTA9_1价差"
    axhline = 0
    start_year = 2015
    def get_ts_whole_progress(self):
        month_list = ["09", "01"]
        all_main_quote_df = TA_Base.get_TA_main_month_quote_df()
        spread_series = main_month_quote_2_spread_series(month_list, all_main_quote_df)
        tmp_df = pd.DataFrame([spread_series], index=[self.col_name]).T
        return tmp_df

    def seasonal_plot(self, title=None, start_year=None, axhline=None):
        tmp_df_interpolated, fig, axis = super(PTASpread9_1, self).seasonal_plot(title=self.col_name, start_year = self.start_year, 
                                              axhline=self.axhline, date_constraint=[9, 17])
        axis = Plot_Base.add_month_span(axis, tmp_df_interpolated, 9)
        return tmp_df_interpolated, fig, axis


###########################################################################################################################
""" 其他价差(计算指标) """ 

class MEGMinusPTAHuaDong(spread_base, Computed):
    field_name = u"其他价差"
    col_name = u"MEG-PTA现货价差"
    axhline = 0
    def get_ts_whole_progress(self):
        relevant_col_list = [u"MEG现货价格_华东", "PTA现货价格_华东"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"MEG现货价格_华东"] - tmp_total[u"PTA现货价格_华东"]
        return tmp_total

class PXMinusMXXianHuoJiaCha(spread_base, Computed):
    field_name = u"其他价差"
    col_name = u"PX-MX现货价差"
    axhline = 0
    def get_ts_whole_progress(self):
        relevant_col_list = [u"PX价格_CFR_台湾", "MX价格_FOB_韩国"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"PX价格_CFR_台湾"] - tmp_total[u"MX价格_FOB_韩国"]
        return tmp_total
    
class PTANeiWaiPanJiaCha(spread_base, Computed):
    field_name = u"其他价差"
    col_name = u"PTA内外盘价差"
    axhline = 0
    def get_ts_whole_progress(self):
        relevant_col_list = [u"PTA现货价格_华东", "PTA现货价格_外盘", "汇卖价_美元兑人民币"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total["PTA现货价格_华东"] - tmp_total["PTA现货价格_外盘"] * 1.17 \
                                   * 1.065 * tmp_total["汇卖价_美元兑人民币"]
        return tmp_total
    
class ShiNaoYouLieJieJiaCha(spread_base, Computed):
    field_name = u"其他价差"
    col_name = u"石脑油裂解价差"
    axhline = 0
    def get_ts_whole_progress(self):
        relevant_col_list = [u"石脑油价格_CFR_日本", "BRENT结算价"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"石脑油价格_CFR_日本"] - tmp_total[u"BRENT结算价"] * 7.35
        return tmp_total

class BrentMinusWTIYuanYouJiaCha(spread_base, Computed):
    field_name = u"其他价差"
    col_name = u"BRENT-WTI原油价差"
    axhline = 0
    def get_ts_whole_progress(self):
        relevant_col_list = [u"BRENT结算价", "WTI结算价"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"BRENT结算价"] - tmp_total[u"WTI结算价"]
        return tmp_total
















if __name__ == "__main__":
#    df = PTASpread9_1().get_ts()
    df, fig, axis = PTABasis1().seasonal_plot()
    
    
    
    
    
    
    
    
    
    
    
    
    
    