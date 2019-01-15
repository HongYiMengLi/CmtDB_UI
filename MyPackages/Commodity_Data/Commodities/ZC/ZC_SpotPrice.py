# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 16:35:12 2018

@author: 李弘一萌
"""

import pandas as pd
from datetime import datetime
from .ZC_Base import ZC_Base
from ...Base.DataType_Base import Manual, Computed, WindData
from ...Base.Plot_Base import Plot_Base
from matplotlib.ticker import FuncFormatter

class spot_price_base(ZC_Base, Plot_Base):
    table_english_name = "SpotPrice"
    table_chinese_name = u"现货价格"
    
    def output(self):
        print("SpotPrice")
    
    def get_relevant_df(self, col_list):
        local_col_name_list = spot_price_base.get_all_table_classname()
        col_cls_list = []
        for x in col_list:
            col_cls_name = str(ZC_Base.get_class_name(x))
            if col_cls_name not in local_col_name_list:
                col_cls_list.append(eval(ZC_Base.get_table_class_full_variable(x)))
            else:
                col_cls_list.append(eval(col_cls_name))
        ts_list = [x().get_ts() for x in col_cls_list]
        tmp_table_df = pd.concat(ts_list, axis=1).dropna(how="all")
        return tmp_table_df  

    
###########################################################################################################################
""" CCI动力煤价格指数 """    

class DongLiMeiJiaGeZhiShu_CCI5500_RMBHanShui(spot_price_base, WindData):
    field_name = u"CCI动力煤价格指数"
    col_name = u"动力煤价格指数_CCI5500_RMB含税"
    wind_code = "S5130993"

class DongLiMeiJiaGeZhiShu_CCI5000_RMBHanShui(spot_price_base, WindData):
    field_name = u"CCI动力煤价格指数"
    col_name = u"动力煤价格指数_CCI5000_RMB含税"
    wind_code = "S5130995"

class DongLiMeiJiaGeZhiShu_CCIJinKou5500_RMBHanShui(spot_price_base, WindData):
    field_name = u"CCI动力煤价格指数"
    col_name = u"动力煤价格指数_CCI进口5500_RMB含税"
    wind_code = "S5130997"

class DongLiMeiJiaGeZhiShu_CCIJinKou5500_USD(spot_price_base, WindData):
    field_name = u"CCI动力煤价格指数"
    col_name = u"动力煤价格指数_CCI进口5500_USD"
    wind_code = "S5130998"    
    
    
###########################################################################################################################
""" 产地市场价 """    

class DongLiMeiShiChangJia_Q5500_YuLinChan_ShanXi(spot_price_base, WindData):
    field_name = u"产地市场价"
    col_name = u"动力煤市场价_Q5500_榆林产_陕西"
    wind_code = "S5131959"    
    
###########################################################################################################################
""" 港口库提价 """    

class DongLiMeiGangKouKuTiJia_Q5500_A20Prct_V28Prct_0Dot7PrctS_AoZhouChan_GuangZhouGang(spot_price_base, WindData):
    field_name = u"港口库提价"
    col_name = u"动力煤港口库提价_Q5500_A20%_V28%_0.7%S_澳洲产_广州港"
    wind_code = "S5101482"    

###########################################################################################################################
""" 港口平仓价 """    

class DongLiMeiGangKouPingCangJia_Q5500_HuangHuaGang(spot_price_base, WindData):
    field_name = u"港口平仓价"
    col_name = u"动力煤港口平仓价_Q5500_黄骅港"
    wind_code = "S5131932"  

class DongLiMeiGangKouPingCangJia_Q5500_QinHuangDaoGang(spot_price_base, WindData):
    field_name = u"港口平仓价"
    col_name = u"动力煤港口平仓价_Q5500_秦皇岛港"
    wind_code = "S5101377"  
    
class DongLiMeiGangKouPingCangJia_Q5000_QinHuangDaoGang(spot_price_base, WindData):
    field_name = u"港口平仓价"
    col_name = u"动力煤港口平仓价_Q5000_秦皇岛港"
    wind_code = "S5131940"  

###########################################################################################################################
""" 国际煤价指数 """    

class ARADongLiMeiZhiShu_OuZhouARAGang(spot_price_base, WindData):
    field_name = u"国际煤价指数"
    col_name = u"ARA动力煤指数_欧洲ARA港"
    wind_code = "S5101710"  

class RBDongLiMeiZhiShu_NanFangLiChaDeGang(spot_price_base, WindData):
    field_name = u"国际煤价指数"
    col_name = u"RB动力煤指数_南方理查德港"
    wind_code = "S5101711"  

class NEWCDongLiMeiZhiShu_AoZhouNiuKaSiErGang(spot_price_base, WindData):
    field_name = u"国际煤价指数"
    col_name = u"NEWC动力煤指数_澳洲纽卡斯尔港"
    wind_code = "S5101712"  

###########################################################################################################################
""" 易煤指数 """    

class DongLiMeiYiMeiZhiShu_Q5500_0Dot8PrctS_BeiFangGang(spot_price_base, WindData):
    field_name = u"易煤指数"
    col_name = u"动力煤易煤指数_Q5500_0.8%S_北方港"
    wind_code = "S5133502"  

class DongLiMeiYiMeiZhiShu_Q5500_0Dot8PrctS_ChangJiangKou(spot_price_base, WindData):
    field_name = u"易煤指数"
    col_name = u"动力煤易煤指数_Q5500_0.8%S_长江口"
    wind_code = "S5133500"  




















    
    
    



if __name__ == "__main__":
    ts = YeHuaQiChuChangJia_JingBoShiHua().get_ts()