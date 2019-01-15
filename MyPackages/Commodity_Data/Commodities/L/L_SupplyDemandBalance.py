# -*- coding: utf-8 -*-
"""
Created on Mon Aug 27 08:36:17 2018

@author: 李弘一萌
"""

import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt
from .L_Base import L_Base
from . import L_Macro, L_Others, L_Inventory
from .L_Device import L_Device_Process
from ...Base.DataType_Base import Manual, Computed, WindData, Auto
from ...Base.Plot_Base import Plot_Base
from matplotlib.ticker import FuncFormatter
import calendar



class sdb_base(L_Base, Plot_Base):
    table_english_name = "SupplyDemandBalance"
    table_chinese_name = u"供需平衡表"
    progress_table = pd.DataFrame()
#    original_db_filepath = data_path + u"LPP价格数据库.xlsx"
    
    def output(self):
        print("SupplyDemandBalance")


    def get_relevant_df(self, col_list):
        local_col_name_list = sdb_base.get_all_table_classname()
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




    
#    def get_relevant_df(self, col_list):
#        local_col_name_list = sdb_base.get_all_table_classname()
#        col_cls_list = []
#        for x in col_list:
#            col_cls_name = str(L_Base.get_class_name(x))
#            if col_cls_name not in local_col_name_list:
#                col_cls_list.append(eval(L_Base.get_table_class_full_variable(x)))
#            else:
#                col_cls_list.append(eval(col_cls_name))
#        if len(col_list) != 0:   
#            for col_cls in col_cls_list:
#                col_obj = col_cls()
#                if col_obj.col_name not in self.progress_table:
#                    if isinstance(col_obj, Computed):
#                        col_obj.progress_table = self.progress_table
#                        tmp_total_table = col_obj.get_ts_whole_progress()  
#                        self.progress_table = tmp_total_table.copy()  
#                    else:
#                        tmp_total_ts = col_obj.get_ts()
#                        self.progress_table = pd.concat([self.progress_table, tmp_total_ts], axis=1, sort=False)
#            tmp_table_df = self.progress_table
#        else:
#            pass
#        return tmp_table_df 
    
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
""" 计算指标 """
 
class PEChanNeng(sdb_base, Computed):
    field_name = u"产能"
    col_name = u"PE产能"    
    def get_ts_whole_progress(self):
        tmp_series = L_Device_Process.get_device_capability()
        tmp_series.name = self.col_name
        tmp_total = tmp_series.to_frame()
        return tmp_total
    
class LLDChanNeng(sdb_base, Computed):
    field_name = u"产能"
    col_name = u"LLD产能"    
    def get_ts_whole_progress(self):
        tmp_series = L_Device_Process.get_device_capability(u"线性")
        tmp_series.name = self.col_name
        tmp_total = tmp_series.to_frame()
        return tmp_total

class HDChanNeng(sdb_base, Computed):
    field_name = u"产能"
    col_name = u"HD产能"    
    def get_ts_whole_progress(self):
        tmp_series = L_Device_Process.get_device_capability(u"低压")
        tmp_series.name = self.col_name
        tmp_total = tmp_series.to_frame()
        return tmp_total

class LDChanNeng(sdb_base, Computed):
    field_name = u"产能"
    col_name = u"LD产能"    
    def get_ts_whole_progress(self):
        tmp_series = L_Device_Process.get_device_capability(u"高压")
        tmp_series.name = self.col_name
        tmp_total = tmp_series.to_frame()
        return tmp_total
    
class QuanMiDuChanNeng(sdb_base, Computed):
    field_name = u"产能"
    col_name = u"全密度产能"    
    def get_ts_whole_progress(self):
        tmp_series = L_Device_Process.get_device_capability(u"全密度")
        tmp_series.name = self.col_name
        tmp_total = tmp_series.to_frame()
        return tmp_total
    




###########################################################################################################################
""" 产量 """     
""" 计算指标 """  

class PERiDuChanLiang(sdb_base, Computed):
    field_name = u"产量"
    col_name = u"PE日度产量"
    start_year = 2015
    def get_ts_whole_progress(self):
        tmp_series = L_Device_Process.get_product_yield() / 365
        tmp_series.name = self.col_name
        tmp_total = tmp_series.to_frame()
        return tmp_total
    def seasonal_plot(self, title=None, start_year=None, axhline=None):
        tmp_df_interpolated, fig, axis = super(sdb_base, self).seasonal_plot(title=title, start_year=start_year)
        axis.yaxis.set_major_formatter(FuncFormatter(lambda y, _: '{:.2f}'.format(y)))
        return tmp_df_interpolated, fig, axis

