# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 10:48:40 2018

@author: 李弘一萌
"""

import pandas as pd
from datetime import datetime
from .J_Base import J_Base
from . import J_SpotPrice
from ..JM import JM_SpotPrice
from ...Base.DataType_Base import Manual, Computed, WindData
from ...Base.Plot_Base import Plot_Base
from matplotlib.ticker import FuncFormatter

class sdb_base(J_Base, Plot_Base):
    table_english_name = "SupplyDemandBalance"
    table_chinese_name = u"供需平衡表"
    
    def output(self):
        print(self.table_english_name)
    
    def get_relevant_df(self, col_list):
        local_col_name_list = sdb_base.get_all_table_classname()
        col_cls_list = []
        for x in col_list:
            col_cls_name = str(J_Base.get_class_name(x))
            if col_cls_name not in local_col_name_list:
                col_cls_list.append(eval(J_Base.get_table_class_full_variable(x)))
            else:
                col_cls_list.append(eval(col_cls_name))
        ts_list = [x().get_ts() for x in col_cls_list]
        tmp_table_df = pd.concat(ts_list, axis=1).dropna(how="all")
        return tmp_table_df 
    

###########################################################################################################################
""" 产量 """  

class JiaoTanChanLiang_DangYueZhi(sdb_base, WindData):
    field_name = u"产量"
    col_name = u"焦炭产量_当月值"    
    wind_code = "S0026997"
    
class JiaoTanChanLiang_DangYueTongBi(sdb_base, WindData):
    field_name = u"产量"
    col_name = u"焦炭产量_当月同比"    
    wind_code = "S0026998"
    
class JiaoTanChanLiang_LeiJiZhi(sdb_base, WindData):
    field_name = u"产量"
    col_name = u"焦炭产量_累计值"    
    wind_code = "S0026999"
    
class JiaoTanChanLiang_LeiJiTongBi(sdb_base, WindData):
    field_name = u"产量"
    col_name = u"焦炭产量_累计同比"    
    wind_code = "S0027000"
    
    
class JiaoTanChanLiang_ZhongDianGangChangRiJunChanLiang(sdb_base, Manual):
    field_name = u"产量"
    col_name = u"焦炭产量_重点钢厂日均产量"    

class JiaoTanChanLiang_ZhongDianGangChangJiaoTanChanLiang(sdb_base, Manual):
    field_name = u"产量"
    col_name = u"焦炭产量_重点钢厂焦炭产量"    
    
class JiaoTanChanLiang_DuLiJiaoHuaChangRiJunChanLiang(sdb_base, Manual):
    field_name = u"产量"
    col_name = u"焦炭产量_独立焦化厂日均产量"    
    
     
###########################################################################################################################
""" 开工率 """     
    
class DuLiJiaoHuaChangChanNengLiYongLv(sdb_base, Manual):
    field_name = u"开工率"
    col_name = u"独立焦化厂产能利用率"   

class DuLiJiaoHuaChangChanNengLiYongLv_DongBeiDiQu(sdb_base, Manual):
    field_name = u"开工率"
    col_name = u"独立焦化厂产能利用率_东北地区"   

class DuLiJiaoHuaChangChanNengLiYongLv_HuaBeiDiQu(sdb_base, Manual):
    field_name = u"开工率"
    col_name = u"独立焦化厂产能利用率_华北地区"   

class DuLiJiaoHuaChangChanNengLiYongLv_HuaDongDiQu(sdb_base, Manual):
    field_name = u"开工率"
    col_name = u"独立焦化厂产能利用率_华东地区"   

class DuLiJiaoHuaChangChanNengLiYongLv_HuaZhongDiQu(sdb_base, Manual):
    field_name = u"开工率"
    col_name = u"独立焦化厂产能利用率_华中地区"   

class DuLiJiaoHuaChangChanNengLiYongLv_XiBeiDiQu(sdb_base, Manual):
    field_name = u"开工率"
    col_name = u"独立焦化厂产能利用率_西北地区"   

class DuLiJiaoHuaChangChanNengLiYongLv_XiNanDiQu(sdb_base, Manual):
    field_name = u"开工率"
    col_name = u"独立焦化厂产能利用率_西南地区"   

class DuLiJiaoHuaChangChanNengLiYongLv_ChanNeng100YiXia(sdb_base, Manual):
    field_name = u"开工率"
    col_name = u"独立焦化厂产能利用率_产能100以下"   

class DuLiJiaoHuaChangChanNengLiYongLv_ChanNeng100To200(sdb_base, Manual):
    field_name = u"开工率"
    col_name = u"独立焦化厂产能利用率_产能100-200"   

class DuLiJiaoHuaChangChanNengLiYongLv_ChanNeng200YiShang(sdb_base, Manual):
    field_name = u"开工率"
    col_name = u"独立焦化厂产能利用率_产能200以上"   




###########################################################################################################################
""" 出口 """  

class JiaoTanJiBanJiaoTanChuKouShuLiang_DangYueZhi(sdb_base, WindData):
    field_name = u"出口"
    col_name = u"焦炭及半焦炭出口数量_当月值"    
    wind_code = "S0027007"   

###########################################################################################################################
""" 进口 """  

class JiaoTanJiBanJiaoTanJinKouShuLiang_DangYueZhi(sdb_base, WindData):
    field_name = u"进口"
    col_name = u"焦炭及半焦炭进口数量_当月值"    
    wind_code = "S5118227"   
    
###########################################################################################################################
""" 焦化利润 """  

class LianJiaoLiRun_ShanXi(sdb_base, Computed):
    field_name = u"焦化利润"
    col_name = u"炼焦利润_山西"
    def get_ts_whole_progress(self):
        relevant_col_list = [u"一级冶金焦车板价_A<12.5%,S<0.7%,Mt<7%,M25>90%,CSR>60%_吕梁产_山西", u"煤焦油市场价_灰分0.13%_粘度4.0_水分4.0%_吕梁产_山西",
                             u"硫酸铵市场价_N>21%_水分<1%_吕梁产_山西", u"粗苯市场价_密度0.87-0.90_馏出量>93%_吕梁产_山西"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_series_list = [JM_SpotPrice.FeiMeiCheBanJia_ALT10Prct_V24To28Prct_SLT1Dot3Prct_GGT85Prct_GuJiaoChan_ShanXi().get_ts(),
                           JM_SpotPrice.ShouMeiCheBanJia_ALT11Prct_V_14To16Prct_SLT0Dot5Prct_GGT30Prct_M9Prct_ChangZhiChan_ShanXi().get_ts(), 
                           JM_SpotPrice.OneThirdJiaoMeiCheBanJia_ALT10Prct_V31To34Prct_SLT1Prct_GGT85Prct_Y18To22_LvLiangChan_ShanXi().get_ts()]
        tmp_df = pd.concat(tmp_series_list, axis=1, sort=False)
        tmp_total = pd.concat([tmp_total, tmp_df], axis=1)
        tmp_total[self.col_name] = tmp_total[u"一级冶金焦车板价_A<12.5%,S<0.7%,Mt<7%,M25>90%,CSR>60%_吕梁产_山西"] + (tmp_total[u"煤焦油市场价_灰分0.13%_粘度4.0_水分4.0%_吕梁产_山西"] \
                                   * 0.034 + tmp_total[u"硫酸铵市场价_N>21%_水分<1%_吕梁产_山西"] * 0.01 + tmp_total[u"粗苯市场价_密度0.87-0.90_馏出量>93%_吕梁产_山西"] * 0.01) \
                                   - (tmp_total[u"肥煤车板价_A<10%_V24-28%_S<1.3%_G>85%_古交产_山西"] * 0.15 + tmp_total[u"1/3焦煤车板价_A<10%_V:31-34%_S<1%_G>85%_Y18-22_吕梁产_山西"] * 0.5 \
                                   + tmp_total[u"瘦煤车板价_A<11%_V_14-16%_S<0.5%_G>30%_M9%_长治产_山西"] * 0.15) * 1.33 - 130
        return tmp_total


        
if __name__ == "__main__":
    a = PJSheHuiKuCun().seasonal_plot()
    
    
    
    
    
    
    
    
    
    