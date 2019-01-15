# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 10:45:53 2018

@author: 李弘一萌
"""

import pandas as pd
from datetime import datetime
from .CU_Base import CU_Base
from ...Base.DataType_Base import Manual, Computed, WindData
from ...Base.Plot_Base import Plot_Base
from matplotlib.ticker import FuncFormatter

class downstream_base(CU_Base, Plot_Base):
    table_english_name = "Downstream"
    table_chinese_name = u"下游"
#    original_db_filepath = data_path + u"LPP价格数据库.xlsx"
    
    def output(self):
        print("Downstream")
    
    def get_relevant_df(self, col_list):
        local_col_name_list = downstream_base.get_all_table_classname()
        col_cls_list = []
        for x in col_list:
            col_cls_name = str(CU_Base.get_class_name(x))
            if col_cls_name not in local_col_name_list:
                col_cls_list.append(eval(CU_Base.get_table_class_full_variable(x)))
            else:
                col_cls_list.append(eval(col_cls_name))
        ts_list = [x().get_ts() for x in col_cls_list]
        tmp_table_df = pd.concat(ts_list, axis=1).dropna(how="all")
        return tmp_table_df 


###########################################################################################################################
""" 电力电网 """


class DianWangJiBenJianSheTouZiWanChengE_LeiJiZhi(downstream_base, WindData):
    field_name = u"电力电网"
    col_name = u"电网基本建设投资完成额_累计值"
    wind_code = "S5108453"
    
class DianYuanJiBenJianSheTouZiWanChengE_LeiJiZhi(downstream_base, WindData):
    field_name = u"电力电网"
    col_name = u"电源基本建设投资完成额_累计值"
    wind_code = "S5108448"
    
class ChanLiang_FaDianSheBei_DangYueZhi(downstream_base, WindData):
    field_name = u"电力电网"
    col_name = u"产量_发电设备_当月值"
    wind_code = "S0027818"
    
class ChanLiang_FaDianLiang_DangYueZhi(downstream_base, WindData):
    field_name = u"电力电网"
    col_name = u"产量_发电量_当月值"
    wind_code = "S0027012"
    

    
###########################################################################################################################
""" 房地产 """


class BenNianGouZhiTuDiMianJi_LeiJiZhi(downstream_base, WindData):
    field_name = u"房地产"
    col_name = u"本年购置土地面积_累计值"
    wind_code = "S0029666"
        
class FangWuShiGongMianJi_LeiJiZhi(downstream_base, WindData):
    field_name = u"房地产"
    col_name = u"房屋施工面积_累计值"
    wind_code = "S0029668"    
    
class FangWuXinKaiGongMianJi_LeiJiZhi(downstream_base, WindData):
    field_name = u"房地产"
    col_name = u"房屋新开工面积_累计值"
    wind_code = "S0029669"    
    
class FangWuJunGongMianJi_LeiJiZhi(downstream_base, WindData):
    field_name = u"房地产"
    col_name = u"房屋竣工面积_累计值"
    wind_code = "S0029670"    
    
class ShangPinFangXiaoShouMianJi_LeiJiZhi(downstream_base, WindData):
    field_name = u"房地产"
    col_name = u"商品房销售面积_累计值"
    wind_code = "S0029658"    
    
###########################################################################################################################
""" 家电及日用品 """

class KongDiaoChanLiang_DangYueZhi(downstream_base, WindData):
    field_name = u"家电及日用品"
    col_name = u"空调产量_当月值"
    wind_code = "S0028202"    

class JiaYongDianBingXiangChanLiang_DangYueZhi(downstream_base, WindData):
    field_name = u"家电及日用品"
    col_name = u"家用电冰箱产量_当月值"
    wind_code = "S0028206"  
    
class CaiDianChanLiang_DangYueZhi(downstream_base, WindData):
    field_name = u"家电及日用品"
    col_name = u"彩电产量_当月值"
    wind_code = "S0028198"    

class LengGuiChanLiang_DangYueZhi(downstream_base, WindData):
    field_name = u"家电及日用品"
    col_name = u"冷柜产量_当月值"
    wind_code = "S0028214"    
    
class JiaYongXiYiJiChanLiang_DangYueZhi(downstream_base, WindData):
    field_name = u"家电及日用品"
    col_name = u"家用洗衣机产量_当月值"
    wind_code = "S0028210"    

class ShouJiChanLiang_DangYueZhi(downstream_base, WindData):
    field_name = u"家电及日用品"
    col_name = u"手机产量_当月值"
    wind_code = "S0070283"    
    
class WeiXingDianZiJiSuanJiChanLiang_DangYueZhi(downstream_base, WindData):
    field_name = u"家电及日用品"
    col_name = u"微型电子计算机产量_当月值"
    wind_code = "S0028194"    

###########################################################################################################################
""" 汽车交运 """

class QiCheChanLiang_DangYueZhi(downstream_base, WindData):
    field_name = u"汽车交运"
    col_name = u"汽车产量_当月值"
    wind_code = "S0105523"    

class QiCheXiaoLiang_DangYueZhi(downstream_base, WindData):
    field_name = u"汽车交运"
    col_name = u"汽车销量_当月值"
    wind_code = "S0105710"  
    
class MoTuoCheChanLiang_DangYueZhi(downstream_base, WindData):
    field_name = u"汽车交运"
    col_name = u"摩托车产量_当月值"
    wind_code = "S0027862"    

class TieLuJiCheChanLiang_DangYueZhi(downstream_base, WindData):
    field_name = u"汽车交运"
    col_name = u"铁路机车产量_当月值"
    wind_code = "S0027854"    
    
class XinNengYuanQiCheChanLiang_DangYueZhi(downstream_base, WindData):
    field_name = u"汽车交运"
    col_name = u"新能源汽车产量_当月值"
    wind_code = "S0243299"    

    
###########################################################################################################################
""" 铜加工材价格 """    

class WuYangTongSi3mm_Ying_JiaGe(downstream_base, Manual):
    field_name = u"铜加工材价格"
    col_name = u"3mm无氧铜丝(硬)价格"
    
class WuYangTongSi3mm_Ruan_JiaGe(downstream_base, Manual):
    field_name = u"铜加工材价格"
    col_name = u"3mm无氧铜丝(软)价格"

class WuYangTongGan8mmJiaGe(downstream_base, Manual):
    field_name = u"铜加工材价格"
    col_name = u"8mm无氧铜杆价格"

class QiBaoXianJiaGe(downstream_base, Manual):
    field_name = u"铜加工材价格"
    col_name = u"漆包线价格"


###########################################################################################################################
""" 中国固定资产投资 """

class GuDingZiChanTouZiWanChengE_LeiJiZhi(downstream_base, WindData):
    field_name = u"中国固定资产投资"
    col_name = u"固定资产投资完成额_累计值"
    wind_code = "M0000272"    

class XinZengGuDingZiChanTouZiWanChengE_LeiJiZhi(downstream_base, WindData):
    field_name = u"中国固定资产投资"
    col_name = u"新增固定资产投资完成额_累计值"
    wind_code = "M0000274"    

class FangDiChanKaiFaTouZiWanChengE_LeiJiZhi(downstream_base, WindData):
    field_name = u"中国固定资产投资"
    col_name = u"房地产开发投资完成额_累计值"
    wind_code = "S0029656"    

class GuDingZiChanTouZiWanChengE_ZhiZaoYe_LeiJiZhi(downstream_base, WindData):
    field_name = u"中国固定资产投资"
    col_name = u"固定资产投资完成额_制造业_累计值"
    wind_code = "M0000356"    

class GuDingZiChanTouZiWanChengE_JiChuSheShiJianSheTouZi_LeiJiZhi(downstream_base, WindData):
    field_name = u"中国固定资产投资"
    col_name = u"固定资产投资完成额_基础设施建设投资_累计值"
    wind_code = "M5440434"    

class GuDingZiChanTouZiWanChengE_JianZhuYe_LeiJiZhi(downstream_base, WindData):
    field_name = u"中国固定资产投资"
    col_name = u"固定资产投资完成额_建筑业_累计值"
    wind_code = "M0000426"    











    
    
if __name__ == "__main__":
    ts = DiLunChangSiChanXiaoLv_15TianPingJun().get_ts()
    
    
    
    
    
    
    




    
    
    