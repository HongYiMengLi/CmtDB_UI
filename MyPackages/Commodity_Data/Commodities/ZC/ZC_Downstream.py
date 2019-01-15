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

class downstream_base(ZC_Base, Plot_Base):
    table_english_name = "Downstream"
    table_chinese_name = u"下游"
    
    def output(self):
        print("Downstream")
    
    def get_relevant_df(self, col_list):
        local_col_name_list = downstream_base.get_all_table_classname()
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
""" 六大电厂 """

class RiJunHaoMeiLiang_ZheDian(downstream_base, WindData):
    field_name = u"六大电厂"
    col_name = u"日均耗煤量_浙电"
    wind_code = "S5116608"  
    
class RiJunHaoMeiLiang_ShangDian(downstream_base, WindData):
    field_name = u"六大电厂"
    col_name = u"日均耗煤量_上电"
    wind_code = "S5116609"  
    
class RiJunHaoMeiLiang_YueDian(downstream_base, WindData):
    field_name = u"六大电厂"
    col_name = u"日均耗煤量_粤电"
    wind_code = "S5116610"  
    
class RiJunHaoMeiLiang_GuoDian(downstream_base, WindData):
    field_name = u"六大电厂"
    col_name = u"日均耗煤量_国电"
    wind_code = "S5116611"  
    
class RiJunHaoMeiLiang_DaTang(downstream_base, WindData):
    field_name = u"六大电厂"
    col_name = u"日均耗煤量_大唐"
    wind_code = "S5116612"  
    
class RiJunHaoMeiLiang_HuaDian(downstream_base, WindData):
    field_name = u"六大电厂"
    col_name = u"日均耗煤量_华电"
    wind_code = "S5116613"  
    
class RiJunHaoMeiLiang_HeJi(downstream_base, WindData):
    field_name = u"六大电厂"
    col_name = u"日均耗煤量_合计"
    wind_code = "S5116614"  
    
class MeiTanKuCun_ZheDian(downstream_base, WindData):
    field_name = u"六大电厂"
    col_name = u"煤炭库存_浙电"
    wind_code = "S5116615"  
    
class MeiTanKuCun_ShangDian(downstream_base, WindData):
    field_name = u"六大电厂"
    col_name = u"煤炭库存_上电"
    wind_code = "S5116616"  
    
class MeiTanKuCun_YueDian(downstream_base, WindData):
    field_name = u"六大电厂"
    col_name = u"煤炭库存_粤电"
    wind_code = "S5116617"  
    
class MeiTanKuCun_GuoDian(downstream_base, WindData):
    field_name = u"六大电厂"
    col_name = u"煤炭库存_国电"
    wind_code = "S5116618"  
    
class MeiTanKuCun_DaTang(downstream_base, WindData):
    field_name = u"六大电厂"
    col_name = u"煤炭库存_大唐"
    wind_code = "S5116619"  
    
class MeiTanKuCun_HuaDian(downstream_base, WindData):
    field_name = u"六大电厂"
    col_name = u"煤炭库存_华电"
    wind_code = "S5116620"  
    
class MeiTanKuCun_DianChangHeJi(downstream_base, WindData):
    field_name = u"六大电厂"
    col_name = u"煤炭库存_电厂合计"
    wind_code = "S5116621"  
    
class MeiTanKuCunKeYongTianShu_ZheDian(downstream_base, WindData):
    field_name = u"六大电厂"
    col_name = u"煤炭库存可用天数_浙电"
    wind_code = "S5124368"  
    
class MeiTanKuCunKeYongTianShu_ShangDian(downstream_base, WindData):
    field_name = u"六大电厂"
    col_name = u"煤炭库存可用天数_上电"
    wind_code = "S5124369"  
    
class MeiTanKuCunKeYongTianShu_YueDian(downstream_base, WindData):
    field_name = u"六大电厂"
    col_name = u"煤炭库存可用天数_粤电"
    wind_code = "S5124370"  
    
class MeiTanKuCunKeYongTianShu_GuoDian(downstream_base, WindData):
    field_name = u"六大电厂"
    col_name = u"煤炭库存可用天数_国电"
    wind_code = "S5124371"  
    
class MeiTanKuCunKeYongTianShu_DaTang(downstream_base, WindData):
    field_name = u"六大电厂"
    col_name = u"煤炭库存可用天数_大唐"
    wind_code = "S5124372"  
    
class MeiTanKuCunKeYongTianShu_HuaDian(downstream_base, WindData):
    field_name = u"六大电厂"
    col_name = u"煤炭库存可用天数_华电"
    wind_code = "S5124373"  
    
class MeiTanKuCunKeYongTianShu_ZongJi(downstream_base, WindData):
    field_name = u"六大电厂"
    col_name = u"煤炭库存可用天数_总计"
    wind_code = "S5116622"  
    
    
###########################################################################################################################
""" 水库站水文信息 """

class ShuiWei_SanXia_ShangYou(downstream_base, WindData):
    field_name = u"水库站水文信息"
    col_name = u"水位_三峡_上游"
    wind_code = "S5110940"  

class ShuiWei_SanXia_XiaYou(downstream_base, WindData):
    field_name = u"水库站水文信息"
    col_name = u"水位_三峡_下游"
    wind_code = "S5110941" 

class LiuLiang_SanXia_RuKu(downstream_base, WindData):
    field_name = u"水库站水文信息"
    col_name = u"流量_三峡_入库"
    wind_code = "S5110944" 

class LiuLiang_SanXia_ChuKu(downstream_base, WindData):
    field_name = u"水库站水文信息"
    col_name = u"流量_三峡_出库"
    wind_code = "S5110945" 




























    

    