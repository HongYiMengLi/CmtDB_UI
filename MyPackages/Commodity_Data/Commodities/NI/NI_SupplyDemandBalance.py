# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 10:48:40 2018

@author: 李弘一萌
"""

import pandas as pd
from datetime import datetime
from .NI_Base import NI_Base
from ...Base.DataType_Base import Manual, Computed, WindData
from ...Base.Plot_Base import Plot_Base
from matplotlib.ticker import FuncFormatter

class sdb_base(NI_Base, Plot_Base):
    table_english_name = "SupplyDemandBalance"
    table_chinese_name = u"供需平衡表"
    
    def output(self):
        print(self.table_english_name)
    
    def get_relevant_df(self, col_list):
        local_col_name_list = sdb_base.get_all_table_classname()
        col_cls_list = []
        for x in col_list:
            col_cls_name = str(NI_Base.get_class_name(x))
            if col_cls_name not in local_col_name_list:
                col_cls_list.append(eval(NI_Base.get_table_class_full_variable(x)))
            else:
                col_cls_list.append(eval(col_cls_name))
        ts_list = [x().get_ts() for x in col_cls_list]
        tmp_table_df = pd.concat(ts_list, axis=1).dropna(how="all")
        return tmp_table_df 



###########################################################################################################################
""" 电解镍产量 """    

class DianJieNieChanLiang_QuanGuo_DangYueZhi(sdb_base, Manual):
    field_name = u"电解镍产量"
    col_name = u"电解镍产量_全国_当月值"    

###########################################################################################################################
""" 镍铁产量 """   

class NieTieChanLiang_NeiMeng_DangYueZhi(sdb_base, WindData):
    field_name = u"镍铁产量"
    col_name = u"镍铁产量_内蒙_当月值"    
    wind_code = "S5708575"

class NieTieChanLiang_ShanDong_DangYueZhi(sdb_base, WindData):
    field_name = u"镍铁产量"
    col_name = u"镍铁产量_山东_当月值"    
    wind_code = "S5708576"
    
class NieTieChanLiang_QiTa_DangYueZhi(sdb_base, WindData):
    field_name = u"镍铁产量"
    col_name = u"镍铁产量_其他_当月值"    
    wind_code = "S5708577"
    
class NieTieChanLiang_JiangSu_DangYueZhi(sdb_base, WindData):
    field_name = u"镍铁产量"
    col_name = u"镍铁产量_江苏_当月值"    
    wind_code = "S5708571"
   
class NieTieChanLiang_LiaoNing_DangYueZhi(sdb_base, WindData):
    field_name = u"镍铁产量"
    col_name = u"镍铁产量_辽宁_当月值"    
    wind_code = "S5708569"
    
class NieTieChanLiang_JinShuDun_QuanGuo_DangYueZhi(sdb_base, WindData):
    field_name = u"镍铁产量"
    col_name = u"镍铁产量(金属吨)_全国_当月值"    
    wind_code = "S5711258"
    
class NieTieChanLiang_QuanGuo_DangYueZhi(sdb_base, WindData):
    field_name = u"镍铁产量"
    col_name = u"镍铁产量_全国_当月值"    
    wind_code = "S5708578"

###########################################################################################################################
""" 镍铁进口数量 """   
    
class NieTieJinKouShuLiang_DangYueZhi(sdb_base, WindData):
    field_name = u"镍铁进口数量"
    col_name = u"镍铁进口数量_当月值"    
    wind_code = "S0062248"
    
class NieTieJinKouShuLiang_YinDuNiXiYa_DangYueZhi(sdb_base, WindData):
    field_name = u"镍铁进口数量"
    col_name = u"镍铁进口数量_印度尼西亚_当月值"    
    wind_code = "S5805023"
    
class NieTieJinKouShuLiang_BaXi_DangYueZhi(sdb_base, WindData):
    field_name = u"镍铁进口数量"
    col_name = u"镍铁进口数量_巴西_当月值"    
    wind_code = "S5805034"
    
class NieTieJinKouShuLiang_GeLunBiYa_DangYueZhi(sdb_base, WindData):
    field_name = u"镍铁进口数量"
    col_name = u"镍铁进口数量_哥伦比亚_当月值"    
    wind_code = "S5805035"
    
class NieTieJinKouShuLiang_XinKaDuoNiYa_DangYueZhi(sdb_base, WindData):
    field_name = u"镍铁进口数量"
    col_name = u"镍铁进口数量_新喀多尼亚_当月值"    
    wind_code = "S5805039"
    
class NieTieJinKouShuLiang_MianDian_DangYueZhi(sdb_base, WindData):
    field_name = u"镍铁进口数量"
    col_name = u"镍铁进口数量_缅甸_当月值"    
    wind_code = "S5810460"

###########################################################################################################################
""" 其他进口数量 """  
    
class JingLianNieJiHeJinJinKouShuLiang_DangYueZhi(sdb_base, WindData):
    field_name = u"其他进口数量"
    col_name = u"精炼镍及合金进口数量_当月值"    
    wind_code = "S0116258"
    
###########################################################################################################################
""" 供应缺口 """  
    
class NieGongXuPingHeng_WBMS_LeiJiZhi(sdb_base, WindData):
    field_name = u"供应缺口"
    col_name = u"镍供需平衡_WBMS_累计值"    
    wind_code = "S5808555"    
    start_year = 2014
    axhline = 0   
    def seasonal_plot(self):
        tmp_df_interpolated, fig, axis = super(sdb_base, self).seasonal_plot(start_year=self.start_year, 
                                              axhline=self.axhline, mode="month", plot_type="bar")
        axis.set_xticklabels(["", "1-2月", "1-3月", "1-4月", "1-5月", "1-6月", "1-7月", "1-8月", "1-9月", 
                              "1-10月", "1-11月", "1-12月"], fontsize=27, ha="center")
        return tmp_df_interpolated, fig, axis
    
###########################################################################################################################
""" 镍铁开工率 """  
    
class NieTieKaiGongLv_LiaoNing_DangYueZhi(sdb_base, WindData):
    field_name = u"镍铁开工率"
    col_name = u"镍铁开工率_辽宁_当月值"    
    wind_code = "S5708369"    

class NieTieKaiGongLv_JiangSu_DangYueZhi(sdb_base, WindData):
    field_name = u"镍铁开工率"
    col_name = u"镍铁开工率_江苏_当月值"    
    wind_code = "S5708371" 

class NieTieKaiGongLv_NeiMeng_DangYueZhi(sdb_base, WindData):
    field_name = u"镍铁开工率"
    col_name = u"镍铁开工率_内蒙_当月值"    
    wind_code = "S5708375" 
    
class NieTieKaiGongLv_ShanDong_DangYueZhi(sdb_base, WindData):
    field_name = u"镍铁开工率"
    col_name = u"镍铁开工率_山东_当月值"    
    wind_code = "S5708376" 
    
class NieTieKaiGongLv_QiTa_DangYueZhi(sdb_base, WindData):
    field_name = u"镍铁开工率"
    col_name = u"镍铁开工率_其他_当月值"    
    wind_code = "S5708377" 

class NieTieKaiGongLv_QuanGuo_DangYueZhi(sdb_base, WindData):
    field_name = u"镍铁开工率"
    col_name = u"镍铁开工率_全国_当月值"    
    wind_code = "S5708378" 




if __name__ == "__main__":
    a = PNISheHuiKuCun().seasonal_plot()
    
    
    
    
    
    
    
    
    
    