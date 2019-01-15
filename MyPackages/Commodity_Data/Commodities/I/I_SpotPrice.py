# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 16:35:12 2018

@author: 李弘一萌
"""

import pandas as pd
from datetime import datetime
from .I_Base import I_Base
from ...Base.DataType_Base import Manual, Computed, WindData
from ...Base.Plot_Base import Plot_Base
from matplotlib.ticker import FuncFormatter

class spot_price_base(I_Base, Plot_Base):
    table_english_name = "SpotPrice"
    table_chinese_name = u"现货价格"
#    original_db_filepath = data_path + u"LPP价格数据库.xlsx"
    
    def output(self):
        print("SpotPrice")
    
    def get_relevant_df(self, col_list):
        local_col_name_list = spot_price_base.get_all_table_classname()
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
""" 废钢价格 """    

class FeiGangBuHanShuiShiChangJia_6_8mm_TangShan(spot_price_base, WindData):
    field_name = u"出口现货报价"
    col_name = u"废钢不含税市场价_6-8mm_唐山"
    wind_code = "S5700017"

###########################################################################################################################
""" 港口现货价格 """    

class TieKuangCheBanJia_AoDaLiYaJinBuBaFen61Pct_QingDaoGang(spot_price_base, Manual):
    field_name = u"港口现货价格"
    col_name = u"铁矿车板价_澳大利亚金布巴粉61%_青岛港"
    
class GuoChanTieJingKuangHanShuiJia_62PctPinWei_GanJi(spot_price_base, WindData):
    field_name = u"港口现货价格"
    col_name = u"国产铁精矿含税价_62%品位_干基"
    wind_code = "S5704664"   
     
class TieKuangCheBanJia_BaXiKaLaJiaSiFen65Pct_QingDaoGang(spot_price_base, WindData):
    field_name = u"港口现货价格"
    col_name = u"铁矿车板价_巴西卡拉加斯粉65%_青岛港"
    wind_code = "S0202726" 
    
class TieKuangCheBanJia_AoDaLiYaYangDiFen58Pct_QingDaoGang(spot_price_base, WindData):
    field_name = u"港口现货价格"
    col_name = u"铁矿车板价_澳大利亚杨迪粉58%_青岛港"
    wind_code = "S0110155"       
    
class TieKuangCheBanJia_AoDaLiYaPBFenKuang61Dot5Pct_QingDaoGang(spot_price_base, WindData):
    field_name = u"港口现货价格"
    col_name = u"铁矿车板价_澳大利亚PB粉矿61.5%_青岛港"
    wind_code = "S0174655"       
    
class TieKuangCheBanJia_AoDaLiYaPBKuaiKuang62Dot5Pct_QingDaoGang(spot_price_base, WindData):
    field_name = u"港口现货价格"
    col_name = u"铁矿车板价_澳大利亚PB块矿62.5%_青岛港"
    wind_code = "S0174656"       
    
class TieKuangCheBanJia_AoDaLiYaLuoBuHeFen57Pct_QingDaoGang(spot_price_base, WindData):
    field_name = u"港口现货价格"
    col_name = u"铁矿车板价_澳大利亚罗布河粉57%_青岛港"
    wind_code = "S0183609"       
    
class TieKuangCheBanJia_YinDuFenKuang62Pct_LianYunGang(spot_price_base, WindData):
    field_name = u"港口现货价格"
    col_name = u"铁矿车板价_印度粉矿62%_连云港"
    wind_code = "S0110167" 

class TieKuangCheBanJia_AoDaLiYaPBFenKuang61Dot5Pct_LianYunGang(spot_price_base, WindData):
    field_name = u"港口现货价格"
    col_name = u"铁矿车板价_澳大利亚PB粉矿61.5%_连云港"
    wind_code = "S0110172" 

class TieKuangCheBanJia_AoDaLiYaPBKuaiKuang62Dot5Pct_LianYunGang(spot_price_base, WindData):
    field_name = u"港口现货价格"
    col_name = u"铁矿车板价_澳大利亚PB块矿62.5%_连云港"
    wind_code = "S0110173" 

class TieKuangCheBanJia_AoDaLiYaYangDiFen58Pct_LianYunGang(spot_price_base, WindData):
    field_name = u"港口现货价格"
    col_name = u"铁矿车板价_澳大利亚杨迪粉58%_连云港"
    wind_code = "S0202729" 

class TieKuangCheBanJia_BaXiKaLaJiaSiFen65Pct_LianYunGang(spot_price_base, WindData):
    field_name = u"港口现货价格"
    col_name = u"铁矿车板价_巴西卡拉加斯粉65%_连云港"
    wind_code = "S0202731" 

class TieKuangCheBanJia_YinDuFenKuang62Pct_RiZhaoGang(spot_price_base, WindData):
    field_name = u"港口现货价格"
    col_name = u"铁矿车板价_印度粉矿62%_日照港"
    wind_code = "S0110177" 

class TieKuangCheBanJia_AoDaLiYaPBFenKuang61Dot5Pct_RiZhaoGang(spot_price_base, WindData):
    field_name = u"港口现货价格"
    col_name = u"铁矿车板价_澳大利亚PB粉矿61.5%_日照港"
    wind_code = "S0110182" 

class TieKuangCheBanJia_AoDaLiYaPBKuaiKuang62Dot5Pct_RiZhaoGang(spot_price_base, WindData):
    field_name = u"港口现货价格"
    col_name = u"铁矿车板价_澳大利亚PB块矿62.5%_日照港"
    wind_code = "S0110183" 

class TieKuangCheBanJia_AoDaLiYaNiuManFenKuang62Pct_RiZhaoGang(spot_price_base, WindData):
    field_name = u"港口现货价格"
    col_name = u"铁矿车板价_澳大利亚纽曼粉矿62%_日照港"
    wind_code = "S0110184"     
    
class TieKuangCheBanJia_AoDaLiYaMaiKeFen61Pct_RiZhaoGang(spot_price_base, WindData):
    field_name = u"港口现货价格"
    col_name = u"铁矿车板价_澳大利亚麦克粉61%_日照港"
    wind_code = "S0202732"   

class TieKuangCheBanJia_AoDaLiYaYangDiFen58Pct_RiZhaoGang(spot_price_base, WindData):
    field_name = u"港口现货价格"
    col_name = u"铁矿车板价_澳大利亚杨迪粉58%_日照港"
    wind_code = "S0202733"   

class TieKuangCheBanJia_AoDaLiYaLuoBuHeFen57Pct_RiZhaoGang(spot_price_base, WindData):
    field_name = u"港口现货价格"
    col_name = u"铁矿车板价_澳大利亚罗布河粉57%_日照港"
    wind_code = "S0202734"   

class TieKuangCheBanJia_AoDaLiYaPBFen61Dot5Pct_JingTangGang(spot_price_base, WindData):
    field_name = u"港口现货价格"
    col_name = u"铁矿车板价_澳大利亚PB粉61.5%_京唐港"
    wind_code = "S0183606"   

class TieKuangCheBanJia_AoDaLiYaPBKuai62Dot5Pct_JingTangGang(spot_price_base, WindData):
    field_name = u"港口现货价格"
    col_name = u"铁矿车板价_澳大利亚PB块62.5%_京唐港"
    wind_code = "S0202753"   

class TieKuangCheBanJia_AoDaLiYaMaiKeFen61Pct_JingTangGang(spot_price_base, WindData):
    field_name = u"港口现货价格"
    col_name = u"铁矿车板价_澳大利亚麦克粉61%_京唐港"
    wind_code = "S0202754"   

class TieKuangCheBanJia_AoDaLiYaYangDiFen58Pct_JingTangGang(spot_price_base, WindData):
    field_name = u"港口现货价格"
    col_name = u"铁矿车板价_澳大利亚杨迪粉58%_京唐港"
    wind_code = "S0202755"   

class TieKuangCheBanJia_BaXiKaLaJiaSiFen65Pct_JingTangGang(spot_price_base, WindData):
    field_name = u"港口现货价格"
    col_name = u"铁矿车板价_巴西卡拉加斯粉65%_京唐港"
    wind_code = "S0202760"   

class TieKuangCheBanJia_AoDaLiYaPBFenKuang61Pct_ZhanJiangGang(spot_price_base, WindData):
    field_name = u"港口现货价格"
    col_name = u"铁矿车板价_澳大利亚PB粉矿61%_湛江港"
    wind_code = "S5707562"       
    
class TieKuangCheBanJia_AoDaLiYaPBFenKuang61Pct_JiangYinGang(spot_price_base, WindData):
    field_name = u"港口现货价格"
    col_name = u"铁矿车板价_澳大利亚PB粉矿61%_江阴港"
    wind_code = "S5707552"
    
class TieKuangCheBanJia_AoDaLiYaPBFenKuang61Pct_TaiCangGang(spot_price_base, WindData):
    field_name = u"港口现货价格"
    col_name = u"铁矿车板价_澳大利亚PB粉矿61%_太仓港"
    wind_code = "S5707546"
    
class TieKuangCheBanJia_AoDaLiYaPBFenKuang61Pct_NanTongGang(spot_price_base, WindData):
    field_name = u"港口现货价格"
    col_name = u"铁矿车板价_澳大利亚PB粉矿61%_南通港"
    wind_code = "S5707534"
    
class TieKuangCheBanJia_AoDaLiYaPBFenKuang61Pct_CaoFeiDianGang(spot_price_base, WindData):
    field_name = u"港口现货价格"
    col_name = u"铁矿车板价_澳大利亚PB粉矿61%_曹妃甸港"
    wind_code = "S5707573"
    
###########################################################################################################################
""" 外盘价格 """    

class TieKuangShiJieSuanJia_XinJiaoSuoDiaoQi_DangYue(spot_price_base, WindData):
    field_name = u"外盘价格"
    col_name = u"铁矿石结算价_新交所掉期_当月"
    wind_code = "S5700062"
    
class TieKuangShiJieSuanJia_XinJiaoSuoDiaoQi_1GeYue(spot_price_base, WindData):
    field_name = u"外盘价格"
    col_name = u"铁矿石结算价_新交所掉期_1个月"
    wind_code = "S5708142"

class TieKuangShiJieSuanJia_XinJiaoSuoDiaoQi_2GeYue(spot_price_base, WindData):
    field_name = u"外盘价格"
    col_name = u"铁矿石结算价_新交所掉期_2个月"
    wind_code = "S5708143"

class TieKuangShiJieSuanJia_XinJiaoSuoDiaoQi_3GeYue(spot_price_base, WindData):
    field_name = u"外盘价格"
    col_name = u"铁矿石结算价_新交所掉期_3个月"
    wind_code = "S5708144"

class TieKuangShiJieSuanJia_XinJiaoSuoDiaoQi_4GeYue(spot_price_base, WindData):
    field_name = u"外盘价格"
    col_name = u"铁矿石结算价_新交所掉期_4个月"
    wind_code = "S5708145"

class TieKuangShiJieSuanJia_XinJiaoSuoDiaoQi_5GeYue(spot_price_base, WindData):
    field_name = u"外盘价格"
    col_name = u"铁矿石结算价_新交所掉期_5个月"
    wind_code = "S5708146"

class TieKuangShiJieSuanJia_XinJiaoSuoDiaoQi_6GeYue(spot_price_base, WindData):
    field_name = u"外盘价格"
    col_name = u"铁矿石结算价_新交所掉期_6个月"
    wind_code = "S5708147"

class TieKuangShiJieSuanJia_XinJiaoSuoDiaoQi_7GeYue(spot_price_base, WindData):
    field_name = u"外盘价格"
    col_name = u"铁矿石结算价_新交所掉期_7个月"
    wind_code = "S5708148"

class TieKuangShiJieSuanJia_XinJiaoSuoDiaoQi_8GeYue(spot_price_base, WindData):
    field_name = u"外盘价格"
    col_name = u"铁矿石结算价_新交所掉期_8个月"
    wind_code = "S5708149"

class TieKuangShiJieSuanJia_XinJiaoSuoDiaoQi_9GeYue(spot_price_base, WindData):
    field_name = u"外盘价格"
    col_name = u"铁矿石结算价_新交所掉期_9个月"
    wind_code = "S5708150"    
    
class TieKuangShiJieSuanJia_XinJiaoSuoDiaoQi_10GeYue(spot_price_base, WindData):
    field_name = u"外盘价格"
    col_name = u"铁矿石结算价_新交所掉期_10个月"
    wind_code = "S5708151"

class TieKuangShiJieSuanJia_XinJiaoSuoDiaoQi_11GeYue(spot_price_base, WindData):
    field_name = u"外盘价格"
    col_name = u"铁矿石结算价_新交所掉期_11个月"
    wind_code = "S5708152"

class TieKuangShiJieSuanJia_XinJiaoSuoDiaoQi_12GeYue(spot_price_base, WindData):
    field_name = u"外盘价格"
    col_name = u"铁矿石结算价_新交所掉期_12个月"
    wind_code = "S5708153"    
    
    
    
    
    
    
    
    

if __name__ == "__main__":
    ts = PIXianHuoJiaGe_HuaDong().get_ts()