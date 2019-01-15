# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 10:48:24 2018

@author: 李弘一萌
"""

import pandas as pd
from datetime import datetime
from .BU_Base import BU_Base
from . import BU_SpotPrice, BU_Upstream, BU_FuturesPrice, BU_Macro
from ...Base.DataType_Base import Manual, Computed, WindData
from ...Base.Plot_Base import Plot_Base
from ....Futures_Data.Quote.QuoteData import QuoteData
from ...Base.Spread_Generate import main_month_quote_2_spread_series
from matplotlib.ticker import FuncFormatter

class spread_base(BU_Base, Plot_Base):
    table_english_name = "Spread"
    table_chinese_name = u"价差与比价"
#    original_db_filepath = data_path + u"LPP价格数据库.xlsx"
    
    def output(self):
        print("Spread")
    
    def get_relevant_df(self, col_list):
        ts_list = [eval(BU_Base.get_table_class_full_variable(x))().get_ts() for x in col_list]
        tmp_table_df = pd.concat(ts_list, axis=1).dropna(how="all")
        return tmp_table_df  
    
###########################################################################################################################
""" 比价 """ 
""" 计算指标 """
    

    
class HanGuoLiQingOverRanLiaoYou180CSTBiJia(spread_base, Computed):
    field_name = u"比价"
    col_name = u"韩国沥青/燃料油180CST比价"
    def get_ts_whole_progress(self):
        relevant_col_list = [u"沥青现货价格_FOB_韩国", u"韩国燃料油180CST现货价格"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"沥青现货价格_FOB_韩国"] / tmp_total[u"韩国燃料油180CST现货价格"]
        return tmp_total

class ShanDongXianHuoOverLiQing06BiJia(spread_base, Computed):
    field_name = u"比价"
    col_name = u"山东现货/沥青06比价"
    def get_ts_whole_progress(self):
        relevant_col_list = [u"沥青现货价格_山东", u"BU06合约收盘价"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"沥青现货价格_山东"] / tmp_total[u"BU06合约收盘价"]
        return tmp_total

class ShanDongXianHuoOverLiQing09BiJia(spread_base, Computed):
    field_name = u"比价"
    col_name = u"山东现货/沥青09比价"
    def get_ts_whole_progress(self):
        relevant_col_list = [u"沥青现货价格_山东", u"BU09合约收盘价"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"沥青现货价格_山东"] / tmp_total[u"BU09合约收盘价"]
        return tmp_total
    
class ShanDongXianHuoOverLiQing12BiJia(spread_base, Computed):
    field_name = u"比价"
    col_name = u"山东现货/沥青12比价"
    def get_ts_whole_progress(self):
        relevant_col_list = [u"沥青现货价格_山东", u"BU12合约收盘价"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"沥青现货价格_山东"] / tmp_total[u"BU12合约收盘价"]
        return tmp_total

class HuaDongXianHuoOverLiQing06BiJia(spread_base, Computed):
    field_name = u"比价"
    col_name = u"华东现货/沥青12比价"
    def get_ts_whole_progress(self):
        relevant_col_list = [u"沥青现货价格_华东", u"BU06合约收盘价"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"沥青现货价格_华东"] / tmp_total[u"BU06合约收盘价"]
        return tmp_total

class HuaDongXianHuoOverLiQing09BiJia(spread_base, Computed):
    field_name = u"比价"
    col_name = u"华东现货/沥青12比价"
    def get_ts_whole_progress(self):
        relevant_col_list = [u"沥青现货价格_华东", u"BU09合约收盘价"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"沥青现货价格_华东"] / tmp_total[u"BU09合约收盘价"]
        return tmp_total

class HuaDongXianHuoOverLiQing12BiJia(spread_base, Computed):
    field_name = u"比价"
    col_name = u"华东现货/沥青12比价"
    def get_ts_whole_progress(self):
        relevant_col_list = [u"沥青现货价格_华东", u"BU12合约收盘价"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"沥青现货价格_华东"] / tmp_total[u"BU12合约收盘价"]
        return tmp_total

class XinJiaPoLiQingOverBrentBiJia(spread_base, Computed):
    field_name = u"比价"
    col_name = u"新加坡沥青/Brent比价"
    def get_ts_whole_progress(self):
        relevant_col_list = [u"沥青现货价格_FOB_新加坡", u"Brent结算价"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"沥青现货价格_FOB_新加坡"] / tmp_total[u"Brent结算价"]
        return tmp_total

class XinJiaPo180CSTOverBrentBiJia(spread_base, Computed):
    field_name = u"比价"
    col_name = u"新加坡180CST/Brent比价"
    def get_ts_whole_progress(self):
        relevant_col_list = [u"新加坡燃料油180CST现货价格", u"Brent结算价"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"新加坡燃料油180CST现货价格"] / tmp_total[u"Brent结算价"]
        return tmp_total

class XinJiaPo380CSTOverBrentBiJia(spread_base, Computed):
    field_name = u"比价"
    col_name = u"新加坡380CST/Brent比价"
    def get_ts_whole_progress(self):
        relevant_col_list = [u"新加坡燃料油380CST现货价格", u"Brent结算价"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"新加坡燃料油380CST现货价格"] / tmp_total[u"Brent结算价"]
        return tmp_total

class BU06Over180CSTBiJia(spread_base, Computed):
    field_name = u"比价"
    col_name = u"BU06/180CST比价"
    def get_ts_whole_progress(self):
        relevant_col_list = [u"BU06合约收盘价", u"新加坡燃料油180CST现货价格", u"汇卖价_美元兑人民币"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"BU06合约收盘价"] / tmp_total[u"新加坡燃料油180CST现货价格"] / tmp_total[u"汇卖价_美元兑人民币"]
        return tmp_total

class BU09Over180CSTBiJia(spread_base, Computed):
    field_name = u"比价"
    col_name = u"BU09/180CST比价"
    def get_ts_whole_progress(self):
        relevant_col_list = [u"BU09合约收盘价", u"新加坡燃料油180CST现货价格", u"汇卖价_美元兑人民币"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"BU09合约收盘价"] / tmp_total[u"新加坡燃料油180CST现货价格"] / tmp_total[u"汇卖价_美元兑人民币"]
        return tmp_total
    
class BU12Over180CSTBiJia(spread_base, Computed):
    field_name = u"比价"
    col_name = u"BU06/180CST比价"
    def get_ts_whole_progress(self):
        relevant_col_list = [u"BU12合约收盘价", u"新加坡燃料油180CST现货价格", u"汇卖价_美元兑人民币"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"BU12合约收盘价"] / tmp_total[u"新加坡燃料油180CST现货价格"] / tmp_total[u"汇卖价_美元兑人民币"]
        return tmp_total
    
class BU06Over380CSTBiJia(spread_base, Computed):
    field_name = u"比价"
    col_name = u"BU06/380CST比价"
    def get_ts_whole_progress(self):
        relevant_col_list = [u"BU06合约收盘价", u"新加坡燃料油380CST现货价格", u"汇卖价_美元兑人民币"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"BU06合约收盘价"] / tmp_total[u"新加坡燃料油380CST现货价格"] / tmp_total[u"汇卖价_美元兑人民币"]
        return tmp_total
    
class BU09Over380CSTBiJia(spread_base, Computed):
    field_name = u"比价"
    col_name = u"BU06/380CST比价"
    def get_ts_whole_progress(self):
        relevant_col_list = [u"BU09合约收盘价", u"新加坡燃料油380CST现货价格", u"汇卖价_美元兑人民币"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"BU09合约收盘价"] / tmp_total[u"新加坡燃料油380CST现货价格"] / tmp_total[u"汇卖价_美元兑人民币"]
        return tmp_total
    
class BU12Over380CSTBiJia(spread_base, Computed):
    field_name = u"比价"
    col_name = u"BU12/380CST比价"
    def get_ts_whole_progress(self):
        relevant_col_list = [u"BU12合约收盘价", u"新加坡燃料油380CST现货价格", u"汇卖价_美元兑人民币"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"BU12合约收盘价"] / tmp_total[u"新加坡燃料油380CST现货价格"] / tmp_total[u"汇卖价_美元兑人民币"]
        return tmp_total
    
class BU06OverBrentBiJia(spread_base, Computed):
    field_name = u"比价"
    col_name = u"BU06/Brent比价"
    def get_ts_whole_progress(self):
        relevant_col_list = [u"BU06合约收盘价", u"Brent结算价", u"汇卖价_美元兑人民币"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"BU06合约收盘价"] / tmp_total[u"Brent结算价"] / tmp_total[u"汇卖价_美元兑人民币"]
        return tmp_total    

class BU09OverBrentBiJia(spread_base, Computed):
    field_name = u"比价"
    col_name = u"BU09/Brent比价"
    def get_ts_whole_progress(self):
        relevant_col_list = [u"BU09合约收盘价", u"Brent结算价", u"汇卖价_美元兑人民币"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"BU09合约收盘价"] / tmp_total[u"Brent结算价"] / tmp_total[u"汇卖价_美元兑人民币"]
        return tmp_total 

class BU12OverBrentBiJia(spread_base, Computed):
    field_name = u"比价"
    col_name = u"BU12/Brent比价"
    def get_ts_whole_progress(self):
        relevant_col_list = [u"BU12合约收盘价", u"Brent结算价", u"汇卖价_美元兑人民币"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"BU12合约收盘价"] / tmp_total[u"Brent结算价"] / tmp_total[u"汇卖价_美元兑人民币"]
        return tmp_total 

class ShanDongLiQingOverBrentBiJia(spread_base, Computed):
    field_name = u"比价"
    col_name = u"山东沥青/Brent比价"
    def get_ts_whole_progress(self):
        relevant_col_list = [u"沥青现货价格_山东", u"Brent结算价", u"汇卖价_美元兑人民币"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"沥青现货价格_山东"] / tmp_total[u"Brent结算价"] / tmp_total[u"汇卖价_美元兑人民币"]
        return tmp_total 


class BUOverBrentBiJia_JiCha_06(spread_base, Computed):
    field_name = u"比价"
    col_name = u"BU/Brent比价_基差_06"
    def get_ts_whole_progress(self):
        relevant_col_list = [u"沥青现货价格_山东", u"BU06合约收盘价", u"Brent结算价", u"汇卖价_美元兑人民币"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = (tmp_total[u"沥青现货价格_山东"] - tmp_total[u"BU06合约收盘价"])/ tmp_total[u"Brent结算价"] / tmp_total[u"汇卖价_美元兑人民币"]
        return tmp_total 


class BUOverBrentBiJia_JiCha_09(spread_base, Computed):
    field_name = u"比价"
    col_name = u"BU/Brent比价_基差_09"
    def get_ts_whole_progress(self):
        relevant_col_list = [u"沥青现货价格_山东", u"BU09合约收盘价", u"Brent结算价", u"汇卖价_美元兑人民币"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = (tmp_total[u"沥青现货价格_山东"] - tmp_total[u"BU09合约收盘价"])/ tmp_total[u"Brent结算价"] / tmp_total[u"汇卖价_美元兑人民币"]
        return tmp_total 


class BUOverBrentBiJia_JiCha_12(spread_base, Computed):
    field_name = u"比价"
    col_name = u"BU/Brent比价_基差_12"
    def get_ts_whole_progress(self):
        relevant_col_list = [u"沥青现货价格_山东", u"BU12合约收盘价", u"Brent结算价", u"汇卖价_美元兑人民币"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = (tmp_total[u"沥青现货价格_山东"] - tmp_total[u"BU12合约收盘价"])/ tmp_total[u"Brent结算价"] / tmp_total[u"汇卖价_美元兑人民币"]
        return tmp_total 

###########################################################################################################################
""" 地区价差(计算指标) """ 

class LiQingChangSanJiaoMinusHuaNanJiaCha(spread_base, Computed):
    field_name = u"地区价差"
    col_name = u"沥青长三角-华南价差"
    def get_ts_whole_progress(self):
        relevant_col_list = [u"沥青现货价格_华东", "沥青现货价格_华南"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"沥青现货价格_华东"] - tmp_total[u"沥青现货价格_华南"]
        return tmp_total
    
class LiQingChangSanJiaoMinusShanDongJiaCha(spread_base, Computed):
    field_name = u"地区价差"
    col_name = u"沥青长三角-山东价差"
    def get_ts_whole_progress(self):
        relevant_col_list = [u"沥青现货价格_华东", "沥青现货价格_山东"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"沥青现货价格_华东"] - tmp_total[u"沥青现货价格_山东"]
        return tmp_total

class LiQingChangSanJiaoMinusXiNanJiaCha(spread_base, Computed):
    field_name = u"地区价差"
    col_name = u"沥青长三角-西南价差"
    def get_ts_whole_progress(self):
        relevant_col_list = [u"沥青现货价格_华东", "国产重交价格_西南"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"沥青现货价格_华东"] - tmp_total[u"国产重交价格_西南"]
        return tmp_total

class LiQingHuaNanMinusXiNanJiaCha(spread_base, Computed):
    field_name = u"地区价差"
    col_name = u"沥青华南-西南价差"
    def get_ts_whole_progress(self):
        relevant_col_list = [u"沥青现货价格_华南", "国产重交价格_西南"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"沥青现货价格_华南"] - tmp_total[u"国产重交价格_西南"]
        return tmp_total

class LiQingShanDongMinusXiBeiJiaCha(spread_base, Computed):
    field_name = u"地区价差"
    col_name = u"沥青山东-西北价差"
    def get_ts_whole_progress(self):
        relevant_col_list = [u"沥青现货价格_山东", "国产重交价格_西北"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"沥青现货价格_山东"] - tmp_total[u"国产重交价格_西北"]
        return tmp_total

class LiQingShanDongMinusDongBeiJiaCha(spread_base, Computed):
    field_name = u"地区价差"
    col_name = u"沥青山东-东北价差"
    def get_ts_whole_progress(self):
        relevant_col_list = [u"沥青现货价格_山东", "国产重交价格_东北"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"沥青现货价格_山东"] - tmp_total[u"国产重交价格_东北"]
        return tmp_total    
    
    
###########################################################################################################################
""" 基差(计算指标) """ 

class LiQingChangSanJiaoZhuLiJiCha(spread_base, Computed):
    field_name = u"基差"
    col_name = u"沥青长三角主力基差"
    axhline = 0
    def get_ts_whole_progress(self):
        relevant_col_list = [u"沥青现货价格_华东", "BU主力合约收盘价"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"沥青现货价格_华东"] - tmp_total[u"BU主力合约收盘价"]
        return tmp_total
    
    def seasonal_plot(self, title=None, start_year=None, axhline=None):
        tmp_df_interpolated, fig, axis = super(LiQingChangSanJiaoZhuLiJiCha, self).seasonal_plot(title=self.col_name, axhline=self.axhline)
        return tmp_df_interpolated, fig, axis

class LiQingHuaNanZhuLiJiCha(spread_base, Computed):
    field_name = u"基差"
    col_name = u"沥青华南主力基差"
    axhline = 0
    def get_ts_whole_progress(self):
        relevant_col_list = [u"沥青现货价格_华南", "BU主力合约收盘价"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"沥青现货价格_华南"] - tmp_total[u"BU主力合约收盘价"]
        return tmp_total
    
    def seasonal_plot(self, title=None, start_year=None, axhline=None):
        tmp_df_interpolated, fig, axis = super(LiQingHuaNanZhuLiJiCha, self).seasonal_plot(title=self.col_name, axhline=self.axhline)
        return tmp_df_interpolated, fig, axis
    
class LiQingShanDongZhuLiJiCha(spread_base, Computed):
    field_name = u"基差"
    col_name = u"沥青山东主力基差"
    axhline = 0
    def get_ts_whole_progress(self):
        relevant_col_list = [u"沥青现货价格_山东", "BU主力合约收盘价"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"沥青现货价格_山东"] - tmp_total[u"BU主力合约收盘价"]
        return tmp_total
    
    def seasonal_plot(self, title=None, start_year=None, axhline=None):
        tmp_df_interpolated, fig, axis = super(LiQingShanDongZhuLiJiCha, self).seasonal_plot(title=self.col_name, axhline=self.axhline)
        return tmp_df_interpolated, fig, axis

    
class LiQingChangSanJiao06JiCha(spread_base, Computed):
    field_name = u"基差"
    col_name = u"沥青长三角06基差"
    axhline = 0
    def get_ts_whole_progress(self):
        relevant_col_list = [u"沥青现货价格_华东", "BU06合约收盘价"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"沥青现货价格_华东"] - tmp_total[u"BU06合约收盘价"]
        return tmp_total
    
    def seasonal_plot(self, title=None, start_year=None, axhline=None):
        tmp_df_interpolated, fig, axis = super(LiQingChangSanJiao06JiCha, self).seasonal_plot(title=self.col_name, axhline=self.axhline, date_constraint=[6, 17])
        axis = Plot_Base.add_month_span(axis, tmp_df_interpolated, 6)
        return tmp_df_interpolated, fig, axis


class LiQingChangSanJiao09JiCha(spread_base, Computed):
    field_name = u"基差"
    col_name = u"沥青长三角09基差"
    axhline = 0
    def get_ts_whole_progress(self):
        relevant_col_list = [u"沥青现货价格_华东", "BU09合约收盘价"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"沥青现货价格_华东"] - tmp_total[u"BU09合约收盘价"]
        return tmp_total
    
    def seasonal_plot(self, title=None, start_year=None, axhline=None):
        tmp_df_interpolated, fig, axis = super(LiQingChangSanJiao09JiCha, self).seasonal_plot(title=self.col_name, axhline=self.axhline, date_constraint=[9, 17])
        axis = Plot_Base.add_month_span(axis, tmp_df_interpolated, 9)
        return tmp_df_interpolated, fig, axis

    
class LiQingChangSanJiao12JiCha(spread_base, Computed):
    field_name = u"基差"
    col_name = u"沥青长三角12基差"
    axhline = 0
    def get_ts_whole_progress(self):
        relevant_col_list = [u"沥青现货价格_华东", "BU12合约收盘价"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"沥青现货价格_华东"] - tmp_total[u"BU12合约收盘价"]
        return tmp_total
    
    def seasonal_plot(self, title=None, start_year=None, axhline=None):
        tmp_df_interpolated, fig, axis = super(LiQingChangSanJiao12JiCha, self).seasonal_plot(title=self.col_name, axhline=self.axhline, date_constraint=[12, 17])
        axis = Plot_Base.add_month_span(axis, tmp_df_interpolated, 12)
        return tmp_df_interpolated, fig, axis
    

class LiQingShanDong06JiCha(spread_base, Computed):
    field_name = u"基差"
    col_name = u"沥青山东06基差"
    axhline = 0
    def get_ts_whole_progress(self):
        relevant_col_list = [u"沥青现货价格_山东", "BU06合约收盘价"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"沥青现货价格_山东"] - tmp_total[u"BU06合约收盘价"]
        return tmp_total
    
    def seasonal_plot(self, title=None, start_year=None, axhline=None):
        tmp_df_interpolated, fig, axis = super(LiQingShanDong06JiCha, self).seasonal_plot(title=self.col_name, axhline=self.axhline, date_constraint=[6, 17])
        axis = Plot_Base.add_month_span(axis, tmp_df_interpolated, 6)
        return tmp_df_interpolated, fig, axis


class LiQingShanDong09JiCha(spread_base, Computed):
    field_name = u"基差"
    col_name = u"沥青山东09基差"
    axhline = 0
    def get_ts_whole_progress(self):
        relevant_col_list = [u"沥青现货价格_山东", "BU09合约收盘价"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"沥青现货价格_山东"] - tmp_total[u"BU09合约收盘价"]
        return tmp_total
    
    def seasonal_plot(self, title=None, start_year=None, axhline=None):
        tmp_df_interpolated, fig, axis = super(LiQingShanDong09JiCha, self).seasonal_plot(title=self.col_name, axhline=self.axhline, date_constraint=[9, 17])
        axis = Plot_Base.add_month_span(axis, tmp_df_interpolated, 9)
        return tmp_df_interpolated, fig, axis

    
class LiQingShanDong12JiCha(spread_base, Computed):
    field_name = u"基差"
    col_name = u"沥青山东12基差"
    axhline = 0
    def get_ts_whole_progress(self):
        relevant_col_list = [u"沥青现货价格_山东", "BU12合约收盘价"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"沥青现货价格_山东"] - tmp_total[u"BU12合约收盘价"]
        return tmp_total
    
    def seasonal_plot(self, title=None, start_year=None, axhline=None):
        tmp_df_interpolated, fig, axis = super(LiQingShanDong12JiCha, self).seasonal_plot(title=self.col_name, axhline=self.axhline, date_constraint=[12, 17])
        axis = Plot_Base.add_month_span(axis, tmp_df_interpolated, 12)
        return tmp_df_interpolated, fig, axis

class LiQingHuaNan06JiCha(spread_base, Computed):
    field_name = u"基差"
    col_name = u"沥青华南06基差"
    axhline = 0
    def get_ts_whole_progress(self):
        relevant_col_list = [u"沥青现货价格_华南", "BU06合约收盘价"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"沥青现货价格_华南"] - tmp_total[u"BU06合约收盘价"]
        return tmp_total
    
    def seasonal_plot(self, title=None, start_year=None, axhline=None):
        tmp_df_interpolated, fig, axis = super(LiQingHuaNan06JiCha, self).seasonal_plot(title=self.col_name, axhline=self.axhline, date_constraint=[6, 17])
        axis = Plot_Base.add_month_span(axis, tmp_df_interpolated, 6)
        return tmp_df_interpolated, fig, axis


class LiQingHuaNan09JiCha(spread_base, Computed):
    field_name = u"基差"
    col_name = u"沥青华南09基差"
    axhline = 0
    def get_ts_whole_progress(self):
        relevant_col_list = [u"沥青现货价格_华南", "BU09合约收盘价"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"沥青现货价格_华南"] - tmp_total[u"BU09合约收盘价"]
        return tmp_total
    
    def seasonal_plot(self, title=None, start_year=None, axhline=None):
        tmp_df_interpolated, fig, axis = super(LiQingHuaNan09JiCha, self).seasonal_plot(title=self.col_name, axhline=self.axhline, date_constraint=[9, 17])
        axis = Plot_Base.add_month_span(axis, tmp_df_interpolated, 9)
        return tmp_df_interpolated, fig, axis

    
class LiQingHuaNan12JiCha(spread_base, Computed):
    field_name = u"基差"
    col_name = u"沥青华南12基差"
    axhline = 0
    def get_ts_whole_progress(self):
        relevant_col_list = [u"沥青现货价格_华南", "BU12合约收盘价"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"沥青现货价格_华南"] - tmp_total[u"BU12合约收盘价"]
        return tmp_total
    
    def seasonal_plot(self, title=None, start_year=None, axhline=None):
        tmp_df_interpolated, fig, axis = super(LiQingHuaNan12JiCha, self).seasonal_plot(title=self.col_name, axhline=self.axhline, date_constraint=[12, 17])
        axis = Plot_Base.add_month_span(axis, tmp_df_interpolated, 12)
        return tmp_df_interpolated, fig, axis


###########################################################################################################################
""" 品种价差(计算指标) """ 

class ShanDongChaiYouMinusLiQingJiaCha(spread_base, Computed):
    field_name = u"品种价差"
    col_name = u"山东柴油-沥青价差"
    def get_ts_whole_progress(self):
        relevant_col_list = [u"柴油_0#_山东地炼", "沥青现货价格_山东"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"柴油_0#_山东地炼"] - tmp_total[u"沥青现货价格_山东"]
        return tmp_total

class JiaoHuaLiaoMinusShanDongLiQingJiaCha(spread_base, Computed):
    field_name = u"品种价差"
    col_name = u"焦化料-山东沥青价差"
    def get_ts_whole_progress(self):
        relevant_col_list = [u"焦化料价格_山东", "沥青现货价格_山东"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"焦化料价格_山东"] - tmp_total[u"沥青现货价格_山东"]
        return tmp_total
    
class XinJiaPoRanLiaoYou180CSTMinusLiQingJiaCha(spread_base, Computed):
    field_name = u"品种价差"
    col_name = u"新加坡燃料油180CST-沥青价差"
    def get_ts_whole_progress(self):
        relevant_col_list = [u"新加坡燃料油180CST现货价格", "沥青现货价格_FOB_新加坡"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"新加坡燃料油180CST现货价格"] - tmp_total[u"沥青现货价格_FOB_新加坡"]
        return tmp_total
    
class XinJiaPoRanLiaoYou380CSTMinusLiQingJiaCha(spread_base, Computed):
    field_name = u"品种价差"
    col_name = u"新加坡燃料油380CST-沥青价差"
    def get_ts_whole_progress(self):
        relevant_col_list = [u"新加坡燃料油380CST现货价格", "沥青现货价格_FOB_新加坡"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"新加坡燃料油380CST现货价格"] - tmp_total[u"沥青现货价格_FOB_新加坡"]
        return tmp_total

class XinJiaPoRanLiaoYou380CSTMinus180CST(spread_base, Computed):
    field_name = u"品种价差"
    col_name = u"新加坡燃料油380CST-180CST价差"
    start_year = 2014
    def get_ts_whole_progress(self):
        relevant_col_list = [u"新加坡燃料油380CST现货价格", "新加坡燃料油180CST现货价格"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"新加坡燃料油380CST现货价格"] - tmp_total[u"新加坡燃料油180CST现货价格"]
        return tmp_total
    
class QiYouMinusLiQingJiaCha(spread_base, Computed):
    field_name = u"品种价差"
    col_name = u"汽油-沥青价差"
    def get_ts_whole_progress(self):
        relevant_col_list = [u"汽油_华北", "沥青现货价格_山东"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"汽油_华北"] - tmp_total[u"沥青现货价格_山东"]
        return tmp_total





    
###########################################################################################################################
""" 月间价差(计算指标) """ 

class BU06Minus09JiaCha(spread_base, Computed):
    field_name = u"月间价差"
    col_name = u"BU6_9价差"
    axhline = 0
    start_year = 2014
    def get_ts_whole_progress(self):
        month_list = ["06", "09"]
        all_main_quote_df = BU_Base.get_BU_main_month_quote_df()
        spread_series = main_month_quote_2_spread_series(month_list, all_main_quote_df)
        tmp_df = pd.DataFrame([spread_series], index=[self.col_name]).T
        return tmp_df

    def seasonal_plot(self, title=None, start_year=None, axhline=None):
        tmp_df_interpolated, fig, axis = super(BU06Minus09JiaCha, self).seasonal_plot(title=self.col_name, start_year = self.start_year, 
                                              axhline=self.axhline, date_constraint=[6, 17])
        axis = Plot_Base.add_month_span(axis, tmp_df_interpolated, 6)
        return tmp_df_interpolated, fig, axis
        
class BU09MinusBU12JiaCha(spread_base, Computed):
    field_name = u"月间价差"
    col_name = u"BU9_12价差"
    axhline = 0
    start_year = 2014
    def get_ts_whole_progress(self):
        month_list = ["09", "12"]
        all_main_quote_df = BU_Base.get_BU_main_month_quote_df()
        spread_series = main_month_quote_2_spread_series(month_list, all_main_quote_df)
        tmp_df = pd.DataFrame([spread_series], index=[self.col_name]).T
        return tmp_df

    def seasonal_plot(self, title=None, start_year=None, axhline=None):
        tmp_df_interpolated, fig, axis = super(BU09MinusBU12JiaCha, self).seasonal_plot(title=self.col_name, start_year = self.start_year, 
                                              axhline=self.axhline, date_constraint=[9, 17])
        axis = Plot_Base.add_month_span(axis, tmp_df_interpolated, 9)
        return tmp_df_interpolated, fig, axis    
      

class BU12MinusBU06JiaCha(spread_base, Computed):
    field_name = u"月间价差"
    col_name = u"BU12_6价差"
    axhline = 0
    start_year = 2014
    def get_ts_whole_progress(self):
        month_list = ["12", "06"]
        all_main_quote_df = BU_Base.get_BU_main_month_quote_df()
        spread_series = main_month_quote_2_spread_series(month_list, all_main_quote_df)
        tmp_df = pd.DataFrame([spread_series], index=[self.col_name]).T
        return tmp_df

    def seasonal_plot(self, title=None, start_year=None, axhline=None):
        tmp_df_interpolated, fig, axis = super(BU12MinusBU06JiaCha, self).seasonal_plot(title=self.col_name, start_year = self.start_year, 
                                              axhline=self.axhline, date_constraint=[12, 17])
        axis = Plot_Base.add_month_span(axis, tmp_df_interpolated, 12)
        return tmp_df_interpolated, fig, axis  
        

class BU06MinusBU12JiaCha(spread_base, Computed):
    field_name = u"月间价差"
    col_name = u"BU6_12价差"
    axhline = 0
    start_year = 2014
    def get_ts_whole_progress(self):
        month_list = ["06", "12"]
        all_main_quote_df = BU_Base.get_BU_main_month_quote_df()
        spread_series = main_month_quote_2_spread_series(month_list, all_main_quote_df)
        tmp_df = pd.DataFrame([spread_series], index=[self.col_name]).T
        return tmp_df

    def seasonal_plot(self, title=None, start_year=None, axhline=None):
        tmp_df_interpolated, fig, axis = super(BU06MinusBU12JiaCha, self).seasonal_plot(title=self.col_name, start_year = self.start_year, 
                                              axhline=self.axhline, date_constraint=[6, 17])
        axis = Plot_Base.add_month_span(axis, tmp_df_interpolated, 6)
        return tmp_df_interpolated, fig, axis 
#
#class BU01MinusBU06JiaCha(spread_base, Computed):
#    field_name = u"月间价差"
#    col_name = u"BU1_6价差"
#    axhline = 0
#    start_year = 2014
#    def get_ts_whole_progress(self):
#        month_list = ["01", "06"]
#        all_main_quote_df = BU_Base.get_BU_quote_df()
#        spread_series = main_month_quote_2_spread_series(month_list, all_main_quote_df)
#        tmp_df = pd.DataFrame([spread_series], index=[self.col_name]).T
#        return tmp_df
#
#    def seasonal_plot(self, title=None, start_year=None, axhline=None):
#        tmp_df_interpolated, fig, axis = super(BU01MinusBU06JiaCha, self).seasonal_plot(title=self.col_name, start_year = self.start_year, 
#                                              axhline=self.axhline, date_constraint=[1, 17])
#        axis = Plot_Base.add_month_span(axis, tmp_df_interpolated, 1)
#        return tmp_df_interpolated, fig, axis 

if __name__ == "__main__":
#    ts = BU06OverBrentBiJia().get_ts()
    ts = XinJiaPoRanLiaoYou380CSTMinus180CST().seasonal_plot()
    
    
    
    
    
    
    
    
    
    
    
    
    