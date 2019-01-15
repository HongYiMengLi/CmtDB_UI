# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 10:45:53 2018

@author: 李弘一萌
"""

import pandas as pd
from datetime import datetime
from .ZN_Base import ZN_Base
from ...Base.DataType_Base import Manual, Computed, WindData
from ...Base.Plot_Base import Plot_Base
from matplotlib.ticker import FuncFormatter

class downstream_base(ZN_Base, Plot_Base):
    table_english_name = "Downstream"
    table_chinese_name = u"下游"
    
    def output(self):
        print("Downstream")
    
    def get_relevant_df(self, col_list):
        local_col_name_list = downstream_base.get_all_table_classname()
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
""" 镀锌板产量 """


class DuXinBan_DaiChanLiang_ZhongDianQiYe_LeiJiZhi(downstream_base, WindData):
    field_name = u"镀锌板产量"
    col_name = u"镀锌板(带)产量_重点企业_累计值"
    wind_code = "S0114079"
    
class DuXinBan_DaiXiaoShouLiang_ZhongDianQiYe_LeiJiZhi(downstream_base, WindData):
    field_name = u"镀锌板产量"
    col_name = u"镀锌板(带)销售量_重点企业_累计值"
    wind_code = "S0066451"
    
class DuXinBan_DaiXiaoShouLiang_ChuKou_LeiJiZhi(downstream_base, WindData):
    field_name = u"镀锌板产量"
    col_name = u"镀锌板(带)销售量_出口_累计值"
    wind_code = "S0066631"
    
class DuXinBan_DaiKuCun_DuXinBan_Dai(downstream_base, WindData):
    field_name = u"镀锌板产量"
    col_name = u"镀锌板(带)库存_镀锌板(带)"
    wind_code = "S0066739"
    

    
###########################################################################################################################
""" 镀锌板卷价格 """

class DuXinBanJuanJiaGe_0Dot5mmDuXin_ShangHai(downstream_base, WindData):
    field_name = u"镀锌板卷价格"
    col_name = u"镀锌板卷价格_0.5mm镀锌_上海"
    wind_code = "S5704810"
        
class DuXinBanJuanJiaGe_0Dot5mmDuXin_TianJin(downstream_base, WindData):
    field_name = u"镀锌板卷价格"
    col_name = u"镀锌板卷价格_0.5mm镀锌_天津"
    wind_code = "S5704813"    
    
class DuXinBanJuanJiaGe_0Dot5mmDuXin_GuangZhou(downstream_base, WindData):
    field_name = u"镀锌板卷价格"
    col_name = u"镀锌板卷价格_0.5mm镀锌_广州"
    wind_code = "S5704815"    
    
class DuXinBanJuanJiaGe_0Dot5mmDuXin_BoXing(downstream_base, WindData):
    field_name = u"镀锌板卷价格"
    col_name = u"镀锌板卷价格_0.5mm镀锌_博兴"
    wind_code = "S5704814"    
    

###########################################################################################################################
""" 锌合金价格 """

class XinHeJinJiaGe_Zamak5OverZX03_GuoChan(downstream_base, WindData):
    field_name = u"锌合金价格"
    col_name = u"锌合金价格_Zamak5/ZX03_国产"
    wind_code = "S5801799"    
    
class XinHeJinJiaGe_Zamak3OverZX01_GuoChan(downstream_base, WindData):
    field_name = u"锌合金价格"
    col_name = u"锌合金价格_Zamak3/ZX01_国产"
    wind_code = "S5801798"    

    
    
if __name__ == "__main__":
    ts = DiLunChangSiChanXiaoLv_15TianPingJun().get_ts()
    
    
    
    
    
    
    




    
    
    