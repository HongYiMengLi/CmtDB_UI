# -*- coding: utf-8 -*-

"""
Created on Mon Jun 25 14:16:12 2018

@author: Administrator
"""

import pandas as pd
import numpy as np
from datetime import datetime, date
from .CmtData import Cmt_Data
from ...Data_API.Wind.WindAPI import wind
from ...Data_API.Wind.WindError import EmptyError
from ...Data_Path.data_path import Data_Path
from ...SQL.Table_Create import sql_cnt_profile
from sqlalchemy.orm import sessionmaker


def cnt2cmt(cnt_code):
    count = 0
    for x in cnt_code:
        if x.isdigit():
            break
        count += 1
    return cnt_code[:count]

class Cnt_Data(Cmt_Data):
    relative_local_path = Data_Path.relative_local_db_path() + "cnt_list/"
    default_mode = "db" # "db": 从数据库提取; "local": 从本地提取

    def __init__(self, contract_name, cmt_profile, cnt_profile, update_flag=False, mode=default_mode):
        self.cnt_profile = cnt_profile
        tmp_cnt, tmp_cmt = self.check_cnt_name(contract_name, update_flag)
        super(Cnt_Data, self).__init__(tmp_cmt, cmt_profile)
        self._cnt_code = tmp_cnt

        
    def check_cnt_name(self, contract_name, update_flag):        
        if type(contract_name) == str:
            contract_name = str(contract_name).upper()
            if contract_name in self.cnt_profile.index:
                return contract_name, self.cnt_profile.loc[contract_name, "cmt"]
            elif contract_name in self.cnt_profile["cnt_without_exch"].tolist():
                tmp_cnt = self.cnt_profile.index[self.cnt_profile["cnt_without_exch"]==contract_name.upper()][0]
                tmp_cmt = self.cnt_profile[self.cnt_profile["cnt_without_exch"]==contract_name.upper()]["cmt"][0]
                return tmp_cnt, tmp_cmt
            elif update_flag == True:
                return contract_name, cnt2cmt(contract_name)
        raise Exception("No such contract: " + str(contract_name))

            
    @property
    def cnt_code(self):
        return self._cnt_code
    
    @property
    def cnt_name(self):
        return self.cnt_code[:-4]
    
    @property
    def cnt_year(self):
        tmp_name = self.cnt_name
        tmp_digit = "".join([x for x in tmp_name if x.isdigit()])
        if len(tmp_digit) == 3:
            if (int(tmp_digit[0]) >= 6) and (int(tmp_digit[0]) <= 9):
                return "201" + tmp_digit[0]
            else:
                return "202" + tmp_digit[0]
        elif len(tmp_digit) == 4:
            if int(tmp_digit[:2]) > 89:
                return "19" + tmp_digit[:2]
            else:
                return "20" + tmp_digit[:2]
        else:
            raise Exception("Year Error:" + self.cnt_code)
    
    @property
    def cnt_month(self):
        tmp_name = self.cnt_name
        tmp_digit = "".join([x for x in tmp_name if x.isdigit()])
        return tmp_digit[-2:]
    
    #method
    def __cmp__(self,s):
        self.date = date(int(self.cnt_year), int(self.cnt_month), 1)
        s.date = date(int(s.cnt_year), int(s.cnt_month), 1)
        if self.date > s.date:
            return 1
        elif self.date < s.date:
            return -1
        else:
            return 0

    def __lt__(self, s):
        self.date = date(int(self.cnt_year), int(self.cnt_month), 1)
        s.date = date(int(s.cnt_year), int(s.cnt_month), 1)
        return self.date < s.date

    def __gt__(self, s):
        self.date = date(int(self.cnt_year), int(self.cnt_month), 1)
        s.date = date(int(s.cnt_year), int(s.cnt_month), 1)
        return self.date > s.date

    def __eq__(self, s):
        self.date = date(int(self.cnt_year), int(self.cnt_month), 1)
        s.date = date(int(s.cnt_year), int(s.cnt_month),1)
        return self.date == s.date

    def __le__(self, s):
        self.date = date(int(self.cnt_year), int(self.cnt_month), 1)
        s.date = date(int(s.cnt_year), int(s.cnt_month),1)
        return self.date <= s.date

    def __ge__(self, s):
        self.date = date(int(self.cnt_year), int(self.cnt_month), 1)
        s.date = date(int(s.cnt_year), int(s.cnt_month), 1)
        return self.date >= s.date

    def __ne__(self, s):
        self.date = date(int(self.cnt_year), int(self.cnt_month), 1)
        s.date = date(int(s.cnt_year), int(s.cnt_month), 1)
        return self.date != s.date
    
    @staticmethod
    def sort_cnt_list(tmp_cnt_list, cmt_profile, cnt_profile, update_flag=False, ascending=True):
        tmp_cnt_list = [Cnt_Data(x, cmt_profile, cnt_profile, update_flag) for x in tmp_cnt_list]
        tmp_cnt_list.sort(reverse=not ascending)
        tmp_cnt_list = [x.cnt_code for x in tmp_cnt_list]
        return tmp_cnt_list








    
