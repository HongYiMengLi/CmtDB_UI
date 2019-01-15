# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 10:44:58 2018

@author: 李弘一萌
"""

import pandas as pd
from datetime import datetime
from .HC_Base import HC_Base
from . import HC_Macro, HC_FuturesPrice, HC_SpotPrice
from ..J import J_FuturesPrice
from ..I import I_FuturesPrice
from ..RB import RB_SpotPrice
from ...Base.DataType_Base import Manual, Computed, WindData
from ...Base.Plot_Base import Plot_Base
from matplotlib.ticker import FuncFormatter

class upstream_base(HC_Base, Plot_Base):
    table_english_name = "Upstream"
    table_chinese_name = u"上游"
#    original_db_filepath = data_path + u"LPP价格数据库.xlsx"
    
    def output(self):
        print("Upstream")
    
    def get_relevant_df(self, col_list):
        local_col_name_list = upstream_base.get_all_table_classname()
        col_cls_list = []
        for x in col_list:
            col_cls_name = str(HC_Base.get_class_name(x))
            if col_cls_name not in local_col_name_list:
                col_cls_list.append(eval(HC_Base.get_table_class_full_variable(x)))
            else:
                col_cls_list.append(eval(col_cls_name))
        ts_list = [x().get_ts() for x in col_cls_list]
        tmp_table_df = pd.concat(ts_list, axis=1).dropna(how="all")
        return tmp_table_df
    
###########################################################################################################################
""" 虚拟利润 """
  
class ReZhaJuanBanXuNiLiRun_01HeYue(upstream_base, Computed):
    field_name = u"虚拟利润"
    col_name = u"热轧卷板虚拟利润_01合约"
    axhline = 0
    def get_ts_whole_progress(self):
        relevant_col_list = [u"HC01合约收盘价"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        I_tmp_series = I_FuturesPrice.TieKuang01HeYueShouPanJia().get_ts()
        J_tmp_series = J_FuturesPrice.J01HeYueShouPanJia().get_ts()
        RB_tmp_series = RB_SpotPrice.FeiGangShiChangJia_6To8mm_TangShan().get_ts()
        tmp_total = pd.concat([RB_tmp_series, tmp_total, I_tmp_series, J_tmp_series], axis=1, sort=False)
        tmp_total[self.col_name] = tmp_total[u"HC01合约收盘价"] - (((1.64 * tmp_total[u"I01合约收盘价"] + 0.45 * tmp_total[u"J01合约收盘价"] \
                                   + 380) * 1.01 + 0.12 * 1.16 * tmp_total[u"废钢市场价(含税)_6-8mm_唐山"] ) / 1.12 + 300) * 1.03 - 300
        return tmp_total

class ReZhaJuanBanXuNiLiRun_05HeYue(upstream_base, Computed):
    field_name = u"虚拟利润"
    col_name = u"热轧卷板虚拟利润_05合约"
    axhline = 0
    def get_ts_whole_progress(self):
        relevant_col_list = [u"HC05合约收盘价"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        I_tmp_series = I_FuturesPrice.TieKuang05HeYueShouPanJia().get_ts()
        J_tmp_series = J_FuturesPrice.J05HeYueShouPanJia().get_ts()
        RB_tmp_series = RB_SpotPrice.FeiGangShiChangJia_6To8mm_TangShan().get_ts()
        tmp_total = pd.concat([RB_tmp_series, tmp_total, I_tmp_series, J_tmp_series], axis=1, sort=False)
        tmp_total[self.col_name] = tmp_total[u"HC05合约收盘价"] - (((1.64 * tmp_total[u"I05合约收盘价"] + 0.45 * tmp_total[u"J05合约收盘价"] \
                                   + 380) * 1.01 + 0.12 * 1.16 * tmp_total[u"废钢市场价(含税)_6-8mm_唐山"] ) / 1.12 + 300) * 1.03 - 300
        return tmp_total

class ReZhaJuanBanXuNiLiRun_10HeYue(upstream_base, Computed):
    field_name = u"虚拟利润"
    col_name = u"热轧卷板虚拟利润_10合约"
    axhline = 0
    def get_ts_whole_progress(self):
        relevant_col_list = [u"HC10合约收盘价"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        I_tmp_series = I_FuturesPrice.TieKuang09HeYueShouPanJia().get_ts()
        J_tmp_series = J_FuturesPrice.J09HeYueShouPanJia().get_ts()
        RB_tmp_series = RB_SpotPrice.FeiGangShiChangJia_6To8mm_TangShan().get_ts()
        tmp_total = pd.concat([RB_tmp_series, tmp_total, I_tmp_series, J_tmp_series], axis=1, sort=False)
        tmp_total[self.col_name] = tmp_total[u"HC10合约收盘价"] - (((1.64 * tmp_total[u"I09合约收盘价"] + 0.45 * tmp_total[u"J09合约收盘价"] \
                                   + 380) * 1.01 + 0.12 * 1.16 * tmp_total[u"废钢市场价(含税)_6-8mm_唐山"] ) / 1.12 + 300) * 1.03 - 300
        return tmp_total
    
    
if __name__ == "__main__":
    df = PHCXianHuoJiaGongFei().seasonal_plot()    
    
    
    
    
    
    
    
    
    
    
    
    
    
    