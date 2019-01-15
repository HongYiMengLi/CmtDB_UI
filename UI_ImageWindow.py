# -*- coding: utf-8 -*-
"""
Created on Fri Jan  4 09:30:32 2019

@author: 李弘一萌
"""

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ImageWindow(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1021, 895)        
        self.vbox = QtWidgets.QVBoxLayout(Dialog) 

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "图像"))