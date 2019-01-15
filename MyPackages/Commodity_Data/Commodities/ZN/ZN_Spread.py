# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 10:48:24 2018

@author: 李弘一萌
"""

import pandas as pd
from datetime import datetime
from .ZN_Base import ZN_Base
from . import ZN_SpotPrice, ZN_FuturesPrice, ZN_Downstream, ZN_Macro
from ...Base.Spread_Generate import main_month_quote_2_spread_series
from ...Base.DataType_Base import Manual, Computed, WindData
from ...Base.Plot_Base import Plot_Base
from matplotlib.ticker import FuncFormatter

class spread_base(ZN_Base, Plot_Base):
    table_english_name = "Spread"
    table_chinese_name = u"价差与比价"
    
    def output(self):
        print("Spread")
    
    def get_relevant_df(self, col_list):
        local_col_name_list = spread_base.get_all_table_classname()
        col_cls_list = []
        for x in col_list:
            col_cls_name = str(ZN_Base.get_class_name(x))
            if col_cls_name not in local_col_name_list:
                col_cls_list.append(eval(ZN_Base.get_table_class_full_variable(x)))
            else:
                col_cls_list.append(eval(col_cls_name))
        ts_list = [x().get_ts() for x in col_cls_list]
        tmp_table_df = pd.concat(ts_list, axis=1).dropna(how="all")
        return tmp_table_df 
    
###########################################################################################################################
""" 升贴水 """    

class LMEXinShengTieShui_0To3(spread_base, WindData):
    field_name = u"升贴水"
    col_name = u"LME锌升贴水(0-3)"
    wind_code = "S5806060"
    start_year = 2014
    axhline = 0
    
class LMEXinShengTieShui_3To15(spread_base, WindData):
    field_name = u"升贴水"
    col_name = u"LME锌升贴水(3-15)"
    wind_code = "S5808600"  
    axhline = 0
    
class XinShengTieShui_ZuiXiaoZhi(spread_base, WindData):
    field_name = u"升贴水"
    col_name = u"锌升贴水_最小值"
    wind_code = "S5806287"  
    axhline = 0
    
class No0XinShengTieShui_ZuiXiaoZhi_ShangHaiJinShu(spread_base, WindData):
    field_name = u"升贴水"
    col_name = u"0#锌升贴水_最小值_上海金属"
    wind_code = "S0203265"
    start_year = 2014    
    axhline = 0
    

###########################################################################################################################
""" 进口溢价 """    

class ShangHaiDianJieXinZuiDiYiJia_CIF_TiDan(spread_base, WindData):
    field_name = u"进口溢价"
    col_name = u"上海电解锌最低溢价_CIF(提单)"
    wind_code = "S5809440"
    
class ShangHaiDianJieXinZuiGaoYiJia_CIF_TiDan(spread_base, WindData):
    field_name = u"进口溢价"
    col_name = u"上海电解锌最高溢价_CIF(提单)"
    wind_code = "S5809441"    
    
class ShangHaiDianJieXinZuiDiYiJia_BaoShuiKu_CangDan(spread_base, WindData):
    field_name = u"进口溢价"
    col_name = u"上海电解锌最低溢价_保税库(仓单)"
    wind_code = "S5809448"    
    
class ShangHaiDianJieXinZuiGaoYiJia_BaoShuiKu_CangDan(spread_base, WindData):
    field_name = u"进口溢价"
    col_name = u"上海电解锌最高溢价_保税库(仓单)"
    wind_code = "S5809449"    


###########################################################################################################################
""" 沪粤价差 """ 

class HuYueXinJiaCha(spread_base, Computed):
    field_name = u"沪粤价差"
    col_name = u"沪粤锌价差"
    axhline = 0
    def get_ts_whole_progress(self):
        relevant_col_list = [u"0#锌价格_长江有色市场_平均价", u"0#锌锭(国产)价格_广东南储_平均价_佛山仓库"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"0#锌价格_长江有色市场_平均价"] - tmp_total[u"0#锌锭(国产)价格_广东南储_平均价_佛山仓库"]
        return tmp_total
    
###########################################################################################################################
""" 比价 """ 

class HuLunXinXianHuoBiJia(spread_base, Computed):
    field_name = u"比价"
    col_name = u"沪伦锌现货比价"
    axhline = 0
    def get_ts_whole_progress(self):
        relevant_col_list = [u"0#锌价格_长江有色_最低价(含税)", u"15点LME3个月锌(电子盘)价格", u"LME锌升贴水(0-3)"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"0#锌价格_长江有色_最低价(含税)"] / (tmp_total[u"15点LME3个月锌(电子盘)价格"] + \
                                   tmp_total[u"LME锌升贴水(0-3)"])
        return tmp_total
    
class JinKouXinJunHengBiJia(spread_base, Computed):
    field_name = u"比价"
    col_name = u"进口锌均衡比价"
    axhline = 0
    def get_ts_whole_progress(self):
        relevant_col_list = [u"上海电解锌最低溢价_CIF(提单)", u"15点LME3个月锌(电子盘)价格", u"LME锌升贴水(0-3)"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = (tmp_total[u"15点LME3个月锌(电子盘)价格"] + tmp_total[u"LME锌升贴水(0-3)"] + tmp_total[u"上海电解锌最低溢价_CIF(提单)"]) \
                                   / (tmp_total[u"15点LME3个月锌(电子盘)价格"] + tmp_total[u"LME锌升贴水(0-3)"])
        return tmp_total

class HuLunXinZhuLiHeYueBiJia(spread_base, Computed):
    field_name = u"比价"
    col_name = u"沪伦锌主力合约比价"
    axhline = 0
    def get_ts_whole_progress(self):
        relevant_col_list = [u"锌期货收盘价(活跃合约)", u"期货收盘价(电子盘)_LME3个月锌"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"锌期货收盘价(活跃合约)"] / tmp_total[u"期货收盘价(电子盘)_LME3个月锌"]
        return tmp_total



###########################################################################################################################
""" 进口利润 """  

class XianHuoXinJinKouLiRun(spread_base, Computed):
    field_name = u"进口利润"
    col_name = u"现货锌进口利润"    
    def get_ts_whole_progress(self):
        relevant_col_list = [u"0#锌价格_长江有色_最低价(含税)", u"15点LME3个月锌(电子盘)价格", u"上海电解锌最低溢价_CIF(提单)",
                             u"即期汇率_美元兑人民币", u"LME锌升贴水(0-3)"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"0#锌价格_长江有色_最低价(含税)"] - (tmp_total[u"15点LME3个月锌(电子盘)价格"] + \
                                   tmp_total[u"LME锌升贴水(0-3)"] + tmp_total[u"上海电解锌最低溢价_CIF(提单)"]) * tmp_total[u"即期汇率_美元兑人民币"] \
                                   * 1.16 * 1.01 - 150
        return tmp_total   

    
class HuXinSanYueHeYueJinKouLiRu(spread_base, Computed):
    field_name = u"进口利润"
    col_name = u"沪锌三月合约进口利润"    
    def get_ts_whole_progress(self):
        relevant_col_list = [u"锌期货收盘价(连三)", u"15点LME3个月锌(电子盘)价格", u"上海电解锌最低溢价_CIF(提单)",
                             u"即期汇率_美元兑人民币", u"LME锌升贴水(0-3)"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"锌期货收盘价(连三)"] - (tmp_total[u"15点LME3个月锌(电子盘)价格"] + \
                                   tmp_total[u"上海电解锌最低溢价_CIF(提单)"]) * tmp_total[u"即期汇率_美元兑人民币"] * 1.16 * 1.01 - 150
        return tmp_total 









if __name__ == "__main__":
#    df = PZNSpread9_1().get_ts()
    df, fig, axis = LMEXinShengTieShui_0To3().seasonal_plot()
    
    
    
    
    
    
    
    
    
    
    
    
    
    