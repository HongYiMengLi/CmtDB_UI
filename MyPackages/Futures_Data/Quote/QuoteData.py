# -*- coding: utf-8 -*-
"""
Created on Fri Jun 22 13:51:19 2018

@author: 李弘一萌
"""

import pandas as pd
import numpy as np
import os
from datetime import datetime,date,timedelta
from ...Data_API.Wind.WindAPI import wind
from ...Data_API.Wind.WindError import WindError, EmptyError
from ...Data_Path.data_path import Data_Path
from ..Profile.CmtData import Cmt_Data
from ..Profile.CntData import Cnt_Data
from ..DateTime.Trade_Date import Trade_Date
from ...SQL.Table_Create import sql_daily_quote
from ...SQL.SQL_Connection import SQL_Connection

from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_
from sqlalchemy import MetaData, Table
from sqlalchemy import Column, Integer, String, DateTime, Float



def medium_output(update_list,update_date_df,my_mode):
    if len(update_list) != 0:
        tmp_update_df = pd.concat(update_list, sort=False)
        tmp_update_df.to_csv(QuoteData.Daily.relative_local_path + "tmp_update.csv", mode=my_mode)
    update_date_df.to_csv(QuoteData.Daily.relative_local_path + "cmt_daily_updated_date_log.csv")
    return tmp_update_df


def check_exist_in_original_index(new_df, original_df):
    filtered_index_list = []
    for index in new_df.index.tolist():
        if index not in original_df.index.tolist():
            filtered_index_list.append(index)
    filtered_new_df = new_df.loc[filtered_index_list, :].copy()
    return filtered_new_df


