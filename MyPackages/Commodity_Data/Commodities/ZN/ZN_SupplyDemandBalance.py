# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 10:48:40 2018

@author: 李弘一萌
"""

import pandas as pd
from datetime import datetime
from .ZN_Base import ZN_Base
from ...Base.DataType_Base import Manual, Computed, WindData
from ...Base.Plot_Base import Plot_Base
from matplotlib.ticker import FuncFormatter

class sdb_base(ZN_Base, Plot_Base):
    table_english_name = "SupplyDemandBalance"
    table_chinese_name = u"供需平衡表"
    
    def output(self):
        print(self.table_english_name)
    
    def get_relevant_df(self, col_list):
        local_col_name_list = sdb_base.get_all_table_classname()
        col_cls_list = []
        for x in col_list:
            col_cls_name = str(ZN_Base.get_class_name(x))
            if col_cls_name not in local_col_name_list:
                col_cls_list.append(eval(ZN_Base.get_table_class_full_variable(x)))
            else:
                col_cls_list.append(eval(col_cls_name))
        ts_list = [x().get_ts() for x in col_cls_list]
        tmp_table_df = pd.concat(ts_list, axis=1).dropna(how="all")
        return tmp_table_df 


###########################################################################################################################
""" 产量 """   

class QuanQiuXinKuangChanLiang_ILZSG_DangYueZhi(sdb_base, WindData):
    field_name = u"产量"
    col_name = u"全球锌矿产量_ILZSG_当月值"    
    wind_code = "S5806607"

class QuanQiuJingLianXinChanLiang_ILZSG_DangYueZhi(sdb_base, WindData):
    field_name = u"产量"
    col_name = u"全球精炼锌产量_ILZSG_当月值"    
    wind_code = "S5806608"
    
class JingLianXinChanLiang_ILZSG_ZhongGuo_DangYueZhi(sdb_base, WindData):
    field_name = u"产量"
    col_name = u"精炼锌产量_ILZSG_中国_当月值"    
    wind_code = "S5808351"
    
class XinChanLiang_DangYueZhi(sdb_base, WindData):
    field_name = u"产量"
    col_name = u"锌产量_当月值"    
    wind_code = "S0027583"
   
class XinChanLiang_DangYueTongBi(sdb_base, WindData):
    field_name = u"产量"
    col_name = u"锌产量_当月同比"    
    wind_code = "S0027584"
    
class XinChanLiang_LeiJiTongBi(sdb_base, WindData):
    field_name = u"产量"
    col_name = u"锌产量_累计同比"    
    wind_code = "S0027586"
    


###########################################################################################################################
""" 进口量 """   
    
class JingLianXinJinKouShuLiang_AoDaLiYa_LeiJiZhi(sdb_base, WindData):
    field_name = u"进口量"
    col_name = u"精炼锌进口数量_澳大利亚_累计值"    
    wind_code = "S0116581"
    
class JingLianXinJinKouShuLiang_HaSaKeSiTan_LeiJiZhi(sdb_base, WindData):
    field_name = u"进口量"
    col_name = u"精炼锌进口数量_哈萨克斯坦_累计值"    
    wind_code = "S0116583"
    
class JingLianXinJinKouShuLiang_YinDu_LeiJiZhi(sdb_base, WindData):
    field_name = u"进口量"
    col_name = u"精炼锌进口数量_印度_累计值"    
    wind_code = "S0116585"
    
class JingLianXinJinKouShuLiang_HanGuo_LeiJiZhi(sdb_base, WindData):
    field_name = u"进口量"
    col_name = u"精炼锌进口数量_韩国_累计值"    
    wind_code = "S0116586"
    
class JingLianXinJinKouShuLiang_XiBanYa_LeiJiZhi(sdb_base, WindData):
    field_name = u"进口量"
    col_name = u"精炼锌进口数量_西班牙_累计值"    
    wind_code = "S0255680"
    


###########################################################################################################################
""" 消耗量 """  
    
class QuanQiuJingLianXinXiaoHaoLiang_ILZSG_DangYueZhi(sdb_base, WindData):
    field_name = u"消耗量"
    col_name = u"全球精炼锌消耗量_ILZSG_当月值"    
    wind_code = "S5806609"
    
class JingLianXinXiaoFeiLiang_ILZSG_ZhongGuo_DangYueZhi(sdb_base, WindData):
    field_name = u"消耗量"
    col_name = u"精炼锌消费量_ILZSG_中国_当月值"    
    wind_code = "S5808373"
    
###########################################################################################################################
""" 供需缺口 """  
    
class QuanQiuJingLianXinGuoShengOrQueKou_ILZSG_DangYueZhi(sdb_base, WindData):
    field_name = u"供需缺口"
    col_name = u"全球精炼锌过剩/缺口_ILZSG_当月值"    
    wind_code = "S5806610"    


class XinGongXuPingHeng_WBMS_LeiJiZhi(sdb_base, WindData):
    field_name = u"供需缺口"
    col_name = u"锌供需平衡_WBMS_累计值"    
    wind_code = "S5808556" 
    start_year = 2014
    axhline = 0   
    def seasonal_plot(self):
        tmp_df_interpolated, fig, axis = super(sdb_base, self).seasonal_plot(start_year=self.start_year, 
                                              axhline=self.axhline, mode="month", plot_type="bar")
        axis.set_xticklabels(["", "1-2月", "1-3月", "1-4月", "1-5月", "1-6月", "1-7月", "1-8月", "1-9月", 
                              "1-10月", "1-11月", "1-12月"], fontsize=27, ha="center")
        return tmp_df_interpolated, fig, axis



if __name__ == "__main__":
    a = PZNSheHuiKuCun().seasonal_plot()
    
    
    
    
    
    
    
    
    
    