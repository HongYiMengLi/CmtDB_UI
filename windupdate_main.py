# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 14:51:47 2019

@author: 李弘一萌
"""

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
import numpy as np
from UI_WindUpdateWindow import Ui_WindUpdateWindow

import sys
sys.path.append("..\..")
import pandas as pd
from MyPackages.Commodity_Data.APP_Base.Update_Base import CMTDB_Update
from MyPackages.Commodity_Data.Global_Factory import Global_Factory
from MyPackages.Commodity_Data.IndexTable import CmtDB_Index
from datetime import datetime

class WindUpdate_Main(QWidget, Ui_WindUpdateWindow):
    def __init__(self, cmt_list, parent=None):
        super(WindUpdate_Main,self).__init__()
        self.setupUi(self)
        self.setWindowTitle("万得数据更新")
        self.cmt_list = cmt_list        
        show_list = cmt_list
        
        show_list.append("以上全部")
        tmp_font = QFont("Microsoft YaHei", 13)
        self.textwindow.setReadOnly(True)
        tmp_font.setBold(True)
        self.setFont(tmp_font)
        self.cb.addItems(show_list)
        self.thread = update_worker(show_list)
        self.btn.clicked.connect(self.onBTNClicked)
        self.thread.sinOut.connect(self.onReceiveStr)
        self.thread.completed_signal.connect(self.onCompleted)
        
    def onReceiveStr(self, log):
        self.textwindow.append(log)
        
    def onCompleted(self):
        self.btn.setEnabled(True)
        
    def onBTNClicked(self):
        self.btn.setEnabled(False)
        tmp_cmt_name = str(self.cb.currentText())
        self.thread.setcmt(tmp_cmt_name)
        self.thread.start()

        
class update_worker(QThread):
    sinOut = pyqtSignal(str)
    completed_signal = pyqtSignal()
    
    def __init__(self, cmt_list, parent=None):
        super(update_worker, self).__init__(parent)
        self.cmt_list = cmt_list
        
    
    def __del__(self):
        self.wait()

    def setcmt(self, cmt):
        self.cmt = cmt
        
    def run(self):
        if self.cmt != "以上全部":
            self.sinOut.emit("正在更新%s万得数据......" % self.cmt)
            ui_wind_update(self.sinOut, self.cmt, update_type="Wind").standard_wind_update()
            log = "%s本次万得数据更新完毕" % (self.cmt)
            self.sinOut.emit(log)            
        else:
            for cmt in self.cmt_list:
                self.sinOut.emit("正在更新%s万得数据......" % cmt)
                ui_wind_update(self.sinOut, cmt, update_type="Wind").standard_wind_update()
                log = "%s本次万得数据更新完毕" % (cmt)
                self.sinOut.emit(log)
    
        self.completed_signal.emit()
    
class ui_wind_update(CMTDB_Update):
    def __init__(self, sinOut, cmt_name, update_type, spec_col=None):
        super(ui_wind_update, self).__init__(cmt_name, update_type, spec_col)
        self.sinOut = sinOut
    
    # 重载wind update模块
    def wind_table_update(self, wind_df, dstfile=None, start_date=None):
        if dstfile is None:
            dstfile = self.default_dstfile
        update_df_list = []
        for index, row in wind_df.iterrows():
            tmp_col_obj = Global_Factory.getobj(row["data_name"], self.cmt_name)
            tmp_update_df = tmp_col_obj.download_wind_quote(start_date=start_date)
            if (tmp_update_df is None) or (len(tmp_update_df) == 0):
                log =  "%s：'%s'无新数据更新；" % (self.cmt_name, tmp_col_obj.col_name)
                self.sinOut.emit(log)
                continue        
            tmp_update_df.columns = ["value"]
            tmp_update_df["field"] = tmp_col_obj.field_name
            tmp_update_df["col"] = tmp_col_obj.col_name
            tmp_update_df["date"] = tmp_update_df.index.tolist()
            tmp_update_df["table"] = tmp_col_obj.table_chinese_name
            log = "%s：'%s'更新%d条数据，更新起始日期%s，截止日期%s" % (self.cmt_name, tmp_col_obj.col_name, len(tmp_update_df), 
                                                            tmp_update_df.index[0].to_pydatetime().strftime("%Y-%m-%d"), 
                                                            tmp_update_df.index[-1].to_pydatetime().strftime("%Y-%m-%d")) 
            self.sinOut.emit(log)
            update_df_list.append(tmp_update_df)
        if len(update_df_list) == 0:
            log = "%s本次无万得数据更新" % (self.cmt_name)
            self.sinOut.emit(log)
            return None
        transformed_df = pd.concat(update_df_list)
        transformed_df.reset_index(inplace=True)
        transformed_df = transformed_df.drop(["index"], axis=1)
        transformed_df = self.drop_non_float_value(transformed_df)
        transformed_df.reset_index(inplace=True)
        transformed_df = transformed_df.drop(["index"], axis=1)
        transformed_df.to_excel(dstfile + "/update_transformed.xlsx", encoding="gbk")

        return transformed_df
    
    def standard_wind_update(self, mode="merge", start_date=None):
        dstfile = self.backup_original_update()
        wind_df = CmtDB_Index().get_wind_index_df(self.cmt_name)
        df = self.wind_table_update(wind_df, dstfile, start_date)
        if df is not None:
            self.upload_table(df, mode)
            self.backup_update_df(df)
            # 更新index数据库
            index_update_df = df.groupby("col").last().drop(["value", "field", "table"], axis=1).reset_index().rename(columns={"date": "last_date"})
            index_update_df["update_date"] = datetime.today()
            index_update_df["cmt"] = self.cmt_name            
            CmtDB_Index.update_sql_cmtdb_condition(index_update_df)
            log = "%s本次更新万得数据已入库！" % (self.cmt_name)
            self.sinOut.emit(log)
        return df

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = WindUpdate_Main(["L", "PP"])
    main.show()
    #app.installEventFilter(main)
    sys.exit(app.exec_())