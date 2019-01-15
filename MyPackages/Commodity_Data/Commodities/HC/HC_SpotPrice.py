# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 16:35:12 2018

@author: 李弘一萌
"""

import pandas as pd
from datetime import datetime
from .HC_Base import HC_Base
from ...Base.DataType_Base import Manual, Computed, WindData
from ...Base.Plot_Base import Plot_Base
from matplotlib.ticker import FuncFormatter

class spot_price_base(HC_Base, Plot_Base):
    table_english_name = "SpotPrice"
    table_chinese_name = u"现货价格"
#    original_db_filepath = data_path + u"LPP价格数据库.xlsx"
    
    def output(self):
        print("SpotPrice")
    
    def get_relevant_df(self, col_list):
        local_col_name_list = spot_price_base.get_all_table_classname()
        col_cls_list = []
        for x in col_list:
            col_cls_name = str(HC_Base.get_class_name(x))
            if col_cls_name not in local_col_name_list:
                col_cls_list.append(eval(HC_Base.get_table_class_full_variable(x)))
            else:
                col_cls_list.append(eval(col_cls_name))
        ts_list = [x().get_ts() for x in col_cls_list]
        tmp_table_df = pd.concat(ts_list, axis=1).dropna(how="all")
        return tmp_table_df  
    
###########################################################################################################################
""" 出口现货报价 """    

class ReJuanChuKouFOBBaoJia_Q235B_5Dot5_1500_ShangHaiGang(spot_price_base, Manual):
    field_name = u"出口现货报价"
    col_name = u"热卷出口FOB报价_Q235B_5.5*1500_上海港"

class ReJuanChuKouFOBBaoJia_Q235B_5Dot5_1500_TianJinGang(spot_price_base, Manual):
    field_name = u"出口现货报价"
    col_name = u"热卷出口FOB报价_Q235B_5.5*1500_天津港"
    

###########################################################################################################################
""" 现货市场价格 """    

    
class ReJuanXianHuoJiaGe_Q235B_4Dot75mm_QuanGuo(spot_price_base, WindData):
    field_name = u"现货市场价格"
    col_name = u"热卷现货价格_Q235B_4.75mm_全国"
    wind_code = "S5707804"        
    
class ReJuanXianHuoJiaGe_Q235B_4Dot75mm_TianJin(spot_price_base, WindData):
    field_name = u"现货市场价格"
    col_name = u"热卷现货价格_Q235B_4.75mm_天津"
    wind_code = "S0073209"       
    
class ReJuanXianHuoJiaGe_Q235B_4Dot75mm_GuangZhou(spot_price_base, WindData):
    field_name = u"现货市场价格"
    col_name = u"热卷现货价格_Q235B_4.75mm_广州"
    wind_code = "S0033263"       
    
class ReJuanXianHuoJiaGe_Q235B_4Dot75mm_ShangHai(spot_price_base, WindData):
    field_name = u"现货市场价格"
    col_name = u"热卷现货价格_Q235B_4.75mm_上海"
    wind_code = "S0033272"       
    
class ReJuanXianHuoJiaGe_Q235B_4Dot75mm_HangZhou(spot_price_base, WindData):
    field_name = u"现货市场价格"
    col_name = u"热卷现货价格_Q235B_4.75mm_杭州"
    wind_code = "S5704863"       
    
class ReJuanXianHuoJiaGe_Q235B_4Dot75mm_NanJing(spot_price_base, WindData):
    field_name = u"现货市场价格"
    col_name = u"热卷现货价格_Q235B_4.75mm_南京"
    wind_code = "S5704864"      
    
class ReJuanXianHuoJiaGe_Q235B_4Dot75mm_WuHan(spot_price_base, WindData):
    field_name = u"现货市场价格"
    col_name = u"热卷现货价格_Q235B_4.75mm_武汉"
    wind_code = "S0033277"      
    
class LengJuanXianHuoJiaGe_1Dot0mm_ShangHai(spot_price_base, WindData):
    field_name = u"现货市场价格"
    col_name = u"冷卷现货价格_1.0mm_上海"
    wind_code = "S0033155"  
    
class LengJuanXianHuoJiaGe_1Dot0mm_TianJin(spot_price_base, WindData):
    field_name = u"现货市场价格"
    col_name = u"冷卷现货价格_1.0mm_天津"
    wind_code = "S0073204"  
    
class LengJuanXianHuoJiaGe_1Dot0mm_GuangZhou(spot_price_base, WindData):
    field_name = u"现货市场价格"
    col_name = u"冷卷现货价格_1.0mm_广州"
    wind_code = "S0033145"      
    
class DuXinBanJuanXianHuoJiaGe_0Dot5mm_ShangHai(spot_price_base, WindData):
    field_name = u"现货市场价格"
    col_name = u"镀锌板卷现货价格_0.5mm_上海"
    wind_code = "S5704810"      
    
    
    
    
    
    
    
if __name__ == "__main__":
    ts = PHCXianHuoJiaGe_HuaDong().get_ts()