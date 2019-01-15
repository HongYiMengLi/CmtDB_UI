# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 10:47:54 2018

@author: 李弘一萌
"""

import pandas as pd
from datetime import datetime
from .I_Base import I_Base
from ...Base.DataType_Base import Manual, Computed, WindData
from ...Base.Plot_Base import Plot_Base
from matplotlib.ticker import FuncFormatter

class inventory_base(I_Base, Plot_Base):
    table_english_name = "Inventory"
    table_chinese_name = u"库存"
#    original_db_filepath = data_path + u"LPP价格数据库.xlsx"
    
    def output(self):
        print("Inventory")
    
    def get_relevant_df(self, col_list):
        local_col_name_list = inventory_base.get_all_table_classname()
        col_cls_list = []
        for x in col_list:
            col_cls_name = str(I_Base.get_class_name(x))
            if col_cls_name not in local_col_name_list:
                col_cls_list.append(eval(I_Base.get_table_class_full_variable(x)))
            else:
                col_cls_list.append(eval(col_cls_name))
        ts_list = [x().get_ts() for x in col_cls_list]
        tmp_table_df = pd.concat(ts_list, axis=1).dropna(how="all")
        return tmp_table_df 

###########################################################################################################################
""" 钢厂库存 """    

class TieKuangShiShaoJieFenKuangZongKuCun_JinKouKuang_64JiaYangBenGangChang(inventory_base, Manual):
    field_name = u"钢厂库存"
    col_name = u"铁矿石烧结粉矿总库存_进口矿_64家样本钢厂"

class TieKuangShiKuCun_GangChangTieKuangPingJunKeYongTianShu(inventory_base, Manual):
    field_name = u"钢厂库存"
    col_name = u"铁矿石库存_钢厂铁矿平均可用天数"
    
    
###########################################################################################################################
""" 港口库存 """    

class TieKuangShiKuCun_MaoYiKuang_45GeGangKouHeJi(inventory_base, Manual):
    field_name = u"港口库存"
    col_name = u"铁矿石库存_贸易矿_45个港口合计"

class TieKuangShiKuCun_KuaiKuang_45GeGangKouZongJi(inventory_base, Manual):
    field_name = u"港口库存"
    col_name = u"铁矿石库存_块矿_45个港口总计"
    
class TieKuangShiKuCun_QiuTuanKuang_45GeGangKouZongJi(inventory_base, Manual):
    field_name = u"港口库存"
    col_name = u"铁矿石库存_球团矿_45个港口总计"

class TieKuangShiKuCun_TieJingFen_45GeGangKouZongJi(inventory_base, Manual):
    field_name = u"港口库存"
    col_name = u"铁矿石库存_铁精粉_45个港口总计"
    
class TieKuangShiZongKuCun_GangKouHeJi(inventory_base, WindData):
    field_name = u"港口库存"
    col_name = u"铁矿石总库存_港口合计"    
    wind_code = "S0110152" 

class TieKuangShiKuCun_AoZhouKuang(inventory_base, WindData):
    field_name = u"港口库存"
    col_name = u"铁矿石库存_澳洲矿"    
    wind_code = "S0110149" 

class TieKuangShiKuCun_BaXiKuang(inventory_base, WindData):
    field_name = u"港口库存"
    col_name = u"铁矿石库存_巴西矿"    
    wind_code = "S0110150" 

class TieKuangShiKuCun_BaYuQuan(inventory_base, WindData):
    field_name = u"港口库存"
    col_name = u"铁矿石库存_鲅鱼圈"    
    wind_code = "S6400612" 

class TieKuangShiKuCun_DaLianGang(inventory_base, WindData):
    field_name = u"港口库存"
    col_name = u"铁矿石库存_大连港"    
    wind_code = "S6400615" 

class TieKuangShiKuCun_TianJinGang(inventory_base, WindData):
    field_name = u"港口库存"
    col_name = u"铁矿石库存_天津港"    
    wind_code = "S6400616" 

class TieKuangShiKuCun_JingTangGang(inventory_base, WindData):
    field_name = u"港口库存"
    col_name = u"铁矿石库存_京唐港"    
    wind_code = "S6400617" 

class TieKuangShiKuCun_CaoFeiDian(inventory_base, WindData):
    field_name = u"港口库存"
    col_name = u"铁矿石库存_曹妃甸"    
    wind_code = "S6400618" 

class TieKuangShiKuCun_RiZhaoGang(inventory_base, WindData):
    field_name = u"港口库存"
    col_name = u"铁矿石库存_日照港"    
    wind_code = "S6400622" 

class TieKuangShiKuCun_QingDaoGang(inventory_base, WindData):
    field_name = u"港口库存"
    col_name = u"铁矿石库存_青岛港"    
    wind_code = "S6400621" 

class TieKuangShiKuCun_LanShanGang(inventory_base, WindData):
    field_name = u"港口库存"
    col_name = u"铁矿石库存_岚山港"    
    wind_code = "S6400623" 

class TieKuangShiKuCun_LianYunGang(inventory_base, WindData):
    field_name = u"港口库存"
    col_name = u"铁矿石库存_连云港"    
    wind_code = "S6400624"    
        
class TieKuangShiKuCun_TaiCangGang(inventory_base, WindData):
    field_name = u"港口库存"
    col_name = u"铁矿石库存_太仓港"    
    wind_code = "S6400627" 
    
class TieKuangShiKuCun_ZhenJiangGang(inventory_base, WindData):
    field_name = u"港口库存"
    col_name = u"铁矿石库存_镇江港"    
    wind_code = "S6400628" 
    

###########################################################################################################################
""" 国内矿山库存 """    

class TieKuangShiKuCun_TieJingFen_DaXingKuangShan(inventory_base, Manual):
    field_name = u"国内矿山库存"
    col_name = u"铁矿石库存_铁精粉_大型矿山"
    
class TieKuangShiKuCun_TieJingFen_ZhongXingKuangShan(inventory_base, Manual):
    field_name = u"国内矿山库存"
    col_name = u"铁矿石库存_铁精粉_中型矿山"    
    
class TieKuangShiKuCun_TieJingFen_XiaoXingKuangShan(inventory_base, Manual):
    field_name = u"国内矿山库存"
    col_name = u"铁矿石库存_铁精粉_小型矿山"    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    