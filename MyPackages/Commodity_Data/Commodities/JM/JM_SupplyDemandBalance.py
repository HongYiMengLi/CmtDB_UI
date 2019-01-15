# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 10:48:40 2018

@author: 李弘一萌
"""

import pandas as pd
from datetime import datetime
from .JM_Base import JM_Base
from ...Base.DataType_Base import Manual, Computed, WindData
from ...Base.Plot_Base import Plot_Base
from matplotlib.ticker import FuncFormatter

class sdb_base(JM_Base, Plot_Base):
    table_english_name = "SupplyDemandBalance"
    table_chinese_name = u"供需平衡表"
    
    def output(self):
        print(self.table_english_name)
    
    def get_relevant_df(self, col_list):
        local_col_name_list = sdb_base.get_all_table_classname()
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
""" 产量 """  

class YuanMeiChanLiang_DangYueZhi(sdb_base, WindData):
    field_name = u"产量"
    col_name = u"原煤产量_当月值"    
    wind_code = "S0026989"
    
class LianJiaoMeiChanLiang_DangYueZhi(sdb_base, WindData):
    field_name = u"产量"
    col_name = u"炼焦煤(炼焦精煤)产量_当月值"    
    wind_code = "S5118233"




###########################################################################################################################
""" 出口 """  

class LianJiaoMeiChuKouShuLiang_DangYueZhi(sdb_base, WindData):
    field_name = u"出口"
    col_name = u"炼焦煤出口数量_当月值"    
    wind_code = "S5118232"   

###########################################################################################################################
""" 进口 """  

class LianJiaoMeiJinKouShuLiang_DangYueZhi(sdb_base, WindData):
    field_name = u"进口"
    col_name = u"炼焦煤进口数量_当月值"    
    wind_code = "S5118231"   
    
class LianJiaoMeiJinKouShuLiang_AoDaLiYa_DangYueZhi(sdb_base, WindData):
    field_name = u"进口"
    col_name = u"炼焦煤进口数量_澳大利亚_当月值"    
    wind_code = "S5103140"   
    
class LianJiaoMeiJinKouShuLiang_JiaMaDa_DangYueZhi(sdb_base, WindData):
    field_name = u"进口"
    col_name = u"炼焦煤进口数量_加拿大_当月值"    
    wind_code = "S5103141"   

class LianJiaoMeiJinKouShuLiang_MengGu_DangYueZhi(sdb_base, WindData):
    field_name = u"进口"
    col_name = u"炼焦煤进口数量_蒙古_当月值"    
    wind_code = "S5103142"   

class LianJiaoMeiJinKouShuLiang_ELuoSiLianBang_DangYueZhi(sdb_base, WindData):
    field_name = u"进口"
    col_name = u"炼焦煤进口数量_俄罗斯联邦_当月值"    
    wind_code = "S5103143"   
    
class LianJiaoMeiJinKouShuLiang_MeiGuo_DangYueZhi(sdb_base, WindData):
    field_name = u"进口"
    col_name = u"炼焦煤进口数量_美国_当月值"    
    wind_code = "S5103144"   


###########################################################################################################################
""" 销量 """  

class GongYeJinXingYeMeiTanXiaoLiang(sdb_base, Manual):
    field_name = u"销量"
    col_name = u"供冶金行业煤炭销量"    
    
if __name__ == "__main__":
    a = PJSheHuiKuCun().seasonal_plot()
    
    
    
    
    
    
    
    
    
    