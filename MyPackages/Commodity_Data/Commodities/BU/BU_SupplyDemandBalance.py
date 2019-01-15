# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 10:48:40 2018

@author: 李弘一萌
"""

import pandas as pd
from datetime import datetime
from .BU_Base import BU_Base
from ...Base.DataType_Base import Manual, Computed, WindData
from ...Base.Plot_Base import Plot_Base
from matplotlib.ticker import FuncFormatter

class sdb_base(BU_Base, Plot_Base):
    table_english_name = "SupplyDemandBalance"
    table_chinese_name = u"供需平衡表"
    
    def output(self):
        print(self.table_english_name)
    
    def get_relevant_df(self, col_list):
        local_col_name_list = sdb_base.get_all_table_classname()
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
""" 进出口 """    

class LiQingJinKouLiang(sdb_base, Manual):
    field_name = u"进出口"
    col_name = u"沥青进口量"
    
class LiQingChuKouLiang(sdb_base, Manual):
    field_name = u"进出口"
    col_name = u"沥青出口量"

class LiQingJingJinKou(sdb_base, Computed):
    field_name = u"进出口"
    col_name = u"沥青净进口"    
    def get_ts_whole_progress(self):
        relevant_col_list = [u"沥青进口量", u"沥青出口量"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"沥青进口量"] - tmp_total[u"沥青出口量"] 
        return tmp_total

class ShiYouLiQing_27132000_JinKouShuLiang(sdb_base, WindData):
    field_name = u"国内现货价格"
    col_name = u"石油沥青_27132000_进口数量"
    wind_code = "S5437978"
    
###########################################################################################################################
""" 开工率 """  

class LiQingKaiGongLv_XiBei(sdb_base, Manual):
    field_name = u"开工率"
    col_name = u"沥青开工率_西北"

    def seasonal_plot(self, title=None, start_year=None, axhline=None):
        tmp_df_interpolated, fig, axis = super(sdb_base, self).seasonal_plot(title=title, start_year=start_year)
        axis.yaxis.set_major_formatter(FuncFormatter(lambda y, _: '{:.0%}'.format(y)))
        return tmp_df_interpolated, fig, axis

class LiQingKaiGongLv_DongBei(sdb_base, Manual):
    field_name = u"开工率"
    col_name = u"沥青开工率_东北"
    def seasonal_plot(self, title=None, start_year=None, axhline=None):
        tmp_df_interpolated, fig, axis = super(sdb_base, self).seasonal_plot(title=title, start_year=start_year)
        axis.yaxis.set_major_formatter(FuncFormatter(lambda y, _: '{:.0%}'.format(y)))
        return tmp_df_interpolated, fig, axis

class LiQingKaiGongLv_ShanDong(sdb_base, Manual):
    field_name = u"开工率"
    col_name = u"沥青开工率_山东"
    def seasonal_plot(self, title=None, start_year=None, axhline=None):
        tmp_df_interpolated, fig, axis = super(sdb_base, self).seasonal_plot(title=title, start_year=start_year)
        axis.yaxis.set_major_formatter(FuncFormatter(lambda y, _: '{:.0%}'.format(y)))
        return tmp_df_interpolated, fig, axis

class LiQingKaiGongLv_ChangSanJiao(sdb_base, Manual):
    field_name = u"开工率"
    col_name = u"沥青开工率_长三角"
    def seasonal_plot(self, title=None, start_year=None, axhline=None):
        tmp_df_interpolated, fig, axis = super(sdb_base, self).seasonal_plot(title=title, start_year=start_year)
        axis.yaxis.set_major_formatter(FuncFormatter(lambda y, _: '{:.0%}'.format(y)))
        return tmp_df_interpolated, fig, axis

class LiQingKaiGongLv_HuaNan(sdb_base, Manual):
    field_name = u"开工率"
    col_name = u"沥青开工率_华南"
    def seasonal_plot(self, title=None, start_year=None, axhline=None):
        tmp_df_interpolated, fig, axis = super(sdb_base, self).seasonal_plot(title=title, start_year=start_year)
        axis.yaxis.set_major_formatter(FuncFormatter(lambda y, _: '{:.0%}'.format(y)))
        return tmp_df_interpolated, fig, axis

class LiQingKaiGongLv_LiQingChang(sdb_base, Manual):
    field_name = u"开工率"
    col_name = u"沥青开工率_沥青厂"
    def seasonal_plot(self, title=None, start_year=None, axhline=None):
        tmp_df_interpolated, fig, axis = super(sdb_base, self).seasonal_plot(title=title, start_year=start_year)
        axis.yaxis.set_major_formatter(FuncFormatter(lambda y, _: '{:.0%}'.format(y)))
        return tmp_df_interpolated, fig, axis
    
###########################################################################################################################
""" 月度产量 """  

class LiQingChanLiang_ZhongGuo(sdb_base, Manual):
    field_name = u"月度产量"
    col_name = u"沥青月度产量_中国"
    
class LiQingChanLiang_ZhongShiYou(sdb_base, Manual):
    field_name = u"月度产量"
    col_name = u"沥青月度产量_中石油"    

class LiQingChanLiang_ZhongShiHua(sdb_base, Manual):
    field_name = u"月度产量"
    col_name = u"沥青月度产量_中石化"

class LiQingChanLiang_ZhongHaiYou(sdb_base, Manual):
    field_name = u"月度产量"
    col_name = u"沥青月度产量_中海油"

class LiQingChanLiang_DiFangLianChang(sdb_base, Manual):
    field_name = u"月度产量"
    col_name = u"沥青月度产量_地方炼厂"
    
class ShiYouLiQingChanLiang(sdb_base, WindData):
    field_name = u"月度产量"
    col_name = u"石油沥青月度产量"
    wind_code = "S0073067"
          
###########################################################################################################################
""" 产能 """  

class LiQingChanNeng_QuanGuo(sdb_base, Manual):
    field_name = u"产能"
    col_name = u"沥青产能_全国"

class LiQingChanNeng_HuaDong(sdb_base, Manual):
    field_name = u"产能"
    col_name = u"沥青产能_华东"

class LiQingChanNeng_ShanDong(sdb_base, Manual):
    field_name = u"产能"
    col_name = u"沥青产能_山东"

class LiQingChanNeng_HuaNanXiNan(sdb_base, Manual):
    field_name = u"产能"
    col_name = u"沥青产能_华南西南"

###########################################################################################################################
""" 日度产量 """  

class LiQingRiDuChanLiang_LiShiZhi_QuanGuo(sdb_base, Manual):
    field_name = u"日度产量"
    col_name = u"沥青日度产量_历史值_全国"
    def seasonal_plot(self, title=None, start_year=None, axhline=None):
        tmp_df_interpolated, fig, axis = super(sdb_base, self).seasonal_plot(title=title, start_year=start_year)
        axis.yaxis.set_major_formatter(FuncFormatter(lambda y, _: '{:.2f}'.format(y)))
        return tmp_df_interpolated, fig, axis

class LiQingRiDuChanLiang_LiShiZhi_HuaDong(sdb_base, Manual):
    field_name = u"日度产量"
    col_name = u"沥青日度产量_历史值_华东"
    def seasonal_plot(self, title=None, start_year=None, axhline=None):
        tmp_df_interpolated, fig, axis = super(sdb_base, self).seasonal_plot(title=title, start_year=start_year)
        axis.yaxis.set_major_formatter(FuncFormatter(lambda y, _: '{:.2f}'.format(y)))
        return tmp_df_interpolated, fig, axis
    
class LiQingRiDuChanLiang_LiShiZhi_ShanDong(sdb_base, Manual):
    field_name = u"日度产量"
    col_name = u"沥青日度产量_历史值_山东"
    def seasonal_plot(self, title=None, start_year=None, axhline=None):
        tmp_df_interpolated, fig, axis = super(sdb_base, self).seasonal_plot(title=title, start_year=start_year)
        axis.yaxis.set_major_formatter(FuncFormatter(lambda y, _: '{:.2f}'.format(y)))
        return tmp_df_interpolated, fig, axis
    
class LiQingRiDuChanLiang_LiShiZhi_HuaNanXiNan(sdb_base, Manual):
    field_name = u"日度产量"
    col_name = u"沥青日度产量_历史值_华南西南"
    def seasonal_plot(self, title=None, start_year=None, axhline=None):
        tmp_df_interpolated, fig, axis = super(sdb_base, self).seasonal_plot(title=title, start_year=start_year)
        axis.yaxis.set_major_formatter(FuncFormatter(lambda y, _: '{:.2f}'.format(y)))
        return tmp_df_interpolated, fig, axis
        
    
class LiQingRiDuChanLiangYuGu_QuanGuo(sdb_base, Computed):
    field_name = u"日度产量"
    col_name = u"沥青日度产量预估_全国"
    def get_ts_whole_progress(self):        
        relevant_col_list = [u"沥青日度产量_历史值_全国", u"沥青产能_全国", u"沥青开工率_沥青厂"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total["预估"] = tmp_total["沥青产能_全国"].fillna(method="ffill") * tmp_total["沥青开工率_沥青厂"].fillna(method="bfill") / 365
        tmp_ts1 = tmp_total["预估"].resample("D").bfill()
        tmp_ts = tmp_total["沥青日度产量_历史值_全国"].dropna()
        tmp_ts = pd.concat([tmp_ts, tmp_ts1[tmp_ts1.index>tmp_ts.index[-1]]])
        tmp_ts.name = self.col_name
        tmp_total = pd.concat([tmp_total, tmp_ts], axis=1, sort=False)
        return tmp_total  
    def seasonal_plot(self, title=None, start_year=None, axhline=None):
        tmp_df_interpolated, fig, axis = super(sdb_base, self).seasonal_plot(title=title, start_year=start_year)
        axis.yaxis.set_major_formatter(FuncFormatter(lambda y, _: '{:.2f}'.format(y)))
        return tmp_df_interpolated, fig, axis
        
    
class LiQingRiDuChanLiangYuGu_HuaDong(sdb_base, Computed):
    field_name = u"日度产量"
    col_name = u"沥青日度产量预估_华东"
    def get_ts_whole_progress(self):
        relevant_col_list = [u"沥青日度产量_历史值_华东", u"沥青产能_华东", u"沥青开工率_长三角"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total["预估"] = tmp_total["沥青产能_华东"].fillna(method="ffill") * tmp_total["沥青开工率_长三角"].fillna(method="bfill") / 365
        tmp_ts1 = tmp_total["预估"].resample("D").bfill()
        tmp_ts = tmp_total["沥青日度产量_历史值_华东"].dropna()
        tmp_ts = pd.concat([tmp_ts, tmp_ts1[tmp_ts1.index>tmp_ts.index[-1]]])
        tmp_ts.name = self.col_name
        tmp_total = pd.concat([tmp_total, tmp_ts], axis=1, sort=False)
        return tmp_total  
    def seasonal_plot(self, title=None, start_year=None, axhline=None):
        tmp_df_interpolated, fig, axis = super(sdb_base, self).seasonal_plot(title=title, start_year=start_year)
        axis.yaxis.set_major_formatter(FuncFormatter(lambda y, _: '{:.2f}'.format(y)))
        return tmp_df_interpolated, fig, axis
        
    
class LiQingRiDuChanLiangYuGu_ShanDong(sdb_base, Computed):
    field_name = u"日度产量"
    col_name = u"沥青日度产量预估_山东"
    def get_ts_whole_progress(self):
        relevant_col_list = [u"沥青日度产量_历史值_山东", u"沥青产能_山东", u"沥青开工率_山东"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total["预估"] = tmp_total["沥青产能_山东"].fillna(method="ffill") * tmp_total["沥青开工率_山东"].fillna(method="bfill") / 365
        tmp_ts1 = tmp_total["预估"].resample("D").bfill()
        tmp_ts = tmp_total["沥青日度产量_历史值_山东"].dropna()
        tmp_ts = pd.concat([tmp_ts, tmp_ts1[tmp_ts1.index>tmp_ts.index[-1]]])
        tmp_ts.name = self.col_name
        tmp_total = pd.concat([tmp_total, tmp_ts], axis=1, sort=False)
        return tmp_total  
    def seasonal_plot(self, title=None, start_year=None, axhline=None):
        tmp_df_interpolated, fig, axis = super(sdb_base, self).seasonal_plot(title=title, start_year=start_year)
        axis.yaxis.set_major_formatter(FuncFormatter(lambda y, _: '{:.2f}'.format(y)))
        return tmp_df_interpolated, fig, axis
        
    
class LiQingRiDuChanLiangYuGu_HuaNanXiNan(sdb_base, Computed):
    field_name = u"日度产量"
    col_name = u"沥青日度产量预估_华南西南"
    def get_ts_whole_progress(self):
        relevant_col_list = [u"沥青日度产量_历史值_华南西南", u"沥青产能_华南西南", u"沥青开工率_华南"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total["预估"] = tmp_total["沥青产能_华南西南"].fillna(method="ffill") * tmp_total["沥青开工率_华南"].fillna(method="bfill") / 365
        tmp_ts1 = tmp_total["预估"].resample("D").bfill()
        tmp_ts = tmp_total["沥青日度产量_历史值_华南西南"].dropna()
        tmp_ts = pd.concat([tmp_ts, tmp_ts1[tmp_ts1.index>tmp_ts.index[-1]]])
        tmp_ts.name = self.col_name
        tmp_total = pd.concat([tmp_total, tmp_ts], axis=1, sort=False)
        return tmp_total  
    def seasonal_plot(self, title=None, start_year=None, axhline=None):
        tmp_df_interpolated, fig, axis = super(sdb_base, self).seasonal_plot(title=title, start_year=start_year)
        axis.yaxis.set_major_formatter(FuncFormatter(lambda y, _: '{:.2f}'.format(y)))
        return tmp_df_interpolated, fig, axis
        
    
###########################################################################################################################
""" 表观消费量 """ 

class LiQingBiaoGuanXiaoFeiLiang(sdb_base, Computed):
    field_name = u"表观消费量"
    col_name = u"沥青表观消费量"    
    def get_ts_whole_progress(self):
        relevant_col_list = [u"沥青净进口", u"沥青月度产量_中国"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total["沥青月度产量_中国"] + tmp_total["沥青净进口"]
        return tmp_total  
    
class LiQingBiaoGuanXiaoFeiLiangZengSu(sdb_base, Computed):
    field_name = u"表观消费量"
    col_name = u"沥青表观消费量增速"    
    def get_ts_whole_progress(self):
        relevant_col_list = [u"沥青表观消费量"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"沥青表观消费量"] / tmp_total[u"沥青表观消费量"].shift(12) - 1
        return tmp_total      


if __name__ == "__main__":
    a = LiQingRiDuChanLiangYuGu_HuaNanXiNan().get_ts()
    
    
    
    
    
    
    
    
    
    