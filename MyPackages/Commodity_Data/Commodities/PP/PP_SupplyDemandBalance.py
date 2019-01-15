# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 09:13:47 2018

@author: 李弘一萌
"""

import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt
from .PP_Base import PP_Base
from . import PP_Macro
from . import PP_Inventory
from . import PP_Others
from ...Base.DataType_Base import Manual, Computed, WindData, Auto
from ...Base.Plot_Base import Plot_Base
from matplotlib.ticker import FuncFormatter
import calendar



class sdb_base(PP_Base, Plot_Base):
    table_english_name = "SupplyDemandBalance"
    table_chinese_name = u"供需平衡表"
    
    def output(self):
        print("SupplyDemandBalance")
    
    def get_relevant_df(self, col_list):
        local_col_name_list = sdb_base.get_all_table_classname()
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
    
    def expected_value(self, original_name, tmp_total):
        last_date = tmp_total.index[-1]
        tmp_total["month"] = [x.month for x in tmp_total.index]
        expect_start = "%d-%d-01" % (last_date.year, last_date.month + 1) if last_date.month != 12 else \
                       "%d-%d-01" % (last_date.year + 1, 1)
        expect_end = "%d-%d-31" % (last_date.year, 12) if last_date.month != 12 else "%d-%d-01" % (last_date.year + 1, 12)
        expect_date_range = pd.date_range(start=expect_start, end=expect_end, freq="M")
        expect_ts = pd.Series([np.nan]*len(expect_date_range), index=expect_date_range)     
        if len(expect_ts) > 12:
            expect_ts = expect_ts.iloc[:12].copy()
        for i in range(len(expect_ts)):
            tmp_date = expect_ts.index[i]
            tmp_month = tmp_date.month
            tmp_hist = tmp_total[tmp_total["month"]==tmp_month].loc[:, original_name]
            tmp_expected_value = tmp_hist.iloc[-1] * (1 + tmp_hist.pct_change(1).iloc[-3:].mean())
            expect_ts.iloc[i] = tmp_expected_value
        expect_ts.name = self.col_name
        return expect_ts.to_frame()
    
    
###########################################################################################################################
""" 产能 """     
 
class PPChanNeng(sdb_base, Manual):
    field_name = u"产能"
    col_name = u"PP产能"    

###########################################################################################################################
""" 日度产量 """    

  

class PPLaSiRiDuChanLiang(sdb_base, Manual):
    field_name = u"日度产量"
    col_name = u"PP拉丝日度产量" 
    def seasonal_plot(self, title=None, start_year=None, axhline=None):
        tmp_df_interpolated, fig, axis = super(sdb_base, self).seasonal_plot(title=title, start_year=start_year)
        axis.yaxis.set_major_formatter(FuncFormatter(lambda y, _: '{:.2f}'.format(y)))
        return tmp_df_interpolated, fig, axis

class PPPuTongZhuSuRiDuChanLiang(sdb_base, Manual):
    field_name = u"日度产量"
    col_name = u"PP普通注塑日度产量" 
    def seasonal_plot(self, title=None, start_year=None, axhline=None):
        tmp_df_interpolated, fig, axis = super(sdb_base, self).seasonal_plot(title=title, start_year=start_year)
        axis.yaxis.set_major_formatter(FuncFormatter(lambda y, _: '{:.2f}'.format(y)))
        return tmp_df_interpolated, fig, axis

class PPBoBiZhuSuRiDuChanLiang(sdb_base, Manual):
    field_name = u"日度产量"
    col_name = u"PP薄壁注塑日度产量" 
    def seasonal_plot(self, title=None, start_year=None, axhline=None):
        tmp_df_interpolated, fig, axis = super(sdb_base, self).seasonal_plot(title=title, start_year=start_year)
        axis.yaxis.set_major_formatter(FuncFormatter(lambda y, _: '{:.2f}'.format(y)))
        return tmp_df_interpolated, fig, axis

class PPDiRongGongJuRiDuChanLiang(sdb_base, Manual):
    field_name = u"日度产量"
    col_name = u"PP低熔共聚日度产量" 
    def seasonal_plot(self, title=None, start_year=None, axhline=None):
        tmp_df_interpolated, fig, axis = super(sdb_base, self).seasonal_plot(title=title, start_year=start_year)
        axis.yaxis.set_major_formatter(FuncFormatter(lambda y, _: '{:.2f}'.format(y)))
        return tmp_df_interpolated, fig, axis

class PPZhongRongGongJuRiDuChanLiang(sdb_base, Manual):
    field_name = u"日度产量"
    col_name = u"PP中熔共聚日度产量" 
    def seasonal_plot(self, title=None, start_year=None, axhline=None):
        tmp_df_interpolated, fig, axis = super(sdb_base, self).seasonal_plot(title=title, start_year=start_year)
        axis.yaxis.set_major_formatter(FuncFormatter(lambda y, _: '{:.2f}'.format(y)))
        return tmp_df_interpolated, fig, axis

class PPGaoRongGongJuRiDuChanLiang(sdb_base, Manual):
    field_name = u"日度产量"
    col_name = u"PP高熔共聚日度产量" 
    def seasonal_plot(self, title=None, start_year=None, axhline=None):
        tmp_df_interpolated, fig, axis = super(sdb_base, self).seasonal_plot(title=title, start_year=start_year)
        axis.yaxis.set_major_formatter(FuncFormatter(lambda y, _: '{:.2f}'.format(y)))
        return tmp_df_interpolated, fig, axis

class PPQiTaGongJuRiDuChanLiang(sdb_base, Manual):
    field_name = u"日度产量"
    col_name = u"PP其他共聚日度产量" 
    def seasonal_plot(self, title=None, start_year=None, axhline=None):
        tmp_df_interpolated, fig, axis = super(sdb_base, self).seasonal_plot(title=title, start_year=start_year)
        axis.yaxis.set_major_formatter(FuncFormatter(lambda y, _: '{:.2f}'.format(y)))
        return tmp_df_interpolated, fig, axis

class PPXianWeiRiDuChanLiang(sdb_base, Manual):
    field_name = u"日度产量"
    col_name = u"PP纤维日度产量" 
    def seasonal_plot(self, title=None, start_year=None, axhline=None):
        tmp_df_interpolated, fig, axis = super(sdb_base, self).seasonal_plot(title=title, start_year=start_year)
        axis.yaxis.set_major_formatter(FuncFormatter(lambda y, _: '{:.2f}'.format(y)))
        return tmp_df_interpolated, fig, axis

class BOPPRiDuChanLiang(sdb_base, Manual):
    field_name = u"日度产量"
    col_name = u"BOPP日度产量"
    def seasonal_plot(self, title=None, start_year=None, axhline=None):
        tmp_df_interpolated, fig, axis = super(sdb_base, self).seasonal_plot(title=title, start_year=start_year)
        axis.yaxis.set_major_formatter(FuncFormatter(lambda y, _: '{:.2f}'.format(y)))
        return tmp_df_interpolated, fig, axis

class PPTouMingRiDuChanLiang(sdb_base, Manual):
    field_name = u"日度产量"
    col_name = u"PP透明日度产量"  
    def seasonal_plot(self, title=None, start_year=None, axhline=None):
        tmp_df_interpolated, fig, axis = super(sdb_base, self).seasonal_plot(title=title, start_year=start_year)
        axis.yaxis.set_major_formatter(FuncFormatter(lambda y, _: '{:.2f}'.format(y)))
        return tmp_df_interpolated, fig, axis
    
class CPPRiDuChanLiang(sdb_base, Manual):
    field_name = u"日度产量"
    col_name = u"CPP日度产量" 
    def seasonal_plot(self, title=None, start_year=None, axhline=None):
        tmp_df_interpolated, fig, axis = super(sdb_base, self).seasonal_plot(title=title, start_year=start_year)
        axis.yaxis.set_major_formatter(FuncFormatter(lambda y, _: '{:.2f}'.format(y)))
        return tmp_df_interpolated, fig, axis

class PPGuanCaiRiDuChanLiang(sdb_base, Manual):
    field_name = u"日度产量"
    col_name = u"PP管材日度产量"   
    def seasonal_plot(self, title=None, start_year=None, axhline=None):
        tmp_df_interpolated, fig, axis = super(sdb_base, self).seasonal_plot(title=title, start_year=start_year)
        axis.yaxis.set_major_formatter(FuncFormatter(lambda y, _: '{:.2f}'.format(y)))
        return tmp_df_interpolated, fig, axis
    
class PPZhuanYongLiaoRiDuChanLiang(sdb_base, Manual):
    field_name = u"日度产量"
    col_name = u"PP专用料日度产量"  
    def seasonal_plot(self, title=None, start_year=None, axhline=None):
        tmp_df_interpolated, fig, axis = super(sdb_base, self).seasonal_plot(title=title, start_year=start_year)
        axis.yaxis.set_major_formatter(FuncFormatter(lambda y, _: '{:.2f}'.format(y)))
        return tmp_df_interpolated, fig, axis       

""" 计算指标 """

class PPZhuSuRiDuChanLiang(sdb_base, Computed):
    field_name = u"日度产量"
    col_name = u"PP注塑日度产量"      
    
    def get_ts_whole_progress(self):
        relevant_col_list = [u"PP普通注塑日度产量", u"PP薄壁注塑日度产量"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total.sum(axis=1)
        return tmp_total  
    
    def seasonal_plot(self, title=None, start_year=None, axhline=None):
        tmp_df_interpolated, fig, axis = super(sdb_base, self).seasonal_plot(title=title, start_year=start_year)
        axis.yaxis.set_major_formatter(FuncFormatter(lambda y, _: '{:.2f}'.format(y)))
        return tmp_df_interpolated, fig, axis


class PPGongJuRiDuChanLiang(sdb_base, Computed):
    field_name = u"日度产量"
    col_name = u"PP共聚日度产量"      
    
    def get_ts_whole_progress(self):
        relevant_col_list = [u"PP低熔共聚日度产量", u"PP中熔共聚日度产量", u"PP高熔共聚日度产量", u"PP其他共聚日度产量"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total.sum(axis=1)
        return tmp_total   
    
    def seasonal_plot(self, title=None, start_year=None, axhline=None):
        tmp_df_interpolated, fig, axis = super(sdb_base, self).seasonal_plot(title=title, start_year=start_year)
        axis.yaxis.set_major_formatter(FuncFormatter(lambda y, _: '{:.2f}'.format(y)))
        return tmp_df_interpolated, fig, axis
    
class PPRiDuChanLiang(sdb_base, Computed):
    field_name = u"日度产量"
    col_name = u"PP日度产量"      
    
    def get_ts_whole_progress(self):
        relevant_col_list = [u"PP拉丝日度产量", u"PP普通注塑日度产量", u"PP薄壁注塑日度产量", u"PP低熔共聚日度产量", u"PP中熔共聚日度产量", 
                             u"PP高熔共聚日度产量", u"PP其他共聚日度产量", u"PP纤维日度产量", u"BOPP日度产量", u"PP透明日度产量", 
                             u"CPP日度产量", u"PP管材日度产量", u"PP专用料日度产量"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total.sum(axis=1)
        return tmp_total    
    
    def seasonal_plot(self, title=None, start_year=None, axhline=None):
        tmp_df_interpolated, fig, axis = super(sdb_base, self).seasonal_plot(title=title, start_year=start_year)
        axis.yaxis.set_major_formatter(FuncFormatter(lambda y, _: '{:.2f}'.format(y)))
        return tmp_df_interpolated, fig, axis
    
    
###########################################################################################################################
""" 月度产量 """  
""" 计算指标 """
def modify_yield(ts):
    cap = PPChanNeng().get_ts().resample("M").sum() / 365
    yield_ts = PPRiDuChanLiang().get_ts().resample("M").sum()
    ratio = yield_ts / cap
    today = datetime.today()
    today = datetime(today.year, today.month, calendar.monthrange(today.year, today.month)[1])
    ratio[ratio.index <= today] = 1
    ts = ts * ratio
    return ts
    



class PPYueDuChanLiang(sdb_base, Computed):
    field_name = u"月度产量"
    col_name = u"PP月度产量"    
    def get_ts_whole_progress(self):
        relevant_col_list = [u"PP日度产量"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_series = tmp_total[u"PP日度产量"].resample("M").sum()
        tmp_series = modify_yield(tmp_series)
        tmp_series.name = self.col_name
        return tmp_series.to_frame()

    def seasonal_plot(self, title=None, start_year=None, axhline=None):
        tmp_df_interpolated, fig, axis = super(sdb_base, self).seasonal_plot(title=title, start_year=start_year, 
                                              axhline=axhline, mode="month")
        return tmp_df_interpolated, fig, axis
    
class PPLaSiYueDuChanLiang(sdb_base, Computed):
    field_name = u"月度产量"
    col_name = u"PP拉丝月度产量"    
    def get_ts_whole_progress(self):
        relevant_col_list = [u"PP拉丝日度产量"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_series = tmp_total[u"PP拉丝日度产量"].resample("M").sum()
        tmp_series = modify_yield(tmp_series)
        tmp_series.name = self.col_name
        return tmp_series.to_frame()

    def seasonal_plot(self, title=None, start_year=None, axhline=None):
        tmp_df_interpolated, fig, axis = super(sdb_base, self).seasonal_plot(title=title, start_year=start_year, 
                                              axhline=axhline, mode="month")
        return tmp_df_interpolated, fig, axis
    
class PPZhuSuYueDuChanLiang(sdb_base, Computed):
    field_name = u"月度产量"
    col_name = u"PP注塑月度产量"    
    def get_ts_whole_progress(self):
        relevant_col_list = [u"PP注塑日度产量"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_series = tmp_total[u"PP注塑日度产量"].resample("M").sum()
        tmp_series = modify_yield(tmp_series)
        tmp_series.name = self.col_name
        return tmp_series.to_frame()

    def seasonal_plot(self, title=None, start_year=None, axhline=None):
        tmp_df_interpolated, fig, axis = super(sdb_base, self).seasonal_plot(title=title, start_year=start_year, 
                                              axhline=axhline, mode="month")
        return tmp_df_interpolated, fig, axis
    
class PPBoBiZhuSuYueDuChanLiang(sdb_base, Computed):
    field_name = u"月度产量"
    col_name = u"PP薄壁注塑月度产量"    
    def get_ts_whole_progress(self):
        relevant_col_list = [u"PP薄壁注塑日度产量"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_series = tmp_total[u"PP薄壁注塑日度产量"].resample("M").sum()
        tmp_series = modify_yield(tmp_series)
        tmp_series.name = self.col_name
        return tmp_series.to_frame()

    def seasonal_plot(self, title=None, start_year=None, axhline=None):
        tmp_df_interpolated, fig, axis = super(sdb_base, self).seasonal_plot(title=title, start_year=start_year, 
                                              axhline=axhline, mode="month")
        return tmp_df_interpolated, fig, axis
    
class PPDiRongGongJuYueDuChanLiang(sdb_base, Computed):
    field_name = u"月度产量"
    col_name = u"PP低熔共聚月度产量"    
    def get_ts_whole_progress(self):
        relevant_col_list = [u"PP低熔共聚日度产量"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_series = tmp_total[u"PP低熔共聚日度产量"].resample("M").sum()
        tmp_series = modify_yield(tmp_series)
        tmp_series.name = self.col_name
        return tmp_series.to_frame()

    def seasonal_plot(self, title=None, start_year=None, axhline=None):
        tmp_df_interpolated, fig, axis = super(sdb_base, self).seasonal_plot(title=title, start_year=start_year, 
                                              axhline=axhline, mode="month")
        return tmp_df_interpolated, fig, axis
    
class PPZhongRongGongJuYueDuChanLiang(sdb_base, Computed):
    field_name = u"月度产量"
    col_name = u"PP中熔共聚月度产量"    
    def get_ts_whole_progress(self):
        relevant_col_list = [u"PP中熔共聚日度产量"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_series = tmp_total[u"PP中熔共聚日度产量"].resample("M").sum()
        tmp_series = modify_yield(tmp_series)
        tmp_series.name = self.col_name
        return tmp_series.to_frame()

    def seasonal_plot(self, title=None, start_year=None, axhline=None):
        tmp_df_interpolated, fig, axis = super(sdb_base, self).seasonal_plot(title=title, start_year=start_year, 
                                              axhline=axhline, mode="month")
        return tmp_df_interpolated, fig, axis
    
class PPGaoRongGongJuYueDuChanLiang(sdb_base, Computed):
    field_name = u"月度产量"
    col_name = u"PP高熔共聚月度产量"    
    def get_ts_whole_progress(self):
        relevant_col_list = [u"PP高熔共聚日度产量"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_series = tmp_total[u"PP高熔共聚日度产量"].resample("M").sum()
        tmp_series = modify_yield(tmp_series)
        tmp_series.name = self.col_name
        return tmp_series.to_frame()

    def seasonal_plot(self, title=None, start_year=None, axhline=None):
        tmp_df_interpolated, fig, axis = super(sdb_base, self).seasonal_plot(title=title, start_year=start_year, 
                                              axhline=axhline, mode="month")
        return tmp_df_interpolated, fig, axis
    
class PPGongJuYueDuChanLiang(sdb_base, Computed):
    field_name = u"月度产量"
    col_name = u"PP共聚月度产量"    
    def get_ts_whole_progress(self):
        relevant_col_list = [u"PP共聚日度产量"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_series = tmp_total[u"PP共聚日度产量"].resample("M").sum()
        tmp_series = modify_yield(tmp_series)
        tmp_series.name = self.col_name
        return tmp_series.to_frame()

    def seasonal_plot(self, title=None, start_year=None, axhline=None):
        tmp_df_interpolated, fig, axis = super(sdb_base, self).seasonal_plot(title=title, start_year=start_year, 
                                              axhline=axhline, mode="month")
        return tmp_df_interpolated, fig, axis
    
class PPXianWeiYueDuChanLiang(sdb_base, Computed):
    field_name = u"月度产量"
    col_name = u"PP纤维月度产量"    
    def get_ts_whole_progress(self):
        relevant_col_list = [u"PP纤维日度产量"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_series = tmp_total[u"PP纤维日度产量"].resample("M").sum()
        tmp_series = modify_yield(tmp_series)
        tmp_series.name = self.col_name
        return tmp_series.to_frame()

    def seasonal_plot(self, title=None, start_year=None, axhline=None):
        tmp_df_interpolated, fig, axis = super(sdb_base, self).seasonal_plot(title=title, start_year=start_year, 
                                              axhline=axhline, mode="month")
        return tmp_df_interpolated, fig, axis
    
class BOPPYueDuChanLiang(sdb_base, Computed):
    field_name = u"月度产量"
    col_name = u"BOPP月度产量"    
    def get_ts_whole_progress(self):
        relevant_col_list = [u"BOPP日度产量"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_series = tmp_total[u"BOPP日度产量"].resample("M").sum()
        tmp_series = modify_yield(tmp_series)
        tmp_series.name = self.col_name
        return tmp_series.to_frame()

    def seasonal_plot(self, title=None, start_year=None, axhline=None):
        tmp_df_interpolated, fig, axis = super(sdb_base, self).seasonal_plot(title=title, start_year=start_year, 
                                              axhline=axhline, mode="month")
        return tmp_df_interpolated, fig, axis
    
class PPTouMingYueDuChanLiang(sdb_base, Computed):
    field_name = u"月度产量"
    col_name = u"PP透明月度产量"    
    def get_ts_whole_progress(self):
        relevant_col_list = [u"PP透明日度产量"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_series = tmp_total[u"PP透明日度产量"].resample("M").sum()
        tmp_series = modify_yield(tmp_series)
        tmp_series.name = self.col_name
        return tmp_series.to_frame()

    def seasonal_plot(self, title=None, start_year=None, axhline=None):
        tmp_df_interpolated, fig, axis = super(sdb_base, self).seasonal_plot(title=title, start_year=start_year, 
                                              axhline=axhline, mode="month")
        return tmp_df_interpolated, fig, axis
    
class CPPYueDuChanLiang(sdb_base, Computed):
    field_name = u"月度产量"
    col_name = u"CPP月度产量"    
    def get_ts_whole_progress(self):
        relevant_col_list = [u"CPP日度产量"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_series = tmp_total[u"CPP日度产量"].resample("M").sum()
        tmp_series = modify_yield(tmp_series)
        tmp_series.name = self.col_name
        return tmp_series.to_frame()

    def seasonal_plot(self, title=None, start_year=None, axhline=None):
        tmp_df_interpolated, fig, axis = super(sdb_base, self).seasonal_plot(title=title, start_year=start_year, 
                                              axhline=axhline, mode="month")
        return tmp_df_interpolated, fig, axis
    
class PPGuanCaiYueDuChanLiang(sdb_base, Computed):
    field_name = u"月度产量"
    col_name = u"PP管材月度产量"    
    def get_ts_whole_progress(self):
        relevant_col_list = [u"PP管材日度产量"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_series = tmp_total[u"PP管材日度产量"].resample("M").sum()
        tmp_series = modify_yield(tmp_series)
        tmp_series.name = self.col_name
        return tmp_series.to_frame()

    def seasonal_plot(self, title=None, start_year=None, axhline=None):
        tmp_df_interpolated, fig, axis = super(sdb_base, self).seasonal_plot(title=title, start_year=start_year, 
                                              axhline=axhline, mode="month")
        return tmp_df_interpolated, fig, axis
    
class PPZhuanYongLiaoYueDuChanLiang(sdb_base, Computed):
    field_name = u"月度产量"
    col_name = u"PP专用料月度产量"    
    def get_ts_whole_progress(self):
        relevant_col_list = [u"PP专用料日度产量"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_series = tmp_total[u"PP专用料日度产量"].resample("M").sum()
        tmp_series = modify_yield(tmp_series)
        tmp_series.name = self.col_name
        return tmp_series.to_frame()

    def seasonal_plot(self, title=None, start_year=None, axhline=None):
        tmp_df_interpolated, fig, axis = super(sdb_base, self).seasonal_plot(title=title, start_year=start_year, 
                                              axhline=axhline, mode="month")
        return tmp_df_interpolated, fig, axis
    
class PPYueDuChanLiang_YuGu(sdb_base, Computed):
    field_name = u"月度产量"
    col_name = u"PP月度产量(预估)"    
    def get_ts_whole_progress(self):
        relevant_col_list = [u"PP日度产量"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_series = tmp_total[u"PE日度产量"].resample("M").sum()
        tmp_series.name = self.col_name
        return tmp_series.to_frame()


###########################################################################################################################
""" 进口 """  
class PPJinKouLiang(sdb_base, Manual):
    field_name = u"进口"
    col_name = u"PP进口量" 
    start_year = 2014

    def seasonal_plot(self, title=None, start_year=None, axhline=None):
        tmp_df_interpolated, fig, axis = super(sdb_base, self).seasonal_plot(title=title, start_year=start_year, 
                                              axhline=axhline, mode="month")
        return tmp_df_interpolated, fig, axis
    
class PPJinKouLiang_YuGu(sdb_base, Computed):
    field_name = u"进口"
    col_name = u"PP进口量(预估)" 
    start_year = 2014
    
    def get_ts_whole_progress(self):
        relevant_col_list = [u"PP进口量"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_expect_df = self.expected_value(u"PP进口量", tmp_total)
        return tmp_expect_df
    
    def seasonal_plot(self, title=None, start_year=None, axhline=None):
        tmp_series = PPJinKouLiang().get_ts()
        tmp_df_interpolated, fig, axis = super(sdb_base, self).seasonal_plot(title=title, start_year=start_year, 
                                              axhline=axhline, mode="month", original_ts=tmp_series)
        return tmp_df_interpolated, fig, axis  
    
class JunJuPPJinKouLiang(sdb_base, Manual):
    field_name = u"进口"
    col_name = u"均聚PP进口量" 
    start_year = 2014
    
    def seasonal_plot(self, title=None, start_year=None, axhline=None):
        tmp_df_interpolated, fig, axis = super(sdb_base, self).seasonal_plot(title=title, start_year=start_year, 
                                              axhline=axhline, mode="month")
        return tmp_df_interpolated, fig, axis
    
    
class GongJuPPJinKouLiang(sdb_base, Manual):
    field_name = u"进口"
    col_name = u"共聚PP进口量" 
    start_year = 2014

    def seasonal_plot(self, title=None, start_year=None, axhline=None):
        tmp_df_interpolated, fig, axis = super(sdb_base, self).seasonal_plot(title=title, start_year=start_year, 
                                              axhline=axhline, mode="month")
        return tmp_df_interpolated, fig, axis
    
class QiTaPPJinKouLiang(sdb_base, Manual):
    field_name = u"进口"
    col_name = u"其他PP进口量" 
    start_year = 2014

    def seasonal_plot(self, title=None, start_year=None, axhline=None):
        tmp_df_interpolated, fig, axis = super(sdb_base, self).seasonal_plot(title=title, start_year=start_year, 
                                              axhline=axhline, mode="month")
        return tmp_df_interpolated, fig, axis
    
###########################################################################################################################
""" 出口 """  
class PPChuKouLiang(sdb_base, Manual):
    field_name = u"出口"
    col_name = u"PP出口量" 
    start_year = 2014

    def seasonal_plot(self, title=None, start_year=None, axhline=None):
        tmp_df_interpolated, fig, axis = super(sdb_base, self).seasonal_plot(title=title, start_year=start_year, 
                                              axhline=axhline, mode="month")
        return tmp_df_interpolated, fig, axis


class PPChuKouLiang_YuGu(sdb_base, Computed):
    field_name = u"出口"
    col_name = u"PP出口量(预估)" 
    start_year = 2014
    
    def get_ts_whole_progress(self):
        relevant_col_list = [u"PP出口量"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_expect_df = self.expected_value(u"PP出口量", tmp_total)
        return tmp_expect_df
    
    def seasonal_plot(self, title=None, start_year=None, axhline=None):
        tmp_series = PPChuKouLiang().get_ts()
        tmp_df_interpolated, fig, axis = super(sdb_base, self).seasonal_plot(title=title, start_year=start_year, 
                                              axhline=axhline, mode="month", original_ts=tmp_series)
        return tmp_df_interpolated, fig, axis 

    
class JunJuPPChuKouLiang(sdb_base, Manual):
    field_name = u"出口"
    col_name = u"均聚PP出口量" 
    start_year = 2014

    def seasonal_plot(self, title=None, start_year=None, axhline=None):
        tmp_df_interpolated, fig, axis = super(sdb_base, self).seasonal_plot(title=title, start_year=start_year, 
                                              axhline=axhline, mode="month")
        return tmp_df_interpolated, fig, axis
    
class GongJuPPChuKouLiang(sdb_base, Manual):
    field_name = u"出口"
    col_name = u"共聚PP出口量" 
    start_year = 2014

    def seasonal_plot(self, title=None, start_year=None, axhline=None):
        tmp_df_interpolated, fig, axis = super(sdb_base, self).seasonal_plot(title=title, start_year=start_year, 
                                              axhline=axhline, mode="month")
        return tmp_df_interpolated, fig, axis
    
class QiTaPPChuKouLiang(sdb_base, Manual):
    field_name = u"出口"
    col_name = u"其他PP出口量" 
    start_year = 2014

    def seasonal_plot(self, title=None, start_year=None, axhline=None):
        tmp_df_interpolated, fig, axis = super(sdb_base, self).seasonal_plot(title=title, start_year=start_year, 
                                              axhline=axhline, mode="month")
        return tmp_df_interpolated, fig, axis
    
###########################################################################################################################
""" 净进口 """  
""" 计算指标 """

class PPJingJinKouLiang(sdb_base, Computed):
    field_name = u"净进口"
    col_name = u"PP净进口量"    
    start_year = 2014
    def get_ts_whole_progress(self):
        relevant_col_list = [u"PP进口量", u"PP出口量"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"PP进口量"] - tmp_total[u"PP出口量"]
        return tmp_total


    
class PPJingJinKouLiang_YuGu(sdb_base, Computed):
    field_name = u"净进口"
    col_name = u"PP净进口量(预估)"   
    start_year = 2014
    def get_ts_whole_progress(self):
        relevant_col_list = [u"PP净进口量"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_expect_df = self.expected_value(u"PP净进口量", tmp_total)
        return tmp_expect_df

    def seasonal_plot(self, title=None, start_year=None, axhline=None):
        tmp_series = PPJingJinKouLiang().get_ts()
        tmp_df_interpolated, fig, axis = super(sdb_base, self).seasonal_plot(title=title, start_year=start_year, 
                                              axhline=axhline, mode="month", original_ts=tmp_series)
        return tmp_df_interpolated, fig, axis    
    
class JunJuPPJingJinKouLiang(sdb_base, Computed):
    field_name = u"净进口"
    col_name = u"均聚PP净进口量" 
    start_year = 2014
    def get_ts_whole_progress(self):
        relevant_col_list = [u"均聚PP进口量", u"均聚PP出口量"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"均聚PP进口量"] - tmp_total[u"均聚PP出口量"]
        return tmp_total

    
class JunJuPPJingJinKouLiang_YuGu(sdb_base, Computed):
    field_name = u"净进口"
    col_name = u"均聚PP净进口量(预估)"   
    start_year = 2014
    def get_ts_whole_progress(self):
        relevant_col_list = [u"均聚PP净进口量"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_expect_df = self.expected_value(u"均聚PP净进口量", tmp_total)
        return tmp_expect_df

    def seasonal_plot(self, title=None, start_year=None, axhline=None):
        tmp_series = JunJuPPJingJinKouLiang().get_ts()
        tmp_df_interpolated, fig, axis = super(sdb_base, self).seasonal_plot(title=title, start_year=start_year, 
                                              axhline=axhline, mode="month", original_ts=tmp_series)
        return tmp_df_interpolated, fig, axis   
    
class GongJuPPJingJinKouLiang(sdb_base, Computed):
    field_name = u"净进口"
    col_name = u"共聚PP净进口量"
    start_year = 2014    
    def get_ts_whole_progress(self):
        relevant_col_list = [u"共聚PP进口量", u"共聚PP出口量"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"共聚PP进口量"] - tmp_total[u"共聚PP出口量"]
        return tmp_total
    
class GongJuPPJingJinKouLiang_YuGu(sdb_base, Computed):
    field_name = u"净进口"
    col_name = u"共聚PP净进口量(预估)"    
    start_year = 2014
    def get_ts_whole_progress(self):
        relevant_col_list = [u"共聚PP净进口量"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_expect_df = self.expected_value(u"共聚PP净进口量", tmp_total)
        return tmp_expect_df

    def seasonal_plot(self, title=None, start_year=None, axhline=None):
        tmp_series = GongJuPPJingJinKouLiang().get_ts()
        tmp_df_interpolated, fig, axis = super(sdb_base, self).seasonal_plot(title=title, start_year=start_year, 
                                              axhline=axhline, mode="month", original_ts=tmp_series)
        return tmp_df_interpolated, fig, axis 
    
    
    
###########################################################################################################################
""" 废料 """  

class QiTaFeiLiaoJinKouLiang(sdb_base, Manual):
    field_name = u"废料"
    col_name = u"其他废料进口量" 
    start_year = 2014
    
class PPFeiLiaoJinKouLiang(sdb_base, Computed):
    field_name = u"废料"
    col_name = u"PP废料进口量" 
    start_year = 2014
    
    def get_ts_whole_progress(self):
        relevant_col_list = [u"其他废料进口量"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = 0.4656 * tmp_total[u"其他废料进口量"]
        return tmp_total

    def seasonal_plot(self, title=None, start_year=None, axhline=None):
        tmp_df_interpolated, fig, axis = super(sdb_base, self).seasonal_plot(title=title, start_year=start_year, 
                                              axhline=axhline, mode="month")
        return tmp_df_interpolated, fig, axis   
    
    
    
###########################################################################################################################
""" 表观消费量 """  
""" 计算指标 """
    
class PPBiaoGuanXiaoFeiLiang(sdb_base, Computed):
    field_name = u"净进口"
    col_name = u"PP表观消费量"    
    def get_ts_whole_progress(self):
        relevant_col_list = [u"PP月度产量", u"PP净进口量", u"PP废料进口量"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[u"PP废料进口量"][tmp_total.index > tmp_total[u"PP废料进口量"].dropna().index[-1]] = 0
        tmp_total[self.col_name] = tmp_total[u"PP月度产量"] + tmp_total[u"PP净进口量"] + tmp_total[u"PP废料进口量"]
        return tmp_total

class PPBiaoGuanXiaoFeiLiang_YuGu(sdb_base, Computed):
    field_name = u"净进口"
    col_name = u"PP表观消费量(预估)"    
    def get_ts_whole_progress(self):
        relevant_col_list = [u"PP月度产量", u"PP净进口量", u"PP净进口量(预估)", u"PP废料进口量", u"PP表观消费量"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[u"净进口预估"] = tmp_total[u"PP净进口量"].fillna(0) + tmp_total[u"PP净进口量(预估)"].fillna(0)
        tmp_total[u"PP废料进口量"][tmp_total.index > tmp_total[u"PP废料进口量"].dropna().index[-1]] = 0        
        tmp_total[self.col_name] = tmp_total[u"PP月度产量"] + tmp_total[u"净进口预估"] + tmp_total[u"PP废料进口量"]
        tmp_total[self.col_name][tmp_total.index <= tmp_total[u"PP表观消费量"].dropna().index[-1]] = np.nan
        return tmp_total

    def seasonal_plot(self, title=None, start_year=None, axhline=None):
        tmp_series = PPBiaoGuanXiaoFeiLiang().get_ts()
        tmp_df_interpolated, fig, axis = super(sdb_base, self).seasonal_plot(title=title, start_year=start_year, 
                                              axhline=axhline, mode="month", original_ts=tmp_series)
        return tmp_df_interpolated, fig, axis 
    
###########################################################################################################################
""" 消费量 """  
""" 计算指标 """

class PPYueDuXiaoFeiLiang(sdb_base, Computed):
    field_name = u"消费量"
    col_name = u"PP月度消费量"    
    def get_ts_whole_progress(self):
        relevant_col_list = [u"PP表观消费量", u"月度PP社会库存"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"PP表观消费量"] - tmp_total[u"月度PP社会库存"].diff()
        return tmp_total  
    
class PPYueDuXiaoFeiLiang_YuGu(sdb_base, Computed):
    field_name = u"消费量"
    col_name = u"PP月度消费量(预估)"    
    def get_ts_whole_progress(self):
        relevant_col_list = [u"PP月度消费量"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_expect_df = self.expected_value(u"PP月度消费量", tmp_total)
        return tmp_expect_df

    def seasonal_plot(self, title=None, start_year=None, axhline=None):
        tmp_series = PPYueDuXiaoFeiLiang().get_ts()
        tmp_df_interpolated, fig, axis = super(sdb_base, self).seasonal_plot(title=title, start_year=start_year, 
                                              axhline=axhline, mode="month", original_ts=tmp_series)
        return tmp_df_interpolated, fig, axis 

###########################################################################################################################
""" 库存 """  
""" 计算指标 """

class YueDuPPSheHuiKuCun(sdb_base, Computed):
    field_name = u"库存"
    col_name = u"月度PP社会库存"    
    def get_ts_whole_progress(self):
        tmp_inventory = PP_Inventory.PPSheHuiKuCun().get_ts()
        tmp_series = tmp_inventory.resample("M").last()
        tmp_series.name = self.col_name
        return tmp_series.to_frame()

class YueDuPPSheHuiKuCun_YuGu(sdb_base, Computed):
    field_name = u"库存"
    col_name = u"月度PP社会库存(预估)"    
    def get_ts_whole_progress(self):
        relevant_col_list = [u"月度PP社会库存", u"PP月度消费量(预估)", u"PP表观消费量(预估)"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = np.nan
        tmp_total[self.col_name][tmp_total.index > tmp_total[u"月度PP社会库存"].dropna().index[-1]] = tmp_total[u"月度PP社会库存"].dropna().iloc[-1]
        tmp_total["sum"] = tmp_total[u"PP表观消费量(预估)"] - tmp_total[u"PP月度消费量(预估)"]
        tmp_total["cumsum"] = tmp_total["sum"][tmp_total.index > tmp_total[u"月度PP社会库存"].dropna().index[-1]].cumsum()
        tmp_total[self.col_name] += tmp_total["cumsum"]
        return tmp_total

    def seasonal_plot(self, title=None, start_year=None, axhline=None):
        tmp_series = YueDuPPSheHuiKuCun().get_ts()
        tmp_df_interpolated, fig, axis = super(sdb_base, self).seasonal_plot(title=title, start_year=start_year, 
                                              axhline=axhline, mode="month", original_ts=tmp_series)
        return tmp_df_interpolated, fig, axis 
    
###########################################################################################################################
""" 库消比 """  
""" 计算指标 """

class PPKuXiaoBi(sdb_base, Computed):
    field_name = u"库消比"
    col_name = u"PP库消比"    
    def get_ts_whole_progress(self):
        relevant_col_list = [u"月度PP社会库存", u"PP月度消费量"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[u"当月天数"] = [calendar.monthrange(x.year, x.month)[1] for x in tmp_total.index]
        tmp_total[self.col_name] = tmp_total[u"月度PP社会库存"] / (tmp_total[u"PP月度消费量"] / tmp_total[u"当月天数"])
        return tmp_total   

class PPKuXiaoBi_YuGu(sdb_base, Computed):
    field_name = u"库消比"
    col_name = u"PP库消比(预估)"    
    def get_ts_whole_progress(self):
        relevant_col_list = [u"月度PP社会库存", u"PP月度消费量", u"月度PP社会库存(预估)", u"PP月度消费量(预估)", u"PP库消比"]        
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[u"社会库存预估"] = tmp_total[u"月度PP社会库存"].fillna(0) + tmp_total[u"月度PP社会库存(预估)"].fillna(0)
        tmp_total[u"社会库存预估"][tmp_total[u"月度PP社会库存"].isnull() & tmp_total[u"月度PP社会库存(预估)"].isnull()] = np.nan
        tmp_total[u"消费量预估"] = tmp_total[u"PP月度消费量"].fillna(0) + tmp_total[u"PP月度消费量(预估)"].fillna(0)
        tmp_total[u"消费量预估"][tmp_total[u"PP月度消费量"].isnull() & tmp_total[u"PP月度消费量(预估)"].isnull()] = np.nan        
        tmp_total[u"当月天数"] = [calendar.monthrange(x.year, x.month)[1] for x in tmp_total.index]
        tmp_total[self.col_name] = tmp_total[u"社会库存预估"] / (tmp_total[u"消费量预估"] / tmp_total[u"当月天数"])
        tmp_total.loc[tmp_total.index <= tmp_total[u"PP库消比"].dropna().index[-1], self.col_name] = np.nan
        return tmp_total 

    def seasonal_plot(self, title=None, start_year=None, axhline=None):
        tmp_series = PPKuXiaoBi().get_ts()
        tmp_df_interpolated, fig, axis = super(sdb_base, self).seasonal_plot(title=title, start_year=start_year, 
                                              axhline=axhline, mode="month", original_ts=tmp_series)
        return tmp_df_interpolated, fig, axis 
###########################################################################################################################

if __name__ == "__main__":
#    ts = PPGongJuYueDuChanLiang().get_ts()
    ts, fig, axis = BOPPRiDuChanLiang().seasonal_plot()
#
















    
    
    
    