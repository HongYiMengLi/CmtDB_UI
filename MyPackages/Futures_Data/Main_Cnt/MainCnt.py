# -*- coding: utf-8 -*-
"""
Created on Fri Jun 29 09:20:01 2018

@author: 李弘一萌
"""

import pandas as pd
import numpy as np
import copy
from datetime import datetime, date, timedelta
from ..DateTime.Trade_Date import Trade_Date
from ...Data_Path.data_path import Data_Path
from ..Profile.CntData import Cnt_Data
from ..Quote.QuoteData import QuoteData
from ...SQL.Table_Create import sql_main_cnt
from sqlalchemy.orm import sessionmaker


class Main_Cnt(object):
    relative_db_path = Data_Path.relative_local_db_path()
    tmp_filename = relative_db_path + "main_cnt/main_cnt_active.csv"
    default_mode = "db"

    @staticmethod
    def get_main_cnt(index_type="date", mode=default_mode):
        if mode == "local":
            tmp_df = pd.read_csv(Main_Cnt.tmp_filename, index_col=0, parse_dates=[0])
            if index_type=="date":
                tmp_df.index = Trade_Date.timestamp2date(tmp_df.index)
        elif mode == "db":
            session = sessionmaker()
            session.configure(bind=sql_main_cnt.engine)
            s = session()
            class_variable = sql_main_cnt.SQL_Main_Cnt_Data 
            try:
                           
                tmp_query = s.query(class_variable.cmt, class_variable.date, class_variable.contract)
                tmp_df = pd.read_sql(tmp_query.statement, sql_main_cnt.engine, index_col=["date", "cmt"])
                tmp_df = tmp_df.unstack()
                tmp_df.columns = [x[1] for x in tmp_df.columns]
            except Exception as e:
                print(repr(e))
                s.rollback()
                raise e
            finally:
                s.close() 
        return tmp_df

    @staticmethod
    def get_local_single_main_cnt(index_type="date"):
        tmp_df = pd.read_csv(Main_Cnt.relative_db_path + "main_cnt/single_update/main_cnt_total.csv", 
                             index_col=0, parse_dates=[0])
        if index_type=="date":
            tmp_df.index = Trade_Date.timestamp2date(tmp_df.index)
        return tmp_df
    
    @staticmethod
    def get_local_main_cnt_smoothed_price(index_type="date"):
        tmp_df = pd.read_csv(Main_Cnt.relative_db_path + "main_cnt/main_cnt_smoothed_price.csv", 
                             index_col=0, parse_dates=[0])
        if index_type=="date":
            tmp_df.index = Trade_Date.timestamp2date(tmp_df.index)
        return tmp_df

    @staticmethod
    def get_local_single_main_cnt_smoothed_price(index_type="date"):
        tmp_df = pd.read_csv(Main_Cnt.relative_db_path + "main_cnt/single_update/main_cnt_smoothed_price.csv", 
                             index_col=0, parse_dates=[0])
        if index_type=="date":
            tmp_df.index = Trade_Date.timestamp2date(tmp_df.index)
        return tmp_df
    
    @staticmethod
    def compute_main_cnt_by_oi(cmt, max_oi_cnt, effective_cnt, main_cnt_df, decide_param):
        cnt_all_list = effective_cnt.index.tolist() 
        main_cnt_list = list(max_oi_cnt)
        original_cnt = main_cnt_list[0]
        sub_cnt = main_cnt_df[cmt][-decide_param]
        
        decide_flag = False        
        back_cnt_list = main_cnt_df[cmt].unique().tolist()
        back_cnt_list.pop()
        filtered_main_cnt_list = copy.deepcopy(main_cnt_list)
        
        for t in range(len(main_cnt_list)):
            tdate = max_oi_cnt.index[t]
            if original_cnt in effective_cnt.index:
                if effective_cnt.loc[original_cnt,"last_trade_date"] >= tdate:
                    if decide_flag==False:
                        if main_cnt_list[t]==sub_cnt:
                            filtered_main_cnt_list[t] = sub_cnt
                        else:
                            if main_cnt_list[t] in back_cnt_list:
                                filtered_main_cnt_list[t] = sub_cnt
                            else:
                                original_cnt = sub_cnt
                                sub_cnt = main_cnt_list[t]
                                decide_flag = True
                                filtered_main_cnt_list[t] = original_cnt
                                decide_day = 1
                    elif decide_flag==True:
                        filtered_main_cnt_list[t] = original_cnt
                        if main_cnt_list[t]==sub_cnt:
                            decide_day += 1
                            if decide_day>=decide_param:
                                decide_flag = False
                                original_cnt = sub_cnt
                                back_cnt_list = cnt_all_list[:(cnt_all_list.index(sub_cnt))]
                        elif main_cnt_list[t]==original_cnt:
                            decide_flag = False
                            sub_cnt = main_cnt_list[t]
                        else:
                            sub_cnt = main_cnt_list[t]  
            else:
                filtered_main_cnt_list[t] = main_cnt_list[t]
                original_cnt = main_cnt_list[t]
                sub_cnt = main_cnt_list[t]
                back_cnt_list = cnt_all_list[:(cnt_all_list.index(sub_cnt))]
                decide_flag = False 
        result = pd.Series(filtered_main_cnt_list[decide_param:],index=max_oi_cnt.index[decide_param:])
        return result
    
    @staticmethod
    def main_cnt_construct(cmt_list, start_date, end_date, decide_param = 2):
        start_date = datetime.strptime(start_date,"%Y-%m-%d").date()
        end_date = datetime.strptime(end_date,"%Y-%m-%d").date()
        main_cnt_series_list = []    
        for cmt in cmt_list:
            #持仓量矩阵
            cnt_data = Cnt_Data.generate_effective_cnt_df(cmt, start_date, end_date)
            if len(cnt_data) == 0:
                 main_cnt_series_list.append(pd.Series([],name=cmt))
                 continue
            else:
                cnt_data["contract_issue_date"] = Trade_Date.timestamp2date(cnt_data["contract_issue_date"].tolist())
                cnt_data["last_trade_date"] = Trade_Date.timestamp2date(cnt_data["last_trade_date"].tolist())
                if start_date < cnt_data["contract_issue_date"].iloc[0]:
                    base_date = cnt_data["contract_issue_date"].iloc[0] + timedelta(days=1)
                else:
                    base_date = start_date
                effective_cnt = cnt_data.copy()
                cnt_all_list = list(cnt_data.index)
                oi_data = QuoteData.Daily.get_cmt_quote("open_interest", cmt)
                oi_data.index = Trade_Date.timestamp2date(oi_data.index.tolist())
                oi_data = oi_data[oi_data.index >= base_date]
                oi_data = oi_data[cnt_all_list].dropna(how="all").fillna(0)
                
                
                #考虑持仓量相同的情况
                oi_data = oi_data[~(oi_data.max(axis=1)==0)]
                max_count_f = lambda x: x[x==x.max()].count()
                max_oi_count = oi_data.apply(max_count_f,axis=1)
                print(cmt+"持仓量相等情况个数%d" % len(max_oi_count[max_oi_count>1]))
                
                #处理数据
                #万得下载的持仓量数据有时在合约未上市或退市后仍有数据，导致之后横向比较出现错误，因此需要过滤掉无效数据
                for cnt in cnt_all_list:
                    last_trade_date = effective_cnt.loc[cnt,"last_trade_date"]
                    if last_trade_date in oi_data.index:
                        oi_data.loc[oi_data.index>last_trade_date,cnt] = 0
                    first_trade_date = effective_cnt.loc[cnt,"contract_issue_date"]
                    if first_trade_date in oi_data.index:
                        oi_data.loc[oi_data.index<first_trade_date,cnt] = 0
           
                #找最大持仓量合约
                max_oi_cnt_f = lambda x: x.idxmax()
                max_oi_cnt = oi_data.apply(max_oi_cnt_f,axis=1)
               
                main_cnt_list = list(max_oi_cnt)
                original_cnt = main_cnt_list[0]
                sub_cnt = main_cnt_list[0]                
                decide_flag = False        
                back_cnt_list = []
                filtered_main_cnt_list = copy.deepcopy(main_cnt_list)                
                for t in range(len(main_cnt_list)):
                    today = max_oi_cnt.index[t]
                    if effective_cnt.loc[original_cnt,"last_trade_date"] >= today:
                        if decide_flag==False:
                            if main_cnt_list[t]==sub_cnt:
                                filtered_main_cnt_list[t] = sub_cnt
                            else:
                                if main_cnt_list[t] in back_cnt_list:
                                    filtered_main_cnt_list[t] = sub_cnt
                                else:
                                    original_cnt = sub_cnt
                                    sub_cnt = main_cnt_list[t]
                                    decide_flag = True
                                    filtered_main_cnt_list[t] = original_cnt
                                    decide_day = 1
                        elif decide_flag==True:
                            filtered_main_cnt_list[t] = original_cnt
                            if main_cnt_list[t]==sub_cnt:
                                decide_day += 1
                                if decide_day>=decide_param:
                                    decide_flag = False
                                    original_cnt = sub_cnt
                                    back_cnt_list = cnt_all_list[:(cnt_all_list.index(sub_cnt))]
                            elif main_cnt_list[t]==original_cnt:
                                decide_flag = False
                                sub_cnt = main_cnt_list[t]
                            else:
                                sub_cnt = main_cnt_list[t]  
                    else:
                        filtered_main_cnt_list[t] = main_cnt_list[t]
                        original_cnt = main_cnt_list[t]
                        sub_cnt = main_cnt_list[t]
                        back_cnt_list = cnt_all_list[:(cnt_all_list.index(sub_cnt))]
                        decide_flag = False 
                filter_main_cnt = pd.Series(filtered_main_cnt_list,index=max_oi_cnt.index)
                filter_main_cnt.name = cmt
                main_cnt_series_list.append(filter_main_cnt)
        main_cnt_df = pd.concat(main_cnt_series_list,axis=1)
        return main_cnt_df


    @staticmethod
    def compute_smoothed_main_price(single_update=False):
        if not single_update:
            print(u"开始更新主力合约平滑连续价格")      
            main_cnt_df = Main_Cnt.get_main_cnt(mode="local")
        else:            
            main_cnt_df = Main_Cnt.get_local_single_main_cnt()        
        cmt_list = main_cnt_df.columns.tolist()
        smoothed_series = []        
        for cmt in cmt_list:
            cnt_df = QuoteData.Daily.get_cmt_quote("close", cmt, mode="local")
            main_cnt_series = main_cnt_df[cmt].dropna()
            cnt_ret_df = cnt_df.pct_change()
            main_ret_series = pd.Series(np.zeros(len(main_cnt_series)), index=main_cnt_series.index)
            for tdate in main_cnt_series.index:
                main_ret_series.loc[tdate] = cnt_ret_df.loc[tdate, main_cnt_series.loc[tdate]]
            main_ret_series += 1
            main_ret_series.iloc[0] = cnt_df.loc[main_ret_series.index[0], main_cnt_series.iloc[0]]
            main_price = main_ret_series.cumprod()
            main_price.name = cmt
            smoothed_series.append(main_price)
        smoothed_df = pd.concat(smoothed_series,axis=1, sort=False)
        if not single_update:
            smoothed_df.to_csv(Main_Cnt.relative_db_path + "main_cnt/main_cnt_smoothed_price.csv")
            print(u"主力合约平滑连续价格更新完毕")
        else:
            smoothed_df.to_csv(Main_Cnt.relative_db_path + "main_cnt/single_update/main_cnt_smoothed_price.csv")
        return smoothed_df    

    
    @staticmethod
    def update_local_main_cnt(update_end_date, single_update=False, decide_param=2):
        if not single_update:
            main_cnt_df = Main_Cnt.get_main_cnt(mode="local")
        else:
            main_cnt_df = Main_Cnt.get_local_single_main_cnt()
            
        cmt_list = main_cnt_df.columns.tolist()
        start_date = main_cnt_df.index[-1] + timedelta(days=1)
        end_date = datetime.strptime(update_end_date,"%Y-%m-%d").date()
        if start_date > end_date:
            print("主力合约更新日期错误，无法更新主力合约数据")
            return None
        else:    
            start_date = main_cnt_df.index[-decide_param]
            main_cnt_series_list = []  
            for cmt in cmt_list:
                print(cmt + u"开始更新主力合约")
                cnt_data = Cnt_Data.generate_effective_cnt_df(cmt, datetime(start_date.year, start_date.month, start_date.day),
                                                              datetime(end_date.year, end_date.month, end_date.day))
                cnt_data["contract_issue_date"] = Trade_Date.timestamp2date(cnt_data["contract_issue_date"].tolist())
                cnt_data["last_trade_date"] = Trade_Date.timestamp2date(cnt_data["last_trade_date"].tolist())
                if start_date < cnt_data["contract_issue_date"].iloc[0]:
                    base_date = cnt_data["contract_issue_date"].iloc[0] + timedelta(days=1)
                else:
                    base_date = start_date
                # 导入有效合约及持仓量
                effective_cnt = cnt_data.copy()
                cnt_all_list = list(cnt_data.index)
                oi_data = QuoteData.Daily.get_cmt_quote("open_interest", cmt, mode="local")
                oi_data.index = Trade_Date.timestamp2date(oi_data.index.tolist())
                oi_data = oi_data[oi_data.index >= base_date]
                oi_data = oi_data[cnt_all_list].dropna(how="all").fillna(0)
                
                # 处理无效持仓数据
                for cnt in cnt_all_list:
                    last_trade_date = effective_cnt.loc[cnt,"last_trade_date"]
                    if last_trade_date in oi_data.index:
                        oi_data.loc[oi_data.index>last_trade_date,cnt] = 0
                    first_trade_date = effective_cnt.loc[cnt,"contract_issue_date"]
                    if first_trade_date in oi_data.index:
                        oi_data.loc[oi_data.index<first_trade_date,cnt] = 0
                
                #找最大持仓量合约
                max_oi_cnt_f = lambda x: x.idxmax()
                max_oi_cnt = oi_data.apply(max_oi_cnt_f,axis=1)
                # 计算主力合约
                filter_main_cnt = Main_Cnt.compute_main_cnt_by_oi(cmt, max_oi_cnt, effective_cnt, main_cnt_df, decide_param)
                filter_main_cnt.name = cmt
                main_cnt_series_list.append(filter_main_cnt)
