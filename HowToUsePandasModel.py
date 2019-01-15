# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 18:31:00 2018

@author: Administrator
"""

def btn_clk(self):
    path = self.lineEdit.text()
    df = pd.read_csv(path)
    model = PandasModel(df)
    self.tableView.setModel(model)
