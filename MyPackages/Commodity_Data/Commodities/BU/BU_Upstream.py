# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 10:44:58 2018

@author: 李弘一萌
"""

import pandas as pd
from datetime import datetime
from .BU_Base import BU_Base
from . import BU_Macro, BU_SpotPrice, BU_FuturesPrice
from ...Base.DataType_Base import Manual, Computed, WindData
from ...Base.Plot_Base import Plot_Base
from ....Futures_Data.Quote.QuoteData import QuoteData
from matplotlib.ticker import FuncFormatter

class upstream_base(BU_Base, Plot_Base):
    table_english_name = "Upstream"
    table_chinese_name = u"上游"
#    original_db_filepath = data_path + u"LPP价格数据库.xlsx"
    
    def output(self):
        print("Upstream")
    
    def get_relevant_df(self, col_list):
        local_col_name_list = upstream_base.get_all_table_classname()
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
""" 国内现货价 """  

class ChaiYou_No0_QuanGuo(upstream_base, WindData):
    field_name = u"国内现货价"
    col_name = u"柴油_0#_全国"
    wind_code = "S5443781"


class ChaiYou_No0_ShanDongDiLian(upstream_base, WindData):
    field_name = u"国内现货价"
    col_name = u"柴油_0#_山东地炼"
    wind_code = "S5443782"
    

class QiYou_HuaBei_Before2012(upstream_base, WindData):
    field_name = u"国内现货价"
    col_name = u"汽油_2012年前"
    wind_code = "S5441659"

class QiYou_HuaBei_After2012(upstream_base, WindData):
    field_name = u"国内现货价"
    col_name = u"汽油_2012年后"
    wind_code = "S5134414"

class QiYou_HuaBei(upstream_base, Computed):
    field_name = u"国内现货价"
    col_name = u"汽油_华北"
    def get_ts_whole_progress(self):
        relevant_col_list = [u"汽油_2012年前", u"汽油_2012年后"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        pivot_date = datetime(2017, 2, 23)
        ts1 = tmp_total[tmp_total.index<pivot_date][u"汽油_2012年前"]
        ts2 = tmp_total[tmp_total.index>=pivot_date][u"汽油_2012年后"]
        tmp_total[self.col_name] = pd.concat([ts1, ts2])
        return tmp_total

class HanGuoCIFLiQingWanShuiJia_HuaDong(upstream_base, Computed):
    field_name = u"国内现货价"
    col_name = u"韩国CIF沥青完税价_华东"
    def get_ts_whole_progress(self):
        relevant_col_list = [u"沥青现货价格_CIF_韩国_华东", u"汇卖价_美元兑人民币"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total["沥青现货价格_CIF_韩国_华东"] * tmp_total["汇卖价_美元兑人民币"] * 1.16 * 1.056 + 30
        return tmp_total

class XinJiaPoCIFLiQingWanShuiJia_HuaNan(upstream_base, Computed):
    field_name = u"国内现货价"
    col_name = u"新加坡CIF沥青完税价_华南"
    def get_ts_whole_progress(self):
        relevant_col_list = [u"沥青现货价格_CIF_新加坡_华南", u"汇卖价_美元兑人民币"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total["沥青现货价格_CIF_新加坡_华南"] * tmp_total["汇卖价_美元兑人民币"] * 1.16 + 30
        return tmp_total
    
###########################################################################################################################
""" 美金价 """  
     
class ZhongLianYouJiaJia(upstream_base, Manual):
    field_name = u"美金价"
    col_name = u"中联油加价"

class ChuanYunFei_HanGuo_HuaNan(upstream_base, Manual):
    field_name = u"美金价"
    col_name = u"船运费_韩国_华南"

class ChuanYunFei_HanGuo_HuaDong(upstream_base, Manual):
    field_name = u"美金价"
    col_name = u"船运费_韩国_华东"

class ChuanYunFei_XinJiaPo_HuaNan(upstream_base, Manual):
    field_name = u"美金价"
    col_name = u"船运费_新加坡_华南"

class ChuanYunFei_XinJiaPo_HuaDong(upstream_base, Manual):
    field_name = u"美金价"
    col_name = u"船运费_新加坡_华东"

class MaRuiDuiWTITieShui(upstream_base, Manual):
    field_name = u"美金价"
    col_name = u"马瑞对WTI贴水"    
    
class BrentJieSuanJia(upstream_base, WindData):
    field_name = u"美金价"
    col_name = u"Brent结算价"
    wind_code = "S0031525"

class WTIJieSuanJia(upstream_base, WindData):
    field_name = u"美金价"
    col_name = u"WTI结算价"
    wind_code = "M0000005"

class DuLiYouXianHuoJia(upstream_base, WindData):
    field_name = u"美金价"
    col_name = u"杜里油现货价"
    wind_code = "S0031535"


""" 计算指标 """ 

class MaRuiYouChengBen(upstream_base, Computed):
    field_name = u"美金价"
    col_name = u"马瑞油成本"  
    def get_ts_whole_progress(self):
        relevant_col_list = [u"马瑞对WTI贴水", u"中联油加价"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"马瑞对WTI贴水"].fillna(0) + tmp_total[u"中联油加价"]
        return tmp_total
    
class MaRuiYouJiaGe(upstream_base, Computed):
    field_name = u"美金价"
    col_name = u"马瑞油价格"  
    def get_ts_whole_progress(self):
        relevant_col_list = [u"马瑞油成本", u"WTI结算价"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"马瑞油成本"] + tmp_total[u"WTI结算价"]
        return tmp_total    
    
###########################################################################################################################
""" 税费 """ 

class QiYouXiaoFeiShui(upstream_base, Manual):
    field_name = u"税费"
    col_name = u"汽油消费税"
    
class ChaiYouXiaoFeiShui(upstream_base, Manual):
    field_name = u"税费"
    col_name = u"柴油消费税"    
    
###########################################################################################################################
""" 原油进口 """ 

class YuanYouJinKouShuLiang_DangYueZhi(upstream_base, WindData):
    field_name = u"原油进口"
    col_name = u"原油进口数量_当月值"
    wind_code = "S0027235"

class YuanYouJinKouLiang_WeiNeiRuiLa(upstream_base, WindData):
    field_name = u"原油进口"
    col_name = u"原油进口量_委内瑞拉"
    wind_code = "S5429093"

###########################################################################################################################
""" 进口利润 """ 
class LiQingJinKouLiRun_XinJiaPo_HuaNan(upstream_base, Computed):
    field_name = u"进口利润"
    col_name = u"沥青进口利润_新加坡_华南"  
    def get_ts_whole_progress(self):
        relevant_col_list = [u"沥青现货价格_CIF_新加坡_华南", u"沥青现货价格_华南", u"汇卖价_美元兑人民币"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"沥青现货价格_华南"] - (tmp_total[u"沥青现货价格_CIF_新加坡_华南"] * tmp_total[u"汇卖价_美元兑人民币"] \
                                   * 1.17 + 30)
        return tmp_total
    
class LiQingJinKouLiRun_HanGuo_HuaDong(upstream_base, Computed):
    field_name = u"进口利润"
    col_name = u"沥青进口利润_韩国_华东"  
    def get_ts_whole_progress(self):
        relevant_col_list = [u"沥青现货价格_CIF_韩国_华东", u"沥青现货价格_华东", u"汇卖价_美元兑人民币"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"沥青现货价格_华东"] - (tmp_total[u"沥青现货价格_CIF_韩国_华东"] * tmp_total[u"汇卖价_美元兑人民币"] \
                                   * 1.17 * 1.056 + 30)
        return tmp_total
    
class LiQingJinKouLiRun_HanGuo_HuaNan(upstream_base, Computed):
    field_name = u"进口利润"
    col_name = u"沥青进口利润_韩国_华南"  
    def get_ts_whole_progress(self):
        relevant_col_list = [u"沥青现货价格_CIF_韩国_华南", u"沥青现货价格_华南", u"汇卖价_美元兑人民币"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"沥青现货价格_华南"] - (tmp_total[u"沥青现货价格_CIF_韩国_华南"] * tmp_total[u"汇卖价_美元兑人民币"] \
                                   * 1.17 * 1.056 + 30)
        return tmp_total
    
class LiQingJinKouLiRun_TaiGuo_HuaNan(upstream_base, Computed):
    field_name = u"进口利润"
    col_name = u"沥青进口利润_泰国_华南"  
    def get_ts_whole_progress(self):
        relevant_col_list = [u"沥青现货价格_CIF_泰国_华南", u"沥青现货价格_华南", u"汇卖价_美元兑人民币"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"沥青现货价格_华南"] - (tmp_total[u"沥青现货价格_CIF_泰国_华南"] * tmp_total[u"汇卖价_美元兑人民币"] \
                                   * 1.17 + 30)
        return tmp_total

class LiQingJinKouLiRun_XinJiaPo_HuaDong(upstream_base, Computed):
    field_name = u"进口利润"
    col_name = u"沥青进口利润_新加坡_华东"  
    def get_ts_whole_progress(self):
        relevant_col_list = [u"沥青现货价格_CIF_新加坡_华东", u"沥青现货价格_华东", u"汇卖价_美元兑人民币"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"沥青现货价格_华东"] - (tmp_total[u"沥青现货价格_CIF_新加坡_华东"] * tmp_total[u"汇卖价_美元兑人民币"] \
                                   * 1.17 + 30)
        return tmp_total

###########################################################################################################################
""" 生产利润 """ 

class MaRuiYouShengChanLiQingLiRun_ShanDong(upstream_base, Computed):
    field_name = u"生产利润"
    col_name = u"马瑞油生产沥青利润_山东" 
    axhline = 0
    def get_ts_whole_progress(self):
        relevant_col_list = [u"液化气出厂价_京博石化", u"汽油_华北", u"柴油_0#_山东地炼", u"沥青现货价格_山东", u"汇卖价_美元兑人民币", u"WTI结算价", 
                             u"马瑞油成本", u"汽油消费税", u"柴油消费税"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"液化气出厂价_京博石化"] * 0.0255 + tmp_total[u"汽油_华北"] * 0.124 + tmp_total[u"柴油_0#_山东地炼"] * 0.2291 + \
                                   tmp_total[u"沥青现货价格_山东"] * 0.6012 - (tmp_total[u"WTI结算价"] + tmp_total[u"马瑞油成本"]) * 6.59 * 1.16 * \
                                   tmp_total[u"汇卖价_美元兑人民币"] - 100 - 150 - 0.2291 * 1000 / 0.84 * tmp_total[u"柴油消费税"] - \
                                   0.124 * 1000 / 0.725 * tmp_total[u"汽油消费税"]
        return tmp_total

class LiQing06PanMianLiRun(upstream_base, Computed):
    field_name = u"生产利润"
    col_name = u"沥青06盘面利润"  
    def get_ts_whole_progress(self):
        relevant_col_list = [u"液化气出厂价_京博石化", u"汽油_华北", u"柴油_0#_山东地炼", u"BU06合约收盘价", u"汇卖价_美元兑人民币", u"WTI结算价", 
                             u"马瑞油成本", u"汽油消费税", u"柴油消费税"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"液化气出厂价_京博石化"] * 0.0255 + tmp_total[u"汽油_华北"] * 0.124 + tmp_total[u"柴油_0#_山东地炼"] * 0.2291 + \
                                   tmp_total[u"BU06合约收盘价"] * 0.6012 - (tmp_total[u"WTI结算价"] + tmp_total[u"马瑞油成本"]) * 6.59 * 1.16 * \
                                   tmp_total[u"汇卖价_美元兑人民币"] - 100 - 150 - 0.2291 * 1000 / 0.84 * tmp_total[u"柴油消费税"] - \
                                   0.124 * 1000 / 0.725 * tmp_total[u"汽油消费税"]
        return tmp_total
    
class LiQing09PanMianLiRun(upstream_base, Computed):
    field_name = u"生产利润"
    col_name = u"沥青09盘面利润"  
    def get_ts_whole_progress(self):
        relevant_col_list = [u"液化气出厂价_京博石化", u"汽油_华北", u"柴油_0#_山东地炼", u"BU09合约收盘价", u"汇卖价_美元兑人民币", u"WTI结算价", 
                             u"马瑞油成本", u"汽油消费税", u"柴油消费税"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"液化气出厂价_京博石化"] * 0.0255 + tmp_total[u"汽油_华北"] * 0.124 + tmp_total[u"柴油_0#_山东地炼"] * 0.2291 + \
                                   tmp_total[u"BU09合约收盘价"] * 0.6012 - (tmp_total[u"WTI结算价"] + tmp_total[u"马瑞油成本"]) * 6.59 * 1.16 * \
                                   tmp_total[u"汇卖价_美元兑人民币"] - 100 - 150 - 0.2291 * 1000 / 0.84 * tmp_total[u"柴油消费税"] - \
                                   0.124 * 1000 / 0.725 * tmp_total[u"汽油消费税"]
        return tmp_total
    
class LiQing12PanMianLiRun(upstream_base, Computed):
    field_name = u"生产利润"
    col_name = u"沥青12盘面利润"  
    def get_ts_whole_progress(self):
        relevant_col_list = [u"液化气出厂价_京博石化", u"汽油_华北", u"柴油_0#_山东地炼", u"BU12合约收盘价", u"汇卖价_美元兑人民币", u"WTI结算价", 
                             u"马瑞油成本", u"汽油消费税", u"柴油消费税"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"液化气出厂价_京博石化"] * 0.0255 + tmp_total[u"汽油_华北"] * 0.124 + tmp_total[u"柴油_0#_山东地炼"] * 0.2291 + \
                                   tmp_total[u"BU12合约收盘价"] * 0.6012 - (tmp_total[u"WTI结算价"] + tmp_total[u"马瑞油成本"]) * 6.59 * 1.16 * \
                                   tmp_total[u"汇卖价_美元兑人民币"] - 100 - 150 - 0.2291 * 1000 / 0.84 * tmp_total[u"柴油消费税"] - \
                                   0.124 * 1000 / 0.725 * tmp_total[u"汽油消费税"]
        return tmp_total
    
class MaRuiYouZongHeLianZhiLiRun_BuChanLiQing(upstream_base, Computed):
    field_name = u"生产利润"
    col_name = u"马瑞油综合炼制利润_不产沥青"  
    def get_ts_whole_progress(self):
        relevant_col_list = [u"液化气出厂价_京博石化", u"汽油_华北", u"柴油_0#_山东地炼", u"石油焦_2#A_出厂价_滨阳燃化", u"汇卖价_美元兑人民币", u"WTI结算价", 
                             u"马瑞油成本", u"汽油消费税", u"柴油消费税"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"液化气出厂价_京博石化"] * 0.0857 + tmp_total[u"汽油_华北"] * 0.2589 + tmp_total[u"柴油_0#_山东地炼"] * 0.4762 + \
                                   tmp_total[u"石油焦_2#A_出厂价_滨阳燃化"] * 0.1509 - (tmp_total[u"WTI结算价"] + tmp_total[u"马瑞油成本"]) * 6.59 * 1.16 * \
                                   tmp_total[u"汇卖价_美元兑人民币"] - 100 - 150 - 0.4762 * 1000 / 0.84 * tmp_total[u"柴油消费税"] - \
                                   0.2589 * 1000 / 0.725 * tmp_total[u"汽油消费税"]
        return tmp_total
    
class JiaoHuaLuJingLiRun(upstream_base, Computed):
    field_name = u"生产利润"
    col_name = u"焦化路径利润"  
    def get_ts_whole_progress(self):
        relevant_col_list = [u"液化气出厂价_京博石化", u"汽油_华北", u"柴油_0#_山东地炼", u"石油焦_2#A_出厂价_滨阳燃化", u"汇卖价_美元兑人民币", u"蜡油_2#_出厂价_中海滨州", 
                             u"焦化料价格_山东", u"汽油消费税", u"柴油消费税"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"液化气出厂价_京博石化"] * 0.0835 + tmp_total[u"汽油_华北"] * 0.1924 + tmp_total[u"柴油_0#_山东地炼"] * 0.37 + \
                                   tmp_total[u"石油焦_2#A_出厂价_滨阳燃化"] * 0.2365 + tmp_total[u"蜡油_2#_出厂价_中海滨州"] * 0.1111 - tmp_total[u"焦化料价格_山东"] \
                                   * 1.16 - 100 - 150 - 0.37 * 1000 / 0.84 * tmp_total[u"柴油消费税"] - 0.1924 * 1000 / 0.725 * tmp_total[u"汽油消费税"]
        return tmp_total
    
class MaRuiYouZongHeLianZhiLiRun(upstream_base, Computed):
    field_name = u"生产利润"
    col_name = u"马瑞油综合炼制利润"  
    def get_ts_whole_progress(self):
        relevant_col_list = [u"液化气出厂价_京博石化", u"汽油_华北", u"柴油_0#_山东地炼", u"石油焦_2#A_出厂价_滨阳燃化", u"汇卖价_美元兑人民币", u"WTI结算价", 
                             u"马瑞油成本", u"汽油消费税", u"柴油消费税"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"液化气出厂价_京博石化"] * 0.0857 + tmp_total[u"汽油_华北"] * 0.2589 + tmp_total[u"柴油_0#_山东地炼"] * 0.4762 + \
                                   tmp_total[u"石油焦_2#A_出厂价_滨阳燃化"] * 0.1509 - (tmp_total[u"WTI结算价"] + tmp_total[u"马瑞油成本"]) * 6.59 * 1.16 * \
                                   tmp_total[u"汇卖价_美元兑人民币"] - 100 - 150 - 0.4762 * 1000 / 0.84 * tmp_total[u"柴油消费税"] - \
                                   0.1984 * 1000 / 0.725 * tmp_total[u"汽油消费税"]
        return tmp_total
    

if __name__ == "__main__":
    tmp_df = BrentJieSuanJia().get_ts()

    
    
    
    
    
    
    
    
    
    
    
    
    