#                print cmt + "主力合约数据更新完毕"
            update_main_df = pd.concat(main_cnt_series_list,axis=1)
            update_main_df = update_main_df[~update_main_df.index.duplicated()]
            if not single_update:
                update_main_df.to_csv(Main_Cnt.tmp_filename, mode="a", header=None)
            else:
                update_main_df.to_csv(Main_Cnt.relative_db_path + "main_cnt/single_update/main_cnt_total.csv", 
                                      mode="a", header=None)
        return update_main_df
    
    @staticmethod
    def daily_update_main_cnt_and_smoothed_price(update_date):
        Main_Cnt.update_local_main_cnt(update_date)
        Main_Cnt.compute_smoothed_main_price()
        
    @staticmethod
    def daily_update_specail_main_cnt_and_smoothed_price(update_date):
        Main_Cnt.update_local_main_cnt(update_date, single_update=True)
        Main_Cnt.compute_smoothed_main_price(single_update=True)


###############################################################################
    @staticmethod
    def active_cmt_distributed_table_2_clustered():
        main_cnt_df = Main_Cnt.get_main_cnt(index_type="timestamp", mode="local")
        stack_main_cnt_ts = main_cnt_df.stack()
        stack_main_cnt_ts.name = "contract"
        stack_main_cnt_ts.index.names = ["date", "cmt"]
        smoothed_price_df = Main_Cnt.get_local_main_cnt_smoothed_price(index_type="timestamp")
        stack_smoothed_price_ts = smoothed_price_df.stack()
        stack_smoothed_price_ts.name = "smoothed_price"
        stack_smoothed_price_ts.index.names = ["date", "cmt"]
        total_df = pd.concat([stack_main_cnt_ts, stack_smoothed_price_ts], axis=1)
        total_df = total_df.reset_index()
        return total_df

    @staticmethod
    def single_cmt_distributed_table_2_clustered():
        main_cnt_df = Main_Cnt.get_local_single_main_cnt(index_type="timestamp")
        stack_main_cnt_ts = main_cnt_df.stack()
        stack_main_cnt_ts.name = "contract"
        stack_main_cnt_ts.index.names = ["date", "cmt"]
        smoothed_price_df = Main_Cnt.get_local_single_main_cnt_smoothed_price(index_type="timestamp")
        stack_smoothed_price_ts = smoothed_price_df.stack()
        stack_smoothed_price_ts.name = "smoothed_price"
        stack_smoothed_price_ts.index.names = ["date", "cmt"]
        total_df = pd.concat([stack_main_cnt_ts, stack_smoothed_price_ts], axis=1)
        total_df = total_df.reset_index()
        return total_df
    
    @staticmethod
    def type_translate(ts):
        if "date" in ts.index:
            ts["date"] = ts["date"].to_pydatetime()
        if "smoothed_price" in ts.index:
            ts["smoothed_price"] = float(ts["smoothed_price"])      
        return ts
    
    @staticmethod
    def cmt_upload_table(total_table_df, mode):
        total_table_df["date"] = [x.to_pydatetime() for x in total_table_df["date"]]
        session = sessionmaker()
        session.configure(bind=sql_main_cnt.engine)
        s = session()
        try:
            if mode == "replace":
                sql_main_cnt.SQL_Main_Cnt_Data.__table__.drop(sql_main_cnt.engine)
                sql_main_cnt.SQL_Main_Cnt_Data.__table__.create(sql_main_cnt.engine)
            for i in range(len(total_table_df)):  
                tmp_ts = total_table_df.iloc[i,:].copy()
                tmp_ts = Main_Cnt.type_translate(tmp_ts)
                record = sql_main_cnt.SQL_Main_Cnt_Data(**dict(tmp_ts))
                s.add(record)
            s.commit() #Attempt to commit all the records
        except Exception as e:
            print(repr(e))
            s.rollback() #Rollback the changes on error
            raise e
        finally:
            s.close() #Close the connection
        return

    @staticmethod
    def update_sql_main_cnt_and_smoothed_price():
        df = Main_Cnt.active_cmt_distributed_table_2_clustered()
        print(u"开始更新主力合约数据库")
        Main_Cnt.cmt_upload_table(df, mode="replace")
        print(u"主力合约数据库更新完毕")
        
    @staticmethod
    def update_sql_special_main_cnt_and_smoothed_price():
        df = Main_Cnt.single_cmt_distributed_table_2_clustered()
        print(u"开始更新特殊主力合约数据库")
        df = df.interpolate()
        Main_Cnt.cmt_upload_table(df, mode="append")
        print(u"特殊主力合约数据库更新完毕")
    
    @staticmethod
    def sql_get_main_cnt():
        session = sessionmaker()
        session.configure(bind=sql_main_cnt.engine)
        s = session()
        class_variable = sql_main_cnt.SQL_Main_Cnt_Data 
        try:
                       
            tmp_query = s.query(class_variable.cmt, class_variable.date, class_variable.contract)
            tmp_df = pd.read_sql(tmp_query.statement, sql_main_cnt.engine, index_col=["date", "cmt"])
            tmp_df = tmp_df.unstack()
            tmp_df.columns = [x[1] for x in tmp_df.columns]
        except Exception as e:
            print(repr(e))
            s.rollback()
            raise e
        finally:
            s.close()            
        return tmp_df
        
    
if __name__ == "__main__":
    update_date = "2018-10-08"
#    update_main_df = Main_Cnt.update_local_main_cnt(update_date, single_update=True)
#    df = Main_Cnt.compute_soomthed_main_price(single_update=True)
    
#    base_date = "2007-06-06"
#    end_date = "2018-07-13" 
#    df = Main_Cnt.main_cnt_construct(["OI.CZC"], base_date, end_date)
#    df.to_csv(Main_Cnt.relative_db_path + "main_cnt/single_update/main_cnt_total.csv")
#    df = Main_Cnt.compute_soomthed_main_price(single_update=True)
    df = Main_Cnt.update_local_main_cnt(update_date)
#    Main_Cnt.daily_update_specail_main_cnt_and_smoothed_price(update_date)
    
#    df1 = Main_Cnt.active_cmt_distributed_table_2_clustered()
#    df2 = Main_Cnt.single_cmt_distributed_table_2_clustered()
    
#    Main_Cnt.sql_update_main_cnt_and_smoothed_price()
#    Main_Cnt.sql_update_specail_main_cnt_and_smoothed_price()
        
#    tmp_df = Main_Cnt.sql_get_main_cnt()    
        
        
        
        
        
        
        
        
        
        