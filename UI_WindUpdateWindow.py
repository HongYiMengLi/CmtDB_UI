# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 09:28:55 2019

@author: 李弘一萌
"""

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_WindUpdateWindow(object):
    def setupUi(self, WindUpdateWindow):
        WindUpdateWindow.setObjectName("WindUpdateWindow")
        WindUpdateWindow.resize(1200, 600)
        self.vbox = QtWidgets.QVBoxLayout(WindUpdateWindow) 
        self.hwg1 = QtWidgets.QWidget()
        self.hbox1 = QtWidgets.QHBoxLayout() 
        self.cb = QtWidgets.QComboBox()   
        self.hbox2 = QtWidgets.QHBoxLayout()
        self.hbox2.addWidget(self.cb)
        self.groupbox1 = QtWidgets.QGroupBox("品种")
        self.groupbox1.setLayout(self.hbox2)
        self.btn = QtWidgets.QPushButton("开始更新万得数据")   
        self.hbox1.addWidget(self.groupbox1)
        self.hbox1.addWidget(self.btn)
        self.hwg1.setLayout(self.hbox1)
        self.textwindow = QtWidgets.QTextEdit()
        self.hbox3 = QtWidgets.QHBoxLayout()
        self.hbox3.addWidget(self.textwindow)
        self.groupbox2 = QtWidgets.QGroupBox("更新日志")
        self.groupbox2.setLayout(self.hbox3)
        
        self.vbox.addWidget(self.hwg1)
        self.vbox.addWidget(self.groupbox2)
        self.setLayout(self.vbox)

        self.retranslateUi(WindUpdateWindow)
        QtCore.QMetaObject.connectSlotsByName(WindUpdateWindow)

    def retranslateUi(self, WindUpdateWindow):
        _translate = QtCore.QCoreApplication.translate
        WindUpdateWindow.setWindowTitle(_translate("WindUpdateWindow", "万得数据更新"))