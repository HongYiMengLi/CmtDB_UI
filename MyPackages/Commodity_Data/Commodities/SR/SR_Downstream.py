# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 10:45:53 2018

@author: 李弘一萌
"""

import pandas as pd
from datetime import datetime
from .SR_Base import SR_Base
from . import SR_SpotPrice
from ...Base.DataType_Base import Manual, Computed, WindData
from ...Base.Plot_Base import Plot_Base
from matplotlib.ticker import FuncFormatter

class downstream_base(SR_Base, Plot_Base):
    table_english_name = "Downstream"
    table_chinese_name = u"下游"
    
    def output(self):
        print("Downstream")
    
    def get_relevant_df(self, col_list):
        local_col_name_list = downstream_base.get_all_table_classname()
        col_cls_list = []
        for x in col_list:
            col_cls_name = str(SR_Base.get_class_name(x))
            if col_cls_name not in local_col_name_list:
                col_cls_list.append(eval(SR_Base.get_table_class_full_variable(x)))
            else:
                col_cls_list.append(eval(col_cls_name))
        ts_list = [x().get_ts() for x in col_cls_list]
        tmp_table_df = pd.concat(ts_list, axis=1).dropna(how="all")
        return tmp_table_df 
    
    
###########################################################################################################################
""" 含糖食品产量 """

class TangGuo_HanTangShiPinChanLiang(downstream_base, Manual):
    field_name = u"含糖食品产量"
    col_name = u"糖果_含糖食品产量"
    
class SuDongZhuShiPin_HanTangShiPinChanLiang(downstream_base, Manual):
    field_name = u"含糖食品产量"
    col_name = u"速冻主食品_含糖食品产量"
    
class RuZhiPin_HanTangShiPinChanLiang(downstream_base, Manual):
    field_name = u"含糖食品产量"
    col_name = u"乳制品_含糖食品产量"
    
class GuanTou_HanTangShiPinChanLiang(downstream_base, Manual):
    field_name = u"含糖食品产量"
    col_name = u"罐头_含糖食品产量"
    
class TanSuanYinLiao_HanTangShiPinChanLiang(downstream_base, Manual):
    field_name = u"含糖食品产量"
    col_name = u"碳酸饮料_含糖食品产量"
    
class GuoZhiJiGuoZhiYinLiao_HanTangShiPinChanLiang(downstream_base, Manual):
    field_name = u"含糖食品产量"
    col_name = u"果汁及果汁饮料_含糖食品产量"
    
class LengDongYinPin_HanTangShiPinChanLiang(downstream_base, Manual):
    field_name = u"含糖食品产量"
    col_name = u"冷冻饮品_含糖食品产量"
    

class ZongHe_HanTangShiPinChanLiang(downstream_base, Computed):
    field_name = u"含糖食品产量"
    col_name = u"总和_含糖食品产量"   
    def get_ts_whole_progress(self):
        relevant_col_list = [u"糖果_含糖食品产量", u"速冻主食品_含糖食品产量", u"乳制品_含糖食品产量", u"罐头_含糖食品产量", 
                             u"碳酸饮料_含糖食品产量", u"果汁及果汁饮料_含糖食品产量", u"冷冻饮品_含糖食品产量"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total.sum(axis=1)
        return tmp_total  






























    

    