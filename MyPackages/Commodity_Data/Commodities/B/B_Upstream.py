# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 10:44:58 2018

@author: 李弘一萌
"""

import pandas as pd
from datetime import datetime
from MyFutureClass.CmtDataBase.Commodities.B.B_Base import B_Base
from MyFutureClass.CmtDataBase.Base.DataType_Base import Manual, Computed, WindData
from MyFutureClass.CmtDataBase.Base.Plot_Base import Plot_Base
from MyFutureClass.Data.QuoteData import QuoteData
from matplotlib.ticker import FuncFormatter

class upstream_base(B_Base, Plot_Base):
    table_english_name = "Upstream"
    table_chinese_name = u"上游"
#    original_db_filepath = data_path + u"LPP价格数据库.xlsx"
    
    def output(self):
        print("Upstream")
    
    def get_relevant_df(self, col_list):
        local_col_name_list = upstream_base.get_all_table_classname()
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
""" 出口量 """  

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
""" 进口成本 """  

class JinKouDaDouDaoGangWanShuiChengBen_MeiWan(upstream_base, Computed):
    field_name = u"进口成本"
    col_name = u"进口大豆到港完税成本_美湾"
    def get_ts_whole_progress(self):
#        relevant_col_list = [u"中国棉花328价格指数", u"涤短价格_1.4D直纺涤短"]
#        tmp_total = self.get_relevant_df(relevant_col_list)
#        tmp_total[self.col_name] = tmp_total[u"中国棉花328价格指数"] - tmp_total[u"涤短价格_1.4D直纺涤短"]
#        return tmp_total  
        pass

class JinKouDaDouDaoGangWanShuiChengBen_MeiXi(upstream_base, Computed):
    field_name = u"进口成本"
    col_name = u"进口大豆到港完税成本_美西"
    def get_ts_whole_progress(self):
#        relevant_col_list = [u"中国棉花328价格指数", u"涤短价格_1.4D直纺涤短"]
#        tmp_total = self.get_relevant_df(relevant_col_list)
#        tmp_total[self.col_name] = tmp_total[u"中国棉花328价格指数"] - tmp_total[u"涤短价格_1.4D直纺涤短"]
#        return tmp_total  
        pass

class JinKouDaDouDaoGangWanShuiChengBen_BaXi(upstream_base, Computed):
    field_name = u"进口成本"
    col_name = u"进口大豆到港完税成本_巴西"
    def get_ts_whole_progress(self):
#        relevant_col_list = [u"中国棉花328价格指数", u"涤短价格_1.4D直纺涤短"]
#        tmp_total = self.get_relevant_df(relevant_col_list)
#        tmp_total[self.col_name] = tmp_total[u"中国棉花328价格指数"] - tmp_total[u"涤短价格_1.4D直纺涤短"]
#        return tmp_total  
        pass

class JinKouDaDouDaoGangWanShuiChengBen_AGenTing(upstream_base, Computed):
    field_name = u"进口成本"
    col_name = u"进口大豆到港完税成本_阿根廷"
    def get_ts_whole_progress(self):
#        relevant_col_list = [u"中国棉花328价格指数", u"涤短价格_1.4D直纺涤短"]
#        tmp_total = self.get_relevant_df(relevant_col_list)
#        tmp_total[self.col_name] = tmp_total[u"中国棉花328价格指数"] - tmp_total[u"涤短价格_1.4D直纺涤短"]
#        return tmp_total  
        pass
    
###########################################################################################################################
""" 升贴水 """ 

class JinKouDaDouFOBShengTieShui_MeiWan(upstream_base, Manual):
    field_name = u"升贴水"
    col_name = u"进口大豆FOB升贴水_美湾"

class JinKouDaDouFOBShengTieShui_MeiXi(upstream_base, Manual):
    field_name = u"升贴水"
    col_name = u"进口大豆FOB升贴水_美西"

class JinKouDaDouFOBShengTieShui_BaXi(upstream_base, Manual):
    field_name = u"升贴水"
    col_name = u"进口大豆FOB升贴水_巴西"

class JinKouDaDouFOBShengTieShui_AGenTing(upstream_base, Manual):
    field_name = u"升贴水"
    col_name = u"进口大豆FOB升贴水_阿根廷"
    
class JinKouDaDouCNFShengTieShui_MeiWan(upstream_base, Manual):
    field_name = u"升贴水"
    col_name = u"进口大豆CNF升贴水_美湾"

class JinKouDaDouCNFShengTieShui_MeiXi(upstream_base, Manual):
    field_name = u"升贴水"
    col_name = u"进口大豆CNF升贴水_美西"

class JinKouDaDouCNFShengTieShui_BaXi(upstream_base, Manual):
    field_name = u"升贴水"
    col_name = u"进口大豆CNF升贴水_巴西"

class JinKouDaDouCNFShengTieShui_AGenTing(upstream_base, Manual):
    field_name = u"升贴水"
    col_name = u"进口大豆CNF升贴水_阿根廷"    

###########################################################################################################################
""" 优良率 """ 

class MeiGuoDaDouYouLiangLv(upstream_base, Manual):
    field_name = u"优良率"
    col_name = u"美国大豆优良率"

###########################################################################################################################
""" 运费 """  

class JinKouDaDouHaiYunFei_MeiWan(upstream_base, Manual):
    field_name = u"运费"
    col_name = u"进口大豆海运费_美湾"

class JinKouDaDouHaiYunFei_MeiXi(upstream_base, Manual):
    field_name = u"运费"
    col_name = u"进口大豆海运费_美西"

class JinKouDaDouHaiYunFei_BaXi(upstream_base, Manual):
    field_name = u"运费"
    col_name = u"进口大豆海运费_巴西"

class JinKouDaDouHaiYunFei_AGenTing(upstream_base, Manual):
    field_name = u"运费"
    col_name = u"进口大豆海运费_阿根廷"

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

class JinKouDaDouJinKouLiang(upstream_base, Manual):
    field_name = u"进口量"
    col_name = u"进口大豆进口量"

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
""" 期初库存 """  

class JinKouDaDouQiChuKuCun(upstream_base, Manual):
    field_name = u"期初库存"
    col_name = u"进口大豆期初库存"    
    
###########################################################################################################################
""" 期末库存 """  

class JinKouDaDouQiMoKuCun(upstream_base, Manual):
    field_name = u"期末库存"
    col_name = u"进口大豆期末库存"      

###########################################################################################################################
""" 食用及膨化用量 """  

class JinKouDaDouShiYongJiPengHuaYongLiang(upstream_base, Manual):
    field_name = u"食用及膨化用量"
    col_name = u"进口大豆食用及膨化用量"   
    
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

class JinKouDaDouYaZhaLiang(upstream_base, Manual):
    field_name = u"压榨量"
    col_name = u"进口大豆压榨量"
    
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
    
###########################################################################################################################
""" 总供应量 """ 

class JinKouDaDouZongGongYingLiang(upstream_base, Manual):
    field_name = u"总供应量"
    col_name = u"进口大豆总供应量"    
    
###########################################################################################################################
""" 总使用量 """ 

class JinKouDaDouZongShiYongLiang(upstream_base, Manual):
    field_name = u"总使用量"
    col_name = u"进口大豆总使用量"    
    
    
    
if __name__ == "__main__":
    df = MianHuaGongJianJinDu_YueDuLeiJi().get_ts()    
    
    
    
    
    
    
    
    
    
    
    
    
    
    