class LLDRiDuChanLiang(sdb_base, Computed):
    field_name = u"产量"
    col_name = u"LLD日度产量" 
    start_year = 2015
    def get_ts_whole_progress(self):
        relevant_col_list = [u"LLD日度产量(LLD装置)", u"LLD日度产量(全密度装置)"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"LLD日度产量(LLD装置)"] + tmp_total[u"LLD日度产量(全密度装置)"]
        return tmp_total
    
    def seasonal_plot(self, title=None, start_year=None, axhline=None):
        tmp_df_interpolated, fig, axis = super(sdb_base, self).seasonal_plot(title=title, start_year=start_year)
        axis.yaxis.set_major_formatter(FuncFormatter(lambda y, _: '{:.2f}'.format(y)))
        return tmp_df_interpolated, fig, axis
    
class LLDRiDuChanLiang_LLDZhuangZhi(sdb_base, Computed):
    field_name = u"产量"
    col_name = u"LLD日度产量(LLD装置)"    
    def get_ts_whole_progress(self):
        tmp_series = L_Device_Process.get_product_yield_for_specific_field(u"线性", u"线性") / 365
        tmp_series.name = self.col_name
        tmp_total = tmp_series.to_frame()
        return tmp_total
    
class LLDRiDuChanLiang_QuanMiDuZhuangZhi(sdb_base, Computed):
    field_name = u"产量"
    col_name = u"LLD日度产量(全密度装置)"    
    def get_ts_whole_progress(self):
        tmp_series = L_Device_Process.get_product_yield_for_specific_field(u"全密度", u"线性") / 365
        tmp_series.name = self.col_name
        tmp_total = tmp_series.to_frame()
        return tmp_total

class HDRiDuChanLiang(sdb_base, Computed):
    field_name = u"产量"
    col_name = u"HD日度产量"  
    start_year = 2015
    def get_ts_whole_progress(self):
        relevant_col_list = [u"HD日度产量(HD装置)", u"HD日度产量(全密度装置)"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"HD日度产量(HD装置)"] + tmp_total[u"HD日度产量(全密度装置)"]
        return tmp_total
    
    def seasonal_plot(self, title=None, start_year=None, axhline=None):
        tmp_df_interpolated, fig, axis = super(sdb_base, self).seasonal_plot(title=title, start_year=start_year)
        axis.yaxis.set_major_formatter(FuncFormatter(lambda y, _: '{:.2f}'.format(y)))
        return tmp_df_interpolated, fig, axis

class HDRiDuChanLiang_HDZhuangZhi(sdb_base, Computed):
    field_name = u"产量"
    col_name = u"HD日度产量(HD装置)"    
    def get_ts_whole_progress(self):
        tmp_series = L_Device_Process.get_product_yield_for_specific_field(u"低压", u"低压") / 365
        tmp_series.name = self.col_name
        tmp_total = tmp_series.to_frame()
        return tmp_total

class HDRiDuChanLiang_QuanMiDuZhuangZhi(sdb_base, Computed):
    field_name = u"产量"
    col_name = u"HD日度产量(全密度装置)"    
    def get_ts_whole_progress(self):
        tmp_series = L_Device_Process.get_product_yield_for_specific_field(u"全密度", u"低压") / 365
        tmp_series.name = self.col_name
        tmp_total = tmp_series.to_frame()
        return tmp_total

class LDRiDuChanLiang(sdb_base, Computed):
    field_name = u"产量"
    col_name = u"LD日度产量" 
    start_year = 2015
    def get_ts_whole_progress(self):
        tmp_series = L_Device_Process.get_product_yield_for_specific_field(u"高压", u"高压") / 365
        tmp_series.name = self.col_name
        tmp_total = tmp_series.to_frame()
        return tmp_total
    
    def seasonal_plot(self, title=None, start_year=None, axhline=None):
        tmp_df_interpolated, fig, axis = super(sdb_base, self).seasonal_plot(title=title, start_year=start_year)
        axis.yaxis.set_major_formatter(FuncFormatter(lambda y, _: '{:.2f}'.format(y)))
        return tmp_df_interpolated, fig, axis
    
    
    
class PERiDuChanLiang_YuGu(sdb_base, Computed):
    field_name = u"产量"
    col_name = u"PE日度产量(预估)"    
    def get_ts_whole_progress(self):
        tmp_series = L_Device_Process.get_product_yield()
        tmp_series.name = self.col_name
        tmp_total = tmp_series.to_frame()
        return tmp_total

class LLDRiDuChanLiang_YuGu(sdb_base, Computed):
    field_name = u"产量"
    col_name = u"LLD日度产量(预估)"    
    def get_ts_whole_progress(self):
        relevant_col_list = [u"LLD日度产量(LLD装置)", u"LLD日度产量(全密度装置)"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"LLD日度产量(LLD装置)"] - tmp_total[u"LLD日度产量(全密度装置)"]        
        return tmp_total
    
