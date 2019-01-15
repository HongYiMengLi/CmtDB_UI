# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 10:44:58 2018

@author: 李弘一萌
"""

import pandas as pd
from datetime import datetime
from .TA_Base import TA_Base
from . import TA_Macro
from . import TA_SpotPrice
from . import TA_FuturesPrice
from ...Base.DataType_Base import Manual, Computed, WindData
from ...Base.Plot_Base import Plot_Base
from matplotlib.ticker import FuncFormatter

class upstream_base(TA_Base, Plot_Base):
    table_english_name = "Upstream"
    table_chinese_name = u"上游"
    
    def output(self):
        print("Upstream")
    
    def get_relevant_df(self, col_list):
        local_col_name_list = upstream_base.get_all_table_classname()
        col_cls_list = []
        for x in col_list:
            col_cls_name = str(TA_Base.get_class_name(x))
            if col_cls_name not in local_col_name_list:
                col_cls_list.append(eval(TA_Base.get_table_class_full_variable(x)))
            else:
                col_cls_list.append(eval(col_cls_name))
        ts_list = [x().get_ts() for x in col_cls_list]
        tmp_table_df = pd.concat(ts_list, axis=1).dropna(how="all")
        return tmp_table_df
    
###########################################################################################################################
""" 美金价 """  
     

class WTIJieSuanJia(upstream_base, WindData):
    field_name = u"美金价"
    col_name = u"WTI结算价"
    wind_code = "M0000005"
    
class BrentJieSuanJia(upstream_base, WindData):
    field_name = u"美金价"
    col_name = u"BRENT结算价"
    wind_code = "S0031525"
    
class ShiNaoYouJiaGe_CFR_RiBen(upstream_base, WindData):
    field_name = u"美金价"
    col_name = u"石脑油价格_CFR_日本"
    wind_code = "S5428960"
 
class MXJiaGe_CFR_TaiWan(upstream_base, WindData):
    field_name = u"美金价"
    col_name = u"MX价格_CFR_台湾"
    wind_code = "S5419003"
 
class MXJiaGe_FOB_HanGuo(upstream_base, WindData):
    field_name = u"美金价"
    col_name = u"MX价格_FOB_韩国"
    wind_code = "S5400548"
 
class PXJiaGe_CFR_TaiWan(upstream_base, WindData):
    field_name = u"美金价"
    col_name = u"PX价格_CFR_台湾"
    wind_code = "S5419005"
 
class PXJiaGe_FOB_HanGuo(upstream_base, WindData):
    field_name = u"美金价"
    col_name = u"PX价格_FOB_韩国"  
    wind_code = "S5419004"
 
class YiXiJiaGe_CFR_DongBeiYa(upstream_base, WindData):
    field_name = u"美金价"
    col_name = u"乙烯价格_CFR_东北亚"
    wind_code = "S5400549"
     
""" 计算指标 """ 

class BrentMultipliesTongDunBi(upstream_base, Computed):
    field_name = u"美金价"
    col_name = u"BRENT*桶吨比"   
    def get_ts_whole_progress(self):
        relevant_col_list = [u"BRENT结算价"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"BRENT结算价"] * 7.35
        return tmp_total  
    
###########################################################################################################################
""" 人民币价 """  

class MXXianHuoJia_HuaDong(upstream_base, WindData):
    field_name = u"人民币价"
    col_name = u"MX现货价_华东"
    wind_code = "S5438976"


class PXChuChangJia_ShangHaiShiHua(upstream_base, WindData):
    field_name = u"人民币价"
    col_name = u"PX出厂价_上海石化"
    wind_code = "S5439004"
    

class SCYuanYouJieSuanJia(upstream_base, WindData):
    field_name = u"人民币价"
    col_name = u"SC原油结算价"
    wind_code = "S0265092"
    
###########################################################################################################################
""" MEG价格 """   

class MEGXianHuoJiaGe_CFR_ZhongGuoZhuGang(upstream_base, WindData):
    field_name = u"MEG价格"
    col_name = u"MEG现货价格_CFR_中国主港"
    wind_code = "S5439164"

    
class MEGXianHuoJiaGe_HuaDong(upstream_base, WindData):
    field_name = u"MEG价格"
    col_name = u"MEG现货价格_华东"
    wind_code = "S5439184"

    
class MEGXianHuoJiaGe_HuaNan(upstream_base, WindData):
    field_name = u"MEG价格"
    col_name = u"MEG现货价格_华南"
    wind_code = "S5439183"


###########################################################################################################################
""" 成本 """  
""" 计算指标 """      

class PTAYuanLiaoChengBen(upstream_base, Computed):
    field_name = u"成本"
    col_name = u"PTA原料成本"
    def get_ts_whole_progress(self):
        relevant_col_list = [u"PX价格_CFR_台湾", u"汇卖价_美元兑人民币"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"PX价格_CFR_台湾"] * 0.655 * 1.17 * 1.02 * tmp_total[u"汇卖价_美元兑人民币"]
        return tmp_total    
    
class PTAShengChanChengBen(upstream_base, Computed):
    field_name = u"成本"
    col_name = u"PTA生产成本"
    def get_ts_whole_progress(self):
        relevant_col_list = [u"PTA原料成本"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"PTA原料成本"] + 500
        return tmp_total       

    
###########################################################################################################################
""" PX利润 """  
""" 计算指标 """      

class PXJiaGongLiRun(upstream_base, Computed):
    field_name = u"PX利润"
    col_name = u"PX加工利润"
    start_year = 2014
    def get_ts_whole_progress(self):
        relevant_col_list = [u"PX价格_CFR_台湾", u"石脑油价格_CFR_日本"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"PX价格_CFR_台湾"] - tmp_total[u"石脑油价格_CFR_日本"]
        return tmp_total    

###########################################################################################################################
""" 进口成本 """      
""" 计算指标 """ 
class MEGJinKouChengBen(upstream_base, Computed):
    field_name = u"进口成本"
    col_name = u"MEG进口成本"
    def get_ts_whole_progress(self):
        relevant_col_list = ["MEG现货价格_CFR_中国主港", "汇卖价_美元兑人民币"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"MEG现货价格_CFR_中国主港"] * tmp_total[u"汇卖价_美元兑人民币"] * 1.055 * 1.17
        return tmp_total  
    
    
###########################################################################################################################
""" 进口利润 """      
""" 计算指标 """      

class PXJinKouLiRun(upstream_base, Computed):
    field_name = u"进口利润"
    col_name = u"PX进口利润"
    def get_ts_whole_progress(self):
        relevant_col_list = [u"PX价格_CFR_台湾", u"石脑油价格_CFR_日本"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"PX价格_CFR_台湾"] - tmp_total[u"石脑油价格_CFR_日本"]
        return tmp_total    
    
class MEGJinKouLiRun(upstream_base, Computed):
    field_name = u"进口利润"
    col_name = u"MEG进口利润"
    def get_ts_whole_progress(self):
        relevant_col_list = ["MEG现货价格_华东", "MEG进口成本"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"MEG现货价格_华东"] - tmp_total[u"MEG进口成本"]
        return tmp_total      

    
###########################################################################################################################
""" 生产利润 """  
""" 计算指标 """      

class PTAShengChanLiRun(upstream_base, Computed):
    field_name = u"生产利润"
    col_name = u"PTA生产利润"
    def get_ts_whole_progress(self):
        relevant_col_list = [u"PTA生产成本", u"PTA现货价格_华东"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"PTA现货价格_华东"] - tmp_total[u"PTA生产成本"]
        return tmp_total    
    
###########################################################################################################################
""" 加工费 """  
""" 计算指标 """      

class PTAXianHuoJiaGongFei(upstream_base, Computed):
    field_name = u"加工费"
    col_name = u"PTA现货加工费"
    start_year = 2015
    def get_ts_whole_progress(self):
        relevant_col_list = [u"PTA现货价格_华东", u"PTA原料成本"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"PTA现货价格_华东"] - tmp_total[u"PTA原料成本"]
        return tmp_total
    
class PTA01JiaGongFei(upstream_base, Computed):
    field_name = u"加工费"
    col_name = u"PTA01加工费"
    start_year = 2015
    def get_ts_whole_progress(self):
        relevant_col_list = [u"PTA01合约收盘价", u"PTA原料成本"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"PTA01合约收盘价"] - tmp_total[u"PTA原料成本"]
        return tmp_total

class PTA05JiaGongFei(upstream_base, Computed):
    field_name = u"加工费"
    col_name = u"PTA05加工费"
    def get_ts_whole_progress(self):
        relevant_col_list = [u"PTA05合约收盘价", u"PTA原料成本"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"PTA05合约收盘价"] - tmp_total[u"PTA原料成本"]
        return tmp_total

class PTA09JiaGongFei(upstream_base, Computed):
    field_name = u"加工费"
    col_name = u"PTA09加工费"
    def get_ts_whole_progress(self):
        relevant_col_list = [u"PTA09合约收盘价", u"PTA原料成本"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"PTA09合约收盘价"] - tmp_total[u"PTA原料成本"]
        return tmp_total    
    
    
if __name__ == "__main__":
    df = PXJiaGongLiRun().seasonal_plot()    
    
    
    
    
    
    
    
    
    
    
    
    
    
    