# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 14:19:08 2019

@author: Administrator
"""

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
import numpy as np
from UI_IndexOutput import Ui_IndexOuptputWindow

import sys
sys.path.append("..\..")
from MyPackages.Commodity_Data.IndexTable import CmtDB_Index

class IndexOutput_Main(QWidget, Ui_IndexOuptputWindow):
    def __init__(self, cmt_list, parent=None):
        super(IndexOutput_Main,self).__init__()
        self.setupUi(self)
#        self.setWindowTitle("万得数据更新")
        self.cmt_list = cmt_list        
        show_list = cmt_list
        
        show_list.append("以上全部")
        tmp_font = QFont("Microsoft YaHei", 13)        
        tmp_font.setBold(True)
        self.setFont(tmp_font)
        
        self.cb.addItems(show_list)
        self.btn.clicked.connect(self.onBTNClicked)

        
        
    def onBTNClicked(self):
        cmt = str(self.cb.currentText())
        if cmt != "以上全部":
            fname, ok = QFileDialog.getSaveFileName(self, "另存为", QDir.homePath() + "/" + cmt + "索引.xlsx", "Excel Files (*.xlsx)")
            if ok:            
                ifsaved = CmtDB_Index().save_index_table_for_cmt(cmt, fname)
                if ifsaved:
                    QMessageBox.information(self, "导出", "%s索引导出成功" % cmt)
                else:
                    QMessageBox.warning(self, "导出", "%s索引导出失败" % cmt)
        else:
            fname = QFileDialog.getExistingDirectory(self, "另存为", QDir.homePath())
            unsaved_list = []
            for tmp_cmt in self.cmt_list:
                if tmp_cmt != "以上全部":
                    tmp_fname = fname + "/"+  tmp_cmt + "索引.xlsx"
                    ifsaved = CmtDB_Index().save_index_table_for_cmt(tmp_cmt, tmp_fname)
                    if not ifsaved:
                        unsaved_list.append(tmp_cmt)
            if len(unsaved_list) == 0:
                QMessageBox.information(self, "导出", "全部品种索引导出成功")
            else:
                unsaved_cmts = ",".join(unsaved_list)
                QMessageBox.warning(self, "导出", "除%s以外索引导出成功" % unsaved_cmts)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        