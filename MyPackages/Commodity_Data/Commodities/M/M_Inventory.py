# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 10:47:54 2018

@author: 李弘一萌
"""

import pandas as pd
from datetime import datetime
from .M_Base import M_Base
from ...Base.DataType_Base import Manual, Computed, WindData
from ...Base.Plot_Base import Plot_Base
from matplotlib.ticker import FuncFormatter

class inventory_base(M_Base, Plot_Base):
    table_english_name = "Inventory"
    table_chinese_name = u"库存"
#    original_db_filepath = data_path + u"LPP价格数据库.xlsx"
    
    def output(self):
        print("Inventory")
    
    def get_relevant_df(self, col_list):
        local_col_name_list = inventory_base.get_all_table_classname()
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
""" 仓单量 """    

class DouPoCangDanLiang(inventory_base, WindData):
    field_name = u"仓单量"
    col_name = u"豆粕仓单量"    
    wind_code = "S5021738" 
    
###########################################################################################################################
""" 分地区库存量 """

class FenDiQuKuCun_JinKouDaDou_DongBei(inventory_base, Manual):
    field_name = u"分地区库存量"
    col_name = u"分地区库存_进口大豆_东北"    
    
class FenDiQuKuCun_JinKouDaDou_HuaBei(inventory_base, Manual):
    field_name = u"分地区库存量"
    col_name = u"分地区库存_进口大豆_华北"    
    
class FenDiQuKuCun_JinKouDaDou_ShanDong(inventory_base, Manual):
    field_name = u"分地区库存量"
    col_name = u"分地区库存_进口大豆_山东"    
    
class FenDiQuKuCun_JinKouDaDou_HuaZhong(inventory_base, Manual):
    field_name = u"分地区库存量"
    col_name = u"分地区库存_进口大豆_华中"    
    
class FenDiQuKuCun_JinKouDaDou_HuaDong(inventory_base, Manual):
    field_name = u"分地区库存量"
    col_name = u"分地区库存_进口大豆_华东"    
    
class FenDiQuKuCun_JinKouDaDou_GuangDong(inventory_base, Manual):
    field_name = u"分地区库存量"
    col_name = u"分地区库存_进口大豆_广东"    
    
class FenDiQuKuCun_JinKouDaDou_GuangXi(inventory_base, Manual):
    field_name = u"分地区库存量"
    col_name = u"分地区库存_进口大豆_广西"    
    
class FenDiQuKuCun_JinKouDaDou_FuJian(inventory_base, Manual):
    field_name = u"分地区库存量"
    col_name = u"分地区库存_进口大豆_福建"    
    
class FenDiQuKuCun_JinKouDaDou_XiBei(inventory_base, Manual):
    field_name = u"分地区库存量"
    col_name = u"分地区库存_进口大豆_西北"    
    
class FenDiQuKuCun_DouPo_DongBei(inventory_base, Manual):
    field_name = u"分地区库存量"
    col_name = u"分地区库存_豆粕_东北"    
    
class FenDiQuKuCun_DouPo_HuaBei(inventory_base, Manual):
    field_name = u"分地区库存量"
    col_name = u"分地区库存_豆粕_华北"    
    
class FenDiQuKuCun_DouPo_ShanDong(inventory_base, Manual):
    field_name = u"分地区库存量"
    col_name = u"分地区库存_豆粕_山东"    
    
class FenDiQuKuCun_DouPo_HuaZhong(inventory_base, Manual):
    field_name = u"分地区库存量"
    col_name = u"分地区库存_豆粕_华中"    
    
class FenDiQuKuCun_DouPo_HuaDong(inventory_base, Manual):
    field_name = u"分地区库存量"
    col_name = u"分地区库存_豆粕_华东"    
    
class FenDiQuKuCun_DouPo_GuangDong(inventory_base, Manual):
    field_name = u"分地区库存量"
    col_name = u"分地区库存_豆粕_广东"    
    
class FenDiQuKuCun_DouPo_GuangXi(inventory_base, Manual):
    field_name = u"分地区库存量"
    col_name = u"分地区库存_豆粕_广西"    
    
class FenDiQuKuCun_DouPo_FuJian(inventory_base, Manual):
    field_name = u"分地区库存量"
    col_name = u"分地区库存_豆粕_福建"    
    
class FenDiQuKuCun_DouPo_XiBei(inventory_base, Manual):
    field_name = u"分地区库存量"
    col_name = u"分地区库存_豆粕_西北"    
    

###########################################################################################################################
""" 库存量 """

class JinKouDaDouKuCun_YanHaiYouChang(inventory_base, Manual):
    field_name = u"库存量"
    col_name = u"进口大豆库存_沿海油厂" 

class JinKouDaDouKuCun_QuanGuo(inventory_base, Manual):
    field_name = u"库存量"
    col_name = u"进口大豆库存_全国" 

###########################################################################################################################
""" 未执行合同量 """

class DouPoWeiZhiXingHeTong_YanHaiYouChang(inventory_base, Manual):
    field_name = u"未执行合同量"
    col_name = u"豆粕未执行合同_沿海油厂" 

class DouPoWeiZhiXingHeTong_QuanGuo(inventory_base, Manual):
    field_name = u"未执行合同量"
    col_name = u"豆粕未执行合同_全国" 








    
if __name__ == "__main__":
    df = MianHuaRiZongShouChuChengJiaoLiang().get_ts()  












    
    
    