class QuoteData(object):
    """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    class Daily(object):        
        relative_local_path = Data_Path.relative_local_db_path() + "daily_data/"
        key_list = ["date", "contract"]
        field_list = ["open_interest", "close", "volume", "high", "low", "open", "settle"]
        field_code_list = ["oi", "close", "volume", "high", "low", "open", "settle"]
        field_dict = dict(zip(field_list, field_code_list))
        field_reverse_dict = dict(zip(field_code_list, field_list))
        default_mode = "db"
        
        
        ########################################################################################################################
        # 提取日度行情数据  
        
        
        @staticmethod
        def get_cmt_quote(field, cmt, month=None, year=None, mode=default_mode):
            if mode == "local":
                cmt_profile = Cmt_Data.get_cmt_profile()
                cmt_obj = Cmt_Data(cmt, cmt_profile)
                tmp_file_name =  QuoteData.Daily.relative_local_path + field + "/" + cmt_obj.cmt_name + ".csv" 
                tmp_df = pd.read_csv(tmp_file_name, index_col=0, parse_dates=[0])

            elif mode == "db":
                session = sessionmaker()
                session.configure(bind=sql_daily_quote.engine)
                s = session()
                class_variable = sql_daily_quote.SQL_Daily_Quote_Data 
                field_variable = eval("sql_daily_quote.SQL_Daily_Quote_Data." + field)
                try:                               
                    tmp_query = s.query(class_variable.date, class_variable.contract, field_variable).filter(class_variable.cmt == cmt)
                    tmp_df = pd.read_sql(tmp_query.statement, sql_daily_quote.engine, index_col=["date", "contract"])
                    tmp_df = tmp_df.unstack()
                    tmp_df.columns = [x[1] for x in tmp_df.columns]
                except Exception as e:
                    print(repr(e))
                    s.rollback()
                    raise e
                finally:
                    s.close()
            else:
                return None
            
            # 处理年月筛选条件
            if (not month) and (not year):
                return tmp_df
            else:
                cmt_profile, cnt_profile = Cnt_Data.get_profile()
                cnt_obj_list = [Cnt_Data(x, cmt_profile, cnt_profile) for x in tmp_df.columns.tolist()]
                if month:
                    cnt_obj_list = [x for x in cnt_obj_list if int(x.cnt_month) == month]
                if year:
                    cnt_obj_list = [x for x in cnt_obj_list if int(x.cnt_year) == year]
                tmp_df_new = tmp_df[[x.cnt_code for x in cnt_obj_list]].copy()
                return tmp_df_new
        

        
        
        @staticmethod
        def get_cmt_from_cnt(field, cnt, mode=default_mode):
            cmt_profile, cnt_profile = Cnt_Data.get_profile()
            cnt_obj = Cnt_Data(cnt, cmt_profile, cnt_profile)
            cmt_df = QuoteData.Daily.get_cmt_quote(field, cnt_obj.cmt_code, mode)
            return cmt_df
        

        @staticmethod
        def get_cnt_series(field, cnt, mode=default_mode):
            cmt_profile, cnt_profile = Cnt_Data.get_profile()
            cnt_obj = Cnt_Data(cnt, cmt_profile, cnt_profile)
            cmt_df = QuoteData.Daily.get_cmt_from_cnt(field, cnt, mode)
            cnt_series = cmt_df[cnt_obj.cnt_code]
            return cnt_series
        
        @staticmethod
        def get_local_cmt_last_updated_date_df():
            tmp_file_name =  QuoteData.Daily.relative_local_path + "cmt_daily_updated_date_log.csv"
            updated_df = pd.read_csv(tmp_file_name,index_col=0, parse_dates=[1])
            return updated_df

        @staticmethod
        def get_cnt_quote_for_date():
            tmp_file_name =  QuoteData.Daily.relative_local_path + "cmt_daily_updated_date_log.csv"
            updated_df = pd.read_csv(tmp_file_name,index_col=0,parse_dates=[1])
            return updated_df
        
        ########################################################################################################################
        # 编辑或修改日度行情数据          
        
        @staticmethod
        def set_local_cmt(field, cmt, tmp_df):
            cmt_profile = Cmt_Data.get_cmt_profile()
            cmt_obj = Cmt_Data(cmt, cmt_profile)
            tmp_file_name =  QuoteData.Daily.relative_local_path + field + "/" + cmt_obj.cmt_name + ".csv" 
            tmp_df.to_csv(tmp_file_name)
            return tmp_df
        
        @staticmethod
        def delete_date_row(tmp_df, date_list):
            for date1 in date_list:
                if date1 in tmp_df.index:
                    tmp_df.drop(date1, inplace=True)
            return tmp_df

        
        @staticmethod
        def delete_date_row_for_cmt(date_list, field_list=None, cmt_list=None):
            if cmt_list is None:
                cmt_list = Cmt_Data.get_cmt_list()
            if field_list is None:
                field_list = QuoteData.Daily.field_list
            date_list = [pd.Timestamp(x) for x in date_list]
            for field in field_list:
                for cmt in cmt_list:
                    tmp_df = QuoteData.Daily.get_cmt_quote(field, cmt, mode="local")
                    tmp_df = QuoteData.Daily.delete_date_row(tmp_df, date_list)
                    QuoteData.Daily.set_local_cmt(field, cmt, tmp_df)
                    print(field + " " + cmt + u"删除完毕")
            return
        
        @staticmethod
        def delete_after_date(df, last_date):
            tmp_df = df[df.index <= last_date].copy()
            return tmp_df
        
        
        # single cmt adding a new field
        @staticmethod
        def new_field_local(cmt, new_field_list):
            wind.start_wind()
            tmp_newest_date = Trade_Date.get_newest_date()
            tmp_cnt_df = Cnt_Data.get_cnt_profile_given_cmt(cmt)
            tmp_field_dict = dict(zip(new_field_list,[[] for x in range(len(new_field_list))]))
            for code in tmp_cnt_df.index.tolist():
                start_date = tmp_cnt_df.loc[code,"contract_issue_date"]
                end_date = tmp_cnt_df.loc[code,"last_trade_date"]
                tmp_field_df = wind.wsd(code, new_field_list, start_date, end_date)
                for field in new_field_list:
                    tmp_field_series = tmp_field_df[field.upper()].copy()
                    tmp_field_series.name = code
                    tmp_field_dict[field].append(tmp_field_series)
                print(code + u"下载完毕")
            for field in new_field_list:
                tmp_df = pd.concat(tmp_field_dict[field], axis=1, sort=False)
                tmp_df = QuoteData.Daily.delete_after_date(tmp_df, tmp_newest_date)
                tmp_file_name = QuoteData.Daily.relative_local_path + field + "/" + cmt[:-4] + ".csv"
                tmp_df.to_csv(tmp_file_name)
            return
        
        
        # To be continued
        @staticmethod
        def new_cmt_local(new_cmt_list):

            return
        

        @staticmethod
        def delete_duplicate_date(cmt_list=None, field_list=None):
            if cmt_list == None:
                # 默认所有field
                cmt_list = Cmt_Data.get_cmt_list()            
            if field_list == None:
                # 默认所有field
                field_list = QuoteData.Daily.field_list
            for field in field_list:
                for cmt in cmt_list:
                    tmp_original_quote = QuoteData.Daily.get_cmt_quote(field, cmt, mode="local")
                    tmp_new_quote = tmp_original_quote[~tmp_original_quote.index.duplicated(keep='first')]
                    QuoteData.Daily.set_local_cmt(field, cmt, tmp_new_quote)
            print("删除重复行完毕")
            return

        
        @staticmethod
        def new_local_cmt_updated_tdate():
            cmt_list = Cmt_Data.get_cmt_list()   
            tmp_file_name =  QuoteData.Daily.relative_local_path + "cmt_daily_updated_date_log.csv"
            tmp_last_update_date_list = []
            for cmt in cmt_list:
                cmt_df = QuoteData.Daily.get_cmt_quote("close", cmt, mode="local")
                tmp_last_update_date_list.append(cmt_df.index[-1])
            cmt_updated_df = pd.DataFrame([tmp_last_update_date_list],columns=cmt_list,index=["last_updated_date"]).T
            cmt_updated_df.to_csv(tmp_file_name)
            return cmt_updated_df
        
        # 下载日度行情数据
        @staticmethod
        def update_daily_table(update_end_date, tmp_field_list=field_list):
            wind.start_wind()
            print(u"开始下载日度行情数据")
            # 制作行情字段列表以供下载时使用
            tmp_field_code_list = [QuoteData.Daily.field_dict[field] for field in tmp_field_list]
            # 处理输入更新截止日期参数的类型，使其保持date类型
#            if (type(update_end_date) == str) or (type(update_end_date) == unicode):
            if (type(update_end_date) == str):
                update_end_date = datetime.strptime(str(update_end_date),"%Y-%m-%d").date()
            # 载入所有合约列表
            cmt_list = Cmt_Data.get_cmt_list()
            # 初始化记录下载好的各个品种行情数据df的列表
            update_quote_df_list = []
            # 导入记录各品种上次更新截止日期的文件
            last_update_date_df = QuoteData.Daily.get_local_cmt_last_updated_date_df().copy()
            # 导入存储每日更新数据的临时文件
            # 先初始化其文件path
            update_df_filename = QuoteData.Daily.relative_local_path + "/tmp_update.csv"
            # 若存在该文件，则该文件应为上一日的临时更新数据或是今日未更新完的数据文件
            if os.path.exists(update_df_filename):
                tmp_update_quote_df = pd.read_csv(update_df_filename, index_col=0, parse_dates=[0])
                tmp_update_quote_date = tmp_update_quote_df.index[0].to_pydatetime().date()
                # 通过比较第一个品种的更新日期判断本次导入的是昨天的还是今天（假设每天更新好后所有品种的更新日期应该都一致）
                if tmp_update_quote_date == update_end_date:
                    # 如果与今天的日期相同则继续更新
                    my_mode = "a"
                else:
                    # 否则覆盖
                    my_mode = "w"
            else:
                # 无更新文件的话直接写
                my_mode = "w"
            # 开始对各品种循环下载
            for cmt in cmt_list:
                # 取得品种上次更新截止日期
                if cmt in last_update_date_df.index:
                    last_update_date = last_update_date_df.loc[cmt, "last_updated_date"].to_pydatetime().date()
                else:
                    last_update_date = datetime.today().date() + timedelta(days=-1)
                # 如果发现截止日期与更新日期一致，则说明已经更新过
                if last_update_date >= update_end_date:
                    print(cmt + u"日度行情已更新过")
                else:
                    # 取得品种当日有效合约（在每日更新合约列表文件中获得更新，该文件执行次序在前，因此这里已经更新好今日的有效合约，只需提取）
                    tmp_cnt_list = Cnt_Data.get_effective_cnt_list(cmt, mode="local")
                    # 初始化合约更新数据df列表
                    tmp_cnt_quote_df_list = []
                    # 设置更新起始日期为上个更新截止日期的下一日
                    update_start_date = last_update_date + timedelta(days=1)
                    a=0
                    # 循环合约进行下载
                    for cnt in tmp_cnt_list:
                        try:
                            # 下载合约盘面数据，以日期为行，字段为列的格式组织
                            tmp_cnt_quote_df = wind.wsd(cnt, tmp_field_code_list, update_start_date, update_end_date)
                        except WindError as we:
                            # 下载出现错误时，先对目前已更新品种的更新日期和更新数据进行存储，以便下次继续使用
                            print(cnt + " " + we.errorinfo)
                            medium_output(update_quote_df_list, last_update_date_df, my_mode)
                            raise
                        except EmptyError as ee:
                            # 若出现无数据合约时，理论上可以跳过该合约继续下载，但因为之后在更新本地数据时会用的所有有效合约，这里跳过的话会
                            # 有问题因此用报错处理。一般日度行情即使无数据也会用nan更新，不太可能出现空数据的情况，假如出现说明万得还没更新
                            print(cnt + " " + ee.errorinfo)
                            medium_output(update_quote_df_list, last_update_date_df, my_mode)
                            raise
                        else:
                            # 无问题的话对下载的数据加上index名称“date”和cnt列，并加到合约数据df列表中
                            tmp_cnt_quote_df.index.name = "date"
                            tmp_cnt_quote_df["cmt"] = cmt
                            tmp_cnt_quote_df["contract"] = cnt                            
                            tmp_cnt_quote_df_list.append(tmp_cnt_quote_df)
                    # 如果有效合约为空，说明这段时间该品种没有有效合约，不需要更新（极端不常见，不过FU在2018-6-26时就出现了）
                    if len(tmp_cnt_quote_df_list) == 0:
                        print(cmt + u"本次日度行情更新所有合约无数据")
                    # 否则品种更新完毕，处理品种更新数据
                    else:
                        # 更新数据汇总为一个df并加入总更新列表
                        tmp_cnt_quote_df = pd.concat(tmp_cnt_quote_df_list, sort=False)
                        update_quote_df_list.append(tmp_cnt_quote_df)
                    # 无论是否有数据都认为更新完毕，更新时间记录，直接修改原df的更新时间
                    last_update_date_df.loc[cmt,"last_updated_date"] = update_end_date
                    print(cmt + u"日度行情下载完毕")
            print("") 
            # 所有品种都下载完毕后，输出更新日期和更新数据，日度行情下载模块结束
            if len(update_quote_df_list) != 0:
                tmp_update_df = medium_output(update_quote_df_list, last_update_date_df, my_mode)             
                return tmp_update_df
            else:
                print(u"全品种均更新过, 无需更新")
                return None


        # 下载完整日度行情数据
        @staticmethod
        def download_daily_table(cmt, field, start_date, end_date):
            wind.start_wind()
            print(cmt + " 开始下载日度行情数据")
            tmp_cnt_list = Cnt_Data.generate_effective_cnt_list(cmt, start_date, end_date)
                # 循环合约进行下载
            tmp_cnt_quote_df_list = []
            for cnt in tmp_cnt_list:
                try:
                    # 下载合约盘面数据，以日期为行，字段为列的格式组织
                    tmp_cnt_quote_df = wind.wsd(cnt, [field], start_date, end_date)
                except WindError as we:
                    # 下载出现错误时，先对目前已更新品种的更新日期和更新数据进行存储，以便下次继续使用
                    print(cnt + " " + we.errorinfo)
                    raise
                except EmptyError as ee:
                    # 若出现无数据合约时，理论上可以跳过该合约继续下载，但因为之后在更新本地数据时会用的所有有效合约，这里跳过的话会
                    # 有问题因此用报错处理。一般日度行情即使无数据也会用nan更新，不太可能出现空数据的情况，假如出现说明万得还没更新
                    print(cnt + " " + ee.errorinfo)
                    raise
                else:
                    # 无问题的话对下载的数据加上index名称“date”和cnt列，并加到合约数据df列表中
                    tmp_cnt_quote_df.columns = [cnt]
                    tmp_cnt_quote_df_list.append(tmp_cnt_quote_df)
                # 如果有效合约为空，说明这段时间该品种没有有效合约，不需要更新（极端不常见，不过FU在2018-6-26时就出现了）
            if len(tmp_cnt_quote_df_list) == 0:
                print(cmt + u"本次日度行情更新所有合约无数据")
                return None
            else:
                tmp_df = pd.concat(tmp_cnt_quote_df_list, axis=1, sort=False)
                return tmp_df

            
        @staticmethod
        def update_local_from_table(tmp_update_df=None, field_list=None):
            # 将下载的日度行情数据分不同field更新到本地csv中，使用的是新的本地数据文件夹。在数据库建设完成后需要被淘汰
#            wind.start_wind()
            print(u"开始更新本地日度数据")
            # 取得所有合约列表
            cmt_list = Cmt_Data.get_cmt_list()
            if field_list == None:
                # 默认所有field
                field_list = QuoteData.Daily.field_list
            if tmp_update_df is None:
                # 默认从指定位置载入本次更新下载好的数据，必须要先下载完毕才能进行。 注意此处使用date和contract的multiindex便于unstack
                tmp_update_df = pd.read_csv(QuoteData.Daily.relative_local_path + "tmp_update.csv", index_col=[0, -1], parse_dates=[0])                
            # 分field进行分配
            cmt_profile, cnt_profile = Cnt_Data.get_profile()
#            cnt_obj = Cnt_Data(cnt, cmt_profile, cnt_profile)
            for field in field_list:
                # field在wind中使用的code
                field_code = QuoteData.Daily.field_dict[field]
                # 取得该field的更新series并延展成以日期为行、合约code为列的结构
                tmp_update_quote = tmp_update_df[field_code.upper()].unstack()
                cnt_list = tmp_update_quote.columns.tolist()
                cnt_obj_list = [Cnt_Data(x, cmt_profile, cnt_profile, update_flag=True) for x in cnt_list]
                cnt_cmt_list = [obj.cmt_code for obj in cnt_obj_list]
                cnt_cmt_df = pd.Series(cnt_cmt_list, index=cnt_list)
                # 该series包含所有更新的合约，需要对其品种进行归类
                for cmt in cmt_list:
#                    # 这里简单使用本次下载时采用的合约列表直接提取。假如下载时所有有效合约都得以录入则不会出现问题，否则会出现找不到有些合约的情况
#                    tmp_cnt_list = Cnt_Data.get_effective_cnt_list(cmt)
                    tmp_cnt_list = cnt_cmt_df[cnt_cmt_df==cmt].index.tolist()
                    # 直接用有效合约列表取得该品种的更新数据
                    tmp_cmt_update_quote = tmp_update_quote[tmp_cnt_list].copy()
                    # 取得原数据df
                    tmp_original_quote = QuoteData.Daily.get_cmt_quote(field, cmt, mode="local")
                    tmp_cmt_update_quote = check_exist_in_original_index(tmp_cmt_update_quote, tmp_original_quote)
                    if len(tmp_cmt_update_quote) == 0:
                        continue
                    # 用df的append方法更新
                    tmp_new_quote = tmp_original_quote.append(tmp_cmt_update_quote)
                    # 此时若有新的合约出现需要调整合约位置，Contract类重载了cmp函数因此可以直接sort
                    tmp_cnt_list = tmp_new_quote.columns.tolist()
                    tmp_cnt_list = [Cnt_Data(x, cmt_profile, cnt_profile, update_flag=True) for x in tmp_cnt_list]
                    tmp_cnt_list.sort()
                    tmp_cnt_list = [x.cnt_code for x in tmp_cnt_list]
                    tmp_new_quote = tmp_new_quote[tmp_cnt_list]
                    # 输出到对应本地文件
                    QuoteData.Daily.set_local_cmt(field, cmt, tmp_new_quote)
#                    print field + " " + cmt + u"本地日度盘面更新完毕"
            return 
        
###############################################################################
        # SQL functions
        
        # 所有local转单独df
        @staticmethod
        def distributed_table_2_clustered():
            cmt_list = Cmt_Data.get_cmt_list()
            cmt_transformed_list = []
            for cmt in cmt_list:
                cmt_ts_list = []
                print(cmt)
                for field in QuoteData.Daily.field_list:
                    tmp_df = QuoteData.Daily.get_cmt_quote(field, cmt, mode="local")
                    stack_ts = tmp_df.stack()
                    stack_ts = stack_ts[~stack_ts.index.duplicated()]
                    stack_ts.name = field
                    cmt_ts_list.append(stack_ts)
                    print(field)
                cmt_df = pd.concat(cmt_ts_list, axis=1, sort=False)
                cmt_df.index.names = ["date", "contract"]
                cmt_df["cmt"] = cmt
                cmt_df = cmt_df.dropna(how="all")
                cmt_transformed_list.append(cmt_df)
            total_df = pd.concat(cmt_transformed_list, sort=False)
            return total_df
        
        # 上传单独df
        @staticmethod
        def upload_table(total_table_df, chunksize=40000):
            for i in range(0, len(total_table_df), chunksize):
                print(i)
                tmp_table_df = total_table_df.iloc[i:(i+chunksize), :]
                session = sessionmaker()
                session.configure(bind=sql_daily_quote.engine)
                s = session()
                try:
                    tmp_table_df.to_sql("daily_quote", sql_daily_quote.engine, if_exists="append")
                    s.commit() #Attempt to commit all the records
                except Exception as e:
                    print(repr(e))
                    s.rollback() #Rollback the changes on error
                    raise e
                finally:
                    s.close() #Close the connection
            return
        
        @staticmethod
        def type_translate(ts):
            if "open_interest" in ts.index:
                ts["open_interest"] = int(ts["open_interest"])
            if "volume" in ts.index:
                ts["volume"] = int(ts["volume"])
            if "high" in ts.index:
                ts["high"] = float(ts["high"])
            if "low" in ts.index:
                ts["low"] = float(ts["low"])
            if "close" in ts.index:
                ts["close"] = float(ts["close"])
            if "open" in ts.index:
                ts["open"] = float(ts["open"])
            if "settle" in ts.index:
                ts["settle"] = float(ts["settle"])                
            return ts
        
        @staticmethod
        def update_sql_daily_quote_table(tmp_table_df=None):
            print(u"开始更新日度盘面数据库...")
            if tmp_table_df is None:
                tmp_table_df = pd.read_csv(QuoteData.Daily.relative_local_path + "tmp_update.csv", 
                                            index_col=["date","contract"])
            tmp_table_df.columns = [QuoteData.Daily.field_reverse_dict[x.lower()] if x != "cmt" else "cmt" for x in tmp_table_df.columns]
            tmp_table_df.index.names = ["date", "contract"]
            tmp_table_df = tmp_table_df.reset_index()
            
            session = sessionmaker()
            session.configure(bind=sql_daily_quote.engine)
            s = session()
            try:
                for i in range(len(tmp_table_df)):  
                    tmp_ts = tmp_table_df.iloc[i,:].dropna()
                    tmp_ts = QuoteData.Daily.type_translate(tmp_ts)
                    record = sql_daily_quote.SQL_Daily_Quote_Data(**dict(tmp_ts))
                    s.merge(record)
                s.commit() #Attempt to commit all the records
            except Exception as e:
                print(repr(e))
                s.rollback() #Rollback the changes on error
                raise e
            finally:
                s.close() #Close the connection
            print(u"日度盘面数据库更新完毕")
            return

    
        @staticmethod
        def sql_get_cnt_quote_for_date(cnt_list, field, tdate):
            session = sessionmaker()
            session.configure(bind=sql_daily_quote.engine)
            s = session()
            class_variable = sql_daily_quote.SQL_Daily_Quote_Data 
            field_variable = eval("sql_daily_quote.SQL_Daily_Quote_Data." + field)
            try:
                           
                tmp_query = s.query(class_variable.contract, field_variable).filter(and_(class_variable.contract\
                                    .in_(cnt_list), class_variable.date == tdate))
                tmp_df = pd.read_sql(tmp_query.statement, sql_daily_quote.engine, index_col=["contract"])
                tmp_df.columns = [tdate]
            except Exception as e:
                print(repr(e))
                s.rollback()
                raise e
            finally:
                s.close()                
            return tmp_df  
        
    """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    class Minute(object):
        relative_local_path = Data_Path.relative_local_db_path() + "minute_data/"
        key_list = ["time","contract"]
        field_list = ["open_interest","close","volume","high","low","open"]
        field_code_list = ["oi","close","volume","high","low","open"]
        field_dict = dict(zip(field_list,field_code_list))      
        field_reverse_dict = dict(zip(field_code_list, field_list))
        upload_engine = SQL_Connection.get_connection("minute_quote", charset="utf8")  

        
        
        @staticmethod
        def update_minute_table_from_last_date(update_end_date, tmp_field_list=None):
            if tmp_field_list == None:
                # 默认所有field
                tmp_field_list = QuoteData.Minute.field_list
            tmp_field_code_list = [QuoteData.Minute.field_dict[field] for field in tmp_field_list]
            # 处理输入更新截止日期参数的类型，使其保持str类型
            if (type(update_end_date) == date) or (type(update_end_date) == datetime):
                update_end_date = update_end_date.strftime("%Y-%m-%d")
            # 载入所有合约列表
            cmt_list = Cmt_Data.get_cmt_list()
            # 初始化记录下载好的各个品种行情数据df的列表
            update_quote_df_list = []
            # 导入记录各品种上次更新截止日期的文件
            update_start_date = Trade_Date.get_last_tdate(update_end_date).strftime("%Y-%m-%d")
            update_start_time = update_start_date + " 20:59:00"
            update_end_time = update_end_date + " 15:16:00"
            # 导入存储每日更新数据的临时文件
            # 先初始化其文件path
            update_df_filename = QuoteData.Minute.relative_local_path + "/" + update_end_date + ".csv"
            for cmt in cmt_list:
                print(cmt)
                if cmt == "SC.INE":
                    continue
