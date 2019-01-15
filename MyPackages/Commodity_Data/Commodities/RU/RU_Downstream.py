# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 10:45:53 2018

@author: 李弘一萌
"""

import pandas as pd
from datetime import datetime
from .RU_Base import RU_Base
from ...Base.DataType_Base import Manual, Computed, WindData
from ...Base.Plot_Base import Plot_Base
from matplotlib.ticker import FuncFormatter

class downstream_base(RU_Base, Plot_Base):
    table_english_name = "Downstream"
    table_chinese_name = u"下游"
    
    def output(self):
        print("Downstream")
    
    def get_relevant_df(self, col_list):
        local_col_name_list = downstream_base.get_all_table_classname()
        col_cls_list = []
        for x in col_list:
            col_cls_name = str(RU_Base.get_class_name(x))
            if col_cls_name not in local_col_name_list:
                col_cls_list.append(eval(RU_Base.get_table_class_full_variable(x)))
            else:
                col_cls_list.append(eval(col_cls_name))
        ts_list = [x().get_ts() for x in col_cls_list]
        tmp_table_df = pd.concat(ts_list, axis=1).dropna(how="all")
        return tmp_table_df 
    
    
###########################################################################################################################
""" 产量销量 """

class LunTaiChanLiang(downstream_base, WindData):
    field_name = u"产量销量"
    col_name = u"轮胎产量"
    wind_code = "S5456949"  
    
class QiCheChanLiang(downstream_base, WindData):
    field_name = u"产量销量"
    col_name = u"汽车产量"
    wind_code = "S0105523"  
    
class QiCheXiaoLiang(downstream_base, WindData):
    field_name = u"产量销量"
    col_name = u"汽车销量"
    wind_code = "S0105710"  

###########################################################################################################################
""" 出口 """
    
class XinChongQiXiangJiaoLunTaiChuKouShuLiang(downstream_base, WindData):
    field_name = u"出口"
    col_name = u"新充气橡胶轮胎出口数量"
    wind_code = "S0072011"  
    
class QiCheZhengCheChuKouShuLiang(downstream_base, WindData):
    field_name = u"出口"
    col_name = u"汽车整车出口数量"
    wind_code = "S6110885"  
    
###########################################################################################################################
""" 开工 """
        
class QuanGangTaiKaiGongLv(downstream_base, WindData):
    field_name = u"开工"
    col_name = u"全钢胎开工率"
    wind_code = "S6124650"  
    
class BanGangTaiKaiGongLv(downstream_base, WindData):
    field_name = u"开工"
    col_name = u"半钢胎开工率"
    wind_code = "S6124651"    

###########################################################################################################################
""" 库存 """
        
class QiCheKuCun(downstream_base, WindData):
    field_name = u"库存"
    col_name = u"汽车库存"
    wind_code = "S6125070" 
        
class ChengYongCheKuCun(downstream_base, WindData):
    field_name = u"库存"
    col_name = u"乘用车库存"
    wind_code = "S6125071" 
    
class ShangYongCheKuCun(downstream_base, WindData):
    field_name = u"库存"
    col_name = u"商用车库存"
    wind_code = "S6125072"
        
class QiCheJingXiaoShangKuCunYuJingZhiShu(downstream_base, WindData):
    field_name = u"库存"
    col_name = u"汽车经销商库存预警指数"
    wind_code = "S6124430" 
























    

    