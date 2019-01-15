# -*- coding: utf-8 -*-
"""
Created on Wed Aug 22 10:34:12 2018

@author: Administrator
"""

"""
Created on Tue Jul 10 13:39:53 2018

@author: Administrator
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime, Float


Base = declarative_base()
col_dict = {
        "table": String(200),
        "field": String(200),
        "col": String(200),
        "date": DateTime,
        "value": Float
        }


class SQL_CommonData(Base):
    __tablename__ = "common_data"
    
    col = Column(col_dict["col"], primary_key=True)
    table = Column(col_dict["table"], primary_key=True)
    field = Column(col_dict["field"], primary_key=True)
    date = Column(col_dict["date"], primary_key=True)
    value = Column(col_dict["value"], nullable=False)




    
#Base.metadata.create_all(engine)