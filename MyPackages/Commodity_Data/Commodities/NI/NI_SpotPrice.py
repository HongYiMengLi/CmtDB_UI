# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 16:35:12 2018

@author: 李弘一萌
"""

import pandas as pd
from datetime import datetime
from .NI_Base import NI_Base
from ...Base.DataType_Base import Manual, Computed, WindData
from ...Base.Plot_Base import Plot_Base
from matplotlib.ticker import FuncFormatter

class spot_price_base(NI_Base, Plot_Base):
    table_english_name = "SpotPrice"
    table_chinese_name = u"现货价格"
    
    def output(self):
        print("SpotPrice")
    
    def get_relevant_df(self, col_list):
        local_col_name_list = spot_price_base.get_all_table_classname()
        col_cls_list = []
        for x in col_list:
            col_cls_name = str(NI_Base.get_class_name(x))
            if col_cls_name not in local_col_name_list:
                col_cls_list.append(eval(NI_Base.get_table_class_full_variable(x)))
            else:
                col_cls_list.append(eval(col_cls_name))
        ts_list = [x().get_ts() for x in col_cls_list]
        tmp_table_df = pd.concat(ts_list, axis=1).dropna(how="all")
        return tmp_table_df  
    
###########################################################################################################################
""" 电解镍价格 """    

class No1DianJieNieJiaGe_ChangJiangYouSeShiChang_ZuiDiJia(spot_price_base, WindData):
    field_name = u"电解镍价格"
    col_name = u"1#电解镍价格_长江有色市场_最低价(含税)"
    wind_code = "S5810894"
    
class No1DianJieNieJiaGe_ChangJiangYouSeShiChang_PingJunJia(spot_price_base, WindData):
    field_name = u"电解镍价格"
    col_name = u"1#电解镍价格_长江有色市场_平均价"
    wind_code = "S5807008"
    
class No1DianJieNieJiaGe_GuangDongNanChu_PingJunJia_JinChuan_FoShanCangKu(spot_price_base, WindData):
    field_name = u"电解镍价格"
    col_name = u"1#电解镍价格_广东南储_平均价_金川_佛山仓库"
    wind_code = "S0048090"
    
    
###########################################################################################################################
""" 镍铁价格 """      

class DiNieTieHanShuiJia_1Dot5To1Dot8Prct_ShanXi(spot_price_base, WindData):
    field_name = u"镍铁价格"
    col_name = u"低镍铁含税价_1.5-1.8%_山西"
    wind_code = "S5811532"    

class DiNieTieHanShuiJia_DiNieTie_1Dot5To1Dot8Prct_LiaoNing(spot_price_base, WindData):
    field_name = u"镍铁价格"
    col_name = u"低镍铁含税价_低镍铁_1.5-1.8%_辽宁"
    wind_code = "S5811533"    

class DiNieTieHanShuiJia_DiNieTie_1Dot5To1Dot8Prct_JiangSu(spot_price_base, WindData):
    field_name = u"镍铁价格"
    col_name = u"低镍铁含税价_低镍铁_1.5-1.8%_江苏"
    wind_code = "S5811534"    

class DiNieTieHanShuiJia_DiNieTie_1Dot5To1Dot8Prct_ShanDong(spot_price_base, WindData):
    field_name = u"镍铁价格"
    col_name = u"低镍铁含税价_低镍铁_1.5-1.8%_山东"
    wind_code = "S5811535"    

class DiNieTieHanShuiJia_DiNieTie_1Dot5To1Dot8Prct_GuangXi(spot_price_base, WindData):
    field_name = u"镍铁价格"
    col_name = u"低镍铁含税价_低镍铁_1.5-1.8%_广西"
    wind_code = "S5811536"    

class DiNieTieHanShuiJia_DiNieTie_1Dot5To1Dot8Prct_HeBei(spot_price_base, WindData):
    field_name = u"镍铁价格"
    col_name = u"低镍铁含税价_低镍铁_1.5-1.8%_河北"
    wind_code = "S5811537"    

class GaoLuNieTieHanShuiJia_4To6Prct_ShanXi(spot_price_base, WindData):
    field_name = u"镍铁价格"
    col_name = u"高炉镍铁含税价_4-6%_山西"
    wind_code = "S5811538"    

class GaoLuNieTieHanShuiJia_GaoLuNieTie_4To6Prct_ShanDong(spot_price_base, WindData):
    field_name = u"镍铁价格"
    col_name = u"高炉镍铁含税价_高炉镍铁_4-6%_山东"
    wind_code = "S5811539"    

class GaoLuNieTieHanShuiJia_GaoLuNieTie_4To6Prct_JiangSu(spot_price_base, WindData):
    field_name = u"镍铁价格"
    col_name = u"高炉镍铁含税价_高炉镍铁_4-6%_江苏"
    wind_code = "S5811540"    

class GaoNieTieHanShuiJia_7To10Prct_NeiMeng(spot_price_base, WindData):
    field_name = u"镍铁价格"
    col_name = u"高镍铁含税价_7-10%_内蒙"
    wind_code = "S5811528"    

class GaoNieTieHanShuiJia_GaoNieTie_7To10Prct_JiangSu(spot_price_base, WindData):
    field_name = u"镍铁价格"
    col_name = u"高镍铁含税价_高镍铁_7-10%_江苏"
    wind_code = "S5811529"    

class GaoNieTieHanShuiJia_GaoNieTie_7To10Prct_LiaoNing(spot_price_base, WindData):
    field_name = u"镍铁价格"
    col_name = u"高镍铁含税价_高镍铁_7-10%_辽宁"
    wind_code = "S5811530"    

class GaoNieTieHanShuiJia_GaoNieTie_7To10Prct_ShanDong(spot_price_base, WindData):
    field_name = u"镍铁价格"
    col_name = u"高镍铁含税价_高镍铁_7-10%_山东"
    wind_code = "S5811531"    


    

if __name__ == "__main__":
    ts = PNIXianHuoJiaGe_HuaDong().get_ts()