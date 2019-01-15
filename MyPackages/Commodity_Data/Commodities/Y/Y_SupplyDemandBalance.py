# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 10:48:40 2018

@author: 李弘一萌
"""

import pandas as pd
from datetime import datetime
from .Y_Base import Y_Base
from ...Base.DataType_Base import Manual, Computed, WindData
from ...Base.Plot_Base import Plot_Base
from matplotlib.ticker import FuncFormatter

class sdb_base(Y_Base, Plot_Base):
    table_english_name = "SupplyDemandBalance"
    table_chinese_name = u"供需平衡表"
    
    def output(self):
        print(self.table_english_name)
    
    def get_relevant_df(self, col_list):
        local_col_name_list = sdb_base.get_all_table_classname()
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
""" 豆油供需_年度 """    

class DouYou_QiChuKuCun_NianDu(sdb_base, Manual):
    field_name = u"豆油供需_年度"
    col_name = u"豆油_期初库存_年度"

class DouYou_GuoNeiChanLiang_NianDu(sdb_base, Manual):
    field_name = u"豆油供需_年度"
    col_name = u"豆油_国内产量_年度"

class DouYou_JinKouLiang_NianDu(sdb_base, Manual):
    field_name = u"豆油供需_年度"
    col_name = u"豆油_进口量_年度"
    
class DouYou_GuoNeiShiYongLiang_NianDu(sdb_base, Manual):
    field_name = u"豆油供需_年度"
    col_name = u"豆油_国内使用量_年度"
     
class DouYou_ShiYongXiaoHao(sdb_base, Manual):
    field_name = u"豆油供需_年度"
    col_name = u"豆油_食用消耗"
     
class DouYou_QiTaXiaoHao(sdb_base, Manual):
    field_name = u"豆油供需_年度"
    col_name = u"豆油_其他消耗"
     
class DouYou_ChuKouLiang_NianDu(sdb_base, Manual):
    field_name = u"豆油供需_年度"
    col_name = u"豆油_出口量_年度"
     
class DouYou_QiMoKuCun_NianDu(sdb_base, Manual):
    field_name = u"豆油供需_年度"
    col_name = u"豆油_期末库存_年度"
     
    
###########################################################################################################################
""" 豆油供需_月度 """  

class DouYou_QiChuKuCun_YueDu(sdb_base, Manual):
    field_name = u"豆油供需_月度"
    col_name = u"豆油_期初库存_月度"

class DouYou_GuoNeiChanLiang_YueDu(sdb_base, Manual):
    field_name = u"豆油供需_月度"
    col_name = u"豆油_国内产量_月度"
    
class DouYou_JinKouLiang_YueDu(sdb_base, Manual):
    field_name = u"豆油供需_月度"
    col_name = u"豆油_进口量_月度"
    
class DouYou_GuoNeiShiYongLiang_YueDu(sdb_base, Manual):
    field_name = u"豆油供需_月度"
    col_name = u"豆油_国内使用量_月度"

class DouYou_ChuKouLiang_YueDu(sdb_base, Manual):
    field_name = u"豆油供需_月度"
    col_name = u"豆油_出口量_月度"

class DouYou_QiMoKuCun_YueDu(sdb_base, Manual):
    field_name = u"豆油供需_月度"
    col_name = u"豆油_期末库存_月度"

###########################################################################################################################
""" 国内大豆压榨 """  

class DaDouYaZhaLiang(sdb_base, Manual):
    field_name = u"国内大豆压榨"
    col_name = u"大豆压榨量"

class DouYouYaZhaChuYouLiang(sdb_base, Manual):
    field_name = u"国内大豆压榨"
    col_name = u"豆油压榨出油量"

class DouYouYaZhaChuPoLiang(sdb_base, Manual):
    field_name = u"国内大豆压榨"
    col_name = u"豆油压榨出粕量"

class DouYouChanNengLiYongLv(sdb_base, Manual):
    field_name = u"国内大豆压榨"
    col_name = u"豆油产能利用率"
    
if __name__ == "__main__":
    a = JiaChunJinKouLiang().get_ts()
    
    
    
    
    
    
    
    
    
    