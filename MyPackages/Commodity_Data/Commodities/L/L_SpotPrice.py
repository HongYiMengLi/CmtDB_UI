# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 19:05:30 2018

@author: 李弘一萌
"""

import pandas as pd
from datetime import datetime
from .L_Base import L_Base
from . import L_Macro, L_Others
from ...Base.DataType_Base import Manual, Computed, WindData
from ...Base.Plot_Base import Plot_Base
from matplotlib.ticker import FuncFormatter

class spot_price_base(L_Base, Plot_Base):
    table_english_name = "SpotPrice"
    table_chinese_name = u"现货价格"
#    original_db_filepath = data_path + u"LPP价格数据库.xlsx"
    
    def output(self):
        print("SpotPrice")
    
    def get_relevant_df(self, col_list):
        local_col_name_list = spot_price_base.get_all_table_classname()
        col_cls_list = []
        for x in col_list:
            col_cls_name = str(L_Base.get_class_name(x))
            if col_cls_name not in local_col_name_list:
                col_cls_list.append(eval(L_Base.get_table_class_full_variable(x)))
            else:
                col_cls_list.append(eval(col_cls_name))
        ts_list = [x().get_ts() for x in col_cls_list]
        tmp_table_df = pd.concat(ts_list, axis=1).dropna(how="all")
        return tmp_table_df  
        

###########################################################################################################################
""" 美金盘 """     
     
class LLDPE_CFRYuanDong(spot_price_base, WindData):
    field_name = u"美金盘"
    col_name = u"LLDPE:CFR价格_远东"
    wind_code = "S5400536"
    
class LLDPE_CFRDongNanYa(spot_price_base, WindData):
    field_name = u"美金盘"
    col_name = u"LLDPE:CFR价格_东南亚"
    wind_code = "S5431476"
    
class LDDPE_CFRZhongGuo(spot_price_base, WindData):
    field_name = u"美金盘"
    col_name = u"LLDPE:CFR价格_中国"
    wind_code = "S5431473"


###########################################################################################################################
""" 出口价折算 """  
""" 计算指标 """
 
class LChuKouMeiJinJia(spot_price_base, Computed):
    field_name = u"出口价折算"
    col_name = u"L出口美金价格"    
    def get_ts_whole_progress(self):
        relevant_col_list = [u"LLD膜价格_华东(煤化工)", u"汇卖价(中行):美元兑人民币", u"增值税"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = (tmp_total[u"LLD膜价格_华东(煤化工)"] - (tmp_total[u"LLD膜价格_华东(煤化工)"] / (1 + tmp_total[u"增值税"])) \
                                     * 0.13) / tmp_total[u"汇卖价(中行):美元兑人民币"] + 35
        return tmp_total
    

###########################################################################################################################
""" LDPE废料价格 """  

class LaiZhouEVAOverLvXianEVA(spot_price_base, Manual):
    field_name = u"LDPE废料价格"
    col_name = u"LDPE废料_莱州/莒县EVA"

class JinKou98GaoYaDaJianMoOverHeBeiBaoDingEVA(spot_price_base, Manual):
    field_name = u"LDPE废料价格"
    col_name = u"LDPE废料_进口98高压大件膜/河北保定EVA"
    
###########################################################################################################################
""" 石化出厂价 """  
    
class QiLuShiHua7042(spot_price_base, WindData):
    field_name = u"石化出厂价"
    col_name = u"LLD膜价格_齐鲁石化7042"
    wind_code = "S5431105"
 
class QiLuShiHua2012TN00(spot_price_base, WindData):
    field_name = u"石化出厂价"
    col_name = u"LD膜价格_齐鲁石化2012TN00"
    wind_code = "S5431041"

###########################################################################################################################
""" PEPP国内现货 """  
 
class LLDMoHuaBei(spot_price_base, Manual):
    field_name = u"LLDPE国内现货"
    col_name = u"LLD膜价格_华北"
 
class LLDMoHuaDongMeiHuaGong(spot_price_base, Manual):
    field_name = u"LLDPE国内现货"
    col_name = u"LLD膜价格_华东(煤化工)"
 
class LLDMoZhongShiHua(spot_price_base, Manual):
    field_name = u"LLDPE国内现货"
    col_name = u"LLD膜价格_中石化"
 
class LLDHuaDongJinKou(spot_price_base, Manual):
    field_name = u"LLDPE国内现货"
    col_name = u"LLD价格_华东进口"
 
class LLDMoHuaNan(spot_price_base, Manual):
    field_name = u"LLDPE国内现货"
    col_name = u"LLD膜价格_华南"
 
class LDMoLiao(spot_price_base, Manual):
    field_name = u"LDPE国内现货"
    col_name = u"LD膜料价格_华东"

class HDZhuSu(spot_price_base, Manual):
    field_name = u"HDPE国内现货"
    col_name = u"HD注塑价格_华东"


    
    


    
if __name__ == "__main__":
#    aaa = vars()["field"]
#    print a.__name__
#    aaa = KengKouMei_DongSheng()
#    df = aaa.generate_wind_quote()
    
#    ts = ZengZhiShui().get_ts()
    
#    fig_tuple = PPYouZhiLiRun().seasonal_plot()
#    LPP_Plot.add_month_span(fig_tuple[2], fig_tuple[0], 5)
    
#    a = spot_price_base.get_all_manual_class()
#    b = [x.col_name for x in a.values()]
#    c = [x.field_name for x in a.values()]
#    d = pd.DataFrame([b, c], index=["col", "field"]).T
#    f = d.sort_values(by=["field", "col"])
#    e = pd.DataFrame([], columns=f["col"].values.tolist())
#    e.to_excel(data_path + "update.xlsx", encoding="gbk")
    
    a = LChuKouMeiJinJia().get_ts()
    
    
    
    
    






























