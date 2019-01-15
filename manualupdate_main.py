# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 13:56:48 2019

@author: Administrator
"""

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
import pandas as pd
import numpy as np
from UI_ManualUpdateWindow import Ui_ManualUpdateWindow

import sys
sys.path.append("..\..")
from MyPackages.Commodity_Data.APP_Base.Update_Base import CMTDB_Update
from MyPackages.Commodity_Data.Global_Factory import Global_Factory
from MyPackages.Commodity_Data.IndexTable import CmtDB_Index
from datetime import datetime


class ManualUpdate_Main(QWidget, Ui_ManualUpdateWindow):
    def __init__(self, cmt_list, parent=None):
        super(ManualUpdate_Main,self).__init__()
        self.setupUi(self)
#        self.setWindowTitle("万得数据更新")
        self.cmt_list = cmt_list        
        self.show_list = cmt_list        
#        self.show_list.append("以上全部")
        
        tmp_font = QFont("Microsoft YaHei", 13)
        self.textwindow.setReadOnly(True)
        tmp_font.setBold(True)
        self.setFont(tmp_font)

        self.init_alltable()
        self.init_selectedtable()
        self.select_btn.clicked.connect(self.onSelectedBTNClicked)
        self.delete_btn.clicked.connect(self.onDeleteBTNClicked)
        self.start_btn.clicked.connect(self.onStartBTNClicked)
        
        
        self.thread = update_worker()
        self.thread.sinOut.connect(self.onReceiveStr)
        self.thread.completed_signal.connect(self.onCompleted)

    def init_alltable(self):
        self.allTable.setColumnCount(1)
        self.allTable.setRowCount(len(self.cmt_list))
        self.allTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.allTable.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.allTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.allTable.setShowGrid(False)
        self.allTable.verticalHeader().setVisible(False)
        self.allTable.horizontalHeader().setVisible(False)
        tmp_index = 0
        for cmt in self.cmt_list:
            self.allTable.setItem(tmp_index , 0,  QTableWidgetItem(cmt))
            tmp_index += 1
        self.allTable.cellDoubleClicked.connect(self.onAddcmt)

    def init_selectedtable(self):
        self.selectedTable.setColumnCount(1)
        self.selectedTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.selectedTable.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.selectedTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.selectedTable.setShowGrid(False)
        self.selectedTable.verticalHeader().setVisible(False)
        self.selectedTable.horizontalHeader().setVisible(False)
        self.selectedTable.setSelectionMode(QAbstractItemView.MultiSelection)
        self.selectedTable.cellDoubleClicked.connect(self.onDeletecmt)

    def onAddcmt(self, r, c):
        item = self.allTable.item(r, c).clone()
        items = self.selectedTable.findItems(item.text(), Qt.MatchExactly)
        if not items:
            rowPosition = self.selectedTable.rowCount()
            self.selectedTable.insertRow(rowPosition)
            self.selectedTable.setItem(rowPosition, 0, item)
        self.allTable.clearSelection()

    def onDeletecmt(self, r, c):
        self.selectedTable.removeRow(r)
        
    def onSelectedBTNClicked(self):
        selected_item_list = self.allTable.selectedItems()
        for item in selected_item_list:
            items = self.selectedTable.findItems(item.text(), Qt.MatchExactly)
            if not items:
                rowPosition = self.selectedTable.rowCount()
                self.selectedTable.insertRow(rowPosition)
                self.selectedTable.setItem(rowPosition, 0, item.clone())
        self.allTable.clearSelection()

    def onDeleteBTNClicked(self):
        indexes = self.selectedTable.selectionModel().selectedRows()
        for index in sorted(indexes, reverse=True):
            self.selectedTable.removeRow(index.row()) 
        self.selectedTable.clearSelection()
            
        
        
    def onReceiveStr(self, log):
        self.textwindow.append(log)
        
    def onCompleted(self):
        self.start_btn.setEnabled(True)
      
    def onStartBTNClicked(self):
        self.start_btn.setEnabled(False)
        selected_cmt_list = [self.selectedTable.item(x, 0).text() for x in range(self.selectedTable.rowCount())]
        if len(selected_cmt_list) == 0:
            QMessageBox.warning(self, "更新失败", "您未选择要更新的品种")
            self.start_btn.setEnabled(True)
        else:
            fname, ok = QFileDialog.getOpenFileName(self, "另存为", QDir.homePath(), "Excel Files (*.xlsx)")
            if ok:            
                self.thread.set_param(selected_cmt_list, fname)
                self.thread.start()
            else:
                self.start_btn.setEnabled(True)

        
class update_worker(QThread):
    sinOut = pyqtSignal(str)
    completed_signal = pyqtSignal()
    
    def __init__(self, parent=None):
        super(update_worker, self).__init__(parent)

    def __del__(self):
        self.wait()

    def set_param(self, selected_cmt_list, path):
        self.cmt_list = selected_cmt_list
        self.local_path = path
        
    def run(self):
        self.sinOut.emit("正在更新手动数据...")
        update_list = [ui_manual_update(self.sinOut, x, update_type="Manual") for x in self.cmt_list]
        df, log = ui_manual_update.standard_local_update(update_list, self.local_path)
        self.sinOut.emit(log)
        self.completed_signal.emit()
        
        
        
class ui_manual_update(CMTDB_Update):
    def __init__(self, sinOut, cmt_name, update_type, spec_col=None):
        super(ui_manual_update, self).__init__(cmt_name, update_type, spec_col)
        self.sinOut = sinOut
        
        
    def table_generate_from_file(self, table):
        transformed_series_list = []
        false_list = []
        for col in table.columns.tolist():
            if not self.cmt_cls.check_col_available(col):
                false_list.append(col)
                print("Warning：" + col + "不存在于" + self.cmt_name + "数据库中")
            else:
                print(col + u"开始转换")
                tmp_series = table[col].dropna()
                if len(tmp_series) == 0:
                    tmp_log = "%s：'%s'更新0条数据\n" % (self.cmt_name, col)
                    self.sinOut.emit(tmp_log)
                    continue
                tmp_col_obj = Global_Factory.getobj(col, self.cmt_name)
                if hasattr(tmp_col_obj, "update_table_generate"):
                    tmp_transformed_df = tmp_col_obj.update_table_generate(tmp_series)
                    tmp_log = "%s：'%s'更新%d条数据，更新起始日期%s，截止日期%s；" % (self.cmt_name, col, len(tmp_transformed_df), 
                                                                  tmp_transformed_df["date"].iloc[0].to_pydatetime().strftime("%Y-%m-%d"), 
                                                                  tmp_transformed_df["date"].iloc[-1].to_pydatetime().strftime("%Y-%m-%d"))  
                    self.sinOut.emit(tmp_log)                    
                    transformed_series_list.append(tmp_transformed_df)
        transformed_df = pd.concat(transformed_series_list)
        transformed_df.reset_index(inplace=True)
        transformed_df = transformed_df.drop(["index"], axis=1)
        transformed_df = CMTDB_Update.drop_non_float_value(transformed_df)
        transformed_df.reset_index(inplace=True)
        transformed_df = transformed_df.drop(["index"], axis=1)
        return transformed_df, tmp_log, false_list
    
    @staticmethod
    def standard_local_update(update_obj_list, srcfile):
        update_df = CMTDB_Update.local_table_load(srcfile)
        log = ""
        false_set_list = []
        cmt_name_list = [x.cmt_name for x in update_obj_list]
        for update_obj in update_obj_list:
            transformed_df, new_log, false_list = update_obj.table_generate_from_file(update_df)
            log += new_log
            false_set_list.append(set(false_list))
            if len(transformed_df) != 0:
                update_obj.upload_table(transformed_df)
                update_obj.backup_update_df(transformed_df)
                index_update_df = transformed_df.groupby("col").last().drop(["value", "field", "table"], axis=1).reset_index().rename(columns={"date": "last_date"})
                index_update_df["update_date"] = datetime.today()
                index_update_df["cmt"] = update_obj.cmt_name            
                CmtDB_Index.update_sql_cmtdb_condition(index_update_df)
                log = "%s本次更新手动数据已入库！" % (update_obj.cmt_name)
                update_obj.sinOut.emit(log)
        total_false_col_list = list(set.intersection(*false_set_list))
        if len(total_false_col_list) != 0: 
            log += ",".join(total_false_col_list) + "不存在于" + ",".join(cmt_name_list) + "数据库中, 未更新这些指标！"
        else:
            log += "本次" + ",".join(cmt_name_list) + "数据库手动更新完成！"    
        log += "\n"
        print(log)    
        return update_df, log        
        
    