# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 16:35:12 2018

@author: 李弘一萌
"""

import pandas as pd
from datetime import datetime
from .SR_Base import SR_Base
from ...Base.DataType_Base import Manual, Computed, WindData
from ...Base.Plot_Base import Plot_Base
from matplotlib.ticker import FuncFormatter

class spot_price_base(SR_Base, Plot_Base):
    table_english_name = "SpotPrice"
    table_chinese_name = u"现货价格"
    
    def output(self):
        print("SpotPrice")
    
    def get_relevant_df(self, col_list):
        local_col_name_list = spot_price_base.get_all_table_classname()
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
""" 白糖替代品价格 """    

class GuoPuTangJiangF55JiaGe(spot_price_base, Manual):
    field_name = u"白糖替代品价格"
    col_name = u"果葡糖浆F55价格"

###########################################################################################################################
""" 电子盘价格 """    

class LiuZhouDianZiPanJiaGe_JinYueDiSanZhouJiaGe(spot_price_base, Manual):
    field_name = u"电子盘价格"
    col_name = u"柳州电子盘价格_近月第三周价格"
    
###########################################################################################################################
""" 国内现货价格 """    

class BaiTangXianHuoJiaGe_HeBeiGaoCheng(spot_price_base, Manual):
    field_name = u"国内现货价格"
    col_name = u"白糖现货价格_河北藁城"

class BaiTangXianHuoJiaGe_HeBeiQinHuangDao(spot_price_base, Manual):
    field_name = u"国内现货价格"
    col_name = u"白糖现货价格_河北秦皇岛"

class BaiTangXianHuoJiaGe_HeBeiTangShan(spot_price_base, Manual):
    field_name = u"国内现货价格"
    col_name = u"白糖现货价格_河北唐山"

class BaiTangXianHuoJiaGe_HeBeiXingTai(spot_price_base, Manual):
    field_name = u"国内现货价格"
    col_name = u"白糖现货价格_河北邢台"

class BaiTangXianHuoJiaGe_HeNanZhengZhou(spot_price_base, Manual):
    field_name = u"国内现货价格"
    col_name = u"白糖现货价格_河南郑州"

class BaiTangXianHuoJiaGe_ShangHai(spot_price_base, Manual):
    field_name = u"国内现货价格"
    col_name = u"白糖现货价格_上海"

class BaiTangXianHuoJiaGe_JiangSuXuZhou(spot_price_base, Manual):
    field_name = u"国内现货价格"
    col_name = u"白糖现货价格_江苏徐州"

class BaiTangXianHuoJiaGe_JiangSuNanJing(spot_price_base, Manual):
    field_name = u"国内现货价格"
    col_name = u"白糖现货价格_江苏南京"

class BaiTangXianHuoJiaGe_JiangSuNanTong(spot_price_base, Manual):
    field_name = u"国内现货价格"
    col_name = u"白糖现货价格_江苏南通"

class BaiTangXianHuoJiaGe_ZheJiangPingHu(spot_price_base, Manual):
    field_name = u"国内现货价格"
    col_name = u"白糖现货价格_浙江平湖"

class BaiTangXianHuoJiaGe_ShanXiXianYang(spot_price_base, Manual):
    field_name = u"国内现货价格"
    col_name = u"白糖现货价格_陕西咸阳"

class BaiTangXianHuoJiaGe_HuBeiWuHan(spot_price_base, Manual):
    field_name = u"国内现货价格"
    col_name = u"白糖现货价格_湖北武汉"

class BaiTangXianHuoJiaGe_YunNanKunMing(spot_price_base, Manual):
    field_name = u"国内现货价格"
    col_name = u"白糖现货价格_云南昆明"

class BaiTangXianHuoJiaGe_YunNanXiangYun(spot_price_base, Manual):
    field_name = u"国内现货价格"
    col_name = u"白糖现货价格_云南祥云"

class BaiTangXianHuoJiaGe_GuangXi(spot_price_base, Manual):
    field_name = u"国内现货价格"
    col_name = u"白糖现货价格_广西"

class BaiTangXianHuoJiaGe_GuangDongFoShan(spot_price_base, Manual):
    field_name = u"国内现货价格"
    col_name = u"白糖现货价格_广东佛山"

class BaiTangXianHuoJiaGe_LiaoNingYingKou(spot_price_base, Manual):
    field_name = u"国内现货价格"
    col_name = u"白糖现货价格_辽宁营口"

class BaiTangXianHuoJiaGe_BeiJing(spot_price_base, Manual):
    field_name = u"国内现货价格"
    col_name = u"白糖现货价格_北京"

class BaiTangXianHuoJiaGe_TianJin(spot_price_base, Manual):
    field_name = u"国内现货价格"
    col_name = u"白糖现货价格_天津"

class BaiTangXianHuoJiaGe_ShanDongQingDao(spot_price_base, Manual):
    field_name = u"国内现货价格"
    col_name = u"白糖现货价格_山东青岛"

class BaiTangXianHuoJiaGe_ShanDongRiZhao(spot_price_base, Manual):
    field_name = u"国内现货价格"
    col_name = u"白糖现货价格_山东日照"





if __name__ == "__main__":
    ts = YeHuaQiChuChangJia_JingBoShiHua().get_ts()