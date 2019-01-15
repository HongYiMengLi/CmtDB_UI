# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 10:47:39 2018

@author: 李弘一萌
"""

import pandas as pd
from datetime import datetime
from .I_Base import I_Base
from ...Base.DataType_Base import Manual, Computed, WindData
from ...Base.Plot_Base import Plot_Base
from matplotlib.ticker import FuncFormatter


class macro_base(I_Base, Plot_Base):
    table_english_name = "Macro"
    table_chinese_name = u"宏观"

        

##########################################################################################################################
""" 海运价格 """     
     
class ZhongJianJia_MeiYuanDuiRenMinBi(macro_base, WindData):
    field_name = u"海运价格"
    col_name = u"海运指数_波罗的海干散货指数(BDI)"
    wind_code = "S0031550"
    

class HaiYunZhiShu_HaoWangJiaoXingYunFeiZhiShu(macro_base, WindData):
    field_name = u"海运价格"
    col_name = u"海运指数_好望角型运费指数(BCI)"
    wind_code = "S0031552"

    
    


    
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