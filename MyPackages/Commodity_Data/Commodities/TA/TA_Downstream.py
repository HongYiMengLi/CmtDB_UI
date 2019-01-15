# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 10:45:53 2018

@author: 李弘一萌
"""

import pandas as pd
from datetime import datetime
from .TA_Base import TA_Base
from . import TA_SpotPrice
from . import TA_Upstream
from ...Base.DataType_Base import Manual, Computed, WindData
from ...Base.Plot_Base import Plot_Base
from matplotlib.ticker import FuncFormatter

class downstream_base(TA_Base, Plot_Base):
    table_english_name = "Downstream"
    table_chinese_name = u"下游"
    
    def output(self):
        print("Downstream")
    
    def get_relevant_df(self, col_list):
        local_col_name_list = downstream_base.get_all_table_classname()
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
""" 销量 """

class QingFangChengXiaoLiang(downstream_base, Manual):
    field_name = u"销量"
    col_name = u"轻纺城销量"

class ChangXianZhiWuXiaoLiang(downstream_base, Manual):
    field_name = u"销量"
    col_name = u"长纤织物销量"
    
class DuanXianZhiWuXiaoLiang(downstream_base, Manual):
    field_name = u"销量"
    col_name = u"短纤织物销量"




    
###########################################################################################################################
""" 产销率 """

class ChangSiZuiDiChanXiaoLv(downstream_base, WindData):
    field_name = u"产销率"
    col_name = u"长丝最低产销率"
    wind_code = "S5440920"
    
class ChangSiZuiGaoChanXiaoLv(downstream_base, WindData):
    field_name = u"产销率"
    col_name = u"长丝最高产销率"
    wind_code = "S5440919"
   
class DuanXianZuiDiChanXiaoLv(downstream_base, WindData):
    field_name = u"产销率"
    col_name = u"短纤最低产销率"
    wind_code = "S5440918"
   
class DuanXianZuiGaoChanXiaoLv(downstream_base, WindData):
    field_name = u"产销率"
    col_name = u"短纤最高产销率"
    wind_code = "S5440917"
   
""" 计算指标 """
    
class ChangSiPingJunChanXiaoLv(downstream_base, Computed):
    field_name = u"产销率"
    col_name = u"长丝平均产销率"
    def get_ts_whole_progress(self):
        relevant_col_list = [u"长丝最低产销率", u"长丝最高产销率"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total.mean(axis=1)
        return tmp_total 


class DuanSiPingJunChanXiaoLv(downstream_base, Computed):
    field_name = u"产销率"
    col_name = u"短纤平均产销率"
    def get_ts_whole_progress(self):
        relevant_col_list = [u"短纤最低产销率", u"短纤最高产销率"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total.mean(axis=1)
        return tmp_total    

    
class DiLunChangSiChanXiaoLv_15TianPingJun(downstream_base, Computed):
    field_name = u"产销率"
    col_name = u"涤纶长丝产销率_15天平均"
    start_year = 2015
    def get_ts_whole_progress(self):
        relevant_col_list = [u"长丝平均产销率"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"长丝平均产销率"].rolling(15).mean()
        return tmp_total 

    
class DiLunDuanXianChanXiaoLv_15TianPingJun(downstream_base, Computed):
    field_name = u"产销率"
    col_name = u"涤纶短纤产销率_15天平均"
    def get_ts_whole_progress(self):
        relevant_col_list = [u"短纤平均产销率"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"短纤平均产销率"].rolling(15).mean()
        return tmp_total 

 
    
###########################################################################################################################
""" 成交量 """
""" 计算指标 """

class QingFangChengChengJiaoLiang_15TianPingJun(downstream_base, Computed):
    field_name = u"成交量"
    col_name = u"轻纺城成交量_15天平均"
    def get_ts_whole_progress(self):
        relevant_col_list = [u"轻纺城销量"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"轻纺城销量"].rolling(15).mean()
        return tmp_total
    
    
    
###########################################################################################################################
""" 聚酯价格 """

class JuZhiQiePianJiaGe_PingJi_FOBZhongGuo(downstream_base, WindData):
    field_name = u"聚酯价格"
    col_name = u"聚酯切片价格_瓶级_FOB_中国"
    wind_code = "S5439962"    
    
class JuZhiQiePianJiaGe_PingJi_HuaDong(downstream_base, WindData):
    field_name = u"聚酯价格"
    col_name = u"聚酯切片价格_瓶级_华东"
    wind_code = "S5439965" 

class JuZhiQiePianJiaGe_PingJi_YouGuangQiePian_HuaDong(downstream_base, WindData):
    field_name = u"聚酯价格"
    col_name = u"聚酯切片价格_有光切片_华东"
    wind_code = "S5439988" 

class JuZhiQiePianJiaGe_PingJi_BanGuangQiePian_HuaDong(downstream_base, WindData):
    field_name = u"聚酯价格"
    col_name = u"聚酯切片价格_半光切片_华东"
    wind_code = "S5439987" 

class DiLunPOY150DJiaGe(downstream_base, WindData):
    field_name = u"聚酯价格"
    col_name = u"涤纶POY150D价格"
    wind_code = "S5440017" 
    
class DiLunDTY150DJiaGe(downstream_base, WindData):
    field_name = u"聚酯价格"
    col_name = u"涤纶DTY150D价格"
    wind_code = "S5440016" 
    
class DiLunFDY150DJiaGe(downstream_base, WindData):
    field_name = u"聚酯价格"
    col_name = u"涤纶FDY150D价格"
    wind_code = "S5440018" 
    
class ZhiFangDiLunDuanXianJiaGe(downstream_base, WindData):
    field_name = u"聚酯价格"
    col_name = u"直纺涤纶短纤价格"
    wind_code = "S5440021" 

###########################################################################################################################
""" 聚酯成本 """
""" 计算指标 """

class JuZhiYuanLiaoChengBen(downstream_base, Computed):
    field_name = u"聚酯成本"
    col_name = u"聚酯原料成本"
    def get_ts_whole_progress(self):
        relevant_col_list = [u"PTA现货价格_华东",u"MEG现货价格_华东"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"PTA现货价格_华东"] * 0.865 + tmp_total[u"MEG现货价格_华东"] * 0.345
        return tmp_total
    
###########################################################################################################################
""" 聚酯利润 """
""" 计算指标 """

class JuZhiXiaoShouLiRun_PingPian(downstream_base, Computed):
    field_name = u"聚酯利润"
    col_name = u"聚酯销售利润_瓶片"
    def get_ts_whole_progress(self):
        relevant_col_list = [u"聚酯切片价格_瓶级_华东",u"聚酯原料成本"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"聚酯切片价格_瓶级_华东"] - tmp_total[u"聚酯原料成本"] - 350
        return tmp_total

class JuZhiXiaoShouLiRun_QiePian(downstream_base, Computed):
    field_name = u"聚酯利润"
    col_name = u"聚酯销售利润_切片"
    def get_ts_whole_progress(self):
        relevant_col_list = [u"聚酯切片价格_半光切片_华东",u"聚酯原料成本"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"聚酯切片价格_半光切片_华东"] - tmp_total[u"聚酯原料成本"] - 350
        return tmp_total

class POYLiRun(downstream_base, Computed):
    field_name = u"聚酯利润"
    col_name = u"POY利润"
    start_year = 2014
    def get_ts_whole_progress(self):
        relevant_col_list = [u"涤纶POY150D价格",u"聚酯原料成本"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"涤纶POY150D价格"] - tmp_total[u"聚酯原料成本"] - 1000
        return tmp_total

class DTYLiRun(downstream_base, Computed):
    field_name = u"聚酯利润"
    col_name = u"DTY利润"
    def get_ts_whole_progress(self):
        relevant_col_list = [u"涤纶DTY150D价格",u"聚酯原料成本"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"涤纶DTY150D价格"] - tmp_total[u"聚酯原料成本"] - 2300
        return tmp_total

class FDYLiRun(downstream_base, Computed):
    field_name = u"聚酯利润"
    col_name = u"FDY利润"
    def get_ts_whole_progress(self):
        relevant_col_list = [u"涤纶FDY150D价格",u"聚酯原料成本"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"涤纶FDY150D价格"] - tmp_total[u"聚酯原料成本"] - 1400
        return tmp_total

class DiLunDuanXianLiRun(downstream_base, Computed):
    field_name = u"聚酯利润"
    col_name = u"涤纶短纤利润"
    def get_ts_whole_progress(self):
        relevant_col_list = [u"直纺涤纶短纤价格",u"聚酯原料成本"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"直纺涤纶短纤价格"] - tmp_total[u"聚酯原料成本"] - 1200
        return tmp_total


###########################################################################################################################
""" 棉花价格 """

class CFFuturesPrice(downstream_base, WindData):
    field_name = u"棉花价格"
    col_name = u"棉花主力合约收盘价"
    wind_code = "M0066361"  

class MianHuaXianHuoJiaGe_HuaDong(downstream_base, WindData):
    field_name = u"棉花价格"
    col_name = u"棉花现货价格_华东"
    wind_code = "S5005958"  
    
    
    
if __name__ == "__main__":
    ts = DiLunChangSiChanXiaoLv_15TianPingJun().get_ts()
    
    
    
    
    
    
    




    
    
    