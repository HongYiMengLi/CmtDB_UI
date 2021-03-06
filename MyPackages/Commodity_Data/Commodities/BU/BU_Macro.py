# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 10:47:39 2018

@author: 李弘一萌
"""

import pandas as pd
from datetime import datetime
from .BU_Base import BU_Base
from ...Base.DataType_Base import WindData
from ...Base.Plot_Base import Plot_Base


class macro_base(BU_Base, Plot_Base):
    table_english_name = "Macro"
    table_chinese_name = u"宏观"

        

###########################################################################################################################
""" 外汇 """     
     
class HuiMaiJia_MeiYuanDongRenMinBi(macro_base, WindData):
    field_name = u"外汇"
    col_name = u"汇卖价_美元兑人民币"
    wind_code = "M0066316"
    



    
    


    
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