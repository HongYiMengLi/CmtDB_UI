# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 16:35:12 2018

@author: 李弘一萌
"""

import pandas as pd
from datetime import datetime
from .RB_Base import RB_Base
from ...Base.DataType_Base import Manual, Computed, WindData
from ...Base.Plot_Base import Plot_Base
from matplotlib.ticker import FuncFormatter

class spot_price_base(RB_Base, Plot_Base):
    table_english_name = "SpotPrice"
    table_chinese_name = u"现货价格"
    
    def output(self):
        print("SpotPrice")
    
    def get_relevant_df(self, col_list):
        local_col_name_list = spot_price_base.get_all_table_classname()
        col_cls_list = []
        for x in col_list:
            col_cls_name = str(RB_Base.get_class_name(x))
            if col_cls_name not in local_col_name_list:
                col_cls_list.append(eval(RB_Base.get_table_class_full_variable(x)))
            else:
                col_cls_list.append(eval(col_cls_name))
        ts_list = [x().get_ts() for x in col_cls_list]
        tmp_table_df = pd.concat(ts_list, axis=1).dropna(how="all")
        return tmp_table_df  
    
###########################################################################################################################
""" 出口现货报价 """    

class LuoWenChuKouFOBBaoJia_HRB400_ShangHaiGang(spot_price_base, Manual):
    field_name = u"出口现货报价"
    col_name = u"螺纹出口FOB报价_HRB400_上海港"

class LuoWenChuKouFOBBaoJia_HRB400_TianJinGang(spot_price_base, Manual):
    field_name = u"出口现货报价"
    col_name = u"螺纹出口FOB报价_HRB400_天津港"
    


###########################################################################################################################
""" 钢厂出厂价 """      

class LuoWenChuChangHanShuiJia_HRB400_14To25mm_ShaGang(spot_price_base, WindData):
    field_name = u"钢厂出厂价"
    col_name = u"螺纹出厂含税价_HRB400_14-25mm_沙钢"
    wind_code = "S5707351"
    

###########################################################################################################################
""" 钢坯价格 """      

class FangPiXianHuoJiaGe_Q235B_TangShan(spot_price_base, WindData):
    field_name = u"钢坯价格"
    col_name = u"方坯现货价格_Q235B_唐山"
    wind_code = "S0143493"    

###########################################################################################################################
""" 废钢价格 """      

class FeiGangShiChangJia_6To8mm_TangShan(spot_price_base, WindData):
    field_name = u"废钢价格"
    col_name = u"废钢市场价(含税)_6-8mm_唐山"
    wind_code = "S5700017"    
    
###########################################################################################################################
""" 现货市场价格 """    

class GaoXianXianHuoJiaGe_HPB235_8mm_ShangHai(spot_price_base, Manual):
    field_name = u"现货市场价格"
    col_name = u"高线现货价格_HPB235_8.0mm_上海"

class GaoXianXianHuoJiaGe_HPB235_8mm_HangZhou(spot_price_base, Manual):
    field_name = u"现货市场价格"
    col_name = u"高线现货价格_HPB235_8.0mm_杭州"
    
class LuoWenGangXianHuoJiaGe_HRB400_16To25mm_QuanGuo(spot_price_base, WindData):
    field_name = u"现货市场价格"
    col_name = u"螺纹钢现货价格_HRB400_16-25mm_全国"
    wind_code = "S5914455"        
    
class LuoWenGangXianHuoJiaGe_HRB400_20mm_ShangHai(spot_price_base, WindData):
    field_name = u"现货市场价格"
    col_name = u"螺纹钢现货价格_HRB400_20mm_上海"
    wind_code = "S0073209"       
    
class LuoWenGangXianHuoJiaGe_HRB400_20mm_TianJin(spot_price_base, WindData):
    field_name = u"现货市场价格"
    col_name = u"螺纹钢现货价格_HRB400_20mm_天津"
    wind_code = "S0033263"       
    
class LuoWenGangXianHuoJiaGe_HRB400_20mm_HangZhou(spot_price_base, WindData):
    field_name = u"现货市场价格"
    col_name = u"螺纹钢现货价格_HRB400_20mm_杭州"
    wind_code = "S5704863"       
    
class LuoWenGangXianHuoJiaGe_HRB400_20mm_GuangZhou(spot_price_base, WindData):
    field_name = u"现货市场价格"
    col_name = u"螺纹钢现货价格_HRB400_20mm_广州"
    wind_code = "S5704864"       
    
    
    
    
    

if __name__ == "__main__":
    ts = PRBXianHuoJiaGe_HuaDong().get_ts()