########################################################################################################################
# 提取cnt数据    
    
    # 提取所有历史cnt profile
    @staticmethod
    def get_cnt_profile(mode=default_mode):
        if mode == "local":
            tmp_file_name = Cnt_Data.relative_local_path + "all_cnt.csv" 
            tmp_df = pd.read_csv(tmp_file_name, index_col=0, parse_dates=["contract_issue_date","last_trade_date"])
        elif mode == "db":
            session = sessionmaker()
            session.configure(bind=sql_cnt_profile.engine)
            s = session()
            try:
                tmp_query = s.query(sql_cnt_profile.SQL_Cnt_Data)
                tmp_df = pd.read_sql(tmp_query.statement, sql_cnt_profile.engine, index_col="contract")
            except Exception as e:
                print(repr(e))
                s.rollback()
                raise e
            finally:
                s.close()
        return tmp_df

    @staticmethod
    def get_profile(mode=default_mode):
        cnt_profile = Cnt_Data.get_cnt_profile(mode=mode)
        cmt_profile = Cmt_Data.get_cmt_profile(mode=mode)
        return cmt_profile, cnt_profile
    
    @staticmethod
    def get_cnt_profile_given_cmt(cmt, mode=default_mode):
        tmp_cnt_df = Cnt_Data.get_cnt_profile(mode=mode)
        tmp_cnt_given_cmt = tmp_cnt_df[tmp_cnt_df["cmt"]==cmt]
        return tmp_cnt_given_cmt    

    @staticmethod
    def get_cnt_first_trade_date(cnt, mode=default_mode):
        tmp_cnt_df = Cnt_Data.get_cnt_profile(mode=mode)
        tmp_cnt_given_cmt = tmp_cnt_df.loc[cnt, "contract_issue_date"]
        return tmp_cnt_given_cmt   
    
    @staticmethod
    def get_cnt_last_trade_date(cnt, mode=default_mode):
        tmp_cnt_df = Cnt_Data.get_cnt_profile(mode=mode)
        tmp_cnt_given_cmt = tmp_cnt_df.loc[cnt, "last_trade_date"]
        return tmp_cnt_given_cmt   

    @staticmethod
    def get_cnt_date_diff(cnt1, cnt2, mode=default_mode):
        tmp_cnt_df = Cnt_Data.get_cnt_profile(mode=mode)
        tmp_cnt1 = tmp_cnt_df.loc[cnt1, "last_trade_date"]
        tmp_cnt2 = tmp_cnt_df.loc[cnt2, "last_trade_date"]
        delta_t = (tmp_cnt2 - tmp_cnt1).days
        return delta_t  
    
    # generate effective cnt for given time interval and cmt
    @staticmethod
    def generate_effective_cnt_df(cmt, start_date=None, end_date=None, mode=default_mode):
        tmp_cnt_total_df = Cnt_Data.get_cnt_profile_given_cmt(cmt, mode=mode)
        if start_date is None and end_date is None:
            tmp_cnt_df = tmp_cnt_total_df
        else:
            if end_date is not None:
                if type(end_date) == str:
                    end_date = datetime.strptime(end_date,"%Y-%m-%d")
                elif type(end_date) == datetime.date:
                    end_date = datetime(end_date.year, end_date.month, end_date.day)
            if start_date is not None:
                if type(start_date) == str:
                    start_date = datetime.strptime(start_date,"%Y-%m-%d")
                elif type(start_date) == datetime.date:
                    start_date = datetime(start_date.year, start_date.month, start_date.day)
            tmp_cnt_df = tmp_cnt_total_df[(tmp_cnt_total_df["contract_issue_date"] <= end_date) & 
                                          (tmp_cnt_total_df["last_trade_date"] >= start_date)]
        return tmp_cnt_df  

    @staticmethod
    def generate_effective_cnt_list(cmt, start_date=None, end_date=None, mode=default_mode):
        df = Cnt_Data.generate_effective_cnt_df(cmt, start_date, end_date, mode)
        return df.index.tolist()  

    # get effective cnt at the time
    @staticmethod
    def get_effective_cnt_list(cmt, mode=default_mode):
        cnt_df = Cnt_Data.get_cnt_profile_given_cmt(cmt, mode=mode)
        effective_cnt_list = cnt_df[cnt_df["active"] == 1].index.tolist()
        return effective_cnt_list      
    
    @staticmethod
    def get_effective_cnt_df(cmt, mode=default_mode):
        cnt_df = Cnt_Data.get_cnt_profile_given_cmt(cmt, mode=mode)
        effective_cnt_list = cnt_df[cnt_df["active"] == 1].copy()
        return effective_cnt_list 









