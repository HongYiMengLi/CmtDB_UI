# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 16:35:12 2018

@author: 李弘一萌
"""

import pandas as pd
from datetime import datetime
from .M_Base import M_Base
from ...Base.DataType_Base import Manual, Computed, WindData
from ...Base.Plot_Base import Plot_Base
from matplotlib.ticker import FuncFormatter

class spot_price_base(M_Base, Plot_Base):
    table_english_name = "SpotPrice"
    table_chinese_name = u"现货价格"
#    original_db_filepath = data_path + u"LPP价格数据库.xlsx"
    
    def output(self):
        print("SpotPrice")
    
    def get_relevant_df(self, col_list):
        local_col_name_list = spot_price_base.get_all_table_classname()
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
""" 国内现货价格 """    

class DouPoXianHuoJiaGe_ZhangJiaGang(spot_price_base, Manual):
    field_name = u"国内现货价格"
    col_name = u"豆粕现货价格_张家港"
    
class DouPoXianHuoJiaGe_NanTong(spot_price_base, Manual):
    field_name = u"国内现货价格"
    col_name = u"豆粕现货价格_南通"
    
class DouPoXianHuoJiaGe_NanJing(spot_price_base, Manual):
    field_name = u"国内现货价格"
    col_name = u"豆粕现货价格_南京"
    
class DouPoXianHuoJiaGe_TianJin(spot_price_base, Manual):
    field_name = u"国内现货价格"
    col_name = u"豆粕现货价格_天津"
    
class DouPoXianHuoJiaGe_RiZhao(spot_price_base, Manual):
    field_name = u"国内现货价格"
    col_name = u"豆粕现货价格_日照"
       
class DouPoXianHuoJiaGe_ZhenJiang(spot_price_base, Manual):
    field_name = u"国内现货价格"
    col_name = u"豆粕现货价格_镇江"
    
class DouPoXianHuoJiaGe_LianYunGang(spot_price_base, Manual):
    field_name = u"国内现货价格"
    col_name = u"豆粕现货价格_连云港"
    
class DouPoXianHuoJiaGe_TaiZhou(spot_price_base, Manual):
    field_name = u"国内现货价格"
    col_name = u"豆粕现货价格_泰州"
    
class DouPoXianHuoJiaGe_TaiXing(spot_price_base, Manual):
    field_name = u"国内现货价格"
    col_name = u"豆粕现货价格_泰兴"
    
class DouPoXianHuoJiaGe_DongGuan(spot_price_base, Manual):
    field_name = u"国内现货价格"
    col_name = u"豆粕现货价格_东莞"
    
class DouPoXianHuoJiaGe_ZhanJiang(spot_price_base, Manual):
    field_name = u"国内现货价格"
    col_name = u"豆粕现货价格_湛江"
    
class DouPoXianHuoJiaGe_YangJiang(spot_price_base, Manual):
    field_name = u"国内现货价格"
    col_name = u"豆粕现货价格_阳江"
    


if __name__ == "__main__":
    ts = YeHuaQiChuChangJia_JingBoShiHua().get_ts()