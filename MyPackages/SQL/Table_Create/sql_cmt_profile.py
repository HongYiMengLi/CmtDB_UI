# -*- coding: utf-8 -*-
"""
Created on Thu Jul 05 14:45:51 2018

@author: Administrator
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine,Column,Integer,String,DateTime,Float
from ..SQL_Connection import SQL_Connection
from ..database_dict import db_name

table_name = "cmt_profile"
class_name = "Cmt_Data"
database_name = db_name[class_name]

engine = SQL_Connection.get_connection(database_name, charset="utf8")
Base = declarative_base()
col_dict = {
        "cmt": String(50),
        "chinese_name": String(50),
        "multiplier": Integer,
        "margin": Float,
        "issue_date": DateTime,
        "main_months": String(50),
        "category": String(100),
        "exchange": String(50),
        "full_chinese_name": String(100),
        "price_unit": String(100),
        "price_limit": Float,
        "min_price_change": Float,
        "delivery_months": String(100),
        "trade_hours": String(200),
        "last_trade_date": String(100),
        "delivery_date": String(100),
        "active": Integer
        }


class SQL_Cmt_Data(Base):
    __tablename__ = table_name
    
    cmt = Column(col_dict["cmt"], primary_key=True)
    chinese_name = Column(col_dict["chinese_name"], nullable=False)
    multiplier = Column(col_dict["multiplier"], nullable=False)
    margin = Column(col_dict["margin"], nullable=False)
    issue_date = Column(col_dict["issue_date"], nullable=False)
    main_months = Column(col_dict["main_months"], nullable=False)
    category = Column(col_dict["category"], nullable=False)
    exchange = Column(col_dict["exchange"], nullable=False)
    full_chinese_name = Column(col_dict["full_chinese_name"], nullable=False)
    price_unit = Column(col_dict["price_unit"], nullable=False)
    price_limit = Column(col_dict["price_limit"], nullable=False)
    min_price_change = Column(col_dict["min_price_change"], nullable=False)
    delivery_months = Column(col_dict["delivery_months"], nullable=False)
    trade_hours = Column(col_dict["trade_hours"], nullable=False)
    last_trade_date = Column(col_dict["last_trade_date"], nullable=False)
    delivery_date = Column(col_dict["delivery_date"], nullable=False)
    active = Column(col_dict["active"], nullable=False)
    
        
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