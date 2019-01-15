# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'my_first.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1021, 895)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        # 原布局
#        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
#        self.gridLayout_2.setObjectName("gridLayout_2")
#        self.gridLayout = QtWidgets.QGridLayout()
#        self.gridLayout.setSpacing(10)
#        self.gridLayout.setObjectName("gridLayout")
#        self.tableWidget = QtWidgets.QTableView(self.centralwidget)
#        self.tableWidget.setObjectName("tableWidget")
#        self.gridLayout.addWidget(self.tableWidget, 3, 2, 7, 8)
#        self.treeWidget = QtWidgets.QTreeWidget(self.centralwidget)
#        self.treeWidget.setObjectName("treeWidget")
#        self.treeWidget.headerItem().setText(0, "1")
#        self.gridLayout.addWidget(self.treeWidget, 0, 0, 10, 2)
#        self.tableWidget_2 = QtWidgets.QTableWidget(self.centralwidget)
#        self.tableWidget_2.setObjectName("tableWidget_2")
#        self.tableWidget_2.setColumnCount(0)
#        self.tableWidget_2.setRowCount(0)
#        self.gridLayout.addWidget(self.tableWidget_2, 0, 2, 3, 8)
#        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
#        MainWindow.setCentralWidget(self.centralwidget)
        
        # 新布局
        self.hbox = QtWidgets.QHBoxLayout(self.centralwidget) 
        
        self.tableWidget = QtWidgets.QTableView(self.centralwidget)
        self.tableWidget.setObjectName("tableWidget")
        self.treeWidget = QtWidgets.QTreeWidget(self.centralwidget)
        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget.headerItem().setText(0, "1")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(0)
        self.tableWidget_2.setRowCount(0)
   
    
        self.splitter1 = QtWidgets.QSplitter(QtCore.Qt.Vertical)
        self.splitter1.addWidget(self.tableWidget_2)
        self.splitter1.addWidget(self.tableWidget) 
        self.splitter1.setStretchFactor(1, 3)
        self.splitter2 = QtWidgets.QSplitter(QtCore.Qt.Horizontal)
        self.splitter2.addWidget(self.treeWidget)
        self.splitter2.addWidget(self.splitter1)   
        self.splitter2.setStretchFactor(1, 2)
        self.hbox.addWidget(self.splitter2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1021, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "数据库简易测试版"))

