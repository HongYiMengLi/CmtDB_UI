# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 10:45:53 2018

@author: 李弘一萌
"""

import pandas as pd
from datetime import datetime
from .NI_Base import NI_Base
from ...Base.DataType_Base import Manual, Computed, WindData
from ...Base.Plot_Base import Plot_Base
from matplotlib.ticker import FuncFormatter

class downstream_base(NI_Base, Plot_Base):
    table_english_name = "Downstream"
    table_chinese_name = u"下游"
#    original_db_filepath = data_path + u"LPP价格数据库.xlsx"
    
    def output(self):
        print("Downstream")
    
    def get_relevant_df(self, col_list):
        local_col_name_list = downstream_base.get_all_table_classname()
        col_cls_list = []
        for x in col_list:
            col_cls_name = str(NI_Base.get_class_name(x))
            if col_cls_name not in local_col_name_list:
                col_cls_list.append(eval(NI_Base.get_table_class_full_variable(x)))
            else:
                col_cls_list.append(eval(col_cls_name))
        ts_list = [x().get_ts() for x in col_cls_list]
        tmp_table_df = pd.concat(ts_list, axis=1).dropna(how="all")
        return tmp_table_df 


###########################################################################################################################
""" 不锈钢产量 """


class BuXiuCuGangChanLiang_ZhuLiuChangHeJi(downstream_base, WindData):
    field_name = u"不锈钢产量"
    col_name = u"不锈粗钢产量_主流厂合计"
    wind_code = "S5721237"
    
class BuXiuCuGangChanLiang_200Xi(downstream_base, WindData):
    field_name = u"不锈钢产量"
    col_name = u"不锈粗钢产量_200系"
    wind_code = "S5721238"
    
class BuXiuCuGangChanLiang_300Xi(downstream_base, WindData):
    field_name = u"不锈钢产量"
    col_name = u"不锈粗钢产量_300系"
    wind_code = "S5721239"
    
class BuXiuCuGangChanLiang_400Xi(downstream_base, WindData):
    field_name = u"不锈钢产量"
    col_name = u"不锈粗钢产量_400系"
    wind_code = "S5721240"
    
class BuXiuCuGangChanLiang_QuanQiu_DangJiZhi(downstream_base, WindData):
    field_name = u"不锈钢产量"
    col_name = u"不锈粗钢产量_全球_当季值"
    wind_code = "S5707372"
    
class BuXiuCuGangChanLiang_XiOuHeFeiZhou_DangJiZhi(downstream_base, WindData):
    field_name = u"不锈钢产量"
    col_name = u"不锈粗钢产量_西欧和非洲_当季值"
    wind_code = "S5707368"
    
class BuXiuCuGangChanLiang_ZhongOuHeDongOu_DangJiZhi(downstream_base, WindData):
    field_name = u"不锈钢产量"
    col_name = u"不锈粗钢产量_中欧和东欧_当季值"
    wind_code = "S5707369"
    
class BuXiuCuGangChanLiang_MeiZhou_DangJiZhi(downstream_base, WindData):
    field_name = u"不锈钢产量"
    col_name = u"不锈粗钢产量_美洲_当季值"
    wind_code = "S5707370"
    
class BuXiuCuGangChanLiang_YaZhou_DangJiZhi(downstream_base, WindData):
    field_name = u"不锈钢产量"
    col_name = u"不锈粗钢产量_亚洲_当季值"
    wind_code = "S5707371"
    
###########################################################################################################################
""" 不锈钢成本 """


class BuXiuGangChangShengChanChengBen_YiDiNieTieWeiYuanLiao(downstream_base, Manual):
    field_name = u"不锈钢成本"
    col_name = u"不锈钢厂生产成本_以低镍铁为原料"
    
class BuXiuGangChangShengChanChengBen_YiGaoNieTieWeiYuanLiao(downstream_base, Manual):
    field_name = u"不锈钢成本"
    col_name = u"不锈钢厂生产成本_以高镍铁为原料"    
    
    
###########################################################################################################################
""" 不锈钢价格 """

class BuXiuGangJiaGe_304Over2BJuanBan_2Dot0mm_TaiGang_WuXi(downstream_base, WindData):
    field_name = u"不锈钢价格"
    col_name = u"不锈钢价格_304/2B卷板_2.0mm_太钢_无锡"
    wind_code = "S5705139"
        
class BuXiuGangJiaGe_201Over2BJuanBan_2Dot0mm_WuXi(downstream_base, WindData):
    field_name = u"不锈钢价格"
    col_name = u"不锈钢价格_201/2B卷板_2.0mm_无锡"
    wind_code = "S5705135"    
    
class BuXiuGangJiaGe_430Over2BJuanBan_2Dot0mm_WuXi(downstream_base, WindData):
    field_name = u"不锈钢价格"
    col_name = u"不锈钢价格_430/2B卷板_2.0mm_无锡"
    wind_code = "S5705137"    
    
class BuXiuGangJiaGe_FeiBuXiuGang_304_FoShan(downstream_base, WindData):
    field_name = u"不锈钢价格"
    col_name = u"不锈钢价格_废不锈钢_304_佛山"
    wind_code = "S5705461"    
    
class BuXiuGangJiaGe_FeiBuXiuGang_304_WuXi(downstream_base, WindData):
    field_name = u"不锈钢价格"
    col_name = u"不锈钢价格_废不锈钢_304_无锡"
    wind_code = "S5705464"    
    
###########################################################################################################################
""" 不锈钢库存 """

class BuXiuGangKuCun_ZongJi_FoShan(downstream_base, WindData):
    field_name = u"不锈钢库存"
    col_name = u"不锈钢库存_总计_佛山"
    wind_code = "S5708356"    
    
class BuXiuGangKuCun_ZongJi_WuXi(downstream_base, WindData):
    field_name = u"不锈钢库存"
    col_name = u"不锈钢库存_总计_无锡"
    wind_code = "S5708368"    

    
###########################################################################################################################
""" 不锈钢利润 """    
    
class BuXiuGangChangShengChanLiRun_YiDiNieTieWeiYuanLiao(downstream_base, Computed):
    field_name = u"不锈钢利润"
    col_name = u"不锈钢厂生产利润_以低镍铁为原料"    
    def get_ts_whole_progress(self):
        relevant_col_list = [u"不锈钢价格_304/2B卷板_2.0mm_太钢_无锡", u"不锈钢厂生产成本_以低镍铁为原料"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"不锈钢价格_304/2B卷板_2.0mm_太钢_无锡"] - tmp_total[u"不锈钢厂生产成本_以低镍铁为原料"]
        return tmp_total

class BuXiuGangChangShengChanLiRun_YiGaoNieTieWeiYuanLiao(downstream_base, Computed):
    field_name = u"不锈钢利润"
    col_name = u"不锈钢厂生产利润_以高镍铁为原料"    
    def get_ts_whole_progress(self):
        relevant_col_list = [u"不锈钢价格_304/2B卷板_2.0mm_太钢_无锡", u"不锈钢厂生产成本_以高镍铁为原料"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"不锈钢价格_304/2B卷板_2.0mm_太钢_无锡"] - tmp_total[u"不锈钢厂生产成本_以高镍铁为原料"]
        return tmp_total

###########################################################################################################################
""" 硫酸镍价格 """

class LiuSuanNieJiaGe_ChangJiangYouSeShiChang_PingJunJia(downstream_base, WindData):
    field_name = u"硫酸镍价格"
    col_name = u"硫酸镍价格_长江有色市场_平均价"
    wind_code = "S0048092"    


    
    
if __name__ == "__main__":
    ts = DiLunChangSiChanXiaoLv_15TianPingJun().get_ts()
    
    
    
    
    
    
    




    
    
    