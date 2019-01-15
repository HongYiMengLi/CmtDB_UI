# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 16:35:12 2018

@author: 李弘一萌
"""

import pandas as pd
from datetime import datetime
from .CF_Base import CF_Base
from ...Base.DataType_Base import Manual, Computed, WindData
from ...Base.Plot_Base import Plot_Base
from matplotlib.ticker import FuncFormatter

class spot_price_base(CF_Base, Plot_Base):
    table_english_name = "SpotPrice"
    table_chinese_name = u"现货价格"
#    original_db_filepath = data_path + u"LPP价格数据库.xlsx"
    
    def output(self):
        print("SpotPrice")
    
    def get_relevant_df(self, col_list):
        local_col_name_list = spot_price_base.get_all_table_classname()
        col_cls_list = []
        for x in col_list:
            col_cls_name = str(CF_Base.get_class_name(x))
            if col_cls_name not in local_col_name_list:
                col_cls_list.append(eval(CF_Base.get_table_class_full_variable(x)))
            else:
                col_cls_list.append(eval(col_cls_name))
        ts_list = [x().get_ts() for x in col_cls_list]
        tmp_table_df = pd.concat(ts_list, axis=1).dropna(how="all")
        return tmp_table_df  

    
###########################################################################################################################
""" 分省到厂价 """    

class MianHuaXianHuoJiaGe_AnHui(spot_price_base, Manual):
    field_name = u"分省到厂价"
    col_name = u"棉花现货价格_安徽"
    
class MianHuaXianHuoJiaGe_HeBei(spot_price_base, Manual):
    field_name = u"分省到厂价"
    col_name = u"棉花现货价格_河北"

class MianHuaXianHuoJiaGe_GuangDong(spot_price_base, Manual):
    field_name = u"分省到厂价"
    col_name = u"棉花现货价格_广东"

class MianHuaXianHuoJiaGe_HeNan(spot_price_base, Manual):
    field_name = u"分省到厂价"
    col_name = u"棉花现货价格_河南"

class MianHuaXianHuoJiaGe_HuBei(spot_price_base, Manual):
    field_name = u"分省到厂价"
    col_name = u"棉花现货价格_湖北"

class MianHuaXianHuoJiaGe_HuNan(spot_price_base, Manual):
    field_name = u"分省到厂价"
    col_name = u"棉花现货价格_湖南"
    
class MianHuaXianHuoJiaGe_JiangSu(spot_price_base, Manual):
    field_name = u"分省到厂价"
    col_name = u"棉花现货价格_江苏"

class MianHuaXianHuoJiaGe_ShanDong(spot_price_base, Manual):
    field_name = u"分省到厂价"
    col_name = u"棉花现货价格_山东"

class MianHuaXianHuoJiaGe_ShanXi(spot_price_base, Manual):
    field_name = u"分省到厂价"
    col_name = u"棉花现货价格_山西"

class MianHuaXianHuoJiaGe_ShanXii(spot_price_base, Manual):
    field_name = u"分省到厂价"
    col_name = u"棉花现货价格_陕西"

class MianHuaXianHuoJiaGe_JiangXi(spot_price_base, Manual):
    field_name = u"分省到厂价"
    col_name = u"棉花现货价格_江西"

class MianHuaXianHuoJiaGe_ZheJiang(spot_price_base, Manual):
    field_name = u"分省到厂价"
    col_name = u"棉花现货价格_浙江"

class MianHuaXianHuoJiaGe_ZhongQing(spot_price_base, Manual):
    field_name = u"分省到厂价"
    col_name = u"棉花现货价格_重庆"

class MianHuaXianHuoJiaGe_FuJian(spot_price_base, Manual):
    field_name = u"分省到厂价"
    col_name = u"棉花现货价格_福建"

class MianHuaXianHuoJiaGe_SiChuan(spot_price_base, Manual):
    field_name = u"分省到厂价"
    col_name = u"棉花现货价格_四川"

class MianHuaXianHuoJiaGe_XinJiang(spot_price_base, Manual):
    field_name = u"分省到厂价"
    col_name = u"棉花现货价格_新疆"

class MianHuaXianHuoJiaGe_GanSu(spot_price_base, Manual):
    field_name = u"分省到厂价"
    col_name = u"棉花现货价格_甘肃"





if __name__ == "__main__":
    ts = YeHuaQiChuChangJia_JingBoShiHua().get_ts()