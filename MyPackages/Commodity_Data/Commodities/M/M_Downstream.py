# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 10:45:53 2018

@author: 李弘一萌
"""

import pandas as pd
from datetime import datetime
from .M_Base import M_Base
from ...Base.DataType_Base import Manual, Computed, WindData
from ...Base.Plot_Base import Plot_Base
from matplotlib.ticker import FuncFormatter

class downstream_base(M_Base, Plot_Base):
    table_english_name = "Downstream"
    table_chinese_name = u"下游"
    
    def output(self):
        print("Downstream")
    
    def get_relevant_df(self, col_list):
        local_col_name_list = downstream_base.get_all_table_classname()
        col_cls_list = []
        for x in col_list:
            col_cls_name = str(M_Base.get_class_name(x))
            if col_cls_name not in local_col_name_list:
                col_cls_list.append(eval(M_Base.get_table_class_full_variable(x)))
            else:
                col_cls_list.append(eval(col_cls_name))
        ts_list = [x().get_ts() for x in col_cls_list]
        tmp_table_df = pd.concat(ts_list, axis=1).dropna(how="all")
        return tmp_table_df 
    
    
###########################################################################################################################
""" 成交量 """

class DouPoLeiJiChengJiaoLiang_Zhou(downstream_base, Manual):
    field_name = u"成交量"
    col_name = u"豆粕累计成交量（周）"
    
class DouPoRiJunChengJiaoLiang_Zhou(downstream_base, Manual):
    field_name = u"成交量"
    col_name = u"豆粕日均成交量（周）"
    
###########################################################################################################################
""" 存栏量 """

class ShengZhuCunLanLiang(downstream_base, WindData):
    field_name = u"存栏量"
    col_name = u"生猪存栏量"
    wind_code = "S0114186"

class NengFanMuZhuCunLanLiang(downstream_base, WindData):
    field_name = u"存栏量"
    col_name = u"能繁母猪存栏量"
    wind_code = "S0114187"

###########################################################################################################################
""" 生猪价格 """

class ShengZhuJiaGe_WaiSanYuan_JiLin(downstream_base, Manual):
    field_name = u"生猪价格"
    col_name = u"生猪价格_外三元_吉林"

class ShengZhuJiaGe_WaiSanYuan_SiChuan(downstream_base, Manual):
    field_name = u"生猪价格"
    col_name = u"生猪价格_外三元_四川"

class ShengZhuJiaGe_WaiSanYuan_ShanDong(downstream_base, Manual):
    field_name = u"生猪价格"
    col_name = u"生猪价格_外三元_山东"

class ShengZhuJiaGe_WaiSanYuan_HeNan(downstream_base, Manual):
    field_name = u"生猪价格"
    col_name = u"生猪价格_外三元_河南"

class ShengZhuJiaGe_WaiSanYuan_GuangDong(downstream_base, Manual):
    field_name = u"生猪价格"
    col_name = u"生猪价格_外三元_广东"

class ShengZhuJiaGe_WaiSanYuan_QuanGuo(downstream_base, Manual):
    field_name = u"生猪价格"
    col_name = u"生猪价格_外三元_全国"

###########################################################################################################################
""" 生猪养殖费用 """

class ShengZhuYangZhiQiTaFeiYong_JiLin(downstream_base, Manual):
    field_name = u"生猪养殖费用"
    col_name = u"生猪养殖其他费用_吉林"

class ShengZhuYangZhiQiTaFeiYong_SiChuan(downstream_base, Manual):
    field_name = u"生猪养殖费用"
    col_name = u"生猪养殖其他费用_四川"

class ShengZhuYangZhiQiTaFeiYong_ShanDong(downstream_base, Manual):
    field_name = u"生猪养殖费用"
    col_name = u"生猪养殖其他费用_山东"

class ShengZhuYangZhiQiTaFeiYong_HeNan(downstream_base, Manual):
    field_name = u"生猪养殖费用"
    col_name = u"生猪养殖其他费用_河南"

class ShengZhuYangZhiQiTaFeiYong_GuangDong(downstream_base, Manual):
    field_name = u"生猪养殖费用"
    col_name = u"生猪养殖其他费用_广东"

class ShengZhuYangZhiQiTaFeiYong_QuanGuo(downstream_base, Manual):
    field_name = u"生猪养殖费用"
    col_name = u"生猪养殖其他费用_全国"

###########################################################################################################################
""" 养殖利润 """

class ShengZhuYangZhiLiRun_TouJunYingLi_JiLin(downstream_base, Manual):
    field_name = u"养殖利润"
    col_name = u"生猪养殖利润_头均盈利_吉林"

class ShengZhuYangZhiLiRun_TouJunYingLi_SiChuan(downstream_base, Manual):
    field_name = u"养殖利润"
    col_name = u"生猪养殖利润_头均盈利_四川"

class ShengZhuYangZhiLiRun_TouJunYingLi_ShanDong(downstream_base, Manual):
    field_name = u"养殖利润"
    col_name = u"生猪养殖利润_头均盈利_山东"

class ShengZhuYangZhiLiRun_TouJunYingLi_HeNan(downstream_base, Manual):
    field_name = u"养殖利润"
    col_name = u"生猪养殖利润_头均盈利_河南"

class ShengZhuYangZhiLiRun_TouJunYingLi_GuangDong(downstream_base, Manual):
    field_name = u"养殖利润"
    col_name = u"生猪养殖利润_头均盈利_广东"

class ShengZhuYangZhiLiRun_TouJunYingLi_QuanGuo(downstream_base, Manual):
    field_name = u"养殖利润"
    col_name = u"生猪养殖利润_头均盈利_全国"

class YangZhiLiRun_ZiFanZiYangShengZhu(downstream_base, WindData):
    field_name = u"养殖利润"
    col_name = u"生猪养殖利润_头均盈利_吉林"
    wind_code = "S5021738"

class YangZhiLiRun_WaiGouZiZhu(downstream_base, Manual):
    field_name = u"养殖利润"
    col_name = u"养殖利润_外购仔猪"
    wind_code = "S5021739"

###########################################################################################################################
""" 仔猪价格 """

class ZiZhuJiaGe_JiLin(downstream_base, Manual):
    field_name = u"仔猪价格"
    col_name = u"仔猪价格_吉林"

class ZiZhuJiaGe_SiChuan(downstream_base, Manual):
    field_name = u"仔猪价格"
    col_name = u"仔猪价格_四川"

class ZiZhuJiaGe_ShanDong(downstream_base, Manual):
    field_name = u"仔猪价格"
    col_name = u"仔猪价格_山东"

class ZiZhuJiaGe_HeNan(downstream_base, Manual):
    field_name = u"仔猪价格"
    col_name = u"仔猪价格_河南"

class ZiZhuJiaGe_GuangDong(downstream_base, Manual):
    field_name = u"仔猪价格"
    col_name = u"仔猪价格_广东"

class ZiZhuJiaGe_QuanGuo(downstream_base, Manual):
    field_name = u"仔猪价格"
    col_name = u"仔猪价格_全国"

###########################################################################################################################
""" 仔猪价格 """

class ZhuLiangBiJia_QuanGuo(downstream_base, WindData):
    field_name = u"仔猪价格"
    col_name = u"猪粮比价_全国"
    wind_code = "S5021736"

class ZhuLiaoBiJia_QuanGuo(downstream_base, WindData):
    field_name = u"仔猪价格"
    col_name = u"猪料比价_全国"
    wind_code = "S5021737"




    

    