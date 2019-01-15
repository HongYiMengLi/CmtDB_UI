# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 10:44:58 2018

@author: 李弘一萌
"""

import pandas as pd
from datetime import datetime
from .SR_Base import SR_Base
from . import SR_FuturesPrice, SR_Macro
from ...Base.DataType_Base import Manual, Computed, WindData
from ...Base.Plot_Base import Plot_Base
from matplotlib.ticker import FuncFormatter

class upstream_base(SR_Base, Plot_Base):
    table_english_name = "Upstream"
    table_chinese_name = u"上游"
    
    def output(self):
        print("Upstream")
    
    def get_relevant_df(self, col_list):
        local_col_name_list = upstream_base.get_all_table_classname()
        col_cls_list = []
        for x in col_list:
            col_cls_name = str(SR_Base.get_class_name(x))
            if col_cls_name not in local_col_name_list:
                col_cls_list.append(eval(SR_Base.get_table_class_full_variable(x)))
            else:
                col_cls_list.append(eval(col_cls_name))
        ts_list = [x().get_ts() for x in col_cls_list]
        tmp_table_df = pd.concat(ts_list, axis=1).dropna(how="all")
        return tmp_table_df

###########################################################################################################################
""" 国内甘蔗种植面积 """  

class ShuangZhouZhiTangBiLi_BaXi_UNICA(upstream_base, Manual):
    field_name = u"巴西压榨情况"
    col_name = u"双周制糖比例_巴西_UNICA"

class LeiJiZhiTangBiLi_BaXi_UNICA(upstream_base, Manual):
    field_name = u"巴西压榨情况"
    col_name = u"累计制糖比例_巴西_UNICA"

class ShuangZhouDunGanZheChanTangLiang_BaXi_UNICA(upstream_base, Manual):
    field_name = u"巴西压榨情况"
    col_name = u"双周吨甘蔗产糖量_巴西_UNICA"

class LeiJiDunGanZheChanTangLiang_BaXi_UNICA(upstream_base, Manual):
    field_name = u"巴西压榨情况"
    col_name = u"累计吨甘蔗产糖量_巴西_UNICA"

class ShuangZhouZhiTangLiang_BaXi_UNICA(upstream_base, Manual):
    field_name = u"巴西压榨情况"
    col_name = u"双周制糖量_巴西_UNICA"

class LeiJiZhiTangLiang_BaXi_UNICA(upstream_base, Manual):
    field_name = u"巴西压榨情况"
    col_name = u"累计制糖量_巴西_UNICA"


###########################################################################################################################
""" 国内甘蔗种植面积 """  

class GanZheZhongZhiMianJi_GuangXi(upstream_base, Manual):
    field_name = u"国内甘蔗种植面积"
    col_name = u"甘蔗种植面积_广西"

class GanZheZhongZhiMianJi_GuangDong(upstream_base, Manual):
    field_name = u"国内甘蔗种植面积"
    col_name = u"甘蔗种植面积_广东"

class GanZheZhongZhiMianJi_YunNan(upstream_base, Manual):
    field_name = u"国内甘蔗种植面积"
    col_name = u"甘蔗种植面积_云南"

class GanZheZhongZhiMianJi_HaiNan(upstream_base, Manual):
    field_name = u"国内甘蔗种植面积"
    col_name = u"甘蔗种植面积_海南"

class GanZheZhongZhiMianJi_NeiMengGu(upstream_base, Manual):
    field_name = u"国内甘蔗种植面积"
    col_name = u"甘蔗种植面积_内蒙古"

class GanZheZhongZhiMianJi_XinJiang(upstream_base, Manual):
    field_name = u"国内甘蔗种植面积"
    col_name = u"甘蔗种植面积_新疆"

class GanZheZhongZhiMianJi_QuanGuo(upstream_base, Manual):
    field_name = u"国内甘蔗种植面积"
    col_name = u"甘蔗种植面积_全国"

class GanZheZhongZhiMianJi_QuanGuo_NongYeNongCunBu(upstream_base, Manual):
    field_name = u"国内甘蔗种植面积"
    col_name = u"甘蔗种植面积_全国_农业农村部"

###########################################################################################################################
""" 国内糖料单产 """  

class GanZheDanChan_QuanGuo_NongYeNongCunBu(upstream_base, Manual):
    field_name = u"国内糖料单产"
    col_name = u"甘蔗单产_全国_农业农村部"

    
###########################################################################################################################
""" 开榨收榨进度 """  

class QuanGuoKaiZhaShouZhaJinDu(upstream_base, Manual):
    field_name = u"开榨收榨进度"
    col_name = u"全国开榨收榨进度"

class GuangXiKaiZhaShouZhaJinDu(upstream_base, Manual):
    field_name = u"开榨收榨进度"
    col_name = u"广西开榨收榨进度"




###########################################################################################################################
""" 气温 """  

class LiuZhouZuiGaoQiWen(upstream_base, Manual):
    field_name = u"气温"
    col_name = u"柳州最高气温"

class LiuZhouZuiDiQiWen(upstream_base, Manual):
    field_name = u"气温"
    col_name = u"柳州最低气温"

class ChongZuoZuiGaoQiWen(upstream_base, Manual):
    field_name = u"气温"
    col_name = u"崇左最高气温"

class ChongZuoZuiDiQiWen(upstream_base, Manual):
    field_name = u"气温"
    col_name = u"崇左最低气温"

    
class ZhouYeWenCha_LiuZhou(upstream_base, Computed):
    field_name = u"气温"
    col_name = u"昼夜温差_柳州"  
    def get_ts_whole_progress(self):
        relevant_col_list = [u"柳州最高气温", u"柳州最低气温"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"柳州最高气温"] - tmp_total[u"柳州最低气温"]
        return tmp_total
    
class ZhouYeWenCha_ChongZuo(upstream_base, Computed):
    field_name = u"气温"
    col_name = u"昼夜温差_崇左"  
    def get_ts_whole_progress(self):
        relevant_col_list = [u"崇左最高气温", u"崇左最低气温"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"崇左最高气温"] - tmp_total[u"崇左最低气温"]
        return tmp_total    

###########################################################################################################################
""" 进口 """  

class TaiGuoQiXianShengShui(upstream_base, Manual):
    field_name = u"进口"
    col_name = u"泰国期现升水"

class BaXiQiXianShengShui(upstream_base, Manual):
    field_name = u"进口"
    col_name = u"巴西期现升水"

class TaiGuoHaiYunFei(upstream_base, Manual):
    field_name = u"进口"
    col_name = u"泰国海运费"

class BaXiHaiYunFei(upstream_base, Manual):
    field_name = u"进口"
    col_name = u"巴西海运费"

class ShiTangJinKouLiang_QuanGuo_HaiGuanZongShu(upstream_base, Manual):
    field_name = u"进口"
    col_name = u"食糖进口量_全国_海关总署"
    
    
    
class TaiGuoPeiENeiJinKouChengBen(upstream_base, Computed):
    field_name = u"进口"
    col_name = u"泰国配额内进口成本"  
    def get_ts_whole_progress(self):
        relevant_col_list = [u"原糖近月合约价格_ICE", u"泰国期现升水", u"美元兑在岸人民币汇率", u"泰国海运费"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = (((tmp_total[u"原糖近月合约价格_ICE"] + tmp_total[u"泰国期现升水"]) * tmp_total[u"美元兑在岸人民币汇率"] * 1.0275 \
                                   * 22.046 + tmp_total[u"泰国海运费"] * tmp_total[u"美元兑在岸人民币汇率"]) * 1.004616 * 1.01 * 1.00125 + 70) * \
                                   1.15 * 1.16 * 1.04 + 450
        return tmp_total
    
class TaiGuoPeiENeiJinKouLiRun(upstream_base, Computed):
    field_name = u"进口"
    col_name = u"泰国配额内进口利润"  
    def get_ts_whole_progress(self):
        relevant_col_list = [u"泰国配额内进口成本", u"白糖现货价格_山东日照"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"白糖现货价格_山东日照"] - tmp_total[u"泰国配额内进口成本"]
        return tmp_total

class BaXiPeiENeiJinKouChengBen(upstream_base, Computed):
    field_name = u"进口"
    col_name = u"巴西配额内进口成本"  
    def get_ts_whole_progress(self):
        relevant_col_list = [u"原糖近月合约价格_ICE", u"巴西期现升水", u"美元兑在岸人民币汇率", u"巴西海运费"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = (((tmp_total[u"原糖近月合约价格_ICE"] + tmp_total[u"巴西期现升水"]) * tmp_total[u"美元兑在岸人民币汇率"] * 1.0275 \
                                   * 22.046 + tmp_total[u"巴西海运费"] * tmp_total[u"美元兑在岸人民币汇率"]) * 1.004616 * 1.01 * 1.00125 + 70) * \
                                   1.15 * 1.16 * 1.04 + 450
        return tmp_total
    
class BaXiPeiENeiJinKouLiRun(upstream_base, Computed):
    field_name = u"进口"
    col_name = u"巴西配额内进口利润"  
    def get_ts_whole_progress(self):
        relevant_col_list = [u"白糖现货价格_山东日照", u"巴西配额内进口成本"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"白糖现货价格_山东日照"] - tmp_total[u"巴西配额内进口成本"]
        return tmp_total
    
class TaiGuoPeiEWaiJinKouChengBen(upstream_base, Computed):
    field_name = u"进口"
    col_name = u"泰国配额外进口成本"  
    def get_ts_whole_progress(self):
        relevant_col_list = [u"原糖近月合约价格_ICE", u"泰国期现升水", u"美元兑在岸人民币汇率", u"泰国海运费"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = (((tmp_total[u"原糖近月合约价格_ICE"] + tmp_total[u"泰国期现升水"]) * tmp_total[u"美元兑在岸人民币汇率"] * 1.0275 \
                                   * 22.046 + tmp_total[u"泰国海运费"] * tmp_total[u"美元兑在岸人民币汇率"]) * 1.004616 * 1.01 * 1.00125 + 70) * \
                                   1.9 * 1.16 * 1.04 + 450
        return tmp_total
    
class TaiGuoPeiEWaiJinKouLiRun(upstream_base, Computed):
    field_name = u"进口"
    col_name = u"泰国配额外进口利润"  
    def get_ts_whole_progress(self):
        relevant_col_list = [u"白糖现货价格_山东日照", u"泰国配额外进口成本"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"白糖现货价格_山东日照"] - tmp_total[u"泰国配额外进口成本"]
        return tmp_total


class BaXiPeiEWaiJinKouChengBen(upstream_base, Computed):
    field_name = u"进口"
    col_name = u"巴西配额外进口成本"  
    def get_ts_whole_progress(self):
        relevant_col_list = [u"原糖近月合约价格_ICE", u"巴西期现升水", u"美元兑在岸人民币汇率", u"巴西海运费"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = (((tmp_total[u"原糖近月合约价格_ICE"] + tmp_total[u"巴西期现升水"]) * tmp_total[u"美元兑在岸人民币汇率"] * 1.0275 \
                                   * 22.046 + tmp_total[u"巴西海运费"] * tmp_total[u"美元兑在岸人民币汇率"]) * 1.004616 * 1.01 * 1.00125 + 70) * \
                                   1.9 * 1.16 * 1.04 + 450
        return tmp_total
    
class BaXiPeiEWaiJinKouLiRun(upstream_base, Computed):
    field_name = u"进口"
    col_name = u"巴西配额外进口利润"  
    def get_ts_whole_progress(self):
        relevant_col_list = [u"白糖现货价格_山东日照", u"巴西配额外进口成本"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"白糖现货价格_山东日照"] - tmp_total[u"巴西配额外进口成本"]
        return tmp_total    
    
    
    
    
    

    
    
if __name__ == "__main__":
    df = PTAXianHuoJiaGongFei().seasonal_plot()    
    
    
    
    
    
    
    
    
    
    
    
    
    
    