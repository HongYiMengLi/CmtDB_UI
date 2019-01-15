# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 16:35:12 2018

@author: 李弘一萌
"""

import pandas as pd
from datetime import datetime
from .P_Base import P_Base
from ...Base.DataType_Base import Manual, Computed, WindData
from ...Base.Plot_Base import Plot_Base
from matplotlib.ticker import FuncFormatter

class spot_price_base(P_Base, Plot_Base):
    table_english_name = "SpotPrice"
    table_chinese_name = u"现货价格"
    
    def output(self):
        print("SpotPrice")
    
    def get_relevant_df(self, col_list):
        local_col_name_list = spot_price_base.get_all_table_classname()
        col_cls_list = []
        for x in col_list:
            col_cls_name = str(P_Base.get_class_name(x))
            if col_cls_name not in local_col_name_list:
                col_cls_list.append(eval(P_Base.get_table_class_full_variable(x)))
            else:
                col_cls_list.append(eval(col_cls_name))
        ts_list = [x().get_ts() for x in col_cls_list]
        tmp_table_df = pd.concat(ts_list, axis=1).dropna(how="all")
        return tmp_table_df  

    
###########################################################################################################################
""" 国内现货价格 """    

class ZongLvYouXianHuoJiaGe_HuaBei_TianJin(spot_price_base, Manual):
    field_name = u"国内现货价格"
    col_name = u"棕榈油现货价格_华北_天津"
    
class ZongLvYouXianHuoJiaGe_HuaDong_ZhangJiaGang(spot_price_base, Manual):
    field_name = u"国内现货价格"
    col_name = u"棕榈油现货价格_华东_张家港"
    
class ZongLvYouXianHuoJiaGe_HuaDong_ZhenJiang(spot_price_base, Manual):
    field_name = u"国内现货价格"
    col_name = u"棕榈油现货价格_华东_镇江"
    
class ZongLvYouXianHuoJiaGe_HuaDong_TaiXing(spot_price_base, Manual):
    field_name = u"国内现货价格"
    col_name = u"棕榈油现货价格_华东_泰兴"
    
class ZongLvYouXianHuoJiaGe_HuaDong_TaiZhou(spot_price_base, Manual):
    field_name = u"国内现货价格"
    col_name = u"棕榈油现货价格_华东_泰州"
    
class ZongLvYouXianHuoJiaGe_HuaDong_NanTong(spot_price_base, Manual):
    field_name = u"国内现货价格"
    col_name = u"棕榈油现货价格_华东_南通"
    
class ZongLvYouXianHuoJiaGe_HuaDong_GuangZhou(spot_price_base, Manual):
    field_name = u"国内现货价格"
    col_name = u"棕榈油现货价格_华东_广州"
    
class ZongLvYouXianHuoJiaGe_HuaDong_DongGuan(spot_price_base, Manual):
    field_name = u"国内现货价格"
    col_name = u"棕榈油现货价格_华东_东莞"
    
class ZongLvYouXianHuoJiaGe_HuaNan_YangZhou(spot_price_base, Manual):
    field_name = u"国内现货价格"
    col_name = u"棕榈油现货价格_华南_扬州"
    
class ZongLvYouXianHuoJiaGe_HuaNan_YiZheng(spot_price_base, Manual):
    field_name = u"国内现货价格"
    col_name = u"棕榈油现货价格_华南_仪征"
    



if __name__ == "__main__":
    ts = PeHuaQiChuChangJia_JingBoShiHua().get_ts()