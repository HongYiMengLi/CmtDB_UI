# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 10:19:15 2019

@author: Administrator
"""
from PyQt5.QtWidgets import *
from datetime import datetime
from PyQt5.QtGui import QIcon, QBrush, QColor, QCursor, QFont
from PyQt5.QtCore import Qt, QDir, QDate
from PyQt5.QtWidgets import QTreeWidgetItem, QHeaderView
import pandas as pd
import numpy as np
from PyQt5.QtCore import QCoreApplication

class DateDialog(QDialog):
    def __init__(self, parent = None):
        super(DateDialog, self).__init__(parent)

        layout = QVBoxLayout(self)

        # nice widget for editing the date
        self.dateEdit = QDateEdit(self)
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setDate(QDate.currentDate())
        layout.addWidget(self.dateEdit)

        # OK and Cancel buttons
        buttons = QDialogButtonBox(
            QDialogButtonBox.Ok | QDialogButtonBox.Cancel,
            Qt.Horizontal, self)
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)
        layout.addWidget(buttons)

    # get current date and time from the dialog
    def dateTime(self):
        return self.dateEdit.date()

    # static method to create the dialog and return (date, time, accepted)
    @staticmethod
    def getDate(parent = None):
        dialog = DateDialog(parent)
        result = dialog.exec_()
        tmp_date = dialog.dateTime()
        return (datetime(tmp_date.year(), tmp_date.month(), tmp_date.day()), result == QDialog.Accepted)
    