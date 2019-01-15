# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 10:45:53 2018

@author: 李弘一萌
"""

import pandas as pd
from datetime import datetime
from .I_Base import I_Base
from . import I_SpotPrice, I_Upstream
from ...Base.DataType_Base import Manual, Computed, WindData
from ...Base.Plot_Base import Plot_Base
from matplotlib.ticker import FuncFormatter

class downstream_base(I_Base, Plot_Base):
    table_english_name = "Downstream"
    table_chinese_name = u"下游"
#    original_db_filepath = data_path + u"LPP价格数据库.xlsx"
    
    def output(self):
        print("Downstream")
    
    def get_relevant_df(self, col_list):
        local_col_name_list = downstream_base.get_all_table_classname()
        col_cls_list = []
        for x in col_list:
            col_cls_name = str(I_Base.get_class_name(x))
            if col_cls_name not in local_col_name_list:
                col_cls_list.append(eval(I_Base.get_table_class_full_variable(x)))
            else:
                col_cls_list.append(eval(col_cls_name))
        ts_list = [x().get_ts() for x in col_cls_list]
        tmp_table_df = pd.concat(ts_list, axis=1).dropna(how="all")
        return tmp_table_df 


###########################################################################################################################
""" 粗钢产量 """

class CuGangRiJunChanLiang_ZhongDianQiYe(downstream_base, WindData):
    field_name = u"粗钢产量"
    col_name = u"粗钢日均产量_重点企业"
    wind_code = "S5708246"

class CuGangChanLiang_DangYueZhi(downstream_base, WindData):
    field_name = u"粗钢产量"
    col_name = u"粗钢产量_当月值"
    wind_code = "S0027374"

   

###########################################################################################################################
""" 高炉生产 """

class MysteelQuanGuoGangChangGaoLuChanNengLiYongLv(downstream_base, Manual):
    field_name = u"高炉生产"
    col_name = u"Mysteel全国钢厂高炉产能利用率" 
    
class GaoLuKaiGongLv_QuanGuo(downstream_base, WindData):
    field_name = u"高炉生产"
    col_name = u"高炉开工率_全国"
    wind_code = "S5708175"

class YingLiGangChangBiLv_QuanGuo(downstream_base, WindData):
    field_name = u"高炉生产"
    col_name = u"盈利钢厂比率_全国"
    wind_code = "S5708339"

class GaoLuKaiGongLv_TangShan(downstream_base, WindData):
    field_name = u"高炉生产"
    col_name = u"高炉开工率_唐山"
    wind_code = "S5707135"


































    
if __name__ == "__main__":
    ts = DiLunChangSiChanXiaoLv_15TianPingJun().get_ts()
    
    
    
    
    
    
    




    
    
    