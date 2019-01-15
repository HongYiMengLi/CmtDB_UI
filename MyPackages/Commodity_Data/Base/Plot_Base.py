# -*- coding: utf-8 -*-
"""
Created on Fri Sep 14 10:00:39 2018

@author: 李弘一萌
"""

import pandas as pd
import numpy as np
import os
import calendar
from datetime import datetime
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
from datetime import datetime, timedelta
import matplotlib.dates as mdates
from matplotlib.ticker import FuncFormatter, MultipleLocator, LinearLocator, MaxNLocator
from matplotlib.colors import LinearSegmentedColormap

def df_interpolate(df, mode="seasonal"):
    if mode == "seasonal":
        df_neweast = df.iloc[:,-1].copy()
        count = 0
        for i in range(-1,-len(df),-1):
            if np.isnan(df_neweast.iloc[i]):
                continue
            else:
                count = i + 1
                break
        if count != 0:
            df_neweast = df_neweast.iloc[:count]
        df = pd.concat([df.iloc[:,:-1].interpolate(),df_neweast.interpolate()],axis=1)
        return df
    elif mode == "time_series":
        return df.interpolate()


    
def time_series_to_seasonal_tranform(tmp_series):
#    tmp_series.index = [x.to_pydatetime() for x in tmp_series.index]
    total_year_list = [x.year for x in tmp_series.index]
    year_list = []
    for x in total_year_list:
        if x in year_list:
            continue
        else:
            year_list.append(x)
    year_series_list = []
    for year in year_list:
        tmp_year_series = tmp_series.loc[[x for x in tmp_series.index if x.year == year]].copy()
        tmp_year_series.name = year
#        tmp_year_series.index = [x.strftime("%m-%d") for x in tmp_year_series.index]
        tmp_year_series.index = [datetime(2016, x.month, x.day) for x in tmp_year_series.index]
        if datetime(2016,1,1) not in tmp_year_series.index:
            tmp_added_series = pd.Series(np.nan, index=[datetime(2016,1,1)])
            tmp_added_series.name = tmp_year_series.name
            tmp_year_series = pd.concat([tmp_added_series, tmp_year_series])
        year_series_list.append(tmp_year_series)
    tmp_df = pd.concat(year_series_list,axis=1)
    tmp_df.dropna(how="all", axis=1, inplace=True)        
    return tmp_df 

def month_time_series_to_seasonal_tranform(tmp_series):
#    tmp_series.index = [x.to_pydatetime() for x in tmp_series.index]
    total_year_list = [x.year for x in tmp_series.index]
    year_list = []
    for x in total_year_list:
        if x in year_list:
            continue
        else:
            year_list.append(x)
    year_series_list = []
    for year in year_list:
        tmp_year_series = tmp_series.loc[[x for x in tmp_series.index if x.year == year]].copy()
        tmp_year_series.name = year
#        tmp_year_series.index = [x.strftime("%m-%d") for x in tmp_year_series.index]
        tmp_year_series.index = [x.month for x in tmp_year_series.index]
        year_series_list.append(tmp_year_series)
    tmp_df = pd.concat(year_series_list,axis=1)
    tmp_df.dropna(how="all", axis=1, inplace=True)        
    return tmp_df 

def expected_process(expected_ts):
    expected_year_list = list(set([x.year for x in expected_ts.index]))
    if len(expected_year_list) != 1:
        raise Exception("wrong expected time series length")
    expected_year = expected_year_list[0]
    expected_ts.index = [datetime(2016, x.month, x.day) for x in expected_ts.index]
    expected_ts.name = str(expected_year) + "E"
    if datetime(2016,1,1) not in expected_ts.index:
            tmp_added_series = pd.Series(np.nan, index=[datetime(2016,1,1)])
            tmp_added_series.name = expected_ts.name
            expected_ts = pd.concat([tmp_added_series, expected_ts])
    return expected_ts

