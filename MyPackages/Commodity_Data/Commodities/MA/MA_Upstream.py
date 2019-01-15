# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 10:44:58 2018

@author: 李弘一萌
"""

import pandas as pd
from datetime import datetime
from .MA_Base import MA_Base
from . import MA_Macro, MA_SpotPrice, MA_FuturesPrice
from ...Base.DataType_Base import Manual, Computed, WindData
from ...Base.Plot_Base import Plot_Base
from matplotlib.ticker import FuncFormatter

class upstream_base(MA_Base, Plot_Base):
    table_english_name = "Upstream"
    table_chinese_name = u"上游"
#    original_db_filepath = data_path + u"LPP价格数据库.xlsx"
    
    def output(self):
        print("Upstream")
    
    def get_relevant_df(self, col_list):
        local_col_name_list = upstream_base.get_all_table_classname()
        col_cls_list = []
        for x in col_list:
            col_cls_name = str(MA_Base.get_class_name(x))
            if col_cls_name not in local_col_name_list:
                col_cls_list.append(eval(MA_Base.get_table_class_full_variable(x)))
            else:
                col_cls_list.append(eval(col_cls_name))
        ts_list = [x().get_ts() for x in col_cls_list]
        tmp_table_df = pd.concat(ts_list, axis=1).dropna(how="all")
        return tmp_table_df

###########################################################################################################################
""" 煤制 """  

class KengKouMeiJiaGe_DongSheng(upstream_base, WindData):
    field_name = u"煤制"
    col_name = u"坑口煤价格_东胜"
    wind_code = "S5101766"


class JiaChunMeiZhiLiRun(upstream_base, Computed):
    field_name = u"煤制"
    col_name = u"甲醇煤制利润"
    start_year = 2014
    def get_ts_whole_progress(self):
        relevant_col_list = [u"甲醇价格_内蒙古", u"坑口煤价格_东胜"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"甲醇价格_内蒙古"] - tmp_total[u"坑口煤价格_东胜"] * 2.1 - 600
        return tmp_total
    
###########################################################################################################################
""" 进口利润 """  
     
class JiaChunJinKouLiRun(upstream_base, Computed):
    field_name = u"进口利润"
    col_name = u"甲醇进口利润"
    axhline = 0
    start_year = 2014
    def get_ts_whole_progress(self):
        relevant_col_list = [u"甲醇价格_江苏", u"甲醇价格_CFR_中国", u"人民币汇率中间价"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"甲醇价格_江苏"] - tmp_total[u"甲醇价格_CFR_中国"] * tmp_total[u"人民币汇率中间价"] * 1.17 * 1.05 - 45
        return tmp_total
    
    
###########################################################################################################################
""" 天然气制 """ 

class TianRanQiJiaGe(upstream_base, WindData):
    field_name = u"天然气制"
    col_name = u"天然气价格"
    wind_code = "S5122533"
    

    
if __name__ == "__main__":
    df= JiaChunMeiZhiLiRun().get_ts()    
    
    
    
    
    
    
    
    
    
    
    
    
    
    