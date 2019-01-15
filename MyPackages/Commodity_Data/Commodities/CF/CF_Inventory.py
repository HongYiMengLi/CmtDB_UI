# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 10:47:54 2018

@author: 李弘一萌
"""

import pandas as pd
from datetime import datetime
from .CF_Base import CF_Base
from ...Base.DataType_Base import Manual, Computed, WindData
from ...Base.Plot_Base import Plot_Base
from matplotlib.ticker import FuncFormatter

class inventory_base(CF_Base, Plot_Base):
    table_english_name = "Inventory"
    table_chinese_name = u"库存"
#    original_db_filepath = data_path + u"LPP价格数据库.xlsx"
    
    def output(self):
        print("Inventory")
    
    def get_relevant_df(self, col_list):
        local_col_name_list = inventory_base.get_all_table_classname()
        col_cls_list = []
        for x in col_list:
            col_cls_name = str(CF_Base.get_class_name(x))
            if col_cls_name not in local_col_name_list:
                col_cls_list.append(eval(CF_Base.get_table_class_full_variable(x)))
            else:
                col_cls_list.append(eval(col_cls_name))
        ts_list = [x().get_ts() for x in col_cls_list]
        tmp_table_df = pd.concat(ts_list, axis=1).dropna(how="all")
        return tmp_table_df 

    
###########################################################################################################################
""" 仓单 """    

class MianHuaCangDan(inventory_base, WindData):
    field_name = u"仓单"
    col_name = u"棉花仓单"    
    wind_code = "S0049502" 

###########################################################################################################################
""" 有效预报 """ 

class MianHuaYouXiaoYuBao(inventory_base, WindData):
    field_name = u"有效预报"
    col_name = u"棉花有效预报"    
    wind_code = "S0049517" 


###########################################################################################################################
""" 仓单+有效预报 """ 
    
class MianHuaCangDanPlusYouXiaoYuBao(inventory_base, Computed):
    field_name = u"仓单+有效预报"
    col_name = u"棉花仓单+有效预报"   
    def get_ts_whole_progress(self):
        relevant_col_list = [u"棉花仓单", u"棉花有效预报"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total.sum(axis=1, skipna=True)
        return tmp_total  

    
###########################################################################################################################
""" 工业库存 """ 

class MianHuaGongYeKuCun_QuanGuo(inventory_base, WindData):
    field_name = u"工业库存"
    col_name = u"棉花工业库存_全国"    
    wind_code = "S5022147"     
    
class MianHuaGongYeKuCun_JinKouZhanBi(inventory_base, WindData):
    field_name = u"工业库存"
    col_name = u"棉花工业库存_进口占比"    
    wind_code = "S5022151"       
    
class MianHuaGongYeKuCun_XinJiangZhanBi(inventory_base, WindData):
    field_name = u"工业库存"
    col_name = u"棉花工业库存_新疆占比"    
    wind_code = "S5022150"       
    
###########################################################################################################################
""" 每日抛储 """

class MianHuaMeiRiJiHuaPaoChuLiang(inventory_base, Manual):
    field_name = u"每日抛储"
    col_name = u"棉花每日计划抛储量"    
    
class MianHuaShiJiChengJiaoLiang(inventory_base, Manual):
    field_name = u"每日抛储"
    col_name = u"棉花实际成交量"      
    
class MianHuaShiJiChengJiaoLv(inventory_base, Manual):
    field_name = u"每日抛储"
    col_name = u"棉花实际成交率"      
    
class JiangMianGuaPaiLiang(inventory_base, Manual):
    field_name = u"每日抛储"
    col_name = u"疆棉挂牌量"      
    
class JiangMianZhanBi(inventory_base, Manual):
    field_name = u"每日抛储"
    col_name = u"疆棉占比"  

class JiangMianChengJiaoLv(inventory_base, Manual):
    field_name = u"每日抛储"
    col_name = u"疆棉成交率"      
    
class DiChanMianGuaPaiLiang(inventory_base, Manual):
    field_name = u"每日抛储"
    col_name = u"地产棉挂牌量"    
    
class DiChanMianZhanBi(inventory_base, Manual):
    field_name = u"每日抛储"
    col_name = u"地产棉占比"      
    
class DiChanMianChengJiaoLv(inventory_base, Manual):
    field_name = u"每日抛储"
    col_name = u"地产棉成交率"      
    
class MianHuaShiJiChengJiaoJunJia(inventory_base, Manual):
    field_name = u"每日抛储"
    col_name = u"棉花实际成交均价"      
    
class MianHuaZheGuoChan3128JiaGe(inventory_base, Manual):
    field_name = u"每日抛储"
    col_name = u"棉花折国产3128价格"  

class MianHuaJingPaiDiJia(inventory_base, Manual):
    field_name = u"每日抛储"
    col_name = u"棉花竞拍底价"      

    
###########################################################################################################################
""" 商业库存 """ 

class MianHuaShangYeKuCun_QuanGuo(inventory_base, WindData):
    field_name = u"商业库存"
    col_name = u"棉花商业库存_全国"    
    wind_code = "S5022087"         
    
class MianHuaShangYeKuCun_NeiDi(inventory_base, WindData):
    field_name = u"商业库存"
    col_name = u"棉花商业库存_内地"    
    wind_code = "S5022089"  

class MianHuaShangYeKuCun_XinJiang(inventory_base, WindData):
    field_name = u"商业库存"
    col_name = u"棉花商业库存_新疆"    
    wind_code = "S5022088"  


###########################################################################################################################
""" 收储 """

class MianHuaShouChuRiChengJiaoLiang(inventory_base, Manual):
    field_name = u"收储"
    col_name = u"棉花收储日成交量"    

class MianHuaDaDanShouChu(inventory_base, Manual):
    field_name = u"收储"
    col_name = u"棉花大单收储"  
    
class MianHuaRiZongShouChuChengJiaoLiang(inventory_base, Computed):
    field_name = u"收储"
    col_name = u"棉花日总收储成交量"      
    def get_ts_whole_progress(self):
        relevant_col_list = [u"棉花收储日成交量", "棉花大单收储"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total.sum(axis=1, skipna=True)
        return tmp_total

    
###########################################################################################################################
""" 下游库存 """

class FangQiMianHuaKuCun_RiJun(inventory_base, Manual):
    field_name = u"下游库存"
    col_name = u"纺企棉花库存_日均"  

class FangQiMianHuaKuCun_ZhouJun(inventory_base, Manual):
    field_name = u"下游库存"
    col_name = u"纺企棉花库存_周均"  

class FangQiMianHuaKuCun_YueJun(inventory_base, Manual):
    field_name = u"下游库存"
    col_name = u"纺企棉花库存_月均"  

class FangQiMianShaKuCun_RiJun(inventory_base, Manual):
    field_name = u"下游库存"
    col_name = u"纺企棉纱库存_日均"  

class FangQiMianShaKuCun_ZhouJun(inventory_base, Manual):
    field_name = u"下游库存"
    col_name = u"纺企棉纱库存_周均"  

class FangQiMianShaKuCun_YueJun(inventory_base, Manual):
    field_name = u"下游库存"
    col_name = u"纺企棉纱库存_月均"  

class ZhiChangMianShaKuCun_RiJun(inventory_base, Manual):
    field_name = u"下游库存"
    col_name = u"织厂棉纱库存_日均"  

class ZhiChangMianShaKuCun_ZhouJun(inventory_base, Manual):
    field_name = u"下游库存"
    col_name = u"织厂棉纱库存_周均"  

class ZhiChangMianShaKuCun_YueJun(inventory_base, Manual):
    field_name = u"下游库存"
    col_name = u"织厂棉纱库存_月均"  

class ZhiChangPiBuKuCun_RiJun(inventory_base, Manual):
    field_name = u"下游库存"
    col_name = u"织厂坯布库存_日均"  

class ZhiChangPiBuKuCun_ZhouJun(inventory_base, Manual):
    field_name = u"下游库存"
    col_name = u"织厂坯布库存_周均"  

class ZhiChangPiBuKuCun_YueJun(inventory_base, Manual):
    field_name = u"下游库存"
    col_name = u"织厂坯布库存_月均"  


    
if __name__ == "__main__":
    df = MianHuaRiZongShouChuChengJiaoLiang().get_ts()  












    
    
    