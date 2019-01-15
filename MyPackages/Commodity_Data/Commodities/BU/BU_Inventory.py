# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 10:47:54 2018

@author: 李弘一萌
"""

import pandas as pd
from datetime import datetime
from .BU_Base import BU_Base
from ...Base.DataType_Base import Manual, Computed, WindData
from ...Base.Plot_Base import Plot_Base
from matplotlib.ticker import FuncFormatter

class inventory_base(BU_Base, Plot_Base):
    table_english_name = "Inventory"
    table_chinese_name = u"库存"
#    original_db_filepath = data_path + u"LPP价格数据库.xlsx"
    
    def output(self):
        print("Inventory")
    
    def get_relevant_df(self, col_list):
        local_col_name_list = inventory_base.get_all_table_classname()
        col_cls_list = []
        for x in col_list:
            col_cls_name = str(BU_Base.get_class_name(x))
            if col_cls_name not in local_col_name_list:
                col_cls_list.append(eval(BU_Base.get_table_class_full_variable(x)))
            else:
                col_cls_list.append(eval(col_cls_name))
        ts_list = [x().get_ts() for x in col_cls_list]
        tmp_table_df = pd.concat(ts_list, axis=1).dropna(how="all")
        return tmp_table_df 

    
###########################################################################################################################
""" 仓单 """    

class LiQingKuCunQiHuo_ZongJi(inventory_base, WindData):
    field_name = u"仓单"
    col_name = u"沥青库存期货_总计"    
    wind_code = "S0204821" 

class LiQingKuCunQiHuo_CangKu(inventory_base, WindData):
    field_name = u"仓单"
    col_name = u"沥青库存期货_仓库"    
    wind_code = "S0204801" 

class LiQingKuCunQiHuo_ChangKu(inventory_base, WindData):
    field_name = u"仓单"
    col_name = u"沥青库存期货_厂库"    
    wind_code = "S0204802" 

class LiQingKuCunQiHuo_GuangDongCangKu_NanYueWuLiu(inventory_base, WindData):
    field_name = u"仓单"
    col_name = u"沥青库存期货_广东仓库_南粤物流"    
    wind_code = "S0204803" 

class LiQingKuCunQiHuo_GuangDongChangKu_ZhongYouGaoFu(inventory_base, WindData):
    field_name = u"仓单"
    col_name = u"沥青库存期货_广东厂库_中油高富"    
    wind_code = "S0204804" 

class LiQingKuCunQiHuo_JiangSuCangKu_HeJi(inventory_base, WindData):
    field_name = u"仓单"
    col_name = u"沥青库存期货_江苏仓库_合计"    
    wind_code = "S0204805" 

class LiQingKuCunQiHuo_JiangSuCangKu_HengTaiLiQing(inventory_base, WindData):
    field_name = u"仓单"
    col_name = u"沥青库存期货_江苏仓库_恒泰沥青"    
    wind_code = "S0204806" 

class LiQingKuCunQiHuo_JiangSuCangKu_JinHaiHongYe(inventory_base, WindData):
    field_name = u"仓单"
    col_name = u"沥青库存期货_江苏仓库_金海宏业"    
    wind_code = "S0204807" 

class LiQingKuCunQiHuo_JiangSuCangKu_SanFengShiHua(inventory_base, WindData):
    field_name = u"仓单"
    col_name = u"沥青库存期货_江苏仓库_三峰石化"    
    wind_code = "S0204808" 

class LiQingKuCunQiHuo_JiangSuCangKu_XinYueLiQing(inventory_base, WindData):
    field_name = u"仓单"
    col_name = u"沥青库存期货_江苏仓库_新越沥青"    
    wind_code = "S0204809"     
    
class LiQingKuCunQiHuo_JiangSuChangKu_HeJi(inventory_base, WindData):
    field_name = u"仓单"
    col_name = u"沥青库存期货_江苏厂库_合计"    
    wind_code = "S0204810"     
    
class LiQingKuCunQiHuo_JiangSuChangKu_JinHaiHongYe(inventory_base, WindData):
    field_name = u"仓单"
    col_name = u"沥青库存期货_江苏厂库_金海宏业"    
    wind_code = "S0204811"     
    
class LiQingKuCunQiHuo_JiangSuChangKu_ZhongHaiTaiZhouShiHua(inventory_base, WindData):
    field_name = u"仓单"
    col_name = u"沥青库存期货_江苏厂库_中海泰州石化"    
    wind_code = "S0204812"     
    
class LiQingKuCunQiHuo_JiangSuChangKu_ZhongYouJiangSu(inventory_base, WindData):
    field_name = u"仓单"
    col_name = u"沥青库存期货_江苏厂库_中油江苏"    
    wind_code = "S0204813"     
    
class LiQingKuCunQiHuo_ShanDongChangKu_HeJi(inventory_base, WindData):
    field_name = u"仓单"
    col_name = u"沥青库存期货_山东厂库_合计"    
    wind_code = "S0204814"     
    
class LiQingKuCunQiHuo_ShanDongChangKu_ShanDongJinShi(inventory_base, WindData):
    field_name = u"仓单"
    col_name = u"沥青库存期货_山东厂库_山东金石"    
    wind_code = "S0204815"     
    
class LiQingKuCunQiHuo_ShanDongChangKu_ZhongHaiLiQing(inventory_base, WindData):
    field_name = u"仓单"
    col_name = u"沥青库存期货_山东厂库_中海沥青"    
    wind_code = "S0204816"    
    
class LiQingKuCunQiHuo_ShanDongChangKu_ZhongHuaHongRun(inventory_base, WindData):
    field_name = u"仓单"
    col_name = u"沥青库存期货_山东厂库_中化弘润"    
    wind_code = "S0204817"    
    
class LiQingKuCunQiHuo_ZheJiangCangKu_HeJi(inventory_base, WindData):
    field_name = u"仓单"
    col_name = u"沥青库存期货_浙江仓库_合计"    
    wind_code = "S0204820"    
    
class LiQingKuCunQiHuo_ZheJiangCangKu_AiSiKaiBaoYing(inventory_base, WindData):
    field_name = u"仓单"
    col_name = u"沥青库存期货_浙江仓库_爱思开宝盈"    
    wind_code = "S0204818"    
    
class LiQingKuCunQiHuo_ZheJiangCangKu_FuKangShiHua(inventory_base, WindData):
    field_name = u"仓单"
    col_name = u"沥青库存期货_浙江仓库_富康石化"    
    wind_code = "S0204819"        
    
    
###########################################################################################################################
""" 国内库存 """    

class LiQingKuCun_XiBei(inventory_base, Manual):
    field_name = u"国内库存"
    col_name = u"沥青库存_西北"    
    def seasonal_plot(self, title=None, start_year=None, axhline=None):
        tmp_df_interpolated, fig, axis = super(inventory_base, self).seasonal_plot(title=title, start_year=start_year)
        axis.yaxis.set_major_formatter(FuncFormatter(lambda y, _: '{:.0%}'.format(y)))
        return tmp_df_interpolated, fig, axis
        
class LiQingKuCun_DongBei(inventory_base, Manual):
    field_name = u"国内库存"
    col_name = u"沥青库存_东北"   
    def seasonal_plot(self, title=None, start_year=None, axhline=None):
        tmp_df_interpolated, fig, axis = super(inventory_base, self).seasonal_plot(title=title, start_year=start_year)
        axis.yaxis.set_major_formatter(FuncFormatter(lambda y, _: '{:.0%}'.format(y)))
        return tmp_df_interpolated, fig, axis
    
class LiQingKuCun_ShanDong(inventory_base, Manual):
    field_name = u"国内库存"
    col_name = u"沥青库存_山东"   
    def seasonal_plot(self, title=None, start_year=None, axhline=None):
        tmp_df_interpolated, fig, axis = super(inventory_base, self).seasonal_plot(title=title, start_year=start_year)
        axis.yaxis.set_major_formatter(FuncFormatter(lambda y, _: '{:.0%}'.format(y)))
        return tmp_df_interpolated, fig, axis
    
class LiQingKuCun_ChangSanJiao(inventory_base, Manual):
    field_name = u"国内库存"
    col_name = u"沥青库存_长三角"   
    def seasonal_plot(self, title=None, start_year=None, axhline=None):
        tmp_df_interpolated, fig, axis = super(inventory_base, self).seasonal_plot(title=title, start_year=start_year)
        axis.yaxis.set_major_formatter(FuncFormatter(lambda y, _: '{:.0%}'.format(y)))
        return tmp_df_interpolated, fig, axis
    
class LiQingKuCun_HuaNan(inventory_base, Manual):
    field_name = u"国内库存"
    col_name = u"沥青库存_华南"   
    def seasonal_plot(self, title=None, start_year=None, axhline=None):
        tmp_df_interpolated, fig, axis = super(inventory_base, self).seasonal_plot(title=title, start_year=start_year)
        axis.yaxis.set_major_formatter(FuncFormatter(lambda y, _: '{:.0%}'.format(y)))
        return tmp_df_interpolated, fig, axis
    
class LiQingKuCun_HeJi(inventory_base, Manual):
    field_name = u"国内库存"
    col_name = u"沥青库存_合计"       
    def seasonal_plot(self, title=None, start_year=None, axhline=None):
        tmp_df_interpolated, fig, axis = super(inventory_base, self).seasonal_plot(title=title, start_year=start_year)
        axis.yaxis.set_major_formatter(FuncFormatter(lambda y, _: '{:.0%}'.format(y)))
        return tmp_df_interpolated, fig, axis
        
    
    

if __name__ == "__main__":
    ts = LiQingKuCun_ShanDong().get_ts()    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    