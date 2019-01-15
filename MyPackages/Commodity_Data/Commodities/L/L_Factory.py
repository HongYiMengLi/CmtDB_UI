# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 10:40:48 2018

@author: 李弘一萌
"""

import pandas as pd
from .L_Base import L_Base
from . import L_SpotPrice, L_FuturesPrice, L_Macro, L_Upstream, L_Downstream
from . import L_Inventory, L_Spread, L_Others, L_SupplyDemandBalance
#from sqlalchemy.orm import sessionmaker
#from sqlalchemy import and_



class L_Factory(object):
    @staticmethod
    def getobj(col):
        class_name, table_module_name = L_Base.get_col_class_table(col)
        tmp_obj = eval(table_module_name + "." + class_name)()
        return tmp_obj

    @staticmethod
    def getBaseObj():
        return L_Base()    
#    @staticmethod
#    def get_quote_list_df(col_list):
#        session = sessionmaker()
#        session.configure(bind=SQL_Table.engine)
#        s = session()
#        ts_list = []
#        try:            
#            for col in col_list:
#                if not LPP_Base.check_col_available(col):
#                    raise Exception(u"Wrong Col Name:" + col)
#                tmp_obj = LPP_Factory.getLPP(col)
#                tmp_table = tmp_obj.table_name
#                tmp_field = tmp_obj.field_name
#                class_variable = eval("SQL_Table.SQL_LPP_" + tmp_table)            
#                tmp_query = s.query(class_variable.date, class_variable.value).filter(and_(class_variable.col==col, 
#                                   class_variable.field==tmp_field))
#                tmp_series = pd.read_sql(tmp_query.statement, SQL_Table.engine, index_col="date").iloc[:,0]
#                tmp_series.name = col
#                if len(tmp_series) != 0:
#                    ts_list.append(tmp_series)
#        except Exception, e:
#            print repr(e)
#            s.rollback()
#            raise e
#        finally:
#            s.close()
#        if len(ts_list) == 0:
#            return None
#        else:
#            tmp_df = pd.concat(ts_list, axis=1)
#            return tmp_df
        
if __name__ == "__main__":
    col_list = [u"LLD价格_华东进口"]
    col = u"LLDPE:CFR价格_远东"
    a = L_Factory().getL(col)
    bbb = a.get_ts()
#    df = LPP_Factory.get_quote_list_df(col_list)
#    df = df.apply(lambda x: x*10000)
#    bbb = LPP_price.PPLaSiHuaDong()
#    bbb.output()