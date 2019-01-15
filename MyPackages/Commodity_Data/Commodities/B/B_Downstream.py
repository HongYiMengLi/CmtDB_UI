# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 10:45:53 2018

@author: 李弘一萌
"""

import pandas as pd
from datetime import datetime
from MyFutureClass.CmtDataBase.Commodities.CF.CF_Base import CF_Base
from MyFutureClass.CmtDataBase.Commodities.CF import CF_SpotPrice
from MyFutureClass.CmtDataBase.Base.DataType_Base import Manual, Computed, WindData
from MyFutureClass.CmtDataBase.Base.Plot_Base import Plot_Base

from MyFutureClass.Data.QuoteData import QuoteData
from matplotlib.ticker import FuncFormatter

class downstream_base(CF_Base, Plot_Base):
    table_english_name = "Downstream"
    table_chinese_name = u"下游"
    
    def output(self):
        print("Downstream")
    
    def get_relevant_df(self, col_list):
        local_col_name_list = downstream_base.get_all_table_classname()
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
""" PMI值 """

class FangZhiYePMI(downstream_base, WindData):
    field_name = u"PMI值"
    col_name = u"纺织业PMI"
    wind_code = "S5319065"  
    
class FangZhiYePMI_XinDingDan(downstream_base, WindData):
    field_name = u"PMI值"
    col_name = u"纺织业PMI_新订单"
    wind_code = "S5319066" 
    
class FangZhiYePMI_KaiJiLv(downstream_base, WindData):
    field_name = u"PMI值"
    col_name = u"纺织业PMI_开机率"
    wind_code = "S5319068" 

class FangZhiYePMI_ShengChanLiang(downstream_base, WindData):
    field_name = u"PMI值"
    col_name = u"纺织业PMI_生产量"
    wind_code = "S5319067" 
    
class FangZhiYePMI_MianShaKuCun(downstream_base, WindData):
    field_name = u"PMI值"
    col_name = u"纺织业PMI_棉纱库存"
    wind_code = "S5319069" 
    
class FangZhiYePMI_MianHuaKuCun(downstream_base, WindData):
    field_name = u"PMI值"
    col_name = u"纺织业PMI_棉花库存"
    wind_code = "S5319070" 
    
###########################################################################################################################
""" 成品出口 """

class FangZhiFuZhuangFuShiYeChuKouJiaoHuoZhi_DangYueZhi(downstream_base, WindData):
    field_name = u"成品出口"
    col_name = u"纺织服装服饰业出口交货值_当月值"
    wind_code = "M0058976"  

class FangZhiFuZhuangFuShiYeChuKouJiaoHuoZhi_LeiJiZhi(downstream_base, WindData):
    field_name = u"成品出口"
    col_name = u"纺织服装服饰业出口交货值_累计值"
    wind_code = "M0059054"  

###########################################################################################################################
""" 开机率 """

class ChunMianShaChangFuHe_RiJun(downstream_base, Manual):
    field_name = u"开机率"
    col_name = u"纯棉纱厂负荷_日均"

class ChunMianShaChangFuHe_ZhouJun(downstream_base, Manual):
    field_name = u"开机率"
    col_name = u"纯棉纱厂负荷_周均"
    
class ChunMianShaChangFuHe_YueJun(downstream_base, Manual):
    field_name = u"开机率"
    col_name = u"纯棉纱厂负荷_月均"

class QuanMianPiBuFuHe_RiJun(downstream_base, Manual):
    field_name = u"开机率"
    col_name = u"全棉坯布负荷_日均"

class QuanMianPiBuFuHe_ZhouJun(downstream_base, Manual):
    field_name = u"开机率"
    col_name = u"全棉坯布负荷_周均"
    
class QuanMianPiBuFuHe_YueJun(downstream_base, Manual):
    field_name = u"开机率"
    col_name = u"全棉坯布负荷_月均"


###########################################################################################################################
""" 棉纱产量 """

class MianShaChanLiang_YueDu(downstream_base, Manual):
    field_name = u"棉纱产量"
    col_name = u"棉纱产量_月度"

###########################################################################################################################
""" 棉纱出口量 """

class MianShaChuKou_YueDu(downstream_base, WindData):
    field_name = u"棉纱出口量"
    col_name = u"棉纱出口_月度"
    wind_code = "S0072049"  

###########################################################################################################################
""" 棉纱进口价格 """

class JinKouMianShaJiaGe_YinDu_C32S_GangKouTiHuoJia(downstream_base, WindData):
    field_name = u"棉纱进口价格"
    col_name = u"进口棉纱价格_印度_C32S_港口提货价"
    wind_code = "S5318617"  

###########################################################################################################################
""" 棉纱进口量 """

class MianShaJinKou_YueDu(downstream_base, WindData):
    field_name = u"棉纱进口量"
    col_name = u"棉纱进口_月度"
    wind_code = "S0071186"  

###########################################################################################################################
""" 棉纱进口指数 """

class JinKouMianShaJiaGeZhiShu_GangKouTiHuoJia_C32S(downstream_base, WindData):
    field_name = u"棉纱进口指数"
    col_name = u"进口棉纱价格指数(FCY_Index)_港口提货价_C32S"
    wind_code = "S5318605"  

class JinKouMianShaJiaGeZhiShu_DaoGangJia_C32S(downstream_base, WindData):
    field_name = u"棉纱进口指数"
    col_name = u"进口棉纱价格指数(FCY_Index)_到港价_C32S"
    wind_code = "S5318602" 

###########################################################################################################################
""" 棉纱指数 """

class JianCeXiTongJC40SZhiShu_CNCotton(downstream_base, WindData):
    field_name = u"棉纱指数"
    col_name = u"监测系统JC40S指数_CNCotton"
    wind_code = "S5329495"  

class JianCeXiTongC32SZhiShu_CNCotton(downstream_base, WindData):
    field_name = u"棉纱指数"
    col_name = u"监测系统C32S指数_CNCotton"
    wind_code = "S5329494"

class JianCeXiTongC32SZhiShu_CF_Index(downstream_base, WindData):
    field_name = u"棉纱指数"
    col_name = u"监测系统C32S指数_CF_Index"
    wind_code = "S5318588"

    
###########################################################################################################################
""" 加工利润 """
    
class MianShaJiaGongLiRun_JiShi(downstream_base, Computed):
    field_name = u"加工利润"
    col_name = u"棉纱加工利润_即时"   
    def get_ts_whole_progress(self):
        relevant_col_list = [u"监测系统C32S指数_CNCotton", u"中国棉花328价格指数"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"监测系统C32S指数_CNCotton"] - tmp_total[u"中国棉花328价格指数"] * 1.1 - 6100
        return tmp_total  


class MianShaJiaGongLiRun_10TianKuCun(downstream_base, Computed):
    field_name = u"加工利润"
    col_name = u"棉纱加工利润_10天库存"   
    def get_ts_whole_progress(self):
        relevant_col_list = [u"监测系统C32S指数_CNCotton", u"中国棉花328价格指数"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"监测系统C32S指数_CNCotton"] - tmp_total[u"中国棉花328价格指数"].shift(10) * 1.1 - 6100
        return tmp_total  


class MianShaJiaGongLiRun_20TianKuCun(downstream_base, Computed):
    field_name = u"加工利润"
    col_name = u"棉纱加工利润_20天库存"   
    def get_ts_whole_progress(self):
        relevant_col_list = [u"监测系统C32S指数_CNCotton", u"中国棉花328价格指数"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"监测系统C32S指数_CNCotton"] - tmp_total[u"中国棉花328价格指数"].shift(20) * 1.1 - 6100
        return tmp_total  


class MianShaJiaGongLiRun_30TianKuCun(downstream_base, Computed):
    field_name = u"加工利润"
    col_name = u"棉纱加工利润_30天库存"   
    def get_ts_whole_progress(self):
        relevant_col_list = [u"监测系统C32S指数_CNCotton", u"中国棉花328价格指数"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"监测系统C32S指数_CNCotton"] - tmp_total[u"中国棉花328价格指数"].shift(30) * 1.1 - 6100
        return tmp_total  






























    

    