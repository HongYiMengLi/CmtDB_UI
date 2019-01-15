# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 10:48:24 2018

@author: 李弘一萌
"""

import pandas as pd
from datetime import datetime
from .AL_Base import AL_Base
from . import AL_SpotPrice, AL_FuturesPrice, AL_Downstream, AL_Macro, AL_Others, AL_Upstream
from ...Base.Spread_Generate import main_month_quote_2_spread_series
from ...Base.DataType_Base import Manual, Computed, WindData
from ...Base.Plot_Base import Plot_Base
from matplotlib.ticker import FuncFormatter

class spread_base(AL_Base, Plot_Base):
    table_english_name = "Spread"
    table_chinese_name = u"价差与比价"
#    original_db_filepath = data_path + u"LPP价格数据库.xlsx"
    
    def output(self):
        print("Spread")
    
    def get_relevant_df(self, col_list):
        local_col_name_list = spread_base.get_all_table_classname()
        col_cls_list = []
        for x in col_list:
            col_cls_name = str(AL_Base.get_class_name(x))
            if col_cls_name not in local_col_name_list:
                col_cls_list.append(eval(AL_Base.get_table_class_full_variable(x)))
            else:
                col_cls_list.append(eval(col_cls_name))
        ts_list = [x().get_ts() for x in col_cls_list]
        tmp_table_df = pd.concat(ts_list, axis=1).dropna(how="all")
        return tmp_table_df 
    
###########################################################################################################################
""" 升贴水 """    
class A00LvShengTieShui_ZuiXiaoZhi_ShangHaiJinShu(spread_base, WindData):
    field_name = u"升贴水"
    col_name = u"A00铝升贴水_最小值_上海金属"
    wind_code = "S0203261"
    start_year = 2014
    axhline = 0
    
class A00LvDingShengTieShui_ZuiXiaoZhi(spread_base, WindData):
    field_name = u"升贴水"
    col_name = u"A00铝锭升贴水_最小值"
    wind_code = "S5806285"
    axhline = 0
    
class A00LvDingShengTieShui_ZuiDaZhi(spread_base, WindData):
    field_name = u"升贴水"
    col_name = u"A00铝锭升贴水_最大值"
    wind_code = "S5806286"    
    axhline = 0
    
class LMELvShengTieShui_0To3(spread_base, WindData):
    field_name = u"升贴水"
    col_name = u"LME铝升贴水(0-3)"
    wind_code = "S5806059"   
    start_year = 2014
    axhline = 0
    
class ShangHaiDianJieLvZuiDiYiJia_CIF_TiDan(spread_base, WindData):
    field_name = u"国内现货铜升贴水"
    col_name = u"上海电解铝最低溢价_CIF(提单)"
    wind_code = "S5809438"
    
class ShangHaiDianJieLvZuiGaoYiJia_CIF_TiDan(spread_base, WindData):
    field_name = u"国内现货铜升贴水"
    col_name = u"上海电解铝最高溢价_CIF(提单)"
    wind_code = "S5809439"  


###########################################################################################################################
""" 氧化铝国内外价差 """  

class YangHuaLvGuoNeiWaiJiaCha(spread_base, Computed):
    field_name = u"氧化铝国内外价差"
    col_name = u"氧化铝国内外价差"
    axhline = 0
    def get_ts_whole_progress(self):
        relevant_col_list = [u"氧化铝出口平均单价_当月值(人民币计价)", u"氧化铝平均价_一级_山西"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"氧化铝出口平均单价_当月值(人民币计价)"] - tmp_total[u"氧化铝平均价_一级_山西"]
        return tmp_total    



###########################################################################################################################
""" 沪伦比价 """ 

class HuLunLvBiJia(spread_base, Computed):
    field_name = u"沪伦比价"
    col_name = u"沪伦铝比价"
    axhline = 0
    def get_ts_whole_progress(self):
        relevant_col_list = [u"期货收盘价(电子盘)_LME3个月铝", u"期货结算价(活跃合约)_铝"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] =  tmp_total[u"期货结算价(活跃合约)_铝"] / tmp_total[u"期货收盘价(电子盘)_LME3个月铝"]
        return tmp_total

    
###########################################################################################################################
""" 电解铝盘面利润 """  


class DianJieLvPanMianChengBen(spread_base, Computed):
    field_name = u"电解铝盘面利润"
    col_name = u"电解铝盘面成本"
    axhline = 0
    def get_ts_whole_progress(self):
        relevant_col_list = [u"氧化铝平均价", "预焙阳极(电解铝用辅料)市场价(含税)_西南地区", 
                             "预焙阳极(电解铝用辅料)市场价(含税)_西北地区", "干法氟化铝(电解铝用辅料)市场价(含税)", "冰晶石(电解铝用辅料)市场价(含税)"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"氧化铝平均价"] * 1.9  + \
                                   (tmp_total[u"预焙阳极(电解铝用辅料)市场价(含税)_西南地区"] + tmp_total[u"预焙阳极(电解铝用辅料)市场价(含税)_西北地区"]) / 2 \
                                   * 0.45 + tmp_total[u"干法氟化铝(电解铝用辅料)市场价(含税)"] * 0.025 + tmp_total[u"冰晶石(电解铝用辅料)市场价(含税)"] * 0.015 \
                                   + 6500
        return tmp_total  


class DianJieLvPanMianLiRun(spread_base, Computed):
    field_name = u"电解铝盘面利润"
    col_name = u"电解铝盘面利润"
    axhline = 0
    start_year = 2014
    def get_ts_whole_progress(self):
        relevant_col_list = [u"期货收盘价(活跃合约)_沪铝", u"电解铝盘面成本"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"期货收盘价(活跃合约)_沪铝"] - tmp_total[u"电解铝盘面成本"]
        return tmp_total  
    
###########################################################################################################################
""" 电解铝沪粤价差 """  

class HuYueLvJiaCha(spread_base, Computed):
    field_name = u"电解铝沪粤价差"
    col_name = u"沪粤铝价差"
    axhline = 0
    def get_ts_whole_progress(self):
        relevant_col_list = [u"国产A00铝(批售含票)价格_南海有色(灵通)_平均价_佛山", u"电解铝价格_长江有色市场_平均价_A00"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"国产A00铝(批售含票)价格_南海有色(灵通)_平均价_佛山"] - tmp_total[u"电解铝价格_长江有色市场_平均价_A00"]
        return tmp_total  
        
    
###########################################################################################################################
""" 电解铝进口利润 """  

class DianJieLvJinKouChengBen(spread_base, Computed):
    field_name = u"电解铝进口利润"
    col_name = u"电解铝进口成本"    
    def get_ts_whole_progress(self):
        relevant_col_list = [u"15点LME3个月铝(电子盘)价格", u"上海电解铝最低溢价_CIF(提单)",
                             u"即期汇率_美元兑人民币", u"LME铝升贴水(0-3)", "增值税"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = (tmp_total[u"15点LME3个月铝(电子盘)价格"] + tmp_total[u"LME铝升贴水(0-3)"] + tmp_total[u"上海电解铝最低溢价_CIF(提单)"]) \
                                   * tmp_total[u"即期汇率_美元兑人民币"] * (1 + tmp_total[u"增值税"]) + 150
#        tmp_total[self.col_name] = tmp_total[u"15点LME3个月铝(电子盘)价格"] + tmp_total[u"LME铝升贴水(0-3)"] + tmp_total[u"上海电解铝最低溢价_CIF(提单)"]
        return tmp_total   
        
class DianJieLvJinKouLiRun(spread_base, Computed):
    field_name = u"电解铝进口利润"
    col_name = u"电解铝进口利润"    
    def get_ts_whole_progress(self):
        relevant_col_list = [u"电解铝价格_长江有色市场_平均价_A00", "电解铝进口成本"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"电解铝价格_长江有色市场_平均价_A00"] - tmp_total[u"电解铝进口成本"]
        return tmp_total   
    










if __name__ == "__main__":
    df = HuLunLvBiJia().get_ts()
#    df, fig, axis = DianJieLvPanMianLiRun().seasonal_plot()
    
    
    
    
    
    
    
    
    
    
    
    
    
    