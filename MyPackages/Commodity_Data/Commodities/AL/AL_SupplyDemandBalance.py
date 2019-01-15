# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 10:48:40 2018

@author: 李弘一萌
"""

import pandas as pd
from datetime import datetime
from .AL_Base import AL_Base
from ...Base.DataType_Base import Manual, Computed, WindData
from ...Base.Plot_Base import Plot_Base
from matplotlib.ticker import FuncFormatter
import matplotlib.pyplot as plt

class sdb_base(AL_Base, Plot_Base):
    table_english_name = "SupplyDemandBalance"
    table_chinese_name = u"供需平衡表"
    
    def output(self):
        print(self.table_english_name)
    
    def get_relevant_df(self, col_list):
        local_col_name_list = sdb_base.get_all_table_classname()
        col_cls_list = []
        for x in col_list:
            col_cls_name = str(AL_Base.get_class_name(x))
            if col_cls_name not in local_col_name_list:
                col_cls_list.append(eval(AL_Base.get_table_class_full_variable(x)))
            else:
                col_cls_list.append(eval(col_cls_name))
        ts_list = [x().get_ts() for x in col_cls_list]
        tmp_table_df = pd.concat(ts_list, axis=1).dropna(how="all")
        return tmp_table_df 



###########################################################################################################################
""" 电解铝供应 """    

class YuanLvRiJunChanLiang_QuanQiu_DangYueZhi(sdb_base, WindData):
    field_name = u"电解铝供应"
    col_name = u"原铝日均产量_全球_当月值"    
    wind_code = "S0203446"

class YuanLvChanLiang_ZhongOuHeDongOu_DangYueZhi(sdb_base, WindData):
    field_name = u"电解铝供应"
    col_name = u"原铝产量_中欧和东欧_当月值"    
    wind_code = "S0203443"

class YuanLvChanLiang_ZhongGuo_DangYueZhi(sdb_base, WindData):
    field_name = u"电解铝供应"
    col_name = u"原铝产量_中国_当月值"    
    wind_code = "S0203439"

class YuanLvChanLiang_YaZhou_ChuZhongGuo_DangYueZhi(sdb_base, WindData):
    field_name = u"电解铝供应"
    col_name = u"原铝产量_亚洲(除中国)_当月值"    
    wind_code = "S0203437"

class YuanLvChanLiang_XiOu_DangYueZhi(sdb_base, WindData):
    field_name = u"电解铝供应"
    col_name = u"原铝产量_西欧_当月值"    
    wind_code = "S0203442"

class YuanLvChanLiang_QuanQiu_DangYueZhi(sdb_base, WindData):
    field_name = u"电解铝供应"
    col_name = u"原铝产量_全球_当月值"    
    wind_code = "S0203445"

class YuanLvChanLiang_NanMeiZhou_DangYueZhi(sdb_base, WindData):
    field_name = u"电解铝供应"
    col_name = u"原铝产量_南美洲_当月值"    
    wind_code = "S0203441"

class YuanLvChanLiang_HaiHeHui_DangYueZhi(sdb_base, WindData):
    field_name = u"电解铝供应"
    col_name = u"原铝产量_海合会_当月值"    
    wind_code = "S0203438"

class YuanLvChanLiang_FeiZhou_DangYueZhi(sdb_base, WindData):
    field_name = u"电解铝供应"
    col_name = u"原铝产量_非洲_当月值"    
    wind_code = "S0203436"

class YuanLvChanLiang_DaYangZhou_DangYueZhi(sdb_base, WindData):
    field_name = u"电解铝供应"
    col_name = u"原铝产量_大洋洲_当月值"    
    wind_code = "S0203444"

class YuanLvChanLiang_BeiMeiZhou_DangYueZhi(sdb_base, WindData):
    field_name = u"电解铝供应"
    col_name = u"原铝产量_北美洲_当月值"    
    wind_code = "S0203440"

class YuanLvChanLiang_DianJieLv_LeiJiZhi(sdb_base, WindData):
    field_name = u"电解铝供应"
    col_name = u"原铝产量(电解铝)_累计值"    
    wind_code = "S0027565"

class YuanLvChanLiang_DianJieLv_LeiJiTongBi(sdb_base, WindData):
    field_name = u"电解铝供应"
    col_name = u"原铝产量(电解铝)_累计同比"    
    wind_code = "S0027566"

class DianJieLvZongChanNeng_ALD(sdb_base, WindData):
    field_name = u"电解铝供应"
    col_name = u"电解铝总产能_ALD"    
    wind_code = "S5809466"

class DianJieLvZaiChanChanNeng_ALD(sdb_base, WindData):
    field_name = u"电解铝供应"
    col_name = u"电解铝在产产能_ALD"    
    wind_code = "S5809465"

class DianJieLvKaiGongLv_ALD(sdb_base, WindData):
    field_name = u"电解铝供应"
    col_name = u"电解铝开工率_ALD"    
    wind_code = "S5809467"


###########################################################################################################################
""" 电解铝进出口 """   
    
class DianJieLvJinKouZiGeGuoShuJu(sdb_base, Manual):
    field_name = u"电解铝进出口"
    col_name = u"电解铝进口自各国数据"    
    
class DianJieLvChuKouZhiGeGuoShuJu(sdb_base, Manual):
    field_name = u"电解铝进出口"
    col_name = u"电解铝出口至各国数据"    
    
class YuanLvJingJinKouLiang_DangYueZhi(sdb_base, WindData):
    field_name = u"电解铝进出口"
    col_name = u"原铝净进口量_当月值"    
    wind_code = "S5808246"
    
class YuanLvJinKouShuLiang_LeiJiZhi(sdb_base, WindData):
    field_name = u"电解铝进出口"
    col_name = u"原铝进口数量_累计值"    
    wind_code = "S0116251"
    
class YuanLvJinKouShuLiang_DangYueZhi(sdb_base, WindData):
    field_name = u"电解铝进出口"
    col_name = u"原铝进口数量_当月值"    
    wind_code = "S0116250"
    
class YuanLvChuKouShuLiang_LeiJiZhi(sdb_base, WindData):
    field_name = u"电解铝进出口"
    col_name = u"原铝出口数量_累计值"    
    wind_code = "S0116281"

class YuanLvChuKouShuLiang_DangYueZhi(sdb_base, WindData):
    field_name = u"电解铝进出口"
    col_name = u"原铝出口数量_当月值"    
    wind_code = "S0116280"
    
###########################################################################################################################
""" 电解铝市场整理 """  
    
class ZhongGuoDianJieLvXinZengChanNengLieBiao_2018To2020Nian(sdb_base, Manual):
    field_name = u"电解铝市场整理"
    col_name = u"中国电解铝新增产能列表_2018-2020年"    

class ZhongGuoDianJieLvQiYeGongGeiCeGaiGeZhiHuanChanNengLieBiao_2017To2018Nian(sdb_base, Manual):
    field_name = u"电解铝市场整理"
    col_name = u"中国电解铝企业供给侧改革置换产能列表_2017-2018年" 
    
###########################################################################################################################
""" 电解铝需求 """  
    
class YuanLv_DianJieLv_XiaoLiang(sdb_base, WindData):
    field_name = u"电解铝需求"
    col_name = u"原铝(电解铝)_销量"    
    wind_code = "S0152400"    

class YuanLvBiaoGuanXiaoFeiLiang_DangYueZhi(sdb_base, Computed):
    field_name = u"电解铝需求"
    col_name = u"原铝表观消费量_当月值"    
    def get_ts_whole_progress(self):
        relevant_col_list = [u"原铝产量_中国_当月值", u"原铝净进口量_当月值"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"原铝产量_中国_当月值"] + tmp_total[u"原铝净进口量_当月值"]
        return tmp_total  

###########################################################################################################################
""" 电解铝供需平衡 """  

class LvGongXuPingHeng_WBMS_LeiJiZhi(sdb_base, WindData):
    field_name = u"电解铝供需平衡"
    col_name = u"铝供需平衡_WBMS_累计值"    
    wind_code = "S5808558"   
    start_year = 2014
    axhline = 0   
    def seasonal_plot(self):
        tmp_df_interpolated, fig, axis = super(sdb_base, self).seasonal_plot(start_year=self.start_year, 
                                              axhline=self.axhline, mode="month", plot_type="bar")
        axis.set_xticklabels(["", "1-2月", "1-3月", "1-4月", "1-5月", "1-6月", "1-7月", "1-8月", "1-9月", 
                              "1-10月", "1-11月", "1-12月"], fontsize=27, ha="center")
        return tmp_df_interpolated, fig, axis


if __name__ == "__main__":
    g = LvGongXuPingHeng_WBMS_LeiJiZhi().get_ts()
#    a = LvGongXuPingHeng_WBMS_LeiJiZhi().seasonal_plot()
    
    
    
    
    
    
    
    
    
    