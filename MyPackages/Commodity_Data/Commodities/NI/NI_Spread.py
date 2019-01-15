# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 10:48:24 2018

@author: 李弘一萌
"""

import pandas as pd
from datetime import datetime
from .NI_Base import NI_Base
from . import NI_SpotPrice, NI_FuturesPrice, NI_Upstream, NI_Downstream, NI_Macro
from ..ZC import ZC_SpotPrice
from ..J import J_SpotPrice
from ...Base.Spread_Generate import main_month_quote_2_spread_series
from ...Base.DataType_Base import Manual, Computed, WindData
from ...Base.Plot_Base import Plot_Base
from matplotlib.ticker import FuncFormatter

class spread_base(NI_Base, Plot_Base):
    table_english_name = "Spread"
    table_chinese_name = u"价差与比价"
    
    def output(self):
        print("Spread")
    
    def get_relevant_df(self, col_list):
        local_col_name_list = spread_base.get_all_table_classname()
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
""" 电解镍升贴水 """    

class JinChuanNieShengTieShui_ZuiXiaoZhi(spread_base, WindData):
    field_name = u"电解镍升贴水"
    col_name = u"金川镍升贴水_最小值"
    wind_code = "S5810894"
    axhline = 0
    
class ENieShengTieShui_ZuiXiaoZhi(spread_base, WindData):
    field_name = u"电解镍升贴水"
    col_name = u"俄镍升贴水_最小值"
    wind_code = "S5715356"   
    start_year = 2014
    axhline = 0
    
class NieShengTieShuiPingJunJia_ShangHaiWuMao(spread_base, WindData):
    field_name = u"电解镍升贴水"
    col_name = u"镍升贴水平均价_上海物贸"
    wind_code = "S5820802"  
    axhline = 0
    
class LMENieShengTieShui_0To3(spread_base, WindData):
    field_name = u"电解镍升贴水"
    col_name = u"LME镍升贴水(0-3)"
    wind_code = "S5806063" 
    start_year = 2014
    axhline = 0
    
class LMENieShengTieShui_3To15(spread_base, WindData):
    field_name = u"电解镍升贴水"
    col_name = u"LME镍升贴水(3-15)"
    wind_code = "S5808602" 
    axhline = 0
    
class GaoNieShengTieDuiDianJieNieShengTieShui(spread_base, Computed):
    field_name = u"电解镍升贴水"
    col_name = u"高镍生铁对电解镍升贴水"
    axhline = 0
    def get_ts_whole_progress(self):
        relevant_col_list = [u"高镍铁含税价_高镍铁_7-10%_山东", u"期货成交量(活跃合约)_镍"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"高镍铁含税价_高镍铁_7-10%_山东"] - tmp_total[u"期货成交量(活跃合约)_镍"] / 100
        return tmp_total    


###########################################################################################################################
""" 电解镍溢价 """    

class ShangHaiDianJieNieZuiDiYiJia_CIF_TiDan(spread_base, WindData):
    field_name = u"电解镍溢价"
    col_name = u"上海电解镍最低溢价_CIF(提单)"
    wind_code = "S5809442"
    
class ShangHaiDianJieNieZuiGaoYiJia_CIF_TiDan(spread_base, WindData):
    field_name = u"电解镍升贴水"
    col_name = u"上海电解镍最高溢价_CIF(提单)"
    wind_code = "S5809443"    
    
class ShangHaiDianJieNieZuiDiYiJia_BaoShuiKu_CangDan(spread_base, WindData):
    field_name = u"电解镍升贴水"
    col_name = u"上海电解镍最低溢价_保税库(仓单)"
    wind_code = "S5809450"    
    
class ShangHaiDianJieNieZuiGaoYiJia_BaoShuiKu_CangDan(spread_base, WindData):
    field_name = u"电解镍升贴水"
    col_name = u"上海电解镍最高溢价_保税库(仓单)"
    wind_code = "S5809451"    

    
###########################################################################################################################
""" 比价 """ 


class HuLunNieXianHuoBiJia(spread_base, Computed):
    field_name = u"比价"
    col_name = u"沪伦镍现货比价"
    axhline = 0
    def get_ts_whole_progress(self):
        relevant_col_list = [u"1#电解镍价格_长江有色市场_最低价(含税)", u"15点LME3个月镍(电子盘)价格", u"LME镍升贴水(0-3)"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"1#电解镍价格_长江有色市场_最低价(含税)"] / (tmp_total[u"15点LME3个月镍(电子盘)价格"] + \
                                   tmp_total[u"LME镍升贴水(0-3)"])
        return tmp_total
    
class JinKouNieJunHengBiJia(spread_base, Computed):
    field_name = u"比价"
    col_name = u"进口镍均衡比价"
    axhline = 0
    def get_ts_whole_progress(self):
        relevant_col_list = [u"上海电解镍最低溢价_CIF(提单)", u"15点LME3个月镍(电子盘)价格", u"LME镍升贴水(0-3)"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = (tmp_total[u"15点LME3个月镍(电子盘)价格"] + tmp_total[u"LME镍升贴水(0-3)"] + tmp_total[u"上海电解镍最低溢价_CIF(提单)"]) \
                                   / (tmp_total[u"15点LME3个月镍(电子盘)价格"] + tmp_total[u"LME镍升贴水(0-3)"])
        return tmp_total

class NieZhuLiHeYueBiJia(spread_base, Computed):
    field_name = u"比价"
    col_name = u"镍主力合约比价"
    axhline = 0
    def get_ts_whole_progress(self):
        relevant_col_list = [u"期货收盘价(活跃合约)_镍", u"期货收盘价(电子盘)_LME3个月镍"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"期货收盘价(活跃合约)_镍"] / tmp_total[u"期货收盘价(电子盘)_LME3个月镍"]
        return tmp_total

class BuXiuGangYuNieBanBiJia(spread_base, Computed):
    field_name = u"比价"
    col_name = u"不锈钢与镍板比价"
    axhline = 0
    def get_ts_whole_progress(self):
        relevant_col_list = [u"不锈钢价格_304/2B卷板_2.0mm_太钢_无锡", u"期货收盘价(活跃合约)_镍"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"不锈钢价格_304/2B卷板_2.0mm_太钢_无锡"] / tmp_total[u"期货收盘价(活跃合约)_镍"]
        return tmp_total

class NieTieYuNieKuangBiJia(spread_base, Computed):
    field_name = u"比价"
    col_name = u"镍铁与镍矿比价"
    axhline = 0
    def get_ts_whole_progress(self):
        relevant_col_list = [u"高镍铁含税价_高镍铁_7-10%_山东", u"印尼镍矿价格_Ni_1.6-1.7Fe_20-25%_华南"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"高镍铁含税价_高镍铁_7-10%_山东"] / tmp_total[u"印尼镍矿价格_Ni_1.6-1.7Fe_20-25%_华南"]
        return tmp_total

###########################################################################################################################
""" 进口利润 """  

class XianHuoNieJinKouLiRun(spread_base, Computed):
    field_name = u"进口利润"
    col_name = u"现货镍进口利润" 
    axhline = 0
    def get_ts_whole_progress(self):
        relevant_col_list = [u"1#电解镍价格_长江有色市场_最低价(含税)", u"15点LME3个月镍(电子盘)价格", u"上海电解镍最低溢价_CIF(提单)",
                             u"即期汇率_美元兑人民币", u"LME镍升贴水(0-3)"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"1#电解镍价格_长江有色市场_最低价(含税)"] - (tmp_total[u"15点LME3个月镍(电子盘)价格"] + \
                                   tmp_total[u"LME镍升贴水(0-3)"] + tmp_total[u"上海电解镍最低溢价_CIF(提单)"]) * tmp_total[u"即期汇率_美元兑人民币"] \
                                   * 1.16 * 1.02 - 200
        return tmp_total   

    
class HuNieZhuLiHeYueJinKouLiRun(spread_base, Computed):
    field_name = u"进口利润"
    col_name = u"沪镍主力合约进口利润" 
    axhline = 0
    def get_ts_whole_progress(self):
        relevant_col_list = [u"期货收盘价(活跃合约)_镍", u"15点LME3个月镍(电子盘)价格", u"上海电解镍最低溢价_CIF(提单)",
                             u"即期汇率_美元兑人民币", u"LME镍升贴水(0-3)"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"期货收盘价(活跃合约)_镍"] - (tmp_total[u"15点LME3个月镍(电子盘)价格"] + \
                                   tmp_total[u"上海电解镍最低溢价_CIF(提单)"]) * tmp_total[u"即期汇率_美元兑人民币"] * 1.16 * 1.02 - 200
        return tmp_total 

###########################################################################################################################
""" 生产利润 """  
    
class NieTieShengChanLiRun(spread_base, Computed):
    field_name = u"生产利润"
    col_name = u"镍铁生产利润"   
    axhline = 0
    start_year = 2014
    def get_ts_whole_progress(self):
        relevant_col_list = [u"高镍铁含税价_高镍铁_7-10%_山东", "菲律宾镍矿价格_Ni_1.5-1.6Fe_25-30%_华北"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_ts_list = [tmp_total, 
                       ZC_SpotPrice.DongLiMeiGangKouPingCangJia_Q5500_QinHuangDaoGang().get_ts(), 
                       J_SpotPrice.ZhunYiJiYeJinJiaoChuChangJia_HanShui_FuShun().get_ts()]
        tmp_total = pd.concat(tmp_ts_list, axis=1, sort=False)
        tmp_total[self.col_name] = tmp_total[u"高镍铁含税价_高镍铁_7-10%_山东"] - (4125 + tmp_total[u"菲律宾镍矿价格_Ni_1.5-1.6Fe_25-30%_华北"] * 9.21 + \
                                   tmp_total[u"动力煤港口平仓价_Q5500_秦皇岛港"] + tmp_total[u"准一级冶金焦出厂价(含税)_抚顺"] * 0.45) / 10
        return tmp_total   

class NieTiePanMianLiRun(spread_base, Computed):
    field_name = u"生产利润"
    col_name = u"镍铁盘面生产利润"   
    axhline = 0
    start_year = 2014
    def get_ts_whole_progress(self):
        relevant_col_list = [u"期货收盘价(电子盘)_LME3个月镍", "菲律宾镍矿价格_Ni_1.5-1.6Fe_25-30%_华北", "即期汇率_美元兑人民币"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_ts_list = [tmp_total, 
                       ZC_SpotPrice.DongLiMeiGangKouPingCangJia_Q5500_QinHuangDaoGang().get_ts(), 
                       J_SpotPrice.ZhunYiJiYeJinJiaoChuChangJia_HanShui_FuShun().get_ts()]
        tmp_total = pd.concat(tmp_ts_list, axis=1, sort=False)
        tmp_total[self.col_name] = tmp_total[u"期货收盘价(电子盘)_LME3个月镍"] - (4125 + tmp_total[u"菲律宾镍矿价格_Ni_1.5-1.6Fe_25-30%_华北"] * 9.21 + \
                                   tmp_total[u"动力煤港口平仓价_Q5500_秦皇岛港"] + tmp_total[u"准一级冶金焦出厂价(含税)_抚顺"] * 0.45) * 10 / (1.16 * tmp_total["即期汇率_美元兑人民币"])
        return tmp_total   






if __name__ == "__main__":
    df = NieTieShengChanLiRun().get_ts()
#    df, fig, axis = NieTiePanMianLiRun().seasonal_plot()
    
    
    
    
    
    
    
    
    
    
    
    
    
    