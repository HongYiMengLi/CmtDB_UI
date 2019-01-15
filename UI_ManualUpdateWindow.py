# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 11:29:15 2019

@author: 李弘一萌
"""

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ManualUpdateWindow(object):
    def setupUi(self, ManualUpdateWindow):
        ManualUpdateWindow.setObjectName("ManualUpdateWindow")
        ManualUpdateWindow.resize(1200, 800)
        self.vbox1 = QtWidgets.QVBoxLayout(ManualUpdateWindow) 
        
        self.hwg1 = QtWidgets.QWidget()
        self.hbox1 = QtWidgets.QHBoxLayout()
        
        self.hbox2 = QtWidgets.QHBoxLayout()
        self.groupbox1 = QtWidgets.QGroupBox("待选品种")
        self.allTable = QtWidgets.QTableWidget()
        self.allTable.setObjectName("allTable")
        self.allTable.setColumnCount(0)
        self.allTable.setRowCount(0)
        self.hbox2.addWidget(self.allTable)
        self.groupbox1.setLayout(self.hbox2)
        
        self.hbox3 = QtWidgets.QHBoxLayout()
        self.groupbox2 = QtWidgets.QGroupBox("已选品种")
        self.selectedTable = QtWidgets.QTableWidget(self.groupbox2)
        self.selectedTable.setObjectName("selectedTable")
        self.selectedTable.setColumnCount(0)
        self.selectedTable.setRowCount(0)
        self.hbox3.addWidget(self.selectedTable)
        self.groupbox2.setLayout(self.hbox3)
        
        
        self.hwg2 = QtWidgets.QWidget()
        self.vbox2 = QtWidgets.QVBoxLayout() 
        self.select_btn = QtWidgets.QPushButton(">>>")
        self.delete_btn = QtWidgets.QPushButton("<<<")
        self.vbox2.addWidget(self.select_btn)
        self.vbox2.addWidget(self.delete_btn)
        self.hwg2.setLayout(self.vbox2)
        
        self.hbox1.addWidget(self.groupbox1)
        self.hbox1.addWidget(self.hwg2)
        self.hbox1.addWidget(self.groupbox2)
        self.hwg1.setLayout(self.hbox1)

        self.hbox5 = QtWidgets.QHBoxLayout()
        self.hwg5 = QtWidgets.QWidget() 
        self.hwg3 = QtWidgets.QWidget()       
        self.start_btn = QtWidgets.QPushButton("开始更新手动数据")
        self.hwg4 = QtWidgets.QWidget()
        self.hbox5.addWidget(self.hwg3)
        self.hbox5.addWidget(self.start_btn)
        self.hbox5.addWidget(self.hwg4)
        self.hwg5.setLayout(self.hbox5)
        
        self.hbox4 = QtWidgets.QHBoxLayout()
        self.groupbox3 = QtWidgets.QGroupBox("更新日志")
        self.textwindow = QtWidgets.QTextEdit()
        self.hbox4.addWidget(self.textwindow)
        self.groupbox3.setLayout(self.hbox4)
                
        self.vbox1.addWidget(self.hwg1)
        self.vbox1.addWidget(self.hwg5)
        self.vbox1.addWidget(self.groupbox3)
        self.setLayout(self.vbox1)

        self.retranslateUi(ManualUpdateWindow)
        QtCore.QMetaObject.connectSlotsByName(ManualUpdateWindow)

    def retranslateUi(self, ManualUpdateWindow):
        _translate = QtCore.QCoreApplication.translate
        ManualUpdateWindow.setWindowTitle(_translate("ManualUpdateWindow", "手动数据更新"))