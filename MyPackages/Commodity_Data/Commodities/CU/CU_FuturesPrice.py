# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 15:20:08 2018

@author: 李弘一萌
"""

import pandas as pd
from datetime import datetime
from .CU_Base import CU_Base
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

class futures_price_base(CU_Base, Plot_Base):
    table_english_name = "FuturesPrice"
    table_chinese_name = u"期货数据"
#    original_db_filepath = data_path + u"LPP价格数据库.xlsx"
    
    def output(self):
        print("FuturesPrice")
    
    def get_relevant_df(self, col_list):
        local_col_name_list = futures_price_base.get_all_table_classname()
        col_cls_list = []
        for x in col_list:
            col_cls_name = str(CU_Base.get_class_name(x))
            if col_cls_name not in local_col_name_list:
                col_cls_list.append(eval(CU_Base.get_table_class_full_variable(x)))
            else:
                col_cls_list.append(eval(col_cls_name))
        ts_list = [x().get_ts() for x in col_cls_list]
        tmp_table_df = pd.concat(ts_list, axis=1).dropna(how="all")
        return tmp_table_df 
    
    
    
    
    
    
    
###########################################################################################################################
""" 铜期货价 """     


class QiHuoShouPanJia_LianSan_YinJiTong(futures_price_base, WindData):
    field_name = u"铜期货价"
    col_name = u"期货收盘价(连三)_阴极铜"
    wind_code = "S0116879"   
    
class QiHuoShouPanJia_LME3GeYueTong(futures_price_base, WindData):
    field_name = u"铜期货价"
    col_name = u"期货收盘价_LME3个月铜"
    wind_code = "S0029750"   
        
class LME3GeYueTong15Dian_DianZiPan_JiaGe(futures_price_base, Manual):
    field_name = u"铜期货价"
    col_name = u"15点LME3个月铜(电子盘)价格"

    
    
    
if __name__ == "__main__":
    df = CU10HeYueShouPanJia().get_ts()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    