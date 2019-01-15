# -*- coding: utf-8 -*-
"""
Created on Mon Aug 27 08:34:29 2018

@author: 李弘一萌
"""

import pandas as pd
from datetime import datetime
from .L_Base import L_Base
from . import L_SpotPrice, L_Others, L_Macro
from ...Base.DataType_Base import Manual, Computed, WindData
from ...Base.Plot_Base import Plot_Base
from matplotlib.ticker import FuncFormatter

class upstream_base(L_Base, Plot_Base):
    table_english_name = "Upstream"
    table_chinese_name = u"上游"
#    original_db_filepath = data_path + u"LPP价格数据库.xlsx"
    
    def output(self):
        print("Upstream")
    
    def get_relevant_df(self, col_list):
        local_col_name_list = upstream_base.get_all_table_classname()
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
 
class YiXi_CFRDongBeiYa(upstream_base, WindData):
    field_name = u"油制"
    col_name = u"乙烯:CFR价格_东北亚"
    wind_code = "S5400549"
 

""" 计算指标 """  
    
class LYouZhiLiRun(upstream_base, Computed):
    field_name = u"油制"
    col_name = u"L油制利润"
    def get_ts_whole_progress(self):
        relevant_col_list = [u"LLD膜价格_中石化", u"石脑油:CFR价格_日本", u"汇卖价(中行):美元兑人民币", u"增值税"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"LLD膜价格_中石化"] - ((tmp_total[u"石脑油:CFR价格_日本"] * tmp_total[u"汇卖价(中行):美元兑人民币"] \
                                   * 1.01 * (1 + tmp_total[u"增值税"]) + 50) * 1.35 + 1200)
        return tmp_total    
    
    
###########################################################################################################################
""" 煤制 """  

class KengKouMei_DongSheng(upstream_base, WindData):
    field_name = u"煤制"
    col_name = u"坑口煤价格_东胜"
    wind_code = "S5101766"
    def download_wind_quote(self, start_date=None, end_date=None):
        tmp_update_df = super(KengKouMei_DongSheng, self).download_wind_quote(start_date=start_date, end_date=end_date)
        if tmp_update_df is not None:
            tmp_series = self.get_ts()
            if start_date is None:
                tmp_last = pd.DataFrame(tmp_series.iloc[-1:].copy())
                tmp_last.columns = tmp_update_df.columns
                tmp_update_df = pd.concat([tmp_last, tmp_update_df])
                tmp_update_df = tmp_update_df[~tmp_update_df.index.duplicated()]
            tmp_update_df = tmp_update_df.resample("B").bfill()
        return tmp_update_df
    
""" 计算指标 """ 

class LMeiZhiLiRun(upstream_base, Computed):
    field_name = u"煤制"
    col_name = u"L煤制利润"
    def get_ts_whole_progress(self):
        relevant_col_list = [u"LLD膜价格_华东(煤化工)", u"坑口煤价格_东胜"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[u"坑口煤价格_东胜"] = tmp_total[u"坑口煤价格_东胜"].fillna(method="ffill")
        tmp_total[self.col_name] = tmp_total[u"LLD膜价格_华东(煤化工)"] - 260 - tmp_total[u"坑口煤价格_东胜"] * 7.41 - 4780.57
        return tmp_total

###########################################################################################################################    
""" MTO """ 
class NeiMengJiaChunJiaGe(upstream_base, WindData):
    field_name = u"MTO"
    col_name = u"甲醇价格_内蒙"
    wind_code = "S5418767"

class JiangSuJiaChunJiaGe(upstream_base, WindData):
    field_name = u"MTO"
    col_name = u"甲醇价格_江苏"
    wind_code = "S5418787"

class JiaChun_CFRZhongGuo(upstream_base, WindData):
    field_name = u"MTO"
    col_name = u"甲醇:CFR价格_中国"
    wind_code = "S5416976"
    
""" 计算指标 """ 

class XiBeiLWaiGouJiaChunZhiLiRun(upstream_base, Computed):
    field_name = u"MTO"
    col_name = u"L外购甲醇制利润_西北"
    axhline = 0
    start_year = 2016
    def get_ts_whole_progress(self):
        relevant_col_list = [u"LLD膜价格_华东(煤化工)", u"甲醇价格_内蒙"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"LLD膜价格_华东(煤化工)"] - 260 - tmp_total[u"甲醇价格_内蒙"] * 2.8 - 1100
        return tmp_total    
    
###########################################################################################################################
""" 利润 """
""" 计算指标 """         
class LJinKouLiRun(upstream_base, Computed):
    field_name = u"利润"
    col_name = u"L进口利润"
    axhline = 0    
    def get_ts_whole_progress(self):
        relevant_col_list = [u"LLD价格_华东进口", u"LLDPE:CFR价格_远东", u"汇卖价(中行):美元兑人民币", u"增值税"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"LLD价格_华东进口"] - tmp_total[u"LLDPE:CFR价格_远东"] * tmp_total[u"汇卖价(中行):美元兑人民币"] \
                                    * 1.065 * (1 + tmp_total[u"增值税"]) - 100
        return tmp_total
    
class LChuKouLiRun(upstream_base, Computed):
    field_name = u"利润"
    col_name = u"L出口利润"
    axhline = 0 
    start_year = 2015
    def get_ts_whole_progress(self):
        relevant_col_list = [u"LLDPE:CFR价格_远东", u"L出口美金价格"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"LLDPE:CFR价格_远东"] - tmp_total[u"L出口美金价格"]
        return tmp_total

class LZhuanYunJiaCha(upstream_base, Computed):
    field_name = u"利润"
    col_name = u"L转运价差"
    axhline = 0
    start_year = 2015
    fig_title = u"L转运价差_中国至东南亚"    
    def get_ts_whole_progress(self):
        relevant_col_list = [u"LLDPE:CFR价格_东南亚", u"LLDPE:CFR价格_中国"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"LLDPE:CFR价格_东南亚"] - tmp_total[u"LLDPE:CFR价格_中国"]
        return tmp_total
    
if __name__ == "__main__":
#    aaa = vars()["field"]
#    print a.__name__
    aaa = KengKouMei_DongSheng().get_ts()
#    df = aaa.generate_wind_quote()
    
#    ts = KengKouMei_DongSheng().download_wind_quote()
    
#    fig_tuple = PPYouZhiLiRun().seasonal_plot()
#    LPP_Plot.add_month_span(fig_tuple[2], fig_tuple[0], 5)
    
#    a = spot_price_base.get_all_manual_class()
#    b = [x.col_name for x in a.values()]
#    c = [x.field_name for x in a.values()]
#    d = pd.DataFrame([b, c], index=["col", "field"]).T
#    f = d.sort_values(by=["field", "col"])
#    e = pd.DataFrame([], columns=f["col"].values.tolist())
#    e.to_excel(data_path + "update.xlsx", encoding="gbk")