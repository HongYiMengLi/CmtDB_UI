# -*- coding: utf-8 -*-
"""
Created on Thu Aug 16 16:47:10 2018

@author: Administrator
"""

import os

class CmtDB_Data_Path(object):
    @staticmethod
    def relative_local_db_path():
        current_path = os.getcwd()
        tmp_index = current_path.find("Work")
        if tmp_index == -1:
#            raise Exception("Wrong Path: Work not founded")
            return ""
        else:
            relative_db_path = current_path[:(tmp_index+4)] + "/CommodityDataBase/Commodities/"
            return relative_db_path
        
        


if __name__ == "__main__":
    my_path = CmtDB_Data_Path.relative_local_db_path()
    print(my_path)