def month_expected_process(expected_ts):
    expected_year_list = list(set([x.year for x in expected_ts.index]))
    if len(expected_year_list) != 1:
        raise Exception("wrong expected time series length")
    expected_year = expected_year_list[0]
    expected_ts.index = [x.month for x in expected_ts.index]
    expected_ts.name = str(expected_year) + "E"
    return expected_ts

def time_series_to_seasonal_tranform_date_constraint(tmp_series, date_constraint):
    total_tdate_list = [x for x in tmp_series.index]
    year_list = []
    standard_date_list = []
    standard_date_list.append(datetime(total_tdate_list[0].year-1, date_constraint[0], date_constraint[1]))
    for tdate in total_tdate_list:
        if tdate.year in year_list:
            continue
        else:
            year_list.append(tdate.year)
            standard_date_list.append(datetime(tdate.year, date_constraint[0], date_constraint[1]))
    standard_date_list.append(datetime(tdate.year+1, date_constraint[0], date_constraint[1]))
    count = 0
    year_spread_list = []
    for standard_date in standard_date_list:
        if standard_date != standard_date_list[-1]:
            tmp_near_date = standard_date
            tmp_far_date = standard_date_list[count+1]
            tmp_year_spread_series = tmp_series[(tmp_series.index > tmp_near_date) & 
                                                (tmp_series.index <= tmp_far_date)].copy()
            count += 1
            if len(tmp_year_spread_series) != 0:
                tmp_year_spread_series.name = tmp_far_date.year
                new_tmp_year_spread = tmp_year_spread_series.copy()
                new_index_list = []
                for x in tmp_year_spread_series.index:
                    if x.year != tmp_far_date.year:
                        new_index_list.append(datetime(2016, x.month, x.day))
                    else:
                        if x.month == 2 and x.day == 29:
                            new_tmp_year_spread.drop(x, inplace=True)
                            continue
                        else:
                            new_index_list.append(datetime(2017, x.month, x.day))
                new_tmp_year_spread.index = new_index_list
                year_spread_list.append(new_tmp_year_spread)
    spread_df = pd.concat(year_spread_list, axis=1)
    return spread_df   
            

    
class Plot_Base(object):
    
    @staticmethod
    def series_seasonal_process(tmp_series, date_constraint=None, expected=None):
        if date_constraint is None:
            tmp_series_transformed = time_series_to_seasonal_tranform(tmp_series)
        else:
            tmp_series_transformed = time_series_to_seasonal_tranform_date_constraint(tmp_series, date_constraint)
        if expected is not None:
            expected_new = expected_process(expected)
            tmp_series_transformed = pd.concat([tmp_series_transformed, expected_new], axis=1)
        tmp_df_interpolated = df_interpolate(tmp_series_transformed, mode="seasonal")
        return tmp_df_interpolated



    @staticmethod
    def month_series_seasonal_process(tmp_series, start_year=None, expected=None):
        tmp_series_transformed = month_time_series_to_seasonal_tranform(tmp_series)
        if start_year is not None:
            tmp_series_transformed = Plot_Base.series_seasonal_filter_year(tmp_series_transformed, start_year)
        if expected is not None:
            expected_new = month_expected_process(expected)
            tmp_series_transformed = pd.concat([tmp_series_transformed, expected_new], axis=1)
        return tmp_series_transformed


    
    @staticmethod
    def series_seasonal_filter_year(tmp_interpolated_df, start_year):
        tmp_inter_df = tmp_interpolated_df.T
        tmp_interpolated_df = tmp_inter_df[tmp_inter_df.index >= start_year].T
        return tmp_interpolated_df
    
    @staticmethod
    def add_month_span(ax, tmp_df, tmp_month):
        # Getting the boundaries for dates in feb and march
        start_flag = False
        start_index = 0
        for x in range(1, len(tmp_df)):
            if tmp_df.index[-x].month == tmp_month:
                if not start_flag:
                    start_flag = True
                    start_index = x
            elif start_flag:
                end_index = x
                break
            
                
