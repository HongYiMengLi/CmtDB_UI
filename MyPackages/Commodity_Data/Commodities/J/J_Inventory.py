# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 10:47:54 2018

@author: 李弘一萌
"""

import pandas as pd
from datetime import datetime
from .J_Base import J_Base
from ...Base.DataType_Base import Manual, Computed, WindData
from ...Base.Plot_Base import Plot_Base
from matplotlib.ticker import FuncFormatter

class inventory_base(J_Base, Plot_Base):
    table_english_name = "Inventory"
    table_chinese_name = u"库存"
#    original_db_filepath = data_path + u"LPP价格数据库.xlsx"
    
    def output(self):
        print("Jnventory")
    
    def get_relevant_df(self, col_list):
        local_col_name_list = inventory_base.get_all_table_classname()
        col_cls_list = []
        for x in col_list:
            col_cls_name = str(J_Base.get_class_name(x))
            if col_cls_name not in local_col_name_list:
                col_cls_list.append(eval(J_Base.get_table_class_full_variable(x)))
            else:
                col_cls_list.append(eval(col_cls_name))
        ts_list = [x().get_ts() for x in col_cls_list]
        tmp_table_df = pd.concat(ts_list, axis=1).dropna(how="all")
        return tmp_table_df 

###########################################################################################################################
""" 钢厂库存 """    

class JiaoTanKuCun_GangChang_110Jia(inventory_base, Manual):
    field_name = u"钢厂库存"
    col_name = u"焦炭库存_钢厂_110家"

class JiaoTanKuCun_GangChang_DongBeiDiQu(inventory_base, Manual):
    field_name = u"钢厂库存"
    col_name = u"焦炭库存_钢厂_东北地区"

class JiaoTanKuCun_GangChang_HuaBeiDiQu(inventory_base, Manual):
    field_name = u"钢厂库存"
    col_name = u"焦炭库存_钢厂_华北地区"

class JiaoTanKuCun_GangChang_HuaDongDiQu(inventory_base, Manual):
    field_name = u"钢厂库存"
    col_name = u"焦炭库存_钢厂_华东地区"

class JiaoTanKuCun_GangChang_HuaNanDiQu(inventory_base, Manual):
    field_name = u"钢厂库存"
    col_name = u"焦炭库存_钢厂_华南地区"

class JiaoTanKuCun_GangChang_HuaZhongDiQu(inventory_base, Manual):
    field_name = u"钢厂库存"
    col_name = u"焦炭库存_钢厂_华中地区"

class JiaoTanKuCun_GangChang_XiBeiDiQu(inventory_base, Manual):
    field_name = u"钢厂库存"
    col_name = u"焦炭库存_钢厂_西北地区"

class JiaoTanKuCun_GangChang_XiNanDiQu(inventory_base, Manual):
    field_name = u"钢厂库存"
    col_name = u"焦炭库存_钢厂_西南地区"


    
    
###########################################################################################################################
""" 港口库存 """    

class JiaoTanGangKouKuCun_QingDaoGang(inventory_base, WindData):
    field_name = u"港口库存"
    col_name = u"焦炭港口库存_青岛港"    
    wind_code = "S5136709"

class JiaoTanGangKouKuCun_RiZhaoGang(inventory_base, WindData):
    field_name = u"港口库存"
    col_name = u"焦炭港口库存_日照港"    
    wind_code = "S5116630"
    
class JiaoTanGangKouKuCun_LianYunGang(inventory_base, WindData):
    field_name = u"港口库存"
    col_name = u"焦炭港口库存_连云港"    
    wind_code = "S5116629"
    
class JiaoTanGangKouKuCun_TianJinGang(inventory_base, WindData):
    field_name = u"港口库存"
    col_name = u"焦炭港口库存_天津港"    
    wind_code = "S5120058"
    
class JiaoTanGangKouKuCun_SiGangKouHeJi(inventory_base, Computed):
    field_name = u"港口库存"
    col_name = u"焦炭港口库存_四港口合计"    
    def get_ts_whole_progress(self):
        relevant_col_list = [u"焦炭港口库存_青岛港", u"焦炭港口库存_日照港", u"焦炭港口库存_连云港", u"焦炭港口库存_天津港"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total.sum(axis=1)
        return tmp_total
    
###########################################################################################################################
""" 焦企库存 """    

class JiaoTanKuCun_DuLiJiaoHuaChang(inventory_base, Manual):
    field_name = u"焦企库存"
    col_name = u"焦炭库存_独立焦化厂"
    
class JiaoTanKuCun_DuLiJiaoHuaChang_HuaBeiDiQu(inventory_base, Manual):
    field_name = u"焦企库存"
    col_name = u"焦炭库存_独立焦化厂_华北地区"
    
class JiaoTanKuCun_DuLiJiaoHuaChang_DongBeiDiQu(inventory_base, Manual):
    field_name = u"焦企库存"
    col_name = u"焦炭库存_独立焦化厂_东北地区"
    
class JiaoTanKuCun_DuLiJiaoHuaChang_XiBeiDiQu(inventory_base, Manual):
    field_name = u"焦企库存"
    col_name = u"焦炭库存_独立焦化厂_西北地区"
    
class JiaoTanKuCun_DuLiJiaoHuaChang_HuaZhongDiQu(inventory_base, Manual):
    field_name = u"焦企库存"
    col_name = u"焦炭库存_独立焦化厂_华中地区"
    
class JiaoTanKuCun_DuLiJiaoHuaChang_XiNanDiQu(inventory_base, Manual):
    field_name = u"焦企库存"
    col_name = u"焦炭库存_独立焦化厂_西南地区"
    
class JiaoTanKuCun_DuLiJiaoHuaChang_ChanNeng100YiXia(inventory_base, Manual):
    field_name = u"焦企库存"
    col_name = u"焦炭库存_独立焦化厂_产能100以下"
    
class JiaoTanKuCun_DuLiJiaoHuaChang_ChanNeng100To200(inventory_base, Manual):
    field_name = u"焦企库存"
    col_name = u"焦炭库存_独立焦化厂_产能100-200"
    
class JiaoTanKuCun_DuLiJiaoHuaChang_ChanNeng200YiShang(inventory_base, Manual):
    field_name = u"焦企库存"
    col_name = u"焦炭库存_独立焦化厂_产能200以上"
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    