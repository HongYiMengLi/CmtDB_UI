# -*- coding: utf-8 -*-
"""
Created on Tue Sep 04 08:39:11 2018

@author: 李弘一萌
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime, Float, Integer


Base = declarative_base()

# 装置总表
col_dict = {
        "date": DateTime,
        "company": String(200),
        "device_name": String(200),
        "field": String(200),
        "pipeline": String(200),
        "product": String(200),
        "product_specifict_class": String(200),
        "product_field": String(200),
        "product_yield": Float,
        "capability": Float
        }


class SQL_Device(Base):
    __tablename__ = "device"
    
    company = Column(col_dict["company"], primary_key=True)
    device_name = Column(col_dict["device_name"], primary_key=True)
    pipeline = Column(col_dict["pipeline"], primary_key=True)
    date = Column(col_dict["date"], primary_key=True)
    field = Column(col_dict["field"], nullable=False)
    product = Column(col_dict["product"], nullable=False)
    product_specifict_class = Column(col_dict["product_specifict_class"], nullable=False)
    product_field = Column(col_dict["product_field"], nullable=False)
    product_yield = Column(col_dict["product_yield"], nullable=False)
    capability = Column(col_dict["capability"], nullable=False)


# 装置profile表
device_profile_col_dict = {
                            "company": String(200),
                            "field": String(200),
                            "area": String(200),
                            "capability": Float,
                            "pipe_line": String(200),
                            "classname": String(200),
                            "available_date": DateTime,
                            }

    
class SQL_Device_Profile(Base):
    __tablename__ = "device_profile"
        
    company = Column(device_profile_col_dict["company"], primary_key=True)
    field = Column(device_profile_col_dict["field"], primary_key=True)
    area = Column(device_profile_col_dict["area"], primary_key=True)
    capability = Column(device_profile_col_dict["capability"], nullable=False)
    pipe_line = Column(device_profile_col_dict["pipe_line"], nullable=False)
    classname = Column(device_profile_col_dict["classname"], nullable=False)
    available_date = Column(device_profile_col_dict["available_date"], nullable=False)
    
# 产品牌号表    
product_license_dict = {
                        "id": Integer,
                        "product": String(200),
                        "classname": String(200),
                        "typical_company": String(200),
                        "application": String(200),
                        "characteristic": String(200)
                        }

    
class SQL_Product_License(Base):
    __tablename__ = "product_license"
    
    id = Column(product_license_dict["id"], primary_key=True)
    product = Column(product_license_dict["product"], nullable=False)
    classname = Column(product_license_dict["classname"], nullable=False)
    typical_company = Column(product_license_dict["typical_company"], nullable=True)
    application = Column(product_license_dict["application"], nullable=True)
    characteristic = Column(product_license_dict["characteristic"], nullable=True)
 
# 产品类别对应大类表    
field_dict = {
                "product_class": String(200),
                "field": String(200),
                }

    
class SQL_Field_List(Base):
    __tablename__ = "field_list"
    
    product_class = Column(field_dict["product_class"], primary_key=True)
    field = Column(field_dict["field"], nullable=False)
    
    
    
    
    
    
    