#                tmp_cnt_list = Cnt_Data.get_effective_cnt_list(cmt)    
                tmp_cnt_list = Cnt_Data.generate_effective_cnt_list(cmt, update_end_date, update_end_date)
                tmp_cnt_quote_df_list = []
                # 循环合约进行下载
                for cnt in tmp_cnt_list:
                    try:
                        # 下载合约盘面数据，以日期为行，字段为列的格式组织
                        tmp_cnt_quote_df = wind.wsi(cnt,tmp_field_code_list,update_start_time,update_end_time)
                        tmp_cnt_quote_df.columns = tmp_field_list
                    except WindError as we:
                        # 下载出现错误时，先对目前已更新品种的更新日期和更新数据进行存储，以便下次继续使用
                        if we.errorcode == -40520007:
                            continue
                        else:
                            print(cnt + " " + we.errorinfo)
                            raise
#                    except EmptyError as ee:
#                        # 若出现无数据合约时，理论上可以跳过该合约继续下载，但因为之后在更新本地数据时会用的所有有效合约，这里跳过的话会
#                        # 有问题因此用报错处理。一般日度行情即使无数据也会用nan更新，不太可能出现空数据的情况，假如出现说明万得还没更新
#                        print cnt + " " + ee.errorinfo
#                        raise
                    else:
                        # 无问题的话对下载的数据加上index名称“date”和cnt列，并加到合约数据df列表中
                        tmp_cnt_quote_df.dropna(how="all",inplace=True)
                        if len(tmp_cnt_quote_df) != 0:
                            tmp_cnt_quote_df.index.name = "time"
                            tmp_cnt_quote_df["contract"] = cnt
                            tmp_cnt_quote_df_list.append(tmp_cnt_quote_df)
                if len(tmp_cnt_quote_df_list) == 0:
                    print(cmt + u"本次分钟行情更新所有合约无数据")
                else:
                    print(cmt + u"分钟行情下载完毕")
                    tmp_cnt_quote_df = pd.concat(tmp_cnt_quote_df_list, sort=False)
                    update_quote_df_list.append(tmp_cnt_quote_df)
            tmp_update_df = pd.concat(update_quote_df_list, sort=False)
            tmp_update_df.sort_index(inplace=True)
            
            tmp_update_df.to_csv(update_df_filename)
            return tmp_update_df
                    
        @staticmethod
        def update_local_from_table(tmp_update_df=None):
            update_df_filename = QuoteData.Minute.relative_local_path + "/tmp_update.csv"
            if tmp_update_df is None:
                # 默认从指定位置载入本次更新下载好的数据，必须要先下载完毕才能进行。 注意此处使用date和contract的multiindex便于unstack
                tmp_update_df = pd.read_csv(update_df_filename, index_col=0, parse_dates=[0])
            original_df_filename = QuoteData.Minute.relative_local_path + "/minute.csv"
            tmp_update_df.to_csv(original_df_filename,mode="a")
            return      
        
        @staticmethod
        def upload_table(tmp_date, tmp_table_df=None):
            print(u"开始更新分钟盘面数据库...")
            if tmp_table_df is None:
                tmp_table_df = pd.read_csv(QuoteData.Minute.relative_local_path + tmp_date + ".csv", 
                                            index_col=["time","contract"])
            
