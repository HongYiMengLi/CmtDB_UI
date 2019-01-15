# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 10:48:24 2018

@author: 李弘一萌
"""

import pandas as pd
from datetime import datetime
from .CU_Base import CU_Base
from . import CU_SpotPrice, CU_FuturesPrice, CU_Downstream, CU_Macro, CU_Others, CU_Upstream
from ...Base.Spread_Generate import main_month_quote_2_spread_series
from ...Base.DataType_Base import Manual, Computed, WindData
from ...Base.Plot_Base import Plot_Base
from matplotlib.ticker import FuncFormatter

class spread_base(CU_Base, Plot_Base):
    table_english_name = "Spread"
    table_chinese_name = u"价差与比价"
#    original_db_filepath = data_path + u"LPP价格数据库.xlsx"
    
    def output(self):
        print("Spread")
    
    def get_relevant_df(self, col_list):
        local_col_name_list = spread_base.get_all_table_classname()
        col_cls_list = []
        for x in col_list:
            col_cls_name = str(CU_Base.get_class_name(x))
            if col_cls_name not in local_col_name_list:
                col_cls_list.append(eval(CU_Base.get_table_class_full_variable(x)))
            else:
                col_cls_list.append(eval(col_cls_name))
        ts_list = [x().get_ts() for x in col_cls_list]
        tmp_table_df = pd.concat(ts_list, axis=1).dropna(how="all")
        return tmp_table_df 
    
###########################################################################################################################
""" LME升贴水 """    

class LMETongShengTieShui_0To3(spread_base, WindData):
    field_name = u"LME升贴水"
    col_name = u"LME铜升贴水(0-3)"
    wind_code = "S5806058"
    start_year = 2014
    axhline = 0
    
class LMETongShengTieShui_3To15(spread_base, WindData):
    field_name = u"LME升贴水"
    col_name = u"LME铜升贴水(3-15)"
    wind_code = "S5808597"  
    start_year = 2014
    axhline = 0
    

###########################################################################################################################
""" 国内现货铜升贴水 """    

class TongShengTieShui_ZuiXiaoZhi_ChangJiangYouSeShiChang(spread_base, WindData):
    field_name = u"国内现货铜升贴水"
    col_name = u"铜升贴水_最小值_长江有色市场"
    wind_code = "S5806281"
    axhline = 0
    
class TongShengTieShui_ZuiDaZhi_ChangJiangYouSeShiChang(spread_base, WindData):
    field_name = u"国内现货铜升贴水"
    col_name = u"铜升贴水_最大值_长江有色市场"
    wind_code = "S5806282"    
    axhline = 0

class No1DianJieTongShengTieShui_ZuiXiaoZhi_ShangHaiYouSe(spread_base, WindData):
    field_name = u"国内现货铜升贴水"
    col_name = u"1#电解铜升贴水_最小值_上海有色"
    wind_code = "S5806283"
    axhline = 0
    
class No1DianJieTongShengTieShui_ZuiXiaoZhi_ShangHaiJinShu(spread_base, WindData):
    field_name = u"国内现货铜升贴水"
    col_name = u"1#铜升贴水_最小值_上海金属"
    wind_code = "S0203259"
    start_year = 2014
    axhline = 0
    
class No1DianJieTongShengTieShui_ZuiDaZhi_ShangHaiYouSe(spread_base, WindData):
    field_name = u"国内现货铜升贴水"
    col_name = u"1#电解铜升贴水_最大值_上海有色"
    wind_code = "S5806284"   
    axhline = 0

class ShangHaiDianJieTongZuiDiYiJia_CIF_TiDan(spread_base, WindData):
    field_name = u"国内现货铜升贴水"
    col_name = u"上海电解铜最低溢价_CIF(提单)"
    wind_code = "S5807320"
    axhline = 0
    
class ShangHaiDianJieTongZuiGaoYiJia_CIF_TiDan(spread_base, WindData):
    field_name = u"国内现货铜升贴水"
    col_name = u"上海电解铜最高溢价_CIF(提单)"
    wind_code = "S5807321"  
    axhline = 0
    

###########################################################################################################################
""" 基差 """  
    
class JingTongXianHuoMinusQiHuoShouPanJia_LianSan(spread_base, Computed):
    field_name = u"基差"
    col_name = u"精铜现货-期货收盘价(连三)"
    axhline = 0
    def get_ts_whole_progress(self):
        relevant_col_list = [u"精铜价格_最高价_铜_长江有色市场", u"精铜价格_最低价_铜_长江有色市场", u"期货收盘价(连三)_阴极铜"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = (tmp_total[u"精铜价格_最高价_铜_长江有色市场"] + tmp_total[u"精铜价格_最低价_铜_长江有色市场"]) / 2 \
                                   - tmp_total[u"期货收盘价(连三)_阴极铜"]
        return tmp_total    


###########################################################################################################################
""" 精废铜价差 """  
    
class JingFeiTongJiaChaJunJia(spread_base, Computed):
    field_name = u"精废铜价差"
    col_name = u"精废铜价差均价"
    axhline = 0
    def get_ts_whole_progress(self):
        relevant_col_list = [u"精铜价格_最高价_铜_长江有色市场", u"精铜价格_最低价_铜_长江有色市场", u"废铜价格_1#光亮铜线_佛山"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = (tmp_total[u"精铜价格_最高价_铜_长江有色市场"] + tmp_total[u"精铜价格_最低价_铜_长江有色市场"]) / 2 \
                                   - tmp_total[u"废铜价格_1#光亮铜线_佛山"]
        return tmp_total    

    
###########################################################################################################################
""" 比价 """ 


class HuLunXianHuoBiZhi(spread_base, Computed):
    field_name = u"比价"
    col_name = u"沪伦现货比值"
    axhline = 0
    def get_ts_whole_progress(self):
        relevant_col_list = [u"精铜价格_最高价_铜_长江有色市场", u"期货收盘价_LME3个月铜", u"LME铜升贴水(0-3)"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"精铜价格_最高价_铜_长江有色市场"] / (tmp_total[u"期货收盘价_LME3个月铜"] + \
                                   tmp_total[u"LME铜升贴水(0-3)"])
        return tmp_total
    
class HuLunSanYueQiBiZhi(spread_base, Computed):
    field_name = u"比价"
    col_name = u"沪伦三月期比值"
    axhline = 0
    def get_ts_whole_progress(self):
        relevant_col_list = [u"期货收盘价(连三)_阴极铜", u"15点LME3个月铜(电子盘)价格"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"期货收盘价(连三)_阴极铜"] / tmp_total[u"15点LME3个月铜(电子盘)价格"]
        return tmp_total


###########################################################################################################################
""" 精铜进口利润 """  

class JingTongJinKouChengBen(spread_base, Computed):
    field_name = u"精铜进口利润"
    col_name = u"精铜进口成本"    
    def get_ts_whole_progress(self):
        relevant_col_list = ["15点LME3个月铜(电子盘)价格", "上海电解铜最低溢价_CIF(提单)", "即期汇率_美元兑人民币", "LME铜升贴水(0-3)", "增值税"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = (tmp_total[u"15点LME3个月铜(电子盘)价格"] + tmp_total[u"LME铜升贴水(0-3)"] + tmp_total[u"上海电解铜最低溢价_CIF(提单)"]) \
                                   * tmp_total[u"即期汇率_美元兑人民币"] * (1 + tmp_total["增值税"]) + 150
        return tmp_total 
    
class JingTongJinKouLiRun(spread_base, Computed):
    field_name = u"精铜进口利润"
    col_name = u"精铜进口利润"    
    def get_ts_whole_progress(self):
        relevant_col_list = [u"精铜价格_最低价_铜_长江有色市场", "精铜进口成本"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"精铜价格_最低价_铜_长江有色市场"] - tmp_total[u"精铜进口成本"]
        return tmp_total   
        
    
class SanYueQiTongJinKouLiRun(spread_base, Computed):
    field_name = u"精铜进口利润"
    col_name = u"三月期铜进口利润"    
    def get_ts_whole_progress(self):
        relevant_col_list = [u"期货收盘价(连三)_阴极铜", u"15点LME3个月铜(电子盘)价格", u"上海电解铜最低溢价_CIF(提单)", "增值税", "USDCNY_NDF_3个月"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"期货收盘价(连三)_阴极铜"] - ((tmp_total[u"15点LME3个月铜(电子盘)价格"] + \
                                   tmp_total[u"上海电解铜最低溢价_CIF(提单)"]) * tmp_total[u"USDCNY_NDF_3个月"] * (1 + tmp_total["增值税"]) + 150)
        return tmp_total 








if __name__ == "__main__":
    df = JingTongJinKouLiRun().get_ts()
#    df, fig, axis = No1DianJieTongShengTieShui_ZuiXiaoZhi_ShangHaiJinShu().seasonal_plot()
    
    
    
    
    
    
    
    
    
    
    
    
    
    