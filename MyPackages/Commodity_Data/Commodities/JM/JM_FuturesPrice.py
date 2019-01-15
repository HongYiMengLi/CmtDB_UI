# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 15:20:08 2018

@author: 李弘一萌
"""

import pandas as pd
from datetime import datetime
from .JM_Base import JM_Base
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

class futures_price_base(JM_Base, Plot_Base):
    table_english_name = "FuturesPrice"
    table_chinese_name = u"期货价格"
#    original_db_filepath = data_path + u"LPP价格数据库.xlsx"
    
    def output(self):
        print("FuturesPrice")
    
    def get_relevant_df(self, col_list):
        local_col_name_list = futures_price_base.get_all_table_classname()
        col_cls_list = []
        for x in col_list:
            col_cls_name = str(JM_Base.get_class_name(x))
            if col_cls_name not in local_col_name_list:
                col_cls_list.append(eval(JM_Base.get_table_class_full_variable(x)))
            else:
                col_cls_list.append(eval(col_cls_name))
        ts_list = [x().get_ts() for x in col_cls_list]
        tmp_table_df = pd.concat(ts_list, axis=1).dropna(how="all")
        return tmp_table_df 
    
        
###########################################################################################################################
""" 国内期货价格 """     
    
    
class JM01HeYueShouPanJia(futures_price_base, Computed):
    field_name = u"国内期货价格"
    col_name = u"JM01合约收盘价"
    def get_ts_whole_progress(self):
        quote_df = self.get_JM_quote_df(month=1)
        quote_ts = month_quote_df_2_series(quote_df)
        quote_ts.name = self.col_name
        return quote_ts.to_frame()


class JM05HeYueShouPanJia(futures_price_base, Computed):
    field_name = u"国内期货价格"
    col_name = u"JM05合约收盘价"
    def get_ts_whole_progress(self):
        quote_df = self.get_JM_quote_df(month=5)
        quote_ts = month_quote_df_2_series(quote_df)
        quote_ts.name = self.col_name
        return quote_ts.to_frame()


class JM09HeYueShouPanJia(futures_price_base, Computed):
    field_name = u"国内期货价格"
    col_name = u"JM09合约收盘价"
    def get_ts_whole_progress(self):
        quote_df = self.get_JM_quote_df(month=9)
        quote_ts = month_quote_df_2_series(quote_df)
        quote_ts.name = self.col_name  
        return quote_ts.to_frame()
    
    
if __name__ == "__main__":
    df = TieKuang09HeYueShouPanJia().get_ts()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    