#        period = tmp_df[tmp_df.index.month == tmp_month].index
        # Highlighting
        if start_flag:
            if start_index == 1:
                period = tmp_df.index[(-end_index+1):]
            else:
                period = tmp_df.index[(-end_index+1):(-start_index+1)]
            ax.axvspan(min(period), max(period), facecolor='k', edgecolor='none', alpha=.2)
        return ax

    @staticmethod
    def last_line_highlight(axis):
        leg = axis.get_legend()
        axis.lines[-1].set_color("r")
        axis.lines[-1].set_linewidth(7)
        leg.get_lines()[-1].set_linewidth(7)
        leg.get_lines()[-1].set_color("r")
        return axis
    
    
    @staticmethod
    def last_line_highlight_expected(axis):    
        axis.lines[-2].set_color("r")
        axis.lines[-2].set_linewidth(10)   
        axis.lines[-1].set_linestyle("--")
        leg = axis.get_legend()
        leg.get_lines()[-1].set_linestyle("--")
        leg.get_lines()[-2].set_linewidth(10)
        leg.get_lines()[-2].set_color("r")
        return axis
        
    @staticmethod    
    def plot_module(tmp_df, title):
        fig = plt.figure(figsize=(19.2,10.8), dpi=100)
        axis = fig.add_subplot(111)
        my_colormap = ["dodgerblue", "slateblue", "darkorange",  "seagreen", "salmon",  "black"]
        cmap = LinearSegmentedColormap.from_list('mycmap', my_colormap)
        tmp_df.plot(ax=axis, color=my_colormap)
        axis.minorticks_off()
        axis.set_title(title, fontsize=40)
        axis.xaxis.set_tick_params(labelsize=40)
        axis.yaxis.set_tick_params(labelsize=40)
        
        plt.xlim(tmp_df.index[0], tmp_df.index[-1])
        plt.ylim(tmp_df.min().min() * 0.99, tmp_df.max().max() * 1.01)
        axis.xaxis.set_major_formatter(mdates.DateFormatter("%m"))
        axis.xaxis.set_major_locator(mdates.MonthLocator())

        leg = axis.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05), shadow=True, frameon=False,
            ncol=len(tmp_df.columns.tolist()), fontsize=30)
        plt.setp(axis.lines, linewidth=5)
        plt.setp(axis.xaxis.get_majorticklabels(), rotation=0, ha="left")
        for line in leg.get_lines():
            line.set_linewidth(5)
        axis = Plot_Base.last_line_highlight(axis)
        yticks = list(axis.get_yticks())
        plt.yticks(yticks, yticks)
        axis.yaxis.set_major_formatter(FuncFormatter(lambda y, _: '{:.0f}'.format(y)))
        axis.tick_params(which='major', length=5, width=4, direction='out')
        return fig, axis
    
    @staticmethod    
    def month_plot_module(tmp_df, title):
        fig = plt.figure(figsize=(19.2,10.8), dpi=100)
        axis = fig.add_subplot(111)
        tmp_df.plot(ax=axis)
        axis.minorticks_off()
#        axis.majorticks_on()
        axis.set_title(title, fontsize=40)
        xmajorLocator   = MultipleLocator(1) #将x主刻度标签设置为20的倍数
