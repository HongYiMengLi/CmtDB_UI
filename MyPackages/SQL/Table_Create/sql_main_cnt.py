# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 19:36:23 2018

@author: 李弘一萌
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer, String, DateTime, Float
from ..SQL_Connection import SQL_Connection
from ..database_dict import db_name

table_name = "main_cnt"
class_name = "Main_Cnt"
database_name = db_name[class_name]

engine = SQL_Connection.get_connection(database_name, charset="utf8")
Base = declarative_base()
col_dict = {
        "date": DateTime,
        "cmt": String(50),
        "contract": String(50),
        "smoothed_price": Float,
        }


class SQL_Main_Cnt_Data(Base):
    __tablename__ = table_name    
    cmt = Column(col_dict["cmt"], primary_key=True)
    date = Column(col_dict["date"], primary_key=True)
    contract = Column(col_dict["contract"], nullable=False)
    smoothed_price = Column(col_dict["smoothed_price"], nullable=True)

        
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