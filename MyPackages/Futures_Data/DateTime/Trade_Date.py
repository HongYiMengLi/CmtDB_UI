# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 15:24:27 2018

@author: Administrator
"""

import pandas as pd
import numpy as np
from datetime import datetime,timedelta
from ...Data_API.Wind.WindAPI import wind
from ...Data_Path.data_path import Data_Path
from ...SQL.Table_Create import sql_trade_date
from sqlalchemy.orm import sessionmaker

class Trade_Date(object):
    relative_local_path = Data_Path.relative_local_db_path()
    file_name = relative_local_path + "others\\trade_date.csv"
    default_mode = "db"
    
    @staticmethod
    def timestamp2date(timestamp_list):
        date_list = [x.to_pydatetime().date() for x in timestamp_list]          
        return date_list    


    @staticmethod
    def timestamp2datetime(timestamp_list):
        datetime_list = [x.to_pydatetime() for x in timestamp_list]          
        return datetime_list  

    @staticmethod
    def date2datetime(date_list):
        datetime_list = [datetime(x.year, x.month, x.day) for x in date_list]          
        return datetime_list  
    
    @staticmethod
    def get_trade_date_df(parse=True, mode=default_mode):
        if mode == "local":
            tmp_file_name = Trade_Date.file_name
            if parse == True:
                tmp_df = pd.read_csv(tmp_file_name, index_col=0, parse_dates=[0])
            else:
                tmp_df = pd.read_csv(tmp_file_name, index_col=0)
        elif mode == "db":
            session = sessionmaker()
            session.configure(bind=sql_trade_date.engine)
            s = session()
            try:
                tmp_query = s.query(sql_trade_date.SQL_Trade_Date)
                tmp_df = pd.read_sql(tmp_query.statement, sql_trade_date.engine, index_col="trade_date")
            except Exception as e:
                print(repr(e))
                s.rollback()
                raise e
            finally:
                s.close()
        return tmp_df

    @staticmethod
    def get_trade_date_list(parse=True, mode=default_mode):
        tmp_df = Trade_Date.get_trade_date_df(parse=parse, mode=mode)
        tdate_list = [x.to_pydatetime() for x in tmp_df.index]
        return tdate_list    
    
    
    
    @staticmethod
    def get_newest_date():
        tdate_list = Trade_Date.get_trade_date_df(mode="local").index.tolist()
        return tdate_list[-1].to_pydatetime().date()  

    
    @staticmethod
    def get_update_date():
        today = datetime.today()
        if today.hour < 15:
            today -= timedelta(days=1)            
        return today.date()   

    @staticmethod
    def get_offset_tdate(today, offset_num=1, offset_period="D"):
        wind.start_wind()
        last_tdate = wind.tdate_offset(-offset_num, today, period=offset_period)            
        return last_tdate
    
    @staticmethod
    def get_last_tdate(today):
        wind.start_wind()
        last_tdate = wind.tdate_offset(-1, today)            
        return last_tdate

    @staticmethod
    def get_common_date_list(start_date, end_date):
        wind.start_wind()
        date_list = wind.commom_date_list(start_date, end_date)            
        return date_list

    @staticmethod
    def construct():
        wind.start_wind()
        last_tdate = Trade_Date.get_newest_date()
        update_date = Trade_Date.get_update_date()
        if update_date <= last_tdate:
            print("日期已更新完毕，无需再次更新")
            return None
        else:
            start_date = last_tdate + timedelta(days=1)
            update_list = wind.trade_date_list(start_date,update_date)
            trade_date_list = Trade_Date.get_trade_date_df().index.tolist()
            trade_date_list = Trade_Date.timestamp2date(trade_date_list)
            trade_date_list.extend(update_list)
            trade_date_df = pd.Series(index=trade_date_list)
            trade_date_df.to_csv(Trade_Date.file_name)
            print("交易日列表更新完毕")
            return trade_date_df
        
    @staticmethod
    def update_trade_date():
        wind.start_wind()
        last_tdate = Trade_Date.get_newest_date()
        update_date = Trade_Date.get_update_date()
        if update_date <= last_tdate:
            print("日期已更新完毕，无需再次更新")
            return Trade_Date.get_trade_date_df(mode="local")
        else:
            start_date = last_tdate + timedelta(days=1)
            update_list = wind.trade_date_list(start_date,update_date)
            trade_date_list = Trade_Date.get_trade_date_df().index.tolist()
            trade_date_list = Trade_Date.timestamp2date(trade_date_list)
            trade_date_list.extend(update_list)
            trade_date_df = pd.Series(index=trade_date_list)
            trade_date_df.to_csv(Trade_Date.file_name)
            print("交易日列表更新完毕")
            return trade_date_df
            

    # 上传sql前的类型转换操作
    @staticmethod
    def type_translate(ts):
        tmp_date = ts["trade_date"].to_pydatetime()
        tmp_dict = {"trade_date": tmp_date}          
        return tmp_dict
    
    
    # local cmt profile上传mysql数据库
    @staticmethod
    def upload_sql_trade_date():
        session = sessionmaker()
        session.configure(bind=sql_trade_date.engine)
        s = session()
        df =  Trade_Date.get_trade_date_df(mode="local")
        df.index.name="trade_date"
        df = df.reset_index().dropna(axis=1)
        try:    
            for i in range(len(df)):
                tmp_ts = df.iloc[i, :].copy()
                tmp_dict = Trade_Date.type_translate(tmp_ts)
                record = sql_trade_date.SQL_Trade_Date(**tmp_dict)
                s.add(record) #Add all the records    
            s.commit() #Attempt to commit all the records
        except Exception as e:
            print(repr(e))
            print("Trade Date Error")
            s.rollback() #Rollback the changes on error
        finally:
            s.close() #Close the connection
        return                
    
    
    @staticmethod
    def update_sql_trade_date():
        print(u"开始更新交易日数据库")
        Trade_Date.update_trade_date()
        new_df = Trade_Date.get_trade_date_df()
        new_df.index.name="trade_date"
        new_df = new_df.reset_index().dropna(axis=1)
        if new_df is not None:
            session = sessionmaker()
            session.configure(bind=sql_trade_date.engine)
            s = session()
            try:
                sql_trade_date.SQL_Trade_Date.__table__.drop(sql_trade_date.engine)
                sql_trade_date.SQL_Trade_Date.__table__.create(sql_trade_date.engine)
                for i in range(len(new_df)):
                    tmp_ts = new_df.iloc[i, :].copy()
                    tmp_dict = Trade_Date.type_translate(tmp_ts)
                    record = sql_trade_date.SQL_Trade_Date(**tmp_dict)
                    s.add(record) #Add all the records    
                s.commit() #Attempt to commit all the records
            except Exception as e:
                print(repr(e))
                s.rollback() #Rollback the changes on error
            finally:
                s.close() #Close the connection
            print(u"交易日数据库更新完毕")
            return
    
if __name__ == "__main__":
#    tdate = Trade_Date.get_newest_date()
    Trade_Date.update_trade_date()
    
    
    
    
    
    
    
    
    
    