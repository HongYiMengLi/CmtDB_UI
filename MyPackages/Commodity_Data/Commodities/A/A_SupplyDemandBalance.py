# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 10:48:40 2018

@author: 李弘一萌
"""

import pandas as pd
from datetime import datetime
from .A_Base import A_Base
from ...Base.DataType_Base import Manual, Computed, WindData
from ...Base.Plot_Base import Plot_Base
from matplotlib.ticker import FuncFormatter

class sdb_base(A_Base, Plot_Base):
    table_english_name = "SupplyDemandBalance"
    table_chinese_name = u"供需平衡表"
    
    def output(self):
        print(self.table_english_name)
    
    def get_relevant_df(self, col_list):
        local_col_name_list = sdb_base.get_all_table_classname()
        col_cls_list = []
        for x in col_list:
            col_cls_name = str(A_Base.get_class_name(x))
            if col_cls_name not in local_col_name_list:
                col_cls_list.append(eval(A_Base.get_table_class_full_variable(x)))
            else:
                col_cls_list.append(eval(col_cls_name))
        ts_list = [x().get_ts() for x in col_cls_list]
        tmp_table_df = pd.concat(ts_list, axis=1).dropna(how="all")
        return tmp_table_df 


###########################################################################################################################
""" 产量 """    

class DaDouGuoNeiChanLiang_TianXiaLiangCang(sdb_base, Manual):
    field_name = u"产量"
    col_name = u"大豆国内产量_天下粮仓"

###########################################################################################################################
""" 出口量 """    

class DaDouChuKouLiang_TianXiaLiangCang(sdb_base, Manual):
    field_name = u"出口量"
    col_name = u"大豆出口量_天下粮仓"

###########################################################################################################################
""" 进口量 """    

class DaDouJinKouLiang_TianXiaLiangCang(sdb_base, Manual):
    field_name = u"进口量"
    col_name = u"大豆进口量_天下粮仓"
    
###########################################################################################################################
""" 库存消费比 """    

class DaDouKuCunXiaoFeiBi_TianXiaLiangCang(sdb_base, Manual):
    field_name = u"库存消费比"
    col_name = u"大豆库存消费比_天下粮仓"
        
    
###########################################################################################################################
""" 期初库存 """    

class DaDouQiChuKuCun_TianXiaLiangCang(sdb_base, Manual):
    field_name = u"期初库存"
    col_name = u"大豆期初库存_天下粮仓"
        
###########################################################################################################################
""" 期末库存 """    

class DaDouQiMoKuCun_TianXiaLiangCang(sdb_base, Manual):
    field_name = u"期末库存"
    col_name = u"大豆期末库存_天下粮仓"        
    
###########################################################################################################################
""" 食用及工业消耗量 """    

class DaDouShiYongJiGongYeXiaoHaoLiang_TianXiaLiangCang(sdb_base, Manual):
    field_name = u"期末库存"
    col_name = u"大豆食用及工业消耗量_天下粮仓"        
        
###########################################################################################################################
""" 压榨量 """    

class DaDouYaZhaYongLiang_TianXiaLiangCang(sdb_base, Manual):
    field_name = u"压榨量"
    col_name = u"大豆压榨用量_天下粮仓"        
    
class GuoChanDaDouYaZhaYongLiang_TianXiaLiangCang(sdb_base, Manual):
    field_name = u"压榨量"
    col_name = u"国产大豆压榨用量_天下粮仓"        
      
class JinKouDaDouYaZhaYongLiang_TianXiaLiangCang(sdb_base, Manual):
    field_name = u"压榨量"
    col_name = u"进口大豆压榨用量_天下粮仓"        
      
###########################################################################################################################
""" 种子用量 """    

class DaDouZhongZiYongLiang_TianXiaLiangCang(sdb_base, Manual):
    field_name = u"种子用量"
    col_name = u"大豆种子用量_天下粮仓"     
    
      
###########################################################################################################################
""" 总供应量 """    

class DaDouZongGongYingLiang_TianXiaLiangCang(sdb_base, Manual):
    field_name = u"总供应量"
    col_name = u"大豆总供应量_天下粮仓"      
    
    
class DaDouZongShiYongLiang_TianXiaLiangCang(sdb_base, Manual):
    field_name = u"总供应量"
    col_name = u"大豆总使用量_天下粮仓"      
    
      
    

    
if __name__ == "__main__":
    a = JiaChunJinKouLiang().get_ts()
    
    
    
    
    
    
    
    
    
    