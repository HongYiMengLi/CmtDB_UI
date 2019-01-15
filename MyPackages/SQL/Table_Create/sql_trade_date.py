# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 20:33:34 2018

@author: Administrator
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine,Column,Integer,String,DateTime,Float
from ..SQL_Connection import SQL_Connection
from ..database_dict import db_name

table_name = "trade_date"
class_name = "Trade_Date"
database_name = db_name[class_name]

engine = SQL_Connection.get_connection(database_name, charset="utf8")
Base = declarative_base()
col_dict = {
        "trade_date": DateTime,      
        }


class SQL_Trade_Date(Base):
    __tablename__ = table_name
    
    trade_date = Column(col_dict["trade_date"], primary_key=True)

    
        
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