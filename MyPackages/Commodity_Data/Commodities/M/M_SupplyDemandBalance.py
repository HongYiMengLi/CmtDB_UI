# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 10:48:40 2018

@author: 李弘一萌
"""

import pandas as pd
from datetime import datetime
from .M_Base import M_Base
from ...Base.DataType_Base import Manual, Computed, WindData
from ...Base.Plot_Base import Plot_Base
from matplotlib.ticker import FuncFormatter

class sdb_base(M_Base, Plot_Base):
    table_english_name = "SupplyDemandBalance"
    table_chinese_name = u"供需平衡表"
    
    def output(self):
        print(self.table_english_name)
    
    def get_relevant_df(self, col_list):
        local_col_name_list = sdb_base.get_all_table_classname()
        col_cls_list = []
        for x in col_list:
            col_cls_name = str(M_Base.get_class_name(x))
            if col_cls_name not in local_col_name_list:
                col_cls_list.append(eval(M_Base.get_table_class_full_variable(x)))
            else:
                col_cls_list.append(eval(col_cls_name))
        ts_list = [x().get_ts() for x in col_cls_list]
        tmp_table_df = pd.concat(ts_list, axis=1).dropna(how="all")
        return tmp_table_df 


###########################################################################################################################
""" 产量 """    

class DouPoGuoNeiChanLiang_YueDuGuJi(sdb_base, Manual):
    field_name = u"产量"
    col_name = u"豆粕国内产量_月度估计"

###########################################################################################################################
""" 出口量 """ 
class DouPoChuKouLiang_YueDuGuJi(sdb_base, Manual):
    field_name = u"出口量"
    col_name = u"豆粕出口量_月度估计"

###########################################################################################################################
""" 进口量 """ 
class DouPoJinKouLiang_YueDuGuJi(sdb_base, Manual):
    field_name = u"进口量"
    col_name = u"豆粕进口量_月度估计"

###########################################################################################################################
""" 库存量 """ 
class DouPoQiChuKuCun_YueDuGuJi(sdb_base, Manual):
    field_name = u"库存量"
    col_name = u"豆粕期初库存_月度估计"

class DouPoQiMoKuCun_YueDuGuJi(sdb_base, Manual):
    field_name = u"库存量"
    col_name = u"豆粕期末库存_月度估计"

###########################################################################################################################
""" 需求量 """ 

class DouPoGuoNeiXiaoFei_YueDuGuJi(sdb_base, Manual):
    field_name = u"需求量"
    col_name = u"豆粕国内消费_月度估计"

class DouPoSiYongXiaoFei_YueDuGuJi(sdb_base, Manual):
    field_name = u"需求量"
    col_name = u"豆粕饲用消费_月度估计"

class DouPoShiYongXiaoFei_YueDuGuJi(sdb_base, Manual):
    field_name = u"需求量"
    col_name = u"豆粕食用消费_月度估计"

class DouPoZongShiYongLiang_YueDuGuJi(sdb_base, Manual):
    field_name = u"需求量"
    col_name = u"豆粕总使用量_月度估计"

###########################################################################################################################
""" 压榨量 """

class DaDouYaZhaLiang_YueDuGuJi(sdb_base, Manual):
    field_name = u"压榨量"
    col_name = u"大豆压榨量_月度估计"

###########################################################################################################################
""" 总供应 """
class DouPoZongGongYing_YueDuGuJi(sdb_base, Manual):
    field_name = u"总供应"
    col_name = u"豆粕总供应_月度估计"


    









    
if __name__ == "__main__":
    a = JiaChunJinKouLiang().get_ts()
    
    
    
    
    
    
    
    
    
    