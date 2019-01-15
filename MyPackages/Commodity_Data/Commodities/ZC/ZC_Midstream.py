# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 10:45:53 2018

@author: 李弘一萌
"""

import pandas as pd
from datetime import datetime
from .ZC_Base import ZC_Base
from . import ZC_SpotPrice
from ...Base.DataType_Base import Manual, Computed, WindData
from ...Base.Plot_Base import Plot_Base
from matplotlib.ticker import FuncFormatter

class midstream_base(ZC_Base, Plot_Base):
    table_english_name = "Midstream"
    table_chinese_name = u"中游"
    
    def output(self):
        print("Midstream")
    
    def get_relevant_df(self, col_list):
        local_col_name_list = midstream_base.get_all_table_classname()
        col_cls_list = []
        for x in col_list:
            col_cls_name = str(ZC_Base.get_class_name(x))
            if col_cls_name not in local_col_name_list:
                col_cls_list.append(eval(ZC_Base.get_table_class_full_variable(x)))
            else:
                col_cls_list.append(eval(col_cls_name))
        ts_list = [x().get_ts() for x in col_cls_list]
        tmp_table_df = pd.concat(ts_list, axis=1).dropna(how="all")
        return tmp_table_df 
    
###########################################################################################################################
""" 国际海运指数 """

class BDI_BoLuoDeHaiGanSanHuoZhiShu(midstream_base, WindData):
    field_name = u"国际海运指数"
    col_name = u"BDI_波罗的海干散货指数"
    wind_code = "S0031550"      

class BPI_BaMaMaXingYunFeiZhiShu(midstream_base, WindData):
    field_name = u"国际海运指数"
    col_name = u"BPI_巴拿马型运费指数"
    wind_code = "S0031551"   

class BCI_HaoWangJiaoXingYunFeiZhiShu(midstream_base, WindData):
    field_name = u"国际海运指数"
    col_name = u"BCI_好望角型运费指数"
    wind_code = "S0031552"   

class BSI_ChaoJiDaLingBianXingYunFeiZhiShu(midstream_base, WindData):
    field_name = u"国际海运指数"
    col_name = u"BSI_超级大灵便型运费指数"
    wind_code = "S0031555"   


###########################################################################################################################
""" 国际海运指数 """

class MeiTanKuCun_QinHuangDaoGang(midstream_base, WindData):
    field_name = u"国际海运指数"
    col_name = u"煤炭库存_秦皇岛港"
    wind_code = "S5125187"  

class MeiTanKuCun_CaoFeiDianGang(midstream_base, WindData):
    field_name = u"国际海运指数"
    col_name = u"煤炭库存_曹妃甸港"
    wind_code = "S5125188"  

class MeiTanKuCun_JingTangGangLaoGang(midstream_base, WindData):
    field_name = u"国际海运指数"
    col_name = u"煤炭库存_京唐港老港"
    wind_code = "S5125189"  

class MeiTanKuCun_GuoTouJingTangGang(midstream_base, WindData):
    field_name = u"国际海运指数"
    col_name = u"煤炭库存_国投京唐港"
    wind_code = "S5125190"  

class MeiTanKuCun_HuangHuaGang(midstream_base, WindData):
    field_name = u"国际海运指数"
    col_name = u"煤炭库存_黄骅港"
    wind_code = "S5131051"  

class MaoDiChuanBoShu_QinHuangDaoGang(midstream_base, WindData):
    field_name = u"国际海运指数"
    col_name = u"锚地船舶数_秦皇岛港"
    wind_code = "S5104484"  

class MaoDiChuanBoShu_CaoFeiDianGang(midstream_base, WindData):
    field_name = u"国际海运指数"
    col_name = u"锚地船舶数_曹妃甸港"
    wind_code = "S5125270"  

class MaoDiChuanBoShu_JingTangGangDongGang(midstream_base, WindData):
    field_name = u"国际海运指数"
    col_name = u"锚地船舶数_京唐港东港"
    wind_code = "S5125271"  

class MaoDiChuanBoShu_HuangHuaGang(midstream_base, WindData):
    field_name = u"国际海运指数"
    col_name = u"锚地船舶数_黄骅港"
    wind_code = "S5131050"  

class YuDaoChuanBoShu_QinHuangDaoGang(midstream_base, WindData):
    field_name = u"国际海运指数"
    col_name = u"预到船舶数_秦皇岛港"
    wind_code = "S5104485"  

class YuDaoChuanBoShu_CaoFeiDianGang(midstream_base, WindData):
    field_name = u"国际海运指数"
    col_name = u"预到船舶数_曹妃甸港"
    wind_code = "S5125273"  

class YuDaoChuanBoShu_JingTangGangDongGang(midstream_base, WindData):
    field_name = u"国际海运指数"
    col_name = u"预到船舶数_京唐港东港"
    wind_code = "S5125274"  

class TieLuDiaoRuLiang_QinHuangDaoGang(midstream_base, WindData):
    field_name = u"国际海运指数"
    col_name = u"铁路调入量_秦皇岛港"
    wind_code = "S5104482"  

class TieLuDiaoRuLiang_CaoFeiDianGang(midstream_base, WindData):
    field_name = u"国际海运指数"
    col_name = u"铁路调入量_曹妃甸港"
    wind_code = "S5125266"  

class TieLuDiaoRuLiang_JingTangGangDongGang(midstream_base, WindData):
    field_name = u"国际海运指数"
    col_name = u"铁路调入量_京唐港东港"
    wind_code = "S5125267"  

class TieLuDiaoRuLiang_JingTangGangMeiTanGongSi(midstream_base, WindData):
    field_name = u"国际海运指数"
    col_name = u"铁路调入量_京唐港煤炭公司"
    wind_code = "S5125268"  

class TieLuDiaoRuLiang_HuangHuaGang(midstream_base, WindData):
    field_name = u"国际海运指数"
    col_name = u"铁路调入量_黄骅港"
    wind_code = "S5131048"  

class GangKouTunTuLiang_QinHuangDaoGang(midstream_base, WindData):
    field_name = u"国际海运指数"
    col_name = u"港口吞吐量_秦皇岛港"
    wind_code = "S5104483"  

class GangKouTunTuLiang_CaoFeiDianGang(midstream_base, WindData):
    field_name = u"国际海运指数"
    col_name = u"港口吞吐量_曹妃甸港"
    wind_code = "S5125262"  

class GangKouTunTuLiang_JingTangGangDongGang(midstream_base, WindData):
    field_name = u"国际海运指数"
    col_name = u"港口吞吐量_京唐港东港"
    wind_code = "S5125263"  

class GangKouTunTuLiang_JingTangGangMeiTanGongSi(midstream_base, WindData):
    field_name = u"国际海运指数"
    col_name = u"港口吞吐量_京唐港煤炭公司"
    wind_code = "S5125264"  

class GangKouTunTuLiang_HuangHuaGang(midstream_base, WindData):
    field_name = u"国际海运指数"
    col_name = u"港口吞吐量_黄骅港"
    wind_code = "S5131049"  

###########################################################################################################################
""" 沿海煤炭运价 """

class YanHaiMeiTanYunJia_QinHuangDao_ShangHai_4_5WanDWT(midstream_base, WindData):
    field_name = u"沿海煤炭运价"
    col_name = u"沿海煤炭运价_秦皇岛-上海_4-5万DWT"
    wind_code = "S0167815"  

class YanHaiMeiTanYunJia_QinHuangDao_GuangZhou_5_6WanDWT(midstream_base, WindData):
    field_name = u"沿海煤炭运价"
    col_name = u"沿海煤炭运价_秦皇岛-广州_5-6万DWT"
    wind_code = "S0167812"  

class YanHaiMeiTanYunJia_QinHuangDao_ZhangJiaGang_2_3WanDWT(midstream_base, WindData):
    field_name = u"沿海煤炭运价"
    col_name = u"沿海煤炭运价_秦皇岛-张家港_2-3万DWT"
    wind_code = "S0167816"  

class YanHaiMeiTanYunJia_HuangHua_ShangHai_3_4WanDWT(midstream_base, WindData):
    field_name = u"沿海煤炭运价"
    col_name = u"沿海煤炭运价_黄骅-上海_3-4万DWT"
    wind_code = "S0167817"  

###########################################################################################################################
""" 长江口库存 """

class MeiTanKuCun_RuGaoGang(midstream_base, WindData):
    field_name = u"长江口库存"
    col_name = u"煤炭库存_如皋港"
    wind_code = "S5133550"  

class MeiTanKuCun_ChangHongGuoJi(midstream_base, WindData):
    field_name = u"长江口库存"
    col_name = u"煤炭库存_长宏国际"
    wind_code = "S5133551"  

class MeiTanKuCun_JiangYinGang(midstream_base, WindData):
    field_name = u"长江口库存"
    col_name = u"煤炭库存_江阴港"
    wind_code = "S5133552"  

class MeiTanKuCun_YangZiJiang(midstream_base, WindData):
    field_name = u"长江口库存"
    col_name = u"煤炭库存_扬子江"
    wind_code = "S5133553"  

class MeiTanKuCun_TaiHeGang(midstream_base, WindData):
    field_name = u"长江口库存"
    col_name = u"煤炭库存_太和港"
    wind_code = "S5133554"  

class MeiTanKuCun_HeJi(midstream_base, WindData):
    field_name = u"长江口库存"
    col_name = u"煤炭库存_合计"
    wind_code = "S5133555"  






    

    