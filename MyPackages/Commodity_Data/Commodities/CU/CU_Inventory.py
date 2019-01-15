# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 10:47:54 2018

@author: 李弘一萌
"""

import pandas as pd
from datetime import datetime
from .CU_Base import CU_Base
from ...Base.DataType_Base import Manual, Computed, WindData
from ...Base.Plot_Base import Plot_Base
from matplotlib.ticker import FuncFormatter

class inventory_base(CU_Base, Plot_Base):
    table_english_name = "Inventory"
    table_chinese_name = u"库存"
#    original_db_filepath = data_path + u"LPP价格数据库.xlsx"
    
    def output(self):
        print("Inventory")
    
    def get_relevant_df(self, col_list):
        local_col_name_list = inventory_base.get_all_table_classname()
        col_cls_list = []
        for x in col_list:
            col_cls_name = str(CU_Base.get_class_name(x))
            if col_cls_name not in local_col_name_list:
                col_cls_list.append(eval(CU_Base.get_table_class_full_variable(x)))
            else:
                col_cls_list.append(eval(col_cls_name))
        ts_list = [x().get_ts() for x in col_cls_list]
        tmp_table_df = pd.concat(ts_list, axis=1).dropna(how="all")
        return tmp_table_df 

###########################################################################################################################
""" 境内库存 """    

class SHFEKuCun_YinJiTong(inventory_base, WindData):
    field_name = u"境内库存"
    col_name = u"SHFE库存_阴极铜"
    wind_code = "S0049507"
    
class TongKuCun_ShangHaiQiTaCangKu(inventory_base, WindData):
    field_name = u"境内库存"
    col_name = u"铜库存_上海其他仓库"
    wind_code = "S5811269"    

class TongKuCun_GuangDong(inventory_base, WindData):
    field_name = u"境内库存"
    col_name = u"铜库存_广东"
    wind_code = "S5811271"    

class TongKuCun_WuXi(inventory_base, WindData):
    field_name = u"境内库存"
    col_name = u"铜库存_无锡"
    wind_code = "S5811272"    

class TongKuCun_ChongQing(inventory_base, WindData):
    field_name = u"境内库存"
    col_name = u"铜库存_重庆"
    wind_code = "S5811565"    

class TongKuCun_TianJin(inventory_base, WindData):
    field_name = u"境内库存"
    col_name = u"铜库存_天津"
    wind_code = "S5811566"    

class TongKuCun_JingNeiHeJi(inventory_base, Computed):
    field_name = u"境内库存"
    col_name = u"铜库存_境内合计"
    start_year = 2014
    def get_ts_whole_progress(self):
        relevant_col_list = [u"SHFE库存_阴极铜", u"铜库存_上海其他仓库", u"铜库存_广东", u"铜库存_无锡", u"铜库存_重庆", u"铜库存_天津"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total.sum(axis=1)
        tmp_total = tmp_total[tmp_total[u"SHFE库存_阴极铜"].notnull()]
        return tmp_total     

###########################################################################################################################
""" 境外库存 """    

class COMEX_Tong_KuCun(inventory_base, WindData):
    field_name = u"境外库存"
    col_name = u"COMEX_铜_库存"
    wind_code = "S0114144"    


class LMETong_KuCun_HeJi_QuanQiu(inventory_base, WindData):
    field_name = u"境外库存"
    col_name = u"LME铜_库存_合计_全球"
    wind_code = "S0164318"       
    
class LMETong_KuCun_HeJi_OuZhou(inventory_base, WindData):
    field_name = u"境外库存"
    col_name = u"LME铜_库存_合计_欧洲"
    wind_code = "S0164319"     
    
class LMETong_KuCun_HeJi_YaZhou(inventory_base, WindData):
    field_name = u"境外库存"
    col_name = u"LME铜_库存_合计_亚洲"
    wind_code = "S0164320"     
    
class LMETong_KuCun_HeJi_BeiMeiZhou(inventory_base, WindData):
    field_name = u"境外库存"
    col_name = u"LME铜_库存_合计_北美洲"
    wind_code = "S0164321"     
    
class JingWaiTongKuCunHeJi(inventory_base, Computed):
    field_name = u"境外库存"
    col_name = u"境外铜库存合计"
    start_year = 2014
    def get_ts_whole_progress(self):
        relevant_col_list = [u"COMEX_铜_库存", u"LME铜_库存_合计_全球"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"COMEX_铜_库存"] + tmp_total[u"LME铜_库存_合计_全球"]
        return tmp_total      
    
    

if __name__ == "__main__":
#    df = PZNSpread9_1().get_ts()
    df, fig, axis = TongKuCun_JingNeiHeJi().seasonal_plot()
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    