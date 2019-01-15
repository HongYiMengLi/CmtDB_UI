# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 16:35:12 2018

@author: 李弘一萌
"""

import pandas as pd
from datetime import datetime
from MyFutureClass.CmtDataBase.Commodities.B.B_Base import B_Base
from MyFutureClass.CmtDataBase.Base.DataType_Base import Manual, Computed, WindData
from MyFutureClass.CmtDataBase.Base.Plot_Base import Plot_Base
from MyFutureClass.Data.QuoteData import QuoteData
from matplotlib.ticker import FuncFormatter

class spot_price_base(B_Base, Plot_Base):
    table_english_name = "SpotPrice"
    table_chinese_name = u"现货价格"
#    original_db_filepath = data_path + u"LPP价格数据库.xlsx"
    
    def output(self):
        print("SpotPrice")
    
    def get_relevant_df(self, col_list):
        local_col_name_list = spot_price_base.get_all_table_classname()
        col_cls_list = []
        for x in col_list:
            col_cls_name = str(B_Base.get_class_name(x))
            if col_cls_name not in local_col_name_list:
                col_cls_list.append(eval(B_Base.get_table_class_full_variable(x)))
            else:
                col_cls_list.append(eval(col_cls_name))
        ts_list = [x().get_ts() for x in col_cls_list]
        tmp_table_df = pd.concat(ts_list, axis=1).dropna(how="all")
        return tmp_table_df  

    
###########################################################################################################################
""" 到厂成本 """    

class JinKouDaDouDaoChangChengBen(spot_price_base, Computed):
    field_name = u"到厂成本"
    col_name = u"进口大豆到厂成本"
    def get_ts_whole_progress(self):
#        relevant_col_list = [u"中国棉花328价格指数", "CF01合约收盘价"]
#        tmp_total = self.get_relevant_df(relevant_col_list)
#        tmp_total[self.col_name] = tmp_total[u"中国棉花328价格指数"] - tmp_total[u"CF01合约收盘价"]
#        return tmp_total
        pass


if __name__ == "__main__":
    ts = YeHuaQiChuChangJia_JingBoShiHua().get_ts()