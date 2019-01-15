# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 10:47:54 2018

@author: 李弘一萌
"""

import pandas as pd
from datetime import datetime
from .ZN_Base import ZN_Base
from ...Base.DataType_Base import Manual, Computed, WindData
from ...Base.Plot_Base import Plot_Base
from matplotlib.ticker import FuncFormatter

class inventory_base(ZN_Base, Plot_Base):
    table_english_name = "Inventory"
    table_chinese_name = u"库存"
    
    def output(self):
        print("Inventory")
    
    def get_relevant_df(self, col_list):
        local_col_name_list = inventory_base.get_all_table_classname()
        col_cls_list = []
        for x in col_list:
            col_cls_name = str(ZN_Base.get_class_name(x))
            if col_cls_name not in local_col_name_list:
                col_cls_list.append(eval(ZN_Base.get_table_class_full_variable(x)))
            else:
                col_cls_list.append(eval(col_cls_name))
        ts_list = [x().get_ts() for x in col_cls_list]
        tmp_table_df = pd.concat(ts_list, axis=1).dropna(how="all")
        return tmp_table_df 

###########################################################################################################################
""" 国内库存 """    

class XinKuCunXiaoJi_ZongJi(inventory_base, WindData):
    field_name = u"国内库存"
    col_name = u"锌库存小计_总计"
    wind_code = "S0049506"

class XinKuCunXiaoJi_ShangHai_HeJi(inventory_base, WindData):
    field_name = u"国内库存"
    col_name = u"锌库存小计_上海_合计"
    wind_code = "S0163709"
    
class XinKuCunXiaoJi_GuangDong_HeJi(inventory_base, WindData):
    field_name = u"国内库存"
    col_name = u"锌库存小计_广东_合计"
    wind_code = "S0163718"
    
class XinKuCunXiaoJi_JiangSu_HeJi(inventory_base, WindData):
    field_name = u"国内库存"
    col_name = u"锌库存小计_江苏_合计"
    wind_code = "S0212471"

class XinKuCunXiaoJi_ZheJiang_HeJi(inventory_base, WindData):
    field_name = u"国内库存"
    col_name = u"锌库存小计_浙江_合计"
    wind_code = "S0163722"
    
class XinKuCunQiHuo(inventory_base, WindData):
    field_name = u"国内库存"
    col_name = u"锌库存期货"
    wind_code = "S0049498"

class XinDianGuoNeiKuCunHeJi(inventory_base, WindData):
    field_name = u"国内库存"
    col_name = u"锌锭国内库存合计"
    wind_code = "S5811181"
    start_year = 2014
    
###########################################################################################################################
""" 外盘库存 """    

class LMEXinZongKuCun(inventory_base, WindData):
    field_name = u"国内库存"
    col_name = u"LME锌总库存"
    wind_code = "S0029760"
    start_year = 2014

class LMEXin_ZhuXiaoCangDan_HeJi_QuanQiu(inventory_base, WindData):
    field_name = u"国内库存"
    col_name = u"LME锌_注销仓单_合计_全球"
    wind_code = "S0165057"
    
###########################################################################################################################
""" 库存比 """ 
    
class XinZhuXiaoCangDanKuCunBi(inventory_base, Computed):
    field_name = u"库存比"
    col_name = u"锌注销仓单库存比"
    axhline = 0
    def get_ts_whole_progress(self):
        relevant_col_list = [u"LME锌_注销仓单_合计_全球", u"LME锌总库存"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"LME锌_注销仓单_合计_全球"] / tmp_total[u"LME锌总库存"]
        return tmp_total      
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    