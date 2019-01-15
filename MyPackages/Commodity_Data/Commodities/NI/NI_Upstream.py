# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 10:44:58 2018

@author: 李弘一萌
"""

import pandas as pd
from datetime import datetime
from .NI_Base import NI_Base
from ...Base.DataType_Base import Manual, Computed, WindData
from ...Base.Plot_Base import Plot_Base
from matplotlib.ticker import FuncFormatter

class upstream_base(NI_Base, Plot_Base):
    table_english_name = "Upstream"
    table_chinese_name = u"上游"
#    original_db_filepath = data_path + u"LPP价格数据库.xlsx"
    
    def output(self):
        print("Upstream")
    
    def get_relevant_df(self, col_list):
        local_col_name_list = upstream_base.get_all_table_classname()
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
""" 镍矿价格 """  
     

class FeiLvBinHongTuNieKuangJiaGe1Dot5Prct_CIF(upstream_base, Manual):
    field_name = u"镍矿价格"
    col_name = u"菲律宾红土镍矿价格1.5%_CIF"
    
class YinNiHongTuNieKuang1Dot65PrctJiaGe_FOB(upstream_base, Manual):
    field_name = u"镍矿价格"
    col_name = u"印尼红土镍矿1.65%价格_FOB"
    
class FeiLvBinNieKuangJiaGe_Ni_0Dot9To1Dot1Fe_48To50Prct_HuaBei(upstream_base, WindData):
    field_name = u"镍矿价格"
    col_name = u"菲律宾镍矿价格_Ni_0.9-1.1Fe_48-50%_华北"
    wind_code = "S5705523"
    
class FeiLvBinNieKuangJiaGe_Ni_0Dot9To1Dot1Fe_48To50Prct_HuaDong(upstream_base, WindData):
    field_name = u"镍矿价格"
    col_name = u"菲律宾镍矿价格_Ni_0.9-1.1Fe_48-50%_华东"
    wind_code = "S5705524"
    
class FeiLvBinNieKuangJiaGe_Ni_0Dot9To1Dot1Fe_48To50Prct_HuaNan(upstream_base, WindData):
    field_name = u"镍矿价格"
    col_name = u"菲律宾镍矿价格_Ni_0.9-1.1Fe_48-50%_华南"
    wind_code = "S5705525"
    
class FeiLvBinNieKuangJiaGe_Ni_1Dot4To1Dot5Fe_30To35Prct_HuaBei(upstream_base, WindData):
    field_name = u"镍矿价格"
    col_name = u"菲律宾镍矿价格_Ni_1.4-1.5Fe_30-35%_华北"
    wind_code = "S5705526"
    
class FeiLvBinNieKuangJiaGe_Ni_1Dot4To1Dot5Fe_30To35Prct_HuaNan(upstream_base, WindData):
    field_name = u"镍矿价格"
    col_name = u"菲律宾镍矿价格_Ni_1.4-1.5Fe_30-35%_华南"
    wind_code = "S5705528"
    
class FeiLvBinNieKuangJiaGe_Ni_1Dot5To1Dot6Fe_25To30Prct_HuaBei(upstream_base, WindData):
    field_name = u"镍矿价格"
    col_name = u"菲律宾镍矿价格_Ni_1.5-1.6Fe_25-30%_华北"
    wind_code = "S5705529"
    
class FeiLvBinNieKuangJiaGe_Ni_1Dot5To1Dot6Fe_25To30Prct_HuaNan(upstream_base, WindData):
    field_name = u"镍矿价格"
    col_name = u"菲律宾镍矿价格_Ni_1.5-1.6Fe_25-30%_华南"
    wind_code = "S5705531"
    
class YinNiNieKuangJiaGe_Ni_1Dot6To1Dot7Fe_20To25Prct_HuaBei(upstream_base, WindData):
    field_name = u"镍矿价格"
    col_name = u"印尼镍矿价格_Ni_1.6-1.7Fe_20-25%_华北"
    wind_code = "S5705532"
    
class YinNiNieKuangJiaGe_Ni_1Dot6To1Dot7Fe_20To25Prct_HuaNan(upstream_base, WindData):
    field_name = u"镍矿价格"
    col_name = u"印尼镍矿价格_Ni_1.6-1.7Fe_20-25%_华南"
    wind_code = "S5705534"
    
class NieKuangCDFI_ChaoLingBianXingChuan_FeiLvBinSuLiGao_RiZhao(upstream_base, WindData):
    field_name = u"镍矿价格"
    col_name = u"镍矿CDFI_超灵便型船_菲律宾苏里高_日照"
    wind_code = "S0176232"
    
    
    
    
    
    
    
###########################################################################################################################
""" 镍矿进口量 """  

class NieKuangShaJiJingKuangJinKouShuLiang_FeiLvBin_LeiJiZhi(upstream_base, WindData):
    field_name = u"镍矿进口量"
    col_name = u"镍矿砂及精矿进口数量_菲律宾_累计值"
    wind_code = "S0116607"


class NieKuangShaJiJingKuangJinKouShuLiang_YinDuNiXiYa_LeiJiZhi(upstream_base, WindData):
    field_name = u"镍矿进口量"
    col_name = u"镍矿砂及精矿进口数量_印度尼西亚_累计值"
    wind_code = "S0116608"
    

class NieKuangShaJiJingKuangJinKouShuLiang_AoDaLiYa_LeiJiZhi(upstream_base, WindData):
    field_name = u"镍矿进口量"
    col_name = u"镍矿砂及精矿进口数量_澳大利亚_累计值"
    wind_code = "S0116609"

class NieKuangShaJiJingKuangJinKouShuLiang_ELuoSi_LeiJiZhi(upstream_base, WindData):
    field_name = u"镍矿进口量"
    col_name = u"镍矿砂及精矿进口数量_俄罗斯_累计值"
    wind_code = "S0116610"
    
class NieKuangShaJiJingKuangJinKouShuLiang_LeiJiZhi(upstream_base, WindData):
    field_name = u"镍矿进口量"
    col_name = u"镍矿砂及精矿进口数量_累计值"
    wind_code = "S0116269"

    
###########################################################################################################################
""" 镍矿库存 """   

class NieKuangGangKouKuCunHeJi(upstream_base, WindData):
    field_name = u"镍矿库存"
    col_name = u"镍矿港口库存合计"
    wind_code = "S5708486"

    
class NieKuangKuCun_TianJinGang(upstream_base, WindData):
    field_name = u"镍矿库存"
    col_name = u"镍矿库存_天津港"
    wind_code = "S5708477"

    
class NieKuangKuCun_LianYunGang(upstream_base, WindData):
    field_name = u"镍矿库存"
    col_name = u"镍矿库存_连云港"
    wind_code = "S5708478"

class NieKuangKuCun_RiZhaoGang(upstream_base, WindData):
    field_name = u"镍矿库存"
    col_name = u"镍矿库存_日照港"
    wind_code = "S5708479"

    
class NieKuangKuCun_LanShanGang(upstream_base, WindData):
    field_name = u"镍矿库存"
    col_name = u"镍矿库存_岚山港"
    wind_code = "S5708480"

    
class NieKuangKuCun_FangChengGang(upstream_base, WindData):
    field_name = u"镍矿库存"
    col_name = u"镍矿库存_防城港"
    wind_code = "S5708481" 

class NieKuangKuCun_YingKouGang(upstream_base, WindData):
    field_name = u"镍矿库存"
    col_name = u"镍矿库存_营口港"
    wind_code = "S5708482"

    
class NieKuangKuCun_JingTangGang(upstream_base, WindData):
    field_name = u"镍矿库存"
    col_name = u"镍矿库存_京唐港"
    wind_code = "S5708483"

    
class NieKuangKuCun_CaoFeiDianGang(upstream_base, WindData):
    field_name = u"镍矿库存"
    col_name = u"镍矿库存_曹妃甸港"
    wind_code = "S5708484"    

class NieKuangKuCun_TieShanGang(upstream_base, WindData):
    field_name = u"镍矿库存"
    col_name = u"镍矿库存_铁山港"
    wind_code = "S5708485"   

###########################################################################################################################
""" 镍矿消费量 """   

class NieKuangBiaoGuanXiaoFeiLiang_QuanGuo_DangYueZhi(upstream_base, WindData):
    field_name = u"镍矿消费量"
    col_name = u"镍矿表观消费量_全国_当月值"
    wind_code = "S5708454"

class NieKuangBiaoGuanXiaoFeiLiang_LiaoNing_DangYueZhi(upstream_base, WindData):
    field_name = u"镍矿消费量"
    col_name = u"镍矿表观消费量_辽宁_当月值"
    wind_code = "S5708445"

class NieKuangBiaoGuanXiaoFeiLiang_JiangSu_DangYueZhi(upstream_base, WindData):
    field_name = u"镍矿消费量"
    col_name = u"镍矿表观消费量_江苏_当月值"
    wind_code = "S5708447"

class NieKuangBiaoGuanXiaoFeiLiang_NeiMeng_DangYueZhi(upstream_base, WindData):
    field_name = u"镍矿消费量"
    col_name = u"镍矿表观消费量_内蒙_当月值"
    wind_code = "S5708451"

class NieKuangBiaoGuanXiaoFeiLiang_ShanDong_DangYueZhi(upstream_base, WindData):
    field_name = u"镍矿消费量"
    col_name = u"镍矿表观消费量_山东_当月值"
    wind_code = "S5708452"

class NieKuangBiaoGuanXiaoFeiLiang_QiTa_DangYueZhi(upstream_base, WindData):
    field_name = u"镍矿消费量"
    col_name = u"镍矿表观消费量_其他_当月值"
    wind_code = "S5708453"









    
if __name__ == "__main__":
    df = PNIXianHuoJiaGongFei().seasonal_plot()    
    
    
    
    
    
    
    
    
    
    
    
    
    
    