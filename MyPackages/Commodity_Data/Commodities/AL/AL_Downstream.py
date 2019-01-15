# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 10:45:53 2018

@author: 李弘一萌
"""

import pandas as pd
from datetime import datetime
from .AL_Base import AL_Base
from ...Base.DataType_Base import Manual, Computed, WindData
from ...Base.Plot_Base import Plot_Base
from matplotlib.ticker import FuncFormatter

class downstream_base(AL_Base, Plot_Base):
    table_english_name = "Downstream"
    table_chinese_name = u"下游"
#    original_db_filepath = data_path + u"LPP价格数据库.xlsx"
    
    def output(self):
        print("Downstream")
    
    def get_relevant_df(self, col_list):
        local_col_name_list = downstream_base.get_all_table_classname()
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
""" 铝棒库存 """


class LvBang6063KuCun_HeJi(downstream_base, WindData):
    field_name = u"铝棒库存"
    col_name = u"6063铝棒库存_合计"
    wind_code = "S5811163"

###########################################################################################################################
""" 半成品进出口 """


class LvBanChengPinJinKouZiGeGuoShuJu(downstream_base, Manual):
    field_name = u"半成品进出口"
    col_name = u"铝半成品进口自各国数据"
    
class LvBanChengPinChuKouZhiGeGuoShuJu(downstream_base, Manual):
    field_name = u"半成品进出口"
    col_name = u"铝半成品出口至各国数据"    
    
    
###########################################################################################################################
""" 铝合金供应 """

class LvHeJinChanLiang_LeiJiZhi(downstream_base, WindData):
    field_name = u"铝合金供应"
    col_name = u"铝合金产量_累计值"
    wind_code = "S0027577"
        
class LvHeJinChanLiang_LeiJiTongBi(downstream_base, WindData):
    field_name = u"铝合金供应"
    col_name = u"铝合金产量_累计同比"
    wind_code = "S0027578"    
    
class LvHeJinChanLiang_DangYueZhi(downstream_base, WindData):
    field_name = u"铝合金供应"
    col_name = u"铝合金产量_当月值"
    wind_code = "S0027575"    
    
class LvHeJinChanLiang_DangYueTongBi(downstream_base, WindData):
    field_name = u"铝合金供应"
    col_name = u"铝合金产量_当月同比"
    wind_code = "S0027576"    
    

    
###########################################################################################################################
""" 铝合金价格 """

class LvHeJinJiaGe_ZLD104OrZL104_GuoChan(downstream_base, WindData):
    field_name = u"铝合金价格"
    col_name = u"铝合金价格_ZLD104/ZL104_国产"
    wind_code = "S5801793"    
    
class LvHeJinJiaGe_ZLD102OrZL102_GuoChan(downstream_base, WindData):
    field_name = u"铝合金价格"
    col_name = u"铝合金价格_ZLD102/ZL102_国产"
    wind_code = "S5801792"    

class LvHeJinDingJiaGe_ADC12_ShangHai(downstream_base, WindData):
    field_name = u"铝合金价格"
    col_name = u"铝合金锭价格_ADC-12_上海"
    wind_code = "S0048092"      

class LvHeJinDingJiaGe_ADC12_FoShan(downstream_base, WindData):
    field_name = u"铝合金价格"
    col_name = u"铝合金锭价格_ADC-12_佛山"
    wind_code = "S5801915"  
    
class LvHeJinDingJiaGe_A356_ShangHai(downstream_base, WindData):
    field_name = u"铝合金价格"
    col_name = u"铝合金锭价格_A356_上海"
    wind_code = "S5801926"  
    
class LvHeJinDingJiaGe_A356_FoShan(downstream_base, WindData):
    field_name = u"铝合金价格"
    col_name = u"铝合金锭价格_A356_佛山"
    wind_code = "S5801916"  
    
    
###########################################################################################################################
""" 铝合金进出口 """

class LvHeJinChuKouShuLiang_DangYueZhi(downstream_base, WindData):
    field_name = u"铝合金进出口"
    col_name = u"铝合金出口数量_当月值"
    wind_code = "S0116282"    

###########################################################################################################################
""" 未锻造铝进出口 """

class WeiDuanZaoDeLvChuKouShuLiang_DangYueZhi(downstream_base, WindData):
    field_name = u"未锻造铝进出口"
    col_name = u"未锻造的铝(包括铝合金)出口数量_当月值"
    wind_code = "S0027645" 
    
    
    
if __name__ == "__main__":
    ts = DiLunChangSiChanXiaoLv_15TianPingJun().get_ts()
    
    
    
    
    
    
    




    
    
    