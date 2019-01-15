# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 16:35:12 2018

@author: 李弘一萌
"""

import pandas as pd
from datetime import datetime
from .BU_Base import BU_Base
from ...Base.DataType_Base import Manual, Computed, WindData
from ...Base.Plot_Base import Plot_Base
from ....Futures_Data.Quote.QuoteData import QuoteData
from matplotlib.ticker import FuncFormatter

class spot_price_base(BU_Base, Plot_Base):
    table_english_name = "SpotPrice"
    table_chinese_name = u"现货价格"
#    original_db_filepath = data_path + u"LPP价格数据库.xlsx"
    
    def output(self):
        print("SpotPrice")
    
    def get_relevant_df(self, col_list):
        local_col_name_list = spot_price_base.get_all_table_classname()
        col_cls_list = []
        for x in col_list:
            col_cls_name = str(BU_Base.get_class_name(x))
            if col_cls_name not in local_col_name_list:
                col_cls_list.append(eval(BU_Base.get_table_class_full_variable(x)))
            else:
                col_cls_list.append(eval(col_cls_name))
        ts_list = [x().get_ts() for x in col_cls_list]
        tmp_table_df = pd.concat(ts_list, axis=1).dropna(how="all")
        return tmp_table_df  

    
###########################################################################################################################
""" 国内现货价格 """    

class LiQingXianHuoJiaGe_HuaNan(spot_price_base, Manual):
    field_name = u"国内现货价格"
    col_name = u"沥青现货价格_华南"

class LiQingXianHuoJiaGe_HuaDong(spot_price_base, Manual):
    field_name = u"国内现货价格"
    col_name = u"沥青现货价格_华东"

class LiQingXianHuoJiaGe_ShanDong(spot_price_base, Manual):
    field_name = u"国内现货价格"
    col_name = u"沥青现货价格_山东"
    
class GuoChanZhongJiaoJiaGe_XiBei(spot_price_base, Manual):
    field_name = u"国内现货价格"
    col_name = u"国产重交价格_西北"

class GuoChanZhongJiaoJiaGe_DongBei(spot_price_base, Manual):
    field_name = u"国内现货价格"
    col_name = u"国产重交价格_东北"
 
class GuoChanZhongJiaoJiaGe_HuaBei(spot_price_base, Manual):
    field_name = u"国内现货价格"
    col_name = u"国产重交价格_华北"
 
class GuoChanZhongJiaoJiaGe_XiNan(spot_price_base, Manual):
    field_name = u"国内现货价格"
    col_name = u"国产重交价格_西南"
 
class JianZhuLiQingJiaGe_ShanDong(spot_price_base, Manual):
    field_name = u"国内现货价格"
    col_name = u"建筑沥青价格_山东"
 
class PuTongLiQingJiaGe_BeiFang(spot_price_base, Manual):
    field_name = u"国内现货价格"
    col_name = u"普通沥青价格_北方"
 
class GaiXingLiQingJiaGe_HuaNan(spot_price_base, Manual):
    field_name = u"国内现货价格"
    col_name = u"改性沥青价格_华南"
 
class GaiXingLiQingJiaGe_HuaDong(spot_price_base, Manual):
    field_name = u"国内现货价格"
    col_name = u"改性沥青价格_华东"
 
class GaiXingLiQingJiaGe_BeiFang(spot_price_base, Manual):
    field_name = u"国内现货价格"
    col_name = u"改性沥青价格_北方"

class JiaoHuaLiaoJiaGe_ShanDong(spot_price_base, Manual):
    field_name = u"国内现货价格"
    col_name = u"焦化料价格_山东"

class LiQingXianHuoJiaGe_ZhongHai(spot_price_base, WindData):
    field_name = u"国内现货价格"
    col_name = u"沥青现货价格_中海"
    wind_code = "S5121312"
    
    
###########################################################################################################################
""" 美金价 """      

class LiQingXianHuoJiaGe_FOB_XinJiaPo(spot_price_base, Manual):
    field_name = u"美金价"
    col_name = u"沥青现货价格_FOB_新加坡"

class LiQingXianHuoJiaGe_CIF_XinJiaPo_HuaNan(spot_price_base, Manual):
    field_name = u"美金价"
    col_name = u"沥青现货价格_CIF_新加坡_华南"

class LiQingXianHuoJiaGe_CIF_XinJiaPo_HuaDong(spot_price_base, Manual):
    field_name = u"美金价"
    col_name = u"沥青现货价格_CIF_新加坡_华东"

class LiQingXianHuoJiaGe_CIF_HanGuo_HuaNan(spot_price_base, Manual):
    field_name = u"美金价"
    col_name = u"沥青现货价格_CIF_韩国_华南"

class LiQingXianHuoJiaGe_CIF_HanGuo_HuaDong(spot_price_base, Manual):
    field_name = u"美金价"
    col_name = u"沥青现货价格_CIF_韩国_华东"

class LiQingXianHuoJiaGe_CIF_TaiGuo_HuaNan(spot_price_base, Manual):
    field_name = u"美金价"
    col_name = u"沥青现货价格_CIF_泰国_华南"
    
class LiQingXianHuoJiaGe_FOB_HanGuo(spot_price_base, WindData):
    field_name = u"美金价"
    col_name = u"沥青现货价格_FOB_韩国"    
    wind_code = "S5437893"
        
class XinJiaPoRanLiaoYou180CSTXianHuoJiaGe(spot_price_base, WindData):
    field_name = u"美金价"
    col_name = u"新加坡燃料油180CST现货价格"
    wind_code = "S5111910"
    
class XinJiaPoRanLiaoYou380CSTXianHuoJiaGe(spot_price_base, WindData):
    field_name = u"美金价"
    col_name = u"新加坡燃料油380CST现货价格"
    wind_code = "S5111911"    
    
class HanGuoRanLiaoYou180CSTXianHuoJiaGe(spot_price_base, WindData):
    field_name = u"美金价"
    col_name = u"韩国燃料油180CST现货价格"
    wind_code = "S5121376"    
    
###########################################################################################################################
""" 出厂价 """   
    
class YeHuaQiChuChangJia_JingBoShiHua(spot_price_base, WindData):
    field_name = u"出厂价"
    col_name = u"液化气出厂价_京博石化"
    wind_code = "S5121886"  
    
class ShiYouJiao_No2A_ChuChangJia_BinYangRanHua(spot_price_base, WindData):
    field_name = u"出厂价"
    col_name = u"石油焦_2#A_出厂价_滨阳燃化"
    wind_code = "S5123243"      
    
class LaYou_No2_ChuChangJia_ZhongHaiBinZhou(spot_price_base, WindData):
    field_name = u"出厂价"
    col_name = u"蜡油_2#_出厂价_中海滨州"
    wind_code = "S5121257"      
    
    
    
    
    
    
    
    



if __name__ == "__main__":
    spot_list = [LiQingXianHuoJiaGe_HuaNan(), LiQingXianHuoJiaGe_HuaDong(), LiQingXianHuoJiaGe_ShanDong(), 
                 GuoChanZhongJiaoJiaGe_XiBei(), GuoChanZhongJiaoJiaGe_DongBei(), GuoChanZhongJiaoJiaGe_HuaBei(),
                 GuoChanZhongJiaoJiaGe_XiNan(), JianZhuLiQingJiaGe_ShanDong(), PuTongLiQingJiaGe_BeiFang(),
                 GaiXingLiQingJiaGe_HuaNan(), GaiXingLiQingJiaGe_HuaDong(), GaiXingLiQingJiaGe_BeiFang(),
                 LiQingXianHuoJiaGe_ZhongHai()]
    df_list = []
    for x in spot_list:
        ts = x.get_ts()
        df_list.append(ts)
    df = pd.concat(df_list, axis=1, sort=False)
    df.to_excel("沥青国内现货价格.xlsx", encoding="gbk")
        
        
        
        
        
        
        