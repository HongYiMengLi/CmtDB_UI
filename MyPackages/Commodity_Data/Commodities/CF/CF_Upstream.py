# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 10:44:58 2018

@author: 李弘一萌
"""

import pandas as pd
from datetime import datetime
from .CF_Base import CF_Base
from ...Base.DataType_Base import Manual, Computed, WindData
from ...Base.Plot_Base import Plot_Base
from matplotlib.ticker import FuncFormatter

class upstream_base(CF_Base, Plot_Base):
    table_english_name = "Upstream"
    table_chinese_name = u"上游"
#    original_db_filepath = data_path + u"LPP价格数据库.xlsx"
    
    def output(self):
        print("Upstream")
    
    def get_relevant_df(self, col_list):
        local_col_name_list = upstream_base.get_all_table_classname()
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
""" 国内棉花单产 """  

class MianHuaDanChan_QuanGuo_USDA(upstream_base, WindData):
    field_name = u"国内棉花单产"
    col_name = u"棉花单产_全国_USDA"
    wind_code = "S5010981"

class MianHuaDanChan_QuanGuo_GuoJiaTongJiJu(upstream_base, WindData):
    field_name = u"国内棉花单产"
    col_name = u"棉花单产_全国_国家统计局"
    wind_code = "S0031741"
    
class MianHuaDanChan_XinJiang_GuoJiaTongJiJu(upstream_base, WindData):
    field_name = u"国内棉花单产"
    col_name = u"棉花单产_新疆_国家统计局"
    wind_code = "S0038682"

    
###########################################################################################################################
""" 国内棉花生长状况 """  

class MianHuaMiaoQingZhuangKuang_XinJiang_ZhongGuoMianHuaXieHui(upstream_base, Manual):
    field_name = u"国内棉花生长状况"
    col_name = u"棉花苗情状况_新疆_中国棉花协会"

class MianHuaMiaoQingZhuangKuang_HuangHeLiuYu_ZhongGuoMianHuaXieHui(upstream_base, Manual):
    field_name = u"国内棉花生长状况"
    col_name = u"棉花苗情状况_黄河流域_中国棉花协会"

class MianHuaMiaoQingZhuangKuang_ChangJiangLiuYu_ZhongGuoMianHuaXieHui(upstream_base, Manual):
    field_name = u"国内棉花生长状况"
    col_name = u"棉花苗情状况_长江流域_中国棉花协会"

###########################################################################################################################
""" 国内棉花种植面积 """  

class MianHuaYuGuZhongZhiMianJi_QuanGuo_ZhongGuoMianHuaXieHui(upstream_base, Manual):
    field_name = u"国内棉花种植面积"
    col_name = u"棉花预估种植面积_全国_中国棉花协会"

class MianHuaYuGuZhongZhiMianJi_XinJiang_ZhongGuoMianHuaXieHui(upstream_base, Manual):
    field_name = u"国内棉花种植面积"
    col_name = u"棉花预估种植面积_新疆_中国棉花协会"

class MianHuaYuGuZhongZhiMianJi_HuangHeLiuYu_ZhongGuoMianHuaXieHui(upstream_base, Manual):
    field_name = u"国内棉花种植面积"
    col_name = u"棉花预估种植面积_黄河流域_中国棉花协会"

class MianHuaYuGuZhongZhiMianJi_ChangJiangLiuYu_ZhongGuoMianHuaXieHui(upstream_base, Manual):
    field_name = u"国内棉花种植面积"
    col_name = u"棉花预估种植面积_长江流域_中国棉花协会"

class MianHuaZhongZhiMianJi_QuanGuo_GuoJiaTongJiJu(upstream_base, WindData):
    field_name = u"国内棉花种植面积"
    col_name = u"棉花种植面积_全国_国家统计局"
    wind_code = "S0037403"

class MianHuaZhongZhiMianJi_XinJiang_GuoJiaTongJiJu(upstream_base, WindData):
    field_name = u"国内棉花种植面积"
    col_name = u"棉花种植面积_新疆_国家统计局"
    wind_code = "S0037434"
    
class MianHuaBoZhongMianJi_QuanGuo_USDA(upstream_base, WindData):
    field_name = u"国内棉花种植面积"
    col_name = u"棉花播种面积_全国_USDA"
    wind_code = "S0118000"
    
class MianHuaShouHuoMianJi_QuanGuo_USDA(upstream_base, WindData):
    field_name = u"国内棉花种植面积"
    col_name = u"棉花收获面积_全国_USDA"
    wind_code = "S5010979"
    
     
class MianHuaZhongZhiMianJi_NeiDi_GuoJiaTongJiJu(upstream_base, Computed):
    field_name = u"国内棉花种植面积"
    col_name = u"棉花种植面积_内地_国家统计局"  
    def get_ts_whole_progress(self):
        relevant_col_list = [u"棉花种植面积_全国_国家统计局", u"棉花种植面积_新疆_国家统计局"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"棉花种植面积_全国_国家统计局"] - tmp_total[u"棉花种植面积_新疆_国家统计局"]
        return tmp_total
    
    
###########################################################################################################################
""" 美国棉花单产 """ 

class MianHuaDanChanYuGu_MeiGuo_USDA(upstream_base, Manual):
    field_name = u"美国棉花单产"
    col_name = u"棉花单产预估_美国_USDA"
    
###########################################################################################################################
""" 美国棉花面积 """ 

class MianHuaZhongZhiMianJiYuGu_MeiGuo_USDA(upstream_base, Manual):
    field_name = u"美国棉花面积"
    col_name = u"棉花种植面积预估_美国_USDA"    

class MianHuaShouHuoMianJiYuGu_MeiGuo_USDA(upstream_base, Manual):
    field_name = u"美国棉花面积"
    col_name = u"棉花收获面积预估_美国_USDA"

###########################################################################################################################
""" 美国棉花生长状况 """ 

class MeiMianJieXuLv(upstream_base, WindData):
    field_name = u"美国棉花生长状况"
    col_name = u"美棉结絮率"
    wind_code = "S0113814"

class MeiMianTuXuLv(upstream_base, WindData):
    field_name = u"美国棉花生长状况"
    col_name = u"美棉吐絮率"
    wind_code = "S0013815"

class MeiMian_ShengChangZhuangKuangFeiChangBuHao_ZhanBi(upstream_base, WindData):
    field_name = u"美国棉花生长状况"
    col_name = u"美棉_生长状况非常不好_占比"
    wind_code = "S0113809"

class MeiMian_ShengChangZhuangKuangBuHao_ZhanBi(upstream_base, WindData):
    field_name = u"美国棉花生长状况"
    col_name = u"美棉_生长状况不好_占比"
    wind_code = "S0113810"
    
class MeiMian_ShengChangZhuangKuangYiBan_ZhanBi(upstream_base, WindData):
    field_name = u"美国棉花生长状况"
    col_name = u"美棉_生长状况一般_占比"
    wind_code = "S0113811"    
    
class MeiMian_ShengChangZhuangKuangHao_ZhanBi(upstream_base, WindData):
    field_name = u"美国棉花生长状况"
    col_name = u"美棉_生长状况好_占比"
    wind_code = "S0113812"    
    
class MeiMian_ShengChangZhuangKuangFeiChangHao_ZhanBi(upstream_base, WindData):
    field_name = u"美国棉花生长状况"
    col_name = u"美棉_生长状况非常好_占比"
    wind_code = "S0113813"    
    
###########################################################################################################################
""" 美棉上市进度 """ 

class MeiMianCaiZhaiJinDu(upstream_base, WindData):
    field_name = u"美棉上市进度"
    col_name = u"美棉采摘进度"
    wind_code = "S0113816"    
    
###########################################################################################################################
""" 棉花进口价格 """     
    
class JinKouMianHuaJiaGe_YinDu_Shankar_6_DaoGangJia(upstream_base, WindData):
    field_name = u"棉花进口价格"
    col_name = u"进口棉花价格_印度_Shankar-6_到港价"
    wind_code = "S5016883"      

class JinKouMianHuaJiaGe_YinDu_Shankar_6_1PrctGangKouTiHuoJia(upstream_base, WindData):
    field_name = u"棉花进口价格"
    col_name = u"进口棉花价格_印度_Shankar-6_1%港口提货价"
    wind_code = "S5016887"   

class JinKouMianHuaJiaGe_YinDu_Shankar_6_HuaZhunShuiGangKouTiHuoJia(upstream_base, WindData):
    field_name = u"棉花进口价格"
    col_name = u"进口棉花价格_印度_Shankar-6_滑准税港口提货价"
    wind_code = "S5016891"       
    
class JinKouMianHuaJiaGe_MeiGuo_EMOT_M_DaoGangJia(upstream_base, WindData):
    field_name = u"棉花进口价格"
    col_name = u"进口棉花价格_美国_EMOT_M_到港价"
    wind_code = "S5016881"       
    
class JinKouMianHuaJiaGe_MeiGuo_EMOT_M_1PrctGangKouTiHuoJia(upstream_base, WindData):
    field_name = u"棉花进口价格"
    col_name = u"进口棉花价格_美国_EMOT_M_1%港口提货价"
    wind_code = "S5016885"       
    
class JinKouMianHuaJiaGe_MeiGuo_EMOT_M_HuaZhunShuiGangKouTiHuoJia(upstream_base, WindData):
    field_name = u"棉花进口价格"
    col_name = u"进口棉花价格_美国_EMOT_M_滑准税港口提货价"
    wind_code = "S5016889"   

class JinKouMianHuaJiaGeZhiShu_FC_Index_M_DaoGangJia(upstream_base, WindData):
    field_name = u"棉花进口价格"
    col_name = u"进口棉花价格指数(FC_Index)_M_到港价"
    wind_code = "S5016833"   

class JinKouMianHuaJiaGeZhiShu_FC_Index_M_1PrctTiHuoJia(upstream_base, WindData):
    field_name = u"棉花进口价格"
    col_name = u"进口棉花价格指数(FC_Index)_M_1%提货价"
    wind_code = "S5016836"   

class JinKouMianHuaJiaGeZhiShu_FC_Index_M_HuaZhunShuiTiHuoJia(upstream_base, WindData):
    field_name = u"棉花进口价格"
    col_name = u"进口棉花价格指数(FC_Index)_M_滑准税提货价"
    wind_code = "S5016839"   
     
###########################################################################################################################
""" 棉花指数 """ 

class ZhongGuoMianHua_328JiaGeZhiShu(upstream_base, WindData):
    field_name = u"棉花指数"
    col_name = u"中国棉花328价格指数"
    wind_code = "S0031714"      
 
###########################################################################################################################
""" 棉籽收购价 """ 

class MianZiXianHuoJunJia(upstream_base, WindData):
    field_name = u"棉籽收购价"
    col_name = u"棉籽现货均价"
    wind_code = "S5005944"      
    
class MianZiShouGouJia_WuLuMuQi(upstream_base, WindData):
    field_name = u"棉籽收购价"
    col_name = u"棉籽收购价_乌鲁木齐"
    wind_code = "S5005934"     
    
###########################################################################################################################
""" 替代品 """ 

class DiDuanJiaGe_1Dot4DZhiFangDiDuan(upstream_base, Manual):
    field_name = u"替代品"
    col_name = u"涤短价格_1.4D直纺涤短"    

###########################################################################################################################
""" 新棉公检进度 """ 

class MianHuaGongJianJinDu(upstream_base, Manual):
    field_name = u"新棉公检进度"
    col_name = u"棉花公检进度"    

class MianHuaGongJianJinDu_XinJiang(upstream_base, Manual):
    field_name = u"新棉公检进度"
    col_name = u"棉花公检进度_新疆" 

class MianHuaGongJianJinDu_NeiDi(upstream_base, Manual):
    field_name = u"新棉公检进度"
    col_name = u"棉花公检进度_内地" 

class MianHuaGongJianJinDu_YueDuLeiJi(upstream_base, Computed):
    field_name = u"新棉公检进度"
    col_name = u"棉花公检进度_月度累计"
    def get_ts_whole_progress(self):
        relevant_col_list = [u"棉花公检进度"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        
        tmp_ts = tmp_total[u"棉花公检进度"]
        cumsum_value_list = []
        for i in range(len(tmp_ts)):
            tmp_value = tmp_ts.iloc[i]
            if tmp_ts.index[i].month == 9:
                cumsum_value_list.append(tmp_value)
            else:
                if len(cumsum_value_list) == 0:
                    tmp_cumsum = 0
                else:
                    tmp_cumsum = cumsum_value_list[-1]
                cumsum_value_list.append(tmp_cumsum + tmp_value)
        tmp_total[self.col_name] = cumsum_value_list
        return tmp_total  
    
###########################################################################################################################
""" 籽棉收购价 """ 

class ZiMianShouGouJia_3128B_QuanGuoJunJia(upstream_base, WindData):
    field_name = u"籽棉收购价"
    col_name = u"籽棉收购价_3128B_全国均价"
    wind_code = "S5028360"      
    
class ZiMianShouGouJia_3128B_NeiDiJunJia(upstream_base, WindData):
    field_name = u"籽棉收购价"
    col_name = u"籽棉收购价_3128B_内地均价"
    wind_code = "S5028365"  

class ZiMianShouGouJia_3128B_XinJiangJunJia(upstream_base, WindData):
    field_name = u"籽棉收购价"
    col_name = u"籽棉收购价_3128B_新疆均价"
    wind_code = "S6939206"  




    
    
if __name__ == "__main__":
    df = MianHuaGongJianJinDu_YueDuLeiJi().get_ts()    
    
    
    
    
    
    
    
    
    
    
    
    
    
    