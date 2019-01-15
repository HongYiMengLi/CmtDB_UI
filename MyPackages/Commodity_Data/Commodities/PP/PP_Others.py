# -*- coding: utf-8 -*-
"""
Created on Mon Aug 27 16:01:29 2018

@author: 李弘一萌
"""

import pandas as pd
from datetime import datetime
from .PP_Base import PP_Base
from ...Base.DataType_Base import Auto
from ...Base.Plot_Base import Plot_Base
from matplotlib.ticker import FuncFormatter
from . import PP_Macro

class others_base(PP_Base, Plot_Base):
    table_english_name = "Others"
    table_chinese_name = u"其他"
#    original_db_filepath = data_path + u"LPP价格数据库.xlsx"

        

###########################################################################################################################
""" 外汇 """     
     
class HuiMaiJia(others_base, Auto):
    field_name = u"增值税"
    col_name = u"增值税"
    def get_ts(self):
        tmp_table_df = PP_Macro.HuiMaiJia().get_ts()
        tmp_series = pd.Series([0.17]*len(tmp_table_df.index), index=tmp_table_df.index, name=u"增值税") 
        tmp_series.loc[tmp_series.index >= datetime(2018,5,1)] = 0.16    
        return tmp_series



    
    


    
if __name__ == "__main__":
#    aaa = vars()["field"]
#    print a.__name__
#    aaa = KengKouMei_DongSheng()
#    df = aaa.generate_wind_quote()
    
#    ts = ZengZhiShui().get_ts()
    
#    fig_tuple = PPYouZhiLiRun().seasonal_plot()
#    LPP_Plot.add_month_span(fig_tuple[2], fig_tuple[0], 5)
    
#    a = spot_price_base.get_all_manual_class()
#    b = [x.col_name for x in a.values()]
#    c = [x.field_name for x in a.values()]
#    d = pd.DataFrame([b, c], index=["col", "field"]).T
#    f = d.sort_values(by=["field", "col"])
#    e = pd.DataFrame([], columns=f["col"].values.tolist())
#    e.to_excel(data_path + "update.xlsx", encoding="gbk")
    pass