class HDRiDuChanLiang_YuGu(sdb_base, Computed):
    field_name = u"产量"
    col_name = u"HD日度产量(预估)"    
    def get_ts_whole_progress(self):
        tmp_series = L_Device_Process.get_product_yield()
        tmp_series.name = self.col_name
        tmp_total = tmp_series.to_frame()
        return tmp_total
    
class LDRiDuChanLiang_YuGu(sdb_base, Computed):
    field_name = u"产量"
    col_name = u"LD日度产量(预估)"    
    def get_ts_whole_progress(self):
        tmp_series = L_Device_Process.get_product_yield_for_specific_field(u"高压", u"高压")
        tmp_series.name = self.col_name
        tmp_total = tmp_series.to_frame()
        return tmp_total

###########################################################################################################################
""" 开工率 """     
""" 计算指标 """ 
class PEKaiGongLv(sdb_base, Computed):
    field_name = u"开工率"
    col_name = u"PE开工率"    
    
    def get_ts_whole_progress(self):
        relevant_col_list = ["PE日度产量", "PE产能"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total["PE日度产量"] / (tmp_total["PE产能"] / 365)
        return tmp_total

class LLDKaiGongLv(sdb_base, Computed):
    field_name = u"开工率"
    col_name = u"LLD开工率"    
    
    def get_ts_whole_progress(self):
        relevant_col_list = ["LLD日度产量(LLD装置)", "LLD产能"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total["LLD日度产量(LLD装置)"] / (tmp_total["LLD产能"] / 365)
        return tmp_total

class HDKaiGongLv(sdb_base, Computed):
    field_name = u"开工率"
    col_name = u"HD开工率"    
    
    def get_ts_whole_progress(self):
        relevant_col_list = ["HD日度产量", "HD产能"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total["HD日度产量"] / (tmp_total["HD产能"] / 365)
        return tmp_total

class LDKaiGongLv(sdb_base, Computed):
    field_name = u"开工率"
    col_name = u"LD开工率"    
    
    def get_ts_whole_progress(self):
        relevant_col_list = ["LD日度产量", "LD产能"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total["LD日度产量"] / (tmp_total["LD产能"] / 365)
        return tmp_total

class QuanMiDuKaiGongLv(sdb_base, Computed):
    field_name = u"开工率"
    col_name = u"全密度开工率"    
    
    def get_ts_whole_progress(self):
        relevant_col_list = ["LLD日度产量(全密度装置)", "HD日度产量(全密度装置)", "全密度产能"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = (tmp_total["LLD日度产量(全密度装置)"] + tmp_total["LLD日度产量(全密度装置)"]) / (tmp_total["全密度产能"] / 365)
        return tmp_total

class QuanMiDuZhuangZhiLLDZhanBi(sdb_base, Computed):
    field_name = u"开工率"
    col_name = u"全密度装置LLD占比"    
    
    def get_ts_whole_progress(self):
        relevant_col_list = ["LLD日度产量(全密度装置)", "全密度产能"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total["LLD日度产量(全密度装置)"] / (tmp_total["全密度产能"] / 365)
        return tmp_total


class QuanMiDuZhuangZhiHDZhanBi(sdb_base, Computed):
    field_name = u"开工率"
    col_name = u"全密度装置HD占比"    
    
    def get_ts_whole_progress(self):
        relevant_col_list = ["HD日度产量(全密度装置)", "全密度产能"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total["HD日度产量(全密度装置)"] / (tmp_total["全密度产能"] / 365)
        return tmp_total
    
###########################################################################################################################
""" 月度产量 """
""" 计算指标 """

def modify_yield(ts):
    cap = PEChanNeng().get_ts().resample("M").sum() / 365
    yield_ts = PERiDuChanLiang().get_ts().resample("M").sum()
    ratio = yield_ts / cap
    today = datetime.today()
    today = datetime(today.year, today.month, calendar.monthrange(today.year, today.month)[1])
    ratio[ratio.index <= today] = 1
    ts = ts * ratio
    return ts


class PEYueDuChanLiang(sdb_base, Computed):
    field_name = u"产量"
    col_name = u"PE月度产量"    
    def get_ts_whole_progress(self):
        relevant_col_list = [u"PE日度产量"]
        tmp_df = self.get_relevant_df(relevant_col_list)
        tmp_series = tmp_df[u"PE日度产量"].resample("M").sum()
        tmp_series = modify_yield(tmp_series)
        tmp_series.name = self.col_name
        tmp_total = tmp_series.to_frame()
        return tmp_total
    
    def seasonal_plot(self, title=None, start_year=None, axhline=None):
        tmp_df_interpolated, fig, axis = super(sdb_base, self).seasonal_plot(title=title, start_year=start_year, 
                                              axhline=axhline, mode="month")
        return tmp_df_interpolated, fig, axis

class LLDYueDuChanLiang(sdb_base, Computed):
    field_name = u"产量"
    col_name = u"LLD月度产量"    
    def get_ts_whole_progress(self):
        relevant_col_list = [u"LLD日度产量"]
        tmp_df = self.get_relevant_df(relevant_col_list)
        tmp_series = tmp_df[u"LLD日度产量"].resample("M").sum()
        tmp_series = modify_yield(tmp_series)
        tmp_series.name = self.col_name
        tmp_total = tmp_series.to_frame()
        return tmp_total

    def seasonal_plot(self, title=None, start_year=None, axhline=None):
        tmp_df_interpolated, fig, axis = super(sdb_base, self).seasonal_plot(title=title, start_year=start_year, 
                                              axhline=axhline, mode="month")
        return tmp_df_interpolated, fig, axis
    
class HDYueDuChanLiang(sdb_base, Computed):
    field_name = u"产量"
    col_name = u"HD月度产量"    
    def get_ts_whole_progress(self):
        relevant_col_list = [u"HD日度产量"]
        tmp_df = self.get_relevant_df(relevant_col_list)
        tmp_series = tmp_df[u"HD日度产量"].resample("M").sum()
        tmp_series = modify_yield(tmp_series)
        tmp_series.name = self.col_name
        tmp_total = tmp_series.to_frame()
        return tmp_total

    def seasonal_plot(self, title=None, start_year=None, axhline=None):
        tmp_df_interpolated, fig, axis = super(sdb_base, self).seasonal_plot(title=title, start_year=start_year, 
                                              axhline=axhline, mode="month")
        return tmp_df_interpolated, fig, axis
    
    
class LDYueDuChanLiang(sdb_base, Computed):
    field_name = u"产量"
    col_name = u"LD月度产量"    
    def get_ts_whole_progress(self):
        relevant_col_list = [u"LD日度产量"]
        tmp_df = self.get_relevant_df(relevant_col_list)
        tmp_series = tmp_df[u"LD日度产量"].resample("M").sum()
        tmp_series = modify_yield(tmp_series)
        tmp_series.name = self.col_name
        tmp_total = tmp_series.to_frame()
        return tmp_total
    
    def seasonal_plot(self, title=None, start_year=None, axhline=None):
        tmp_df_interpolated, fig, axis = super(sdb_base, self).seasonal_plot(title=title, start_year=start_year, 
                                              axhline=axhline, mode="month")
        return tmp_df_interpolated, fig, axis


###########################################################################################################################
""" 进口 """

class PEJinKouLiang(sdb_base, Manual):
    field_name = u"进口"
    col_name = u"PE进口量"    

class LLDJinKouLiang(sdb_base, Manual):
    field_name = u"进口"
    col_name = u"LLD进口量"   
    
class HDJinKouLiang(sdb_base, Manual):
    field_name = u"进口"
    col_name = u"HD进口量"   
    
class LDJinKouLiang(sdb_base, Manual):
    field_name = u"进口"
    col_name = u"LD进口量"   

###########################################################################################################################
""" 出口 """

class PEChuKouLiang(sdb_base, Manual):
    field_name = u"出口"
    col_name = u"PE出口量"   

class LLDChuKouLiang(sdb_base, Manual):
    field_name = u"出口"
    col_name = u"LLD出口量"   
    
class HDChuKouLiang(sdb_base, Manual):
    field_name = u"出口"
    col_name = u"HD出口量"   
    
class LDChuKouLiang(sdb_base, Manual):
    field_name = u"出口"
    col_name = u"LD出口量"   
    
###########################################################################################################################
""" 净进口 """
""" 计算指标 """

class PEJingJinKouLiang(sdb_base, Computed):
    field_name = u"净进口"
    col_name = u"PE净进口量"    
    def get_ts_whole_progress(self):
        relevant_col_list = [u"PE进口量", u"PE出口量"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"PE进口量"] - tmp_total[u"PE出口量"]
        return tmp_total


class LLDJingJinKouLiang(sdb_base, Computed):
    field_name = u"净进口"
    col_name = u"LLD净进口量"    
    def get_ts_whole_progress(self):
        relevant_col_list = [u"LLD进口量", u"LLD出口量"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"LLD进口量"] - tmp_total[u"LLD出口量"]
        return tmp_total

    
class HDJingJinKouLiang(sdb_base, Computed):
    field_name = u"净进口"
    col_name = u"HD净进口量"    
    def get_ts_whole_progress(self):
        relevant_col_list = [u"HD进口量", u"HD出口量"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"HD进口量"] - tmp_total[u"HD出口量"]
        return tmp_total


class LDJingJinKouLiang(sdb_base, Computed):
    field_name = u"净进口"
    col_name = u"LD净进口量"    
    def get_ts_whole_progress(self):
        relevant_col_list = [u"LD进口量", u"LD出口量"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"LD进口量"] - tmp_total[u"LD出口量"]
        return tmp_total





class PEJingJinKouLiang_YuGu(sdb_base, Computed):
    field_name = u"净进口"
    col_name = u"PE净进口量(预估)"    
    start_year = 2015
    
    def get_ts_whole_progress(self):
        relevant_col_list = [u"PE净进口量"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_expect_df = self.expected_value(u"PE净进口量", tmp_total)
        return tmp_expect_df
    
    def seasonal_plot(self, title=None, start_year=None, axhline=None):
        tmp_series = PEJingJinKouLiang().get_ts()
        tmp_df_interpolated, fig, axis = super(sdb_base, self).seasonal_plot(title=title, start_year=start_year, 
                                              axhline=axhline, mode="month", original_ts=tmp_series)
        return tmp_df_interpolated, fig, axis
    
class LLDJingJinKouLiang_YuGu(sdb_base, Computed):
    field_name = u"净进口"
    col_name = u"LLD净进口量(预估)" 
    start_year = 2015
    
    def get_ts_whole_progress(self):
        relevant_col_list = [u"LLD净进口量"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_expect_df = self.expected_value(u"LLD净进口量", tmp_total)
        return tmp_expect_df
    
    def seasonal_plot(self, title=None, start_year=None, axhline=None):
        tmp_series = LLDJingJinKouLiang().get_ts()
        tmp_df_interpolated, fig, axis = super(sdb_base, self).seasonal_plot(title=title, start_year=start_year, 
                                              axhline=axhline, mode="month", original_ts=tmp_series)
        return tmp_df_interpolated, fig, axis    
    
class HDJingJinKouLiang_YuGu(sdb_base, Computed):
    field_name = u"净进口"
    col_name = u"HD净进口量(预估)" 
    start_year = 2015
    
    def get_ts_whole_progress(self):
        relevant_col_list = [u"HD净进口量"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_expect_df = self.expected_value(u"HD净进口量", tmp_total)
        return tmp_expect_df
    
    def seasonal_plot(self, title=None, start_year=None, axhline=None):
        tmp_series = HDJingJinKouLiang().get_ts()
        tmp_df_interpolated, fig, axis = super(sdb_base, self).seasonal_plot(title=title, start_year=start_year, 
                                              axhline=axhline, mode="month", original_ts=tmp_series)
        return tmp_df_interpolated, fig, axis

class LDJingJinKouLiang_YuGu(sdb_base, Computed):
    field_name = u"净进口"
    col_name = u"LD净进口量(预估)" 
    start_year = 2015
    
    def get_ts_whole_progress(self):
        relevant_col_list = [u"LD净进口量"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_expect_df = self.expected_value(u"LD净进口量", tmp_total)
        return tmp_expect_df
    
    def seasonal_plot(self, title=None, start_year=None, axhline=None):
        tmp_series = LDJingJinKouLiang().get_ts()
        tmp_df_interpolated, fig, axis = super(sdb_base, self).seasonal_plot(title=title, start_year=start_year, 
                                              axhline=axhline, mode="month", original_ts=tmp_series)
        return tmp_df_interpolated, fig, axis

###########################################################################################################################
""" 废料 """

class PEFeiliaoJinKou(sdb_base, Manual):
    field_name = u"废料"
    col_name = u"PE废料进口"  

class PEFeiLiaoChuKou(sdb_base, Manual):
    field_name = u"废料"
    col_name = u"PE废料出口"  

class QiTaSuLiaoFeiLiaoJinKou(sdb_base, Manual):
    field_name = u"废料"
    col_name = u"其他塑料废料进口"  

class QiTaSuLiaoFeiLiaoChuKou(sdb_base, Manual):
    field_name = u"废料"
    col_name = u"其他塑料废料出口"  

""" 计算指标 """

class PEFeiLiaoJingJinKou(sdb_base, Computed):
    field_name = u"废料"
    col_name = u"PE废料净进口"    
    def get_ts_whole_progress(self):
        relevant_col_list = [u"PE废料进口", u"PE废料出口"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"PE废料进口"] - tmp_total[u"PE废料出口"]
        return tmp_total

class PEFeiLiaoJingJinKou_YuGu(sdb_base, Computed):
    field_name = u"废料"
    col_name = u"PE废料净进口(预估)"    
    def get_ts_whole_progress(self):
        relevant_col_list = [u"PE废料净进口"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_expect_df = self.expected_value(u"PE废料净进口", tmp_total)
        tmp_expect_df[self.col_name] = 0
        return tmp_expect_df

    def seasonal_plot(self, title=None, start_year=None, axhline=None):
        tmp_series = PEFeiLiaoJingJinKou().get_ts()
        tmp_df_interpolated, fig, axis = super(sdb_base, self).seasonal_plot(title=title, start_year=start_year, 
                                              axhline=axhline, mode="month", original_ts=tmp_series)
        return tmp_df_interpolated, fig, axis


class QiTaSuLiaoFeiLiaoJingJinKou(sdb_base, Computed):
    field_name = u"废料"
    col_name = u"其他塑料废料净进口"    
    def get_ts_whole_progress(self):
        relevant_col_list = [u"其他塑料废料进口", u"其他塑料废料出口"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"其他塑料废料进口"] - tmp_total[u"其他塑料废料出口"]
        return tmp_total


###########################################################################################################################
""" 表观消费量 """
""" 计算指标 """

class PEBiaoGuanXiaoFeiLiang(sdb_base, Computed):
    field_name = u"表观消费量"
    col_name = u"PE表观消费量"    
    def get_ts_whole_progress(self):
        relevant_col_list = [u"PE月度产量", u"PE净进口量", u"PE废料净进口"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"PE月度产量"] + tmp_total[u"PE净进口量"] + tmp_total[u"PE废料净进口"]
        return tmp_total

class LLDBiaoGuanXiaoFeiLiang(sdb_base, Computed):
    field_name = u"表观消费量"
    col_name = u"LLD表观消费量"    
    def get_ts_whole_progress(self):
        relevant_col_list = [u"LLD月度产量", u"LLD净进口量"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"LLD月度产量"] + tmp_total[u"LLD净进口量"]
        return tmp_total
    
class HDBiaoGuanXiaoFeiLiang(sdb_base, Computed):
    field_name = u"表观消费量"
    col_name = u"HD表观消费量"    
    def get_ts_whole_progress(self):
        relevant_col_list = [u"HD月度产量", u"HD净进口量"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"HD月度产量"] + tmp_total[u"HD净进口量"]
        return tmp_total
    
class LDBiaoGuanXiaoFeiLiang(sdb_base, Computed):
    field_name = u"表观消费量"
    col_name = u"LD表观消费量"    
    def get_ts_whole_progress(self):
        relevant_col_list = [u"LD月度产量", u"LD净进口量"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"LD月度产量"] + tmp_total[u"LD净进口量"]
        return tmp_total

class PEBiaoGuanXiaoFeiLiang_YuGu(sdb_base, Computed):
    field_name = u"表观消费量"
    col_name = u"PE表观消费量(预估)"    
    def get_ts_whole_progress(self):
        relevant_col_list = [u"PE月度产量", u"PE净进口量(预估)", u"PE废料净进口(预估)", u"PE净进口量", u"PE废料净进口", u"PE表观消费量"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[u"净进口预估"] = tmp_total[u"PE净进口量"].fillna(0) + tmp_total[u"PE净进口量(预估)"].fillna(0)
        tmp_total[u"废料预估"] = tmp_total[u"PE废料净进口"].fillna(0) + tmp_total[u"PE废料净进口(预估)"].fillna(0)
        tmp_total[self.col_name] = tmp_total[u"PE月度产量"] + tmp_total[u"净进口预估"] + tmp_total[u"废料预估"]
        tmp_total[self.col_name][tmp_total.index <= tmp_total[u"PE表观消费量"].dropna().index[-1]] = np.nan
        return tmp_total

    def seasonal_plot(self, title=None, start_year=None, axhline=None):
        tmp_series = PEBiaoGuanXiaoFeiLiang().get_ts()
        tmp_df_interpolated, fig, axis = super(sdb_base, self).seasonal_plot(title=title, start_year=start_year, 
                                              axhline=axhline, mode="month", original_ts=tmp_series)
        return tmp_df_interpolated, fig, axis

class LLDBiaoGuanXiaoFeiLiang_YuGu(sdb_base, Computed):
    field_name = u"表观消费量"
    col_name = u"LLD表观消费量(预估)"    
    def get_ts_whole_progress(self):
        relevant_col_list = [u"LLD月度产量", u"LLD净进口量(预估)",  u"LLD净进口量", u"LLD表观消费量"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[u"净进口预估"] = tmp_total[u"LLD净进口量"].fillna(0) + tmp_total[u"LLD净进口量(预估)"].fillna(0)
        tmp_total[self.col_name] = tmp_total[u"LLD月度产量"] + tmp_total[u"净进口预估"]
        tmp_total[self.col_name][tmp_total.index <= tmp_total[u"LLD表观消费量"].dropna().index[-1]] = np.nan
        return tmp_total

    def seasonal_plot(self, title=None, start_year=None, axhline=None):
        tmp_series = LLDBiaoGuanXiaoFeiLiang().get_ts()
        tmp_df_interpolated, fig, axis = super(sdb_base, self).seasonal_plot(title=title, start_year=start_year, 
                                              axhline=axhline, mode="month", original_ts=tmp_series)
        return tmp_df_interpolated, fig, axis

class HDBiaoGuanXiaoFeiLiang_YuGu(sdb_base, Computed):
    field_name = u"表观消费量"
    col_name = u"HD表观消费量(预估)"    
    def get_ts_whole_progress(self):
        relevant_col_list = [u"HD月度产量", u"HD净进口量(预估)", u"HD净进口量", u"HD表观消费量"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[u"净进口预估"] = tmp_total[u"HD净进口量"].fillna(0) + tmp_total[u"HD净进口量(预估)"].fillna(0)
        tmp_total[self.col_name] = tmp_total[u"HD月度产量"] + tmp_total[u"净进口预估"]
        tmp_total[self.col_name][tmp_total.index <= tmp_total[u"HD表观消费量"].dropna().index[-1]] = np.nan
        return tmp_total

    def seasonal_plot(self, title=None, start_year=None, axhline=None):
        tmp_series = HDBiaoGuanXiaoFeiLiang().get_ts()
        tmp_df_interpolated, fig, axis = super(sdb_base, self).seasonal_plot(title=title, start_year=start_year, 
                                              axhline=axhline, mode="month", original_ts=tmp_series)
        return tmp_df_interpolated, fig, axis

class LDBiaoGuanXiaoFeiLiang_YuGu(sdb_base, Computed):
    field_name = u"表观消费量"
    col_name = u"LD表观消费量(预估)"    
    def get_ts_whole_progress(self):
        relevant_col_list = [u"LD月度产量", u"LD净进口量(预估)", u"PE废料净进口(预估)", u"LD净进口量", u"PE废料净进口", u"LD表观消费量"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[u"净进口预估"] = tmp_total[u"LD净进口量"].fillna(0) + tmp_total[u"LD净进口量(预估)"].fillna(0)
        tmp_total[u"废料预估"] = tmp_total[u"PE废料净进口"].fillna(0) + tmp_total[u"PE废料净进口(预估)"].fillna(0)
        tmp_total[self.col_name] = tmp_total[u"LD月度产量"] + tmp_total[u"净进口预估"] + tmp_total[u"废料预估"]
        tmp_total[self.col_name][tmp_total.index <= tmp_total[u"LD表观消费量"].dropna().index[-1]] = np.nan
        return tmp_total

    def seasonal_plot(self, title=None, start_year=None, axhline=None):
        tmp_series = LDBiaoGuanXiaoFeiLiang().get_ts()
        tmp_df_interpolated, fig, axis = super(sdb_base, self).seasonal_plot(title=title, start_year=start_year, 
                                              axhline=axhline, mode="month", original_ts=tmp_series)
        return tmp_df_interpolated, fig, axis
    
###########################################################################################################################
""" 库存 """
""" 计算指标 """

class YueDuPESheHuiKuCun(sdb_base, Computed):
    field_name = u"库存"
    col_name = u"月度PE社会库存"    
    def get_ts_whole_progress(self):
        tmp_inventory = L_Inventory.PESheHuiKuCun().get_ts()
        tmp_series = tmp_inventory.resample("M").last()
        tmp_series.name = self.col_name
        tmp_total = tmp_series.to_frame()
        tmp_total = pd.concat([self.progress_table, tmp_total], axis=1, sort=False)
        return tmp_total

class YueDuPESheHuiKuCun_YuGu(sdb_base, Computed):
    field_name = u"库存"
    col_name = u"月度PE社会库存(预估)"    
    def get_ts_whole_progress(self):
        relevant_col_list = [u"月度PE社会库存", u"PE消费量(预估)", u"PE表观消费量(预估)"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = np.nan
        tmp_total[self.col_name][tmp_total.index > tmp_total[u"月度PE社会库存"].dropna().index[-1]] = tmp_total[u"月度PE社会库存"].dropna().iloc[-1]
        tmp_total["sum"] = tmp_total[u"PE表观消费量(预估)"] - tmp_total[u"PE消费量(预估)"]
        tmp_total["cumsum"] = tmp_total["sum"][tmp_total.index > tmp_total[u"月度PE社会库存"].dropna().index[-1]].cumsum()
        tmp_total[self.col_name] += tmp_total["cumsum"]
        return tmp_total

    def seasonal_plot(self, title=None, start_year=None, axhline=None):
        tmp_series = YueDuPESheHuiKuCun().get_ts()
        tmp_df_interpolated, fig, axis = super(sdb_base, self).seasonal_plot(title=title, start_year=start_year, 
                                              axhline=axhline, mode="month", original_ts=tmp_series)
        return tmp_df_interpolated, fig, axis
    
###########################################################################################################################
""" 需求 """
""" 计算指标 """

class PEXiaoFeiLiang(sdb_base, Computed):
    field_name = u"需求"
    col_name = u"PE消费量"    
    def get_ts_whole_progress(self):
        relevant_col_list = [u"PE表观消费量", u"月度PE社会库存"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"PE表观消费量"] - tmp_total[u"月度PE社会库存"].diff()
        return tmp_total  
    
class PEXiaoFeiLiang_YuGu(sdb_base, Computed):
    field_name = u"需求"
    col_name = u"PE消费量(预估)"    
    def get_ts_whole_progress(self):
        relevant_col_list = [u"PE消费量"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_expect_df = self.expected_value(u"PE消费量", tmp_total)
        return tmp_expect_df    

    def seasonal_plot(self, title=None, start_year=None, axhline=None):
        tmp_series = PEXiaoFeiLiang().get_ts()
        tmp_df_interpolated, fig, axis = super(sdb_base, self).seasonal_plot(title=title, start_year=start_year, 
                                              axhline=axhline, mode="month", original_ts=tmp_series)
        return tmp_df_interpolated, fig, axis
    
###########################################################################################################################
""" 库消比 """
""" 计算指标 """

class PEKuXiaoBi(sdb_base, Computed):
    field_name = u"库消比"
    col_name = u"PE库消比"    
    def get_ts_whole_progress(self):
        relevant_col_list = [u"月度PE社会库存", u"PE消费量"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[u"当月天数"] = [calendar.monthrange(x.year, x.month)[1] for x in tmp_total.index]
        tmp_total[self.col_name] = tmp_total[u"月度PE社会库存"] / (tmp_total[u"PE消费量"] / tmp_total[u"当月天数"])
        return tmp_total   

class PEKuXiaoBi_YuGu(sdb_base, Computed):
    field_name = u"库消比"
    col_name = u"PE库消比(预估)"    
    def get_ts_whole_progress(self):
        relevant_col_list = [u"月度PE社会库存", u"PE消费量", u"月度PE社会库存(预估)", u"PE消费量(预估)", u"PE库消比"]
        
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[u"社会库存预估"] = tmp_total[u"月度PE社会库存"].fillna(0) + tmp_total[u"月度PE社会库存(预估)"].fillna(0)
        tmp_total[u"社会库存预估"][tmp_total[u"月度PE社会库存"].isnull() & tmp_total[u"月度PE社会库存(预估)"].isnull()] = np.nan
        tmp_total[u"消费量预估"] = tmp_total[u"PE消费量"].fillna(0) + tmp_total[u"PE消费量(预估)"].fillna(0)
        tmp_total[u"消费量预估"][tmp_total[u"PE消费量"].isnull() & tmp_total[u"PE消费量(预估)"].isnull()] = np.nan        
        tmp_total[u"当月天数"] = [calendar.monthrange(x.year, x.month)[1] for x in tmp_total.index]
        tmp_total[self.col_name] = tmp_total[u"社会库存预估"] / (tmp_total[u"消费量预估"] / tmp_total[u"当月天数"])
        tmp_total.loc[tmp_total.index <= tmp_total[u"PE库消比"].dropna().index[-1], self.col_name] = np.nan
        return tmp_total 

    def seasonal_plot(self, title=None, start_year=None, axhline=None):
        tmp_series = PEKuXiaoBi().get_ts()
        tmp_df_interpolated, fig, axis = super(sdb_base, self).seasonal_plot(title=title, start_year=start_year, 
                                              axhline=axhline, mode="month", original_ts=tmp_series)
        return tmp_df_interpolated, fig, axis
    
if __name__ == "__main__":
#    ts1 = PEYueDuChanLiang().get_ts()
#    ts2 = LLDYueDuChanLiang().get_ts()
#    ts3 = HDYueDuChanLiang().get_ts()
#    ts4 = LDYueDuChanLiang().get_ts()
#    df = pd.concat([ts1,ts2,ts3,ts4], axis=1)
    
    ts = LLDYueDuChanLiang().seasonal_plot()
#    df, fig, axis = PEFeiLiaoJingJinKou_YuGu().seasonal_plot(start_year=2014)    
    
    
    
    
    
    
    
    
    
    
    