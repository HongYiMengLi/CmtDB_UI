# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 10:48:40 2018

@author: 李弘一萌
"""

import pandas as pd
from datetime import datetime
from MyFutureClass.CmtDataBase.Commodities.B.B_Base import B_Base
from MyFutureClass.CmtDataBase.Base.DataType_Base import Manual, Computed, WindData
from MyFutureClass.CmtDataBase.Base.Plot_Base import Plot_Base
from matplotlib.ticker import FuncFormatter

class sdb_base(B_Base, Plot_Base):
    table_english_name = "SupplyDemandBalance"
    table_chinese_name = u"供需平衡表"
    
    def output(self):
        print(self.table_english_name)
    
    def get_relevant_df(self, col_list):
        local_col_name_list = sdb_base.get_all_table_classname()
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


class DaDouChanLiang_MeiGuo_USDA(sdb_base, Manual):
    field_name = u"产量"
    col_name = u"大豆产量_美国_USDA"

class DaDouChanLiang_BaXi_USDA(sdb_base, Manual):
    field_name = u"产量"
    col_name = u"大豆产量_巴西_USDA"
    
class DaDouChanLiang_AGenTing_USDA(sdb_base, Manual):
    field_name = u"产量"
    col_name = u"大豆产量_阿根廷_USDA"

class DaDouChanLiang_ZhongGuo_USDA(sdb_base, Manual):
    field_name = u"产量"
    col_name = u"大豆产量_中国_USDA"

class DaDouChanLiang_QuanQiu_USDA(sdb_base, Manual):
    field_name = u"产量"
    col_name = u"大豆产量_全球_USDA"
    
class DaDouChanLiang_MeiGuo_YuCe_WIND(sdb_base, WindData):
    field_name = u"产量"
    col_name = u"大豆产量_美国_预测_WIND"
    wind_code = "S0113227"

class DaDouChanLiang_BaXi_YuCe_WIND(sdb_base, WindData):
    field_name = u"产量"
    col_name = u"大豆产量_巴西_预测_WIND"
    wind_code = "S0113241"

class DaDouChanLiang_AGenTing_YuCe_WIND(sdb_base, WindData):
    field_name = u"产量"
    col_name = u"大豆产量_阿根廷_预测_WIND"
    wind_code = "S0113248"

class DaDouChanLiang_ZhongGuo_YuCe_WIND(sdb_base, WindData):
    field_name = u"产量"
    col_name = u"大豆产量_中国_预测_WIND"
    wind_code = "S0113234"

class DaDouChanLiang_QuanQiu_YuCe_WIND(sdb_base, WindData):
    field_name = u"产量"
    col_name = u"大豆产量_全球_预测_WIND"
    wind_code = "S0112358"

class DaDouChanLiang_MeiGuo_GuJi_WIND(sdb_base, WindData):
    field_name = u"产量"
    col_name = u"大豆产量_美国_估计_WIND"
    wind_code = "S0112897"

class DaDouChanLiang_BaXi_GuJi_WIND(sdb_base, WindData):
    field_name = u"产量"
    col_name = u"大豆产量_巴西_估计_WIND"
    wind_code = "S0112911"

class DaDouChanLiang_AGenTing_GuJi_WIND(sdb_base, WindData):
    field_name = u"产量"
    col_name = u"大豆产量_阿根廷_估计_WIND"
    wind_code = "S0112918"

class DaDouChanLiang_ZhongGuo_GuJi_WIND(sdb_base, WindData):
    field_name = u"产量"
    col_name = u"大豆产量_中国_估计_WIND"
    wind_code = "S0112904"

class DaDouChanLiang_QuanQiu_GuJi_WIND(sdb_base, WindData):
    field_name = u"产量"
    col_name = u"大豆产量_全球_估计_WIND"
    wind_code = "S0112305"


###########################################################################################################################
""" 出口量 """  

class DaDouChuKouLiang_MeiGuo_USDA(sdb_base, Manual):
    field_name = u"出口量"
    col_name = u"大豆出口量_美国_USDA"

class DaDouChuKouLiang_BaXi_USDA(sdb_base, Manual):
    field_name = u"出口量"
    col_name = u"大豆出口量_巴西_USDA"

class DaDouChuKouLiang_AGenTing_USDA(sdb_base, Manual):
    field_name = u"出口量"
    col_name = u"大豆出口量_阿根廷_USDA"

class DaDouChuKouLiang_ZhongGuo_USDA(sdb_base, Manual):
    field_name = u"出口量"
    col_name = u"大豆出口量_中国_USDA"

class DaDouChuKouLiang_QuanQiu_USDA(sdb_base, Manual):
    field_name = u"出口量"
    col_name = u"大豆出口量_全球_USDA"

class DaDouChuKou_MeiGuo_YuCe_WIND(sdb_base, WindData):
    field_name = u"出口量"
    col_name = u"大豆出口_美国_预测_WIND"
    wind_code = "S0113231"

class DaDouChuKou_BaXi_YuCe_WIND(sdb_base, WindData):
    field_name = u"出口量"
    col_name = u"大豆出口_巴西_预测_WIND"
    wind_code = "S0113245"

class DaDouChuKou_AGenTing_YuCe_WIND(sdb_base, WindData):
    field_name = u"出口量"
    col_name = u"大豆出口_阿根廷_预测_WIND"
    wind_code = "S0113252"

class DaDouChuKou_ZhongGuo_YuCe_WIND(sdb_base, WindData):
    field_name = u"出口量"
    col_name = u"大豆出口_中国_预测_WIND"
    wind_code = "S0113238"

class DaDouChuKou_QuanQiu_YuCe_WIND(sdb_base, WindData):
    field_name = u"出口量"
    col_name = u"大豆出口_全球_预测_WIND"
    wind_code = "S0112362"

class DaDouChuKou_MeiGuo_GuJi_WIND(sdb_base, WindData):
    field_name = u"出口量"
    col_name = u"大豆出口_美国_估计_WIND"
    wind_code = "S0112901"

class DaDouChuKou_BaXi_GuJi_WIND(sdb_base, WindData):
    field_name = u"出口量"
    col_name = u"大豆出口_巴西_估计_WIND"
    wind_code = "S0112915"

class DaDouChuKou_AGenTing_GuJi_WIND(sdb_base, WindData):
    field_name = u"出口量"
    col_name = u"大豆出口_阿根廷_估计_WIND"
    wind_code = "S0112922"

class DaDouChuKou_ZhongGuo_GuJi_WIND(sdb_base, WindData):
    field_name = u"出口量"
    col_name = u"大豆出口_中国_估计_WIND"
    wind_code = "S0112908"

class DaDouChuKou_QuanQiu_GuJi_WIND(sdb_base, WindData):
    field_name = u"出口量"
    col_name = u"大豆出口_全球_估计_WIND"
    wind_code = "S0112309"

###########################################################################################################################
""" 单产 """  

class DaDouDanChan_MeiGuo_USDA(sdb_base, Manual):
    field_name = u"单产"
    col_name = u"大豆单产_美国_USDA"

class DaDouDanChan_BaXi_USDA(sdb_base, Manual):
    field_name = u"单产"
    col_name = u"大豆单产_巴西_USDA"

class DaDouDanChan_AGenTing_USDA(sdb_base, Manual):
    field_name = u"单产"
    col_name = u"大豆单产_阿根廷_USDA"

class DaDouDanChan_ZhongGuo_USDA(sdb_base, Manual):
    field_name = u"单产"
    col_name = u"大豆单产_中国_USDA"

class DaDouDanChan_QuanQiu_USDA(sdb_base, Manual):
    field_name = u"单产"
    col_name = u"大豆单产_全球_USDA"

class DaDouDanChan_MeiGuo_YuCeNianDu_WIND(sdb_base, WindData):
    field_name = u"单产"
    col_name = u"大豆单产_美国_预测年度_WIND"
    wind_code = "S0118631"

class DaDouDanChan_BaXi_YuCeNianDu_WIND(sdb_base, WindData):
    field_name = u"单产"
    col_name = u"大豆单产_巴西_预测年度_WIND"
    wind_code = "S0118632"

class DaDouDanChan_AGenTing_YuCeNianDu_WIND(sdb_base, WindData):
    field_name = u"单产"
    col_name = u"大豆单产_阿根廷_预测年度_WIND"
    wind_code = "S0118633"

class DaDouDanChan_ZhongGuo_YuCeNianDu_WIND(sdb_base, WindData):
    field_name = u"单产"
    col_name = u"大豆单产_中国_预测年度_WIND"
    wind_code = "S0118635"




    
if __name__ == "__main__":
    a = JiaChunJinKouLiang().get_ts()
    
    
    
    
    
    
    
    
    
    