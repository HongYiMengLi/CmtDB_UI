# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 15:20:08 2018

@author: 李弘一萌
"""

import pandas as pd
from datetime import datetime
from .CF_Base import CF_Base
from ...Base.DataType_Base import Manual, Computed, WindData
from ...Base.Plot_Base import Plot_Base
from matplotlib.ticker import FuncFormatter

def month_quote_df_2_series(df):
    ts_list = []
    for col in df.columns.tolist():
        tmp_series = df[col].dropna()
        ts_list.append(tmp_series)
    result = pd.concat(ts_list)
    result = result[~result.index.duplicated()]
    return result

class futures_price_base(CF_Base, Plot_Base):
    table_english_name = "FuturesPrice"
    table_chinese_name = u"期货盘面"
#    original_db_filepath = data_path + u"LPP价格数据库.xlsx"
    
    def output(self):
        print("FuturesPrice")
    
    def get_relevant_df(self, col_list):
        local_col_name_list = futures_price_base.get_all_table_classname()
        col_cls_list = []
        for x in col_list:
            col_cls_name = str(CF_Base.get_class_name(x))
            if col_cls_name not in local_col_name_list:
                col_cls_list.append(eval(CF_Base.get_table_class_full_variable(x)))
            else:
                col_cls_list.append(eval(col_cls_name))
        ts_list = [x().get_ts() for x in col_cls_list]
        tmp_table_df = pd.concat(ts_list, axis=1).dropna(how="all")
        return tmp_table_df 
    
    
        
###########################################################################################################################
""" 合约价格 """     

    
class CF01HeYueShouPanJia(futures_price_base, Computed):
    field_name = u"合约价格"
    col_name = u"CF01合约收盘价"
    def get_ts_whole_progress(self):
        quote_df = self.get_CF_quote_df(month=1)
        quote_ts = month_quote_df_2_series(quote_df)
        quote_ts.name = self.col_name
        return quote_ts.to_frame()


class CF05HeYueShouPanJia(futures_price_base, Computed):
    field_name = u"合约价格"
    col_name = u"CF05合约收盘价"
    def get_ts_whole_progress(self):
        quote_df = self.get_CF_quote_df(month=5)
        quote_ts = month_quote_df_2_series(quote_df)
        quote_ts.name = self.col_name
        return quote_ts.to_frame()


class CF09HeYueShouPanJia(futures_price_base, Computed):
    field_name = u"合约价格"
    col_name = u"CF09合约收盘价"
    def get_ts_whole_progress(self):
        quote_df = self.get_CF_quote_df(month=9)
        quote_ts = month_quote_df_2_series(quote_df)
        quote_ts.name = self.col_name  
        return quote_ts.to_frame()

class CY01HeYueShouPanJia(futures_price_base, Computed):
    field_name = u"合约价格"
    col_name = u"CY01合约收盘价"
    def get_ts_whole_progress(self):
        quote_df = self.get_CY_quote_df(month=1)
        quote_ts = month_quote_df_2_series(quote_df)
        quote_ts.name = self.col_name
        return quote_ts.to_frame()


class CY05HeYueShouPanJia(futures_price_base, Computed):
    field_name = u"合约价格"
    col_name = u"CY05合约收盘价"
    def get_ts_whole_progress(self):
        quote_df = self.get_CY_quote_df(month=5)
        quote_ts = month_quote_df_2_series(quote_df)
        quote_ts.name = self.col_name
        return quote_ts.to_frame()


class CY09HeYueShouPanJia(futures_price_base, Computed):
    field_name = u"合约价格"
    col_name = u"CY09合约收盘价"
    def get_ts_whole_progress(self):
        quote_df = self.get_CY_quote_df(month=9)
        quote_ts = month_quote_df_2_series(quote_df)
        quote_ts.name = self.col_name  
        return quote_ts.to_frame()
    
class ZhengMianQiHuoJieSuanJia(futures_price_base, WindData):
    field_name = u"合约价格"
    col_name = u"郑棉期货结算价(连续)"    
    wind_code = "S0068131" 


###########################################################################################################################
""" 国内合约持仓量 """ 

class ZhengMianChiCangLiang_ZongHeYue(futures_price_base, WindData):
    field_name = u"国内合约持仓量"
    col_name = u"郑棉持仓量_总合约"    
    wind_code = "M0086465"

###########################################################################################################################
""" CFTC持仓量 """ 

class ICEMianHuaChiCang_FeiShangYeDuoTou(futures_price_base, WindData):
    field_name = u"CFTC持仓量"
    col_name = u"ICE棉花持仓_非商业多头"    
    wind_code = "S0107788"

class ICEMianHuaChiCang_FeiShangYeKongTou(futures_price_base, WindData):
    field_name = u"CFTC持仓量"
    col_name = u"ICE棉花持仓_非商业空头"    
    wind_code = "S0107789"
    
class ICEMianHuaChiCang_FeiShangYeTaoLi(futures_price_base, WindData):
    field_name = u"CFTC持仓量"
    col_name = u"ICE棉花持仓_非商业套利"    
    wind_code = "S0107790"
    









    
if __name__ == "__main__":
    df = CF12HeYueShouPanJia().get_ts()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    