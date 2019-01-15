# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 10:44:58 2018

@author: 李弘一萌
"""

import pandas as pd
from datetime import datetime
from .AL_Base import AL_Base
from . import AL_Macro
from ...Base.DataType_Base import Manual, Computed, WindData
from ...Base.Plot_Base import Plot_Base
from matplotlib.ticker import FuncFormatter

class upstream_base(AL_Base, Plot_Base):
    table_english_name = "Upstream"
    table_chinese_name = u"上游"
#    original_db_filepath = data_path + u"LPP价格数据库.xlsx"
    
    def output(self):
        print("Upstream")
    
    def get_relevant_df(self, col_list):
        local_col_name_list = upstream_base.get_all_table_classname()
        col_cls_list = []
        for x in col_list:
            col_cls_name = str(AL_Base.get_class_name(x))
            if col_cls_name not in local_col_name_list:
                col_cls_list.append(eval(AL_Base.get_table_class_full_variable(x)))
            else:
                col_cls_list.append(eval(col_cls_name))
        ts_list = [x().get_ts() for x in col_cls_list]
        tmp_table_df = pd.concat(ts_list, axis=1).dropna(how="all")
        return tmp_table_df
    
###########################################################################################################################
""" 电解铝辅料价格 """  
     
class YuBeiYangJiShiChangJia_HanShui_XiNanDiQu(upstream_base, WindData):
    field_name = u"电解铝辅料价格"
    col_name = u"预焙阳极(电解铝用辅料)市场价(含税)_西南地区"
    wind_code = "S5418109"
    
class YuBeiYangJiShiChangJia_HanShui_XiBeiDiQu(upstream_base, WindData):
    field_name = u"电解铝辅料价格"
    col_name = u"预焙阳极(电解铝用辅料)市场价(含税)_西北地区"
    wind_code = "S5418110"
    
class GanFaFuHuaLvShiChangJia_HanShui(upstream_base, WindData):
    field_name = u"电解铝辅料价格"
    col_name = u"干法氟化铝(电解铝用辅料)市场价(含税)"
    wind_code = "S5418112"
    
class BingJingShiShiChangJia_HanShui(upstream_base, WindData):
    field_name = u"电解铝辅料价格"
    col_name = u"冰晶石(电解铝用辅料)市场价(含税)"
    wind_code = "S5418111"
    
    
###########################################################################################################################
""" 电解铝辅料市场整理 """  

class ZhongGuoYuBeiYangJiXinZengChanNengLieBiao_2018To2019Nian(upstream_base, Manual):
    field_name = u"电解铝辅料市场整理"
    col_name = u"中国预焙阳极新增产能列表_2018-2019年"
    
###########################################################################################################################
""" 废铝价格 """  

class FeiLvXianPingJunJia_BuHanShui_ShanDongJiNan(upstream_base, WindData):
    field_name = u"废铝价格"
    col_name = u"废铝线平均价(不含税)_山东济南"
    wind_code = "S5808110"


class FeiLvXianPingJunJia_BuHanShui_FeiLvXian_HeBei(upstream_base, WindData):
    field_name = u"废铝价格"
    col_name = u"废铝线平均价(不含税)_废铝线_河北"
    wind_code = "S5808104"
    

class FeiLvJinKouPingJunDanJia_FeiLv_DangYueZhi(upstream_base, WindData):
    field_name = u"废铝价格"
    col_name = u"废铝进口平均单价_废铝_当月值"
    wind_code = "S0117155"


###########################################################################################################################
""" 废铝进出口 """   


class FeiLvJinKouZiGeGuoShuJu(upstream_base, Manual):
    field_name = u"废铝进出口"
    col_name = u"废铝进口自各国数据"

class FeiLvChuKouZhiGeGuoShuJu(upstream_base, Manual):
    field_name = u"废铝进出口"
    col_name = u"废铝出口至各国数据"

class FeiLvJinKouShuLiang_LeiJiZhi(upstream_base, WindData):
    field_name = u"废铝进出口"
    col_name = u"废铝进口数量_累计值"
    wind_code = "S0027655"
    
class FeiLvJinKouShuLiang_LeiJiTongBi(upstream_base, WindData):
    field_name = u"废铝进出口"
    col_name = u"废铝进口数量_累计同比"
    wind_code = "S0027656"

class FeiLvJinKouShuLiang_DangYueZhi(upstream_base, WindData):
    field_name = u"废铝进出口"
    col_name = u"废铝进口数量_当月值"
    wind_code = "S0027654"    



    


###########################################################################################################################
""" 铝土矿供应 """   

class LvTuKuangJiChuChuLiang(upstream_base, WindData):
    field_name = u"铝土矿供应"
    col_name = u"铝土矿基础储量"
    wind_code = "S0029619"

class LvTuKuangChanLiang_ZhongGuo(upstream_base, WindData):
    field_name = u"铝土矿供应"
    col_name = u"铝土矿产量_中国"
    wind_code = "S5800320"

class LvTuKuangChanLiang_QuanQiu(upstream_base, WindData):
    field_name = u"铝土矿供应"
    col_name = u"铝土矿产量_全球"
    wind_code = "S5800324"

###########################################################################################################################
""" 铝土矿进出口 """   

class LvTuKuangChuKouZhiGeGuoShuJu(upstream_base, Manual):
    field_name = u"铝土矿进出口"
    col_name = u"铝土矿出口至各国数据"
    
class LvTuKuangJinKouShuLiang_LeiJiZhi(upstream_base, WindData):
    field_name = u"铝土矿进出口"
    col_name = u"铝土矿进口数量_累计值"
    wind_code = "S0116255"

class LvTuKuangJinKouShuLiang_JiNeiYa_DangYueZhi(upstream_base, WindData):
    field_name = u"铝土矿进出口"
    col_name = u"铝土矿进口数量_几内亚_当月值"
    wind_code = "S0255649"

class LvTuKuangJinKouShuLiang_DangYueZhi(upstream_base, WindData):
    field_name = u"铝土矿进出口"
    col_name = u"铝土矿进口数量_当月值"
    wind_code = "S0116254"

class LvTuKuangJinKouShuLiang_AoDaLiYa_DangYueZhi(upstream_base, WindData):
    field_name = u"铝土矿进出口"
    col_name = u"铝土矿进口数量_澳大利亚_当月值"
    wind_code = "S0116389"

###########################################################################################################################
""" 铝土矿供应 """   

class YangHuaLvKaiGongLv_ShanXi(upstream_base, WindData):
    field_name = u"铝土矿供应"
    col_name = u"氧化铝开工率_山西"
    wind_code = "S5811199"

class YangHuaLvKaiGongLv_ShanDong(upstream_base, WindData):
    field_name = u"铝土矿供应"
    col_name = u"氧化铝开工率_山东"
    wind_code = "S5811198"

class YangHuaLvChanLiang_LeiJiZhi(upstream_base, WindData):
    field_name = u"铝土矿供应"
    col_name = u"氧化铝产量_累计值"
    wind_code = "S0027569"

class YangHuaLvChanLiang_LeiJiTongBi(upstream_base, WindData):
    field_name = u"铝土矿供应"
    col_name = u"氧化铝产量_累计同比"
    wind_code = "S0027570"

class YangHuaLvChanLiang_DangYueZhi(upstream_base, WindData):
    field_name = u"铝土矿供应"
    col_name = u"氧化铝产量_当月值"
    wind_code = "S0027567"

class YangHuaLvChanLiang_DangYueTongBi(upstream_base, WindData):
    field_name = u"铝土矿供应"
    col_name = u"氧化铝产量_当月同比"
    wind_code = "S0027568"

class YangHuaLvALDZongChanNeng(upstream_base, WindData):
    field_name = u"铝土矿供应"
    col_name = u"氧化铝ALD总产能"
    wind_code = "S5809463"

class YangHuaLvALDZaiChanChanNeng(upstream_base, WindData):
    field_name = u"铝土矿供应"
    col_name = u"氧化铝ALD在产产能"
    wind_code = "S5809462"

class YangHuaLvALDKaiGongLv(upstream_base, WindData):
    field_name = u"铝土矿供应"
    col_name = u"氧化铝ALD开工率"
    wind_code = "S5809464"

###########################################################################################################################
""" 铝土矿价格 """   

class LvTuKuangJinKouPingJunDanJia_DangYueZhi(upstream_base, WindData):
    field_name = u"铝土矿价格"
    col_name = u"铝土矿进口平均单价_当月值"
    wind_code = "S5809332"

class LvTuKuangJiaGe_ALOverSIGT7_ShanXi(upstream_base, WindData):
    field_name = u"铝土矿价格"
    col_name = u"铝土矿价格_AL/SI>7_山西"
    wind_code = "S5801874"

class LvTuKuangJiaGe_ALOverSIEqualsTo6_ShanXi(upstream_base, WindData):
    field_name = u"铝土矿价格"
    col_name = u"铝土矿价格_AL/SI=6_山西"
    wind_code = "S5801873"
    
###########################################################################################################################
""" 氧化铝价格 """   

class YangHuaLvPingJunJia_YiJi_ShanXi(upstream_base, WindData):
    field_name = u"氧化铝价格"
    col_name = u"氧化铝平均价_一级_山西"
    wind_code = "S5807051"

class YangHuaLvPingJunJia_YiJi_ShanDong(upstream_base, WindData):
    field_name = u"氧化铝价格"
    col_name = u"氧化铝平均价_一级_山东"
    wind_code = "S5806597"

class YangHuaLvPingJunJia_LianYunGangYiJiAL2O3HanLiangNLT98Dot6Prct_AoDaLiYa(upstream_base, WindData):
    field_name = u"氧化铝价格"
    col_name = u"氧化铝平均价_连云港一级AL2O3含量>=98.6%_澳大利亚"
    wind_code = "S5806594"

class YangHuaLvChuKouPingJunDanJia_DangYueZhi(upstream_base, WindData):
    field_name = u"氧化铝价格"
    col_name = u"氧化铝出口平均单价_当月值"
    wind_code = "S0116948"

class YangHuaLvPingJunJia(upstream_base, Computed):
    field_name = u"氧化铝价格"
    col_name = u"氧化铝平均价"    
    def get_ts_whole_progress(self):
        relevant_col_list = [u"氧化铝平均价_一级_山西", u"氧化铝平均价_一级_山东"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total.mean(axis=1, skipna=True)
        return tmp_total   
    
class YangHuaLvChuKouPingJunDanJia_DangYueZhi_RenMinBiJiJia(upstream_base, Computed):
    field_name = u"氧化铝价格"
    col_name = u"氧化铝出口平均单价_当月值(人民币计价)"    
    def get_ts_whole_progress(self):
        relevant_col_list = [u"氧化铝平均价", "即期汇率_美元兑人民币"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"氧化铝平均价"] * tmp_total[u"即期汇率_美元兑人民币"]
        return tmp_total   

###########################################################################################################################
""" 氧化铝进出口 """   

class YangHuaLvJinKouZiGeGuoShuJu(upstream_base, Manual):
    field_name = u"氧化铝进出口"
    col_name = u"氧化铝进口自各国数据"

class YangHuaLvChuKouZhiGeGuoShuJu(upstream_base, Manual):
    field_name = u"氧化铝进出口"
    col_name = u"氧化铝出口至各国数据"

class YangHuaLvJinKouShuLiang_DangYueZhi(upstream_base, WindData):
    field_name = u"氧化铝进出口"
    col_name = u"氧化铝进口数量_当月值"
    wind_code = "S0027657"
    
class YangHuaLvJinKouShuLiang_LeiJiZhi(upstream_base, WindData):
    field_name = u"氧化铝进出口"
    col_name = u"氧化铝进口数量_累计值"
    wind_code = "S0027658"

class YangHuaLvJinKouShuLiang_LeiJiTongBi(upstream_base, WindData):
    field_name = u"氧化铝进出口"
    col_name = u"氧化铝进口数量_累计同比"
    wind_code = "S0027659"

class YangHuaLvChuKouShuLiang_DangYueZhi(upstream_base, WindData):
    field_name = u"废铝进出口"
    col_name = u"氧化铝出口数量_当月值"
    wind_code = "S0027660"
    
class YangHuaLvChuKouShuLiang_LeiJiZhi(upstream_base, WindData):
    field_name = u"氧化铝进出口"
    col_name = u"氧化铝出口数量_累计值"
    wind_code = "S0027661"
    
class YangHuaLvChuKouShuLiang_LeiJiTongBi(upstream_base, WindData):
    field_name = u"氧化铝进出口"
    col_name = u"氧化铝出口数量_累计同比"
    wind_code = "S0027662"    

class YangHuaLvJingJinKou(upstream_base, Computed):
    field_name = u"氧化铝进出口"
    col_name = u"氧化铝净进口"    
    def get_ts_whole_progress(self):
        relevant_col_list = [u"氧化铝进口自各国数据", u"氧化铝出口至各国数据"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"氧化铝进口自各国数据"] - tmp_total[u"氧化铝出口至各国数据"]
        return tmp_total   
        

###########################################################################################################################
""" 氧化铝库存 """   

    
class YangHuaLvKuCun_QingDaoGang(upstream_base, WindData):
    field_name = u"氧化铝库存"
    col_name = u"氧化铝库存_青岛港"
    wind_code = "S5811175"

class YangHuaLvKuCun_LianYunGang(upstream_base, WindData):
    field_name = u"氧化铝库存"
    col_name = u"氧化铝库存_连云港"
    wind_code = "S5811173"

class YangHuaLvKuCun_HeJi(upstream_base, WindData):
    field_name = u"氧化铝库存"
    col_name = u"氧化铝库存_合计"
    wind_code = "S5811176"

class YangHuaLvKuCun_BaYuQuanGang(upstream_base, WindData):
    field_name = u"氧化铝库存"
    col_name = u"氧化铝库存_鲅鱼圈港"
    wind_code = "S5811174"

###########################################################################################################################
""" 氧化铝市场整理 """  

class ZhongGuoYangHuaLvXinZengChanNengLieBiao_2018To2020Nian(upstream_base, Manual):
    field_name = u"氧化铝市场整理"
    col_name = u"中国氧化铝新增产能列表_2018-2020年"


###########################################################################################################################
""" 氧化铝供需平衡 """  

class YangHuaLvBiaoGuanXiaoFeiLiang(upstream_base, Computed):
    field_name = u"氧化铝供需平衡"
    col_name = u"氧化铝表观消费量"
    
    def get_ts_whole_progress(self):
        relevant_col_list = [u"氧化铝产量_当月值", u"氧化铝净进口"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"氧化铝产量_当月值"] + tmp_total[u"氧化铝净进口"]
        return tmp_total   
        
class YangHuaLvZongXuQiuLiang_DangYueZhi(upstream_base, WindData):
    field_name = u"氧化铝供需平衡"
    col_name = u"氧化铝总需求量_当月值"
    wind_code = "S5808256"

class YangHuaLvXuQiuLiang_YeJinJi_DangYueZhi(upstream_base, WindData):
    field_name = u"氧化铝供需平衡"
    col_name = u"氧化铝需求量_冶金级_当月值"
    wind_code = "S5808254"

class YangHuaLvXuQiuLiang_HuaGongJi_DangYueZhi(upstream_base, WindData):
    field_name = u"氧化铝供需平衡"
    col_name = u"氧化铝需求量_化工级_当月值"
    wind_code = "S5808255"

class YangHuaLvGongYingLiang_DangYueZhi(upstream_base, WindData):
    field_name = u"氧化铝供需平衡"
    col_name = u"氧化铝供应量_当月值"
    wind_code = "S5808252"

class YangHuaLvGongXuPingHeng_DangYueZhi(upstream_base, WindData):
    field_name = u"氧化铝供需平衡"
    col_name = u"氧化铝供需平衡_当月值"
    wind_code = "S5808257"




    
if __name__ == "__main__":
    df = PALXianHuoJiaGongFei().seasonal_plot()    
    
    
    
    
    
    
    
    
    
    
    
    
    
    