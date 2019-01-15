# -*- coding: utf-8 -*-
"""
Created on Mon Aug 27 08:35:24 2018

@author: 李弘一萌
"""

import pandas as pd
from datetime import datetime
from .L_Base import L_Base
from .L_Device import L_Device_Process
from ...Base.DataType_Base import Manual, Computed, WindData
from ...Base.Plot_Base import Plot_Base
from matplotlib.ticker import FuncFormatter

class inventory_base(L_Base, Plot_Base):
    table_english_name = "Inventory"
    table_chinese_name = u"库存"
#    original_db_filepath = data_path + u"LPP价格数据库.xlsx"
    
    def output(self):
        print("Inventory")
    
    def get_relevant_df(self, col_list):
        local_col_name_list = inventory_base.get_all_table_classname()
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
    
    
    
    
################################################################################################################################    
""" 石化库存 """
        
class ZhongShiHua(inventory_base, Manual):
    field_name = u"石化库存"
    col_name = u"石化库存_中石化"
    
class ZhongShiYou(inventory_base, Manual):
    field_name = u"石化库存"
    col_name = u"石化库存_中石油"
    
class ShiHuaZongKuCun(inventory_base, Manual):
    field_name = u"石化库存"
    col_name = u"石化库存_总库存"

""" 计算指标 """

class PEShiHuaKuCun(inventory_base, Computed):
    field_name = u"石化库存"
    col_name = u"PE石化库存"
    def get_ts_whole_progress(self):
#        print self.col_name + u"暂不可用，无L产量占比数据"
#        return None
        relevant_col_list = [u"石化库存_总库存"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        LLD_yield1 = L_Device_Process.get_product_yield_for_specific_field(u"线性", u"线性")
        LLD_yield2 = L_Device_Process.get_product_yield_for_specific_field(u"全密度", u"线性")  
        LLD_yield = pd.concat([LLD_yield1, LLD_yield2], axis=1).fillna(0)
        LLD_yield.columns = ["1", "2"]
        LLD_yield["LLD_yield"] = LLD_yield["1"] + LLD_yield["2"]
        PE_yield = L_Device_Process.get_product_yield()
        PE_yield.name = "PE_yield"
        yield_df = pd.concat([LLD_yield, PE_yield], axis=1)
        yield_df[u"L产量占比"] = yield_df["LLD_yield"] / yield_df["PE_yield"]
        tmp_total = pd.concat([tmp_total, yield_df[u"L产量占比"].copy()], axis=1)
        tmp_total[self.col_name] = tmp_total[u"石化库存_总库存"] * 0.1941 / tmp_total[u"L产量占比"]
        return tmp_total
        
################################################################################################################################    
""" 港口库存 """

class PEShangHaiGang(inventory_base, Manual):
    field_name = u"港口库存"
    col_name = u"PE库存_上海港"

class PETianJingGang(inventory_base, Manual):
    field_name = u"港口库存"
    col_name = u"PE库存_天津港"

class PEHuangPu(inventory_base, Manual):
    field_name = u"港口库存"
    col_name = u"PE库存_黄埔"

class PEQingDaoGang(inventory_base, Manual):
    field_name = u"港口库存"
    col_name = u"PE库存_青岛港"

""" 计算指标 """
class PEGangKouKuCun(inventory_base, Computed):    
    field_name = u"港口库存"
    col_name = u"PE港口总库存"
    axhline = 0
    start_year = 2014    
    
    def get_ts_whole_progress(self):
        relevant_col_list = [u"PE库存_上海港", u"PE库存_天津港", u"PE库存_黄埔", u"PE库存_青岛港"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"PE库存_上海港"] + tmp_total[u"PE库存_天津港"] + \
                                   tmp_total[u"PE库存_黄埔"] + tmp_total[u"PE库存_青岛港"]
        return tmp_total
    
#    def seasonal_plot(self, title=None, start_year=None, axhline=None):
#        if (axhline is None) and (hasattr(self, "axhline")):
#            axhline = self.axhline
#        if (start_year is None) and (hasattr(self, "start_year")):
#            start_year = self.start_year
#        if title is None:
#            if hasattr(self, "fig_title"):
#                title = self.fig_title
#            else:
#                title = self.col_name + u"季节性"
#        tmp_series = self.get_ts()
#        if tmp_series is None:
#            print(self.col_name + u"无法提取历史数据，作图失败")
#            return None
#        tmp_df_interpolated = self.series_seasonal_process(tmp_series)
#        if start_year is not None:
#            tmp_df_interpolated = self.series_seasonal_filter_year(tmp_df_interpolated, start_year)
#        fig, axis = self.plot_module(tmp_df_interpolated, title)
#        leg = axis.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05), fancybox=True, shadow=True, 
#            ncol=4, fontsize=30)
#        for line in leg.get_lines():
#            line.set_linewidth(5)
#        if axhline is not None:
#            axis.axhline(y=axhline, color="k")
#        return tmp_df_interpolated, fig, axis

################################################################################################################################    
""" 社会库存 """

class PESheHuiKuCun(inventory_base, Computed):
    field_name = u"社会库存"
    col_name = u"PE社会库存"
    def get_ts_whole_progress(self):
        relevant_col_list = [u"PE石化库存", u"PE港口总库存", u"PE库存_煤化工"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"PE石化库存"] + tmp_total[u"PE港口总库存"] + tmp_total[u"PE库存_煤化工"] / 10000
        return tmp_total    
        
################################################################################################################################    
""" 煤化工库存 """

class ZhongShiYou_MeiHuaGongHD(inventory_base, Manual):
    field_name = u"煤化工库存"
    col_name = u"LLD库存_中石油(煤化工HD)"
    
class ZhongShiHua_MeiHuaGongLD(inventory_base, Manual):
    field_name = u"煤化工库存"
    col_name = u"LLD库存_中石化(煤化工LD)"

class MeiHuaGongPE(inventory_base, Manual):
    field_name = u"煤化工库存"
    col_name = u"PE库存_煤化工"
    axhline = 0
    start_year = 2016
    
#    def seasonal_plot(self, title=None, start_year=None, axhline=None):
#        if (axhline is None) and (hasattr(self, "axhline")):
#            axhline = self.axhline
#        if (start_year is None) and (hasattr(self, "start_year")):
#            start_year = self.start_year
#        if title is None:
#            if hasattr(self, "fig_title"):
#                title = self.fig_title
#            else:
#                title = self.col_name + u"季节性"
#        tmp_series = self.get_ts() / 10000
#        if tmp_series is None:
#            print(self.col_name + u"无法提取历史数据，作图失败")
#            return None
#        tmp_df_interpolated = self.series_seasonal_process(tmp_series)
#        if start_year is not None:
#            tmp_df_interpolated = self.series_seasonal_filter_year(tmp_df_interpolated, start_year)
#        fig, axis = self.plot_module(tmp_df_interpolated, title)
#        leg = axis.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05), fancybox=True, shadow=True, 
#            ncol=4, fontsize=30)
#        for line in leg.get_lines():
#            line.set_linewidth(5)
#        if axhline is not None:
#            axis.axhline(y=axhline, color="k")
#        return tmp_df_interpolated, fig, axis
    
class MeiHuaGongLLD(inventory_base, Manual):
    field_name = u"煤化工库存"
    col_name = u"LLD库存_煤化工"    


if __name__ == "__main__":    
    a = PESheHuiKuCun().get_ts()
    