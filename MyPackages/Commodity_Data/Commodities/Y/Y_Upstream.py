# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 10:44:58 2018

@author: 李弘一萌
"""

import pandas as pd
from datetime import datetime
from .Y_Base import Y_Base
from ...Base.DataType_Base import Manual, Computed, WindData
from ...Base.Plot_Base import Plot_Base
from matplotlib.ticker import FuncFormatter

class upstream_base(Y_Base, Plot_Base):
    table_english_name = "Upstream"
    table_chinese_name = u"上游"
    
    def output(self):
        print("Upstream")
    
    def get_relevant_df(self, col_list):
        local_col_name_list = upstream_base.get_all_table_classname()
        col_cls_list = []
        for x in col_list:
            col_cls_name = str(Y_Base.get_class_name(x))
            if col_cls_name not in local_col_name_list:
                col_cls_list.append(eval(Y_Base.get_table_class_full_variable(x)))
            else:
                col_cls_list.append(eval(col_cls_name))
        ts_list = [x().get_ts() for x in col_cls_list]
        tmp_table_df = pd.concat(ts_list, axis=1).dropna(how="all")
        return tmp_table_df

###########################################################################################################################
""" 进口价格 """  

class DouYouJinKouJia_BaXi(upstream_base, Manual):
    field_name = u"进口价格"
    col_name = u"豆油进口价_巴西"


class DouYouJinKouJia_AGenTing(upstream_base, Manual):
    field_name = u"进口价格"
    col_name = u"豆油进口价_阿根廷"
    


    
###########################################################################################################################
""" 盘面进口利润 """  

class DouYouJinKouLiRun(upstream_base, Manual):
    field_name = u"盘面进口利润"
    col_name = u"豆油进口利润"








    
    
if __name__ == "__main__":
    df = MianHuaGongJianJinDu_YueDuLeiJi().get_ts()    
    
    
    
    
    
    
    
    
    
    
    
    
    
    