########################################################################################################################
# 修改或编辑cnt数据    
    
    @staticmethod
    def update_local_cnt_list_cmt(cmt, end_date, start_date="1999-01-01"):
        wind.start_wind()
        cnt_df = wind.w_cmt_profile(cmt,start_date,end_date,fields="wind_code,contract_issue_date,last_trade_date")
        cnt_df.set_index("wind_code" ,drop=True, inplace=True)
        cnt_df["cmt"] = [cmt] * len(cnt_df)
        cnt_df["cnt_without_exch"] = [x[:-4] for x in cnt_df.index]
        cnt_df["contract_issue_date"] = [x.strftime("%Y-%m-%d") for x in cnt_df["contract_issue_date"].tolist()]
        cnt_df["last_trade_date"] = [x.strftime("%Y-%m-%d") for x in cnt_df["last_trade_date"].tolist()] 
        return cnt_df


    @staticmethod
    def daily_update_local_cnt_list(update_end_date):
        cmt_list = Cmt_Data.get_cmt_list()
        cnt_df_list = []
        print("开始更新合约列表")
        cmt_profile, cnt_profile = Cnt_Data.get_profile()
        for cmt in cmt_list:
            tmp_cnt_df = Cnt_Data.get_cnt_profile_given_cmt(cmt, mode="local")
            try:
                tmp_update_df = Cnt_Data.update_local_cnt_list_cmt(cmt,update_end_date,update_end_date)
            except EmptyError:
                print(cmt + u"本日无有效合约")
                tmp_cnt_df["active"] = 0
                tmp_cnt_df.to_csv(Cnt_Data.relative_local_path + cmt[:-4] + ".csv")
                cnt_df_list.append(tmp_cnt_df)
                continue
            else:
                updated_cnt_list = [cnt for cnt in tmp_update_df.index.tolist() if cnt not in tmp_cnt_df.index.tolist()]
                tmp_cnt_df = pd.concat([tmp_cnt_df,tmp_update_df.loc[updated_cnt_list,:]], sort=False)
                tmp_cnt_obj_list = Cnt_Data.sort_cnt_list(tmp_cnt_df.index.tolist(), cmt_profile, cnt_profile, update_flag=True)
                tmp_cnt_df = tmp_cnt_df.loc[tmp_cnt_obj_list,:]
                tmp_cnt_df["active"] = 0
                tmp_cnt_df.loc[tmp_update_df.index.tolist(),"active"] = 1
                tmp_cnt_df.to_csv(Cnt_Data.relative_local_path + cmt[:-4] + ".csv")
                cnt_df_list.append(tmp_cnt_df)
#            print cmt + u"合约更新完毕"
        all_cnt_df = pd.concat(cnt_df_list)
        all_cnt_df.to_csv(Cnt_Data.relative_local_path + "all_cnt.csv")
        print("合约信息更新完毕")
        print("")
        return all_cnt_df    
    
  
    @staticmethod
    def type_translate(ts):
        if "active" in ts.index:
            ts["active"] = int(ts["active"])   
        if "contract_issue_date" in ts.index:
            ts["contract_issue_date"] = ts["contract_issue_date"].to_pydatetime()
        if "last_trade_date" in ts.index:
            ts["last_trade_date"] = ts["last_trade_date"].to_pydatetime()
        return ts
    
    @staticmethod
    def update_sql_cnt_profile():
        print(u"开始更新全部合约列表数据库")
        all_cnt_df = Cnt_Data.get_cnt_profile(mode="local")
        all_cnt_df.index.names = ["contract"]
        all_cnt_df.reset_index(inplace=True)

        session = sessionmaker()
        session.configure(bind=sql_cnt_profile.engine)
        s = session()
        try:
            sql_cnt_profile.SQL_Cnt_Data.__table__.drop(sql_cnt_profile.engine)
            sql_cnt_profile.SQL_Cnt_Data.__table__.create(sql_cnt_profile.engine)
            for i in range(len(all_cnt_df)):
                tmp_ts = all_cnt_df.iloc[i,:].copy()
                tmp_ts = Cnt_Data.type_translate(tmp_ts)
                record = sql_cnt_profile.SQL_Cnt_Data(**dict(tmp_ts))
                s.add(record) #Add all the records    
            s.commit() #Attempt to commit all the records
        except Exception as e:
            print(repr(e))
            s.rollback() #Rollback the changes on error
        finally:
            s.close() #Close the connection
        print(u"全部合约列表数据库更新完毕")
        return
    
    
if __name__ == "__main__":
#    cmt_list = Cnt_Data.get_local()
#    cnt_df = Cnt_Data.daily_update_local_cnt_list("2018-7-16")
    aaa = Cnt_Data.get_cnt_date_diff("A1701.DCE", "A1705.DCE")
#    effective_cnt = Cnt_Data.get_effective_cnt_list("A.DCE")
#    Cnt_Data.sql_update_cnt_profile()
#    tmp_df = Cnt_Data.sql_get_cmt("PP.DCE")
        