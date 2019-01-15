# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 16:01:10 2018

@author: 李弘一萌
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer, String, DateTime, Float
from ..SQL_Connection import SQL_Connection
from ..database_dict import db_name

table_name = "daily_quote"
class_name = "QuoteData"
database_name = db_name[class_name]

engine = SQL_Connection.get_connection(database_name, charset="utf8")
Base = declarative_base()
col_dict = {
        "date": DateTime,
        "contract": String(50),
        "cmt": String(50),
        "open_interest": Integer,
        "close": Float,
        "high": Float,
        "low": Float,
        "volume": Integer,
        "settle": Float,
        "open": Float
        }


class SQL_Daily_Quote_Data(Base):
    __tablename__ = table_name    
    contract = Column(col_dict["contract"], primary_key=True)
    date = Column(col_dict["date"], primary_key=True)
    cmt = Column(col_dict["cmt"], primary_key=True)
    open_interest = Column(col_dict["open_interest"], nullable=True)
    close = Column(col_dict["close"], nullable=True)
    open = Column(col_dict["open"], nullable=True)
    high = Column(col_dict["high"], nullable=True)
    low = Column(col_dict["low"], nullable=True)
    volume = Column(col_dict["volume"], nullable=True)
    settle = Column(col_dict["settle"], nullable=True)
        
#    def is_active(self):    #这个和下面几个方法都是意思意思，就是说表类中其实也可以定义一些方法，让数据对象的操作可以更优雅好看
#        return True
#    def is_anonymous(self):
#        return False
#    
#    def get_id(self):
#        return self.id
#    
#    def get_authorized(self):
#        return True
#    
#    def __repr__(self):
#        return "<type 'Account'>{}:{}".format(self.id,self.user_name)

Base.metadata.create_all(engine)