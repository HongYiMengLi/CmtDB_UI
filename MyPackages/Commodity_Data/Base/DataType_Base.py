# -*- coding: utf-8 -*-
"""
Created on Wed Aug 22 10:24:52 2018

@author: Administrator
"""

import pandas as pd
from datetime import datetime, timedelta
from ...Data_API.Wind.WindAPI import wind
from .SQL_CommonData_Base import SQL_CommonData
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_





class DataType_Base(object):
    def get_ts(self):
        session = sessionmaker()
        session.configure(bind=self.engine)
        s = session()
        col = self.col_name
        try:
            tmp_field = self.field_name
            class_variable = SQL_CommonData            
            tmp_query = s.query(class_variable.date, class_variable.value).filter(and_(class_variable.col==col, 
                               class_variable.field==tmp_field))
            tmp_series = pd.read_sql(tmp_query.statement, self.engine, index_col="date").iloc[:, 0]
            tmp_series.name = col
        except Exception as e:
            print(repr(e))
            s.rollback()
            raise e
        finally:
            s.close()
        return tmp_series


class Manual(DataType_Base):
    datatype = "manual"
    def update_table_generate(self, ts):
        df = pd.DataFrame([ts]).T
        tmp_df = df.stack()
        if isinstance(tmp_df.index[0][0], datetime):
            date_index_list = [x[0] for x in tmp_df.index]
        else:
            date_index_list = [x[0].to_pydatetime() for x in tmp_df.index]
        field_list = [x[1] for x in tmp_df.index]
        output_df = pd.DataFrame([date_index_list, field_list, tmp_df.tolist()], index=["date","col","value"]).T
        output_df["col"] = self.col_name
        output_df["table"] = self.table_chinese_name
        output_df["field"] = self.field_name
        return output_df
        
    
class WindData(DataType_Base):
    datatype = "wind"
    def update_table_generate(self, ts):
        df = pd.DataFrame([ts]).T
        tmp_df = df.stack()
        if isinstance(tmp_df.index[0][0], datetime):
            date_index_list = [x[0] for x in tmp_df.index]
        else:
            date_index_list = [x[0].to_pydatetime() for x in tmp_df.index]
        field_list = [x[1] for x in tmp_df.index]
        output_df = pd.DataFrame([date_index_list, field_list, tmp_df.tolist()], index=["date","col","value"]).T
        output_df["col"] = self.col_name
        output_df["table"] = self.table_chinese_name
        output_df["field"] = self.field_name
        return output_df
    
    def download_wind_quote(self, start_date=None, end_date=None):
        wind.start_wind()
        if end_date is None:
            end_date = datetime.today()
        elif type(end_date) == str:
            end_date = datetime.strptime(end_date,"%Y-%m-%d")
        if start_date is not None:
            if type(start_date) == str:
                start_date = datetime.strptime(start_date,"%Y-%m-%d")
        if start_date is None:            
            session = sessionmaker()
            session.configure(bind=self.engine)
            s = session()
            try:                
                tmp_series = self.get_ts()
                s.commit()
            except Exception as e:
                print(repr(e))
                s.rollback()
                raise e
            finally:
                s.close()
            if len(tmp_series) == 0:
                print(self.col_name + u"无数据历史数据，将从2000年开始更新")
                tmp_start_date = datetime(2000, 1, 1)
            else:
                tmp_series.name = self.col_name  
                tmp_last_date = tmp_series.index[-1].to_pydatetime()
                tmp_start_date = tmp_last_date + timedelta(days=1)
        else:
            tmp_start_date = start_date
        if tmp_start_date > end_date:
            print(self.col_name + u"更新时间错误，无需更新")
            return None                   
        tmp_update_df = wind.wsd(self.wind_code, ["close"], tmp_start_date, end_date)
        tmp_update_df.index = [pd.Timestamp(x) for x in tmp_update_df.index]
        tmp_update_df = tmp_update_df[tmp_update_df.index>=tmp_start_date]                           
        if len(tmp_update_df) == 0:
            print(self.col_name + u"无可更新内容")
            return None 
        if self.col_name == u"坑口煤价格:东胜":
            if start_date is None:
                tmp_last = pd.DataFrame(tmp_series.iloc[-1:].copy())
                tmp_last.columns = tmp_update_df.columns
                tmp_update_df = pd.concat([tmp_last, tmp_update_df]).drop_duplicates()
            tmp_update_df = tmp_update_df.resample("B").bfill()
        return tmp_update_df  

        
class Computed(DataType_Base):
    datatype = "computed"    
    def get_ts_whole_progress(self):
        raise Exception("Computed base class shall not have specific ts")
    
    def get_ts(self):
        tmp_df = self.get_ts_whole_progress()
        if tmp_df is None:
            return None
        tmp_ts = tmp_df[self.col_name].dropna()
        return tmp_ts

    
class Auto(DataType_Base):
    datatype = "auto"
    
    
    
    
    
    
    
if __name__ == "__main__":
    df = 1
    aaa = Manual()