#            tmp_table_df.columns = [QuoteData.Minute.field_reverse_dict[x.lower()] for x in tmp_table_df.columns]
            tmp_table_df.index.names = ["time", "contract"]
            tmp_table_df = tmp_table_df[~tmp_table_df.index.duplicated()]
            tmp_table_df = tmp_table_df.reset_index()
            
            table_name = tmp_date
            metadata = MetaData()        
            table_object = Table(table_name, metadata,
                Column("time", DateTime, primary_key=True),                 
                Column("contract", String(50), primary_key=True),        
                Column("open_interest", Integer, nullable=True),
                Column("open", Float, nullable=True),
                Column("high", Float, nullable=True),
                Column("low", Float, nullable=True),
                Column("close", Float, nullable=True),
                Column("volume", Integer, nullable=True)
            )            
            table_object.create(QuoteData.Minute.upload_engine)
            session = sessionmaker()
            session.configure(bind=QuoteData.Minute.upload_engine)
            s = session()
            tmp_dict = [x.to_dict() for _, x in tmp_table_df.iterrows()]
            try:
                s.execute(table_object.insert(), tmp_dict) 
                s.commit() #Attempt to commit all the records
                print(table_name + " 分钟数据上传完毕")
            except Exception as e:
                print(repr(e))
                s.rollback() #Rollback the changes on error
                raise e
            finally:
                s.close() #Close the connection  
                
        @staticmethod
        def sql_get_cnt_minute_quote(tmp_date, cnt, field):
            session = sessionmaker()
            session.configure(bind=QuoteData.Minute.upload_engine)
            s = session()

            
            try:
                sql_query = "select time, " + field + " from " + "`" + tmp_date + \
                            "`" + " where contract = \"" + cnt + "\"" 
                result = s.execute(sql_query)
