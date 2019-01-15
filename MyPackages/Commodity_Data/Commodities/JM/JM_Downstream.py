# -*- coding: utf-8 -*-
"""
Created on Mon Aug 27 08:34:56 2018

@author: 李弘一萌
"""

import pandas as pd
from datetime import datetime
from .JM_Base import JM_Base
from ..J import J_SupplyDemandBalance
from ...Base.DataType_Base import Manual, Computed, WindData
from ...Base.Plot_Base import Plot_Base
from matplotlib.ticker import FuncFormatter

class downstream_base(JM_Base, Plot_Base):
    table_english_name = "Downstream"
    table_chinese_name = u"下游"
#    original_db_filepath = data_path + u"JMPP价格数据库.xlsx"
    
    def output(self):
        print("Downstream")
    
    def get_relevant_df(self, col_list):
        local_col_name_list = downstream_base.get_all_table_classname()
        col_cls_list = []
        for x in col_list:
            col_cls_name = str(JM_Base.get_class_name(x))
            if col_cls_name not in local_col_name_list:
                col_cls_list.append(eval(JM_Base.get_table_class_full_variable(x)))
            else:
                col_cls_list.append(eval(col_cls_name))
        ts_list = [x().get_ts() for x in col_cls_list]
        tmp_table_df = pd.concat(ts_list, axis=1).dropna(how="all")
        return tmp_table_df  
    
    
    
###########################################################################################################################
""" 焦化利润 """  

class LianJiaoLiRun_ShanXi(downstream_base, Computed):
    field_name = u"焦化利润"
    col_name = u"炼焦利润_山西"
    def get_ts_whole_progress(self):
        tmp_series = J_SupplyDemandBalance.LianJiaoLiRun_ShanXi().get_ts(),
        return tmp_series.to_frame()

    
    
if __name__ == "__main__":

    
    ts1, fig1, axis1 = DaXingDiMoChangKaiGongJMv().seasonal_plot()
    ts2, fig2, axis2 = ShuangFangMoJMiRun().seasonal_plot()         
    