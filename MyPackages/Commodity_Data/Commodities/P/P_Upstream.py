# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 10:44:58 2018

@author: 李弘一萌
"""

import pandas as pd
from datetime import datetime
from .P_Base import P_Base
from ...Base.DataType_Base import Manual, Computed, WindData
from ...Base.Plot_Base import Plot_Base
from matplotlib.ticker import FuncFormatter

class upstream_base(P_Base, Plot_Base):
    table_english_name = "Upstream"
    table_chinese_name = u"上游"
    
    def output(self):
        print("Upstream")
    
    def get_relevant_df(self, col_list):
        local_col_name_list = upstream_base.get_all_table_classname()
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
""" 马来西亚产量 """ 

class ZongLvYouChanLiang_MaLaiXiYa(upstream_base, Manual):
    field_name = u"马来西亚产量"
    col_name = u"棕榈油产量_马来西亚"

###########################################################################################################################
""" 马来西亚出口 """ 
    
class ZongLvYouChuKouLiang_MaLaiXiYa(upstream_base, Manual):
    field_name = u"马来西亚出口"
    col_name = u"棕榈油出口量_马来西亚"

###########################################################################################################################
""" 马来西亚库存 """ 	
class ZongLvYouKuCun_MaLaiXiYa(upstream_base, Manual):
    field_name = u"马来西亚库存"
    col_name = u"棕榈油库存_马来西亚"

###########################################################################################################################
""" 马来西亚进口 """ 
class ZongLvYouJinKouJia_MaLaiXiYa(upstream_base, Manual):
    field_name = u"马来西亚进口"
    col_name = u"棕榈油进口价_马来西亚"    

###########################################################################################################################
""" 盘面进口利润 """ 
class ZongLvYouJinKouLiRun_YinNi(upstream_base, Manual):
    field_name = u"盘面进口利润"
    col_name = u"棕榈油进口利润_印尼"  






    
    
if __name__ == "__main__":
    df = MianHuaGongJianJinDu_YueDuLeiJi().get_ts()    
    
    
    
    
    
    
    
    
    
    
    
    
    
    