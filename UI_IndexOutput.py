# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 14:14:33 2019

@author: 李弘一萌
"""

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_IndexOuptputWindow(object):
    def setupUi(self, IndexOuptputWindow):
        IndexOuptputWindow.setObjectName("IndexOuptputWindow")
        IndexOuptputWindow.resize(400, 100)
        self.hbox1 = QtWidgets.QHBoxLayout() 
        self.cb = QtWidgets.QComboBox()   
        self.hbox2 = QtWidgets.QHBoxLayout()
        self.hbox2.addWidget(self.cb)
        self.groupbox1 = QtWidgets.QGroupBox("品种")
        self.groupbox1.setLayout(self.hbox2)
        self.btn = QtWidgets.QPushButton("导出索引文件")   
        self.hbox1.addWidget(self.groupbox1)
        self.hbox1.addWidget(self.btn)
        self.setLayout(self.hbox1)
        

        self.retranslateUi(IndexOuptputWindow)
        QtCore.QMetaObject.connectSlotsByName(IndexOuptputWindow)

    def retranslateUi(self, IndexOuptputWindow):
        _translate = QtCore.QCoreApplication.translate
        IndexOuptputWindow.setWindowTitle(_translate("IndexOuptputWindow", "索引导出"))