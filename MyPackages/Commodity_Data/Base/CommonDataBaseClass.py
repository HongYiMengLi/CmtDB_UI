# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 14:48:22 2018

@author: 李弘一萌
"""

import pandas as pd
from ..IndexTable import CmtDB_Index


class CommonDataBaseClass(object):

    
    
    @classmethod
    def get_col_class_table(cls, col):
        cls, tbl = CmtDB_Index().get_col_class_table_name(col, cls.cmt_name) 
        return cls, tbl    
          
    @classmethod
    def get_col_index_df(cls):
        total_col_df = pd.read_excel(cls.relative_data_path + "files/col_index.xlsx", index_col=0, encoding="gbk") 
        return total_col_df


    @classmethod
    def get_table_index_df(cls):
        total_col_df = pd.read_excel(cls.relative_data_path + "files/table_index.xlsx", index_col=0, encoding="gbk") 
        return total_col_df    

    
    @classmethod
    def check_col_available(cls, col):
        total_col_df = cls.get_col_index_df()
        if col in total_col_df.index.tolist():
            return True
        else:
            return False


    @classmethod
    def get_tables_list(cls):
        total_col_df = cls.get_table_index_df()
        return total_col_df["table_name"].tolist()


    @classmethod
    def get_class_name(cls, col):
        total_col_df = cls.get_col_index_df()
        return total_col_df.loc[col, u"类名"]


    @classmethod
    def get_table_name(cls, col):
        total_col_df = cls.get_col_index_df()
        table_chinese_name = total_col_df.loc[col, u"数据大类"]
        table_df = cls.get_table_index_df()
        table_name = table_df.loc[table_chinese_name, "table_name"]
        return table_name


    @classmethod
    def get_table_class_full_variable(cls, col):
        class_name = cls.get_class_name(col)
        table_name = cls.get_table_name(col)
        return table_name + "." + class_name

    
    @classmethod
    def get_table_class(cls):
        sub_list = cls.__subclasses__()
        return sub_list


    @classmethod
    def get_all_table_classname(cls):
        sub_list = cls.get_table_class()
        sub_name_list = [sub_cls.__name__ for sub_cls in sub_list]
        return sub_name_list
    
    
    @classmethod
    def get_table_base_classname(cls, table):
        sub_list = cls.get_table_class()
        sub_name_list = cls.get_all_table_classname()
        table_name_list = [sub_cls.table_name for sub_cls in sub_list]
        if table not in table_name_list:
            raise Exception(u"Invalid table name:" + table)
        table_dict = dict(zip(table_name_list, sub_name_list))
        return table_dict[table]


    @classmethod
    def get_all_sub_class(cls, all_subclasses={}):
        for subclass in cls.__subclasses__():
            if (subclass.__name__ not in all_subclasses.keys()) and (subclass.cmt_name == cls.cmt_name):
                all_subclasses[subclass.__name__] = subclass
            all_subclasses.update(subclass.get_all_sub_class(all_subclasses))
        return all_subclasses


    @classmethod
    def get_all_windcol_class(cls):
        filtered_all_col_dict = {}
        all_col_dict = cls.get_all_sub_class()
        for key, value in all_col_dict.items():
            if value().cmt_name == cls.cmt_name:
                filtered_all_col_dict[key] = value
        all_wind_col_name_list = [x for x in filtered_all_col_dict.keys() if hasattr(filtered_all_col_dict[x], 'wind_code')]
        all_wind_col_class_list = [filtered_all_col_dict[x] for x in all_wind_col_name_list]
        windcol_dict = dict(zip(all_wind_col_name_list, all_wind_col_class_list))
        return windcol_dict


    @classmethod
    def get_all_manual_class(cls):
        all_col_dict = cls.get_all_sub_class()
        all_manual_col_name_list = [x for x in all_col_dict.keys() if all_col_dict[x]().datatype == u"manual"]
        all_manual_col_class_list = [all_col_dict[x] for x in all_manual_col_name_list]
        manualcol_dict = dict(zip(all_manual_col_name_list, all_manual_col_class_list))
        return manualcol_dict

    @classmethod
    def get_all_col_class(cls):
        all_col_dict = cls.get_all_sub_class()
        all_col_name_list = [x for x in all_col_dict.keys() if hasattr(all_col_dict[x], 'col_name')]
        all_col_class_list = [all_col_dict[x] for x in all_col_name_list]
        col_dict = dict(zip(all_col_name_list, all_col_class_list))
        return col_dict
    
    # 不应该写在这里，应该写在业务模块中
    @classmethod
    def get_original_df(cls, input_filename=None):
        if input_filename is None:
            original_filename = cls.original_db_filepath
        else:
            original_filename = input_filename
        xl = pd.ExcelFile(original_filename)    
        sheet_list = xl.sheet_names
        df_list = []
        for sheet in sheet_list:
            tmp_df = pd.read_excel(original_filename, sheetname=sheet, index_col=0, encoding="gbk")
            df_list.append(tmp_df)
        tmp_total_df = pd.concat(df_list, axis=1)
        return tmp_total_df

    
if __name__ == "__main__":
#    aa = LPP_Base.get_table_base_classname("a") 
    pass