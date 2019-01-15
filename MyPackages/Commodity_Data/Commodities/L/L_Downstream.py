# -*- coding: utf-8 -*-
"""
Created on Mon Aug 27 08:34:56 2018

@author: 李弘一萌
"""

import pandas as pd
from datetime import datetime
from .L_Base import L_Base
from . import L_SpotPrice, L_Others, L_Macro
from ...Base.DataType_Base import Manual, Computed, WindData
from ...Base.Plot_Base import Plot_Base
from matplotlib.ticker import FuncFormatter

class downstream_base(L_Base, Plot_Base):
    table_english_name = "Downstream"
    table_chinese_name = u"下游"
#    original_db_filepath = data_path + u"LPP价格数据库.xlsx"
    
    def output(self):
        print("Downstream")
    
    def get_relevant_df(self, col_list):
        local_col_name_list = downstream_base.get_all_table_classname()
        col_cls_list = []
        for x in col_list:
            col_cls_name = str(L_Base.get_class_name(x))
            if col_cls_name not in local_col_name_list:
                col_cls_list.append(eval(L_Base.get_table_class_full_variable(x)))
            else:
                col_cls_list.append(eval(col_cls_name))
        ts_list = [x().get_ts() for x in col_cls_list]
        tmp_table_df = pd.concat(ts_list, axis=1).dropna(how="all")
        return tmp_table_df  
    
    
    
###########################################################################################################################
""" 农膜价格 """  

class BaiMoDiDuan(downstream_base, Manual):
    field_name = u"农膜价格"
    col_name = u"白膜低端价格"

class BaiMoGaoDuan(downstream_base, Manual):
    field_name = u"农膜价格"
    col_name = u"白膜高端价格"

class ShuangFangMoDiDuan(downstream_base, Manual):
    field_name = u"农膜价格"
    col_name = u"双防膜低端价格"

class ShuangFangMoGaoDuan(downstream_base, Manual):
    field_name = u"农膜价格"
    col_name = u"双防膜高端价格"

class DiMoDiDuan(downstream_base, Manual):
    field_name = u"农膜价格"
    col_name = u"地膜低端价格"
    
class DiMoGaoDuan(downstream_base, Manual):
    field_name = u"农膜价格"
    col_name = u"地膜高端价格"

class XiGuaMoDiDuan(downstream_base, Manual):
    field_name = u"农膜价格"
    col_name = u"西瓜膜低端价格"

class XiGuaMoGaoDuan(downstream_base, Manual):
    field_name = u"农膜价格"
    col_name = u"西瓜膜高端价格"

""" 计算指标 """
 
