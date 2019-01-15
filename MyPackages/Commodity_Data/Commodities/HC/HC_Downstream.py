# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 10:45:53 2018

@author: 李弘一萌
"""

import pandas as pd
from datetime import datetime
from .HC_Base import HC_Base
from . import HC_SpotPrice, HC_Upstream, HC_Macro
from ...Base.DataType_Base import Manual, Computed, WindData
from ...Base.Plot_Base import Plot_Base
from matplotlib.ticker import FuncFormatter

class downstream_base(HC_Base, Plot_Base):
    table_english_name = "Downstream"
    table_chinese_name = u"下游"
#    original_db_filepath = data_path + u"LPP价格数据库.xlsx"
    
    def output(self):
        print("Downstream")
    
    def get_relevant_df(self, col_list):
        local_col_name_list = downstream_base.get_all_table_classname()
        col_cls_list = []
        for x in col_list:
            col_cls_name = str(HC_Base.get_class_name(x))
            if col_cls_name not in local_col_name_list:
                col_cls_list.append(eval(HC_Base.get_table_class_full_variable(x)))
            else:
                col_cls_list.append(eval(col_cls_name))
        ts_list = [x().get_ts() for x in col_cls_list]
        tmp_table_df = pd.concat(ts_list, axis=1).dropna(how="all")
        return tmp_table_df 


###########################################################################################################################
""" 家电行业 """

class KongDiaoChanLiang_DangYueZhi(downstream_base, WindData):
    field_name = u"家电行业"
    col_name = u"空调产量_当月值"
    wind_code = "S0028202"
    
class JiaYongDianBingXiangChanLiang_DangYueZhi(downstream_base, WindData):
    field_name = u"家电行业"
    col_name = u"家用电冰箱产量_当月值"
    wind_code = "S0028206"

class JiaYongXiYiJiChanLiang_DangYueZhi(downstream_base, WindData):
    field_name = u"家电行业"
    col_name = u"家用洗衣机产量_当月值"
    wind_code = "S0028210"
    


###########################################################################################################################
""" 冷卷产量 """

class LengZhaJuanBanZhouChanLiang(downstream_base, Manual):
    field_name = u"冷卷产量"
    col_name = u"冷轧卷板周产量"

class LengZhaBaoBanChanLiang_DangYueZhi(downstream_base, WindData):
    field_name = u"冷卷产量"
    col_name = u"冷轧薄板产量_当月值"
    wind_code = "S0027418"
    
class LengZhaBaoKuanGangDaiChanLiang_DangYueZhi(downstream_base, WindData):
    field_name = u"冷卷产量"
    col_name = u"冷轧薄宽钢带产量_当月值"
    wind_code = "S0027430"
    
class LengZhaZhaiGangDaiChanLiang_DangYueZhi(downstream_base, WindData):
    field_name = u"冷卷产量"
    col_name = u"冷轧窄钢带产量_当月值"
    wind_code = "S0027438"
    
###########################################################################################################################
""" 汽车行业 """

class QiCheChanLiang_DangYueZhi(downstream_base, WindData):
    field_name = u"汽车行业"
    col_name = u"汽车产量_当月值"
    wind_code = "S0027907"

###########################################################################################################################
""" 造船行业 """

class ZaoChuanWanGongLiang_LeiJiZhi(downstream_base, WindData):
    field_name = u"造船行业"
    col_name = u"造船完工量_累计值"
    wind_code = "S6000029"
    
###########################################################################################################################
""" 出口利润 """

class ReJuanChuKouLiRun_ShangHaiGang(downstream_base, Computed):
    field_name = u"出口利润"
    col_name = u"热卷出口利润_上海港"
    
    def get_ts_whole_progress(self):
        relevant_col_list = [u"中间价_美元兑人民币", u"热卷出口FOB报价_Q235B_5.5*1500_上海港", u"热卷现货价格_Q235B_4.75mm_上海"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"热卷出口FOB报价_Q235B_5.5*1500_上海港"] * tmp_total[u"中间价_美元兑人民币"] * (1 + 0.13 / 0.16) - 55 - \
                                   tmp_total[u"热卷现货价格_Q235B_4.75mm_上海"]
        return tmp_total

class LuoWenChuKouLiRun_TianJinGang(downstream_base, Computed):
    field_name = u"出口利润"
    col_name = u"热卷出口利润_天津港"
    
    def get_ts_whole_progress(self):
        relevant_col_list = [u"中间价_美元兑人民币", u"热卷出口FOB报价_Q235B_5.5*1500_天津港", u"热卷现货价格_Q235B_4.75mm_天津"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"热卷出口FOB报价_Q235B_5.5*1500_天津港"] * tmp_total[u"中间价_美元兑人民币"] * (1 + 0.13 / 0.16) - 55 - \
                                   tmp_total[u"热卷现货价格_Q235B_4.75mm_天津"]
        return tmp_total


    
    
    
if __name__ == "__main__":
    ts = DiLunChangSiChanXiaoLv_15TianPingJun().get_ts()
    
    
    
    
    
    
    




    
    
    