#        xmajorFormatter = FormatStrFormatter('%5.1f') #设置x轴标签文本的格式        
        axis.yaxis.set_tick_params(labelsize=40)
        axis.xaxis.set_major_locator(xmajorLocator)
        leg = axis.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05), shadow=True, frameon=False,
            ncol=len(tmp_df.columns.tolist()), fontsize=30)
        plt.setp(axis.lines, linewidth=5, marker="o", markersize=20)
        plt.setp(axis.xaxis.get_majorticklabels(), rotation=0, ha="left")
        for line in leg.get_lines():
            line.set_linewidth(5)
        axis.xaxis.set_tick_params(labelsize=40)
        axis = Plot_Base.last_line_highlight(axis)

        yticks = list(axis.get_yticks())
        plt.yticks(yticks, yticks)
        axis.yaxis.set_major_formatter(FuncFormatter(lambda y, _: '{:.0f}'.format(y)))
        axis.tick_params(which='major', length=10, width=4, direction='inout')
        return fig, axis

    @staticmethod    
    def bar_plot_module(tmp_df, title):
        fig = plt.figure(figsize=(19.2,10.8), dpi=100)
        axis = fig.add_subplot(111)
        my_colormap = ["dodgerblue", "slateblue", "darkorange",  "seagreen", "salmon",  "black"]
        cmap = LinearSegmentedColormap.from_list('mycmap', my_colormap)
        tmp_df.plot.bar(ax=axis, color=my_colormap)
#        axis.minorticks_off()
#        axis.set_title(title, fontsize=40)
#        axis.xaxis.set_tick_params(labelsize=40)
#        axis.yaxis.set_tick_params(labelsize=40)
#        
#        plt.xlim(tmp_df.index[0], tmp_df.index[-1])
#        plt.ylim(tmp_df.min().min() * 0.99, tmp_df.max().max() * 1.01)
#        axis.xaxis.set_major_formatter(mdates.DateFormatter("%m"))
#        axis.xaxis.set_major_locator(mdates.MonthLocator())
#
#        leg = axis.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05), shadow=True, frameon=False,
#            ncol=len(tmp_df.columns.tolist()), fontsize=30)
#        plt.setp(axis.lines, linewidth=5)
#        plt.setp(axis.xaxis.get_majorticklabels(), rotation=0, ha="left")
#        for line in leg.get_lines():
#            line.set_linewidth(5)
#        yticks = list(axis.get_yticks())
#        plt.yticks(yticks, yticks)
#        axis.yaxis.set_major_formatter(FuncFormatter(lambda y, _: '{:.0f}'.format(y)))
#        axis.tick_params(which='major', length=5, width=4, direction='out')
        return fig, axis

    @staticmethod    
    def month_bar_plot_module(tmp_df, title):
        fig = plt.figure(figsize=(19.2,10.8), dpi=100)
        axis = fig.add_subplot(111)
        tmp_df.plot.bar(ax=axis)
        axis.minorticks_off()
#        axis.majorticks_on()
        axis.set_title(title, fontsize=40)
#        xmajorLocator = MultipleLocator(1) #将x主刻度标签设置为20的倍数
#        xmajorFormatter = FormatStrFormatter('%5.1f') #设置x轴标签文本的格式        
        axis.yaxis.set_tick_params(labelsize=40)
#        axis.xaxis.set_major_locator(xmajorLocator)
        leg = axis.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05), shadow=True, frameon=False,
            ncol=len(tmp_df.columns.tolist()), fontsize=30)
#        plt.setp(axis.lines, linewidth=5, marker="o", markersize=20)
        plt.setp(axis.xaxis.get_majorticklabels(), rotation=0, ha="left")
        for line in leg.get_lines():
            line.set_linewidth(5)
        axis.xaxis.set_tick_params(labelsize=40)
