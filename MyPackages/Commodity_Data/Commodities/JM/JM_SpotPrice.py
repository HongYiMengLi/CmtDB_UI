# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 16:35:12 2018

@author: 李弘一萌
"""

import pandas as pd
from datetime import datetime
from .JM_Base import JM_Base
from ...Base.DataType_Base import Manual, Computed, WindData
from ...Base.Plot_Base import Plot_Base
from matplotlib.ticker import FuncFormatter

class spot_price_base(JM_Base, Plot_Base):
    table_english_name = "SpotPrice"
    table_chinese_name = u"现货价格"
#    original_db_filepath = data_path + u"LPP价格数据库.xlsx"
    
    def output(self):
        print("SpotPrice")
    
    def get_relevant_df(self, col_list):
        local_col_name_list = spot_price_base.get_all_table_classname()
        col_cls_list = []
        for x in col_list:
            col_cls_name = str(JM_Base.get_class_name(x))
            if col_cls_name not in local_col_name_list:
                col_cls_list.append(eval(JM_Base.get_table_class_full_variable(x)))
            else:
                col_cls_list.append(eval(col_cls_name))
        ts_list = [x().get_ts() for x in col_cls_list]
        tmp_table_df = pd.concat(ts_list, axis=1).dropna(how="all")
        return tmp_table_df  
    
###########################################################################################################################
""" 1/3焦煤 """    

class OneThirdJiaoMeiCheBanJia_ALT10Prct_V30To32Prct_SLT1Dot8Prct_GGT75Prct_Y16_LvLiangChan_ShanXi(spot_price_base, WindData):
    field_name = u"1/3焦煤"
    col_name = u"1/3焦煤车板价_A<10%_V30-32%_S<1.8%_G>75%_Y16_吕梁产_山西"
    wind_code = "S5120114"

class OneThirdJiaoMeiCheBanJia_A11Prct_S0Dot8PrctV33Prct_G89Prct_Y19_TangShanChan_HeBei(spot_price_base, WindData):
    field_name = u"1/3焦煤"
    col_name = u"1/3焦煤车板价_A11%_S0.8%V33%_G89%_Y19_唐山产_河北"
    wind_code = "S5120115"

class OneThirdJiaoMeiCheBanJia_ALT10Prct_V31To34Prct_SLT1Prct_GGT85Prct_Y18To22_LvLiangChan_ShanXi(spot_price_base, WindData):
    field_name = u"1/3焦煤"
    col_name = u"1/3焦煤车板价_A<10%_V:31-34%_S<1%_G>85%_Y18-22_吕梁产_山西"
    wind_code = "S5132033"
    
    
###########################################################################################################################
""" 肥煤 """ 

class FeiMeiCheBanJia_ALT10Prct_V24To28Prct_SLT1Dot3Prct_GGT85Prct_GuJiaoChan_ShanXi(spot_price_base, WindData):
    field_name = u"肥煤"
    col_name = u"肥煤车板价_A<10%_V24-28%_S<1.3%_G>85%_古交产_山西"
    wind_code = "S5120108"

class FeiMeiCheBanJia_ALT10Prct_V32To34Prct_SLT1Dot3Prct_GGT85Prct_HuoZhouChan_ShanXi(spot_price_base, WindData):
    field_name = u"肥煤"
    col_name = u"肥煤车板价_A<10%_V32-34%_S<1.3%_G>85%_霍州产_山西"
    wind_code = "S5120109"

class FeiMeiCheBanJia_ALT12Prct_VLT28Prct_SLT0Dot45Prct_YGT25_GGT90Prct_HanDanChan_HeBei(spot_price_base, WindData):
    field_name = u"肥煤"
    col_name = u"肥煤车板价_A<12%_V<28%_S<0.45%_Y>25_G>90%_邯郸产_河北"
    wind_code = "S5120110"

class FeiMeiCheBanJia_A9Dot5To10Prct_SLT0Dot6Prct_V26Prct_GGT95_TangShanChan_HeBei(spot_price_base, WindData):
    field_name = u"肥煤"
    col_name = u"肥煤车板价_A9.5-10%_S<0.6%_V26%_G>95_唐山产_河北"
    wind_code = "S5120111"

###########################################################################################################################
""" 瘦煤 """ 

class ShouMeiCheBanJia_ALT11Prct_V_14To16Prct_SLT0Dot5Prct_GGT30Prct_M9Prct_ChangZhiChan_ShanXi(spot_price_base, WindData):
    field_name = u"瘦煤"
    col_name = u"瘦煤车板价_A<11%_V_14-16%_S<0.5%_G>30%_M9%_长治产_山西"
    wind_code = "S5132025"
    
###########################################################################################################################
""" 主焦煤 """ 

class JinKouZhuJiaoMeiDaoChangJia_A11V27_QianAnShaHeYi(spot_price_base, Manual):
    field_name = u"主焦煤"
    col_name = u"进口主焦煤到厂价_A11V27_迁安沙河驿"

class ZhuJiaoMeiShiChangJia_ALT10Dot5Prct_V20To24Prct_SLT1Prct_GGT75Prct_Y12To15_Mt8Prct_LvLiangChan_ShanXi(spot_price_base, WindData):
    field_name = u"主焦煤"
    col_name = u"主焦煤市场价_A<10.5%_V20-24%_S<1%_G>75%_Y12-15_Mt8%_吕梁产_山西"
    wind_code = "S5120097"

class ZhuJiaoMeiCheBanJia_ALT10Dot5Prct_V21To25Prct_SLT1Prct_GGT75Prct_HanDanChan_HeBei(spot_price_base, WindData):
    field_name = u"主焦煤"
    col_name = u"主焦煤车板价_A<10.5%_V21-25%_S<1%_G>75%_邯郸产_河北"
    wind_code = "S5120098"

class FengJingKuangYingJiaoMeiXianHuoJia_CSR74Prct_V20Dot7Prct_A10Dot5Prct_S0Dot6Prct_P0Dot03Prct_AoDaLiYaChan_ZhongGuoDaoAn(spot_price_base, WindData):
    field_name = u"主焦煤"
    col_name = u"峰景矿硬焦煤现货价_CSR74%_V20.7%_A10.5%_S0.6%_P0.03%_澳大利亚产_中国到岸"
    wind_code = "S5120155"

class ZhongDiHuiFaFenYingJiaoMeiXianHuoJia_CSR64Prct_V25Dot5Prct_A9Dot0Prct_S0Dot6Prct_P0Dot05Prct_AoDaLiYaChan_ZhongGuoDaoAn(spot_price_base, WindData):
    field_name = u"主焦煤"
    col_name = u"中低挥发分硬焦煤现货价_CSR64%_V25.5%_A9.0%_S0.6%_P0.05%_澳大利亚产_中国到岸"
    wind_code = "S5120158"

class ZhuJiaoMeiKuTiJia_A9Prct_V26Prct_S0Dot4Prct_G87_Y15_AoDaLiYaChan_JingTangGang(spot_price_base, WindData):
    field_name = u"主焦煤"
    col_name = u"主焦煤库提价_A9%_V26%_S0.4%_G87_Y15_澳大利亚产_京唐港"
    wind_code = "S5112232"

class ZhuJiaoMeiKuTiJia_A8Prct_V25Prct_0Dot9PrctS_G85_ShanXiChan_JingTangGang(spot_price_base, WindData):
    field_name = u"主焦煤"
    col_name = u"主焦煤库提价_A8%_V25%_0.9%S_G85_山西产_京唐港"
    wind_code = "S5112240"

class ZhuJiaoMeiKuTiJia_A10Prct_V24Prct_LT0Dot8PrctS_G80_HeBeiChan_JingTangGang(spot_price_base, WindData):
    field_name = u"主焦煤"
    col_name = u"主焦煤库提价_A10%_V24%_<0.8%S_G80_河北产_京唐港"
    wind_code = "S5112235"

class ZhuJiaoMeiShiChangJia_A_9Dot3Prct_V24Prct_SLT0Dot5Prct_CSR_71Prct_AoDaLiYaChan_JingTangGang(spot_price_base, WindData):
    field_name = u"主焦煤"
    col_name = u"主焦煤市场价_A_9.3%_V24%_S<0.5%_CSR_71%_澳大利亚产_京唐港"
    wind_code = "S5132053"
        
class ZhuJiaoMeiShiChangJia_ALT9Prct_V27Prct_SLT0Dot6Prct_G_79Prct_Y_18_AoDaLiYaChan_JingTangGang(spot_price_base, WindData):
    field_name = u"主焦煤"
    col_name = u"主焦煤市场价_A<9%_V27%_S<0.6%_G_79%_Y_18_澳大利亚产_京唐港"
    wind_code = "S5132054"
    
class ZhuJiaoMeiShiChangJia_ALT9Dot3Prct_VLT26Prct_SLT0Dot5Prct_G_90Prct_Y18_AoDaLiYaChan_RiZhaoGang(spot_price_base, WindData):
    field_name = u"主焦煤"
    col_name = u"主焦煤市场价_A<9.3%_V<26%_S<0.5%_G_90%_Y18_澳大利亚产_日照港"
    wind_code = "S5132128"

class ZhuJiaoMeiKuTiJia_A9Dot5Prct_V19Prct_0Dot6PrctS_GGT80_Y24mm_AoDaLiYaChan_QingDaoGang(spot_price_base, WindData):
    field_name = u"主焦煤"
    col_name = u"主焦煤库提价_A9.5%_V19%_0.6%S_G>80_Y24mm_澳大利亚产_青岛港"
    wind_code = "S5101463"

class JiaoMeiKuTiJia_A10Dot5Prct_V28Prct_LT0Dot6PrctS_G83_GanQiMaoDao(spot_price_base, WindData):
    field_name = u"主焦煤"
    col_name = u"焦煤库提价_A10.5%_V28%_<0.6%S_G83_甘其毛道"
    wind_code = "S5101441"
    
class JiaoMeiKengKouJia_A16To23Prct_V24Prct_0Dot8PrctS_G60_LvLiang_XiaoYi(spot_price_base, WindData):
    field_name = u"主焦煤"
    col_name = u"焦煤坑口价_A16-23%_V24%_0.8%S_G60_吕梁_孝义"
    wind_code = "S0146047"

class JiaoMeiKengKouJia_A14Prct_V17To20Prct_0Dot4PrctS_GGT60_LinFen_GuXian(spot_price_base, WindData):
    field_name = u"主焦煤"
    col_name = u"焦煤坑口价_A14%_V17-20%_0.4%S_G>60_临汾_古县"
    wind_code = "S0146061"
        
class No4JiaoMeiKengKouJia_A15To18Prct_V19To21Prct_LT0Dot6PrctS_GGT75_LvLiang_LiuLin(spot_price_base, WindData):
    field_name = u"主焦煤"
    col_name = u"4号焦煤坑口价_A15-18%_V19-21%_<0.6%S_G>75_吕梁_柳林"
    wind_code = "S0146045"
    
    
    

if __name__ == "__main__":
    ts = PJXianHuoJiaGe_HuaDong().get_ts()