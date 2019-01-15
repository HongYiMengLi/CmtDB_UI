# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 10:45:53 2018

@author: 李弘一萌
"""

import pandas as pd
from datetime import datetime
from .MA_Base import MA_Base
from . import MA_SpotPrice
from ...Base.DataType_Base import Manual, Computed, WindData
from ...Base.Plot_Base import Plot_Base
from matplotlib.ticker import FuncFormatter

class downstream_base(MA_Base, Plot_Base):
    table_english_name = "Downstream"
    table_chinese_name = u"下游"
    
    def output(self):
        print("Downstream")
    
    def get_relevant_df(self, col_list):
        local_col_name_list = downstream_base.get_all_table_classname()
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
""" MTO利润 """

class YiErChunJiaGe_HuaDong(downstream_base, WindData):
    field_name = u"MTO利润"
    col_name = u"乙二醇价格_华东"
    wind_code = "S5443225"  
    
class BingXiJiaGe_ShanDong(downstream_base, WindData):
    field_name = u"MTO利润"
    col_name = u"丙烯价格_山东"
    wind_code = "S5438872"      

class PPChuChangJia_NingBoFuDe(downstream_base, WindData):
    field_name = u"MTO利润"
    col_name = u"PP出厂价_宁波富德"
    wind_code = "S5438872" 
    
    
class JiaChunZhiXiTingLiRun_NingBoFuDe(downstream_base, Computed):
    field_name = u"MTO利润"
    col_name = u"甲醇制烯烃利润_宁波富德" 
    start_year = 2014
    def get_ts_whole_progress(self):
        relevant_col_list = [u"PP出厂价_宁波富德", u"乙二醇价格_华东", u"甲醇价格_江苏"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"PP出厂价_宁波富德"] * 0.4 + tmp_total[u"乙二醇价格_华东"] * 0.5 - (tmp_total[u"甲醇价格_江苏"] * 3 + \
                                   1000) * 0.4 - (tmp_total[u"甲醇价格_江苏"] * 2.5 * 0.57 + 1800) * 0.5
        return tmp_total  
    
###########################################################################################################################
""" 醋酸利润 """

class CuSuanJiaGe_JiangSu(downstream_base, WindData):
    field_name = u"醋酸利润"
    col_name = u"醋酸价格_江苏"
    wind_code = "S5439477"  
    
class CuSuanLiRun(downstream_base, Computed):
    field_name = u"醋酸利润"
    col_name = u"醋酸利润"   
    def get_ts_whole_progress(self):
        relevant_col_list = [u"醋酸价格_江苏", u"甲醇价格_江苏"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"醋酸价格_江苏"] - tmp_total[u"甲醇价格_江苏"] * 0.54 - 900
        return tmp_total  


###########################################################################################################################
""" 甲醛利润 """

class JiaQuanJiaGe(downstream_base, Manual):
    field_name = u"甲醛利润"
    col_name = u"甲醛价格"
    
class JiaQuanLiRun(downstream_base, Computed):
    field_name = u"甲醛利润"
    col_name = u"甲醛利润"   
    def get_ts_whole_progress(self):
        relevant_col_list = [u"甲醛价格", u"甲醇价格_临沂"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"甲醛价格"] - tmp_total[u"甲醇价格_临沂"] * 0.4 - 100
        return tmp_total  
    
    
###########################################################################################################################
""" 二甲醚利润 """

class ErJiaMiJiaGe(downstream_base, WindData):
    field_name = u"二甲醚利润"
    col_name = u"二甲醚价格"
    wind_code = "S5439440"
    
class ErJiaMiLiRun(downstream_base, Computed):
    field_name = u"二甲醚利润"
    col_name = u"二甲醚利润"   
    def get_ts_whole_progress(self):
        relevant_col_list = [u"二甲醚价格", u"甲醇价格_江苏"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"二甲醚价格"] - tmp_total[u"甲醇价格_江苏"] * 1.41 - 300
        return tmp_total  


###########################################################################################################################
""" 下游开工率 """  

class MTOOrMTPKaiGongLv(downstream_base, Manual):
    field_name = u"下游开工率"
    col_name = u"MTO/MTP开工率"
    
class JiaQuanKaiGongLv(downstream_base, Manual):
    field_name = u"下游开工率"
    col_name = u"甲醛开工率"
    
class ErJiaMiKaiGongLv(downstream_base, Manual):
    field_name = u"下游开工率"
    col_name = u"二甲醚开工率"
    start_year = 2015
    
class MTBEKaiGongLv(downstream_base, Manual):
    field_name = u"下游开工率"
    col_name = u"MTBE开工率"
    
class CuSuanKaiGongLv(downstream_base, Manual):
    field_name = u"下游开工率"
    col_name = u"醋酸开工率"
    
class JiaSuoQuanKaiGongLv(downstream_base, Manual):
    field_name = u"下游开工率"
    col_name = u"甲缩醛开工率"
    
class DMFKaiGongLv(downstream_base, Manual):
    field_name = u"下游开工率"
    col_name = u"DMF开工率"
    


if __name__ == "__main__": 
    ts = ErJiaMiJiaGe().get_ts()
#    ts, fig, axis = ErJiaMiKaiGongLv().seasonal_plot()
    





























    

    