#        axis = Plot_Base.last_line_highlight(axis)

        yticks = list(axis.get_yticks())
        plt.yticks(yticks, yticks)
        axis.yaxis.set_major_formatter(FuncFormatter(lambda y, _: '{:.0f}'.format(y)))
        axis.tick_params(which='major', length=10, width=4, direction='inout')
        return fig, axis
    
    def seasonal_plot(self, title=None, start_year=None, axhline=None, mode="daily", date_constraint=None, 
                      original_ts=None, plot_type="line"):
        if (axhline is None) and (hasattr(self, "axhline")):
            axhline = self.axhline
        if (start_year is None) and (hasattr(self, "start_year")):
            start_year = self.start_year
        if title is None:
            if hasattr(self, "fig_title"):
                title = self.fig_title
            else:
                title = self.col_name + u"季节性"
        tmp_series = self.get_ts()
        if original_ts is not None:
            tmp_expected_series = pd.concat([original_ts.iloc[-1:], tmp_series])
        if tmp_series is None:
            print(self.col_name + u"无法提取历史数据，作图失败")
            return None
        if mode == "daily":
            tmp_df_interpolated = self.series_seasonal_process(tmp_series, date_constraint)
            if start_year is not None:
                tmp_df_interpolated = self.series_seasonal_filter_year(tmp_df_interpolated, start_year)
            if plot_type == "line":
                fig, axis = self.plot_module(tmp_df_interpolated, title)
            elif plot_type == "bar":
                fig, axis = self.bar_plot_module(tmp_df_interpolated, title)
        elif mode == "month":
            if original_ts is None:
                tmp_df_interpolated = self.month_series_seasonal_process(tmp_series, start_year)
            else:
                tmp_df_interpolated = self.month_series_seasonal_process(original_ts, start_year, tmp_expected_series)
#            if start_year is not None:
#                tmp_df_interpolated = self.series_seasonal_filter_year(tmp_df_interpolated, start_year)
            if plot_type == "line":
                fig, axis = self.month_plot_module(tmp_df_interpolated, title)
            elif plot_type == "bar":
                fig, axis = self.month_bar_plot_module(tmp_df_interpolated, title)
            if original_ts is not None:
                axis = Plot_Base.last_line_highlight_expected(axis)
        if axhline is not None:
            axis.axhline(y=axhline, color="k")
        return tmp_df_interpolated, fig, axis
     
    def ts_plot(self, start_date=None):
        tmp_title = self.col_name
        tmp_ts_list = [self.get_ts()]
        tmp_df = pd.concat(tmp_ts_list, axis=1, sort=False)
        if not start_date:
            tmp_df = tmp_df[tmp_df.index>=start_date]
        fig, axis = Plot_Base.plot_module(tmp_df, tmp_title)
        axis.minorticks_off()
        axis.set_title(tmp_title, fontsize=40)
        axis.xaxis.set_tick_params(labelsize=40)
        axis.yaxis.set_tick_params(labelsize=40)
        axis.set_xlabel("")
        plt.xlim(tmp_df.index[0], tmp_df.index[-1])
        axis.xaxis.set_major_formatter(mdates.DateFormatter("%y-%m"))
        axis.xaxis.set_major_locator(mdates.MonthLocator())
    
        plt.setp(axis.lines, linewidth=5)
        plt.setp(axis.xaxis.get_majorticklabels(), rotation=0, ha="left")
    
        axis.yaxis.set_major_formatter(FuncFormatter(lambda y, _: '{:.0f}'.format(y)))
        axis.tick_params(which='major', length=5, width=4, direction='out')
        
        axis.xaxis.set_major_formatter(mdates.DateFormatter("%y-%m"))
        axis.xaxis.set_major_locator(mdates.AutoDateLocator())
        axis.xaxis.set_tick_params(labelsize=25, labelrotation=45)
        axis.lines[-1].set_linewidth(6)
        leg = axis.legend(loc='upper center', bbox_to_anchor=(0.5, -0.15), frameon=False, shadow=True, fontsize=20)
        axis.spines['top'].set_visible(False)  #去掉上边框
        return tmp_df, fig, axis
#    def single_seasonal_plot_and_output(self, title=None, start_year=None, axhline=None):
#        fig_tuple = self.seasonal_plot(title, start_year, axhline)
#        if fig_tuple is None:
#            return None
#        else:
#            fig_tuple[1].savefig(LPP_Plot.save_path + u"tmp/" + title + u".jpeg", bbox_inches="tight")
#            return fig_tuple[0]   
    
    
  