class BaiMoJunJia(downstream_base, Computed):
    field_name = u"农膜价格"
    col_name = u"白膜均价"
    def get_ts_whole_progress(self):
        relevant_col_list = [u"白膜低端价格", u"白膜高端价格"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total.mean(axis=1)
        return tmp_total
    
class ShuangFangMoJunJia(downstream_base, Computed):
    field_name = u"农膜价格"
    col_name = u"双防膜均价"
    def get_ts_whole_progress(self):
        relevant_col_list = [u"双防膜低端价格", u"双防膜高端价格"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total.mean(axis=1)
        return tmp_total
    
class DiMoJunJia(downstream_base, Computed):
    field_name = u"农膜价格"
    col_name = u"地膜均价"
    def get_ts_whole_progress(self):
        relevant_col_list = [u"地膜低端价格", u"地膜高端价格"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total.mean(axis=1)
        return tmp_total
    
class XiGuaMoJunJia(downstream_base, Computed):
    field_name = u"农膜价格"
    col_name = u"西瓜膜均价"
    def get_ts_whole_progress(self):
        relevant_col_list = [u"西瓜膜低端价格", u"西瓜膜高端价格"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total.mean(axis=1)
        return tmp_total
    
###########################################################################################################################
""" 农膜开工 """

class DaXingRiGuangMoChangKaiGongLvDiDuan(downstream_base, Manual):
    field_name = u"农膜开工"
    col_name = u"大型日光膜厂低端开工率"

class DaXingRiGuangMoChangKaiGongLvGaoDuan(downstream_base, Manual):
    field_name = u"农膜开工"
    col_name = u"大型日光膜厂高端开工率"

class WanDunGongNengMoChangKaiGongLvDiDuan(downstream_base, Manual):
    field_name = u"农膜开工"
    col_name = u"万吨功能膜厂低端开工率"

class WanDunGongNengMoChangKaiGongLvGaoDuan(downstream_base, Manual):
    field_name = u"农膜开工"
    col_name = u"万吨功能膜厂高端开工率"

class DaXingDiMoChangKaiGongLvDiDuan(downstream_base, Manual):
    field_name = u"农膜开工"
    col_name = u"大型地膜厂低端开工率"    

class DaXingDiMoChangKaiGongLvGaoDuan(downstream_base, Manual):
    field_name = u"农膜开工"
    col_name = u"大型地膜厂高端开工率"

""" 计算指标 """
    
class DaXingRiGuangMoChangKaiGongLv(downstream_base, Computed):
    field_name = u"农膜开工"
    col_name = u"大型日光膜厂开工率"
    def get_ts_whole_progress(self):
        relevant_col_list = [u"大型日光膜厂低端开工率", u"大型日光膜厂高端开工率"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total.mean(axis=1)
        return tmp_total
    
class WanDunGongNengMoChangKaiGongLv(downstream_base, Computed):
    field_name = u"农膜开工"
    col_name = u"万吨功能膜厂开工率"
    start_year = 2015
    fig_title = u"功能膜(棚膜)开工率"
    
    def get_ts_whole_progress(self):
        relevant_col_list = [u"万吨功能膜厂低端开工率", u"万吨功能膜厂高端开工率"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total.mean(axis=1)
        return tmp_total
    
    def seasonal_plot(self, title=None, start_year=None, axhline=None):
        tmp_df_interpolated, fig, axis = super(downstream_base, self).seasonal_plot(title=title, start_year=start_year)
        axis.yaxis.set_major_formatter(FuncFormatter(lambda y, _: '{:.0%}'.format(y)))
        return tmp_df_interpolated, fig, axis
    
class DaXingDiMoChangKaiGongLv(downstream_base, Computed):
    field_name = u"农膜开工"
    col_name = u"大型地膜厂开工率"
    start_year = 2015
    
    def get_ts_whole_progress(self):
        relevant_col_list = [u"大型地膜厂低端开工率", u"大型地膜厂高端开工率"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total.mean(axis=1)
        return tmp_total
    
    def seasonal_plot(self, title=None, start_year=None, axhline=None):
        tmp_df_interpolated, fig, axis = super(downstream_base, self).seasonal_plot(title=title, start_year=start_year)
        axis.yaxis.set_major_formatter(FuncFormatter(lambda y, _: '{:.0%}'.format(y)))
        return tmp_df_interpolated, fig, axis


###########################################################################################################################
""" 农膜利润 """
""" 计算指标 """   
class ShuangFangMoLiRun(downstream_base, Computed):
    field_name = u"农膜利润"
    col_name = u"双防膜利润"
    fig_title = u"功能膜利润"
    def get_ts_whole_progress(self):
        relevant_col_list = [u"双防膜均价", u"LD膜价格_齐鲁石化2012TN00", u"LLD膜价格_齐鲁石化7042"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"双防膜均价"] - 0.4 * tmp_total[u"LD膜价格_齐鲁石化2012TN00"] - 0.6 * \
                                    tmp_total[u"LLD膜价格_齐鲁石化7042"] 
        return tmp_total
    
class DiMoLiRun(downstream_base, Computed):
    field_name = u"农膜利润"
    col_name = u"地膜利润"
    start_year = 2015
    axhline = 0
    def get_ts_whole_progress(self):
        relevant_col_list = [u"地膜均价", u"LLD膜价格_齐鲁石化7042"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"地膜均价"] - tmp_total[u"LLD膜价格_齐鲁石化7042"]
        return tmp_total    
    
    
if __name__ == "__main__":

    
    ts1 = DiMoLiRun().get_ts()
#    ts2, fig2, axis2 = ShuangFangMoLiRun().seasonal_plot()         
    