#                tmp_query = s.query(table_object.time, table_object.contract, eval("table_object." + field)).filter(class_variable.contract \
#                                   == cnt)
                tmp_df = pd.DataFrame(list(result))
                if len(tmp_df) != 0:
                    tmp_df.columns = ["time", cnt]
                    tmp_df.set_index("time", inplace=True)
#                tmp_df = tmp_df.unstack()
#                tmp_df.columns = [x[1] for x in tmp_df.columns]
            except Exception as e:
                print(repr(e))
                s.rollback()
                raise e
            finally:
                s.close()
                
            return tmp_df                    
                    
                    
                    
                    
                    
                    
if __name__ == "__main__":
#    print QuoteData.relative_local_path
    cmt = "CF.CZC"
#    cnt = "AP810.CZC"
    field = "close"
    my_field_list = ["settle"]
#    df = QuoteData.Daily.get_local_cmt(field,cmt)
#    df = QuoteData.Minute.sql_get_cnt_minute_quote("2016-09-01", "CF701.CZC", "close")
#    QuoteData.Daily.new_local(field_list)
#    l = QuoteData.Daily.get_local_cnt("close","AP810.CZC")
#    df = QuoteData.Daily.new_local_cmt_updated_tdate()
#    t = QuoteData.Daily.get_local_cmt_last_updated_date("A.DCE")
    
