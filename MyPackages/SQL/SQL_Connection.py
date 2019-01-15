# -*- coding: utf-8 -*-
"""
Created on Tue Jul 03 11:01:51 2018

@author: Administrator
"""

#import config_default
#configs = config_default.configs
from sqlalchemy import create_engine

configs = {
        "host":"192.168.4.127",
        "port":"3306",
        "user":"root",
        "password":"123456"
        }

def merge(defaults, override):
    r = {}
    for k, v in defaults.items():
        if k in override:
            if isinstance(v, dict):
                r[k] = merge(v, override[k])
            else:
                r[k] = override[k]
        else:
            r[k] = v
    return r

def test(i=None):
    if not i:
        return 1
    else:
        return 0
    

class SQL_Connection(object):
    @staticmethod
    def get_configs(home=None):
        if not home:
            my_configs = configs
            return my_configs
        else:
            try:
                import config_override
                my_configs = merge(configs, config_override.configs)
            except ImportError:
                print(u"无homeDB配置文件")
            else:
                return my_configs
    
    @staticmethod
    def get_connection(db, my_encoding="utf-8", charset=None, my_echo=False, home=None):
        my_configs = SQL_Connection.get_configs(home)
        connect_str = "mysql+pymysql://" + my_configs["user"] + ":" + my_configs["password"] + "@" + my_configs["host"] + \
                      ":" + my_configs["port"] + "/" + db
        if charset:
            connect_str += "?charset=" + charset            
        con = create_engine(connect_str, encoding=my_encoding, echo=my_echo)
        return con
            
        
        
if __name__ == "__main__":
    con = SQL_Connection.get_connection("lpp_test")
        
        
        
        
        
        
        
        
        
        
        
        
        
        






