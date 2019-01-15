# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 10:48:40 2018

@author: 李弘一萌
"""

import pandas as pd
from datetime import datetime
from .CU_Base import CU_Base
from ...Base.DataType_Base import Manual, Computed, WindData
from ...Base.Plot_Base import Plot_Base
from matplotlib.ticker import FuncFormatter

class sdb_base(CU_Base, Plot_Base):
    table_english_name = "SupplyDemandBalance"
    table_chinese_name = u"供需平衡表"
    
    def output(self):
        print(self.table_english_name)
    
    def get_relevant_df(self, col_list):
        local_col_name_list = sdb_base.get_all_table_classname()
        col_cls_list = []
        for x in col_list:
            col_cls_name = str(CU_Base.get_class_name(x))
            if col_cls_name not in local_col_name_list:
                col_cls_list.append(eval(CU_Base.get_table_class_full_variable(x)))
            else:
                col_cls_list.append(eval(col_cls_name))
        ts_list = [x().get_ts() for x in col_cls_list]
        tmp_table_df = pd.concat(ts_list, axis=1).dropna(how="all")
        return tmp_table_df 



###########################################################################################################################
""" 供给 """    

class QuanQiuKuangShanChanLiang_DangYueZhi(sdb_base, WindData):
    field_name = u"供给"
    col_name = u"全球矿山产量_当月值"    
    wind_code = "S0148686"

class QuanQiuKuangShanChanNeng_DangYueZhi(sdb_base, WindData):
    field_name = u"供给"
    col_name = u"全球矿山产能_当月值"    
    wind_code = "S0148687"

class QuanQiuKuangShanChanNengLiYongLv_DangYueZhi(sdb_base, WindData):
    field_name = u"供给"
    col_name = u"全球矿山产能利用率_当月值"    
    wind_code = "S0148688"

class QuanQiuYuanShengJingLianTongChanLiang_DangYueZhi(sdb_base, WindData):
    field_name = u"供给"
    col_name = u"全球原生精炼铜产量_当月值"    
    wind_code = "S0148689"

class QuanQiuZaiShengJingLianTongChanLiang_DangYueZhi(sdb_base, WindData):
    field_name = u"供给"
    col_name = u"全球再生精炼铜产量_当月值"    
    wind_code = "S0148690"

class QuanQiuJingLianTongChanLiang_YuanShengPlusZaiSheng_DangYueZhi(sdb_base, WindData):
    field_name = u"供给"
    col_name = u"全球精炼铜产量(原生+再生)_当月值"    
    wind_code = "S0148691"

class QuanQiuJingLianTongChanNeng_DangYueZhi(sdb_base, WindData):
    field_name = u"供给"
    col_name = u"全球精炼铜产能_当月值"    
    wind_code = "S0148692"

class QuanQiuJingLianTongChanNengLiYongLv_DangYueZhi(sdb_base, WindData):
    field_name = u"供给"
    col_name = u"全球精炼铜产能利用率_当月值"    
    wind_code = "S0148693"







###########################################################################################################################
""" 供需缺口 """   
    
class QuanQiuJingTongGuoShengOrQueKou_DangYueZhi(sdb_base, WindData):
    field_name = u"供需缺口"
    col_name = u"全球精铜过剩/缺口_当月值"    
    wind_code = "S0148697"
    
class QuanQiuJingTongGuoShengOrQueKou_JiDiao_DangYueZhi(sdb_base, WindData):
    field_name = u"供需缺口"
    col_name = u"全球精铜过剩/缺口_季调_当月值"    
    wind_code = "S0148698"
    
class TongGongXuPingHeng_WBMS_LeiJiZhi(sdb_base, WindData):
    field_name = u"供需缺口"
    col_name = u"铜供需平衡_WBMS_累计值"    
    wind_code = "S5808559"    
    start_year = 2014
    axhline = 0   
    def seasonal_plot(self):
        tmp_df_interpolated, fig, axis = super(sdb_base, self).seasonal_plot(start_year=self.start_year, 
                                              axhline=self.axhline, mode="month", plot_type="bar")
        axis.set_xticklabels(["", "1-2月", "1-3月", "1-4月", "1-5月", "1-6月", "1-7月", "1-8月", "1-9月", 
                              "1-10月", "1-11月", "1-12月"], fontsize=27, ha="center")
        return tmp_df_interpolated, fig, axis
    
###########################################################################################################################
""" 国内精铜产量 """  
    
class ZhongGuoJingLianTong_TongChanLiang_DangYueZhi(sdb_base, WindData):
    field_name = u"国内精铜产量"
    col_name = u"中国精炼铜(铜)产量_当月值"    
    wind_code = "S0027555"

class ZhongGuoJingLianTong_TongChanLiang_LeiJiZhi(sdb_base, WindData):
    field_name = u"国内精铜产量"
    col_name = u"中国精炼铜(铜)产量_累计值"    
    wind_code = "S0027557"

    
###########################################################################################################################
""" 需求 """  
    
class QuanQiuJingLianTongXiaoFeiLiang_DangYueZhi(sdb_base, WindData):
    field_name = u"需求"
    col_name = u"全球精炼铜消费量_当月值"    
    wind_code = "S0148694"    

###########################################################################################################################
""" 中国进出口贸易 """  
    
class ShangHaiDianJieTongZuiDiYiJia_CIF(sdb_base, WindData):
    field_name = u"中国进出口贸易"
    col_name = u"上海电解铜最低溢价_CIF"    
    wind_code = "S5807320"    

class ShangHaiDianJieTongZuiGaoYiJia_CIF(sdb_base, WindData):
    field_name = u"中国进出口贸易"
    col_name = u"上海电解铜最高溢价_CIF"    
    wind_code = "S5807321" 

class JingLianTongZhongGuoJinKouShuLiang_DangYueZhi(sdb_base, WindData):
    field_name = u"中国进出口贸易"
    col_name = u"精炼铜中国进口数量_当月值"    
    wind_code = "S0116244" 
    




if __name__ == "__main__":
    a = PCUSheHuiKuCun().seasonal_plot()
    
    
    
    
    
    
    
    
    
    