#    tmp_update_df = QuoteData.Daily.daily_update_local("2018-06-26")
#    tmp_update_df = pd.read_csv(QuoteData.Daily.relative_local_path + "tmp_update.csv",index_col=[0,-1])
#    tmp = tmp_update_df["CLOSE"].unstack()
#    QuoteData.Daily.update_table()
    
#    QuoteData.Daily.delete_duplicate_date()
#    QuoteData.Daily.delete_date_row_for_cmt(["2018-07-17"]) 
    
#    df = QuoteData.Minute.update_minute_table_from_last_date("2018-6-27")
#    QuoteData.Minute.update_local_from_table()
    
#    df = QuoteData.Daily.distributed_table_2_clustered()
#    QuoteData.Daily.upload_table(df)
    
#    tmp_date = "2018-10-07"
#    df = pd.read_csv(QuoteData.Minute.relative_local_path + tmp_date + ".csv", 
#                     index_col=["time","contract"])
#    QuoteData.Minute.upload_table(tmp_date, df)
    
#    df = QuoteData.Daily.sql_get_cmt_daily_quote("PP.DCE", "close")

#    cmt = "IF.CFE"
#    df = QuoteData.Daily.download_daily_table(cmt, field, "2010-04-16", "2018-10-08")
    
    
    
    
    
    
    
    
    
    
    
    
    
    






    