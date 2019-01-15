# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 10:48:40 2018

@author: 李弘一萌
"""

import pandas as pd
from datetime import datetime
from .CF_Base import CF_Base
from ...Base.DataType_Base import Manual, Computed, WindData
from ...Base.Plot_Base import Plot_Base
from matplotlib.ticker import FuncFormatter

class sdb_base(CF_Base, Plot_Base):
    table_english_name = "SupplyDemandBalance"
    table_chinese_name = u"供需平衡表"
    
    def output(self):
        print(self.table_english_name)
    
    def get_relevant_df(self, col_list):
        local_col_name_list = sdb_base.get_all_table_classname()
        col_cls_list = []
        for x in col_list:
            col_cls_name = str(CF_Base.get_class_name(x))
            if col_cls_name not in local_col_name_list:
                col_cls_list.append(eval(CF_Base.get_table_class_full_variable(x)))
            else:
                col_cls_list.append(eval(col_cls_name))
        ts_list = [x().get_ts() for x in col_cls_list]
        tmp_table_df = pd.concat(ts_list, axis=1).dropna(how="all")
        return tmp_table_df 


###########################################################################################################################
""" 国内棉花产量 """    

class MianHuaChanLiangYuGu_QuanGuo_ZhongGuoMianHuaXinXiWang(sdb_base, Manual):
    field_name = u"国内棉花产量"
    col_name = u"棉花产量预估_全国_中国棉花信息网"

class MianHuaChanLiangYuGu_QuanGuo_USDA(sdb_base, Manual):
    field_name = u"国内棉花产量"
    col_name = u"棉花产量预估_全国_USDA"

class MianHuaChanLiang_QuanGuo_GuoJiaTongJiJu(sdb_base, WindData):
    field_name = u"国内棉花产量"
    col_name = u"棉花产量_全国_国家统计局"
    wind_code = "S0031760"
    
###########################################################################################################################
""" 国内棉花出口量 """  

class MianHuaChuKouYuGu_QuanGuo_ZhongGuoMianHuaXinXiWang(sdb_base, Manual):
    field_name = u"国内棉花出口量"
    col_name = u"棉花出口预估_全国_中国棉花信息网"

class MianHuaChuKouYuGu_QuanGuo_USDA(sdb_base, Manual):
    field_name = u"国内棉花出口量"
    col_name = u"棉花出口预估_全国_USDA"


class MianHuaChuKou_QuanGuo_HaiGuanZongShu_DangYue(sdb_base, WindData):
    field_name = u"国内棉花出口量"
    col_name = u"棉花出口_全国_海关总署_当月"
    wind_code = "S0072026"

class MianHuaChuKou_QuanGuo_HaiGuanZongShu_LeiJi(sdb_base, WindData):
    field_name = u"国内棉花出口量"
    col_name = u"棉花出口_全国_海关总署_累计"
    wind_code = "S0072211"

###########################################################################################################################
""" 国内棉花进口量 """  

class MianHuaJinKouYuGu_QuanGuo_ZhongGuoMianHuaXinXiWang(sdb_base, Manual):
    field_name = u"国内棉花进口量"
    col_name = u"棉花进口预估_全国_中国棉花信息网"

class MianHuaJinKouYuGu_QuanGuo_USDA(sdb_base, Manual):
    field_name = u"国内棉花进口量"
    col_name = u"棉花进口预估_全国_USDA"

class MianHuaJinKou_QuanGuo_HaiGuanZongShu_DangYue(sdb_base, WindData):
    field_name = u"国内棉花进口量"
    col_name = u"棉花进口_全国_海关总署_当月"
    wind_code = "S0071219"

class MianHuaJinKou_QuanGuo_HaiGuanZongShu_LeiJi(sdb_base, WindData):
    field_name = u"国内棉花进口量"
    col_name = u"棉花进口_全国_海关总署_累计"
    wind_code = "S0071356"

###########################################################################################################################
""" 国内棉花期初库存 """  

class MianHuaQiChuKuCunYuGu_QuanGuo_ZhongGuoMianHuaXinXiWang(sdb_base, Manual):
    field_name = u"国内棉花期初库存"
    col_name = u"棉花期初库存预估_全国_中国棉花信息网"

class MianHuaQiChuKuCunYuGu_QuanGuo_USDA(sdb_base, Manual):
    field_name = u"国内棉花期初库存"
    col_name = u"棉花期初库存预估_全国_USDA"

###########################################################################################################################
""" 国内棉花期末库存 """  

class MianHuaQiMoKuCunYuGu_QuanGuo_ZhongGuoMianHuaXinXiWang(sdb_base, Manual):
    field_name = u"国内棉花期末库存"
    col_name = u"棉花期末库存预估_全国_中国棉花信息网"

class MianHuaQiMoKuCunYuGu_QuanGuo_USDA(sdb_base, Manual):
    field_name = u"国内棉花期末库存"
    col_name = u"棉花期末库存预估_全国_USDA"

###########################################################################################################################
""" 国内棉花消费量 """  

class MianHuaXiaoFeiYuGu_QuanGuo_ZhongGuoMianHuaXinXiWang(sdb_base, Manual):
    field_name = u"国内棉花消费量"
    col_name = u"棉花消费预估_全国_中国棉花信息网"

class MianHuaXiaoFeiYuGu_QuanGuo_USDA(sdb_base, Manual):
    field_name = u"国内棉花消费量"
    col_name = u"棉花消费预估_全国_USDA"

###########################################################################################################################
""" 美国棉花产量 """  

class MianHuaChanLiangYuGu_MeiGuo_USDA(sdb_base, Manual):
    field_name = u"美国棉花产量"
    col_name = u"棉花产量预估_美国_USDA"

###########################################################################################################################
""" 美国棉花出口量 """  

class MianHuaChuKouYuGu_MeiGuo_USDA(sdb_base, Manual):
    field_name = u"美国棉花出口量"
    col_name = u"棉花出口预估_美国_USDA"

###########################################################################################################################
""" 美国棉花进口量 """  

class MianHuaJinKouYuGu_MeiGuo_USDA(sdb_base, Manual):
    field_name = u"美国棉花进口量"
    col_name = u"棉花进口预估_美国_USDA"

###########################################################################################################################
""" 美国棉花期初库存 """  

class MianHuaQiChuKuCunYuGu_MeiGuo_USDA(sdb_base, Manual):
    field_name = u"美国棉花期初库存"
    col_name = u"棉花期初库存预估_美国_USDA"

###########################################################################################################################
""" 美国棉花期末库存 """  

class MianHuaQiMoKuCunYuGu_MeiGuo_USDA(sdb_base, Manual):
    field_name = u"美国棉花期末库存"
    col_name = u"棉花期末库存预估_美国_USDA"

###########################################################################################################################
""" 美国棉花消费量 """  

class MianHuaXiaoFeiYuGu_MeiGuo_USDA(sdb_base, Manual):
    field_name = u"美国棉花消费量"
    col_name = u"棉花消费预估_美国_USDA"

###########################################################################################################################
""" 棉纱产量 """  

class MianShaChanLiang_NianDu(sdb_base, Manual):
    field_name = u"棉纱产量"
    col_name = u"棉纱产量_年度"

###########################################################################################################################
""" 棉纱出口 """  

class MianShaChuKou_NianDu(sdb_base, Manual):
    field_name = u"棉纱出口"
    col_name = u"棉纱出口_年度"

###########################################################################################################################
""" 棉纱进口 """  

class MianShaJinKou_NianDu(sdb_base, Manual):
    field_name = u"棉纱进口"
    col_name = u"棉纱进口_年度"

###########################################################################################################################
""" 棉纱期初库存 """  

class MianShaQiChuKuCun_NianDu(sdb_base, Manual):
    field_name = u"棉纱期初库存"
    col_name = u"棉纱期初库存_年度"

###########################################################################################################################
""" 棉纱期末库存 """  

class MianShaQiMoKuCun_NianDu(sdb_base, Manual):
    field_name = u"棉纱期末库存"
    col_name = u"棉纱期末库存_年度"

###########################################################################################################################
""" 棉纱消费量 """  

class MianShaXiaoFeiLiang_NianDu(sdb_base, Manual):
    field_name = u"棉纱消费量"
    col_name = u"棉纱消费量_年度"

###########################################################################################################################
""" 全球棉花产量 """  

class MianHuaChanLiangYuGu_QuanQiu_USDA(sdb_base, Manual):
    field_name = u"全球棉花产量"
    col_name = u"棉花产量预估_全球_USDA"


###########################################################################################################################
""" 全球棉花出口量 """  

class MianHuaChuKouYuGu_QuanQiu_USDA(sdb_base, Manual):
    field_name = u"全球棉花出口量"
    col_name = u"棉花出口预估_全球_USDA"

###########################################################################################################################
""" 全球棉花进口量 """  

class MianHuaJinKouYuGu_QuanQiu_USDA(sdb_base, Manual):
    field_name = u"全球棉花进口量"
    col_name = u"棉花进口预估_全球_USDA"

###########################################################################################################################
""" 全球棉花期初库存 """  

class MianHuaQiChuKuCunYuGu_QuanQiu_USDA(sdb_base, Manual):
    field_name = u"棉纱期初库存"
    col_name = u"棉花期初库存预估_全球_USDA"

###########################################################################################################################
""" 全球棉花期末库存 """  

class MianHuaQiMoKuCunYuGu_QuanQiu_USDA(sdb_base, Manual):
    field_name = u"全球棉花期末库存"
    col_name = u"棉花期末库存预估_全球_USDA"

###########################################################################################################################
""" 全球棉花消费量 """  

class MianHuaXiaoFeiYuGu_QuanQiu_USDA(sdb_base, Manual):
    field_name = u"全球棉花消费量"
    col_name = u"棉花消费预估_全球_USDA"








    
if __name__ == "__main__":
    a = JiaChunJinKouLiang().get_ts()
    
    
    
    
    
    
    
    
    
    