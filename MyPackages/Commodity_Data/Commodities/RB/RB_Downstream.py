# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 10:45:53 2018

@author: 李弘一萌
"""

import pandas as pd
from datetime import datetime
from .RB_Base import RB_Base
from . import RB_SpotPrice
from . import RB_Upstream, RB_Macro
from ...Base.DataType_Base import Manual, Computed, WindData
from ...Base.Plot_Base import Plot_Base
from matplotlib.ticker import FuncFormatter

class downstream_base(RB_Base, Plot_Base):
    table_english_name = "Downstream"
    table_chinese_name = u"下游"
    
    def output(self):
        print("Downstream")
    
    def get_relevant_df(self, col_list):
        local_col_name_list = downstream_base.get_all_table_classname()
        col_cls_list = []
        for x in col_list:
            col_cls_name = str(RB_Base.get_class_name(x))
            if col_cls_name not in local_col_name_list:
                col_cls_list.append(eval(RB_Base.get_table_class_full_variable(x)))
            else:
                col_cls_list.append(eval(col_cls_name))
        ts_list = [x().get_ts() for x in col_cls_list]
        tmp_table_df = pd.concat(ts_list, axis=1).dropna(how="all")
        return tmp_table_df 


###########################################################################################################################
""" 房地产行业 """

class FangDiChanKaiFaTouZiWanChengE_LeiJiZhi(downstream_base, WindData):
    field_name = u"房地产行业"
    col_name = u"房地产开发投资完成额_累计值"
    wind_code = "S0029656"
    
class BenNianGouZhiTuDiMianJi_LeiJiZhi(downstream_base, WindData):
    field_name = u"房地产行业"
    col_name = u"本年购置土地面积_累计值"
    wind_code = "S0029666"

class TuDiGouZhiFei_LeiJiZhi(downstream_base, WindData):
    field_name = u"房地产行业"
    col_name = u"土地购置费_累计值"
    wind_code = "S0049578"
    
class FangWuShiGongMianJi_LeiJiZhi(downstream_base, WindData):
    field_name = u"房地产行业"
    col_name = u"房屋施工面积_累计值"
    wind_code = "S0029668"
    
class FangWuXinKaiGongMianJi_LeiJiZhi(downstream_base, WindData):
    field_name = u"房地产行业"
    col_name = u"房屋新开工面积_累计值"
    wind_code = "S0029669"
    
class FangWuJunGongMianJi_LeiJiZhi(downstream_base, WindData):
    field_name = u"房地产行业"
    col_name = u"房屋竣工面积_累计值"
    wind_code = "S0029670"
    
class ShangPinFangXiaoShouMianJi_LeiJiZhi(downstream_base, WindData):
    field_name = u"房地产行业"
    col_name = u"商品房销售面积_累计值"
    wind_code = "S0029658"
    
class BaiChengZhuZhaiPingJunJiaGe_YiXianChengShi(downstream_base, WindData):
    field_name = u"房地产行业"
    col_name = u"百城住宅平均价格_一线城市"
    wind_code = "S2707439"
    
class BaiChengZhuZhaiPingJunJiaGe_ErXianChengShi(downstream_base, WindData):
    field_name = u"房地产行业"
    col_name = u"百城住宅平均价格_二线城市"
    wind_code = "S2707440"
    
class BaiChengZhuZhaiPingJunJiaGe_SanXianChengShi(downstream_base, WindData):
    field_name = u"房地产行业"
    col_name = u"百城住宅平均价格_三线城市"
    wind_code = "S2707441"
    
class ShuiNiChanLiang_DangYueZhi(downstream_base, WindData):
    field_name = u"房地产行业"
    col_name = u"水泥产量_当月值"
    wind_code = "S0027703"

###########################################################################################################################
""" 基建行业 """

class GuDingZiChanTouZiWanChengE_JiChuSheShiJianSheTouZi_LeiJiZhi(downstream_base, WindData):
    field_name = u"基建行业"
    col_name = u"固定资产投资完成额_基础设施建设投资_累计值"
    wind_code = "M5440434"

###########################################################################################################################
""" 贸易量 """

class XianLuoCaiGouLiang_ShangHai(downstream_base, WindData):
    field_name = u"基建行业"
    col_name = u"线螺采购量_上海"
    wind_code = "S5704503"

###########################################################################################################################
""" 出口利润 """

class LuoWenChuKouLiRun_ShangHaiGang(downstream_base, Computed):
    field_name = u"出口利润"
    col_name = u"螺纹出口利润_上海港"
    
    def get_ts_whole_progress(self):
        relevant_col_list = [u"中间价_美元兑人民币", u"螺纹出口FOB报价_HRB400_上海港", u"螺纹钢现货价格_HRB400_20mm_上海"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"螺纹出口FOB报价_HRB400_上海港"] * tmp_total[u"中间价_美元兑人民币"] * (1 + 0.13 / 0.16) - 55 - \
                                   tmp_total[u"螺纹钢现货价格_HRB400_20mm_上海"]
        return tmp_total

class LuoWenChuKouLiRun_TianJinGang(downstream_base, Computed):
    field_name = u"出口利润"
    col_name = u"螺纹出口利润_天津港"
    
    def get_ts_whole_progress(self):
        relevant_col_list = [u"中间价_美元兑人民币", u"螺纹出口FOB报价_HRB400_天津港", u"螺纹钢现货价格_HRB400_20mm_天津"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"螺纹出口FOB报价_HRB400_天津港"] * tmp_total[u"中间价_美元兑人民币"] * (1 + 0.13 / 0.16) - 55 - \
                                   tmp_total[u"螺纹钢现货价格_HRB400_20mm_天津"]
        return tmp_total



    
    
if __name__ == "__main__":
    ts = DiLunChangSiChanXiaoLv_15TianPingJun().get_ts()
    
    
    
    
    
    
    




    
    
    