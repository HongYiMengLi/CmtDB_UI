# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 16:35:12 2018

@author: 李弘一萌
"""

import pandas as pd
from datetime import datetime
from .A_Base import A_Base
from ...Base.DataType_Base import Manual, Computed, WindData
from ...Base.Plot_Base import Plot_Base
from matplotlib.ticker import FuncFormatter

class spot_price_base(A_Base, Plot_Base):
    table_english_name = "SpotPrice"
    table_chinese_name = u"现货价格"
    
    def output(self):
        print("SpotPrice")
    
    def get_relevant_df(self, col_list):
        local_col_name_list = spot_price_base.get_all_table_classname()
        col_cls_list = []
        for x in col_list:
            col_cls_name = str(A_Base.get_class_name(x))
            if col_cls_name not in local_col_name_list:
                col_cls_list.append(eval(A_Base.get_table_class_full_variable(x)))
            else:
                col_cls_list.append(eval(col_cls_name))
        ts_list = [x().get_ts() for x in col_cls_list]
        tmp_table_df = pd.concat(ts_list, axis=1).dropna(how="all")
        return tmp_table_df  

    
###########################################################################################################################
""" 国内现货价格 """    

class DouYiDongBeiXianHuoJunJia(spot_price_base, Manual):
    field_name = u"国内现货价格"
    col_name = u"豆一东北现货均价"
    
class DaDouXianHuoJiaGe_WuChang(spot_price_base, Manual):
    field_name = u"国内现货价格"
    col_name = u"大豆现货价格_五常"

class DaDouXianHuoJiaGe_ShangZhi(spot_price_base, Manual):
    field_name = u"国内现货价格"
    col_name = u"大豆现货价格_尚志"

class DaDouXianHuoJiaGe_ACheng(spot_price_base, Manual):
    field_name = u"国内现货价格"
    col_name = u"大豆现货价格_阿城"

class DaDouXianHuoJiaGe_BinXian(spot_price_base, Manual):
    field_name = u"国内现货价格"
    col_name = u"大豆现货价格_宾县"

class DaDouXianHuoJiaGe_BaYan(spot_price_base, Manual):
    field_name = u"国内现货价格"
    col_name = u"大豆现货价格_巴彦"

class DaDouXianHuoJiaGe_QingAn(spot_price_base, Manual):
    field_name = u"国内现货价格"
    col_name = u"大豆现货价格_庆安"

class DaDouXianHuoJiaGe_SuiHua(spot_price_base, Manual):
    field_name = u"国内现货价格"
    col_name = u"大豆现货价格_绥化"

class DaDouXianHuoJiaGe_HaiLun(spot_price_base, Manual):
    field_name = u"国内现货价格"
    col_name = u"大豆现货价格_海伦"

class DaDouXianHuoJiaGe_BeiAn(spot_price_base, Manual):
    field_name = u"国内现货价格"
    col_name = u"大豆现货价格_北安"

class DaDouXianHuoJiaGe_SunWu(spot_price_base, Manual):
    field_name = u"国内现货价格"
    col_name = u"大豆现货价格_孙吴"

class DaDouXianHuoJiaGe_HeiHe(spot_price_base, Manual):
    field_name = u"国内现货价格"
    col_name = u"大豆现货价格_黑河"

class DaDouXianHuoJiaGe_NenJiang(spot_price_base, Manual):
    field_name = u"国内现货价格"
    col_name = u"大豆现货价格_嫩江"

class DaDouXianHuoJiaGe_NaHe(spot_price_base, Manual):
    field_name = u"国内现货价格"
    col_name = u"大豆现货价格_讷河"

class DaDouXianHuoJiaGe_KeShan(spot_price_base, Manual):
    field_name = u"国内现货价格"
    col_name = u"大豆现货价格_克山"

class DaDouXianHuoJiaGe_KeDong(spot_price_base, Manual):
    field_name = u"国内现货价格"
    col_name = u"大豆现货价格_克东"

class DaDouXianHuoJiaGe_BaiQuan(spot_price_base, Manual):
    field_name = u"国内现货价格"
    col_name = u"大豆现货价格_拜泉"

class DaDouXianHuoJiaGe_MuDanJiang(spot_price_base, Manual):
    field_name = u"国内现货价格"
    col_name = u"大豆现货价格_牡丹江"

class DaDouXianHuoJiaGe_MuLeng(spot_price_base, Manual):
    field_name = u"国内现货价格"
    col_name = u"大豆现货价格_穆棱"

class DaDouXianHuoJiaGe_JiXi(spot_price_base, Manual):
    field_name = u"国内现货价格"
    col_name = u"大豆现货价格_鸡西"

class DaDouXianHuoJiaGe_MiShan(spot_price_base, Manual):
    field_name = u"国内现货价格"
    col_name = u"大豆现货价格_密山"

class DaDouXianHuoJiaGe_BoLi(spot_price_base, Manual):
    field_name = u"国内现货价格"
    col_name = u"大豆现货价格_勃利"

class DaDouXianHuoJiaGe_BaoQuanLing(spot_price_base, Manual):
    field_name = u"国内现货价格"
    col_name = u"大豆现货价格_宝泉岭"

class DaDouXianHuoJiaGe_JiaMuSi(spot_price_base, Manual):
    field_name = u"国内现货价格"
    col_name = u"大豆现货价格_佳木斯"

class DaDouXianHuoJiaGe_BaoQing(spot_price_base, Manual):
    field_name = u"国内现货价格"
    col_name = u"大豆现货价格_宝清"

class DaDouXianHuoJiaGe_FuJin(spot_price_base, Manual):
    field_name = u"国内现货价格"
    col_name = u"大豆现货价格_富锦"

class DaDouXianHuoJiaGe_QianJinZhen(spot_price_base, Manual):
    field_name = u"国内现货价格"
    col_name = u"大豆现货价格_前进镇"

class DaDouXianHuoJiaGe_ZhaLanTun(spot_price_base, Manual):
    field_name = u"国内现货价格"
    col_name = u"大豆现货价格_扎兰屯"

class DaDouXianHuoJiaGe_ARongQi(spot_price_base, Manual):
    field_name = u"国内现货价格"
    col_name = u"大豆现货价格_阿荣旗"

class DaDouXianHuoJiaGe_DaYangShu(spot_price_base, Manual):
    field_name = u"国内现货价格"
    col_name = u"大豆现货价格_大杨树"

class DaDouXianHuoJiaGe_JiaoHe(spot_price_base, Manual):
    field_name = u"国内现货价格"
    col_name = u"大豆现货价格_蛟河"

class DaDouXianHuoJiaGe_DunHua(spot_price_base, Manual):
    field_name = u"国内现货价格"
    col_name = u"大豆现货价格_敦化"

class DaDouXianHuoJiaGe_AnTu(spot_price_base, Manual):
    field_name = u"国内现货价格"
    col_name = u"大豆现货价格_安图"

class DaDouXianHuoJiaGe_LongJing(spot_price_base, Manual):
    field_name = u"国内现货价格"
    col_name = u"大豆现货价格_龙井"





if __name__ == "__main__":
    ts = YeHuaQiChuChangJia_JingBoShiHua().get_ts()