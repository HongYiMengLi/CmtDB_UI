# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 10:48:40 2018

@author: 李弘一萌
"""

import pandas as pd
from datetime import datetime
from .TA_Base import TA_Base
from ...Base.DataType_Base import Manual, Computed, WindData
from ...Base.Plot_Base import Plot_Base
from matplotlib.ticker import FuncFormatter

class sdb_base(TA_Base, Plot_Base):
    table_english_name = "SupplyDemandBalance"
    table_chinese_name = u"供需平衡表"
    
    def output(self):
        print(self.table_english_name)
    
    def get_relevant_df(self, col_list):
        local_col_name_list = sdb_base.get_all_table_classname()
        col_cls_list = []
        for x in col_list:
            col_cls_name = str(TA_Base.get_class_name(x))
            if col_cls_name not in local_col_name_list:
                col_cls_list.append(eval(TA_Base.get_table_class_full_variable(x)))
            else:
                col_cls_list.append(eval(col_cls_name))
        ts_list = [x().get_ts() for x in col_cls_list]
        tmp_table_df = pd.concat(ts_list, axis=1).dropna(how="all")
        return tmp_table_df 

###########################################################################################################################
""" 产能 """   
 
class PXChanNeng(sdb_base, Manual):
    field_name = u"产能"
    col_name = u"PX产能"
    
class PTAChanNeng(sdb_base, Manual):
    field_name = u"产能"
    col_name = u"PTA产能"

class JuZhiChanNeng(sdb_base, Manual):
    field_name = u"产能"
    col_name = u"聚酯产能"

###########################################################################################################################
""" 进口 """    

class PXJinKouLiang(sdb_base, Manual):
    field_name = u"进口"
    col_name = u"PX进口量"
    
class PTAJinKouLiang(sdb_base, Manual):
    field_name = u"进口"
    col_name = u"PTA进口量"

###########################################################################################################################
""" 出口 """    

class PXChuKouLiang(sdb_base, Manual):
    field_name = u"出口"
    col_name = u"PX出口量"
    
class PTAChuKouLiang(sdb_base, Manual):
    field_name = u"出口"
    col_name = u"PTA出口量"

###########################################################################################################################
""" 开工 """  
class PXKaiGongLv(sdb_base, Manual):
    field_name = u"开工"
    col_name = u"PX开工率"
    start_year = 2014
    def seasonal_plot(self, title=None, start_year=None, axhline=None):
        tmp_df_interpolated, fig, axis = super(sdb_base, self).seasonal_plot(title=title, start_year=start_year)
        axis.yaxis.set_major_formatter(FuncFormatter(lambda y, _: '{:.0%}'.format(y)))
        return tmp_df_interpolated, fig, axis
    
class PTAKaiGongLv(sdb_base, Manual):
    field_name = u"开工"
    col_name = u"PTA开工率"
    start_year = 2014
    def seasonal_plot(self, title=None, start_year=None, axhline=None):
        tmp_df_interpolated, fig, axis = super(sdb_base, self).seasonal_plot(title=title, start_year=start_year)
        axis.yaxis.set_major_formatter(FuncFormatter(lambda y, _: '{:.0%}'.format(y)))
        return tmp_df_interpolated, fig, axis
    
class JuZhiKaiGongLv(sdb_base, Manual):
    field_name = u"开工"
    col_name = u"聚酯开工率"
    start_year = 2014
    def seasonal_plot(self, title=None, start_year=None, axhline=None):
        tmp_df_interpolated, fig, axis = super(sdb_base, self).seasonal_plot(title=title, start_year=start_year)
        axis.yaxis.set_major_formatter(FuncFormatter(lambda y, _: '{:.0%}'.format(y)))
        return tmp_df_interpolated, fig, axis
    
class ZhiZaoKaiGongLv(sdb_base, Manual):
    field_name = u"开工"
    col_name = u"织造开工率"
    start_year = 2014
    def seasonal_plot(self, title=None, start_year=None, axhline=None):
        tmp_df_interpolated, fig, axis = super(sdb_base, self).seasonal_plot(title=title, start_year=start_year)
        axis.yaxis.set_major_formatter(FuncFormatter(lambda y, _: '{:.0%}'.format(y)))
        return tmp_df_interpolated, fig, axis
    
class PTAYueJunKaiGong(sdb_base, Computed):
    field_name = u"开工"
    col_name = u"PTA月均开工"    
    def get_ts_whole_progress(self):
        relevant_col_list = [u"PTA开工率"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_series = tmp_total[u"PTA开工率"].resample("M").mean()
        tmp_series.name = self.col_name
        return tmp_series.to_frame()
    def seasonal_plot(self, title=None, start_year=None, axhline=None):
        tmp_df_interpolated, fig, axis = super(sdb_base, self).seasonal_plot(title=title, start_year=start_year)
        axis.yaxis.set_major_formatter(FuncFormatter(lambda y, _: '{:.0%}'.format(y)))
        return tmp_df_interpolated, fig, axis
    
###########################################################################################################################
""" 产量 """  

class PXRiChanLiang(sdb_base, Computed):
    field_name = u"产量"
    col_name = u"PX日产量"
    
    def get_ts_whole_progress(self):
        relevant_col_list = [u"PX产能", u"PX开工率"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"PX产能"] * tmp_total[u"PX开工率"] / 365
        return tmp_total
    
class PTARiChanLiang(sdb_base, Computed):
    field_name = u"产量"
    col_name = u"PTA日产量"
    
    def get_ts_whole_progress(self):
        relevant_col_list = [u"PTA产能", u"PTA开工率"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"PTA产能"] * tmp_total[u"PTA开工率"] / 365
        return tmp_total

class JuZhiRiChanLiang(sdb_base, Computed):
    field_name = u"产量"
    col_name = u"聚酯日产量"    
    def get_ts_whole_progress(self):
        relevant_col_list = [u"聚酯产能", u"聚酯开工率"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"聚酯产能"] * tmp_total[u"聚酯开工率"] / 365
        return tmp_total
    
class JuZhiDuiYingPTAXiaoHaoLiang(sdb_base, Computed):
    field_name = u"产量"
    col_name = u"聚酯对应PTA消耗量"    
    def get_ts_whole_progress(self):
        relevant_col_list = [u"聚酯日产量"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"聚酯日产量"] * 0.86
        return tmp_total    
    
class PXYueDuChanLiang(sdb_base, Computed):
    field_name = u"产量"
    col_name = u"PX月度产量"    
    def get_ts_whole_progress(self):
        relevant_col_list = [u"PX日产量"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_series = tmp_total[u"PX日产量"].resample("M").sum()
        tmp_series.name = self.col_name
        return tmp_series.to_frame()     

class PTAYueDuChanLiang(sdb_base, Computed):
    field_name = u"产量"
    col_name = u"PTA月度产量"    
    def get_ts_whole_progress(self):
        relevant_col_list = [u"PTA日产量"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_series = tmp_total[u"PTA日产量"].resample("M").sum()
        tmp_series.name = self.col_name
        return tmp_series.to_frame()     

class JuZhiYueDuChanLiang(sdb_base, Computed):
    field_name = u"产量"
    col_name = u"聚酯月度产量"    
    def get_ts_whole_progress(self):
        relevant_col_list = [u"聚酯日产量"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_series = tmp_total[u"聚酯日产量"].resample("M").sum()
        tmp_series.name = self.col_name
        return tmp_series.to_frame()         

###########################################################################################################################
""" 表观消费量 """ 

class PXBiaoGuanXiaoFeiLiang(sdb_base, Computed):
    field_name = u"表观消费量"
    col_name = u"PX表观消费量"    
    def get_ts_whole_progress(self):
        relevant_col_list = [u"PX月度产量", u"PX进口量", u"PX出口量"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total["PX月度产量"] + tmp_total["PX进口量"] - tmp_total["PX出口量"]
        return tmp_total  
    
###########################################################################################################################
""" 库存 """ 

class PXLeiKuLiang(sdb_base, Computed):
    field_name = u"库存"
    col_name = u"PX累库量"    
    def get_ts_whole_progress(self):
        relevant_col_list = [u"PX表观消费量", u"PTA月度产量"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total["PX表观消费量"] - tmp_total["PTA月度产量"] * 0.66
        return tmp_total 


class PXKuCunLiang(sdb_base, Computed):
    field_name = u"库存"
    col_name = u"PX库存量"    
    def get_ts_whole_progress(self):
        relevant_col_list = [u"PX累库量"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        start_date = datetime(2014, 12, 31)
        original_value = 139.0801
        tmp_total = tmp_total[tmp_total.index>=start_date]
        tmp_total[self.col_name] = tmp_total[u"PX累库量"].cumsum() + original_value
        return tmp_total 


class PXKuCunTianShu(sdb_base, Computed):
    field_name = u"库存"
    col_name = u"PX库存天数"    
    def get_ts_whole_progress(self):
        relevant_col_list = [u"PX库存量", u"PTA产能", u"PTA月均开工"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total["PX库存量"] /(tmp_total["PTA产能"] * tmp_total["PTA月均开工"] / 365) / 0.66
        return tmp_total 
    
    
class PTAQiTaYongTuXiaoFeiLiang(sdb_base, Manual):
    field_name = u"库存"
    col_name = u"PTA其他用途消费量"

    
class PTARiLeiKuLiang(sdb_base, Computed):
    field_name = u"库存"
    col_name = u"PTA日累库量"    
    def get_ts_whole_progress(self):
        relevant_col_list = [u"PTA日产量", u"聚酯对应PTA消耗量", u"PTA其他用途消费量"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total["PTA日产量"] - tmp_total["聚酯对应PTA消耗量"] - tmp_total["PTA其他用途消费量"]
        return tmp_total  


class PTASheHuiKuCun(sdb_base, Computed):
    field_name = u"库存"
    col_name = u"PTA社会库存"    
    def get_ts_whole_progress(self):
        start_date = datetime(2015, 1, 3)
        original_value = 45.93947289        
        relevant_col_list = [u"PTA日累库量", u"PTA进口量", u"PTA出口量"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total = tmp_total[tmp_total.index>=start_date]
        tmp_total["temp_result"] = tmp_total["PTA日累库量"] + tmp_total["PTA进口量"] - tmp_total["PTA出口量"]
        tmp_total[self.col_name] = original_value + tmp_total["temp_result"].cumsum()
        return tmp_total  


class PTAKuXiaoBi(sdb_base, Computed):
    field_name = u"库存"
    col_name = u"PTA库销比"    
    def get_ts_whole_progress(self):
        relevant_col_list = [u"PTA社会库存", u"聚酯产能"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total["PTA社会库存"]  / (tmp_total["聚酯产能"] / 365) / 0.865
        return tmp_total  
    
    
    

if __name__ == "__main__":
    a = PXKuCunLiang().get_ts()
    
    
    
    
    
    
    
    
    
    