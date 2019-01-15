# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 10:44:58 2018

@author: 李弘一萌
"""

import pandas as pd
from datetime import datetime
from .RU_Base import RU_Base
from . import RU_Macro, RU_SpotPrice, RU_FuturesPrice
from ...Base.DataType_Base import Manual, Computed, WindData
from ...Base.Plot_Base import Plot_Base
from matplotlib.ticker import FuncFormatter

class upstream_base(RU_Base, Plot_Base):
    table_english_name = "Upstream"
    table_chinese_name = u"上游"
    
    def output(self):
        print("Upstream")
    
    def get_relevant_df(self, col_list):
        local_col_name_list = upstream_base.get_all_table_classname()
        col_cls_list = []
        for x in col_list:
            col_cls_name = str(RU_Base.get_class_name(x))
            if col_cls_name not in local_col_name_list:
                col_cls_list.append(eval(RU_Base.get_table_class_full_variable(x)))
            else:
                col_cls_list.append(eval(col_cls_name))
        ts_list = [x().get_ts() for x in col_cls_list]
        tmp_table_df = pd.concat(ts_list, axis=1).dropna(how="all")
        return tmp_table_df

###########################################################################################################################
""" 产量 """  

class XiangJiaoChanLiang_TaiGuo(upstream_base, WindData):
    field_name = u"产量"
    col_name = u"橡胶产量_泰国"
    wind_code = "S5400576"

class XiangJiaoChanLiang_YinDuNiXiYa(upstream_base, WindData):
    field_name = u"产量"
    col_name = u"橡胶产量_印度尼西亚"
    wind_code = "S5400577"

class XiangJiaoChanLiang_MaLaiXiYa(upstream_base, WindData):
    field_name = u"产量"
    col_name = u"橡胶产量_马来西亚"
    wind_code = "S5400578"

class XiangJiaoChanLiang_YueNan(upstream_base, WindData):
    field_name = u"产量"
    col_name = u"橡胶产量_越南"
    wind_code = "S5400580"

class XiangJiaoChanLiang_ZhongGuo(upstream_base, WindData):
    field_name = u"产量"
    col_name = u"橡胶产量_中国"
    wind_code = "S5400581"

class XiangJiaoChanLiang_YinDu(upstream_base, WindData):
    field_name = u"产量"
    col_name = u"橡胶产量_印度"
    wind_code = "S5400579"

class XiangJiaoChanLiang_FeiLvBin(upstream_base, WindData):
    field_name = u"产量"
    col_name = u"橡胶产量_菲律宾"
    wind_code = "S5400576"

class XiangJiaoChanLiang_SiLiLanKa(upstream_base, WindData):
    field_name = u"产量"
    col_name = u"橡胶产量_斯里兰卡"
    wind_code = "S5400582"

class XiangJiaoChanLiang_JianPuZhai(upstream_base, WindData):
    field_name = u"产量"
    col_name = u"橡胶产量_柬埔寨"
    wind_code = "S5400584"

class XiangJiaoChanLiang_ANRPCChengYuanGuoHeJi(upstream_base, WindData):
    field_name = u"产量"
    col_name = u"橡胶产量_ANRPC成员国合计"
    wind_code = "S5426627"
    
###########################################################################################################################
""" 单产 """  
     
class XiangJiaoDanChan_TaiGuo(upstream_base, WindData):
    field_name = u"单产"
    col_name = u"橡胶单产_泰国"
    wind_code = "S5426719"
    
class XiangJiaoDanChan_YinDuNiXiYa(upstream_base, WindData):
    field_name = u"单产"
    col_name = u"橡胶单产_印度尼西亚"
    wind_code = "S5426715"

class XiangJiaoDanChan_MaLaiXiYa(upstream_base, WindData):
    field_name = u"单产"
    col_name = u"橡胶单产_马来西亚"
    wind_code = "S5426716"

class XiangJiaoDanChan_YueNan(upstream_base, WindData):
    field_name = u"单产"
    col_name = u"橡胶单产_越南"
    wind_code = "S5426720"

class XiangJiaoDanChan_ZhongGuo(upstream_base, WindData):
    field_name = u"单产"
    col_name = u"橡胶单产_中国"
    wind_code = "S5426713"

class XiangJiaoDanChan_YinDu(upstream_base, WindData):
    field_name = u"单产"
    col_name = u"橡胶单产_印度"
    wind_code = "S5426714"

class XiangJiaoDanChan_FeiLvBin(upstream_base, WindData):
    field_name = u"单产"
    col_name = u"橡胶单产_菲律宾"
    wind_code = "S5426717"

class XiangJiaoDanChan_SiLiLanKa(upstream_base, WindData):
    field_name = u"单产"
    col_name = u"橡胶单产_斯里兰卡"
    wind_code = "S5426718"

class XiangJiaoDanChan_JianPuZhai(upstream_base, WindData):
    field_name = u"单产"
    col_name = u"橡胶单产_柬埔寨"
    wind_code = "S5426715"    

    
###########################################################################################################################
""" 合成胶利润 """ 

class ShunDingShengChanLiRun(upstream_base, Computed):
    field_name = u"合成胶利润"
    col_name = u"顺丁生产利润"  
    def get_ts_whole_progress(self):
        relevant_col_list = [u"顺丁市场价格_华东", u"丁二烯市场价_华东"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"顺丁市场价格_华东"] - (tmp_total[u"丁二烯市场价_华东"] * 1.03 + 3000)
        return tmp_total 
   
class DingBenShengChanLiRun(upstream_base, Computed):
    field_name = u"合成胶利润"
    col_name = u"丁苯生产利润"  
    def get_ts_whole_progress(self):
        relevant_col_list = [u"丁苯市场价格_华东", u"苯乙烯市场价_华东", u"丁二烯市场价_华东"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"丁苯市场价格_华东"] - (tmp_total[u"丁二烯市场价_华东"] * 0.73 + tmp_total[u"苯乙烯市场价_华东"] * \
                                   0.27 + 2800)
        return tmp_total     

###########################################################################################################################
""" 进口利润 """ 

class XiangJiaoJinKouLiRun_MeiJinJiao(upstream_base, Computed):
    field_name = u"进口利润"
    col_name = u"橡胶进口利润_美金胶"  
    def get_ts_whole_progress(self):
        relevant_col_list = [u"RU主力合约收盘价", u"泰国3号烟片(RSS3)美金CIF价格", u"汇卖价_美元兑人民币"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"RU主力合约收盘价"] - ((tmp_total[u"泰国3号烟片(RSS3)美金CIF价格"] * tmp_total[u"汇卖价_美元兑人民币"] + \
                                   1500) * 1.16 + 120)
        return tmp_total 
   
class XiangJiaoJinKouLiRun_BaoShuiQu(upstream_base, Computed):
    field_name = u"进口利润"
    col_name = u"橡胶进口利润_保税区"  
    def get_ts_whole_progress(self):
        relevant_col_list = [u"RU主力合约收盘价", u"泰国3号烟片(RSS3)保税区价格", u"汇卖价_美元兑人民币"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"RU主力合约收盘价"] - ((tmp_total[u"泰国3号烟片(RSS3)保税区价格"] * tmp_total[u"汇卖价_美元兑人民币"] + \
                                   1500) * 1.16 + 120)
        return tmp_total   

    
###########################################################################################################################
""" 进口量 """ 

class TianRanJiHeChengXiangJiaoJinKouShuLiang(upstream_base, WindData):
    field_name = u"进口量"
    col_name = u"天然及合成橡胶(包括胶乳)进口数量"
    wind_code = "S0255519"

class TianRanXiangJiaoJinKouShuLiang(upstream_base, WindData):
    field_name = u"进口量"
    col_name = u"天然橡胶进口数量"
    wind_code = "S0027346"

class TianRanXiangJiaoYanJiaoPianJinKouShuLiang(upstream_base, WindData):
    field_name = u"进口量"
    col_name = u"天然橡胶烟胶片(即烟片胶)进口数量"
    wind_code = "S5402622"

class JiShuFenLeiTianRanXiangJiaoJinKouShuLiang(upstream_base, WindData):
    field_name = u"进口量"
    col_name = u"技术分类天然橡胶(TSNR)(即标准胶)进口数量"
    wind_code = "S0255519"
    
class TianRanJiaoRuJinKouShuLiang(upstream_base, WindData):
    field_name = u"进口量"
    col_name = u"天然胶乳(即乳胶)进口数量"
    wind_code = "S5402621"
    
class HeChengXiangJiaoJinKouShuLiang(upstream_base, WindData):
    field_name = u"进口量"
    col_name = u"合成橡胶进口数量"
    wind_code = "S5005736"

class TianRanXiangJiaoYuHeChengXiangJiaoHunHeWuJinKouShuLiang(upstream_base, WindData):
    field_name = u"进口量"
    col_name = u"天然橡胶与合成橡胶混合物(40028000)进口数量"
    wind_code = "S5402192"    
###########################################################################################################################
""" 原料价格 """ 

class BenYiXiShiChangJia_HuaDong(upstream_base, WindData):
    field_name = u"原料价格"
    col_name = u"苯乙烯市场价_华东"
    wind_code = "S5422007"    

class DingErXiShiChangJia_HuaDong(upstream_base, WindData):
    field_name = u"原料价格"
    col_name = u"丁二烯市场价_华东"
    wind_code = "S5438884" 
    
###########################################################################################################################
""" 种植面积 """ 

class XiangJiaoXinZhongZhiMianJi_TaiGuo(upstream_base, WindData):
    field_name = u"种植面积"
    col_name = u"橡胶新种植面积_泰国"
    wind_code = "S5426690" 
    
class XiangJiaoXinZhongZhiMianJi_YinDuNiXiYa(upstream_base, WindData):
    field_name = u"种植面积"
    col_name = u"橡胶新种植面积_印度尼西亚"
    wind_code = "S5426682" 

class XiangJiaoXinZhongZhiMianJi_MaLaiXiYa(upstream_base, WindData):
    field_name = u"种植面积"
    col_name = u"橡胶新种植面积_马来西亚"
    wind_code = "S5426684" 

class XiangJiaoXinZhongZhiMianJi_YueNan(upstream_base, WindData):
    field_name = u"种植面积"
    col_name = u"橡胶新种植面积_越南"
    wind_code = "S5426692" 

class XiangJiaoXinZhongZhiMianJi_ZhongGuo(upstream_base, WindData):
    field_name = u"种植面积"
    col_name = u"橡胶新种植面积_中国"
    wind_code = "S5426678" 

class XiangJiaoXinZhongZhiMianJi_YinDu(upstream_base, WindData):
    field_name = u"种植面积"
    col_name = u"橡胶新种植面积_印度"
    wind_code = "S5426680" 

class XiangJiaoXinZhongZhiMianJi_FeiLvBin(upstream_base, WindData):
    field_name = u"种植面积"
    col_name = u"橡胶新种植面积_菲律宾"
    wind_code = "S5426686" 

class XiangJiaoXinZhongZhiMianJi_SiLiLanKa(upstream_base, WindData):
    field_name = u"种植面积"
    col_name = u"橡胶新种植面积_斯里兰卡"
    wind_code = "S5426688" 

class XiangJiaoXinZhongZhiMianJi_JianPuZhai(upstream_base, WindData):
    field_name = u"种植面积"
    col_name = u"橡胶新种植面积_柬埔寨"
    wind_code = "S5426676" 

class XiangJiaoZhongXinZhongZhiMianJi_TaiGuo(upstream_base, WindData):
    field_name = u"种植面积"
    col_name = u"橡胶重新种植面积_泰国"
    wind_code = "S5426691" 

class XiangJiaoZhongXinZhongZhiMianJi_YinDuNiXiYa(upstream_base, WindData):
    field_name = u"种植面积"
    col_name = u"橡胶重新种植面积_印度尼西亚"
    wind_code = "S5426683" 

class XiangJiaoZhongXinZhongZhiMianJi_MaLaiXiYa(upstream_base, WindData):
    field_name = u"种植面积"
    col_name = u"橡胶重新种植面积_马来西亚"
    wind_code = "S5426685" 

class XiangJiaoZhongXinZhongZhiMianJi_YueNan(upstream_base, WindData):
    field_name = u"种植面积"
    col_name = u"橡胶重新种植面积_越南"
    wind_code = "S5426693" 

class XiangJiaoZhongXinZhongZhiMianJi_ZhongGuo(upstream_base, WindData):
    field_name = u"种植面积"
    col_name = u"橡胶重新种植面积_中国"
    wind_code = "S5426679" 

class XiangJiaoZhongXinZhongZhiMianJi_YinDu(upstream_base, WindData):
    field_name = u"种植面积"
    col_name = u"橡胶重新种植面积_印度"
    wind_code = "S5426681" 

class XiangJiaoZhongXinZhongZhiMianJi_FeiLvBin(upstream_base, WindData):
    field_name = u"种植面积"
    col_name = u"橡胶重新种植面积_菲律宾"
    wind_code = "S5426687" 

class XiangJiaoZhongXinZhongZhiMianJi_SiLiLanKa(upstream_base, WindData):
    field_name = u"种植面积"
    col_name = u"橡胶重新种植面积_斯里兰卡"
    wind_code = "S5426689" 

class XiangJiaoZhongXinZhongZhiMianJi_JianPuZhai(upstream_base, WindData):
    field_name = u"种植面积"
    col_name = u"橡胶重新种植面积_柬埔寨"
    wind_code = "S5426677" 

class XiangJiaoZongZhongZhiMianJi_TaiGuo(upstream_base, WindData):
    field_name = u"种植面积"
    col_name = u"橡胶总种植面积_泰国"
    wind_code = "S5426708" 

class XiangJiaoZongZhongZhiMianJi_YinDuNiXiYa(upstream_base, WindData):
    field_name = u"种植面积"
    col_name = u"橡胶总种植面积_印度尼西亚"
    wind_code = "S5426700" 

class XiangJiaoZongZhongZhiMianJi_MaLaiXiYa(upstream_base, WindData):
    field_name = u"种植面积"
    col_name = u"橡胶总种植面积_马来西亚"
    wind_code = "S5426702" 

class XiangJiaoZongZhongZhiMianJi_YueNan(upstream_base, WindData):
    field_name = u"种植面积"
    col_name = u"橡胶总种植面积_越南"
    wind_code = "S5426710" 

class XiangJiaoZongZhongZhiMianJi_ZhongGuo(upstream_base, WindData):
    field_name = u"种植面积"
    col_name = u"橡胶总种植面积_中国"
    wind_code = "S5426696" 

class XiangJiaoZongZhongZhiMianJi_YinDu(upstream_base, WindData):
    field_name = u"种植面积"
    col_name = u"橡胶总种植面积_印度"
    wind_code = "S5426698" 

class XiangJiaoZongZhongZhiMianJi_FeiLvBin(upstream_base, WindData):
    field_name = u"种植面积"
    col_name = u"橡胶总种植面积_菲律宾"
    wind_code = "S5426704" 

class XiangJiaoZongZhongZhiMianJi_SiLiLanKa(upstream_base, WindData):
    field_name = u"种植面积"
    col_name = u"橡胶总种植面积_斯里兰卡"
    wind_code = "S5426706" 

class XiangJiaoZongZhongZhiMianJi_JianPuZhai(upstream_base, WindData):
    field_name = u"种植面积"
    col_name = u"橡胶总种植面积_柬埔寨"
    wind_code = "S5426694" 

class XiangJiaoKaiGeMianJi_TaiGuo(upstream_base, WindData):
    field_name = u"种植面积"
    col_name = u"橡胶开割面积_泰国"
    wind_code = "S5426709" 

class XiangJiaoKaiGeMianJi_YinDuNiXiYa(upstream_base, WindData):
    field_name = u"种植面积"
    col_name = u"橡胶开割面积_印度尼西亚"
    wind_code = "S5426701" 

class XiangJiaoKaiGeMianJi_MaLaiXiYa(upstream_base, WindData):
    field_name = u"种植面积"
    col_name = u"橡胶开割面积_马来西亚"
    wind_code = "S5426703" 

class XiangJiaoKaiGeMianJi_YueNan(upstream_base, WindData):
    field_name = u"种植面积"
    col_name = u"橡胶开割面积_越南"
    wind_code = "S5426711" 

class XiangJiaoKaiGeMianJi_ZhongGuo(upstream_base, WindData):
    field_name = u"种植面积"
    col_name = u"橡胶开割面积_中国"
    wind_code = "S5426697" 

class XiangJiaoKaiGeMianJi_YinDu(upstream_base, WindData):
    field_name = u"种植面积"
    col_name = u"橡胶开割面积_印度"
    wind_code = "S5426699" 

class XiangJiaoKaiGeMianJi_FeiLvBin(upstream_base, WindData):
    field_name = u"种植面积"
    col_name = u"橡胶开割面积_菲律宾"
    wind_code = "S5426705" 

class XiangJiaoKaiGeMianJi_SiLiLanKa(upstream_base, WindData):
    field_name = u"种植面积"
    col_name = u"橡胶开割面积_斯里兰卡"
    wind_code = "S5426707" 

class XiangJiaoKaiGeMianJi_JianPuZhai(upstream_base, WindData):
    field_name = u"种植面积"
    col_name = u"橡胶开割面积_柬埔寨"
    wind_code = "S5426695" 














































    
if __name__ == "__main__":
    df = PTAXianHuoJiaGongFei().seasonal_plot()    
    
    
    
    
    
    
    
    
    
    
    
    
    
    