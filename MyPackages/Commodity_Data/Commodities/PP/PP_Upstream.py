# -*- coding: utf-8 -*-
"""
Created on Wed Aug 29 10:56:09 2018

@author: 李弘一萌
"""

import pandas as pd
from datetime import datetime
from .PP_Base import PP_Base
from . import PP_SpotPrice
from . import PP_Macro
from . import PP_Others
from ...Base.DataType_Base import Manual, Computed, WindData
from ...Base.Plot_Base import Plot_Base
from matplotlib.ticker import FuncFormatter

class upstream_base(PP_Base, Plot_Base):
    table_english_name = "Upstream"
    table_chinese_name = u"上游"
    
    def output(self):
        print("Upstream")
    
    def get_relevant_df(self, col_list):
        local_col_name_list = upstream_base.get_all_table_classname()
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
""" 油制 """  
    
class WTIYuanYou(upstream_base, WindData):
    field_name = u"油制"
    col_name = u"WTI原油价格"
    wind_code = "M0000005"
 
class BrentYuanYou(upstream_base, WindData):
    field_name = u"油制"
    col_name = u"布伦特原油价格"
    wind_code = "S0031525"
 
class ShiNaoYou_CFRRiBen(upstream_base, WindData):
    field_name = u"油制"
    col_name = u"石脑油:CFR价格_日本"
    wind_code = "S5428960"

class BingXi_FOBHanGuo(upstream_base, WindData):
    field_name = u"油制"
    col_name = u"丙烯:FOB价格_韩国"
    wind_code = "S5400544"
 
class BingXi_CFRZhongGuo(upstream_base, WindData):
    field_name = u"油制"
    col_name = u"丙烯:CFR价格_中国"
    wind_code = "S5431564"

""" 计算指标 """  
    
class PPYouZhiLiRun(upstream_base, Computed):
    field_name = u"油制"
    col_name = u"PP油制利润"
    def get_ts_whole_progress(self):
        relevant_col_list = [u"PP拉丝价格_中石化", u"石脑油:CFR价格_日本", u"汇卖价(中行):美元兑人民币", u"增值税"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"PP拉丝价格_中石化"] - ((tmp_total[u"石脑油:CFR价格_日本"] * tmp_total[u"汇卖价(中行):美元兑人民币"] \
                                   * 1.01 * (1 + tmp_total[u"增值税"]) + 50) * 1.35 + 800)
        return tmp_total

###########################################################################################################################
""" 煤制 """  

class KengKouMei_DongSheng(upstream_base, WindData):
    field_name = u"煤制"
    col_name = u"坑口煤价格_东胜"
    wind_code = "S5101766"
    def download_wind_quote(self, start_date=None, end_date=None):
        tmp_update_df = super(KengKouMei_DongSheng, self).download_wind_quote(start_date=start_date, end_date=end_date)
        if tmp_update_df is None:
            return None
        else:
            tmp_series = self.get_ts()
            if start_date is None:
                tmp_last = pd.DataFrame(tmp_series.iloc[-1:].copy())
                tmp_last.columns = tmp_update_df.columns
                tmp_update_df = pd.concat([tmp_last, tmp_update_df])
                tmp_update_df = tmp_update_df[~tmp_update_df.index.duplicated()]
            tmp_update_df = tmp_update_df.resample("B").bfill()
            return tmp_update_df
    
""" 计算指标 """  

