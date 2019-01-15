# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 10:47:54 2018

@author: 李弘一萌
"""

import pandas as pd
from datetime import datetime
from .A_Base import A_Base
from ...Base.DataType_Base import Manual, Computed, WindData
from ...Base.Plot_Base import Plot_Base
from matplotlib.ticker import FuncFormatter

class inventory_base(A_Base, Plot_Base):
    table_english_name = "Inventory"
    table_chinese_name = u"库存"
    
    def output(self):
        print("Inventory")
    
    def get_relevant_df(self, col_list):
        local_col_name_list = inventory_base.get_all_table_classname()
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
""" 仓单量 """
    
class DouYiZhuCeCangDanLiang_DaLianZhongChuan(inventory_base, Manual):
    field_name = u"仓单量"
    col_name = u"豆一注册仓单量_大连中船"   
    
    
class DouYiZhuCeCangDanLiang_HaiLunKuoHai(inventory_base, WindData):
    field_name = u"仓单量"
    col_name = u"豆一注册仓单量_海伦阔海"    
    wind_code = "S0266196" 

class DouYiZhuCeCangDanLiang_DunHuaZhiShuKu(inventory_base, WindData):
    field_name = u"仓单量"
    col_name = u"豆一注册仓单量_敦化直属库"    
    wind_code = "S0266199" 

class DouYiZhuCeCangDanLiang_BeiAnZhiShuKu(inventory_base, WindData):
    field_name = u"仓单量"
    col_name = u"豆一注册仓单量_北安直属库"    
    wind_code = "S0252201" 

class DouYiZhuCeCangDanLiang_BeiLiangGang(inventory_base, WindData):
    field_name = u"仓单量"
    col_name = u"豆一注册仓单量_北良港"    
    wind_code = "S0163970" 

class DouYiZhuCeCangDanLiang_DaLianZhiShuKu(inventory_base, WindData):
    field_name = u"仓单量"
    col_name = u"豆一注册仓单量_大连直属库"    
    wind_code = "S0181992" 

class DouYiZhuCeCangDanLiang_DaYaoWanGang(inventory_base, WindData):
    field_name = u"仓单量"
    col_name = u"豆一注册仓单量_大窑湾港"    
    wind_code = "S0252202" 

class DouYiZhuCeCangDanLiang_ErLiangKu(inventory_base, WindData):
    field_name = u"仓单量"
    col_name = u"豆一注册仓单量_二粮库"    
    wind_code = "S0252203" 

class DouYiZhuCeCangDanLiang_GaoTaiKu(inventory_base, WindData):
    field_name = u"仓单量"
    col_name = u"豆一注册仓单量_高泰库"    
    wind_code = "S0252204" 

class DouYiZhuCeCangDanLiang_HaErBinZhiShuKu(inventory_base, WindData):
    field_name = u"仓单量"
    col_name = u"豆一注册仓单量_哈尔滨直属库"    
    wind_code = "S0181993" 

class DouYiCangDanLiang(inventory_base, WindData):
    field_name = u"仓单量"
    col_name = u"豆一仓单量"    
    wind_code = "S0049489" 

class DouYiZhuCeCangDanLiang_HaErBinYiHai(inventory_base, WindData):
    field_name = u"仓单量"
    col_name = u"豆一注册仓单量_哈尔滨益海"    
    wind_code = "S0212361" 

class DouYiZhuCeCangDanLiang_HeRongKu(inventory_base, WindData):
    field_name = u"仓单量"
    col_name = u"豆一注册仓单量_合融库"    
    wind_code = "S0252205" 

class DouYiZhuCeCangDanLiang_HeiShanKu(inventory_base, WindData):
    field_name = u"仓单量"
    col_name = u"豆一注册仓单量_黑山库"    
    wind_code = "S0252206" 

class DouYiZhuCeCangDanLiang_HuaNongKu(inventory_base, WindData):
    field_name = u"仓单量"
    col_name = u"豆一注册仓单量_华农库"    
    wind_code = "S0252207" 

class DouYiZhuCeCangDanLiang_JiLiangKu(inventory_base, WindData):
    field_name = u"仓单量"
    col_name = u"豆一注册仓单量_吉粮库"    
    wind_code = "S0252208" 

class DouYiZhuCeCangDanLiang_JinXinKu(inventory_base, WindData):
    field_name = u"仓单量"
    col_name = u"豆一注册仓单量_金信库"    
    wind_code = "S0252209" 

class DouYiZhuCeCangDanLiang_JuXingKu(inventory_base, WindData):
    field_name = u"仓单量"
    col_name = u"豆一注册仓单量_聚兴库"    
    wind_code = "S0252210" 

class DouYiZhuCeCangDanLiang_LiangYunKu(inventory_base, WindData):
    field_name = u"仓单量"
    col_name = u"豆一注册仓单量_良运库"    
    wind_code = "S0163972" 

class DouYiZhuCeCangDanLiang_LiaoLiangKu(inventory_base, WindData):
    field_name = u"仓单量"
    col_name = u"豆一注册仓单量_辽粮库"    
    wind_code = "S0163973" 

class DouYiZhuCeCangDanLiang_LongLiangKu(inventory_base, WindData):
    field_name = u"仓单量"
    col_name = u"豆一注册仓单量_龙粮库"    
    wind_code = "S0214026" 

class DouYiZhuCeCangDanLiang_QianGuanKu(inventory_base, WindData):
    field_name = u"仓单量"
    col_name = u"豆一注册仓单量_前关库"    
    wind_code = "S0214029" 

class DouYiZhuCeCangDanLiang_SuiLengZhiShuKu(inventory_base, WindData):
    field_name = u"仓单量"
    col_name = u"豆一注册仓单量_绥棱直属库"    
    wind_code = "S0212364" 

class DouYiZhuCeCangDanLiang_WaiYunKu(inventory_base, WindData):
    field_name = u"仓单量"
    col_name = u"豆一注册仓单量_外运库"    
    wind_code = "S0163975" 

class DouYiZhuCeCangDanLiang_WeiWeiDongBeiGongSi(inventory_base, WindData):
    field_name = u"仓单量"
    col_name = u"豆一注册仓单量_维维东北公司"    
    wind_code = "S0212367" 

class DouYiZhuCeCangDanLiang_ZhongZhuanKu(inventory_base, WindData):
    field_name = u"仓单量"
    col_name = u"豆一注册仓单量_中转库"    
    wind_code = "S0214032" 

###########################################################################################################################
""" 国储 """
    
class DaDouGuoChuKuCun(inventory_base, Manual):
    field_name = u"国储"
    col_name = u"大豆国储库存"   
    
class DaDouGuoChuPaiMaiJiaGe(inventory_base, Manual):
    field_name = u"国储"
    col_name = u"大豆国储拍卖价格"   
    
class DaDouGuoChuPaiMaiLiang(inventory_base, Manual):
    field_name = u"国储"
    col_name = u"大豆国储拍卖量"   
    
###########################################################################################################################
""" 临储 """
    
class DaDouJiHuaXiaoShouLiang_LinChuPaiMai(inventory_base, Manual):
    field_name = u"临储"
    col_name = u"大豆计划销售量_临储拍卖"     
    
class DaDouShiJiChengJiaoLiang_LinChuPaiMai(inventory_base, Manual):
    field_name = u"临储"
    col_name = u"大豆实际成交量_临储拍卖"     
    
class DaDouChengJiaoLv_LinChuPaiMai(inventory_base, Manual):
    field_name = u"临储"
    col_name = u"大豆成交率_临储拍卖"     
    
class DaDouChengJiaoJunJia_LinChuPaiMai(inventory_base, Manual):
    field_name = u"临储"
    col_name = u"大豆成交均价_临储拍卖"     
    
class DaDouZuiDiJia_LinChuPaiMai(inventory_base, Manual):
    field_name = u"临储"
    col_name = u"大豆最低价_临储拍卖"   
    
class DaDouZuiGaoJia_LinChuPaiMai(inventory_base, Manual):
    field_name = u"临储"
    col_name = u"大豆最高价_临储拍卖"     
    
class DaDouLinChuZongKuCun(inventory_base, Manual):
    field_name = u"临储"
    col_name = u"大豆临储总库存"     
    
class DaDouLinChuKuCunFenNianDu_2011(inventory_base, Manual):
    field_name = u"临储"
    col_name = u"大豆临储库存分年度_2011"     
    
class DaDouLinChuKuCunFenNianDu_2012(inventory_base, Manual):
    field_name = u"临储"
    col_name = u"大豆临储库存分年度_2012"     
    
class DaDouLinChuKuCunFenNianDu_2013(inventory_base, Manual):
    field_name = u"临储"
    col_name = u"大豆临储库存分年度_2013"     
    
class DaDouLinChuShouGouLiang(inventory_base, Manual):
    field_name = u"临储"
    col_name = u"大豆临储收购量"     
  
    
    
    

    
if __name__ == "__main__":
    df = MianHuaRiZongShouChuChengJiaoLiang().get_ts()  












    
    
    