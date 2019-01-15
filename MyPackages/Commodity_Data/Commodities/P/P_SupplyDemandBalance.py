# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 10:48:40 2018

@author: 李弘一萌
"""

import pandas as pd
from datetime import datetime
from .P_Base import P_Base
from ...Base.DataType_Base import Manual, Computed, WindData
from ...Base.Plot_Base import Plot_Base
from matplotlib.ticker import FuncFormatter

class sdb_base(P_Base, Plot_Base):
    table_english_name = "SupplyDemandBalance"
    table_chinese_name = u"供需平衡表"
    
    def output(self):
        print(self.table_english_name)
    
    def get_relevant_df(self, col_list):
        local_col_name_list = sdb_base.get_all_table_classname()
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
""" 到港量情况 """    

class ZongLvYou_DaoGangLiang(sdb_base, Manual):
    field_name = u"到港量情况"
    col_name = u"棕榈油_到港量"


        
###########################################################################################################################
""" 棕榈油供需_年度 """  

class ZongLvYou_QiChuKuCun(sdb_base, Manual):
    field_name = u"棕榈油供需_年度"
    col_name = u"棕榈油_期初库存"

class ZongLvYou_JinKouLiang(sdb_base, Manual):
    field_name = u"棕榈油供需_年度"
    col_name = u"棕榈油_进口量"

class ZongLvYou_ZongGongYingLiang(sdb_base, Manual):
    field_name = u"棕榈油供需_年度"
    col_name = u"棕榈油_总供应量"

class ZongLvYou_GuoNeiShiYongLiang(sdb_base, Manual):
    field_name = u"棕榈油供需_年度"
    col_name = u"棕榈油_国内使用量"

class ZongLvYou_ShiYongXiaoHao(sdb_base, Manual):
    field_name = u"棕榈油供需_年度"
    col_name = u"棕榈油_食用消耗"

class ZongLvYou_QiTaXiaoHao(sdb_base, Manual):
    field_name = u"棕榈油供需_年度"
    col_name = u"棕榈油_其他消耗"

class ZongLvYou_NianDuChuKouLiang(sdb_base, Manual):
    field_name = u"棕榈油供需_年度"
    col_name = u"棕榈油_年度出口量"

class ZongLvYou_QiMoKuCun(sdb_base, Manual):
    field_name = u"棕榈油供需_年度"
    col_name = u"棕榈油_期末库存"


###########################################################################################################################
""" 棕榈油供需_月度 """  

class ShiYongZongLvYou_QiChuKuCun(sdb_base, Manual):
    field_name = u"棕榈油供需_月度"
    col_name = u"食用棕榈油_期初库存"

class ShiYongZongLvYou_JinKouLiang(sdb_base, Manual):
    field_name = u"棕榈油供需_月度"
    col_name = u"食用棕榈油_进口量"

class ShiYongZongLvYou_ZongGongYingLiang(sdb_base, Manual):
    field_name = u"棕榈油供需_月度"
    col_name = u"食用棕榈油_总供应量"

class ShiYongZongLvYou_GuoNeiShiYongLiang(sdb_base, Manual):
    field_name = u"棕榈油供需_月度"
    col_name = u"食用棕榈油_国内使用量"

class ShiYongZongLvYou_QiMoKuCun(sdb_base, Manual):
    field_name = u"棕榈油供需_月度"
    col_name = u"食用棕榈油_期末库存"


    
if __name__ == "__main__":
    a = JiaChunJinKouLiang().get_ts()
    
    
    
    
    
    
    
    
    
    