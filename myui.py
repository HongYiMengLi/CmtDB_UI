# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 09:00:09 2018

@author: 李弘一萌
"""

from UI_MainWindow import Ui_MainWindow
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QBrush, QColor, QCursor, QFont
from PyQt5.QtCore import Qt, QDir
from PyQt5.QtWidgets import QTreeWidgetItem, QHeaderView
import pandas as pd
import numpy as np
from PyQt5.QtCore import QCoreApplication
import pymysql
import qdarkstyle

import sys
sys.path.append("..\..")
from image_main import Image_Main
from windupdate_main import WindUpdate_Main
from manualupdate_main import ManualUpdate_Main
from indexoutput_main import IndexOutput_Main
from UI_DateDialog import DateDialog

from PandasModel import PandasModel
from MyPackages.Commodity_Data.IndexTable import CmtDB_Index
from MyPackages.Commodity_Data.Global_Factory import Global_Factory
from MyPackages.Futures_Data.Profile.CmtData import Cmt_Data

    
class My_UI(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(My_UI, self).__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon("Data_Center.png"))
        self.init_tree()
        self.init_index_table()
        self.init_df_table()
        self.init_toolbar()
        self.init_menubar()
        self.df = None
        self.cmt_profile = Cmt_Data.get_cmt_profile()
        

    def init_tree(self):
        self.treeWidget.setColumnCount(1)
        # 设置头的标题
        self.treeWidget.setHeaderLabels(['指标名称'])
        self.treeWidget.setColumnWidth(0, 160) 
        
        cmt_index_obj = CmtDB_Index()
        index_df = cmt_index_obj.get_index_tree_dict()
        
        tmp_field = ""
        tmp_cmt = ""
        tmp_table = ""
        tmp_cat = ""
        field_changed = False
        cmt_changed = False
        table_changed = False
        for (field, cmt, table, cat), data_group in index_df.groupby(by=["data_field", "data_cmt", "data_table", 
                                                                      "data_category"], sort=False):
            if tmp_field != field:
                root1 = QTreeWidgetItem(self.treeWidget)
                root1.setText(0, field)
                tmp_field = field
                field_changed = True
            else:
                if field_changed == True:
                    field_changed = False
            if tmp_cmt != cmt or field_changed == True:
                root2 = QTreeWidgetItem(root1)
                root2.setText(0, cmt)
                tmp_cmt = cmt
                cmt_changed = True
            else:
                if cmt_changed == True:
                    cmt_changed = False
                                
            if tmp_table != table or cmt_changed == True or field_changed == True:
                root3 = QTreeWidgetItem(root2)
                root3.setText(0, table)
                tmp_table = table
                table_changed = True
            else:
                if table_changed == True:
                    table_changed = False
            
            if tmp_cat != cat or table_changed == True or cmt_changed == True or field_changed == True:
                root4 = QTreeWidgetItem(root3)
                root4.setText(0, cat)
                tmp_cat = cat
            for _, row in data_group.iterrows():
                child = QTreeWidgetItem(root4)
                child.setText(0, row["data_name"])
        
        # 双击加入index_table
        self.treeWidget.itemDoubleClicked.connect(self.index_table_add_row)   	
        
#        self.treeWidget.addTopLevelItem(root)
#        # 结点全部展开
#        self.treeWidget.expandAll()

    def init_index_table(self):
        self.tableWidget_2.setColumnCount(12)
        self.tableWidget_2.setHorizontalHeaderLabels(["指标名称", "品种", "所属大类", "所属小类", "数据类型", "频率", 
                                                    "数据量", "起始时间", "结束时间", "更新时间", "来源", "备注"])
        self.tableWidget_2.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.tableWidget_2.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget_2.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget_2.setSelectionMode(QAbstractItemView.MultiSelection)
        self.tableWidget_2.verticalHeader().setVisible(False)
#        self.table.setColumnWidth(index, width)
        self.tableWidget_2.setContextMenuPolicy(Qt.CustomContextMenu)  # 右键菜单，如果不设为CustomContextMenu,无法使用customContextMenuRequested
        self.tableWidget_2.customContextMenuRequested.connect(self.onTableWidgetRightClick)


    def init_df_table(self):
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget.verticalHeader().setVisible(False)
        
        
    def init_toolbar(self):
        self.toolbar = self.addToolBar('Exit')
        self.loadAct = QAction(QIcon('play.png'), '提取数据', self)
#        self.loadAct.setShortcut('Ctrl+Q')
        
        self.toolbar.addAction(self.loadAct)
        self.loadAct.triggered.connect(self.populate_df)
        
        self.saveAct = QAction(QIcon('download.png'), '另存为Excel', self)
#        self.loadAct.setShortcut('Ctrl+Q')
        self.toolbar.addAction(self.saveAct)
        self.saveAct.triggered.connect(self.savedf)


        self.deleteIndexAct = QAction(QIcon('clear-index.png'), '清空指标', self)        
        self.toolbar.addAction(self.deleteIndexAct)
        self.deleteIndexAct.triggered.connect(self.clearIndex)  
        
        
        self.deleteTableAct = QAction(QIcon('delete.png'), '清空数据', self)        
        self.toolbar.addAction(self.deleteTableAct)
        self.deleteTableAct.triggered.connect(self.cleardf)   
        
        

    def init_menubar(self):
        self.menubar_file = self.menubar.addMenu("文件")        
        self.menubar_quit = QAction('退出', self)
        self.menubar_quit.setShortcut('Ctrl+Q')
        self.menubar_quit.triggered.connect(QCoreApplication.instance().quit)
        self.menubar_file.addAction(self.menubar_quit)
        
        self.menubar_index = self.menubar.addMenu("索引")        
        self.menubar_index_output = QAction('导出索引', self)
        self.menubar_index_output.triggered.connect(self.onMenuIndexOutput)
        self.menubar_index.addAction(self.menubar_index_output)       
        
        self.menubar_update = self.menubar.addMenu("更新")        
        self.menubar_update_wind = QAction('更新万得数据', self)
        self.menubar_update_wind.triggered.connect(self.onMenuWindUpdate)
        self.menubar_update.addAction(self.menubar_update_wind)    
        self.menubar_update_maunal = QAction('更新手动数据', self)
        self.menubar_update_maunal.triggered.connect(self.onMenuManualUpdate)
        self.menubar_update.addAction(self.menubar_update_maunal) 
        
        
    def index_table_add_row(self, item, column_no): # 将指标加入指标列表
        if item.childCount() == 0:
            rowPosition = self.tableWidget_2.rowCount()
            tmp_col = item.text(0)
            tmp_cmt = item.parent().parent().parent().text(0)
            tmp_cmt_name = Cmt_Data(tmp_cmt, self.cmt_profile).cmt_name 
            tmp_flag = True
            # 检查重复
            if rowPosition > 0:
                for index in range(rowPosition-1):
                    if (self.tableWidget_2.item(index, 0).text() == tmp_col) and (self.tableWidget_2.item(index, 1).text() == tmp_cmt_name):
                        tmp_flag = False
                        break
            
            if tmp_flag == True:
                self.tableWidget_2.insertRow(rowPosition)
                col_info = CmtDB_Index().get_total_index_table()
                col_ts = col_info[(col_info["data_cmt"]==tmp_cmt_name) & (col_info["data_name"]==tmp_col)].iloc[0, :]
                col_ts = col_ts.fillna("")
                self.tableWidget_2.setItem(rowPosition, 0, QTableWidgetItem(str(col_ts["data_name"])))
                self.tableWidget_2.setItem(rowPosition, 1, QTableWidgetItem(str(col_ts["data_cmt"])))         
                self.tableWidget_2.setItem(rowPosition, 2, QTableWidgetItem(str(col_ts["data_table"])))
                self.tableWidget_2.setItem(rowPosition, 3, QTableWidgetItem(str(col_ts["data_category"])))
                self.tableWidget_2.setItem(rowPosition, 4, QTableWidgetItem(str(col_ts["data_type"])))
                self.tableWidget_2.setItem(rowPosition, 5, QTableWidgetItem(str(col_ts["freq"])))
                if col_ts["length"] != "":
                    self.tableWidget_2.setItem(rowPosition, 6, QTableWidgetItem(str(int(col_ts["length"]))))
                if col_ts["start_date"] != "":
                    self.tableWidget_2.setItem(rowPosition, 7, QTableWidgetItem(col_ts["start_date"].strftime("%Y-%m-%d %H:%M:%S")))
                if col_ts["last_date"] != "":   
                    self.tableWidget_2.setItem(rowPosition, 8, QTableWidgetItem(col_ts["last_date"].strftime("%Y-%m-%d %H:%M:%S"))) 
                if col_ts["update_date"] != "":
                    self.tableWidget_2.setItem(rowPosition, 9, QTableWidgetItem(col_ts["update_date"].strftime("%Y-%m-%d %H:%M:%S"))) 
                self.tableWidget_2.setItem(rowPosition , 10, QTableWidgetItem(str(col_ts["source"])))
                self.tableWidget_2.setItem(rowPosition , 11, QTableWidgetItem(str(col_ts["remarks"])))
            
            
    def onTableWidgetRightClick(self, pos):  # 创建tablewidget右键菜单
        table_row_index = self.tableWidget_2.currentRow()
        if table_row_index >= 0:
            menu = QMenu() 
            # 删除
            Delete_Col_Action = menu.addAction("删除指标")
            Delete_Col_Action.triggered.connect(lambda: self.Delete_Col_Slot(table_row_index))
            # 季节性
            menu.addSeparator()
            tmp_cmt_cname = str(self.tableWidget_2.item(table_row_index, 1).text())
            tmp_cmt_name = Cmt_Data(tmp_cmt_cname, self.cmt_profile).cmt_name
            tmp_col = str(self.tableWidget_2.item(table_row_index, 0).text())
            tmp_obj = Global_Factory.getobj(tmp_col, tmp_cmt_name)
            
            Seasonal_Plot_Action = menu.addAction("生成季节性图")
            Seasonal_Plot_Action.triggered.connect(lambda: self.Seasonal_Plot_Slot(tmp_obj))

            TS_Plot_Action = menu.addAction("生成历史时序折线图")
            TS_Plot_Action.triggered.connect(lambda: self.TS_Plot_Slot(tmp_obj))
            
            menu.exec_(QCursor.pos())


    def onMenuWindUpdate(self):  # 菜单栏打开Wind更新界面，传递cmt_list参数
        total_cmt_list = CmtDB_Index().get_all_db_cmt_list()
        cmt_list = total_cmt_list
        self.tmp_update_wind_ui = WindUpdate_Main(cmt_list)
        self.tmp_update_wind_ui.show()


    def onMenuManualUpdate(self):  # 菜单栏打开Wind更新界面，传递cmt_list参数
        total_cmt_list = CmtDB_Index().get_all_db_cmt_list()
        cmt_list = total_cmt_list
        self.tmp_update_manual_ui = ManualUpdate_Main(cmt_list)
        self.tmp_update_manual_ui.show()

            
    def onMenuIndexOutput(self):  # 菜单栏打开Wind更新界面，传递cmt_list参数
        total_cmt_list = CmtDB_Index().get_all_db_cmt_list()
        cmt_list = total_cmt_list
        self.tmp_index_output_ui = IndexOutput_Main(cmt_list)
        self.tmp_index_output_ui.show()

        
    def Seasonal_Plot_Slot(self, col_obj):        
        col_info = CmtDB_Index().get_total_index_table()
        col_ts = col_info[(col_info["data_cmt"]==col_obj.cmt_name) & (col_info["data_name"]==col_obj.col_name)].iloc[0, :]
        tmp_start_year = col_ts["start_date"].year
        tmp_end_date = col_ts["last_date"].year
        year_list = range(tmp_start_year, tmp_end_date+1)
        start_year, ok = QInputDialog.getItem(self, "起始年份", "输入起始年份", [str(x) for x in year_list], 0, False)
        if ok and start_year:             
            self.tmp_image_ui = Image_Main(col_obj, "seasonal", int(start_year))
            self.tmp_image_ui.show()
            

    def TS_Plot_Slot(self, col_obj):        
        col_info = CmtDB_Index().get_total_index_table()
        col_ts = col_info[(col_info["data_cmt"]==col_obj.cmt_name) & (col_info["data_name"]==col_obj.col_name)].iloc[0, :]
        tmp_start_year = col_ts["start_date"]
        tmp_end_date = col_ts["last_date"]
        start_date, ok = DateDialog.getDate()
        if ok and start_date:             
            self.tmp_image_ui = Image_Main(col_obj, "ts", start_date)
            self.tmp_image_ui.show()        
        
    def Delete_Col_Slot(self, table_row_index):
        self.tableWidget_2.removeRow(table_row_index)
        
        
    def populate_df(self):
        if self.tableWidget_2.rowCount() == 0:
            print("无可提取数据")
            return
        else:
            ts_list = []
            for r in range(self.tableWidget_2.rowCount()):
                col_item = self.tableWidget_2.item(r, 0)
                tmp_col = col_item.text()
                cmt_item = self.tableWidget_2.item(r, 1)
                tmp_cmt_cname = cmt_item.text()
                tmp_cmt_name = Cmt_Data(tmp_cmt_cname, self.cmt_profile).cmt_name
                tmp_ts = Global_Factory.getobj(tmp_col, tmp_cmt_name).get_ts()
                ts_list.append(tmp_ts)
            tmp_df = pd.concat(ts_list, axis=1, sort=False)
            
            if len(tmp_df) == 0:
                print("提取数据为空")
                return
            else:
                tmp_df = tmp_df.reset_index()
                tmp_df.rename(columns={'date':'日期'}, inplace=True)
                tmp_ts = tmp_df["日期"].apply(lambda x:x.to_pydatetime().strftime("%Y-%m-%d"))
                tmp_df["日期"] = tmp_ts
                self.model = PandasModel(tmp_df)
                self.df = tmp_df.copy()
                self.tableWidget.setModel(self.model)
                self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)


    def savedf(self):
        fname, ok = QFileDialog.getSaveFileName(self, "另存为", QDir.homePath() + "/数据库下载.xlsx", "Excel Files (*.xlsx)")
        if ok:
            if self.df is None:
                QMessageBox.warning(self, "数据提取错误", "未选择任何数据")
            elif len(self.df) == 0:
                QMessageBox.warning(self, "数据提取错误", "数据长度为0")
            else:
                tmp_df = self.df.copy()
                tmp_df = tmp_df.set_index("日期")
                tmp_df.to_excel(fname, encoding="gbk")

    def cleardf(self):        
        self.df = pd.DataFrame()
        self.model = PandasModel(self.df)
        self.tableWidget.setModel(self.model)

    def clearIndex(self):        
        rowPosition = self.tableWidget_2.rowCount()
        for i in range(rowPosition, 0, -1):
            self.tableWidget_2.removeRow(i-1) 
        
         
#        model = self.model
#        indices = self.tableWidget.selectionModel()
#        for index in sorted(indices):
#            self.model.removeRow(index.row()) 

    def closeEvent(self, event):
        if hasattr(self, "tmp_update_wind_ui"):
            self.tmp_update_wind_ui.close()
        if hasattr(self, "tmp_update_manual_ui"):
            self.tmp_update_manual_ui.close()            
        if hasattr(self, "tmp_image_ui"):
            self.tmp_image_ui.close() 
        if hasattr(self, "tmp_index_output_ui"):
            self.tmp_index_output_ui.close() 
                       
        event.accept()

if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    main_ui = My_UI()
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    myFont = QFont("Microsoft YaHei", 13)
    myFont.setBold(True)
    app.setFont(myFont)
    qssStyle = """                
            QTreeView::branch:has-children:!has-siblings:closed,
            QTreeView::branch:closed:has-children:has-siblings {
                    border-image: none;
                    image: url(branch-closed.png);
            }
            
            QTreeView::branch:open:has-children:!has-siblings,
            QTreeView::branch:open:has-children:has-siblings  {
                    border-image: none;
                    image: url(branch-open.png);
            }
            """
            
    main_ui.setStyleSheet(qssStyle)
    main_ui.showMaximized()
    sys.exit(app.exec_())
#    sys.exit(0)






