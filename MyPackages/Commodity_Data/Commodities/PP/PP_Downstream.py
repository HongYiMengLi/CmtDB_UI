# -*- coding: utf-8 -*-
"""
Created on Wed Aug 29 11:32:23 2018

@author: Administrator
"""

import pandas as pd
from datetime import datetime
from .PP_Base import PP_Base
from . import PP_SpotPrice
from ...Base.DataType_Base import Manual, Computed, WindData
from ...Base.Plot_Base import Plot_Base
from matplotlib.ticker import FuncFormatter

class downstream_base(PP_Base, Plot_Base):
    table_english_name = "Downstream"
    table_chinese_name = u"下游"
    
    def output(self):
        print("Downstream")
    
    def get_relevant_df(self, col_list):
        local_col_name_list = downstream_base.get_all_table_classname()
        col_cls_list = []
        for x in col_list:
            col_cls_name = str(PP_Base.get_class_name(x))
            if col_cls_name not in local_col_name_list:
                col_cls_list.append(eval(PP_Base.get_table_class_full_variable(x)))
            else:
                col_cls_list.append(eval(col_cls_name))
        ts_list = [x().get_ts() for x in col_cls_list]
        tmp_table_df = pd.concat(ts_list, axis=1).dropna(how="all")
        return tmp_table_df 
    
    
###########################################################################################################################
""" BOPP价格 """   

class ZheJiangHouGuangMo(downstream_base, Manual):
    field_name = u"BOPP"
    col_name = u"BOPP市场价_浙江"

class XiaoShanHuaYi(downstream_base, Manual):
    field_name = u"BOPP"
    col_name = u"BOPP出厂价_萧山华益"

class ZheJiangYiMei(downstream_base, Manual):
    field_name = u"BOPP"
    col_name = u"BOPP出厂价_浙江伊美"

###########################################################################################################################
""" BOPP加工费 """ 
""" 计算指标 """

class BOPPShiChangPingJunJiaGongFei(downstream_base, Computed):
    field_name = u"BOPP加工费"
    col_name = u"BOPP加工费_浙江市场"
    start_year = 2015
    def get_ts_whole_progress(self):
        relevant_col_list = [u"BOPP市场价_浙江", u"PP拉丝价格_华东"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"BOPP市场价_浙江"] - tmp_total[u"PP拉丝价格_华东"]
        return tmp_total
    
class XiaoShanHuaYiJiaGongFei(downstream_base, Computed):
    field_name = u"BOPP加工费"
    col_name = u"BOPP加工费_萧山华益"
    fig_title = u"萧山华益BOPP加工费季节性"
    start_year = 2015
    def get_ts_whole_progress(self):
        relevant_col_list = [u"BOPP出厂价_萧山华益", u"PP拉丝价格_华东"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"BOPP出厂价_萧山华益"] - tmp_total[u"PP拉丝价格_华东"]
        return tmp_total
    
class ZheJiangYiMeiJiaGongFei(downstream_base, Computed):
    field_name = u"BOPP加工费"
    col_name = u"BOPP加工费_浙江伊美"
    fig_title = u"浙江伊美BOPP加工费季节性"
    start_year = 2015
    def get_ts_whole_progress(self):
        relevant_col_list = [u"BOPP出厂价_浙江伊美", u"PP拉丝价格_华东"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"BOPP出厂价_浙江伊美"] - tmp_total[u"PP拉丝价格_华东"]
        return tmp_total

if __name__ == "__main__":
    ts = ZheJiangYiMeiJiaGongFei().get_ts()