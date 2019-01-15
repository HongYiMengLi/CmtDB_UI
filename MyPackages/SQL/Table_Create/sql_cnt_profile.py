# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 20:33:34 2018

@author: Administrator
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine,Column,Integer,String,DateTime,Float
from ..SQL_Connection import SQL_Connection
from ..database_dict import db_name

table_name = "cnt_profile"
class_name = "Cnt_Data"
database_name = db_name[class_name]

engine = SQL_Connection.get_connection(database_name, charset="utf8")
Base = declarative_base()
col_dict = {
        "cmt": String(100),
        "contract": String(100),
        "contract_issue_date": DateTime,
        "last_trade_date": DateTime,
        "cnt_without_exch": String(100),
        "active": Integer        
        }


class SQL_Cnt_Data(Base):
    __tablename__ = table_name
    
    contract = Column(col_dict["contract"], primary_key=True)
    cmt = Column(col_dict["cmt"], nullable=False)
    active = Column(col_dict["active"], nullable=False)
    cnt_without_exch = Column(col_dict["cnt_without_exch"], nullable=False)
    contract_issue_date = Column(col_dict["contract_issue_date"], nullable=False)
    last_trade_date = Column(col_dict["last_trade_date"], nullable=False)
    
        
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