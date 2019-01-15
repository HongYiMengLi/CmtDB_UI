# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 10:48:40 2018

@author: 李弘一萌
"""

import pandas as pd
from datetime import datetime
from .OI_Base import OI_Base
from ...Base.DataType_Base import Manual, Computed, WindData
from ...Base.Plot_Base import Plot_Base
from matplotlib.ticker import FuncFormatter

class sdb_base(OI_Base, Plot_Base):
    table_english_name = "SupplyDemandBalance"
    table_chinese_name = u"供需平衡表"
    
    def output(self):
        print(self.table_english_name)
    
    def get_relevant_df(self, col_list):
        local_col_name_list = sdb_base.get_all_table_classname()
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
""" 菜油供需_年度 """    

class CaiYou_QiChuKuCun(sdb_base, Manual):
    field_name = u"菜油供需_年度"
    col_name = u"菜油_期初库存"

class CaiYou_GuoNeiChanLiang(sdb_base, Manual):
    field_name = u"菜油供需_年度"
    col_name = u"菜油_国内产量"

class CaiYou_JinKouLiang(sdb_base, Manual):
    field_name = u"菜油供需_年度"
    col_name = u"菜油_进口量"

class CaiYou_ZongGongYingLiang(sdb_base, Manual):
    field_name = u"菜油供需_年度"
    col_name = u"菜油_总供应量"

class CaiYou_ZongXiaoFeiLiang(sdb_base, Manual):
    field_name = u"菜油供需_年度"
    col_name = u"菜油_总消费量"

class CaiYou_QiMoKuCun(sdb_base, Manual):
    field_name = u"菜油供需_年度"
    col_name = u"菜油_期末库存"

     
    
###########################################################################################################################
""" 油菜籽供需_年度 """  

class YouCaiZi_QiChuKuCun(sdb_base, Manual):
    field_name = u"油菜籽供需_年度"
    col_name = u"油菜籽_期初库存"
    
class YouCaiZi_GuoNeiChanLiang(sdb_base, Manual):
    field_name = u"油菜籽供需_年度"
    col_name = u"油菜籽_国内产量"
    
class YouCaiZi_JinKouLiang(sdb_base, Manual):
    field_name = u"油菜籽供需_年度"
    col_name = u"油菜籽_进口量"

class YouCaiZi_ZongGongYingLiang(sdb_base, Manual):
    field_name = u"油菜籽供需_年度"
    col_name = u"油菜籽_总供应量"

class YouCaiZi_ZongXiaoFeiLiang(sdb_base, Manual):
    field_name = u"油菜籽供需_年度"
    col_name = u"油菜籽_总消费量"

class YouCaiZi_ZhaYouYongLiang_GuoChanCaiZi(sdb_base, Manual):
    field_name = u"油菜籽供需_年度"
    col_name = u"油菜籽_榨油用量_国产菜籽"

class YouCaiZi_ZhaYouYongLiang_JinKouCaiZi(sdb_base, Manual):
    field_name = u"油菜籽供需_年度"
    col_name = u"油菜籽_榨油用量_进口菜籽"

class YouCaiZi_ZhongYongJiSunHao(sdb_base, Manual):
    field_name = u"油菜籽供需_年度"
    col_name = u"油菜籽_种用及损耗"

class YouCaiZi_QiMoKuCun(sdb_base, Manual):
    field_name = u"油菜籽供需_年度"
    col_name = u"油菜籽_期末库存"

    
if __name__ == "__main__":
    a = JiaChunJinKouLiang().get_ts()
    
    
    
    
    
    
    
    
    
    