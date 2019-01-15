# -*- coding: utf-8 -*-
"""
Created on Wed Aug 29 09:27:21 2018

@author: 李弘一萌
"""

import pandas as pd
from datetime import datetime
from .PP_Base import PP_Base
from . import PP_Macro
from . import PP_Others
from ...Base.DataType_Base import Manual, Computed, WindData
from ...Base.Plot_Base import Plot_Base
from matplotlib.ticker import FuncFormatter

class spot_price_base(PP_Base, Plot_Base):
    table_english_name = "SpotPrice"
    table_chinese_name = u"现货价格"
    
    def output(self):
        print("SpotPrice")
    
    def get_relevant_df(self, col_list):
        local_col_name_list = spot_price_base.get_all_table_classname()
        col_cls_list = []
        for x in col_list:
            col_cls_name = str(PP_Base.get_class_name(x))
            if col_cls_name not in local_col_name_list:
                col_cls_list.append(eval(PP_Base.get_table_class_full_variable(x)))
            else:
                col_cls_list.append(eval(col_cls_name))
        ts_list = [x().get_ts() for x in col_cls_list]
        tmp_table_df = pd.concat(ts_list, axis=1).dropna(how="all")
        return tmp_table_df  
    
###########################################################################################################################
""" 美金盘 """    

class PPMeiJinPan_CFRYuanDong(spot_price_base, WindData):
    field_name = u"美金盘"
    col_name = u"PP美金盘:CFR价格_远东"
    wind_code = "S5400540"

class PPZhuSu_CFRYuanDong(spot_price_base, WindData):
    field_name = u"美金盘"
    col_name = u"PP注塑:CFR价格_远东"
    wind_code = "S5431482"  
    
class PPZhuSu_CFRDongNanYa(spot_price_base, WindData):
    field_name = u"美金盘"
    col_name = u"PP注塑:CFR价格_东南亚"
    wind_code = "S5431485"        
    
###########################################################################################################################
""" 废料 """  

class HeBeiWenAn(spot_price_base, Manual):
    field_name = u"废料"
    col_name = u"废料价格_河北文安"    
    
###########################################################################################################################
""" 拉丝国内 """      
   
class PPLaSiHuaBei(spot_price_base, Manual):
    field_name = u"拉丝国内"
    col_name = u"PP拉丝价格_华北"

class PPLaSiHuaDong(spot_price_base, Manual):
    field_name = u"拉丝国内"
    col_name = u"PP拉丝价格_华东"

class PPLaSiFuDe(spot_price_base, Manual):
    field_name = u"拉丝国内"
    col_name = u"PP拉丝价格_富德"

class PPLaSiZhongShiHua(spot_price_base, Manual):
    field_name = u"拉丝国内"
    col_name = u"PP拉丝价格_中石化"

class PPLaSiHuaDongJinKou(spot_price_base, Manual):
    field_name = u"拉丝国内"
    col_name = u"PP拉丝价格_华东进口"

class PPZhuSu(spot_price_base, Manual):
    field_name = u"拉丝国内"
    col_name = u"PP注塑价格_华东"

###########################################################################################################################
""" 低融共丙国内 """ 

class PPDiRongGongBing(spot_price_base, Manual):
    field_name = u"低融共丙国内"
    col_name = u"PP低融共丙_华东"

###########################################################################################################################
""" 粉料 """ 
class PPFenLiaoJingBo(spot_price_base, Manual):
    field_name = u"粉料"
    col_name = u"PP粉料价格_京博"    

class PPFenLiaoHuaDong(spot_price_base, Manual):
    field_name = u"粉料"
    col_name = u"PP粉料价格_华东"

###########################################################################################################################
""" 出口价折算 """

class PPChuKouMeiJinJia(spot_price_base, Computed):
    field_name = u"出口价折算"
    col_name = u"PP出口美金价"    
    def get_ts_whole_progress(self):
        relevant_col_list = [u"PP拉丝价格_华东", u"汇卖价(中行):美元兑人民币", u"增值税"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = (tmp_total[u"PP拉丝价格_华东"] - (tmp_total[u"PP拉丝价格_华东"] / (1 + tmp_total[u"增值税"])) \
                                     * 0.13) / tmp_total[u"汇卖价(中行):美元兑人民币"] + 35
        return tmp_total



if __name__ == "__main__":
    ts = PPChuKouMeiJinJia().seasonal_plot()


























 
    
        