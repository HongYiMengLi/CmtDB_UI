# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 10:45:53 2018

@author: 李弘一萌
"""

import pandas as pd
from datetime import datetime
from .BU_Base import BU_Base
from ...Base.DataType_Base import Manual, Computed, WindData
from ...Base.Plot_Base import Plot_Base
from matplotlib.ticker import FuncFormatter

class downstream_base(BU_Base, Plot_Base):
    table_english_name = "Downstream"
    table_chinese_name = u"下游"
    a = 0
    
    def output(self):
        print("Downstream")
    
    def get_relevant_df(self, col_list):
        local_col_name_list = downstream_base.get_all_table_classname()
        col_cls_list = []
        for x in col_list:
            col_cls_name = str(BU_Base.get_class_name(x))
            if col_cls_name not in local_col_name_list:
                col_cls_list.append(eval(BU_Base.get_table_class_full_variable(x)))
            else:
                col_cls_list.append(eval(col_cls_name))
        ts_list = [x().get_ts() for x in col_cls_list]
        tmp_table_df = pd.concat(ts_list, axis=1).dropna(how="all")
        return tmp_table_df 
    
    
###########################################################################################################################
""" 公路投资 """

class GongLuLiCheng_GaoSuGongLu(downstream_base, WindData):
    field_name = u"公路投资"
    col_name = u"公路里程_高速公路"
    wind_code = "S0044616"  
    
class JiaoTongGuDingZiChanTouZi_GongLuJianShe_QuanGuo_LeiJiZhi(downstream_base, WindData):
    field_name = u"公路投资"
    col_name = u"交通固定资产投资_公路建设_全国_累计值"
    wind_code = "S0068322"      
    
class JiaoTongGuDingZiChanTouZi_GongLuJianShe_DongBuDiQu_LeiJiZhi(downstream_base, WindData):
    field_name = u"公路投资"
    col_name = u"交通固定资产投资_公路建设_东部地区_累计值"
    wind_code = "S0068323"  

class JiaoTongGuDingZiChanTouZi_GongLuJianShe_ZhongBuDiQu_LeiJiZhi(downstream_base, WindData):
    field_name = u"公路投资"
    col_name = u"交通固定资产投资_公路建设_中部地区_累计值"
    wind_code = "S0068324"  

class JiaoTongGuDingZiChanTouZi_GongLuJianShe_XiBuDiQu_LeiJiZhi(downstream_base, WindData):
    field_name = u"公路投资"
    col_name = u"交通固定资产投资_公路建设_西部地区_累计值"
    wind_code = "S0068325"  

class JiaoTongGuDingZiChanTouZi_GongLuJianShe_BeiJing_LeiJiZhi(downstream_base, WindData):
    field_name = u"公路投资"
    col_name = u"交通固定资产投资_公路建设_北京_累计值"
    wind_code = "S0068326"  

class JiaoTongGuDingZiChanTouZi_GongLuJianShe_TianJin_LeiJiZhi(downstream_base, WindData):
    field_name = u"公路投资"
    col_name = u"交通固定资产投资_公路建设_天津_累计值"
    wind_code = "S0068327"  

class JiaoTongGuDingZiChanTouZi_GongLuJianShe_HeBei_LeiJiZhi(downstream_base, WindData):
    field_name = u"公路投资"
    col_name = u"交通固定资产投资_公路建设_河北_累计值"
    wind_code = "S0068328"  

class JiaoTongGuDingZiChanTouZi_GongLuJianShe_ShanXi_LeiJiZhi(downstream_base, WindData):
    field_name = u"公路投资"
    col_name = u"交通固定资产投资_公路建设_山西_累计值"
    wind_code = "S0068329"  

class JiaoTongGuDingZiChanTouZi_GongLuJianShe_NeiMengGu_LeiJiZhi(downstream_base, WindData):
    field_name = u"公路投资"
    col_name = u"交通固定资产投资_公路建设_内蒙古_累计值"
    wind_code = "S0068330"  

class JiaoTongGuDingZiChanTouZi_GongLuJianShe_LiaoNing_LeiJiZhi(downstream_base, WindData):
    field_name = u"公路投资"
    col_name = u"交通固定资产投资_公路建设_辽宁_累计值"
    wind_code = "S0068331"  

class JiaoTongGuDingZiChanTouZi_GongLuJianShe_JiLin_LeiJiZhi(downstream_base, WindData):
    field_name = u"公路投资"
    col_name = u"交通固定资产投资_公路建设_吉林_累计值"
    wind_code = "S0068332"  

class JiaoTongGuDingZiChanTouZi_GongLuJianShe_HeiLongJiang_LeiJiZhi(downstream_base, WindData):
    field_name = u"公路投资"
    col_name = u"交通固定资产投资_公路建设_黑龙江_累计值"
    wind_code = "S0068333"  

class JiaoTongGuDingZiChanTouZi_GongLuJianShe_ShangHai_LeiJiZhi(downstream_base, WindData):
    field_name = u"公路投资"
    col_name = u"交通固定资产投资_公路建设_上海_累计值"
    wind_code = "S0068334"  

class JiaoTongGuDingZiChanTouZi_GongLuJianShe_JiangSu_LeiJiZhi(downstream_base, WindData):
    field_name = u"公路投资"
    col_name = u"交通固定资产投资_公路建设_江苏_累计值"
    wind_code = "S0068335"  

class JiaoTongGuDingZiChanTouZi_GongLuJianShe_ZheJiang_LeiJiZhi(downstream_base, WindData):
    field_name = u"公路投资"
    col_name = u"交通固定资产投资_公路建设_浙江_累计值"
    wind_code = "S0068336"  

class JiaoTongGuDingZiChanTouZi_GongLuJianShe_AnHui_LeiJiZhi(downstream_base, WindData):
    field_name = u"公路投资"
    col_name = u"交通固定资产投资_公路建设_安徽_累计值"
    wind_code = "S0068337"  

class JiaoTongGuDingZiChanTouZi_GongLuJianShe_FuJian_LeiJiZhi(downstream_base, WindData):
    field_name = u"公路投资"
    col_name = u"交通固定资产投资_公路建设_福建_累计值"
    wind_code = "S0068338"      

class JiaoTongGuDingZiChanTouZi_GongLuJianShe_JiangXi_LeiJiZhi(downstream_base, WindData):
    field_name = u"公路投资"
    col_name = u"交通固定资产投资_公路建设_江西_累计值"
    wind_code = "S0068339"   


class JiaoTongGuDingZiChanTouZi_GongLuJianShe_ShanDong_LeiJiZhi(downstream_base, WindData):
    field_name = u"公路投资"
    col_name = u"交通固定资产投资_公路建设_山东_累计值"
    wind_code = "S0068340"   


class JiaoTongGuDingZiChanTouZi_GongLuJianShe_HeNan_LeiJiZhi(downstream_base, WindData):
    field_name = u"公路投资"
    col_name = u"交通固定资产投资_公路建设_河南_累计值"
    wind_code = "S0068341"   


class JiaoTongGuDingZiChanTouZi_GongLuJianShe_HuBei_LeiJiZhi(downstream_base, WindData):
    field_name = u"公路投资"
    col_name = u"交通固定资产投资_公路建设_湖北_累计值"
    wind_code = "S0068342"   

class JiaoTongGuDingZiChanTouZi_GongLuJianShe_HuNan_LeiJiZhi(downstream_base, WindData):
    field_name = u"公路投资"
    col_name = u"交通固定资产投资_公路建设_湖南_累计值"
    wind_code = "S0068343"   

class JiaoTongGuDingZiChanTouZi_GongLuJianShe_GuangDong_LeiJiZhi(downstream_base, WindData):
    field_name = u"公路投资"
    col_name = u"交通固定资产投资_公路建设_广东_累计值"
    wind_code = "S0068344"   

class JiaoTongGuDingZiChanTouZi_GongLuJianShe_GuangXi_LeiJiZhi(downstream_base, WindData):
    field_name = u"公路投资"
    col_name = u"交通固定资产投资_公路建设_广西_累计值"
    wind_code = "S0068345"   

class JiaoTongGuDingZiChanTouZi_GongLuJianShe_HaiNan_LeiJiZhi(downstream_base, WindData):
    field_name = u"公路投资"
    col_name = u"交通固定资产投资_公路建设_海南_累计值"
    wind_code = "S0068346"   

class JiaoTongGuDingZiChanTouZi_GongLuJianShe_ChongQing_LeiJiZhi(downstream_base, WindData):
    field_name = u"公路投资"
    col_name = u"交通固定资产投资_公路建设_重庆_累计值"
    wind_code = "S0068347"       
    
class JiaoTongGuDingZiChanTouZi_GongLuJianShe_SiChuan_LeiJiZhi(downstream_base, WindData):
    field_name = u"公路投资"
    col_name = u"交通固定资产投资_公路建设_四川_累计值"
    wind_code = "S0068348"      
    
class JiaoTongGuDingZiChanTouZi_GongLuJianShe_GuiZhou_LeiJiZhi(downstream_base, WindData):
    field_name = u"公路投资"
    col_name = u"交通固定资产投资_公路建设_贵州_累计值"
    wind_code = "S0068349"      
    
class JiaoTongGuDingZiChanTouZi_GongLuJianShe_YunNan_LeiJiZhi(downstream_base, WindData):
    field_name = u"公路投资"
    col_name = u"交通固定资产投资_公路建设_云南_累计值"
    wind_code = "S0068350"      

class JiaoTongGuDingZiChanTouZi_GongLuJianShe_XiZang_LeiJiZhi(downstream_base, WindData):
    field_name = u"公路投资"
    col_name = u"交通固定资产投资_公路建设_西藏_累计值"
    wind_code = "S0068351"  

class JiaoTongGuDingZiChanTouZi_GongLuJianShe_ShanXii_LeiJiZhi(downstream_base, WindData):
    field_name = u"公路投资"
    col_name = u"交通固定资产投资_公路建设_陕西_累计值"
    wind_code = "S0068352"  
    
class JiaoTongGuDingZiChanTouZi_GongLuJianShe_GanSu_LeiJiZhi(downstream_base, WindData):
    field_name = u"公路投资"
    col_name = u"交通固定资产投资_公路建设_甘肃_累计值"
    wind_code = "S0068353"      

class JiaoTongGuDingZiChanTouZi_GongLuJianShe_QingHai_LeiJiZhi(downstream_base, WindData):
    field_name = u"公路投资"
    col_name = u"交通固定资产投资_公路建设_青海_累计值"
    wind_code = "S0068354"  

class JiaoTongGuDingZiChanTouZi_GongLuJianShe_NingXia_LeiJiZhi(downstream_base, WindData):
    field_name = u"公路投资"
    col_name = u"交通固定资产投资_公路建设_宁夏_累计值"
    wind_code = "S0068355"  
    
class JiaoTongGuDingZiChanTouZi_GongLuJianShe_XinJiang_LeiJiZhi(downstream_base, WindData):
    field_name = u"公路投资"
    col_name = u"交通固定资产投资_公路建设_新疆_累计值"
    wind_code = "S0068356"  

class GuDingZiChanTouZiWanChengDong_JiChuSheShiJianSheTouZi_LeiJiTongBi(downstream_base, WindData):
    field_name = u"公路投资"
    col_name = u"固定资产投资完成额_基础设施建设投资_累计同比"
    wind_code = "M5440435"  

class GuDingZiChanTouZiWanChengDong_LeiJiTongBi(downstream_base, WindData):
    field_name = u"公路投资"
    col_name = u"固定资产投资完成额_累计同比"
    wind_code = "M0000273"  

class QuanGuoJiaoTongGuDingZiChanTouZi_GongLuJianShe_LeiJiTongBi(downstream_base, Computed):
    field_name = u"公路投资"
    col_name = u"全国交通固定资产投资_公路建设_累计同比"   
    def get_ts_whole_progress(self):
        relevant_col_list = [u"交通固定资产投资_公路建设_全国_累计值"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = (tmp_total[u"交通固定资产投资_公路建设_全国_累计值"] / tmp_total[u"交通固定资产投资_公路建设_全国_累计值"].shift(12) - 1) / 100
        return tmp_total  
    
###########################################################################################################################
""" 销量 """

class YaLuJiXiaoLiang_DangYueZhi(downstream_base, WindData):
    field_name = u"公路投资"
    col_name = u"压路机销量_当月值"
    wind_code = "S6001583"  
    
class WaJueJiXiaoLiang_DangYueZhi(downstream_base, WindData):
    field_name = u"公路投资"
    col_name = u"挖掘机销量_当月值"
    wind_code = "S6001312"  




































    

    