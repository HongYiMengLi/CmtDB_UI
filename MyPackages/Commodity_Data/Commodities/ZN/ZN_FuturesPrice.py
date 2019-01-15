# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 15:20:08 2018

@author: 李弘一萌
"""

import pandas as pd
from datetime import datetime
from .ZN_Base import ZN_Base
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

class futures_price_base(ZN_Base, Plot_Base):
    table_english_name = "FuturesPrice"
    table_chinese_name = u"期货数据"
    
    def output(self):
        print("FuturesPrice")
    
    def get_relevant_df(self, col_list):
        local_col_name_list = futures_price_base.get_all_table_classname()
        col_cls_list = []
        for x in col_list:
            col_cls_name = str(ZN_Base.get_class_name(x))
            if col_cls_name not in local_col_name_list:
                col_cls_list.append(eval(ZN_Base.get_table_class_full_variable(x)))
            else:
                col_cls_list.append(eval(col_cls_name))
        ts_list = [x().get_ts() for x in col_cls_list]
        tmp_table_df = pd.concat(ts_list, axis=1).dropna(how="all")
        return tmp_table_df 
    
    
    
    
    
    
    
###########################################################################################################################
""" 价格 """     
    
class LME3GeYueXin15Dian_DianZiPanJiaGe(futures_price_base, Manual):
    field_name = u"价格"
    col_name = u"15点LME3个月锌(电子盘)价格"    

class QiHuoShouPanJia_DianZiPan_LME3GeYueXin(futures_price_base, WindData):
    field_name = u"价格"
    col_name = u"期货收盘价(电子盘)_LME3个月锌"
    wind_code = "S0029758"   

class XianHuoJieSuanJia_LMEXin(futures_price_base, WindData):
    field_name = u"价格"
    col_name = u"现货结算价_LME锌"
    wind_code = "S0029759"   

class XinQiHuoShouPanJia_LianSan(futures_price_base, WindData):
    field_name = u"价格"
    col_name = u"锌期货收盘价(连三)"
    wind_code = "S0116883"   

    
class XinQiHuoShouPanJia_HuoYueHeYue(futures_price_base, WindData):
    field_name = u"价格"
    col_name = u"锌期货收盘价(活跃合约)"
    wind_code = "M0066357"   
        
class XinQiHuoJieSuanJia_HuoYueHeYue(futures_price_base, WindData):
    field_name = u"价格"
    col_name = u"锌期货结算价(活跃合约)"
    wind_code = "S0181391"   

    
###########################################################################################################################
""" 成交量 """     

class QiHuoChengJiaoLiang_LME3GeYueXin(futures_price_base, WindData):
    field_name = u"成交量"
    col_name = u"期货成交量_LME3个月锌"
    wind_code = "M0096637"  

class XinQiHuoChengJiaoLiang_HuoYueHeYue(futures_price_base, WindData):
    field_name = u"成交量"
    col_name = u"锌期货成交量(活跃合约)"
    wind_code = "M0096580" 

###########################################################################################################################
""" 持仓量 """     

class LMEXinChiCangLiang(futures_price_base, WindData):
    field_name = u"持仓量"
    col_name = u"LME锌持仓量"
    wind_code = "S5806054" 

class XinQiHuoChiCangLiang_HuoYueHeYue(futures_price_base, WindData):
    field_name = u"持仓量"
    col_name = u"锌期货持仓量(活跃合约)"
    wind_code = "M0096613" 
    
    
    
    
if __name__ == "__main__":
    df = ZN10HeYueShouPanJia().get_ts()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    