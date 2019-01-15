# -*- coding: utf-8 -*-
"""
Created on Fri Jan  4 10:29:51 2019

@author: Administrator
"""

#-*-coding:utf-8-*-
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
import numpy as np
from UI_ImageWindow import Ui_ImageWindow

import matplotlib
matplotlib.use("Qt5Agg")  # 声明使用QT5
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

#创建一个matplotlib图形绘制类
class MyFigure(FigureCanvas):
    def __init__(self, col_obj, fig_type, start):
        #第一步：创建一个创建Figure
        if fig_type == "seasonal":
            _, self.fig, self.axis = col_obj.seasonal_plot(start_year=start)
        elif fig_type == "ts":
            _, self.fig, self.axis = col_obj.ts_plot(start_date=start)
        #第二步：在父类中激活Figure窗口
        super(MyFigure, self).__init__(self.fig) #此句必不可少，否则不能显示图形
        #第三步：创建一个子图，用于绘制图形用，111表示子图编号，如matlab的subplot(1,1,1)
#        self.axis = self.fig.add_subplot(111)
    #第四步：就是画图，【可以在此类中画，也可以在其它类中画】
#    def plotsin(self):
#        self.axes0 = self.fig.add_subplot(111)
#        t = np.arange(0.0, 3.0, 0.01)
#        s = np.sin(2 * np.pi * t)
#        self.axes0.plot(t, s)
#    def plotcos(self):
#        t = np.arange(0.0, 3.0, 0.01)
#        s = np.sin(2 * np.pi * t)
#        self.axes.plot(t, s)


class Image_Main(QWidget, Ui_ImageWindow):
    def __init__(self, col_obj, fig_type, start, parent=None):
        super(Image_Main, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("显示matplotlib绘制图形")
        self.setMinimumSize(0,0)
        self.col_obj = col_obj
        #第五步：定义MyFigure类的一个实例
        self.F = MyFigure(col_obj, fig_type, start)
        self.toolbar = NavigationToolbar(self.F, parent)
        #self.F.plotsin()
#        self.F.fig, self.F.axis, _ = self.col_obj.seasonal_plot()
        self.vbox.addWidget(self.toolbar)
        self.vbox.addWidget(self.F)
        self.setLayout(self.vbox)

        #add layout to qwidget
        #第六步：在GUI的groupBox中创建一个布局，用于添加MyFigure类的实例（即图形）后其他部件。


#    def plotcos(self):
#        t = np.arange(0.0, 5.0, 0.01)
#        s = np.cos(2 * np.pi * t)
#        self.F.axes.plot(t, s)
#        self.F.fig.suptitle("cos")
#        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = Image_Main()
    main.show()
    #app.installEventFilter(main)
    sys.exit(app.exec_())