class PPMeiZhiLiRun(upstream_base, Computed):
    field_name = u"煤制"
    col_name = u"PP煤制利润"
    axhline = 0
    def get_ts_whole_progress(self):
        relevant_col_list = [u"PP拉丝价格_华东", u"坑口煤价格_东胜"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[u"坑口煤价格_东胜"] = tmp_total[u"坑口煤价格_东胜"].fillna(method="ffill")
        tmp_total[self.col_name] = tmp_total[u"PP拉丝价格_华东"] - 260 - tmp_total[u"坑口煤价格_东胜"] * 7.41 - 4780.57
        return tmp_total

###########################################################################################################################
""" MTO """ 

class JiaChun_CFRZhongGuo(upstream_base, WindData):
    field_name = u"MTO"
    col_name = u"甲醇:CFR价格_中国"
    wind_code = "S5416976"

class JiangSuJiaChunJiaGe(upstream_base, WindData):
    field_name = u"MTO"
    col_name = u"甲醇价格_江苏"
    wind_code = "S5418787"

class NeiMengJiaChunJiaGe(upstream_base, WindData):
    field_name = u"MTO"
    col_name = u"甲醇价格_内蒙"
    wind_code = "S5418767"
    
class MEG(upstream_base, WindData):
    field_name = u"MTO"
    col_name = u"MEG价格_华东"
    wind_code = "S5439184"
    
""" 计算指标 """    
    
class XiBeiPPWaiGouJiaChunZhiLiRun(upstream_base, Computed):
    field_name = u"MTO"
    col_name = u"PP外购甲醇制利润_西北"
    axhline = 0
    start_year = 2016
    def get_ts_whole_progress(self):
        relevant_col_list = [u"PP拉丝价格_华东", u"甲醇价格_内蒙"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"PP拉丝价格_华东"] - 260 - tmp_total[u"甲醇价格_内蒙"] * 2.8 - 1100
        return tmp_total   

class NingBoFuDeMTOZongHeLiRun(upstream_base, Computed):
    field_name = u"MTO"
    col_name = u"MTO综合利润_宁波富德"
    axhline = 0
    start_year = 2016
    def get_ts_whole_progress(self):
        relevant_col_list = [u"PP拉丝价格_华东", u"PP拉丝价格_富德", u"MEG价格_华东", u"甲醇价格_江苏"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[u"PP拉丝富德或华东"] = tmp_total[u"PP拉丝价格_富德"]
        sub_index = tmp_total.index <= datetime(2016,10,27)
        tmp_total.loc[sub_index, u"PP拉丝富德或华东"] =  tmp_total.loc[sub_index, u"PP拉丝价格_华东"]
        tmp_total[self.col_name] = (0.44 * tmp_total[u"PP拉丝富德或华东"] + 0.56 * tmp_total[u"MEG价格_华东"]) - (tmp_total[u"甲醇价格_江苏"] \
                                     * 3 + 400 + 700) * 0.44 - ((tmp_total[u"甲醇价格_江苏"] * 3 + 400) * 0.605 + 600) * 0.56
        return tmp_total

###########################################################################################################################
""" PDH """ 

class BingXi_CFRHuaDong(upstream_base, WindData):
    field_name = u"PDH"
    col_name = u"丙烯:CFR价格_华东"
    wind_code = "S5122021"
    
class BingXi_JingBo(upstream_base, Manual):
    field_name = u"PDH"
    col_name = u"丙烯价格_京博"

class BingXi_WanHua(upstream_base, Manual):
    field_name = u"PDH"
    col_name = u"丙烯价格_万华"
    
""" 计算指标 """
 
class ShanDongBingXi(upstream_base, Computed):
    field_name = u"PDH"
    col_name = u"丙烯价格_山东"
    def get_ts_whole_progress(self):
        relevant_col_list = [u"丙烯价格_京博", u"丙烯价格_万华"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total.mean(axis=1)
        return tmp_total
    
class PDHLiRun(upstream_base, Computed):
    field_name = u"PDH"
    col_name = u"PDH利润"
    axhline = 0
    start_year = 2016
    def get_ts_whole_progress(self):
        relevant_col_list = [u"丙烯价格_山东", u"丙烯:CFR价格_华东", u"汇卖价(中行):美元兑人民币", u"增值税"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"丙烯价格_山东"] - 1.2 * tmp_total[u"丙烯:CFR价格_华东"] * tmp_total[u"汇卖价(中行):美元兑人民币"] * \
                                    (1 + tmp_total[u"增值税"]) * 1.01 - 1500
        return tmp_total

###########################################################################################################################
""" 利润 """     
""" 计算指标 """

class PPJinKouLiRun(upstream_base, Computed):
    field_name = u"利润"
    col_name = u"PP进口利润"
    axhline = 0
    start_year = 2016    
    def get_ts_whole_progress(self):
        relevant_col_list = [u"PP拉丝价格_华东进口", u"PP美金盘:CFR价格_远东", u"汇卖价(中行):美元兑人民币", u"增值税"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"PP拉丝价格_华东进口"] - tmp_total[u"PP美金盘:CFR价格_远东"] * tmp_total[u"汇卖价(中行):美元兑人民币"] \
                                    * 1.065 * (1 + tmp_total[u"增值税"]) - 100
        return tmp_total

class PPChuKouLiRun(upstream_base, Computed):
    field_name = u"利润"
    col_name = u"PP出口利润"
    axhline = 0
    start_year = 2015    
    def get_ts_whole_progress(self):
        relevant_col_list = [u"PP美金盘:CFR价格_远东", u"PP出口美金价"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"PP美金盘:CFR价格_远东"] - tmp_total[u"PP出口美金价"]
        return tmp_total

class PPZhuanYunJiaCha(upstream_base, Computed):
    field_name = u"利润"
    col_name = u"PP转运价差_中国至东南亚"
    axhline = 30
    start_year = 2016    
    def get_ts_whole_progress(self):
        relevant_col_list = [u"PP注塑:CFR价格_东南亚", u"PP注塑:CFR价格_远东"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"PP注塑:CFR价格_东南亚"] - tmp_total[u"PP注塑:CFR价格_远东"]
        return tmp_total


if __name__ == "__main__":
    ts = PPZhuanYunJiaCha().get_ts()






    
    
    
    
    
    
    