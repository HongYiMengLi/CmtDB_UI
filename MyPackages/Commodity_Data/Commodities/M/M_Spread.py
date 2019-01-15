# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 10:48:24 2018

@author: 李弘一萌
"""

import pandas as pd
from datetime import datetime
from .M_Base import M_Base
from . import M_SpotPrice, M_Upstream, M_FuturesPrice
from ...Base.Spread_Generate import main_month_quote_2_spread_series
from ...Base.DataType_Base import Manual, Computed, WindData
from ...Base.Plot_Base import Plot_Base
from matplotlib.ticker import FuncFormatter

class spread_base(M_Base, Plot_Base):
    table_english_name = "Spread"
    table_chinese_name = u"价差"
#    original_db_filepath = data_path + u"LPP价格数据库.xlsx"
    
    def output(self):
        print("Spread")
    
    def get_relevant_df(self, col_list):
        ts_list = [eval(M_Base.get_table_class_full_variable(x))().get_ts() for x in col_list]
        tmp_table_df = pd.concat(ts_list, axis=1).dropna(how="all")
        return tmp_table_df  
    

###########################################################################################################################
""" 基差(计算指标) """ 

    
class DouPoRiZhaoXianHuoJiCha_1YueHeYue(spread_base, Computed):
    field_name = u"基差"
    col_name = u"豆粕日照现货基差_1月合约"
    axhline = 0
    def get_ts_whole_progress(self):
#        relevant_col_list = [u"中国棉花328价格指数", "M01合约收盘价"]
#        tmp_total = self.get_relevant_df(relevant_col_list)
#        tmp_total[self.col_name] = tmp_total[u"中国棉花328价格指数"] - tmp_total[u"M01合约收盘价"]
#        return tmp_total
        pass
    
    def seasonal_plot(self, title=None, start_year=None, axhline=None):
        tmp_df_interpolated, fig, axis = super(DouPoRiZhaoXianHuoJiCha_1YueHeYue, self).seasonal_plot(title=self.col_name, axhline=self.axhline, date_constraint=[1, 17])
        axis = Plot_Base.add_month_span(axis, tmp_df_interpolated, 1)
        return tmp_df_interpolated, fig, axis

class DouPoZhangJiaGangXianHuoJiCha_1YueHeYue(spread_base, Computed):
    field_name = u"基差"
    col_name = u"豆粕张家港现货基差_1月合约"
    axhline = 0
    def get_ts_whole_progress(self):
#        relevant_col_list = [u"中国棉花328价格指数", "M01合约收盘价"]
#        tmp_total = self.get_relevant_df(relevant_col_list)
#        tmp_total[self.col_name] = tmp_total[u"中国棉花328价格指数"] - tmp_total[u"M01合约收盘价"]
#        return tmp_total
        pass
    
    
    def seasonal_plot(self, title=None, start_year=None, axhline=None):
        tmp_df_interpolated, fig, axis = super(DouPoZhangJiaGangXianHuoJiCha_1YueHeYue, self).seasonal_plot(title=self.col_name, axhline=self.axhline, date_constraint=[1, 17])
        axis = Plot_Base.add_month_span(axis, tmp_df_interpolated, 1)
        return tmp_df_interpolated, fig, axis

class DouPoDongGuanXianHuoJiCha_1YueHeYue(spread_base, Computed):
    field_name = u"基差"
    col_name = u"豆粕东莞现货基差_1月合约"
    axhline = 0
    def get_ts_whole_progress(self):
#        relevant_col_list = [u"中国棉花328价格指数", "M01合约收盘价"]
#        tmp_total = self.get_relevant_df(relevant_col_list)
#        tmp_total[self.col_name] = tmp_total[u"中国棉花328价格指数"] - tmp_total[u"M01合约收盘价"]
#        return tmp_total
        pass
    
    def seasonal_plot(self, title=None, start_year=None, axhline=None):
        tmp_df_interpolated, fig, axis = super(DouPoDongGuanXianHuoJiCha_1YueHeYue, self).seasonal_plot(title=self.col_name, axhline=self.axhline, date_constraint=[1, 17])
        axis = Plot_Base.add_month_span(axis, tmp_df_interpolated, 1)
        return tmp_df_interpolated, fig, axis
    
class DouPoRiZhaoXianHuoJiCha_5YueHeYue(spread_base, Computed):
    field_name = u"基差"
    col_name = u"豆粕日照现货基差_5月合约"
    axhline = 0
    def get_ts_whole_progress(self):
#        relevant_col_list = [u"中国棉花328价格指数", "M05合约收盘价"]
#        tmp_total = self.get_relevant_df(relevant_col_list)
#        tmp_total[self.col_name] = tmp_total[u"中国棉花328价格指数"] - tmp_total[u"M05合约收盘价"]
#        return tmp_total
        pass
    
    def seasonal_plot(self, title=None, start_year=None, axhline=None):
        tmp_df_interpolated, fig, axis = super(DouPoRiZhaoXianHuoJiCha_5YueHeYue, self).seasonal_plot(title=self.col_name, axhline=self.axhline, date_constraint=[5, 17])
        axis = Plot_Base.add_month_span(axis, tmp_df_interpolated, 5)
        return tmp_df_interpolated, fig, axis

class DouPoZhangJiaGangXianHuoJiCha_5YueHeYue(spread_base, Computed):
    field_name = u"基差"
    col_name = u"豆粕张家港现货基差_5月合约"
    axhline = 0
    def get_ts_whole_progress(self):
#        relevant_col_list = [u"中国棉花328价格指数", "M05合约收盘价"]
#        tmp_total = self.get_relevant_df(relevant_col_list)
#        tmp_total[self.col_name] = tmp_total[u"中国棉花328价格指数"] - tmp_total[u"M05合约收盘价"]
#        return tmp_total
        pass
    
    def seasonal_plot(self, title=None, start_year=None, axhline=None):
        tmp_df_interpolated, fig, axis = super(DouPoZhangJiaGangXianHuoJiCha_5YueHeYue, self).seasonal_plot(title=self.col_name, axhline=self.axhline, date_constraint=[5, 17])
        axis = Plot_Base.add_month_span(axis, tmp_df_interpolated, 5)
        return tmp_df_interpolated, fig, axis

class DouPoDongGuanXianHuoJiCha_5YueHeYue(spread_base, Computed):
    field_name = u"基差"
    col_name = u"豆粕东莞现货基差_5月合约"
    axhline = 0
    def get_ts_whole_progress(self):
#        relevant_col_list = [u"中国棉花328价格指数", "M05合约收盘价"]
#        tmp_total = self.get_relevant_df(relevant_col_list)
#        tmp_total[self.col_name] = tmp_total[u"中国棉花328价格指数"] - tmp_total[u"M05合约收盘价"]
#        return tmp_total
        pass
    
    def seasonal_plot(self, title=None, start_year=None, axhline=None):
        tmp_df_interpolated, fig, axis = super(DouPoDongGuanXianHuoJiCha_5YueHeYue, self).seasonal_plot(title=self.col_name, axhline=self.axhline, date_constraint=[5, 17])
        axis = Plot_Base.add_month_span(axis, tmp_df_interpolated, 5)
        return tmp_df_interpolated, fig, axis

    
class DouPoRiZhaoXianHuoJiCha_9YueHeYue(spread_base, Computed):
    field_name = u"基差"
    col_name = u"豆粕日照现货基差_9月合约"
    axhline = 0
    def get_ts_whole_progress(self):
#        relevant_col_list = [u"中国棉花328价格指数", "M09合约收盘价"]
#        tmp_total = self.get_relevant_df(relevant_col_list)
#        tmp_total[self.col_name] = tmp_total[u"中国棉花328价格指数"] - tmp_total[u"M09合约收盘价"]
#        return tmp_total
        pass
    
    def seasonal_plot(self, title=None, start_year=None, axhline=None):
        tmp_df_interpolated, fig, axis = super(DouPoRiZhaoXianHuoJiCha_9YueHeYue, self).seasonal_plot(title=self.col_name, axhline=self.axhline, date_constraint=[9, 17])
        axis = Plot_Base.add_month_span(axis, tmp_df_interpolated, 9)
        return tmp_df_interpolated, fig, axis
    
class DouPoZhangJiaGangXianHuoJiCha_9YueHeYue(spread_base, Computed):
    field_name = u"基差"
    col_name = u"豆粕张家港现货基差_9月合约"
    axhline = 0
    def get_ts_whole_progress(self):
#        relevant_col_list = [u"中国棉花328价格指数", "M09合约收盘价"]
#        tmp_total = self.get_relevant_df(relevant_col_list)
#        tmp_total[self.col_name] = tmp_total[u"中国棉花328价格指数"] - tmp_total[u"M09合约收盘价"]
#        return tmp_total
        pass
    
    def seasonal_plot(self, title=None, start_year=None, axhline=None):
        tmp_df_interpolated, fig, axis = super(DouPoZhangJiaGangXianHuoJiCha_9YueHeYue, self).seasonal_plot(title=self.col_name, axhline=self.axhline, date_constraint=[9, 17])
        axis = Plot_Base.add_month_span(axis, tmp_df_interpolated, 9)
        return tmp_df_interpolated, fig, axis
    
class DouPoDongGuanXianHuoJiCha_9YueHeYue(spread_base, Computed):
    field_name = u"基差"
    col_name = u"豆粕东莞现货基差_9月合约"
    axhline = 0
    def get_ts_whole_progress(self):
#        relevant_col_list = [u"中国棉花328价格指数", "M09合约收盘价"]
#        tmp_total = self.get_relevant_df(relevant_col_list)
#        tmp_total[self.col_name] = tmp_total[u"中国棉花328价格指数"] - tmp_total[u"M09合约收盘价"]
#        return tmp_total
        pass
    
    def seasonal_plot(self, title=None, start_year=None, axhline=None):
        tmp_df_interpolated, fig, axis = super(DouPoDongGuanXianHuoJiCha_9YueHeYue, self).seasonal_plot(title=self.col_name, axhline=self.axhline, date_constraint=[9, 17])
        axis = Plot_Base.add_month_span(axis, tmp_df_interpolated, 9)
        return tmp_df_interpolated, fig, axis
    
    
class DouPoYuanYueJiChaBaoJia_ZhangJiaGang(spread_base, Manual):
    field_name = u"基差"
    col_name = u"豆粕远月基差报价_张家港"
    
class DouPoYuanYueJiChaBaoJia_NanTong(spread_base, Manual):
    field_name = u"基差"
    col_name = u"豆粕远月基差报价_南通"
    
class DouPoYuanYueJiChaBaoJia_NanJing(spread_base, Manual):
    field_name = u"基差"
    col_name = u"豆粕远月基差报价_南京"
    
class DouPoYuanYueJiChaBaoJia_TianJin(spread_base, Manual):
    field_name = u"基差"
    col_name = u"豆粕远月基差报价_天津"
    
class DouYuanYueJiChaBaoJia_RiZhao(spread_base, Manual):
    field_name = u"基差"
    col_name = u"豆粕远月基差报价_日照"
    
class DouPoYuanYueJiChaBaoJia_ZhenJiang(spread_base, Manual):
    field_name = u"基差"
    col_name = u"豆粕远月基差报价_镇江"
    
class DouPoYuanYueJiChaBaoJia_LianYunGang(spread_base, Manual):
    field_name = u"基差"
    col_name = u"豆粕远月基差报价_连云港"
    
class DouPoYuanYueJiChaBaoJia_TaiZhou(spread_base, Manual):
    field_name = u"基差"
    col_name = u"豆粕远月基差报价_泰州"
    
class DouPoYuanYueJiChaBaoJia_TaiXing(spread_base, Manual):
    field_name = u"基差"
    col_name = u"豆粕远月基差报价_泰兴"
    
class DouPoYuanYueJiChaBaoJia_DongGuan(spread_base, Manual):
    field_name = u"基差"
    col_name = u"豆粕远月基差报价_东莞"
    
class DouPoYuanYueJiChaBaoJia_ZhanJiang(spread_base, Manual):
    field_name = u"基差"
    col_name = u"豆粕远月基差报价_湛江"
    
class DouPoYuanYueJiChaBaoJia_YangJiang(spread_base, Manual):
    field_name = u"基差"
    col_name = u"豆粕远月基差报价_阳江"
    

###########################################################################################################################
""" 月间价差(计算指标) """ 

class M1_5JiaCha(spread_base, Computed):
    field_name = u"月间价差"
    col_name = u"M1-5价差"
    axhline = 0
    start_year = 2015
    def get_ts_whole_progress(self):
        month_list = ["01", "05"]
        all_main_quote_df = M_Base.get_M_main_month_quote_df()
        spread_series = main_month_quote_2_spread_series(month_list, all_main_quote_df)
        tmp_df = pd.DataFrame([spread_series], index=[self.col_name]).T
        return tmp_df

    def seasonal_plot(self, title=None, start_year=None, axhline=None):
        tmp_df_interpolated, fig, axis = super(M1_5JiaCha, self).seasonal_plot(title=self.col_name, start_year = self.start_year, 
                                              axhline=self.axhline, date_constraint=[1, 17])
        axis = Plot_Base.add_month_span(axis, tmp_df_interpolated, 1)
        return tmp_df_interpolated, fig, axis
        
class M5_9JiaCha(spread_base, Computed):
    field_name = u"月间价差"
    col_name = u"M5-9价差"
    axhline = 0
    start_year = 2015
    def get_ts_whole_progress(self):
        month_list = ["05", "09"]
        all_main_quote_df = M_Base.get_M_main_month_quote_df()
        spread_series = main_month_quote_2_spread_series(month_list, all_main_quote_df)
        tmp_df = pd.DataFrame([spread_series], index=[self.col_name]).T
        return tmp_df

    def seasonal_plot(self, title=None, start_year=None, axhline=None):
        tmp_df_interpolated, fig, axis = super(M5_9JiaCha, self).seasonal_plot(title=self.col_name, start_year = self.start_year, 
                                              axhline=self.axhline, date_constraint=[5, 17])
        axis = Plot_Base.add_month_span(axis, tmp_df_interpolated, 5)
        return tmp_df_interpolated, fig, axis    
      

class M9_1JiaCha(spread_base, Computed):
    field_name = u"月间价差"
    col_name = u"M9-1价差"
    axhline = 0
    start_year = 2015
    def get_ts_whole_progress(self):
        month_list = ["09", "01"]
        all_main_quote_df = M_Base.get_M_main_month_quote_df()
        spread_series = main_month_quote_2_spread_series(month_list, all_main_quote_df)
        tmp_df = pd.DataFrame([spread_series], index=[self.col_name]).T
        return tmp_df

    def seasonal_plot(self, title=None, start_year=None, axhline=None):
        tmp_df_interpolated, fig, axis = super(M9_1JiaCha, self).seasonal_plot(title=self.col_name, start_year = self.start_year, 
                                              axhline=self.axhline, date_constraint=[9, 17])
        axis = Plot_Base.add_month_span(axis, tmp_df_interpolated, 9)
        return tmp_df_interpolated, fig, axis  
        

    
if __name__ == "__main__":
    ts = M1_5JiaCha().seasonal_plot()
    
    
    
    
    
    
    
    
    
    
    
    
    