# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 10:44:58 2018

@author: 李弘一萌
"""

import pandas as pd
from datetime import datetime
from .ZN_Base import ZN_Base
from . import ZN_SpotPrice, ZN_FuturesPrice
from ...Base.DataType_Base import Manual, Computed, WindData
from ...Base.Plot_Base import Plot_Base
from matplotlib.ticker import FuncFormatter

class upstream_base(ZN_Base, Plot_Base):
    table_english_name = "Upstream"
    table_chinese_name = u"上游"
    
    
    def output(self):
        print("Upstream")
    
    def get_relevant_df(self, col_list):
        local_col_name_list = upstream_base.get_all_table_classname()
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
""" 锌矿价格 """  
    
class XinJingKuangPingJunJia_HanShui_55Prct_KunMing(upstream_base, WindData):
    field_name = u"锌矿价格"
    col_name = u"锌精矿平均价(含税)_55%_昆明"
    wind_code = "S5800727"
    
class XinJingKuangPingJunJia_HanShui_45Prct_KunMing(upstream_base, WindData):
    field_name = u"锌矿价格"
    col_name = u"锌精矿平均价(含税)_45%_昆明"
    wind_code = "S5800726"
    
class XinJingKuangDaoChangJia_HanShui_50Prct_XiAn(upstream_base, WindData):
    field_name = u"锌矿价格"
    col_name = u"锌精矿到厂价(含税)_50%_西安"
    wind_code = "S5800722"
    
class XinJingKuangDaoChangJia_HanShui_50Prct_ChenZhou(upstream_base, WindData):
    field_name = u"锌矿价格"
    col_name = u"锌精矿到厂价(含税)_50%_郴州"
    wind_code = "S5800731"
    
class XinJingKuangDaoChangJia_HanShui_50Prct_DanDong(upstream_base, WindData):
    field_name = u"锌矿价格"
    col_name = u"锌精矿到厂价(含税)_50%_丹东"
    wind_code = "S5800730"
    
class XinJingKuangDaoChangJia_HanShui_50Prct_HeChi(upstream_base, WindData):
    field_name = u"锌矿价格"
    col_name = u"锌精矿到厂价(含税)_50%_河池"
    wind_code = "S5800729"
    
class XinJingKuangDaoChangJia_HanShui_50Prct_JiShou(upstream_base, WindData):
    field_name = u"锌矿价格"
    col_name = u"锌精矿到厂价(含税)_50%_吉首"
    wind_code = "S5800728"
    
class XinJingKuangDaoChangJia_HanShui_50Prct_LanZhou(upstream_base, WindData):
    field_name = u"锌矿价格"
    col_name = u"锌精矿到厂价(含税)_50%_兰州"
    wind_code = "S5800725"

    
    
    
    
    
    
    
###########################################################################################################################
""" 锌矿进口量 """  

class XinKuangShaJiJingKuangJinKouShuLiang_DangYueZhi(upstream_base, WindData):
    field_name = u"锌矿进口量"
    col_name = u"锌矿砂及精矿进口数量_当月值"
    wind_code = "S0116272"


class XinKuangShaJiJingKuangJinKouShuLiang_LeiJiZhi(upstream_base, WindData):
    field_name = u"锌矿进口量"
    col_name = u"锌矿砂及精矿进口数量_累计值"
    wind_code = "S0116273"
    

###########################################################################################################################
""" 锌矿产量 """   

class XinXuanKuangChanPinHanXinLiang_DangYueZhi(upstream_base, WindData):
    field_name = u"锌矿产量"
    col_name = u"锌选矿产品含锌量_当月值"
    wind_code = "S0027623"

    
class XinXuanKuangChanPinHanXinLiang_LeiJiZhi(upstream_base, WindData):
    field_name = u"锌矿产量"
    col_name = u"锌选矿产品含锌量_累计值"
    wind_code = "S0027625"

    
class XinXuanKuangChanPinHanXinLiang_LeiJiTongBi(upstream_base, WindData):
    field_name = u"锌矿产量"
    col_name = u"锌选矿产品含锌量_累计同比"
    wind_code = "S0027626"
 

###########################################################################################################################
""" 锌矿加工费 """   

class XinJingKuangZuiDiJiaGongFei_50Prct_BeiFang(upstream_base, WindData):
    field_name = u"锌矿加工费"
    col_name = u"锌精矿最低加工费_50%_北方"
    wind_code = "S5811042"

class XinJingKuangZuiDiJiaGongFei_50Prct_NanFang(upstream_base, WindData):
    field_name = u"锌矿加工费"
    col_name = u"锌精矿最低加工费_50%_南方"
    wind_code = "S5811043"

class XinJingKuangZuiGaoJiaGongFei_50Prct_BeiFang(upstream_base, WindData):
    field_name = u"锌矿加工费"
    col_name = u"锌精矿最高加工费_50%_北方"
    wind_code = "S5811044"

class XinJingKuangZuiGaoJiaGongFei_50Prct_NanFang(upstream_base, WindData):
    field_name = u"锌矿加工费"
    col_name = u"锌精矿最高加工费_50%_南方"
    wind_code = "S5811045"

class XinJingKuangZuiDiJiaGongFei_50Prct_JinKouTC(upstream_base, WindData):
    field_name = u"锌矿加工费"
    col_name = u"锌精矿最低加工费_50%_进口TC"
    wind_code = "S5811046"

class XinJingKuangZuiGaoJiaGongFei_50Prct_JinKouTC(upstream_base, WindData):
    field_name = u"锌矿加工费"
    col_name = u"锌精矿最高加工费_50%_进口TC"
    wind_code = "S5811047"

class GuoChanXinKuangJiaGongFei(upstream_base, Computed):
    field_name = u"锌矿加工费"
    col_name = u"国产锌矿加工费"    
    def get_ts_whole_progress(self):
        relevant_col_list = [u"锌精矿最低加工费_50%_北方", "锌精矿最低加工费_50%_南方", u"锌精矿最高加工费_50%_北方", "锌精矿最高加工费_50%_南方"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total.mean(axis=1, skipna=True)
        return tmp_total   

class XinLianChangShiJiJiaGongFei(upstream_base, Computed):
    field_name = u"锌矿加工费"
    col_name = u"锌炼厂实际加工费"    
    def get_ts_whole_progress(self):
        relevant_col_list = [u"国产锌矿加工费", "锌期货收盘价(活跃合约)"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total["signal"] = tmp_total["锌期货收盘价(活跃合约)"].apply(lambda x: 0 if x <=15000 else x - 15000)
        tmp_total[self.col_name] = tmp_total["signal"] * 0.2 + tmp_total["国产锌矿加工费"]
        return tmp_total   






    
if __name__ == "__main__":
    df = GuoChanXinKuangJiaGongFei().get_ts()    
    
    
    
    
    
    
    
    
    
    
    
    
    
    