# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 10:48:40 2018

@author: 李弘一萌
"""

import pandas as pd
from datetime import datetime
from .I_Base import I_Base
from ...Base.DataType_Base import Manual, Computed, WindData
from ...Base.Plot_Base import Plot_Base
from matplotlib.ticker import FuncFormatter

class sdb_base(I_Base, Plot_Base):
    table_english_name = "SupplyDemandBalance"
    table_chinese_name = u"供需平衡表"
    
    def output(self):
        print(self.table_english_name)
    
    def get_relevant_df(self, col_list):
        local_col_name_list = sdb_base.get_all_table_classname()
        col_cls_list = []
        for x in col_list:
            col_cls_name = str(I_Base.get_class_name(x))
            if col_cls_name not in local_col_name_list:
                col_cls_list.append(eval(I_Base.get_table_class_full_variable(x)))
            else:
                col_cls_list.append(eval(col_cls_name))
        ts_list = [x().get_ts() for x in col_cls_list]
        tmp_table_df = pd.concat(ts_list, axis=1).dropna(how="all")
        return tmp_table_df 



###########################################################################################################################
""" 成交量 """    

class TieKuangShiGangKouXianHuoRiJunChengJiaoLiangHeJi(sdb_base, Manual):
    field_name = u"成交量"
    col_name = u"铁矿石港口现货日均成交量合计"

###########################################################################################################################
""" 港口疏港量 """    

class TieKuangShiRiJunShuGangLiang_45GeGangKouHeJi(sdb_base, Manual):
    field_name = u"港口疏港量"
    col_name = u"铁矿石日均疏港量_45个港口合计"
    

###########################################################################################################################
""" 国内矿产量 """  

class TieKuangShiChanNengLiYongLv_QuanGuo266ZuoKuangShan(sdb_base, Manual):
    field_name = u"国内矿产量"
    col_name = u"铁矿石产能利用率_全国266座矿山"    

class TieKuangShiChanNengLiYongLv_DaXingKuangShan(sdb_base, Manual):
    field_name = u"国内矿产量"
    col_name = u"铁矿石产能利用率_大型矿山"  
    
class TieKuangShiChanNengLiYongLv_ZhongXingKuangShan(sdb_base, Manual):
    field_name = u"国内矿产量"
    col_name = u"铁矿石产能利用率_中型矿山"  
 
class TieKuangShiChanNengLiYongLv_XiaoXingKuangShan(sdb_base, Manual):
    field_name = u"国内矿产量"
    col_name = u"铁矿石产能利用率_小型矿山"  
 
class TieKuangShiChanLiang_TieJingFen_QuanGuo266ZuoKuangShan(sdb_base, Manual):
    field_name = u"国内矿产量"
    col_name = u"铁矿石产量_铁精粉_全国266座矿山"  
 
class TieKuangShiChanLiang_TieJingFen_DaXingKuangShan(sdb_base, Manual):
    field_name = u"国内矿产量"
    col_name = u"铁矿石产量_铁精粉_大型矿山"  
 
class TieKuangShiChanLiang_TieJingFen_ZhongXingKuangShan(sdb_base, Manual):
    field_name = u"国内矿产量"
    col_name = u"铁矿石产量_铁精粉_中型矿山"  
 
class TieKuangShiChanLiang_TieJingFen_XiaoXingKuangShan(sdb_base, Manual):
    field_name = u"国内矿产量"
    col_name = u"铁矿石产量_铁精粉_小型矿山"  
 
class TieKuangShiYuanKuangChanLiang_DangYueZhi(sdb_base, WindData):
    field_name = u"国内矿产量"
    col_name = u"铁矿石原矿产量_当月值" 
    wind_code = "S0027366"
     
###########################################################################################################################
""" 高炉生产 """  

class ShengTieChanLiang_DangYueZhi(sdb_base, WindData):
    field_name = u"高炉生产"
    col_name = u"生铁产量_当月值"    
    wind_code = "S0027370"

###########################################################################################################################
""" 海外矿山发货 """  

class TieKuangShiFaHuoLiang_AoZhou(sdb_base, WindData):
    field_name = u"海外矿山发货"
    col_name = u"铁矿石发货量_澳洲"
    wind_code = "S5708292"
    
class TieKuangShiFaHuoLiang_AoZhouFaZhiZhongGuo(sdb_base, WindData):
    field_name = u"海外矿山发货"
    col_name = u"铁矿石发货量_澳洲发至中国"  
    wind_code = "S5708293"
    
class TieKuangShiLiGangChuanBoShuLiang_AoZhou(sdb_base, Manual):
    field_name = u"海外矿山发货"
    col_name = u"铁矿石离港船舶数量_澳洲"  
    
class TieKuangShiYuJiFaHuoLiang_AoZhou(sdb_base, Manual):
    field_name = u"海外矿山发货"
    col_name = u"铁矿石预计发货量_澳洲"  
    
class TieKuangShiYuJiLiGangChuanBoShuLiang_AoZhou(sdb_base, Manual):
    field_name = u"海外矿山发货"
    col_name = u"铁矿石预计离港船舶数量_澳洲"  
    
class TieKuangShiFaHuoLiang_BaXi(sdb_base, WindData):
    field_name = u"海外矿山发货"
    col_name = u"铁矿石发货量_巴西"  
    wind_code = "S5708280"
    
class TieKuangShiFaZhiZhongGuoHuoLiang_BaXi(sdb_base, Manual):
    field_name = u"海外矿山发货"
    col_name = u"铁矿石发至中国货量_巴西"  
    
class TieKuangShiLiGangChuanBoShuLiang_BaXi(sdb_base, Manual):
    field_name = u"海外矿山发货"
    col_name = u"铁矿石离港船舶数量_巴西"  
    
class TieKuangShiYuJiFaHuoLiang_BaXi(sdb_base, Manual):
    field_name = u"海外矿山发货"
    col_name = u"铁矿石预计发货量_巴西"  
    
class TieKuangShiYuJiLiGangChuanBoShuLiang_BaXi(sdb_base, Manual):
    field_name = u"海外矿山发货"
    col_name = u"铁矿石预计离港船舶数量_巴西"  
    
class TieKuangShiDaoGangLiang_ZhongGuoBeiFang(sdb_base, WindData):
    field_name = u"海外矿山发货"
    col_name = u"铁矿石到港量_中国北方"  
    wind_code = "S5708279"
    
class TieKuangShiChanLiang_LiTuo(sdb_base, Manual):
    field_name = u"海外矿山发货"
    col_name = u"铁矿石产量_力拓"  
    
class TieKuangShiChanLiang_BiHeBiTuo(sdb_base, Manual):
    field_name = u"海外矿山发货"
    col_name = u"铁矿石产量_必和必拓"  
    
class TieKuangShiChanLiang_DanShuiHeGu(sdb_base, Manual):
    field_name = u"海外矿山发货"
    col_name = u"铁矿石产量_淡水河谷"  
    
class TieKuangShiChanLiang_FMG(sdb_base, Manual):
    field_name = u"海外矿山发货"
    col_name = u"铁矿石产量_FMG"  
    
class TieKuangShiChanLiang_YingMeiZiYuan(sdb_base, Manual):
    field_name = u"海外矿山发货"
    col_name = u"铁矿石产量_英美资源(Kumba & Minas-Rio)"  
    
class TieKuangShiChanLiang_CSN(sdb_base, Manual):
    field_name = u"海外矿山发货"
    col_name = u"铁矿石产量_CSN"  
    
class TieKuangShiChanLiang_Atlas(sdb_base, Manual):
    field_name = u"海外矿山发货"
    col_name = u"铁矿石产量_Atlas"  
    
class TieKuangShiChanLiang_NMDC(sdb_base, Manual):
    field_name = u"海外矿山发货"
    col_name = u"铁矿石产量_NMDC"      
    
###########################################################################################################################
""" 进口量 """  

class TieKuangShiJinKouLiang_DangYueZhi(sdb_base, WindData):
    field_name = u"进口量"
    col_name = u"铁矿石进口量_当月值"    
    wind_code = "S0116885"   

class TieKuangShiJinKouLiang_AoDaLiYa(sdb_base, WindData):
    field_name = u"进口量"
    col_name = u"铁矿石进口量_澳大利亚"    
    wind_code = "S0116886"
    
class TieKuangShiJinKouLiang_BaXi(sdb_base, WindData):
    field_name = u"进口量"
    col_name = u"铁矿石进口量_巴西"    
    wind_code = "S0116887"
    
class TieKuangShiJinKouLiang_YinDu(sdb_base, WindData):
    field_name = u"进口量"
    col_name = u"铁矿石进口量_印度"    
    wind_code = "S0116888"
    
class TieKuangShiJinKouLiang_NanFei(sdb_base, WindData):
    field_name = u"进口量"
    col_name = u"铁矿石进口量_南非"    
    wind_code = "S0116889"

if __name__ == "__main__":
    a = PISheHuiKuCun().seasonal_plot()
    
    
    
    
    
    
    
    
    
    