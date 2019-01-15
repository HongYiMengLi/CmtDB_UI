# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 16:35:12 2018

@author: 李弘一萌
"""

import pandas as pd
from datetime import datetime
from .J_Base import J_Base
from ...Base.DataType_Base import Manual, Computed, WindData
from ...Base.Plot_Base import Plot_Base
from matplotlib.ticker import FuncFormatter

class spot_price_base(J_Base, Plot_Base):
    table_english_name = "SpotPrice"
    table_chinese_name = u"现货价格"
#    original_db_filepath = data_path + u"LPP价格数据库.xlsx"
    
    def output(self):
        print("SpotPrice")
    
    def get_relevant_df(self, col_list):
        local_col_name_list = spot_price_base.get_all_table_classname()
        col_cls_list = []
        for x in col_list:
            col_cls_name = str(J_Base.get_class_name(x))
            if col_cls_name not in local_col_name_list:
                col_cls_list.append(eval(J_Base.get_table_class_full_variable(x)))
            else:
                col_cls_list.append(eval(col_cls_name))
        ts_list = [x().get_ts() for x in col_cls_list]
        tmp_table_df = pd.concat(ts_list, axis=1).dropna(how="all")
        return tmp_table_df  
    
###########################################################################################################################
""" 焦炭价格 """    

class YiJiYeJinJiaoShiChangJia_ALT12Dot5Prct_SLT0Dot7Prct_MtLT8Prct_M25GT90Prct_CSRGT58Prct_TangShanChan_HeBei(spot_price_base, WindData):
    field_name = u"焦炭价格"
    col_name = u"一级冶金焦市场价_A<12.5%_S<0.7%_Mt<8%_M25>90%_CSR>58%_唐山产_河北"
    wind_code = "S5120124"

class YiJiYeJinJiaoShiChangJia_ALT12Dot5Prct_SLT0Dot65Prct_MtLT8Prct_M25GT90Prct_CSRGT60Prct_XingTaiChan_HeBei(spot_price_base, WindData):
    field_name = u"焦炭价格"
    col_name = u"一级冶金焦市场价_A<12.5%_S<0.65%_Mt<8%_M25>90%_CSR>60%_邢台产_河北"
    wind_code = "S5120125"

class YiJiYeJinJiaoCheBanJia_ALT12Dot5Prct_SLT0Dot7Prct_MtLT8Prct_M25GT90Prct_CSRGT60Prct_TaiYuanChan_ShanXi(spot_price_base, WindData):
    field_name = u"焦炭价格"
    col_name = u"一级冶金焦车板价_A<12.5%_S<0.7%_Mt<8%_M25>90%_CSR>60%_太原产_山西"
    wind_code = "S5120128"

class YiJiYeJinJiaoCheBanJia_ALT12Dot5Prct_SLT0Dot7Prct_MtLT7Prct_M25GT90Prct_CSRGT60Prct_LinFenChan_ShanXi(spot_price_base, WindData):
    field_name = u"焦炭价格"
    col_name = u"一级冶金焦车板价_A<12.5%_S<0.7%_Mt<7%_M25>90%_CSR>60%_临汾产_山西"
    wind_code = "S5120126"

class ErJiYeJinJiaoCheBanJia_ALT13Dot5Prct_SLT0Dot8Prct_MtLT8Prct_M40GT82Prct_CSRGT60Prct_WuHaiChan_NeiMengGu(spot_price_base, WindData):
    field_name = u"焦炭价格"
    col_name = u"二级冶金焦车板价_A<13.5%_S<0.8%_Mt<8%_M40>82%_CSR>60%_乌海产_内蒙古"
    wind_code = "S5120142"

class ZhunYiJiYeJinJiaoChuChangJia_HanShui_LvLiang(spot_price_base, WindData):
    field_name = u"焦炭价格"
    col_name = u"准一级冶金焦出厂价(含税)_吕梁"
    wind_code = "S5118257"

class ZhunYiJiYeJinJiaoChuChangJia_HanShui_XingTai(spot_price_base, WindData):
    field_name = u"焦炭价格"
    col_name = u"准一级冶金焦出厂价(含税)_邢台"
    wind_code = "S5118274"

class ZhunYiJiYeJinJiaoChuChangJia_HanShui_FuShun(spot_price_base, WindData):
    field_name = u"焦炭价格"
    col_name = u"准一级冶金焦出厂价(含税)_抚顺"
    wind_code = "S5118244"
    
class ErJiYeJinJiaoShiChangJia_ALT13Dot0Prct_SLT0Dot8Prct_MtLT8Prct_M25GT90Prct_CSRGT52Prct_XuZhouChan_JiangSu(spot_price_base, WindData):
    field_name = u"焦炭价格"
    col_name = u"二级冶金焦市场价_A<13.0%_S<0.8%_Mt<8%_M25>90%_CSR>52%_徐州产_江苏"
    wind_code = "S5120136"

class ErJiYeJinJiaoShiChangJia_ALT13Dot5Prct_SLT0Dot75Prct_MtLT10Prct_M25GT90Prct_CSRGT55Prct_LinFenChan_ShanXi(spot_price_base, WindData):
    field_name = u"焦炭价格"
    col_name = u"二级冶金焦市场价_A<13.5%_S<0.75%_Mt<10%_M25>90%_CSR>55%_临汾产_山西"
    wind_code = "S5120138"

class ErJiYeJinJiaoShiChangJia_ALT13Dot0Prct_SLT0Dot7Prct_MtLT8Prct_M25GT88Prct_CSR52To55Prct_TangShanChan_HeBei(spot_price_base, WindData):
    field_name = u"焦炭价格"
    col_name = u"二级冶金焦市场价_A<13.0%_S<0.7%_Mt<8%_M25>88%_CSR52-55%_唐山产_河北"
    wind_code = "S5120141"

class ErJiYeJinJiaoDaoChangJia_ErJiYeJinJiao_HanShui_A13Dot5Prct_S0Dot7Prct_TangShan(spot_price_base, WindData):
    field_name = u"焦炭价格"
    col_name = u"二级冶金焦到厂价_二级冶金焦(含税)_A13.5%_S0.7%_唐山"
    wind_code = "S0033507"

class YiJiYeJinJiaoCheBanJia_ALT12Dot5Prct_SLT0Dot7Prct_MtLT7Prct_M25GT90Prct_CSRGT60Prct_LvLiangChan_ShanXi(spot_price_base, WindData):
    field_name = u"焦炭价格"
    col_name = u"一级冶金焦车板价_A<12.5%,S<0.7%,Mt<7%,M25>90%,CSR>60%_吕梁产_山西"
    wind_code = "S5132227"
    
###########################################################################################################################
""" 港口价格 """    

class YiJiYeJinJiaoPingCangJia_RiZhao(spot_price_base, Manual):
    field_name = u"港口价格"
    col_name = u"一级冶金焦平仓价_日照"

class ZhunYiJiYeJinJiaoPingCangJia_RiZhao(spot_price_base, Manual):
    field_name = u"港口价格"
    col_name = u"准一级冶金焦平仓价_日照"


class ErJiYeJinJiaoXianHuoJia_XiaoLiDu10To30_TianJinGang(spot_price_base, WindData):
    field_name = u"港口价格"
    col_name = u"二级冶金焦现货价_小粒度10-30_天津港"
    wind_code = "S5118191"   
     
class ErJiYeJinJiaoXianHuoJia_ChangGuiLiDu25To90_TianJinGang(spot_price_base, WindData):
    field_name = u"港口价格"
    col_name = u"二级冶金焦现货价_常规粒度25-90_天津港"
    wind_code = "S5118190" 
    
    
###########################################################################################################################
""" 副产品价格 """    

class MeiJiaoYouShiChangJia_HuiFen0Dot13Prct_ZhanDu4Dot0_ShuiFen4Dot0Prct_LvLiangChan_ShanXi(spot_price_base, WindData):
    field_name = u"副产品价格"
    col_name = u"煤焦油市场价_灰分0.13%_粘度4.0_水分4.0%_吕梁产_山西"
    wind_code = "S5449164"

class LiuSuanAnShiChangJia_NGT21Prct_ShuiFenLT1Prct_LvLiangChan_ShanXi(spot_price_base, WindData):
    field_name = u"副产品价格"
    col_name = u"硫酸铵市场价_N>21%_水分<1%_吕梁产_山西"
    wind_code = "S5449112"

class CuBenShiChangJia_MiDu0Dot87To0Dot90_LiuChuLiangGT93Prct_LvLiangChan_ShanXi(spot_price_base, WindData):
    field_name = u"副产品价格"
    col_name = u"粗苯市场价_密度0.87-0.90_馏出量>93%_吕梁产_山西"
    wind_code = "S5449209"     
    

if __name__ == "__main__":
    ts = PJXianHuoJiaGe_HuaDong().get_ts()