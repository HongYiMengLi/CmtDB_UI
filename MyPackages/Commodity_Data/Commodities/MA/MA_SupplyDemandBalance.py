# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 10:48:40 2018

@author: 李弘一萌
"""

import pandas as pd
from datetime import datetime
from .MA_Base import MA_Base
from ...Base.DataType_Base import Manual, Computed, WindData
from ...Base.Plot_Base import Plot_Base
from matplotlib.ticker import FuncFormatter

class sdb_base(MA_Base, Plot_Base):
    table_english_name = "SupplyDemandBalance"
    table_chinese_name = u"供需平衡表"
    
    def output(self):
        print(self.table_english_name)
    
    def get_relevant_df(self, col_list):
        local_col_name_list = sdb_base.get_all_table_classname()
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
""" 港口库存 """    

class JiaChunGangKouKuCun(sdb_base, Manual):
    field_name = u"港口库存"
    col_name = u"甲醇港口库存"
    start_year = 2014
    
###########################################################################################################################
""" 开工率 """  

class JiaChunKaiGongLv_ZhuoChuang(sdb_base, Manual):
    field_name = u"开工率"
    col_name = u"甲醇开工率_卓创"

class JiaChunKaiGongLv_JinLianChuang(sdb_base, Manual):
    field_name = u"开工率"
    col_name = u"甲醇开工率_金联创"


###########################################################################################################################
""" 月度产量 """  

class JiaChunChanLiang(sdb_base, WindData):
    field_name = u"月度产量"
    col_name = u"甲醇产量"
    wind_code = "S0027167"

###########################################################################################################################
""" 净进口 """  

class JiaChunJinKouLiang(sdb_base, WindData):
    field_name = u"净进口"
    col_name = u"甲醇进口量"
    wind_code = "S5401698"
    
###########################################################################################################################
""" 需求 """  

class JiaQuanChanLiang(sdb_base, WindData):
    field_name = u"需求"
    col_name = u"甲醛产量"
    wind_code = "S5437613"

class ErJiaMiChanLiang(sdb_base, WindData):
    field_name = u"需求"
    col_name = u"二甲醚产量"
    wind_code = "S5123789"

class CuSuanChanLiang(sdb_base, WindData):
    field_name = u"需求"
    col_name = u"醋酸产量"
    wind_code = "S0070163"

    
if __name__ == "__main__":
    a = JiaChunJinKouLiang().get_ts()
    
    
    
    
    
    
    
    
    
    