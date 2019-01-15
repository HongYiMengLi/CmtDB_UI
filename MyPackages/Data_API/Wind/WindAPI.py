# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 10:26:36 2018

@author: Administrator
"""

from WindPy import w
from datetime import datetime
from .WindError import WindCheck
import pandas as pd



    
    
class wind(object):
    @staticmethod
    def start_wind():
        w.start()
    
    @staticmethod
    def wsd(code,field_list,start_date,end_date):
        field_str = ",".join(field_list)
        tmp_data = w.wsd(code,field_str,start_date,end_date,"")
        WindCheck(tmp_data)
        tmp_data = pd.DataFrame(tmp_data.Data,index=tmp_data.Fields,columns=tmp_data.Times).T
        return tmp_data
    
    @staticmethod
    def wss(code_list,field_list,tdate,priceAdj="U",cycle="D"):
        if type(tdate) == str:
            tdate = datetime.strptime(tdate,"%Y-%m-%d")
        tdate = tdate.strftime("%Y%m%d")
        field_str = ",".join(field_list)
        tmp_data = w.wss(code_list,field_str,"tradeDate="+tdate+";priceAdj="+priceAdj+";cycle="+cycle)
        WindCheck(tmp_data)
        tmp_data = pd.DataFrame(tmp_data.Data,index=tmp_data.Fields,columns=tmp_data.Codes).T
        return tmp_data    

    @staticmethod
    def wsi(code,field_list,start_time,end_time):
        field_str = ",".join(field_list)
        tmp_data = w.wsi(code,field_str,start_time,end_time,"")
        WindCheck(tmp_data)
        tmp_data = pd.DataFrame(tmp_data.Data,index=tmp_data.Fields,columns=tmp_data.Times).T
        return tmp_data 
    
    @staticmethod
    def w_cmt_oi_rank(varity,start_date,end_date,fields=None,order="long",ranks="all"):
        keywords = "startdate=" + str(start_date) + ";enddate=" + str(end_date) + ";varity=" + str(varity) + ";order_by=" + str(order)\
                    + ";ranks=" + str(ranks)
        if fields is not None:
            keywords += ";field=" + fields        
        tmp_data = w.wset("futureoir",keywords)
        WindCheck(tmp_data)
        tmp_data = pd.DataFrame(tmp_data.Data,index=tmp_data.Fields,columns=tmp_data.Codes).T
        return tmp_data      
    
    @staticmethod
    def w_cnt_oi_rank(cnt,start_date,end_date,fields=None,order="long",ranks="all"):
        keywords = "startdate=" + str(start_date) + ";enddate=" + str(end_date) + ";wind_code=" + str(cnt) + ";order_by=" + str(order)\
                    + ";ranks=" + str(ranks)
        if fields is not None:
            keywords += ";field=" + fields        
        tmp_data = w.wset("futureoir",keywords)
        WindCheck(tmp_data)
        tmp_data = pd.DataFrame(tmp_data.Data,index=tmp_data.Fields,columns=tmp_data.Codes).T
        return tmp_data        
    
    @staticmethod
    def w_cmt_vol_rank(varity,start_date,end_date,fields=None,ranks="all"):
        keywords = "startdate=" + str(start_date) + ";enddate=" + str(end_date) + ";varity=" + str(varity) + ";ranks=" + str(ranks)
        if fields is not None:
            keywords += ";field=" + fields        
        tmp_data = w.wset("futurevir",keywords)
        WindCheck(tmp_data)
        tmp_data = pd.DataFrame(tmp_data.Data,index=tmp_data.Fields,columns=tmp_data.Codes).T
        return tmp_data        

    @staticmethod
    def w_cnt_vol_rank(cnt,start_date,end_date,fields=None,ranks="all"):
        keywords = "startdate=" + str(start_date) + ";enddate=" + str(end_date) + ";wind_code=" + str(cnt) + ";ranks=" + str(ranks)
        if fields is not None:
            keywords += ";field=" + fields        
        tmp_data = w.wset("futurevir",keywords)
        WindCheck(tmp_data)
        tmp_data = pd.DataFrame(tmp_data.Data,index=tmp_data.Fields,columns=tmp_data.Codes).T
        return tmp_data  

    @staticmethod
    def w_cmt_profile(cmt,start_date,end_date,fields=None):
        keywords = "startdate=" + str(start_date) + ";enddate=" + str(end_date) + ";wind_code=" + str(cmt)
        if fields is not None:
            keywords += ";field=" + fields        
        tmp_data = w.wset("futurecc",keywords)
        WindCheck(tmp_data)
        tmp_data = pd.DataFrame(tmp_data.Data,index=tmp_data.Fields,columns=tmp_data.Codes).T
        return tmp_data  
    
    @staticmethod
    def trade_date_list(start_date,end_date):
        tmp_data = w.tdays(start_date, end_date, "")
        WindCheck(tmp_data)
        date_list = [x.date() for x in tmp_data.Data[0]]
        return date_list

    @staticmethod
    def commom_date_list(start_date,end_date):
        tmp_data = w.tdays(start_date, end_date, "Days=Alldays")
        WindCheck(tmp_data)
        date_list = [x.date() for x in tmp_data.Data[0]]
        return date_list
    
    @staticmethod
    def tdate_offset(offset, tdate, period="D", calendar="DCE"):
        tmp_data = w.tdaysoffset(offset, tdate, "Period=" + period +";TradingCalendar="+calendar)
        WindCheck(tmp_data)
        offseted_date = tmp_data.Data[0][0]
        return offseted_date  







    
if __name__ == "__main__":
    a = "RB1901.SHF,RB1810.SHF"
    s = datetime.strptime("2018-05-21","%Y-%m-%d")
    g = s.date()
    e = "2018-06-19"
    t1 = "2018-06-20 21:00:00"
    t2 = "2018-06-21 15:00:00"  
    f = "member_name,long_position,short_position"
    df = wind.wsi("A1809.DCE","close",t1,t2)
    df = wind.trade_date_list(s,e)


























