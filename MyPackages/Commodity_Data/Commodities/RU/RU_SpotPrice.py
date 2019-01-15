# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 16:35:12 2018

@author: 李弘一萌
"""

import pandas as pd
from datetime import datetime
from .RU_Base import RU_Base
from ...Base.DataType_Base import Manual, Computed, WindData
from ...Base.Plot_Base import Plot_Base
from matplotlib.ticker import FuncFormatter

class spot_price_base(RU_Base, Plot_Base):
    table_english_name = "SpotPrice"
    table_chinese_name = u"现货价格"
    
    def output(self):
        print("SpotPrice")
    
    def get_relevant_df(self, col_list):
        local_col_name_list = spot_price_base.get_all_table_classname()
        col_cls_list = []
        for x in col_list:
            col_cls_name = str(RU_Base.get_class_name(x))
            if col_cls_name not in local_col_name_list:
                col_cls_list.append(eval(RU_Base.get_table_class_full_variable(x)))
            else:
                col_cls_list.append(eval(col_cls_name))
        ts_list = [x().get_ts() for x in col_cls_list]
        tmp_table_df = pd.concat(ts_list, axis=1).dropna(how="all")
        return tmp_table_df  

    
###########################################################################################################################
""" 天胶国内现货 """    

class QuanRuJiaoJiaGe_HengShui(spot_price_base, Manual):
    field_name = u"天胶国内现货"
    col_name = u"全乳胶价格_衡水"

class QuanRuJiaoJiaGe_QingDao(spot_price_base, Manual):
    field_name = u"天胶国内现货"
    col_name = u"全乳胶价格_青岛"
   
class QuanRuJiaoJiaGe_ShangHai(spot_price_base, Manual):
    field_name = u"天胶国内现货"
    col_name = u"全乳胶价格_上海"
   
class QuanRuJiaoJiaGe_YunNan(spot_price_base, Manual):
    field_name = u"天胶国内现货"
    col_name = u"全乳胶价格_云南"

class QuanRuJiaoJiaGe_HaiNan(spot_price_base, Manual):
    field_name = u"天胶国内现货"
    col_name = u"全乳胶价格_海南"
        
class YueNan3LJiaGe_WuPiao_HengShui(spot_price_base, Manual):
    field_name = u"天胶国内现货"
    col_name = u"越南3L价格_无票_衡水"

class YueNan3LJiaGe_17PercentPiao_ShangHai(spot_price_base, Manual):
    field_name = u"天胶国内现货"
    col_name = u"越南3L价格_17%票_上海"

class YueNan3LJiaGe_WuPiao_ShanDong(spot_price_base, Manual):
    field_name = u"天胶国内现货"
    col_name = u"越南3L价格_无票_山东"    
    
class YueNan3LJiaGe_WuPiao_GuangDong(spot_price_base, Manual):
    field_name = u"天胶国内现货"
    col_name = u"越南3L价格_无票_广东"        
    
class TaiGuoSanHaoYanPianJiaGe_17PercentPiao_ShanDong(spot_price_base, Manual):
    field_name = u"天胶国内现货"
    col_name = u"泰国三号烟片价格_17%票_山东"    
    
class TaiGuoSanHaoYanPianJiaGe_17PercentPiao_ShangHai(spot_price_base, Manual):
    field_name = u"天胶国内现货"
    col_name = u"泰国三号烟片价格_17%票_上海"    
   
class GuoChanRuJiaoJiaGe_SanZhuang_ShangHai(spot_price_base, Manual):
    field_name = u"天胶国内现货"
    col_name = u"国产乳胶价格_散装_上海"    
   

###########################################################################################################################
""" 原料价格 """   
    
class ShengJiaoPianJiaGe(spot_price_base, Manual):
    field_name = u"原料价格"
    col_name = u"生胶片价格"     
    
class YanPianJiaGe(spot_price_base, Manual):
    field_name = u"原料价格"
    col_name = u"烟片价格"

class JiaoShuiJiaGe(spot_price_base, Manual):
    field_name = u"原料价格"
    col_name = u"胶水价格"

class BeiJiaoJiaGe(spot_price_base, Manual):
    field_name = u"原料价格"
    col_name = u"杯胶价格"    
    
###########################################################################################################################
""" 丁苯1502国内市场报价 """       
    
class DingBenShiChangJiaGe_HuaDong(spot_price_base, Manual):
    field_name = u"丁苯1502国内市场报价"
    col_name = u"丁苯市场价格_华东"     
    
###########################################################################################################################
""" 东南亚美金胶CIF报价 """       
    
class MaLai20HaoBiaoJiaoMeiJinCIFJiaGe(spot_price_base, Manual):
    field_name = u"东南亚美金胶CIF报价"
    col_name = u"马来20号标胶(SMR20)美金CIF价格"      

class TaiGuo20HaoBiaoJiaoMeiJinCIFJiaGe(spot_price_base, Manual):
    field_name = u"东南亚美金胶CIF报价"
    col_name = u"泰国20号标胶(STR20)美金CIF价格"     
    
class TaiGuo3HaoYanPianMeiJinCIFJiaGe(spot_price_base, Manual):
    field_name = u"东南亚美金胶CIF报价"
    col_name = u"泰国3号烟片(RSS3)美金CIF价格"     
    
class YinNi20HaoBiaoJiaoMeiJinCIFJiaGe(spot_price_base, Manual):
    field_name = u"东南亚美金胶CIF报价"
    col_name = u"印尼20号标胶(SIR20)美金CIF价格"     
    
class TaiGuoTongZhuangRuJiaoMeiJinCIFJiaGe(spot_price_base, Manual):
    field_name = u"东南亚美金胶CIF报价"
    col_name = u"泰国桶装乳胶美金CIF价格"     
    
class YueNan3LMeiJinCIFJiaGe(spot_price_base, Manual):
    field_name = u"东南亚美金胶CIF报价"
    col_name = u"越南3L美金CIF价格"     

###########################################################################################################################
""" 青岛保税区现货价格报价 """       
    
class MaLai20HaoBiaoJiaoBaoShuiQuJiaGe(spot_price_base, Manual):
    field_name = u"青岛保税区现货价格报价"
    col_name = u"马来20号标胶(SMR20)保税区价格" 
    
class TaiGuo20HaoBiaoJiaoBaoShuiQuJiaGe(spot_price_base, Manual):
    field_name = u"青岛保税区现货价格报价"
    col_name = u"泰国20号标胶(STR20)保税区价格" 

class TaiGuo3HaoYanPianBaoShuiQuJiaGe(spot_price_base, Manual):
    field_name = u"青岛保税区现货价格报价"
    col_name = u"泰国3号烟片(RSS3)保税区价格" 

class YinNi20HaoBiaoJiaoBaoShuiQuJiaGe(spot_price_base, Manual):
    field_name = u"青岛保税区现货价格报价"
    col_name = u"印尼20号标胶(SIR20)保税区价格" 

class TaiGuoBiaoJiaoFuHeBaoShuiQuJiaGe(spot_price_base, Manual):
    field_name = u"青岛保税区现货价格报价"
    col_name = u"泰国标胶复合保税区价格" 

###########################################################################################################################
""" 顺丁胶国内市场报价 """       
    
class ShunDingShiChangJiaGe_HuaDong(spot_price_base, Manual):
    field_name = u"顺丁胶国内市场报价"
    col_name = u"顺丁市场价格_华东" 
    
    
    
    
    
    
    
    
    
    
    
    
if __name__ == "__main__":
    ts = YeHuaQiChuChangJia_JingBoShiHua().get_ts()