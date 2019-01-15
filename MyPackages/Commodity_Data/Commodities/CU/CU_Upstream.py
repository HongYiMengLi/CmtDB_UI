# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 10:44:58 2018

@author: 李弘一萌
"""

import pandas as pd
from datetime import datetime
from .CU_Base import CU_Base
from ...Base.DataType_Base import Manual, Computed, WindData
from ...Base.Plot_Base import Plot_Base
from matplotlib.ticker import FuncFormatter

class upstream_base(CU_Base, Plot_Base):
    table_english_name = "Upstream"
    table_chinese_name = u"上游"
#    original_db_filepath = data_path + u"LPP价格数据库.xlsx"
    
    def output(self):
        print("Upstream")
    
    def get_relevant_df(self, col_list):
        local_col_name_list = upstream_base.get_all_table_classname()
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
""" 废铜价格 """  
     
    
class FeiTongJiaGe_No1GuangLiangTongXian_FoShan(upstream_base, WindData):
    field_name = u"废铜价格"
    col_name = u"废铜价格_1#光亮铜线_佛山"
    wind_code = "S5806328"
    
class FeiTongJiaGe_No1GuangLiangTongXian_ShangHai(upstream_base, WindData):
    field_name = u"废铜价格"
    col_name = u"废铜价格_1#光亮铜线_上海"
    wind_code = "S5806296"
    
class FeiTongJiaGe_No1Tong_Cu97Prct_TianJin(upstream_base, WindData):
    field_name = u"废铜价格"
    col_name = u"废铜价格_1#铜(Cu97%)_天津"
    wind_code = "S5806311"
    
class FeiTongJiaGe_No1Tong_Cu97Prct_JiangZheHu(upstream_base, WindData):
    field_name = u"废铜价格"
    col_name = u"废铜价格_1#铜(Cu97%)_江浙沪"
    wind_code = "S5806416"
    

    
    
    
    
    
    
###########################################################################################################################
""" 废铜进口量 """  

class FeiTongZhongGuoJinKouShuLiang_DangYueZhi(upstream_base, WindData):
    field_name = u"废铜进口量"
    col_name = u"废铜中国进口数量_当月值"
    wind_code = "S0027639"

  
###########################################################################################################################
""" 铜矿产量 """   

class TongXuanKuangChanPinHanTongLiang_DangYueZhi(upstream_base, WindData):
    field_name = u"铜矿产量"
    col_name = u"铜选矿产品含铜量_当月值"
    wind_code = "S0027615"

    
class TongXuanKuangChanPinHanTongLiang_LeiJiZhi(upstream_base, WindData):
    field_name = u"铜矿产量"
    col_name = u"铜选矿产品含铜量_累计值"
    wind_code = "S0027617"

    

###########################################################################################################################
""" 铜矿加工费 """   

class ZhongGuoTongYeLianChangCuLianFei_TC(upstream_base, WindData):
    field_name = u"铜矿加工费"
    col_name = u"中国铜冶炼厂粗炼费(TC)"
    wind_code = "S5800705"
    start_year = 2014

class ZhongGuoTongYeLianChangJingLianFei_RC(upstream_base, WindData):
    field_name = u"铜矿加工费"
    col_name = u"中国铜冶炼厂精炼费(RC)"
    wind_code = "S5800706"


###########################################################################################################################
""" 铜矿价格 """   

class TongJingKuangPingJunJia_BuHanShui_20Prct_JiangXi(upstream_base, WindData):
    field_name = u"铜矿价格"
    col_name = u"铜精矿平均价(不含税)_20%_江西"
    wind_code = "S5810930"

class TongJingKuangPingJunJia_BuHanShui_20Prct_HuBei(upstream_base, WindData):
    field_name = u"铜矿价格"
    col_name = u"铜精矿平均价(不含税)_20%_湖北"
    wind_code = "S5810931"

class TongJingKuangPingJunJia_BuHanShui_20Prct_NeiMengGu(upstream_base, WindData):
    field_name = u"铜矿价格"
    col_name = u"铜精矿平均价(不含税)_20%_内蒙古"
    wind_code = "S5810932"

class TongJingKuangPingJunJia_BuHanShui_20Prct_YunNan(upstream_base, WindData):
    field_name = u"铜矿价格"
    col_name = u"铜精矿平均价(不含税)_20%_云南"
    wind_code = "S5810933"

###########################################################################################################################
""" 铜矿进口量 """   

class TongKuangShiJiJingKuangZhongGuoJinKouShuLiang_DangYueZhi(upstream_base, WindData):
    field_name = u"铜矿进口量"
    col_name = u"铜矿石及精矿中国进口数量_当月值"
    wind_code = "S0071263"



    
if __name__ == "__main__":
    df = PCUXianHuoJiaGongFei().seasonal_plot()    
    
    
    
    
    
    
    
    
    
    
    
    
    
    