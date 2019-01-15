# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 16:13:19 2018

@author: 李弘一萌
"""

import pandas as pd
from datetime import datetime
from ...Futures_Data.Profile.CntData import Cnt_Data
#from MyFutureClass.Contract.FuturesContract import Contracts






def main_month_quote_2_spread_series(month_list, all_main_quote_df):
    month_code_list = [x for x in all_main_quote_df.columns.tolist() if x[-6:-4] in month_list]
    tmp_total = all_main_quote_df[month_code_list]
    count = 0
    spread_list = []
    cmt_profile, cnt_profile = Cnt_Data.get_profile()
    cnt_obj_list = [Cnt_Data(x, cmt_profile, cnt_profile) for x in tmp_total.columns]
    cnt_obj_list.sort()
    tmp_total = tmp_total[[x.cnt_code for x in cnt_obj_list]]
    for cnt in tmp_total.columns.tolist():
        if (cnt[-6:-4] == month_list[0]) and (cnt != tmp_total.columns.tolist()[-1]):
            next_cnt = tmp_total.columns.tolist()[count+1]
            cnt_obj = Cnt_Data(next_cnt, cmt_profile, cnt_profile)
            tmp_start_date = datetime(int(cnt_obj.cnt_year)-1, int(cnt_obj.cnt_month), 1)
            spread = tmp_total.iloc[:, count] - tmp_total.iloc[:, count+1]
            spread = spread[spread.index >= tmp_start_date]
            spread_list.append(spread.dropna())
        count += 1
    spread_series = pd.concat(spread_list)
    spread_series = spread_series[~spread_series.index.duplicated()]
    return spread_series