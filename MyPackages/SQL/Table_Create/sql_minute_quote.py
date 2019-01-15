# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 18:27:28 2018

@author: 李弘一萌
"""




from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer, String, DateTime, Float
from ..SQL_Connection import SQL_Connection
from ..database_dict import db_name
from sqlalchemy.orm import sessionmaker
from datetime import datetime
import pandas as pd
from sqlalchemy import and_
from sqlalchemy import MetaData, Table


table_name = "quote_minute"
class_name = "QuoteData"
database_name = db_name[class_name]

engine = SQL_Connection.get_connection(database_name, charset="utf8")
Base = declarative_base()
col_dict = {
        "time": DateTime,
        "contract": String(50),
        "open_interest": Integer,
        "close": Float,
        "high": Float,
        "low": Float,
        "volume": Integer,
        "open": Float
        }


class SQL_Minute_Quote_Data(Base):
    __tablename__ = table_name    
    contract = Column(col_dict["contract"], primary_key=True)
    time = Column(col_dict["time"], primary_key=True)
    open_interest = Column(col_dict["open_interest"], nullable=True)
    close = Column(col_dict["close"], nullable=True)
    open = Column(col_dict["open"], nullable=True)
    high = Column(col_dict["high"], nullable=True)
    low = Column(col_dict["low"], nullable=True)
    volume = Column(col_dict["volume"], nullable=True)

def add_start_time(dt):
    dt = dt.replace(hour=20, minute=58, second=0)
    return dt

def add_end_time(dt):
    dt = dt.replace(hour=15, minute=15, second=0)
    return dt

if __name__ == "__main__":
    
#    date_table = Trade_Date.get_trade_date_df()
#    date_list = [x.to_pydatetime() for x in date_table.index[date_table.index >= datetime(2018, 6, 8)].tolist()]
#    start_time_list = [add_start_time(x) for x in date_list[:-1]]
#    end_time_list = [add_end_time(x) for x in date_list[1:]]
#    time_interval_list = zip(start_time_list, end_time_list)
#    original_engine = SQL_Connection.get_connection(database_name, charset="utf8")
    upload_engine = SQL_Connection.get_connection("minute_quote", charset="utf8")  
#    for time_interval in time_interval_list:
#        start_time = time_interval[0]
#        end_time = time_interval[1]
#        table_name = end_time.strftime("%Y-%m-%d")
#        if upload_engine.dialect.has_table(upload_engine, table_name):
#            print table_name + "already exist"
#            continue
#        else:
#            print table_name
#            session = sessionmaker()
#            session.configure(bind=original_engine)
#            s = session()
#            try:
#                tmp_query = s.query(SQL_Minute_Quote_Data).filter(and_(SQL_Minute_Quote_Data.time >= start_time, 
#                                   SQL_Minute_Quote_Data.time <= end_time))
#                tmp_df = pd.read_sql(tmp_query.statement, original_engine)
#                print table_name + "分钟数据提取完毕"
#            except Exception, e:
#                print repr(e)
#                s.rollback()
#                raise e
#            finally:
#                s.close()
#            
#                  
#            metadata = MetaData()        
#            table_object = Table(table_name, metadata,
#                Column("time", col_dict["time"], primary_key=True),                 
#                Column("contract", col_dict["contract"], primary_key=True),        
#                Column("open_interest", col_dict["open_interest"], nullable=True),
#                Column("open", col_dict["open"], nullable=True),
#                Column("high", col_dict["high"], nullable=True),
#                Column("low", col_dict["low"], nullable=True),
#                Column("close", col_dict["close"], nullable=True),
#                Column("volume", col_dict["volume"], nullable=True)
#            )
#            
#            table_object.create(upload_engine)
#            session = sessionmaker()
#            session.configure(bind=upload_engine)
#            s = session()
#            tmp_dict = [x.to_dict() for _, x in tmp_df.iterrows()]
#            try:
#                s.execute(table_object.insert(), tmp_dict) 
#                s.commit() #Attempt to commit all the records
#                print table_name + "分钟数据上传完毕"
#            except Exception, e:
#                print repr(e)
#                s.rollback() #Rollback the changes on error
#                raise e
#            finally:
#                s.close() #Close the connection
    
    table_name = "2018-08-10"
    metadata = MetaData()        
    table_object = Table(table_name, metadata,
        Column("time", col_dict["time"], primary_key=True),                 
        Column("contract", col_dict["contract"], primary_key=True),        
        Column("open_interest", col_dict["open_interest"], nullable=True),
        Column("open", col_dict["open"], nullable=True),
        Column("high", col_dict["high"], nullable=True),
        Column("low", col_dict["low"], nullable=True),
        Column("close", col_dict["close"], nullable=True),
        Column("volume", col_dict["volume"], nullable=True)
    )
    session = sessionmaker()
    session.configure(bind=upload_engine)
    s = session()
    try:
        tmp_query = s.query(table_object)
        tmp_df = pd.read_sql(tmp_query.statement, upload_engine)
#        print table_name + "分钟数据提取完毕"
    except Exception, e:
        print repr(e)
        s.rollback()
        raise e
    finally:
        s.close()

































