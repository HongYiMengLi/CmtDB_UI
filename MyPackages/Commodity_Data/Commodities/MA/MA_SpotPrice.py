# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 16:35:12 2018

@author: 李弘一萌
"""

import pandas as pd
from datetime import datetime
from .MA_Base import MA_Base
from ...Base.DataType_Base import Manual, Computed, WindData
from ...Base.Plot_Base import Plot_Base
from matplotlib.ticker import FuncFormatter

class spot_price_base(MA_Base, Plot_Base):
    table_english_name = "SpotPrice"
    table_chinese_name = u"现货价格"
#    original_db_filepath = data_path + u"LPP价格数据库.xlsx"
    
    def output(self):
        print("SpotPrice")
    
    def get_relevant_df(self, col_list):
        local_col_name_list = spot_price_base.get_all_table_classname()
        col_cls_list = []
        for x in col_list:
            col_cls_name = str(MA_Base.get_class_name(x))
            if col_cls_name not in local_col_name_list:
                col_cls_list.append(eval(MA_Base.get_table_class_full_variable(x)))
            else:
                col_cls_list.append(eval(col_cls_name))
        ts_list = [x().get_ts() for x in col_cls_list]
        tmp_table_df = pd.concat(ts_list, axis=1).dropna(how="all")
        return tmp_table_df  

    
###########################################################################################################################
""" 国内现货 """    



class JiaChunJiaGe_JiangSu(spot_price_base, Manual):
    field_name = u"国内现货"
    col_name = u"甲醇价格_江苏"
    
class JiaChunJiaGe_ZheJiang(spot_price_base, Manual):
    field_name = u"国内现货"
    col_name = u"甲醇价格_浙江"

class JiaChunJiaGe_FuJian(spot_price_base, Manual):
    field_name = u"国内现货"
    col_name = u"甲醇价格_福建"
    
class JiaChunJiaGe_GuangDong(spot_price_base, Manual):
    field_name = u"国内现货"
    col_name = u"甲醇价格_广东"

class JiaChunJiaGe_ShanXi(spot_price_base, Manual):
    field_name = u"国内现货"
    col_name = u"甲醇价格_山西"

class JiaChunJiaGe_HeBei(spot_price_base, Manual):
    field_name = u"国内现货"
    col_name = u"甲醇价格_河北"

class JiaChunJiaGe_LuNan(spot_price_base, Manual):
    field_name = u"国内现货"
    col_name = u"甲醇价格_鲁南"

class JiaChunJiaGe_HeNan(spot_price_base, Manual):
    field_name = u"国内现货"
    col_name = u"甲醇价格_河南"

class JiaChunJiaGe_LiangHu(spot_price_base, Manual):
    field_name = u"国内现货"
    col_name = u"甲醇价格_两湖"

class JiaChunJiaGe_ShanXii(spot_price_base, Manual):
    field_name = u"国内现货"
    col_name = u"甲醇价格_陕西"

class JiaChunJiaGe_NeiMengGu(spot_price_base, Manual):
    field_name = u"国内现货"
    col_name = u"甲醇价格_内蒙古" 

class JiaChunJiaGe_LinYi(spot_price_base, Manual):
    field_name = u"国内现货"
    col_name = u"甲醇价格_临沂" 
    
class JiaChunJiaGe_JiZhun(spot_price_base, Computed):
    field_name = u"国内现货"
    col_name = u"甲醇价格_基准"
    def get_ts_whole_progress(self):
        relevant_col_list = [u"甲醇价格_江苏", u"甲醇价格_广东", u"甲醇价格_福建", u"甲醇价格_河北", u"甲醇价格_临沂", u"甲醇价格_河南", u"甲醇价格_内蒙古"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[u"甲醇价格_河北"] = tmp_total[u"甲醇价格_河北"] + 260
        tmp_total[u"甲醇价格_临沂"] = tmp_total[u"甲醇价格_临沂"] + 200
        tmp_total[u"甲醇价格_河南"] = tmp_total[u"甲醇价格_河南"] + 200
        tmp_total[u"甲醇价格_内蒙古"] = tmp_total[u"甲醇价格_内蒙古"] + 600
        tmp_total[self.col_name] = tmp_total.min(axis=1)
        return tmp_total    
###########################################################################################################################
""" 美金盘 """      

class JiaChunJiaGe_CFR_ZhongGuo(spot_price_base, Manual):
    field_name = u"美金盘"
    col_name = u"甲醇价格_CFR_中国"

class JiaChunJiaGe_CFR_DongNanYa(spot_price_base, Manual):
    field_name = u"美金盘"
    col_name = u"甲醇价格_CFR_东南亚"
    
class JiaChunJiaGe_FOB_MeiWan(spot_price_base, Manual):
    field_name = u"美金盘"
    col_name = u"甲醇价格_FOB_美湾"

class JiaChunJiaGe_CFR_LuTeDan(spot_price_base, Manual):
    field_name = u"美金盘"
    col_name = u"甲醇价格_CFR_鹿特丹"
    
    
    
    
    
    
    
    



if __name__ == "__main__":
    ts = JiaChunJiaGe_JiZhun().get_ts()