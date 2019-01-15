# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 10:47:54 2018

@author: 李弘一萌
"""

import pandas as pd
from datetime import datetime
from .JM_Base import JM_Base
from ...Base.DataType_Base import Manual, Computed, WindData
from ...Base.Plot_Base import Plot_Base
from matplotlib.ticker import FuncFormatter

class inventory_base(JM_Base, Plot_Base):
    table_english_name = "Inventory"
    table_chinese_name = u"库存"
#    original_db_filepath = data_path + u"LPP价格数据库.xlsx"
    
    def output(self):
        print("Inventory")
    
    def get_relevant_df(self, col_list):
        local_col_name_list = inventory_base.get_all_table_classname()
        col_cls_list = []
        for x in col_list:
            col_cls_name = str(JM_Base.get_class_name(x))
            if col_cls_name not in local_col_name_list:
                col_cls_list.append(eval(JM_Base.get_table_class_full_variable(x)))
            else:
                col_cls_list.append(eval(col_cls_name))
        ts_list = [x().get_ts() for x in col_cls_list]
        tmp_table_df = pd.concat(ts_list, axis=1).dropna(how="all")
        return tmp_table_df 

###########################################################################################################################
""" 钢厂炼焦煤库存 """    

class LianJiaoMeiKuCun_GangChangJiaoHuaChang(inventory_base, Manual):
    field_name = u"钢厂炼焦煤库存"
    col_name = u"炼焦煤库存_钢厂焦化厂_110家"

class LianJiaoMeiKuCun_GangChangJiaoHuaChang_DongBeiDiQu(inventory_base, Manual):
    field_name = u"钢厂炼焦煤库存"
    col_name = u"炼焦煤库存_钢厂焦化厂_东北地区"

class LianJiaoMeiKuCun_GangChangJiaoHuaChang_HuaBeiDiQu(inventory_base, Manual):
    field_name = u"钢厂炼焦煤库存"
    col_name = u"炼焦煤库存_钢厂焦化厂_华北地区"

class LianJiaoMeiKuCun_GangChangJiaoHuaChang_HuaDongDiQu(inventory_base, Manual):
    field_name = u"钢厂炼焦煤库存"
    col_name = u"炼焦煤库存_钢厂焦化厂_华东地区"

class LianJiaoMeiKuCun_GangChangJiaoHuaChang_HuaNanDiQu(inventory_base, Manual):
    field_name = u"钢厂炼焦煤库存"
    col_name = u"炼焦煤库存_钢厂焦化厂_华南地区"

class LianJiaoMeiKuCun_GangChangJiaoHuaChang_HuaZhongDiQu(inventory_base, Manual):
    field_name = u"钢厂炼焦煤库存"
    col_name = u"炼焦煤库存_钢厂焦化厂_华中地区"

class LianJiaoMeiKuCun_GangChangJiaoHuaChang_XiBeiDiQu(inventory_base, Manual):
    field_name = u"钢厂炼焦煤库存"
    col_name = u"炼焦煤库存_钢厂焦化厂_西北地区"

class LianJiaoMeiKuCun_GangChangJiaoHuaChang_XiNanDiQu(inventory_base, Manual):
    field_name = u"钢厂炼焦煤库存"
    col_name = u"炼焦煤库存_钢厂焦化厂_西南地区"

class GangChangJiaoHuaChangLianJiaoMeiKuCunPingJunKeYongTianShu(inventory_base, Manual):
    field_name = u"钢厂炼焦煤库存"
    col_name = u"钢厂焦化厂炼焦煤库存平均可用天数_110家"

class GangChangJiaoHuaChangLianJiaoMeiKuCunPingJunKeYongTianShu_DongBeiDiQu(inventory_base, Manual):
    field_name = u"钢厂炼焦煤库存"
    col_name = u"钢厂焦化厂炼焦煤库存平均可用天数_东北地区"

class GangChangJiaoHuaChangLianJiaoMeiKuCunPingJunKeYongTianShu_HuaBeiDiQu(inventory_base, Manual):
    field_name = u"钢厂炼焦煤库存"
    col_name = u"钢厂焦化厂炼焦煤库存平均可用天数_华北地区"

class GangChangJiaoHuaChangLianJiaoMeiKuCunPingJunKeYongTianShu_HuaDongDiQu(inventory_base, Manual):
    field_name = u"钢厂炼焦煤库存"
    col_name = u"钢厂焦化厂炼焦煤库存平均可用天数_华东地区"

class GangChangJiaoHuaChangLianJiaoMeiKuCunPingJunKeYongTianShu_HuaNanDiQu(inventory_base, Manual):
    field_name = u"钢厂炼焦煤库存"
    col_name = u"钢厂焦化厂炼焦煤库存平均可用天数_华南地区"

class GangChangJiaoHuaChangLianJiaoMeiKuCunPingJunKeYongTianShu_HuaZhongDiQu(inventory_base, Manual):
    field_name = u"钢厂炼焦煤库存"
    col_name = u"钢厂焦化厂炼焦煤库存平均可用天数_华中地区"

class GangChangJiaoHuaChangLianJiaoMeiKuCunPingJunKeYongTianShu_XiBeiDiQu(inventory_base, Manual):
    field_name = u"钢厂炼焦煤库存"
    col_name = u"钢厂焦化厂炼焦煤库存平均可用天数_西北地区"

class GangChangJiaoHuaChangLianJiaoMeiKuCunPingJunKeYongTianShu_XiNanDiQu(inventory_base, Manual):
    field_name = u"钢厂炼焦煤库存"
    col_name = u"钢厂焦化厂炼焦煤库存平均可用天数_西南地区"

    
###########################################################################################################################
""" 焦化厂炼焦煤库存 """    


    
    
class DuLiJiaoHuaChangLianJiaoMeiKuCun_XiNan(inventory_base, Manual):
    field_name = u"焦化厂炼焦煤库存"
    col_name = u"独立焦化厂炼焦煤库存_西南"
    
class DuLiJiaoHuaChangLianJiaoMeiKuCun_XiBei(inventory_base, Manual):
    field_name = u"焦化厂炼焦煤库存"
    col_name = u"独立焦化厂炼焦煤库存_西北"
    
class DuLiJiaoHuaChangLianJiaoMeiKuCun_DongBei(inventory_base, Manual):
    field_name = u"焦化厂炼焦煤库存"
    col_name = u"独立焦化厂炼焦煤库存_东北"
    
class DuLiJiaoHuaChangLianJiaoMeiKuCun_HuaZhong(inventory_base, Manual):
    field_name = u"焦化厂炼焦煤库存"
    col_name = u"独立焦化厂炼焦煤库存_华中"
    
class DuLiJiaoHuaChangLianJiaoMeiKuCun_HuaBei(inventory_base, Manual):
    field_name = u"焦化厂炼焦煤库存"
    col_name = u"独立焦化厂炼焦煤库存_华北"
    
class DuLiJiaoHuaChangLianJiaoMeiKuCun_HuaDong(inventory_base, Manual):
    field_name = u"焦化厂炼焦煤库存"
    col_name = u"独立焦化厂炼焦煤库存_华东"

class DuLiJiaoHuaChangLianJiaoMeiKuCunPingJunKeYongTianShu_100Jia(inventory_base, Manual):
    field_name = u"焦化厂炼焦煤库存"
    col_name = u"独立焦化厂炼焦煤库存平均可用天数_100家"
    
class DuLiJiaoHuaChangLianJiaoMeiKuCunPingJunKeYongTianShu_XiNan(inventory_base, Manual):
    field_name = u"焦化厂炼焦煤库存"
    col_name = u"独立焦化厂炼焦煤库存平均可用天数_西南"
    
class DuLiJiaoHuaChangLianJiaoMeiKuCunPingJunKeYongTianShu_XiBei(inventory_base, Manual):
    field_name = u"焦化厂炼焦煤库存"
    col_name = u"独立焦化厂炼焦煤库存平均可用天数_西北"
    
class DuLiJiaoHuaChangLianJiaoMeiKuCunPingJunKeYongTianShu_DongBei(inventory_base, Manual):
    field_name = u"焦化厂炼焦煤库存"
    col_name = u"独立焦化厂炼焦煤库存平均可用天数_东北"
    
class DuLiJiaoHuaChangLianJiaoMeiKuCunPingJunKeYongTianShu_HuaZhong(inventory_base, Manual):
    field_name = u"焦化厂炼焦煤库存"
    col_name = u"独立焦化厂炼焦煤库存平均可用天数_华中"
    
class DuLiJiaoHuaChangLianJiaoMeiKuCunPingJunKeYongTianShu_HuaBei(inventory_base, Manual):
    field_name = u"焦化厂炼焦煤库存"
    col_name = u"独立焦化厂炼焦煤库存平均可用天数_华北"
    
class DuLiJiaoHuaChangLianJiaoMeiKuCunPingJunKeYongTianShu_HuaDong(inventory_base, Manual):
    field_name = u"焦化厂炼焦煤库存"
    col_name = u"独立焦化厂炼焦煤库存平均可用天数_华东"    
    
class DuLiJiaoHuaChangLianJiaoMeiKuCun_ChanNengGT200(inventory_base, Manual):
    field_name = u"焦化厂炼焦煤库存"
    col_name = u"独立焦化厂炼焦煤库存_产能>200"
    
class DuLiJiaoHuaChangLianJiaoMeiKuCun_ChanNeng100To200(inventory_base, Manual):
    field_name = u"焦化厂炼焦煤库存"
    col_name = u"独立焦化厂炼焦煤库存_产能100-200"
    
class DuLiJiaoHuaChangLianJiaoMeiKuCun_ChanNengLT100(inventory_base, Manual):
    field_name = u"焦化厂炼焦煤库存"
    col_name = u"独立焦化厂炼焦煤库存_产能<100"
    
class DuLiJiaoHuaChangLianJiaoMeiKuCunPingJunKeYongTianShu_ChanNengGT200(inventory_base, Manual):
    field_name = u"焦化厂炼焦煤库存"
    col_name = u"独立焦化厂炼焦煤库存平均可用天数_产能>200"
    
class DuLiJiaoHuaChangLianJiaoMeiKuCunPingJunKeYongTianShu_ChanNeng100To200(inventory_base, Manual):
    field_name = u"焦化厂炼焦煤库存"
    col_name = u"独立焦化厂炼焦煤库存平均可用天数_产能100-200"
    
class DuLiJiaoHuaChangLianJiaoMeiKuCunPingJunKeYongTianShu_ChanNengLT100(inventory_base, Manual):
    field_name = u"焦化厂炼焦煤库存"
    col_name = u"独立焦化厂炼焦煤库存平均可用天数_产能<100"        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    