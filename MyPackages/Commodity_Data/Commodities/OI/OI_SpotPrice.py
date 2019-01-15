# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 16:35:12 2018

@author: 李弘一萌
"""

import pandas as pd
from datetime import datetime
from .OI_Base import OI_Base
from ...Base.DataType_Base import Manual, Computed, WindData
from ...Base.Plot_Base import Plot_Base
from matplotlib.ticker import FuncFormatter

class spot_price_base(OI_Base, Plot_Base):
    table_english_name = "SpotPrice"
    table_chinese_name = u"现货价格"
    
    def output(self):
        print("SpotPrice")
    
    def get_relevant_df(self, col_list):
        local_col_name_list = spot_price_base.get_all_table_classname()
        col_cls_list = []
        for x in col_list:
            col_cls_name = str(OI_Base.get_class_name(x))
            if col_cls_name not in local_col_name_list:
                col_cls_list.append(eval(OI_Base.get_table_class_full_variable(x)))
            else:
                col_cls_list.append(eval(col_cls_name))
        ts_list = [x().get_ts() for x in col_cls_list]
        tmp_table_df = pd.concat(ts_list, axis=1).dropna(how="all")
        return tmp_table_df  

    
###########################################################################################################################
""" 国内现货价格 """    

class CaiYouXianHuoJiaGe_HuaDong_TaiZhou(spot_price_base, Manual):
    field_name = u"国内现货价格"
    col_name = u"菜油现货价格_华东_泰州"
    
class CaiYouXianHuoJiaGe_HuaDong_NanJing(spot_price_base, Manual):
    field_name = u"国内现货价格"
    col_name = u"菜油现货价格_华东_南京"
    
class CaiYouXianHuoJiaGe_HuaDong_ZhangJiaGang(spot_price_base, Manual):
    field_name = u"国内现货价格"
    col_name = u"菜油现货价格_华东_张家港"
    
class CaiYouXianHuoJiaGe_HuaDong_ZhenJiang(spot_price_base, Manual):
    field_name = u"国内现货价格"
    col_name = u"菜油现货价格_华东_镇江"
    
class CaiYouXianHuoJiaGe_HuaZhong_HeFei(spot_price_base, Manual):
    field_name = u"国内现货价格"
    col_name = u"菜油现货价格_华中_合肥"
    
class CaiYouXianHuoJiaGe_HuaZhong_WuHan(spot_price_base, Manual):
    field_name = u"国内现货价格"
    col_name = u"菜油现货价格_华中_武汉"
    
class CaiYouXianHuoJiaGe_HuaZhong_ZhongXiang(spot_price_base, Manual):
    field_name = u"国内现货价格"
    col_name = u"菜油现货价格_华中_钟祥"
    
class CaiYouXianHuoJiaGe_HuaNan_DongGuan(spot_price_base, Manual):
    field_name = u"国内现货价格"
    col_name = u"菜油现货价格_华南_东莞"
    
class CaiYouXianHuoJiaGe_HuaNan_FangChengGang(spot_price_base, Manual):
    field_name = u"国内现货价格"
    col_name = u"菜油现货价格_华南_防城港"
    
class CaiYouXianHuoJiaGe_HuaNan_ZhanJiang(spot_price_base, Manual):
    field_name = u"国内现货价格"
    col_name = u"菜油现货价格_华南_湛江"
    
class CaiYouXianHuoJiaGe_HuaNan_QinZhou(spot_price_base, Manual):
    field_name = u"国内现货价格"
    col_name = u"菜油现货价格_华南_钦州"
    
class CaiYouXianHuoJiaGe_HuaNan_ZhangZhou(spot_price_base, Manual):
    field_name = u"国内现货价格"
    col_name = u"菜油现货价格_华南_漳州"
    
class CaiYouXianHuoJiaGe_HuaNan_FuZhou(spot_price_base, Manual):
    field_name = u"国内现货价格"
    col_name = u"菜油现货价格_华南_福州"
    
class CaiYouXianHuoJiaGe_HuaNan_XiaMen(spot_price_base, Manual):
    field_name = u"国内现货价格"
    col_name = u"菜油现货价格_华南_厦门"
    
class CaiYouXianHuoJiaGe_XiNan_ChengDu(spot_price_base, Manual):
    field_name = u"国内现货价格"
    col_name = u"菜油现货价格_西南_成都"
    
class CaiYouXianHuoJiaGe_XiNan_GuangHan(spot_price_base, Manual):
    field_name = u"国内现货价格"
    col_name = u"菜油现货价格_西南_广汉"
    
class CaiYouXianHuoJiaGe_XiNan_ZhongQing(spot_price_base, Manual):
    field_name = u"国内现货价格"
    col_name = u"菜油现货价格_西南_重庆"
    
class CaiYouXianHuoJiaGe_XiNan_DeYang(spot_price_base, Manual):
    field_name = u"国内现货价格"
    col_name = u"菜油现货价格_西南_德阳"
    
class CaiYouXianHuoJiaGe_XiBei_PingYang(spot_price_base, Manual):
    field_name = u"国内现货价格"
    col_name = u"菜油现货价格_西北_平阳"
    


if __name__ == "__main__":
    ts = OIeHuaQiChuChangJia_JingBoShiHua().get_ts()