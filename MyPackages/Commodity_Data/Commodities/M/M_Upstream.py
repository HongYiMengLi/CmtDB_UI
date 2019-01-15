# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 10:44:58 2018

@author: 李弘一萌
"""

import pandas as pd
from datetime import datetime
from .M_Base import M_Base
from ...Base.DataType_Base import Manual, Computed, WindData
from ...Base.Plot_Base import Plot_Base
from matplotlib.ticker import FuncFormatter

class upstream_base(M_Base, Plot_Base):
    table_english_name = "Upstream"
    table_chinese_name = u"上游"
    
    def output(self):
        print("Upstream")
    
    def get_relevant_df(self, col_list):
        local_col_name_list = upstream_base.get_all_table_classname()
        col_cls_list = []
        for x in col_list:
            col_cls_name = str(M_Base.get_class_name(x))
            if col_cls_name not in local_col_name_list:
                col_cls_list.append(eval(M_Base.get_table_class_full_variable(x)))
            else:
                col_cls_list.append(eval(col_cls_name))
        ts_list = [x().get_ts() for x in col_cls_list]
        tmp_table_df = pd.concat(ts_list, axis=1).dropna(how="all")
        return tmp_table_df

###########################################################################################################################
""" 产量 """  

class DaDouChanLiang_MeiGuo_USDA(upstream_base, Manual):
    field_name = u"产量"
    col_name = u"大豆产量_美国_USDA"

class DaDouChanLiang_BaXi_USDA(upstream_base, Manual):
    field_name = u"产量"
    col_name = u"大豆产量_巴西_USDA"
    
class DaDouChanLiang_AGenTing_USDA(upstream_base, Manual):
    field_name = u"产量"
    col_name = u"大豆产量_阿根廷_USDA"

class DaDouChanLiang_ZhongGuo_USDA(upstream_base, Manual):
    field_name = u"产量"
    col_name = u"大豆产量_中国_USDA"

class DaDouChanLiang_QuanQiu_USDA(upstream_base, Manual):
    field_name = u"产量"
    col_name = u"大豆产量_全球_USDA"
    
class DaDouChanLiang_MeiGuo_YuCe_WIND(upstream_base, WindData):
    field_name = u"产量"
    col_name = u"大豆产量_美国_预测_WIND"
    wind_code = "S0113227"

class DaDouChanLiang_BaXi_YuCe_WIND(upstream_base, WindData):
    field_name = u"产量"
    col_name = u"大豆产量_巴西_预测_WIND"
    wind_code = "S0113241"

class DaDouChanLiang_AGenTing_YuCe_WIND(upstream_base, WindData):
    field_name = u"产量"
    col_name = u"大豆产量_阿根廷_预测_WIND"
    wind_code = "S0113248"

class DaDouChanLiang_ZhongGuo_YuCe_WIND(upstream_base, WindData):
    field_name = u"产量"
    col_name = u"大豆产量_中国_预测_WIND"
    wind_code = "S0113234"

class DaDouChanLiang_QuanQiu_YuCe_WIND(upstream_base, WindData):
    field_name = u"产量"
    col_name = u"大豆产量_全球_预测_WIND"
    wind_code = "S0112358"

class DaDouChanLiang_MeiGuo_GuJi_WIND(upstream_base, WindData):
    field_name = u"产量"
    col_name = u"大豆产量_美国_估计_WIND"
    wind_code = "S0112897"

class DaDouChanLiang_BaXi_GuJi_WIND(upstream_base, WindData):
    field_name = u"产量"
    col_name = u"大豆产量_巴西_估计_WIND"
    wind_code = "S0112911"

class DaDouChanLiang_AGenTing_GuJi_WIND(upstream_base, WindData):
    field_name = u"产量"
    col_name = u"大豆产量_阿根廷_估计_WIND"
    wind_code = "S0112918"

class DaDouChanLiang_ZhongGuo_GuJi_WIND(upstream_base, WindData):
    field_name = u"产量"
    col_name = u"大豆产量_中国_估计_WIND"
    wind_code = "S0112904"

class DaDouChanLiang_QuanQiu_GuJi_WIND(upstream_base, WindData):
    field_name = u"产量"
    col_name = u"大豆产量_全球_估计_WIND"
    wind_code = "S0112305"

    
###########################################################################################################################
""" 产能利用率 """  

class DaDouYaZhaKaiJiLv(upstream_base, Manual):
    field_name = u"产能利用率"
    col_name = u"大豆压榨开机率"

###########################################################################################################################
""" 出口量 """  

class DaDouChuKouLiang_MeiGuo_USDA(upstream_base, Manual):
    field_name = u"出口量"
    col_name = u"大豆出口量_美国_USDA"

class DaDouChuKouLiang_BaXi_USDA(upstream_base, Manual):
    field_name = u"出口量"
    col_name = u"大豆出口量_巴西_USDA"

class DaDouChuKouLiang_AGenTing_USDA(upstream_base, Manual):
    field_name = u"出口量"
    col_name = u"大豆出口量_阿根廷_USDA"

class DaDouChuKouLiang_ZhongGuo_USDA(upstream_base, Manual):
    field_name = u"出口量"
    col_name = u"大豆出口量_中国_USDA"

class DaDouChuKouLiang_QuanQiu_USDA(upstream_base, Manual):
    field_name = u"出口量"
    col_name = u"大豆出口量_全球_USDA"

class DaDouChuKou_MeiGuo_YuCe_WIND(upstream_base, WindData):
    field_name = u"出口量"
    col_name = u"大豆出口_美国_预测_WIND"
    wind_code = "S0113231"

class DaDouChuKou_BaXi_YuCe_WIND(upstream_base, WindData):
    field_name = u"出口量"
    col_name = u"大豆出口_巴西_预测_WIND"
    wind_code = "S0113245"

class DaDouChuKou_AGenTing_YuCe_WIND(upstream_base, WindData):
    field_name = u"出口量"
    col_name = u"大豆出口_阿根廷_预测_WIND"
    wind_code = "S0113252"

class DaDouChuKou_ZhongGuo_YuCe_WIND(upstream_base, WindData):
    field_name = u"出口量"
    col_name = u"大豆出口_中国_预测_WIND"
    wind_code = "S0113238"

class DaDouChuKou_QuanQiu_YuCe_WIND(upstream_base, WindData):
    field_name = u"出口量"
    col_name = u"大豆出口_全球_预测_WIND"
    wind_code = "S0112362"

class DaDouChuKou_MeiGuo_GuJi_WIND(upstream_base, WindData):
    field_name = u"出口量"
    col_name = u"大豆出口_美国_估计_WIND"
    wind_code = "S0112901"

class DaDouChuKou_BaXi_GuJi_WIND(upstream_base, WindData):
    field_name = u"出口量"
    col_name = u"大豆出口_巴西_估计_WIND"
    wind_code = "S0112915"

class DaDouChuKou_AGenTing_GuJi_WIND(upstream_base, WindData):
    field_name = u"出口量"
    col_name = u"大豆出口_阿根廷_估计_WIND"
    wind_code = "S0112922"

class DaDouChuKou_ZhongGuo_GuJi_WIND(upstream_base, WindData):
    field_name = u"出口量"
    col_name = u"大豆出口_中国_估计_WIND"
    wind_code = "S0112908"

class DaDouChuKou_QuanQiu_GuJi_WIND(upstream_base, WindData):
    field_name = u"出口量"
    col_name = u"大豆出口_全球_估计_WIND"
    wind_code = "S0112309"

class MeiGuoDaDouBenZhouChuKou_LeiJiZhi(upstream_base, WindData):
    field_name = u"出口量"
    col_name = u"美国大豆本周出口_累计值"
    wind_code = "S0109422"

class MeiGuoDaDouDangQianShiChangNianDuWeiZhuangChuanLiang_DangZhouZhi(upstream_base, WindData):
    field_name = u"出口量"
    col_name = u"美国大豆当前市场年度未装船量_当周值"
    wind_code = "S0109424"

class MeiGuoDaDouDangQianShiChangNianDuChuKouLiang_LeiJiZhi(upstream_base, Computed):
    field_name = u"出口量"
    col_name = u"美国大豆当前市场年度出口量_累计值"   
    def get_ts_whole_progress(self):
        relevant_col_list = [u"美国大豆本周出口_累计值", u"美国大豆当前市场年度未装船量_当周值"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"美国大豆本周出口_累计值"] + tmp_total[u"美国大豆当前市场年度未装船量_当周值"]
        return tmp_total  
    
###########################################################################################################################
""" 单产 """  

class DaDouDanChan_MeiGuo_USDA(upstream_base, Manual):
    field_name = u"单产"
    col_name = u"大豆单产_美国_USDA"

class DaDouDanChan_BaXi_USDA(upstream_base, Manual):
    field_name = u"单产"
    col_name = u"大豆单产_巴西_USDA"

class DaDouDanChan_AGenTing_USDA(upstream_base, Manual):
    field_name = u"单产"
    col_name = u"大豆单产_阿根廷_USDA"

class DaDouDanChan_ZhongGuo_USDA(upstream_base, Manual):
    field_name = u"单产"
    col_name = u"大豆单产_中国_USDA"

class DaDouDanChan_QuanQiu_USDA(upstream_base, Manual):
    field_name = u"单产"
    col_name = u"大豆单产_全球_USDA"

class DaDouDanChan_MeiGuo_YuCeNianDu_WIND(upstream_base, WindData):
    field_name = u"单产"
    col_name = u"大豆单产_美国_预测年度_WIND"
    wind_code = "S0118631"

class DaDouDanChan_BaXi_YuCeNianDu_WIND(upstream_base, WindData):
    field_name = u"单产"
    col_name = u"大豆单产_巴西_预测年度_WIND"
    wind_code = "S0118632"

class DaDouDanChan_AGenTing_YuCeNianDu_WIND(upstream_base, WindData):
    field_name = u"单产"
    col_name = u"大豆单产_阿根廷_预测年度_WIND"
    wind_code = "S0118633"

class DaDouDanChan_ZhongGuo_YuCeNianDu_WIND(upstream_base, WindData):
    field_name = u"单产"
    col_name = u"大豆单产_中国_预测年度_WIND"
    wind_code = "S0118635"

###########################################################################################################################
""" 到港量 """  

class DaDouJinKouDaoGangYuGu(upstream_base, Manual):
    field_name = u"到港量"
    col_name = u"大豆进口到港预估"

class DaDouShiJiDaoGangLiang(upstream_base, Manual):
    field_name = u"到港量"
    col_name = u"大豆实际到港量"

###########################################################################################################################
""" 海运费 """  

class JinKouDaDouHaiYunFei_MeiWan_1Yue(upstream_base, Manual):
    field_name = u"海运费"
    col_name = u"进口大豆海运费_美湾_1月"

class JinKouDaDouHaiYunFei_MeiWan_2Yue(upstream_base, Manual):
    field_name = u"海运费"
    col_name = u"进口大豆海运费_美湾_2月"

class JinKouDaDouHaiYunFei_MeiWan_3Yue(upstream_base, Manual):
    field_name = u"海运费"
    col_name = u"进口大豆海运费_美湾_3月"

class JinKouDaDouHaiYunFei_MeiWan_4Yue(upstream_base, Manual):
    field_name = u"海运费"
    col_name = u"进口大豆海运费_美湾_4月"

class JinKouDaDouHaiYunFei_MeiWan_5Yue(upstream_base, Manual):
    field_name = u"海运费"
    col_name = u"进口大豆海运费_美湾_5月"

class JinKouDaDouHaiYunFei_MeiWan_6Yue(upstream_base, Manual):
    field_name = u"海运费"
    col_name = u"进口大豆海运费_美湾_6月"

class JinKouDaDouHaiYunFei_MeiWan_7Yue(upstream_base, Manual):
    field_name = u"海运费"
    col_name = u"进口大豆海运费_美湾_7月"

class JinKouDaDouHaiYunFei_MeiWan_8Yue(upstream_base, Manual):
    field_name = u"海运费"
    col_name = u"进口大豆海运费_美湾_8月"

class JinKouDaDouHaiYunFei_MeiWan_9Yue(upstream_base, Manual):
    field_name = u"海运费"
    col_name = u"进口大豆海运费_美湾_9月"

class JinKouDaDouHaiYunFei_MeiWan_10Yue(upstream_base, Manual):
    field_name = u"海运费"
    col_name = u"进口大豆海运费_美湾_10月"

class JinKouDaDouHaiYunFei_MeiWan_11Yue(upstream_base, Manual):
    field_name = u"海运费"
    col_name = u"进口大豆海运费_美湾_11月"

class JinKouDaDouHaiYunFei_MeiWan_12Yue(upstream_base, Manual):
    field_name = u"海运费"
    col_name = u"进口大豆海运费_美湾_12月"

class JinKouDaDouHaiYunFei_MeiXi_1Yue(upstream_base, Manual):
    field_name = u"海运费"
    col_name = u"进口大豆海运费_美西_1月"

class JinKouDaDouHaiYunFei_MeiXi_2Yue(upstream_base, Manual):
    field_name = u"海运费"
    col_name = u"进口大豆海运费_美西_2月"

class JinKouDaDouHaiYunFei_MeiXi_3Yue(upstream_base, Manual):
    field_name = u"海运费"
    col_name = u"进口大豆海运费_美西_3月"

class JinKouDaDouHaiYunFei_MeiXi_4Yue(upstream_base, Manual):
    field_name = u"海运费"
    col_name = u"进口大豆海运费_美西_4月"

class JinKouDaDouHaiYunFei_MeiXi_5Yue(upstream_base, Manual):
    field_name = u"海运费"
    col_name = u"进口大豆海运费_美西_5月"

class JinKouDaDouHaiYunFei_MeiXi_6Yue(upstream_base, Manual):
    field_name = u"海运费"
    col_name = u"进口大豆海运费_美西_6月"

class JinKouDaDouHaiYunFei_MeiXi_7Yue(upstream_base, Manual):
    field_name = u"海运费"
    col_name = u"进口大豆海运费_美西_7月"

class JinKouDaDouHaiYunFei_MeiXi_8Yue(upstream_base, Manual):
    field_name = u"海运费"
    col_name = u"进口大豆海运费_美西_8月"

class JinKouDaDouHaiYunFei_MeiXi_9Yue(upstream_base, Manual):
    field_name = u"海运费"
    col_name = u"进口大豆海运费_美西_9月"

class JinKouDaDouHaiYunFei_MeiXi_10Yue(upstream_base, Manual):
    field_name = u"海运费"
    col_name = u"进口大豆海运费_美西_10月"

class JinKouDaDouHaiYunFei_MeiXi_11Yue(upstream_base, Manual):
    field_name = u"海运费"
    col_name = u"进口大豆海运费_美西_11月"

class JinKouDaDouHaiYunFei_MeiXi_12Yue(upstream_base, Manual):
    field_name = u"海运费"
    col_name = u"进口大豆海运费_美西_12月"

class JinKouDaDouHaiYunFei_BaXi_1Yue(upstream_base, Manual):
    field_name = u"海运费"
    col_name = u"进口大豆海运费_巴西_1月"

class JinKouDaDouHaiYunFei_BaXi_2Yue(upstream_base, Manual):
    field_name = u"海运费"
    col_name = u"进口大豆海运费_巴西_2月"

class JinKouDaDouHaiYunFei_BaXi_3Yue(upstream_base, Manual):
    field_name = u"海运费"
    col_name = u"进口大豆海运费_巴西_3月"

class JinKouDaDouHaiYunFei_BaXi_4Yue(upstream_base, Manual):
    field_name = u"海运费"
    col_name = u"进口大豆海运费_巴西_4月"

class JinKouDaDouHaiYunFei_BaXi_5Yue(upstream_base, Manual):
    field_name = u"海运费"
    col_name = u"进口大豆海运费_巴西_5月"

class JinKouDaDouHaiYunFei_BaXi_6Yue(upstream_base, Manual):
    field_name = u"海运费"
    col_name = u"进口大豆海运费_巴西_6月"

class JinKouDaDouHaiYunFei_BaXi_7Yue(upstream_base, Manual):
    field_name = u"海运费"
    col_name = u"进口大豆海运费_巴西_7月"

class JinKouDaDouHaiYunFei_BaXi_8Yue(upstream_base, Manual):
    field_name = u"海运费"
    col_name = u"进口大豆海运费_巴西_8月"

class JinKouDaDouHaiYunFei_BaXi_9Yue(upstream_base, Manual):
    field_name = u"海运费"
    col_name = u"进口大豆海运费_巴西_9月"

class JinKouDaDouHaiYunFei_BaXi_10Yue(upstream_base, Manual):
    field_name = u"海运费"
    col_name = u"进口大豆海运费_巴西_10月"

class JinKouDaDouHaiYunFei_BaXi_11Yue(upstream_base, Manual):
    field_name = u"海运费"
    col_name = u"进口大豆海运费_巴西_11月"

class JinKouDaDouHaiYunFei_BaXi_12Yue(upstream_base, Manual):
    field_name = u"海运费"
    col_name = u"进口大豆海运费_巴西_12月"

class JinKouDaDouHaiYunFei_AGenTing_1Yue(upstream_base, Manual):
    field_name = u"海运费"
    col_name = u"进口大豆海运费_阿根廷_1月"

class JinKouDaDouHaiYunFei_AGenTing_2Yue(upstream_base, Manual):
    field_name = u"海运费"
    col_name = u"进口大豆海运费_阿根廷_2月"

class JinKouDaDouHaiYunFei_AGenTing_3Yue(upstream_base, Manual):
    field_name = u"海运费"
    col_name = u"进口大豆海运费_阿根廷_3月"

class JinKouDaDouHaiYunFei_AGenTing_4Yue(upstream_base, Manual):
    field_name = u"海运费"
    col_name = u"进口大豆海运费_阿根廷_4月"

class JinKouDaDouHaiYunFei_AGenTing_5Yue(upstream_base, Manual):
    field_name = u"海运费"
    col_name = u"进口大豆海运费_阿根廷_5月"

class JinKouDaDouHaiYunFei_AGenTing_6Yue(upstream_base, Manual):
    field_name = u"海运费"
    col_name = u"进口大豆海运费_阿根廷_6月"

class JinKouDaDouHaiYunFei_AGenTing_7Yue(upstream_base, Manual):
    field_name = u"海运费"
    col_name = u"进口大豆海运费_阿根廷_7月"

class JinKouDaDouHaiYunFei_AGenTing_8Yue(upstream_base, Manual):
    field_name = u"海运费"
    col_name = u"进口大豆海运费_阿根廷_8月"

class JinKouDaDouHaiYunFei_AGenTing_9Yue(upstream_base, Manual):
    field_name = u"海运费"
    col_name = u"进口大豆海运费_阿根廷_9月"

class JinKouDaDouHaiYunFei_AGenTing_10Yue(upstream_base, Manual):
    field_name = u"海运费"
    col_name = u"进口大豆海运费_阿根廷_10月"

class JinKouDaDouHaiYunFei_AGenTing_11Yue(upstream_base, Manual):
    field_name = u"海运费"
    col_name = u"进口大豆海运费_阿根廷_11月"

class JinKouDaDouHaiYunFei_AGenTing_12Yue(upstream_base, Manual):
    field_name = u"海运费"
    col_name = u"进口大豆海运费_阿根廷_12月"

###########################################################################################################################
""" 进口成本 """  

class JinKouDaDouDaoGangWanShuiChengBen_MeiWan_1Yue(upstream_base, Computed):
    field_name = u"进口成本"
    col_name = u"进口大豆到港完税成本_美湾_1月"
    def get_ts_whole_progress(self):
#        relevant_col_list = [u"中国棉花328价格指数", u"涤短价格_1.4D直纺涤短"]
#        tmp_total = self.get_relevant_df(relevant_col_list)
#        tmp_total[self.col_name] = tmp_total[u"中国棉花328价格指数"] - tmp_total[u"涤短价格_1.4D直纺涤短"]
#        return tmp_total  
        pass

###########################################################################################################################
""" 进口量 """  

class DaDouJinKouLiang_MeiGuo_USDA(upstream_base, Manual):
    field_name = u"进口量"
    col_name = u"大豆进口量_美国_USDA"

class DaDouJinKouLiang_BaXi_USDA(upstream_base, Manual):
    field_name = u"进口量"
    col_name = u"大豆进口量_巴西_USDA"

class DaDouJinKouLiang_AGenTing_USDA(upstream_base, Manual):
    field_name = u"进口量"
    col_name = u"大豆进口量_阿根廷_USDA"

class DaDouJinKouLiang_ZhongGuo_USDA(upstream_base, Manual):
    field_name = u"进口量"
    col_name = u"大豆进口量_中国_USDA"

class DaDouJinKouLiang_QuanQiu_USDA(upstream_base, Manual):
    field_name = u"进口量"
    col_name = u"大豆进口量_全球_USDA"

class DaDouJinKouLiang_OuMeng_USDA(upstream_base, Manual):
    field_name = u"进口量"
    col_name = u"大豆进口量_欧盟_USDA"

class DaDouJinKouLiang_MoXiGe_USDA(upstream_base, Manual):
    field_name = u"进口量"
    col_name = u"大豆进口量_墨西哥_USDA"

class DaDouJinKouLiang_RiBen_USDA(upstream_base, Manual):
    field_name = u"进口量"
    col_name = u"大豆进口量_日本_USDA"

class DaDouJinKouLiang_HaiGuan(upstream_base, Manual):
    field_name = u"进口量"
    col_name = u"大豆进口量_海关"

###########################################################################################################################
""" 库存 """  

class DaDouQiChuKuCun_MeiGuo_USDA(upstream_base, Manual):
    field_name = u"库存"
    col_name = u"大豆期初库存_美国_USDA"

class DaDouQiChuKuCun_BaXi_USDA(upstream_base, Manual):
    field_name = u"库存"
    col_name = u"大豆期初库存_巴西_USDA"

class DaDouQiChuKuCun_AGenTing_USDA(upstream_base, Manual):
    field_name = u"库存"
    col_name = u"大豆期初库存_阿根廷_USDA"

class DaDouQiChuKuCun_ZhongGuo_USDA(upstream_base, Manual):
    field_name = u"库存"
    col_name = u"大豆期初库存_中国_USDA"

class DaDouQiChuKuCun_QuanQiu_USDA(upstream_base, Manual):
    field_name = u"库存"
    col_name = u"大豆期初库存_全球_USDA"

class DaDouQiMoKuCun_MeiGuo_USDA(upstream_base, Manual):
    field_name = u"库存"
    col_name = u"大豆期末库存_美国_USDA"

class DaDouQiMoKuCun_BaXi_USDA(upstream_base, Manual):
    field_name = u"库存"
    col_name = u"大豆期末库存_巴西_USDA"

class DaDouQiMoKuCun_AGenTing_USDA(upstream_base, Manual):
    field_name = u"库存"
    col_name = u"大豆期末库存_阿根廷_USDA"

class DaDouQiMoKuCun_ZhongGuo_USDA(upstream_base, Manual):
    field_name = u"库存"
    col_name = u"大豆期末库存_中国_USDA"

class DaDouQiMoKuCun_QuanQiu_USDA(upstream_base, Manual):
    field_name = u"库存"
    col_name = u"大豆期末库存_全球_USDA"

class DaDouKuCun_MeiGuo_YuCe_WIND(upstream_base, WindData):
    field_name = u"库存"
    col_name = u"大豆库存_美国_预测_WIND"
    wind_code = "S0113232"

class DaDouKuCun_BaXi_YuCe_WIND(upstream_base, WindData):
    field_name = u"库存"
    col_name = u"大豆库存_巴西_预测_WIND"
    wind_code = "S0113246"

class DaDouKuCun_AGenTing_YuCe_WIND(upstream_base, WindData):
    field_name = u"库存"
    col_name = u"大豆库存_阿根廷_预测_WIND"
    wind_code = "S0113253"

class DaDouKuCun_ZhongGuo_YuCe_WIND(upstream_base, WindData):
    field_name = u"库存"
    col_name = u"大豆库存_中国_预测_WIND"
    wind_code = "S0113239"

class DaDouKuCun_QuanQiu_YuCe_WIND(upstream_base, WindData):
    field_name = u"库存"
    col_name = u"大豆库存_全球_预测_WIND"
    wind_code = "S0112363"

class DaDouKuCun_MeiGuo_GuJi_WIND(upstream_base, WindData):
    field_name = u"库存"
    col_name = u"大豆库存_美国_估计_WIND"
    wind_code = "S0112902"

class DaDouKuCun_BaXi_GuJi_WIND(upstream_base, WindData):
    field_name = u"库存"
    col_name = u"大豆库存_巴西_估计_WIND"
    wind_code = "S0112916"

class DaDouKuCun_AGenTing_GuJi_WIND(upstream_base, WindData):
    field_name = u"库存"
    col_name = u"大豆库存_阿根廷_估计_WIND"
    wind_code = "S0112923"

class DaDouKuCun_ZhongGuo_GuJi_WIND(upstream_base, WindData):
    field_name = u"库存"
    col_name = u"大豆库存_中国_估计_WIND"
    wind_code = "S0112909"

class DaDouKuCun_QuanQiu_GuJi_WIND(upstream_base, WindData):
    field_name = u"库存"
    col_name = u"大豆库存_全球_估计_WIND"
    wind_code = "S0112310"

###########################################################################################################################
""" 库存消费比 """  

class DiDuanMianHuaJiaCha(upstream_base, Computed):
    field_name = u"库存消费比"
    col_name = u"大豆库存消费比_美国_USDA"   
    def get_ts_whole_progress(self):
        relevant_col_list = [u"大豆期末库存_美国_USDA", u"大豆国内总需求_美国_USDA", u"大豆出口量_美国_USDA"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"大豆期末库存_美国_USDA"] / (tmp_total[u"大豆国内总需求_美国_USDA"] + tmp_total[u"大豆出口量_美国_USDA"])
        return tmp_total  

class DaDouKuCunXiaoFeiBi_QuanQiu_USDA(upstream_base, Computed):
    field_name = u"库存消费比"
    col_name = u"大豆库存消费比_全球_USDA"   
    def get_ts_whole_progress(self):
        relevant_col_list = [u"大豆期末库存_全球_USDA", u"大豆国内总需求_全球_USDA"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"大豆期末库存_全球_USDA"] / tmp_total[u"大豆国内总需求_全球_USDA"]
        return tmp_total  

class DaDouKuCunXiaoFeiBi_MeiGuo_YuCe_WIND(upstream_base, Computed):
    field_name = u"库存消费比"
    col_name = u"大豆库存消费比_美国_预测_WIND"   
    def get_ts_whole_progress(self):
        relevant_col_list = [u"大豆期末库存_美国_预测_WIND", u"大豆国内总需求_美国_预测_WIND", u"大豆出口量_美国_预测_WIND"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"大豆期末库存_美国_预测_WIND"] / (tmp_total[u"大豆国内总需求_美国_预测_WIND"] + tmp_total[u"大豆出口量_美国_预测_WIND"])
        return tmp_total  

class DaDouKuCunXiaoFeiBi_QuanQiu_YuCe_WIND(upstream_base, Computed):
    field_name = u"库存消费比"
    col_name = u"大豆库存消费比_全球_预测_WIND"   
    def get_ts_whole_progress(self):
        relevant_col_list = [u"大豆期末库存_全球_预测_WIND", u"大豆国内总需求_全球_预测_WIND"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"大豆期末库存_全球_预测_WIND"] / tmp_total[u"大豆国内总需求_全球_预测_WIND"]
        return tmp_total 

class DaDouKuCunXiaoFeiBi_MeiGuo_GuJi_WIND(upstream_base, Computed):
    field_name = u"库存消费比"
    col_name = u"大豆库存消费比_美国_估计_WIND"   
    def get_ts_whole_progress(self):
        relevant_col_list = [u"大豆期末库存_美国_估计_WIND", u"大豆国内总需求_美国_估计_WIND", u"大豆出口量_美国_估计_WIND"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"大豆期末库存_美国_估计_WIND"] / (tmp_total[u"大豆国内总需求_美国_估计_WIND"] + tmp_total[u"大豆出口量_美国_估计_WIND"])
        return tmp_total  

class DaDouKuCunXiaoFeiBi_QuanQiu_GuJi_WIND(upstream_base, Computed):
    field_name = u"库存消费比"
    col_name = u"大豆库存消费比_全球_估计_WIND"   
    def get_ts_whole_progress(self):
        relevant_col_list = [u"大豆期末库存_全球_估计_WIND", u"大豆国内总需求_全球_估计_WIND"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"大豆期末库存_全球_估计_WIND"] / tmp_total[u"大豆国内总需求_全球_估计_WIND"]
        return tmp_total    

###########################################################################################################################
""" 面积 """  

class DaDouShouHuoMianJi_MeiGuo_USDA(upstream_base, Manual):
    field_name = u"面积"
    col_name = u"大豆收获面积_美国_USDA"

class DaDouShouHuoMianJi_BaXi_USDA(upstream_base, Manual):
    field_name = u"面积"
    col_name = u"大豆收获面积_巴西_USDA"

class DaDouShouHuoMianJi_AGenTing_USDA(upstream_base, Manual):
    field_name = u"面积"
    col_name = u"大豆收获面积_阿根廷_USDA"

class DaDouShouHuoMianJi_ZhongGuo_USDA(upstream_base, Manual):
    field_name = u"面积"
    col_name = u"大豆收获面积_中国_USDA"

class DaDouShouHuoMianJi_QuanQiu_USDA(upstream_base, Manual):
    field_name = u"面积"
    col_name = u"大豆收获面积_全球_USDA"

class DaDouBoZhongMianJi_MeiGuo_YuCeNianDu_WIND(upstream_base, WindData):
    field_name = u"面积"
    col_name = u"大豆播种面积_美国_预测年度_WIND"
    wind_code = "S0118526"

class DaDouBoZhongMianJi_BaXi_YuCeNianDu_WIND(upstream_base, WindData):
    field_name = u"面积"
    col_name = u"大豆播种面积_巴西_预测年度_WIND"
    wind_code = "S0118527"
    
class DaDouBoZhongMianJi_AGenTing_YuCeNianDu_WIND(upstream_base, WindData):
    field_name = u"面积"
    col_name = u"大豆播种面积_阿根廷_预测年度_WIND"
    wind_code = "S0118528"

class DaDouBoZhongMianJi_ZhongGuo_YuCeNianDu_WIND(upstream_base, WindData):
    field_name = u"面积"
    col_name = u"大豆播种面积_中国_预测年度_WIND"
    wind_code = "S0118530"


###########################################################################################################################
""" 升贴水 """  

class JinKouDaDouFOBShengTieShui_MeiWan_1Yue(upstream_base, Manual):
    field_name = u"升贴水"
    col_name = u"进口大豆FOB升贴水_美湾_1月"

class JinKouDaDouFOBShengTieShui_MeiWan_2Yue(upstream_base, Manual):
    field_name = u"升贴水"
    col_name = u"进口大豆FOB升贴水_美湾_2月"

class JinKouDaDouFOBShengTieShui_MeiWan_3Yue(upstream_base, Manual):
    field_name = u"升贴水"
    col_name = u"进口大豆FOB升贴水_美湾_3月"

class JinKouDaDouFOBShengTieShui_MeiWan_4Yue(upstream_base, Manual):
    field_name = u"升贴水"
    col_name = u"进口大豆FOB升贴水_美湾_4月"

class JinKouDaDouFOBShengTieShui_MeiWan_5Yue(upstream_base, Manual):
    field_name = u"升贴水"
    col_name = u"进口大豆FOB升贴水_美湾_5月"

class JinKouDaDouFOBShengTieShui_MeiWan_6Yue(upstream_base, Manual):
    field_name = u"升贴水"
    col_name = u"进口大豆FOB升贴水_美湾_6月"

class JinKouDaDouFOBShengTieShui_MeiWan_7Yue(upstream_base, Manual):
    field_name = u"升贴水"
    col_name = u"进口大豆FOB升贴水_美湾_7月"

class JinKouDaDouFOBShengTieShui_MeiWan_8Yue(upstream_base, Manual):
    field_name = u"升贴水"
    col_name = u"进口大豆FOB升贴水_美湾_8月"

class JinKouDaDouFOBShengTieShui_MeiWan_9Yue(upstream_base, Manual):
    field_name = u"升贴水"
    col_name = u"进口大豆FOB升贴水_美湾_9月"

class JinKouDaDouFOBShengTieShui_MeiWan_10Yue(upstream_base, Manual):
    field_name = u"升贴水"
    col_name = u"进口大豆FOB升贴水_美湾_10月"

class JinKouDaDouFOBShengTieShui_MeiWan_11Yue(upstream_base, Manual):
    field_name = u"升贴水"
    col_name = u"进口大豆FOB升贴水_美湾_11月"

class JinKouDaDouFOBShengTieShui_MeiWan_12Yue(upstream_base, Manual):
    field_name = u"升贴水"
    col_name = u"进口大豆FOB升贴水_美湾_12月"

class JinKouDaDouFOBShengTieShui_MeiXi_1Yue(upstream_base, Manual):
    field_name = u"升贴水"
    col_name = u"进口大豆FOB升贴水_美西_1月"

class JinKouDaDouFOBShengTieShui_MeiXi_2Yue(upstream_base, Manual):
    field_name = u"升贴水"
    col_name = u"进口大豆FOB升贴水_美西_2月"

class JinKouDaDouFOBShengTieShui_MeiXi_3Yue(upstream_base, Manual):
    field_name = u"升贴水"
    col_name = u"进口大豆FOB升贴水_美西_3月"

class JinKouDaDouFOBShengTieShui_MeiXi_4Yue(upstream_base, Manual):
    field_name = u"升贴水"
    col_name = u"进口大豆FOB升贴水_美西_4月"

class JinKouDaDouFOBShengTieShui_MeiXi_5Yue(upstream_base, Manual):
    field_name = u"升贴水"
    col_name = u"进口大豆FOB升贴水_美西_5月"

class JinKouDaDouFOBShengTieShui_MeiXi_6Yue(upstream_base, Manual):
    field_name = u"升贴水"
    col_name = u"进口大豆FOB升贴水_美西_6月"

class JinKouDaDouFOBShengTieShui_MeiXi_7Yue(upstream_base, Manual):
    field_name = u"升贴水"
    col_name = u"进口大豆FOB升贴水_美西_7月"

class JinKouDaDouFOBShengTieShui_MeiXi_8Yue(upstream_base, Manual):
    field_name = u"升贴水"
    col_name = u"进口大豆FOB升贴水_美西_8月"

class JinKouDaDouFOBShengTieShui_MeiXi_9Yue(upstream_base, Manual):
    field_name = u"升贴水"
    col_name = u"进口大豆FOB升贴水_美西_9月"

class JinKouDaDouFOBShengTieShui_MeiXi_10Yue(upstream_base, Manual):
    field_name = u"升贴水"
    col_name = u"进口大豆FOB升贴水_美西_10月"

class JinKouDaDouFOBShengTieShui_MeiXi_11Yue(upstream_base, Manual):
    field_name = u"升贴水"
    col_name = u"进口大豆FOB升贴水_美西_11月"

class JinKouDaDouFOBShengTieShui_MeiXi_12Yue(upstream_base, Manual):
    field_name = u"升贴水"
    col_name = u"进口大豆FOB升贴水_美西_12月"
    
class JinKouDaDouFOBShengTieShui_BaXi_1Yue(upstream_base, Manual):
    field_name = u"升贴水"
    col_name = u"进口大豆FOB升贴水_巴西_1月"

class JinKouDaDouFOBShengTieShui_BaXi_2Yue(upstream_base, Manual):
    field_name = u"升贴水"
    col_name = u"进口大豆FOB升贴水_巴西_2月"

class JinKouDaDouFOBShengTieShui_BaXi_3Yue(upstream_base, Manual):
    field_name = u"升贴水"
    col_name = u"进口大豆FOB升贴水_巴西_3月"

class JinKouDaDouFOBShengTieShui_BaXi_4Yue(upstream_base, Manual):
    field_name = u"升贴水"
    col_name = u"进口大豆FOB升贴水_巴西_4月"

class JinKouDaDouFOBShengTieShui_BaXi_5Yue(upstream_base, Manual):
    field_name = u"升贴水"
    col_name = u"进口大豆FOB升贴水_巴西_5月"

class JinKouDaDouFOBShengTieShui_BaXi_6Yue(upstream_base, Manual):
    field_name = u"升贴水"
    col_name = u"进口大豆FOB升贴水_巴西_6月"

class JinKouDaDouFOBShengTieShui_BaXi_7Yue(upstream_base, Manual):
    field_name = u"升贴水"
    col_name = u"进口大豆FOB升贴水_巴西_7月"

class JinKouDaDouFOBShengTieShui_BaXi_8Yue(upstream_base, Manual):
    field_name = u"升贴水"
    col_name = u"进口大豆FOB升贴水_巴西_8月"

class JinKouDaDouFOBShengTieShui_BaXi_9Yue(upstream_base, Manual):
    field_name = u"升贴水"
    col_name = u"进口大豆FOB升贴水_巴西_9月"

class JinKouDaDouFOBShengTieShui_BaXi_10Yue(upstream_base, Manual):
    field_name = u"升贴水"
    col_name = u"进口大豆FOB升贴水_巴西_10月"

class JinKouDaDouFOBShengTieShui_BaXi_11Yue(upstream_base, Manual):
    field_name = u"升贴水"
    col_name = u"进口大豆FOB升贴水_巴西_11月"

class JinKouDaDouFOBShengTieShui_BaXi_12Yue(upstream_base, Manual):
    field_name = u"升贴水"
    col_name = u"进口大豆FOB升贴水_巴西_12月"

class JinKouDaDouFOBShengTieShui_AGenTing_1Yue(upstream_base, Manual):
    field_name = u"升贴水"
    col_name = u"进口大豆FOB升贴水_阿根廷_1月"

class JinKouDaDouFOBShengTieShui_AGenTing_2Yue(upstream_base, Manual):
    field_name = u"升贴水"
    col_name = u"进口大豆FOB升贴水_阿根廷_2月"

class JinKouDaDouFOBShengTieShui_AGenTing_3Yue(upstream_base, Manual):
    field_name = u"升贴水"
    col_name = u"进口大豆FOB升贴水_阿根廷_3月"

class JinKouDaDouFOBShengTieShui_AGenTing_4Yue(upstream_base, Manual):
    field_name = u"升贴水"
    col_name = u"进口大豆FOB升贴水_阿根廷_4月"

class JinKouDaDouFOBShengTieShui_AGenTing_5Yue(upstream_base, Manual):
    field_name = u"升贴水"
    col_name = u"进口大豆FOB升贴水_阿根廷_5月"

class JinKouDaDouFOBShengTieShui_AGenTing_6Yue(upstream_base, Manual):
    field_name = u"升贴水"
    col_name = u"进口大豆FOB升贴水_阿根廷_6月"

class JinKouDaDouFOBShengTieShui_AGenTing_7Yue(upstream_base, Manual):
    field_name = u"升贴水"
    col_name = u"进口大豆FOB升贴水_阿根廷_7月"

class JinKouDaDouFOBShengTieShui_AGenTing_8Yue(upstream_base, Manual):
    field_name = u"升贴水"
    col_name = u"进口大豆FOB升贴水_阿根廷_8月"

class JinKouDaDouFOBShengTieShui_AGenTing_9Yue(upstream_base, Manual):
    field_name = u"升贴水"
    col_name = u"进口大豆FOB升贴水_阿根廷_9月"

class JinKouDaDouFOBShengTieShui_AGenTing_10Yue(upstream_base, Manual):
    field_name = u"升贴水"
    col_name = u"进口大豆FOB升贴水_阿根廷_10月"

class JinKouDaDouFOBShengTieShui_AGenTing_11Yue(upstream_base, Manual):
    field_name = u"升贴水"
    col_name = u"进口大豆FOB升贴水_阿根廷_11月"

class JinKouDaDouFOBShengTieShui_AGenTing_12Yue(upstream_base, Manual):
    field_name = u"升贴水"
    col_name = u"进口大豆FOB升贴水_阿根廷_12月"



class JinKouDaDouCNFShengTieShui_MeiWan_1Yue(upstream_base, Manual):
    field_name = u"升贴水"
    col_name = u"进口大豆CNF升贴水_美湾_1月"

class JinKouDaDouCNFShengTieShui_MeiWan_2Yue(upstream_base, Manual):
    field_name = u"升贴水"
    col_name = u"进口大豆CNF升贴水_美湾_2月"

class JinKouDaDouCNFShengTieShui_MeiWan_3Yue(upstream_base, Manual):
    field_name = u"升贴水"
    col_name = u"进口大豆CNF升贴水_美湾_3月"

class JinKouDaDouCNFShengTieShui_MeiWan_4Yue(upstream_base, Manual):
    field_name = u"升贴水"
    col_name = u"进口大豆CNF升贴水_美湾_4月"

class JinKouDaDouCNFShengTieShui_MeiWan_5Yue(upstream_base, Manual):
    field_name = u"升贴水"
    col_name = u"进口大豆CNF升贴水_美湾_5月"

class JinKouDaDouCNFShengTieShui_MeiWan_6Yue(upstream_base, Manual):
    field_name = u"升贴水"
    col_name = u"进口大豆CNF升贴水_美湾_6月"

class JinKouDaDouCNFShengTieShui_MeiWan_7Yue(upstream_base, Manual):
    field_name = u"升贴水"
    col_name = u"进口大豆CNF升贴水_美湾_7月"

class JinKouDaDouCNFShengTieShui_MeiWan_8Yue(upstream_base, Manual):
    field_name = u"升贴水"
    col_name = u"进口大豆CNF升贴水_美湾_8月"

class JinKouDaDouCNFShengTieShui_MeiWan_9Yue(upstream_base, Manual):
    field_name = u"升贴水"
    col_name = u"进口大豆CNF升贴水_美湾_9月"

class JinKouDaDouCNFShengTieShui_MeiWan_10Yue(upstream_base, Manual):
    field_name = u"升贴水"
    col_name = u"进口大豆CNF升贴水_美湾_10月"

class JinKouDaDouCNFShengTieShui_MeiWan_11Yue(upstream_base, Manual):
    field_name = u"升贴水"
    col_name = u"进口大豆CNF升贴水_美湾_11月"

class JinKouDaDouCNFShengTieShui_MeiWan_12Yue(upstream_base, Manual):
    field_name = u"升贴水"
    col_name = u"进口大豆CNF升贴水_美湾_12月"

class JinKouDaDouCNFShengTieShui_MeiXi_1Yue(upstream_base, Manual):
    field_name = u"升贴水"
    col_name = u"进口大豆CNF升贴水_美西_1月"

class JinKouDaDouCNFShengTieShui_MeiXi_2Yue(upstream_base, Manual):
    field_name = u"升贴水"
    col_name = u"进口大豆CNF升贴水_美西_2月"

class JinKouDaDouCNFShengTieShui_MeiXi_3Yue(upstream_base, Manual):
    field_name = u"升贴水"
    col_name = u"进口大豆CNF升贴水_美西_3月"

class JinKouDaDouCNFShengTieShui_MeiXi_4Yue(upstream_base, Manual):
    field_name = u"升贴水"
    col_name = u"进口大豆CNF升贴水_美西_4月"

class JinKouDaDouCNFShengTieShui_MeiXi_5Yue(upstream_base, Manual):
    field_name = u"升贴水"
    col_name = u"进口大豆CNF升贴水_美西_5月"

class JinKouDaDouCNFShengTieShui_MeiXi_6Yue(upstream_base, Manual):
    field_name = u"升贴水"
    col_name = u"进口大豆CNF升贴水_美西_6月"

class JinKouDaDouCNFShengTieShui_MeiXi_7Yue(upstream_base, Manual):
    field_name = u"升贴水"
    col_name = u"进口大豆CNF升贴水_美西_7月"

class JinKouDaDouCNFShengTieShui_MeiXi_8Yue(upstream_base, Manual):
    field_name = u"升贴水"
    col_name = u"进口大豆CNF升贴水_美西_8月"

class JinKouDaDouCNFShengTieShui_MeiXi_9Yue(upstream_base, Manual):
    field_name = u"升贴水"
    col_name = u"进口大豆CNF升贴水_美西_9月"

class JinKouDaDouCNFShengTieShui_MeiXi_10Yue(upstream_base, Manual):
    field_name = u"升贴水"
    col_name = u"进口大豆CNF升贴水_美西_10月"

class JinKouDaDouCNFShengTieShui_MeiXi_11Yue(upstream_base, Manual):
    field_name = u"升贴水"
    col_name = u"进口大豆CNF升贴水_美西_11月"

class JinKouDaDouCNFShengTieShui_MeiXi_12Yue(upstream_base, Manual):
    field_name = u"升贴水"
    col_name = u"进口大豆CNF升贴水_美西_12月"
    
class JinKouDaDouCNFShengTieShui_BaXi_1Yue(upstream_base, Manual):
    field_name = u"升贴水"
    col_name = u"进口大豆CNF升贴水_巴西_1月"

class JinKouDaDouCNFShengTieShui_BaXi_2Yue(upstream_base, Manual):
    field_name = u"升贴水"
    col_name = u"进口大豆CNF升贴水_巴西_2月"

class JinKouDaDouCNFShengTieShui_BaXi_3Yue(upstream_base, Manual):
    field_name = u"升贴水"
    col_name = u"进口大豆CNF升贴水_巴西_3月"

class JinKouDaDouCNFShengTieShui_BaXi_4Yue(upstream_base, Manual):
    field_name = u"升贴水"
    col_name = u"进口大豆CNF升贴水_巴西_4月"

class JinKouDaDouCNFShengTieShui_BaXi_5Yue(upstream_base, Manual):
    field_name = u"升贴水"
    col_name = u"进口大豆CNF升贴水_巴西_5月"

class JinKouDaDouCNFShengTieShui_BaXi_6Yue(upstream_base, Manual):
    field_name = u"升贴水"
    col_name = u"进口大豆CNF升贴水_巴西_6月"

class JinKouDaDouCNFShengTieShui_BaXi_7Yue(upstream_base, Manual):
    field_name = u"升贴水"
    col_name = u"进口大豆CNF升贴水_巴西_7月"

class JinKouDaDouCNFShengTieShui_BaXi_8Yue(upstream_base, Manual):
    field_name = u"升贴水"
    col_name = u"进口大豆CNF升贴水_巴西_8月"

class JinKouDaDouCNFShengTieShui_BaXi_9Yue(upstream_base, Manual):
    field_name = u"升贴水"
    col_name = u"进口大豆CNF升贴水_巴西_9月"

class JinKouDaDouCNFShengTieShui_BaXi_10Yue(upstream_base, Manual):
    field_name = u"升贴水"
    col_name = u"进口大豆CNF升贴水_巴西_10月"

class JinKouDaDouCNFShengTieShui_BaXi_11Yue(upstream_base, Manual):
    field_name = u"升贴水"
    col_name = u"进口大豆CNF升贴水_巴西_11月"

class JinKouDaDouCNFShengTieShui_BaXi_12Yue(upstream_base, Manual):
    field_name = u"升贴水"
    col_name = u"进口大豆CNF升贴水_巴西_12月"

class JinKouDaDouCNFShengTieShui_AGenTing_1Yue(upstream_base, Manual):
    field_name = u"升贴水"
    col_name = u"进口大豆CNF升贴水_阿根廷_1月"

class JinKouDaDouCNFShengTieShui_AGenTing_2Yue(upstream_base, Manual):
    field_name = u"升贴水"
    col_name = u"进口大豆CNF升贴水_阿根廷_2月"

class JinKouDaDouCNFShengTieShui_AGenTing_3Yue(upstream_base, Manual):
    field_name = u"升贴水"
    col_name = u"进口大豆CNF升贴水_阿根廷_3月"

class JinKouDaDouCNFShengTieShui_AGenTing_4Yue(upstream_base, Manual):
    field_name = u"升贴水"
    col_name = u"进口大豆CNF升贴水_阿根廷_4月"

class JinKouDaDouCNFShengTieShui_AGenTing_5Yue(upstream_base, Manual):
    field_name = u"升贴水"
    col_name = u"进口大豆CNF升贴水_阿根廷_5月"

class JinKouDaDouCNFShengTieShui_AGenTing_6Yue(upstream_base, Manual):
    field_name = u"升贴水"
    col_name = u"进口大豆CNF升贴水_阿根廷_6月"

class JinKouDaDouCNFShengTieShui_AGenTing_7Yue(upstream_base, Manual):
    field_name = u"升贴水"
    col_name = u"进口大豆CNF升贴水_阿根廷_7月"

class JinKouDaDouCNFShengTieShui_AGenTing_8Yue(upstream_base, Manual):
    field_name = u"升贴水"
    col_name = u"进口大豆CNF升贴水_阿根廷_8月"

class JinKouDaDouCNFShengTieShui_AGenTing_9Yue(upstream_base, Manual):
    field_name = u"升贴水"
    col_name = u"进口大豆CNF升贴水_阿根廷_9月"

class JinKouDaDouCNFShengTieShui_AGenTing_10Yue(upstream_base, Manual):
    field_name = u"升贴水"
    col_name = u"进口大豆CNF升贴水_阿根廷_10月"

class JinKouDaDouCNFShengTieShui_AGenTing_11Yue(upstream_base, Manual):
    field_name = u"升贴水"
    col_name = u"进口大豆CNF升贴水_阿根廷_11月"

class JinKouDaDouCNFShengTieShui_AGenTing_12Yue(upstream_base, Manual):
    field_name = u"升贴水"
    col_name = u"进口大豆CNF升贴水_阿根廷_12月"

###########################################################################################################################
""" 需求量 """  

class DaDouShiYongXuQiu_MeiGuo_USDA(upstream_base, Manual):
    field_name = u"需求量"
    col_name = u"大豆食用需求_美国_USDA"

class DaDouShiYongXuQiu_BaXi_USDA(upstream_base, Manual):
    field_name = u"需求量"
    col_name = u"大豆食用需求_巴西_USDA"

class DaDouShiYongXuQiu_AGenTing_USDA(upstream_base, Manual):
    field_name = u"需求量"
    col_name = u"大豆食用需求_阿根廷_USDA"

class DaDouShiYongXuQiu_ZhongGuo_USDA(upstream_base, Manual):
    field_name = u"需求量"
    col_name = u"大豆食用需求_中国_USDA"

class DaDouShiYongXuQiu_QuanQiu_USDA(upstream_base, Manual):
    field_name = u"需求量"
    col_name = u"大豆食用需求_全球_USDA"

class DaDouSiYongXuQiu_MeiGuo_USDA(upstream_base, Manual):
    field_name = u"需求量"
    col_name = u"大豆饲用需求_美国_USDA"

class DaDouSiYongXuQiu_BaXi_USDA(upstream_base, Manual):
    field_name = u"需求量"
    col_name = u"大豆饲用需求_巴西_USDA"

class DaDouSiYongXuQiu_AGenTing_USDA(upstream_base, Manual):
    field_name = u"需求量"
    col_name = u"大豆饲用需求_阿根廷_USDA"

class DaDouSiYongXuQiu_ZhongGuo_USDA(upstream_base, Manual):
    field_name = u"需求量"
    col_name = u"大豆饲用需求_中国_USDA"

class DaDouSiYongXuQiu_QuanQiu_USDA(upstream_base, Manual):
    field_name = u"需求量"
    col_name = u"大豆饲用需求_全球_USDA"

class DaDouGuoNeiZongXuQiu_MeiGuo_USDA(upstream_base, Manual):
    field_name = u"需求量"
    col_name = u"大豆国内总需求_美国_USDA"

class DaDouGuoNeiZongXuQiu_BaXi_USDA(upstream_base, Manual):
    field_name = u"需求量"
    col_name = u"大豆国内总需求_巴西_USDA"

class DaDouGuoNeiZongXuQiu_AGenTing_USDA(upstream_base, Manual):
    field_name = u"需求量"
    col_name = u"大豆国内总需求_阿根廷_USDA"

class DaDouGuoNeiZongXuQiu_ZhongGuo_USDA(upstream_base, Manual):
    field_name = u"需求量"
    col_name = u"大豆国内总需求_中国_USDA"

class DaDouGuoNeiZongXuQiu_QuanQiu_USDA(upstream_base, Manual):
    field_name = u"需求量"
    col_name = u"大豆国内总需求_全球_USDA"

class DaDouGuoNeiZongXuQiu_MeiGuo_YuCe_WIND(upstream_base, WindData):
    field_name = u"需求量"
    col_name = u"大豆国内总需求_美国_预测_WIND"
    wind_code= "S0113230"

class DaDouGuoNeiZongXuQiu_BaXi_YuCe_WIND(upstream_base, WindData):
    field_name = u"需求量"
    col_name = u"大豆国内总需求_巴西_预测_WIND"
    wind_code= "S0113244"

class DaDouGuoNeiZongXuQiu_AGenTing_YuCe_WIND(upstream_base, WindData):
    field_name = u"需求量"
    col_name = u"大豆国内总需求_阿根廷_预测_WIND"
    wind_code= "S0113251"

class DaDouGuoNeiZongXuQiu_ZhongGuo_YuCe_WIND(upstream_base, WindData):
    field_name = u"需求量"
    col_name = u"大豆国内总需求_中国_预测_WIND"
    wind_code= "S0113237"

class DaDouGuoNeiZongXuQiu_QuanQiu_YuCe_WIND(upstream_base, WindData):
    field_name = u"需求量"
    col_name = u"大豆国内总需求_全球_预测_WIND"
    wind_code= "S0112361"

class DaDouGuoNeiZongXuQiu_MeiGuo_GuJi_WIND(upstream_base, WindData):
    field_name = u"需求量"
    col_name = u"大豆国内总需求_美国_估计_WIND"
    wind_code= "S0112900"

class DaDouGuoNeiZongXuQiu_BaXi_GuJi_WIND(upstream_base, WindData):
    field_name = u"需求量"
    col_name = u"大豆国内总需求_巴西_估计_WIND"
    wind_code= "S0112914"

class DaDouGuoNeiZongXuQiu_AGenTing_GuJi_WIND(upstream_base, WindData):
    field_name = u"需求量"
    col_name = u"大豆国内总需求_阿根廷_估计_WIND"
    wind_code= "S0112921"

class DaDouGuoNeiZongXuQiu_ZhongGuo_GuJi_WIND(upstream_base, WindData):
    field_name = u"需求量"
    col_name = u"大豆国内总需求_中国_估计_WIND"
    wind_code= "S0112907"

class DaDouGuoNeiZongXuQiu_QuanQiu_GuJi_WIND(upstream_base, WindData):
    field_name = u"需求量"
    col_name = u"大豆国内总需求_全球_估计_WIND"
    wind_code= "S0112308"

###########################################################################################################################
""" 压榨利润 """ 

class JinKouDaDouYaZhaLiRun_MeiWan_1Yue(upstream_base, Computed):
    field_name = u"压榨利润"
    col_name = u"进口大豆压榨利润_美湾_1月"

class JinKouDaDouYaZhaLiRun_MeiWan_2Yue(upstream_base, Computed):
    field_name = u"压榨利润"
    col_name = u"进口大豆压榨利润_美湾_2月"

class JinKouDaDouYaZhaLiRun_MeiWan_3Yue(upstream_base, Computed):
    field_name = u"压榨利润"
    col_name = u"进口大豆压榨利润_美湾_3月"

class JinKouDaDouYaZhaLiRun_MeiWan_4Yue(upstream_base, Computed):
    field_name = u"压榨利润"
    col_name = u"进口大豆压榨利润_美湾_4月"

class JinKouDaDouYaZhaLiRun_MeiWan_5Yue(upstream_base, Computed):
    field_name = u"压榨利润"
    col_name = u"进口大豆压榨利润_美湾_5月"

class JinKouDaDouYaZhaLiRun_MeiWan_6Yue(upstream_base, Computed):
    field_name = u"压榨利润"
    col_name = u"进口大豆压榨利润_美湾_6月"

class JinKouDaDouYaZhaLiRun_MeiWan_7Yue(upstream_base, Computed):
    field_name = u"压榨利润"
    col_name = u"进口大豆压榨利润_美湾_7月"

class JinKouDaDouYaZhaLiRun_MeiWan_8Yue(upstream_base, Computed):
    field_name = u"压榨利润"
    col_name = u"进口大豆压榨利润_美湾_8月"

class JinKouDaDouYaZhaLiRun_MeiWan_9Yue(upstream_base, Computed):
    field_name = u"压榨利润"
    col_name = u"进口大豆压榨利润_美湾_9月"

class JinKouDaDouYaZhaLiRun_MeiWan_10Yue(upstream_base, Computed):
    field_name = u"压榨利润"
    col_name = u"进口大豆压榨利润_美湾_10月"

class JinKouDaDouYaZhaLiRun_MeiWan_11Yue(upstream_base, Computed):
    field_name = u"压榨利润"
    col_name = u"进口大豆压榨利润_美湾_11月"

class JinKouDaDouYaZhaLiRun_MeiWan_12Yue(upstream_base, Computed):
    field_name = u"压榨利润"
    col_name = u"进口大豆压榨利润_美湾_12月"

class JinKouDaDouYaZhaLiRun_MeiXi_1Yue(upstream_base, Computed):
    field_name = u"压榨利润"
    col_name = u"进口大豆压榨利润_美西_1月"

class JinKouDaDouYaZhaLiRun_MeiXi_2Yue(upstream_base, Computed):
    field_name = u"压榨利润"
    col_name = u"进口大豆压榨利润_美西_2月"

class JinKouDaDouYaZhaLiRun_MeiXi_3Yue(upstream_base, Computed):
    field_name = u"压榨利润"
    col_name = u"进口大豆压榨利润_美西_3月"

class JinKouDaDouYaZhaLiRun_MeiXi_4Yue(upstream_base, Computed):
    field_name = u"压榨利润"
    col_name = u"进口大豆压榨利润_美西_4月"

class JinKouDaDouYaZhaLiRun_MeiXi_5Yue(upstream_base, Computed):
    field_name = u"压榨利润"
    col_name = u"进口大豆压榨利润_美西_5月"

class JinKouDaDouYaZhaLiRun_MeiXi_6Yue(upstream_base, Computed):
    field_name = u"压榨利润"
    col_name = u"进口大豆压榨利润_美西_6月"

class JinKouDaDouYaZhaLiRun_MeiXi_7Yue(upstream_base, Computed):
    field_name = u"压榨利润"
    col_name = u"进口大豆压榨利润_美西_7月"

class JinKouDaDouYaZhaLiRun_MeiXi_8Yue(upstream_base, Computed):
    field_name = u"压榨利润"
    col_name = u"进口大豆压榨利润_美西_8月"

class JinKouDaDouYaZhaLiRun_MeiXi_9Yue(upstream_base, Computed):
    field_name = u"压榨利润"
    col_name = u"进口大豆压榨利润_美西_9月"

class JinKouDaDouYaZhaLiRun_MeiXi_10Yue(upstream_base, Computed):
    field_name = u"压榨利润"
    col_name = u"进口大豆压榨利润_美西_10月"

class JinKouDaDouYaZhaLiRun_MeiXi_11Yue(upstream_base, Computed):
    field_name = u"压榨利润"
    col_name = u"进口大豆压榨利润_美西_11月"

class JinKouDaDouYaZhaLiRun_MeiXi_12Yue(upstream_base, Computed):
    field_name = u"压榨利润"
    col_name = u"进口大豆压榨利润_美西_12月"
    
class JinKouDaDouYaZhaLiRun_BaXi_1Yue(upstream_base, Computed):
    field_name = u"压榨利润"
    col_name = u"进口大豆压榨利润_巴西_1月"

class JinKouDaDouYaZhaLiRun_BaXi_2Yue(upstream_base, Computed):
    field_name = u"压榨利润"
    col_name = u"进口大豆压榨利润_巴西_2月"

class JinKouDaDouYaZhaLiRun_BaXi_3Yue(upstream_base, Computed):
    field_name = u"压榨利润"
    col_name = u"进口大豆压榨利润_巴西_3月"

class JinKouDaDouYaZhaLiRun_BaXi_4Yue(upstream_base, Computed):
    field_name = u"压榨利润"
    col_name = u"进口大豆压榨利润_巴西_4月"

class JinKouDaDouYaZhaLiRun_BaXi_5Yue(upstream_base, Computed):
    field_name = u"压榨利润"
    col_name = u"进口大豆压榨利润_巴西_5月"

class JinKouDaDouYaZhaLiRun_BaXi_6Yue(upstream_base, Computed):
    field_name = u"压榨利润"
    col_name = u"进口大豆压榨利润_巴西_6月"

class JinKouDaDouYaZhaLiRun_BaXi_7Yue(upstream_base, Computed):
    field_name = u"压榨利润"
    col_name = u"进口大豆压榨利润_巴西_7月"

class JinKouDaDouYaZhaLiRun_BaXi_8Yue(upstream_base, Computed):
    field_name = u"压榨利润"
    col_name = u"进口大豆压榨利润_巴西_8月"

class JinKouDaDouYaZhaLiRun_BaXi_9Yue(upstream_base, Computed):
    field_name = u"压榨利润"
    col_name = u"进口大豆压榨利润_巴西_9月"

class JinKouDaDouYaZhaLiRun_BaXi_10Yue(upstream_base, Computed):
    field_name = u"压榨利润"
    col_name = u"进口大豆压榨利润_巴西_10月"

class JinKouDaDouYaZhaLiRun_BaXi_11Yue(upstream_base, Computed):
    field_name = u"压榨利润"
    col_name = u"进口大豆压榨利润_巴西_11月"

class JinKouDaDouYaZhaLiRun_BaXi_12Yue(upstream_base, Computed):
    field_name = u"压榨利润"
    col_name = u"进口大豆压榨利润_巴西_12月"

class JinKouDaDouYaZhaLiRun_AGenTing_1Yue(upstream_base, Computed):
    field_name = u"压榨利润"
    col_name = u"进口大豆压榨利润_阿根廷_1月"

class JinKouDaDouYaZhaLiRun_AGenTing_2Yue(upstream_base, Computed):
    field_name = u"压榨利润"
    col_name = u"进口大豆压榨利润_阿根廷_2月"

class JinKouDaDouYaZhaLiRun_AGenTing_3Yue(upstream_base, Computed):
    field_name = u"压榨利润"
    col_name = u"进口大豆压榨利润_阿根廷_3月"

class JinKouDaDouYaZhaLiRun_AGenTing_4Yue(upstream_base, Computed):
    field_name = u"压榨利润"
    col_name = u"进口大豆压榨利润_阿根廷_4月"

class JinKouDaDouYaZhaLiRun_AGenTing_5Yue(upstream_base, Computed):
    field_name = u"压榨利润"
    col_name = u"进口大豆压榨利润_阿根廷_5月"

class JinKouDaDouYaZhaLiRun_AGenTing_6Yue(upstream_base, Computed):
    field_name = u"压榨利润"
    col_name = u"进口大豆压榨利润_阿根廷_6月"

class JinKouDaDouYaZhaLiRun_AGenTing_7Yue(upstream_base, Computed):
    field_name = u"压榨利润"
    col_name = u"进口大豆压榨利润_阿根廷_7月"

class JinKouDaDouYaZhaLiRun_AGenTing_8Yue(upstream_base, Computed):
    field_name = u"压榨利润"
    col_name = u"进口大豆压榨利润_阿根廷_8月"

class JinKouDaDouYaZhaLiRun_AGenTing_9Yue(upstream_base, Computed):
    field_name = u"压榨利润"
    col_name = u"进口大豆压榨利润_阿根廷_9月"

class JinKouDaDouYaZhaLiRun_AGenTing_10Yue(upstream_base, Computed):
    field_name = u"压榨利润"
    col_name = u"进口大豆压榨利润_阿根廷_10月"

class JinKouDaDouYaZhaLiRun_AGenTing_11Yue(upstream_base, Computed):
    field_name = u"压榨利润"
    col_name = u"进口大豆压榨利润_阿根廷_11月"

class JinKouDaDouYaZhaLiRun_AGenTing_12Yue(upstream_base, Computed):
    field_name = u"压榨利润"
    col_name = u"进口大豆压榨利润_阿根廷_12月"

###########################################################################################################################
""" 压榨量 """ 

class DaDouYaZhaLiang_MeiGuo_USDA(upstream_base, Manual):
    field_name = u"压榨量"
    col_name = u"大豆压榨量_美国_USDA"

class DaDouYaZhaLiang_BaXi_USDA(upstream_base, Manual):
    field_name = u"压榨量"
    col_name = u"大豆压榨量_巴西_USDA"

class DaDouYaZhaLiang_AGenTing_USDA(upstream_base, Manual):
    field_name = u"压榨量"
    col_name = u"大豆压榨量_阿根廷_USDA"

class DaDouYaZhaLiang_ZhongGuo_USDA(upstream_base, Manual):
    field_name = u"压榨量"
    col_name = u"大豆压榨量_中国_USDA"

class DaDouYaZhaLiang_QuanQiu_USDA(upstream_base, Manual):
    field_name = u"压榨量"
    col_name = u"大豆压榨量_全球_USDA"

class DaDouYaZhaLiang(upstream_base, Manual):
    field_name = u"压榨量"
    col_name = u"大豆压榨量_周度"

###########################################################################################################################
""" 优良率 """ 

class MeiGuoDaDouYouLiangLv(upstream_base, Manual):
    field_name = u"优良率"
    col_name = u"美国大豆优良率"

###########################################################################################################################
""" 总供应 """ 

class DaDouZongGongYing_MeiGuo_USDA(upstream_base, Manual):
    field_name = u"总供应"
    col_name = u"大豆总供应_美国_USDA"

class DaDouZongGongYing_BaXi_USDA(upstream_base, Manual):
    field_name = u"总供应"
    col_name = u"大豆总供应_巴西_USDA"

class DaDouZongGongYing_AGenTing_USDA(upstream_base, Manual):
    field_name = u"总供应"
    col_name = u"大豆总供应_阿根廷_USDA"

class DaDouZongGongYing_ZhongGuo_USDA(upstream_base, Manual):
    field_name = u"总供应"
    col_name = u"大豆总供应_中国_USDA"

class DaDouZongGongYing_QuanQiu_USDA(upstream_base, Manual):
    field_name = u"总供应"
    col_name = u"大豆总供应_全球_USDA"


    
if __name__ == "__main__":
    df = MianHuaGongJianJinDu_YueDuLeiJi().get_ts()    
    
    
    
    
    
    
    
    
    
    
    
    
    
    