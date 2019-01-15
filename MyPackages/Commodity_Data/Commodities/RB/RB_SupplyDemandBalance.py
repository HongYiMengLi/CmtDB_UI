# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 10:48:40 2018

@author: 李弘一萌
"""

import pandas as pd
from datetime import datetime
from .RB_Base import RB_Base
from ...Base.DataType_Base import Manual, Computed, WindData
from ...Base.Plot_Base import Plot_Base
from matplotlib.ticker import FuncFormatter

class sdb_base(RB_Base, Plot_Base):
    table_english_name = "SupplyDemandBalance"
    table_chinese_name = u"供需平衡表"
    
    def output(self):
        print(self.table_english_name)
    
    def get_relevant_df(self, col_list):
        local_col_name_list = sdb_base.get_all_table_classname()
        col_cls_list = []
        for x in col_list:
            col_cls_name = str(RB_Base.get_class_name(x))
            if col_cls_name not in local_col_name_list:
                col_cls_list.append(eval(RB_Base.get_table_class_full_variable(x)))
            else:
                col_cls_list.append(eval(col_cls_name))
        ts_list = [x().get_ts() for x in col_cls_list]
        tmp_table_df = pd.concat(ts_list, axis=1).dropna(how="all")
        return tmp_table_df 



###########################################################################################################################
""" 出口量 """    

class LuoWenChuKouLiang_DangYueZhi(sdb_base, WindData):
    field_name = u"出口量"
    col_name = u"螺纹出口量_当月值"    
    wind_code = "S0060227" 


    
###########################################################################################################################
""" 粗钢产量 """  

class CuGangRiJunChanLiang_ZhongDianQiYe(sdb_base, WindData):
    field_name = u"粗钢产量"
    col_name = u"粗钢日均产量_重点企业"    
    wind_code = "S5708246"
    
    
class CuGangChanLiang_DangYueZhi(sdb_base, WindData):
    field_name = u"粗钢产量"
    col_name = u"粗钢产量_当月值"    
    wind_code = "S0027374"


    
class CuGang_ShengTieChanLiangBi(sdb_base, Computed):
    field_name = u"粗钢产量"
    col_name = u"粗钢-生铁产量比"
    
    def get_ts_whole_progress(self):
        relevant_col_list = [u"粗钢产量_当月值", u"生铁产量_当月值"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"粗钢产量_当月值"] / tmp_total[u"生铁产量_当月值"]
        return tmp_total

###########################################################################################################################
""" 钢铁需求 """  

class CuGangXuQiuLiang_JianZhuXingYe(sdb_base, Manual):
    field_name = u"钢铁需求"
    col_name = u"粗钢需求量_建筑行业"    

###########################################################################################################################
""" 高炉生产 """  

class MysteelQuanGuoGangChangGaoLuChanNengLiYongLv(sdb_base, Manual):
    field_name = u"高炉生产"
    col_name = u"Mysteel全国钢厂高炉产能利用率"  

class GaoLuKaiGongLv_QuanGuo(sdb_base, WindData):
    field_name = u"高炉生产"
    col_name = u"高炉开工率_全国"    
    wind_code = "S5708175"

class YingLiGangChangBiLv_QuanGuo(sdb_base, WindData):
    field_name = u"高炉生产"
    col_name = u"盈利钢厂比率_全国"    
    wind_code = "S5708339"

class GaoLuKaiGongLv_TangShan(sdb_base, WindData):
    field_name = u"高炉生产"
    col_name = u"高炉开工率_唐山"    
    wind_code = "S5707135"

class ShengTieChanLiang_DangYueZhi(sdb_base, WindData):
    field_name = u"高炉生产"
    col_name = u"生铁产量_当月值"    
    wind_code = "S0027370"

###########################################################################################################################
""" 螺纹产量 """  

class LuoWenGangZhouChanLiang(sdb_base, Manual):
    field_name = u"螺纹产量"
    col_name = u"螺纹钢周产量"  
    
    
    

if __name__ == "__main__":
    a = PRBSheHuiKuCun().seasonal_plot()
    
    
    
    
    
    
    
    
    
    