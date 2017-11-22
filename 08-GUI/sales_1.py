# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'code_1.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap

from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QAction, QTableWidget, QTableWidgetItem, QVBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

import pymysql

connection = pymysql.connect(host='localhost', port=3306, user='root',
                       passwd='', db='mobileStore', autocommit=True)

cursor = connection.cursor()


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1058, 774)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(430, -20, 591, 111))
        self.label.setStyleSheet("color: rgb(0, 0, 153);\n"
                                 "font: 75 8pt \"MS Shell Dlg 2\";\n"
                                 "font: 20pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1058, 31))

        self.label_img = QtWidgets.QLabel(self.centralwidget)
        self.label_img.setGeometry(QtCore.QRect(256, 100, 825, 595))
        pixmap = QPixmap("apple3.jpg")
        self.label_img.setPixmap(pixmap)



        self.menubar.setObjectName("menubar")
        self.menuITEM_MASTER = QtWidgets.QMenu(self.menubar)
        self.menuITEM_MASTER.setObjectName("menuITEM_MASTER")
        self.menuSALES_MASTER = QtWidgets.QMenu(self.menubar)
        self.menuSALES_MASTER.setObjectName("menuSALES_MASTER")
        self.menuPURCHASE_MASTER = QtWidgets.QMenu(self.menubar)
        self.menuPURCHASE_MASTER.setObjectName("menuPURCHASE_MASTER")
        self.menuEMP_DETAILS = QtWidgets.QMenu(self.menubar)
        self.menuEMP_DETAILS.setObjectName("menuEMP_DETAILS")
        self.menuDAILY_EXPENSE = QtWidgets.QMenu(self.menubar)
        self.menuDAILY_EXPENSE.setObjectName("menuDAILY_EXPENSE")
        self.menuREPORTS = QtWidgets.QMenu(self.menubar)
        self.menuREPORTS.setObjectName("menuREPORTS")
        self.menuLOGIN = QtWidgets.QMenu(self.menubar)
        self.menuLOGIN.setObjectName("menuLOGIN")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)


        self.actionAdd_New_Item = QtWidgets.QAction(MainWindow)
        self.actionAdd_New_Item.setObjectName("actionAdd_New_Item")
        self.actionEdit_Item = QtWidgets.QAction(MainWindow)
        self.actionEdit_Item.setObjectName("actionEdit_Item")
        self.actionDelete_Item = QtWidgets.QAction(MainWindow)
        self.actionDelete_Item.setObjectName("actionDelete_Item")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")



        self.actionAdd_Sales = QtWidgets.QAction(MainWindow)
        self.actionAdd_Sales.setObjectName("actionAdd_Sales")
        self.actionDelete_Item_2 = QtWidgets.QAction(MainWindow)
        self.actionDelete_Item_2.setObjectName("actionDelete_Item_2")

        self.actionAdd_purchase_Order = QtWidgets.QAction(MainWindow)
        self.actionAdd_purchase_Order.setObjectName("actionAdd_purchase_Order")


        self.actionAdd_Emp_Details = QtWidgets.QAction(MainWindow)
        self.actionAdd_Emp_Details.setObjectName("actionAdd_Emp_Details")

        self.actionAdd_daily_expense = QtWidgets.QAction(MainWindow)
        self.actionAdd_daily_expense.setObjectName("actionAdd_daily_expense")


        self.actionStock_Report = QtWidgets.QAction(MainWindow)
        self.actionStock_Report.setObjectName("actionStock_Report")


        self.actionSales_Report = QtWidgets.QAction(MainWindow)
        self.actionSales_Report.setObjectName("actionSales_Report")


        self.actionPurchase_Report = QtWidgets.QAction(MainWindow)
        self.actionPurchase_Report.setObjectName("actionPurchase_Report")


        self.actionChange_Password = QtWidgets.QAction(MainWindow)
        self.actionChange_Password.setObjectName("actionChange_Password")


        self.menuITEM_MASTER.addAction(self.actionAdd_New_Item)
        self.menuITEM_MASTER.addAction(self.actionEdit_Item)
        self.menuITEM_MASTER.addAction(self.actionDelete_Item)
        self.menuITEM_MASTER.addAction(self.actionExit)

        self.menuSALES_MASTER.addAction(self.actionAdd_Sales)
        self.menuSALES_MASTER.addSeparator()
        self.menuSALES_MASTER.addAction(self.actionDelete_Item_2)

        self.menuPURCHASE_MASTER.addAction(self.actionAdd_purchase_Order)


        self.menuEMP_DETAILS.addAction(self.actionAdd_Emp_Details)

        self.menuDAILY_EXPENSE.addAction(self.actionAdd_daily_expense)

        self.menuREPORTS.addAction(self.actionStock_Report)
        self.menuREPORTS.addAction(self.actionSales_Report)
        self.menuREPORTS.addAction(self.actionPurchase_Report)
        self.menuLOGIN.addAction(self.actionChange_Password)


        self.menubar.addAction(self.menuITEM_MASTER.menuAction())
        self.menubar.addAction(self.menuSALES_MASTER.menuAction())
        self.menubar.addAction(self.menuPURCHASE_MASTER.menuAction())
        self.menubar.addAction(self.menuEMP_DETAILS.menuAction())
        self.menubar.addAction(self.menuDAILY_EXPENSE.menuAction())
        self.menubar.addAction(self.menuREPORTS.menuAction())
        self.menubar.addAction(self.menuLOGIN.menuAction())

        # frame_1 item -add

        self.frame = QtWidgets.QFrame(MainWindow)
        self.frame.setGeometry(QtCore.QRect(0, 100, 1085, 731))
        self.frame.setStyleSheet("background-color: rgb(249, 249, 249);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.label_img = QtWidgets.QLabel(self.frame)
        self.label_img.setGeometry(QtCore.QRect(556, 0, 825, 595))
        pixmap = QPixmap("620x620,5.png")
        self.label_img.setPixmap(pixmap)


        self.label_1 = QtWidgets.QLabel(self.frame)
        self.label_1.setGeometry(QtCore.QRect(140, 50, 60, 16))
        self.label_1.setObjectName("label_1")
        self.lineEdit_1 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_1.setGeometry(QtCore.QRect(210, 50, 113, 21))
        self.lineEdit_1.setText(None)
        self.lineEdit_1.setObjectName("lineEdit_1")

        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(120, 100, 81, 21))
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(210, 100, 113, 21))
        self.lineEdit_2.setText(None)
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(160, 150, 41, 21))
        self.label_3.setObjectName("label_3")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_3.setGeometry(QtCore.QRect(210, 150, 113, 21))
        self.lineEdit_3.setText(None)
        self.lineEdit_3.setObjectName("lineEdit_3")

        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(90, 200, 101, 21))
        self.label_4.setObjectName("label_4")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_4.setGeometry(QtCore.QRect(210, 200, 113, 21))
        self.lineEdit_4.setText(None)
        self.lineEdit_4.setObjectName("lineEdit_4")

        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(150, 250, 61, 21))
        self.label_5.setObjectName("label_5")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_5.setGeometry(QtCore.QRect(210, 250, 113, 21))
        self.lineEdit_5.setText(None)
        self.lineEdit_5.setObjectName("lineEdit_5")

        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(100, 340, 113, 32))
        self.pushButton.setObjectName("pushButton")

        self.pushButton.clicked.connect(self.exec_query)

        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(250, 340, 113, 32))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)

        self.pushButton_3.setGeometry(QtCore.QRect(400, 340, 113, 32))
        self.pushButton_3.setObjectName("pushButton_3")




        self.frame.hide()

        # frame_2 item -edit

        self.frame_2 = QtWidgets.QFrame(MainWindow)
        self.frame_2.setGeometry(QtCore.QRect(0, 100, 1085, 731))
        self.frame_2.setStyleSheet("background-color: rgb(249, 249, 249);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame")

        self.label_6 = QtWidgets.QLabel(self.frame_2)
        self.label_6.setGeometry(QtCore.QRect(140, 50, 60, 16))
        self.label_6.setObjectName("label_6")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_6.setGeometry(QtCore.QRect(210, 50, 113, 21))
        self.lineEdit_6.setText("")
        self.lineEdit_6.setObjectName("lineEdit_6")

        self.label_7 = QtWidgets.QLabel(self.frame_2)
        self.label_7.setGeometry(QtCore.QRect(120, 100, 81, 21))
        self.label_7.setObjectName("label_7")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_7.setGeometry(QtCore.QRect(210, 100, 113, 21))
        self.lineEdit_7.setText("")
        self.lineEdit_7.setObjectName("lineEdit_7")


        self.label_8 = QtWidgets.QLabel(self.frame_2)
        self.label_8.setGeometry(QtCore.QRect(160, 150, 41, 21))
        self.label_8.setObjectName("label_8")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_8.setGeometry(QtCore.QRect(210, 150, 113, 21))
        self.lineEdit_8.setText("")
        self.lineEdit_8.setObjectName("lineEdit_8")


        self.label_9 = QtWidgets.QLabel(self.frame_2)
        self.label_9.setGeometry(QtCore.QRect(90, 200, 101, 21))
        self.label_9.setObjectName("label_9")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_9.setGeometry(QtCore.QRect(210, 200, 113, 21))
        self.lineEdit_9.setText("")
        self.lineEdit_9.setObjectName("lineEdit_9")


        self.label_10 = QtWidgets.QLabel(self.frame_2)
        self.label_10.setGeometry(QtCore.QRect(150, 250, 61, 21))
        self.label_10.setObjectName("label_10")
        self.lineEdit_10 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_10.setGeometry(QtCore.QRect(210, 250, 113, 21))
        self.lineEdit_10.setText("")
        self.lineEdit_10.setObjectName("lineEdit_10")


        self.pushButton_4 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_4.setGeometry(QtCore.QRect(100, 340, 113, 32))
        self.pushButton_4.setObjectName("pushButton_4")

        self.pushButton_4.clicked.connect(self.edit)

        self.pushButton_5 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_5.setGeometry(QtCore.QRect(400, 340, 113, 32))
        self.pushButton_5.setObjectName("pushButton_5")

        self.frame_2.hide()

        # frame_3 item -delete

        self.frame_3 = QtWidgets.QFrame(MainWindow)
        self.frame_3.setGeometry(QtCore.QRect(0, 100, 1085, 731))
        self.frame_3.setStyleSheet("background-color: rgb(249, 249, 249);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame")

        self.label_11 = QtWidgets.QLabel(self.frame_3)
        self.label_11.setGeometry(QtCore.QRect(140, 50, 60, 16))
        self.label_11.setObjectName("label_11")
        self.lineEdit_11 = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_11.setGeometry(QtCore.QRect(210, 50, 113, 21))
        self.lineEdit_11.setText("")
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.label_12 = QtWidgets.QLabel(self.frame_3)
        self.label_12.setGeometry(QtCore.QRect(120, 100, 81, 21))
        self.label_12.setObjectName("label_12")
        self.lineEdit_12 = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_12.setGeometry(QtCore.QRect(210, 100, 113, 21))
        self.lineEdit_12.setText("")
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.label_13 = QtWidgets.QLabel(self.frame_3)
        self.label_13.setGeometry(QtCore.QRect(160, 150, 41, 21))
        self.label_13.setObjectName("label_13")
        self.lineEdit_13 = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_13.setGeometry(QtCore.QRect(210, 150, 113, 21))
        self.lineEdit_13.setText("")
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.label_14= QtWidgets.QLabel(self.frame_3)
        self.label_14.setGeometry(QtCore.QRect(90, 200, 101, 21))
        self.label_14.setObjectName("label_14")
        self.lineEdit_14 = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_14.setGeometry(QtCore.QRect(210, 200, 113, 21))
        self.lineEdit_14.setText("")
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.label_15 = QtWidgets.QLabel(self.frame_3)
        self.label_15.setGeometry(QtCore.QRect(150, 250, 61, 21))
        self.label_15.setObjectName("label_15")
        self.lineEdit_15 = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_15.setGeometry(QtCore.QRect(210, 250, 113, 21))
        self.lineEdit_15.setText("")
        self.lineEdit_15.setObjectName("lineEdit_15")

        self.pushButton_6 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_6.setGeometry(QtCore.QRect(100, 340, 113, 32))
        self.pushButton_6.setObjectName("pushButton_6")

        self.pushButton_6.clicked.connect(self.delete)

        self.pushButton_7 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_7.setGeometry(QtCore.QRect(400, 340, 113, 32))
        self.pushButton_7.setObjectName("pushButton_7")

        self.frame_3.hide()

        # frame_4 sales -add

        self.frame_4 = QtWidgets.QFrame(MainWindow)
        self.frame_4.setGeometry(QtCore.QRect(0, 100, 1085, 731))
        self.frame_4.setStyleSheet("background-color: rgb(255, 153, 255);")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame")

        self.label_img = QtWidgets.QLabel(self.frame_4)
        self.label_img.setGeometry(QtCore.QRect(556, 0, 825, 595))
        pixmap = QPixmap("Samsung-Mobile-Phone-PNG-HD.png")
        self.label_img.setPixmap(pixmap)

        self.label_16 = QtWidgets.QLabel(self.frame_4)
        self.label_16.setGeometry(QtCore.QRect(140, 50, 60, 16))

        self.label_16.setObjectName("label_16")
        self.lineEdit_16 = QtWidgets.QLineEdit(self.frame_4)
        self.lineEdit_16.setGeometry(QtCore.QRect(210, 50, 113, 21))
        self.lineEdit_16.setStyleSheet("background-color: rgb(204, 255, 255);")
        self.lineEdit_16.setText("")
        self.lineEdit_16.setObjectName("lineEdit_16")

        self.label_17 = QtWidgets.QLabel(self.frame_4)
        self.label_17.setGeometry(QtCore.QRect(100, 100, 101, 21))
        self.label_17.setObjectName("label_17")
        self.lineEdit_17 = QtWidgets.QLineEdit(self.frame_4)
        self.lineEdit_17.setGeometry(QtCore.QRect(210, 100, 113, 21))
        self.lineEdit_17.setText("")
        self.lineEdit_17.setObjectName("lineEdit_17")

        self.label_18 = QtWidgets.QLabel(self.frame_4)
        self.label_18.setGeometry(QtCore.QRect(140, 150, 61, 21))
        self.label_18.setObjectName("label_18")
        self.lineEdit_18 = QtWidgets.QLineEdit(self.frame_4)
        self.lineEdit_18.setGeometry(QtCore.QRect(210, 150, 113, 21))
        self.lineEdit_18.setText("")
        self.lineEdit_18.setObjectName("lineEdit_18")

        self.label_19 = QtWidgets.QLabel(self.frame_4)
        self.label_19.setGeometry(QtCore.QRect(90, 200, 101, 21))
        self.label_19.setObjectName("label_19")
        self.lineEdit_19 = QtWidgets.QLineEdit(self.frame_4)
        self.lineEdit_19.setGeometry(QtCore.QRect(210, 200, 113, 21))
        self.lineEdit_19.setText("")
        self.lineEdit_19.setObjectName("lineEdit_19")

        self.label_20 = QtWidgets.QLabel(self.frame_4)
        self.label_20.setGeometry(QtCore.QRect(150, 250, 61, 21))
        self.label_20.setObjectName("label_20")
        self.lineEdit_20 = QtWidgets.QLineEdit(self.frame_4)
        self.lineEdit_20.setGeometry(QtCore.QRect(210, 250, 113, 21))
        self.lineEdit_20.setText("")
        self.lineEdit_20.setObjectName("lineEdit_20")

        self.pushButton_8 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_8.setGeometry(QtCore.QRect(100, 340, 113, 32))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_8.clicked.connect(self.addsales)

        self.pushButton_9 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_9.setGeometry(QtCore.QRect(400, 340, 113, 32))
        self.pushButton_9.setObjectName("pushButton_9")


        self.pushButton_10 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_10.setGeometry(QtCore.QRect(240, 340, 113, 32))
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_10.clicked.connect(self.showsales)

        self.frame_4.hide()

        # frame_5 sales -delete

        self.frame_5 = QtWidgets.QFrame(MainWindow)
        self.frame_5.setGeometry(QtCore.QRect(0, 100, 1085, 731))
        self.frame_5.setStyleSheet("background-color: rgb(255, 153, 255);")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame")

        self.label_img = QtWidgets.QLabel(self.frame_5)
        self.label_img.setGeometry(QtCore.QRect(556, 0, 825, 595))
        pixmap = QPixmap("Samsung-Mobile-Phone-PNG-HD.png")
        self.label_img.setPixmap(pixmap)


        self.label_21 = QtWidgets.QLabel(self.frame_5)
        self.label_21.setGeometry(QtCore.QRect(140, 50, 60, 16))
        self.label_21.setObjectName("label_21")
        self.lineEdit_21 = QtWidgets.QLineEdit(self.frame_5)
        self.lineEdit_21.setGeometry(QtCore.QRect(210, 50, 113, 21))
        self.lineEdit_21.setText("")
        self.lineEdit_21.setObjectName("lineEdit_21")
        self.label_22 = QtWidgets.QLabel(self.frame_5)
        self.label_22.setGeometry(QtCore.QRect(120, 100, 81, 21))
        self.label_22.setObjectName("label_22")
        self.lineEdit_22 = QtWidgets.QLineEdit(self.frame_5)
        self.lineEdit_22.setGeometry(QtCore.QRect(210, 100, 113, 21))
        self.lineEdit_22.setText("")
        self.lineEdit_22.setObjectName("lineEdit_22")
        self.label_23 = QtWidgets.QLabel(self.frame_5)
        self.label_23.setGeometry(QtCore.QRect(160, 150, 41, 21))
        self.label_23.setObjectName("label_23")
        self.lineEdit_23 = QtWidgets.QLineEdit(self.frame_5)
        self.lineEdit_23.setGeometry(QtCore.QRect(210, 150, 113, 21))
        self.lineEdit_23.setText("")
        self.lineEdit_23.setObjectName("lineEdit_23")
        self.label_24 = QtWidgets.QLabel(self.frame_5)
        self.label_24.setGeometry(QtCore.QRect(90, 200, 101, 21))
        self.label_24.setObjectName("label_24")
        self.lineEdit_24 = QtWidgets.QLineEdit(self.frame_5)
        self.lineEdit_24.setGeometry(QtCore.QRect(210, 200, 113, 21))
        self.lineEdit_24.setText("")
        self.lineEdit_24.setObjectName("lineEdit_24")
        self.label_25 = QtWidgets.QLabel(self.frame_5)
        self.label_25.setGeometry(QtCore.QRect(150, 250, 61, 21))
        self.label_25.setObjectName("label_25")
        self.lineEdit_25 = QtWidgets.QLineEdit(self.frame_5)
        self.lineEdit_25.setGeometry(QtCore.QRect(210, 250, 113, 21))
        self.lineEdit_25.setText("")
        self.lineEdit_25.setObjectName("lineEdit_25")
        self.pushButton_11 = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_11.setGeometry(QtCore.QRect(100, 340, 113, 32))
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_11.clicked.connect(self.deletesales)

        self.pushButton_12 = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_12.setGeometry(QtCore.QRect(400, 340, 113, 32))
        self.pushButton_12.setObjectName("pushButton_12")

        self.frame_5.hide()

        # frame_6 purchase -order

        self.frame_6 = QtWidgets.QFrame(MainWindow)
        self.frame_6.setGeometry(QtCore.QRect(0, 100, 1085, 731))
        self.frame_6.setStyleSheet("background-color: rgb(255, 153, 255);")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame")

        self.label_img = QtWidgets.QLabel(self.frame_6)
        self.label_img.setGeometry(QtCore.QRect(556, 0, 825, 595))
        pixmap = QPixmap("Samsung-Mobile-Phone-PNG-HD.png")
        self.label_img.setPixmap(pixmap)

        self.label_26 = QtWidgets.QLabel(self.frame_6)
        self.label_26.setGeometry(QtCore.QRect(119, 50, 81, 20))
        self.label_26.setObjectName("label_26")
        self.lineEdit_26 = QtWidgets.QLineEdit(self.frame_6)
        self.lineEdit_26.setGeometry(QtCore.QRect(210, 50, 113, 21))
        self.lineEdit_26.setText("")
        self.lineEdit_26.setObjectName("lineEdit_26")
        self.label_27 = QtWidgets.QLabel(self.frame_6)
        self.label_27.setGeometry(QtCore.QRect(120, 100, 81, 21))
        self.label_27.setObjectName("label_27")
        self.lineEdit_27 = QtWidgets.QLineEdit(self.frame_6)
        self.lineEdit_27.setGeometry(QtCore.QRect(210, 100, 113, 21))
        self.lineEdit_27.setText("")
        self.lineEdit_27.setObjectName("lineEdit_27")
        self.label_28 = QtWidgets.QLabel(self.frame_6)
        self.label_28.setGeometry(QtCore.QRect(100, 150, 101, 21))
        self.label_28.setObjectName("label_28")
        self.lineEdit_28 = QtWidgets.QLineEdit(self.frame_6)
        self.lineEdit_28.setGeometry(QtCore.QRect(210, 150, 113, 21))
        self.lineEdit_28.setText("")
        self.lineEdit_28.setObjectName("lineEdit_28")
        self.label_29 = QtWidgets.QLabel(self.frame_6)
        self.label_29.setGeometry(QtCore.QRect(130, 200, 71, 16))
        self.label_29.setObjectName("label_29")
        self.lineEdit_29 = QtWidgets.QLineEdit(self.frame_6)
        self.lineEdit_29.setGeometry(QtCore.QRect(210, 200, 113, 21))
        self.lineEdit_29.setText("")
        self.lineEdit_29.setObjectName("lineEdit_29")
        self.label_30 = QtWidgets.QLabel(self.frame_6)
        self.label_30.setGeometry(QtCore.QRect(150, 250, 61, 21))
        self.label_30.setObjectName("label_30")
        self.lineEdit_30 = QtWidgets.QLineEdit(self.frame_6)
        self.lineEdit_30.setGeometry(QtCore.QRect(210, 250, 113, 21))
        self.lineEdit_30.setText("")
        self.lineEdit_30.setObjectName("lineEdit_30")
        self.pushButton_13 = QtWidgets.QPushButton(self.frame_6)
        self.pushButton_13.setGeometry(QtCore.QRect(100, 440, 113, 32))
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_13.clicked.connect(self.addpurchase)


        self.pushButton_14 = QtWidgets.QPushButton(self.frame_6)
        self.pushButton_14.setGeometry(QtCore.QRect(380, 440, 113, 32))
        self.pushButton_14.setObjectName("pushButton_14")


        self.label_31 = QtWidgets.QLabel(self.frame_6)
        self.label_31.setGeometry(QtCore.QRect(140, 300, 61, 21))
        self.label_31.setObjectName("label_31")
        self.lineEdit_31 = QtWidgets.QLineEdit(self.frame_6)
        self.lineEdit_31.setGeometry(QtCore.QRect(210, 300, 113, 21))
        self.lineEdit_31.setText("")
        self.lineEdit_31.setObjectName("lineEdit_31")
        self.label_32 = QtWidgets.QLabel(self.frame_6)
        self.label_32.setGeometry(QtCore.QRect(120, 350, 91, 21))
        self.label_32.setObjectName("label_32")
        self.lineEdit_32 = QtWidgets.QLineEdit(self.frame_6)
        self.lineEdit_32.setGeometry(QtCore.QRect(210, 350, 113, 21))
        self.lineEdit_32.setText("")
        self.lineEdit_32.setObjectName("lineEdit_32")
        self.pushButton_15 = QtWidgets.QPushButton(self.frame_6)
        self.pushButton_15.setGeometry(QtCore.QRect(240, 440, 113, 32))
        self.pushButton_15.setObjectName("pushButton_15")
        self.pushButton_15.clicked.connect(self.showpurchase)

        self.frame_6.hide()

        # frame_7 emp -details

        self.frame_7 = QtWidgets.QFrame(MainWindow)
        self.frame_7.setGeometry(QtCore.QRect(0, 100, 1085, 731))
        self.frame_7.setStyleSheet("background-color: rgb(255, 153, 255);")
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame")

        self.label_img = QtWidgets.QLabel(self.frame_7)
        self.label_img.setGeometry(QtCore.QRect(556, 0, 825, 595))
        pixmap = QPixmap("Samsung-Mobile-Phone-PNG-HD.png")
        self.label_img.setPixmap(pixmap)

        self.label_33 = QtWidgets.QLabel(self.frame_7)
        self.label_33.setGeometry(QtCore.QRect(119, 50, 81, 20))
        self.label_33.setObjectName("label_33")
        self.lineEdit_33 = QtWidgets.QLineEdit(self.frame_7)
        self.lineEdit_33.setGeometry(QtCore.QRect(210, 50, 113, 21))
        self.lineEdit_33.setText("")
        self.lineEdit_33.setObjectName("lineEdit_33")

        self.label_34 = QtWidgets.QLabel(self.frame_7)
        self.label_34.setGeometry(QtCore.QRect(120, 100, 81, 21))
        self.label_34.setObjectName("label_34")
        self.lineEdit_34 = QtWidgets.QLineEdit(self.frame_7)
        self.lineEdit_34.setGeometry(QtCore.QRect(210, 100, 113, 21))
        self.lineEdit_34.setText("")
        self.lineEdit_34.setObjectName("lineEdit_34")

        self.label_35 = QtWidgets.QLabel(self.frame_7)
        self.label_35.setGeometry(QtCore.QRect(160, 150, 41, 21))
        self.label_35.setObjectName("label_35")
        self.lineEdit_35 = QtWidgets.QLineEdit(self.frame_7)
        self.lineEdit_35.setGeometry(QtCore.QRect(210, 150, 113, 21))
        self.lineEdit_35.setText("")
        self.lineEdit_35.setObjectName("lineEdit_35")

        self.label_36 = QtWidgets.QLabel(self.frame_7)
        self.label_36.setGeometry(QtCore.QRect(120, 200, 81, 21))
        self.label_36.setObjectName("label_36")
        self.lineEdit_36 = QtWidgets.QLineEdit(self.frame_7)
        self.lineEdit_36.setGeometry(QtCore.QRect(210, 200, 113, 21))
        self.lineEdit_36.setText("")
        self.lineEdit_36.setObjectName("lineEdit_36")

        # self.label_37 = QtWidgets.QLabel(self.frame_7)
        # self.label_37.setGeometry(QtCore.QRect(120, 250, 91, 21))
        # self.label_37.setObjectName("label_37")
        # self.lineEdit_37 = QtWidgets.QLineEdit(self.frame_7)
        # self.lineEdit_37.setGeometry(QtCore.QRect(210, 250, 113, 21))
        # self.lineEdit_37.setText("")
        # self.lineEdit_37.setObjectName("lineEdit_37")


        self.label_38 = QtWidgets.QLabel(self.frame_7)
        self.label_38.setGeometry(QtCore.QRect(160, 300, 41, 16))
        self.label_38.setObjectName("label_38")
        self.lineEdit_38 = QtWidgets.QLineEdit(self.frame_7)
        self.lineEdit_38.setGeometry(QtCore.QRect(210, 300, 113, 21))
        self.lineEdit_38.setText("")
        self.lineEdit_38.setObjectName("lineEdit_38")





        self.label_39 = QtWidgets.QLabel(self.frame_7)
        self.label_39.setGeometry(QtCore.QRect(170, 350, 31, 21))
        self.label_39.setObjectName("label_39")
        self.lineEdit_39 = QtWidgets.QLineEdit(self.frame_7)
        self.lineEdit_39.setGeometry(QtCore.QRect(210, 350, 113, 21))
        self.lineEdit_39.setText("")
        self.lineEdit_39.setObjectName("lineEdit_39")

        self.label_40 = QtWidgets.QLabel(self.frame_7)
        self.label_40.setGeometry(QtCore.QRect(150, 400, 61, 21))
        self.label_40.setObjectName("label_40")
        self.lineEdit_40 = QtWidgets.QLineEdit(self.frame_7)
        self.lineEdit_40.setGeometry(QtCore.QRect(210, 400, 113, 21))
        self.lineEdit_40.setText("")
        self.lineEdit_40.setObjectName("lineEdit_40")



        self.pushButton_16 = QtWidgets.QPushButton(self.frame_7)
        self.pushButton_16.setGeometry(QtCore.QRect(480, 140, 113, 32))
        self.pushButton_16.setObjectName("pushButton_16")
        self.pushButton_16.clicked.connect(self.addemployee)

        self.pushButton_17 = QtWidgets.QPushButton(self.frame_7)
        self.pushButton_17.setGeometry(QtCore.QRect(480, 200, 113, 32))
        self.pushButton_17.setObjectName("pushButton_17")
        self.pushButton_17.clicked.connect(self.showsemployee)

        self.pushButton_18 = QtWidgets.QPushButton(self.frame_7)
        self.pushButton_18.setGeometry(QtCore.QRect(480, 260, 113, 32))
        self.pushButton_18.setObjectName("pushButton_18")
        self.pushButton_18.clicked.connect(self.deleteemployee)

        self.pushButton_19 = QtWidgets.QPushButton(self.frame_7)
        self.pushButton_19.setGeometry(QtCore.QRect(480, 320, 113, 32))
        self.pushButton_19.setObjectName("pushButton_19")
        self.pushButton_19.clicked.connect(self.updateemployee)

        self.frame_7.hide()

        # frame_8 daily -add expense

        self.frame_8 = QtWidgets.QFrame(MainWindow)
        self.frame_8.setGeometry(QtCore.QRect(0, 100, 1085, 731))
        self.frame_8.setStyleSheet("background-color: rgb(255, 153, 255);")
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame")

        self.label_img = QtWidgets.QLabel(self.frame_8)
        self.label_img.setGeometry(QtCore.QRect(556, 0, 825, 595))
        pixmap = QPixmap("Samsung-Mobile-Phone-PNG-HD.png")
        self.label_img.setPixmap(pixmap)

        self.label_42 = QtWidgets.QLabel(self.frame_8)
        self.label_42.setGeometry(QtCore.QRect(350, 160, 41, 20))
        self.label_42.setObjectName("label_42")
        self.lineEdit_42 = QtWidgets.QLineEdit(self.frame_8)
        self.lineEdit_42.setGeometry(QtCore.QRect(400, 160, 113, 21))
        self.lineEdit_42.setText("")
        self.lineEdit_42.setObjectName("lineEdit_42")
        self.label_43 = QtWidgets.QLabel(self.frame_8)
        self.label_43.setGeometry(QtCore.QRect(340, 220, 51, 21))
        self.label_43.setObjectName("label_43")
        self.lineEdit_43 = QtWidgets.QLineEdit(self.frame_8)
        self.lineEdit_43.setGeometry(QtCore.QRect(400, 220, 113, 21))
        self.lineEdit_43.setText("")
        self.lineEdit_43.setObjectName("lineEdit_43")
        self.label_44 = QtWidgets.QLabel(self.frame_8)
        self.label_44.setGeometry(QtCore.QRect(340, 270, 51, 21))
        self.label_44.setObjectName("label_44")
        self.lineEdit_44 = QtWidgets.QLineEdit(self.frame_8)
        self.lineEdit_44.setGeometry(QtCore.QRect(400, 270, 113, 21))
        self.lineEdit_44.setText("")
        self.lineEdit_44.setObjectName("lineEdit_44")
        self.pushButton_20 = QtWidgets.QPushButton(self.frame_8)
        self.pushButton_20.setGeometry(QtCore.QRect(290, 360, 113, 32))
        self.pushButton_20.setObjectName("pushButton_20")
        self.pushButton_20.clicked.connect(self.adddailyexpense)

        self.pushButton_21 = QtWidgets.QPushButton(self.frame_8)
        self.pushButton_21.setGeometry(QtCore.QRect(410, 360, 113, 32))
        self.pushButton_21.setObjectName("pushButton_21")

        self.frame_8.hide()

        # frame_9 login -change password

        self.frame_9 = QtWidgets.QFrame(MainWindow)
        self.frame_9.setGeometry(QtCore.QRect(0, 100, 1085, 731))
        self.frame_9.setStyleSheet("background-color: rgb(255, 153, 255);")
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame")

        self.label_img = QtWidgets.QLabel(self.frame_9)
        self.label_img.setGeometry(QtCore.QRect(556, 0, 825, 595))
        pixmap = QPixmap("Samsung-Mobile-Phone-PNG-HD.png")
        self.label_img.setPixmap(pixmap)

        self.label_45 = QtWidgets.QLabel(self.frame_9)
        self.label_45.setGeometry(QtCore.QRect(320, 160, 71, 20))
        self.label_45.setObjectName("label_45")
        self.lineEdit_45 = QtWidgets.QLineEdit(self.frame_9)
        self.lineEdit_45.setGeometry(QtCore.QRect(400, 160, 113, 21))
        self.lineEdit_45.setText("")
        self.lineEdit_45.setObjectName("lineEdit_45")
        self.label_46 = QtWidgets.QLabel(self.frame_9)
        self.label_46.setGeometry(QtCore.QRect(300, 220, 91, 21))
        self.label_46.setObjectName("label_46")
        self.lineEdit_46 = QtWidgets.QLineEdit(self.frame_9)
        self.lineEdit_46.setGeometry(QtCore.QRect(400, 220, 113, 21))
        self.lineEdit_46.setText("")
        self.lineEdit_46.setObjectName("lineEdit_46")
        self.label_47 = QtWidgets.QLabel(self.frame_9)
        self.label_47.setGeometry(QtCore.QRect(290, 270, 101, 21))
        self.label_47.setObjectName("label_47")
        self.lineEdit_47 = QtWidgets.QLineEdit(self.frame_9)
        self.lineEdit_47.setGeometry(QtCore.QRect(400, 270, 113, 21))
        self.lineEdit_47.setText("")
        self.lineEdit_47.setObjectName("lineEdit_47")
        self.pushButton_22 = QtWidgets.QPushButton(self.frame_9)
        self.pushButton_22.setGeometry(QtCore.QRect(400, 350, 113, 32))
        self.pushButton_22.setObjectName("pushButton_22")
        self.pushButton_22.clicked.connect(self.loginchange)

        self.frame_9.hide()


        #frame_10 stock -item master
        self.frame_10 = QtWidgets.QFrame(MainWindow)
        self.frame_10.setGeometry(QtCore.QRect(0, 100, 1085, 731))
        self.frame_10.setStyleSheet("background-color: rgb(249, 249, 249);")
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame")

        self.label_img = QtWidgets.QLabel(self.frame_10)
        self.label_img.setGeometry(QtCore.QRect(556, 0, 825, 595))
        pixmap = QPixmap("620x620,5.png")
        self.label_img.setPixmap(pixmap)


        # self.tableView = QtWidgets.QTableView(self.frame_10)
        # self.tableView.setGeometry(QtCore.QRect(155, 120, 451, 381))
        # self.tableView.setObjectName("tableView")
        # self.tableView.resize(500, 500)
        # self.tableView.setStyleSheet("background-color: rgb(204, 255, 255);")

        self.tableWidget = QTableWidget(self.frame_10)
        self.tableWidget.setRowCount(7)
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setItem(0, 0, QTableWidgetItem("Cell (1,1)"))
        self.tableWidget.setItem(0, 1, QTableWidgetItem("Cell (1,2)"))
        self.tableWidget.setItem(0, 2, QTableWidgetItem("Cell (1,3)"))
        self.tableWidget.setItem(0, 3, QTableWidgetItem("Cell (1,4)"))
        self.tableWidget.setItem(0, 4, QTableWidgetItem("Cell (1,5)"))

        # self.tableWidget.setItem(1, 0, QTableWidgetItem("Cell (2,1)"))
        # self.tableWidget.setItem(1, 1, QTableWidgetItem("Cell (2,2)"))
        # self.tableWidget.setItem(1, 2, QTableWidgetItem("Cell (2,3)"))
        # self.tableWidget.setItem(1, 3, QTableWidgetItem("Cell (2,4)"))
        # self.tableWidget.setItem(1, 4, QTableWidgetItem("Cell (2,5)"))

        # self.tableWidget.setItem(2, 0, QTableWidgetItem("Cell (3,1)"))
        # self.tableWidget.setItem(2, 1, QTableWidgetItem("Cell (3,2)"))
        # self.tableWidget.setItem(2, 2, QTableWidgetItem("Cell (3,3)"))
        # self.tableWidget.setItem(2, 3, QTableWidgetItem("Cell (3,4)"))
        # self.tableWidget.setItem(2, 4, QTableWidgetItem("Cell (3,5)"))

        # self.tableWidget.setItem(3, 0, QTableWidgetItem("Cell (4,1)"))
        # self.tableWidget.setItem(3, 1, QTableWidgetItem("Cell (4,2)"))
        # self.tableWidget.setItem(3, 2, QTableWidgetItem("Cell (4,3)"))
        # self.tableWidget.setItem(3, 3, QTableWidgetItem("Cell (4,4)"))
        # self.tableWidget.setItem(3, 4, QTableWidgetItem("Cell (4,5)"))
        #
        # self.tableWidget.setItem(4, 0, QTableWidgetItem("Cell (5,1)"))
        # self.tableWidget.setItem(4, 1, QTableWidgetItem("Cell (5,2)"))
        # self.tableWidget.setItem(4, 2, QTableWidgetItem("Cell (5,3)"))
        # self.tableWidget.setItem(4, 3, QTableWidgetItem("Cell (5,4)"))
        # self.tableWidget.setItem(4, 4, QTableWidgetItem("Cell (5,5)"))
        #
        #
        # self.tableWidget.setItem(5, 0, QTableWidgetItem("Cell (6,1)"))
        # self.tableWidget.setItem(5, 1, QTableWidgetItem("Cell (6,2)"))
        # self.tableWidget.setItem(5, 2, QTableWidgetItem("Cell (6,3)"))
        # self.tableWidget.setItem(5, 3, QTableWidgetItem("Cell (6,4)"))
        # self.tableWidget.setItem(5, 4, QTableWidgetItem("Cell (6,5)"))
        #
        #
        #
        # self.tableWidget.setItem(6, 0, QTableWidgetItem("Cell (7,1)"))
        # self.tableWidget.setItem(6, 1, QTableWidgetItem("Cell (7,2)"))
        # self.tableWidget.setItem(6, 2, QTableWidgetItem("Cell (7,3)"))
        # self.tableWidget.setItem(6, 3, QTableWidgetItem("Cell (7,4)"))
        # self.tableWidget.setItem(6, 4, QTableWidgetItem("Cell (7,5)"))
        self.tableWidget.resize(600,400)



        self.tableWidget.setStyleSheet("background-color: rgb(204, 255, 255);")
        self.tableWidget.move(0, 0)

        self.pushButton_23 = QtWidgets.QPushButton(self.frame_10)
        self.pushButton_23.setGeometry(QtCore.QRect(400, 50, 113, 32))
        self.pushButton_23.setObjectName("pushButton_23")
        self.pushButton_23.clicked.connect(self.stockmaster)
        self.pushButton_23.resize(200, 100)




        self.frame_10.hide()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "MOBILE STORE MANAGEMENT"))
        self.menuITEM_MASTER.setTitle(_translate("MainWindow", "ITEM MASTER"))
        self.menuSALES_MASTER.setTitle(_translate("MainWindow", "SALES MASTER"))
        self.menuPURCHASE_MASTER.setTitle(_translate("MainWindow", "PURCHASE MASTER"))
        self.menuEMP_DETAILS.setTitle(_translate("MainWindow", "EMP DETAILS"))
        self.menuDAILY_EXPENSE.setTitle(_translate("MainWindow", "DAILY EXPENSE"))
        self.menuREPORTS.setTitle(_translate("MainWindow", "REPORTS"))
        self.menuLOGIN.setTitle(_translate("MainWindow", "LOGIN"))

        self.actionAdd_New_Item.setText(_translate("MainWindow", "Add New Item"))

        self.actionAdd_New_Item.triggered.connect(self.showFrame1)

        self.actionEdit_Item.setText(_translate("MainWindow", "Edit Item"))

        self.actionEdit_Item.triggered.connect(self.showFrame2)

        self.actionDelete_Item.setText(_translate("MainWindow", "Delete Item"))
        self.actionDelete_Item.triggered.connect(self.showFrame3)

        self.actionExit.setText(_translate("MainWindow", "Exit"))

        self.actionAdd_Sales.setText(_translate("MainWindow", "Add Sales"))
        self.actionAdd_Sales.triggered.connect(self.showFrame4)
        self.actionDelete_Item_2.setText(_translate("MainWindow", "Delete Sales"))
        self.actionDelete_Item_2.triggered.connect(self.showFrame5)

        self.actionAdd_purchase_Order.setText(_translate("MainWindow", "Purchase Order"))
        self.actionAdd_purchase_Order.triggered.connect(self.showFrame6)

        self.actionAdd_Emp_Details.setText(_translate("MainWindow", "Add Emp Details"))
        self.actionAdd_Emp_Details.triggered.connect(self.showFrame7)

        self.actionAdd_daily_expense.setText(_translate("MainWindow", "Add Expense"))
        self.actionAdd_daily_expense.triggered.connect(self.showFrame8)


        self.actionStock_Report.setText(_translate("MainWindow", "Stock Report"))
        self.actionStock_Report.triggered.connect(self.showFrame10)


        self.actionSales_Report.setText(_translate("MainWindow", "Sales Report"))

        self.actionPurchase_Report.setText(_translate("MainWindow", "Purchase Report"))


        self.actionChange_Password.setText(_translate("MainWindow", "Change Password"))
        self.actionChange_Password.triggered.connect(self.showFrame9)
        # frame_1 item -add


        self.label_1.setText(_translate("MainWindow", "Serial no:"))
        self.label_2.setText(_translate("MainWindow", "Item Name:"))
        self.label_3.setText(_translate("MainWindow", "Color:"))
        self.label_4.setText(_translate("MainWindow", "Company Name:"))
        self.label_5.setText(_translate("MainWindow", "Price:"))
        self.pushButton.setText(_translate("MainWindow", "Add"))
        self.pushButton_2.setText(_translate("MainWindow", "Show all"))
        self.pushButton_3.setText(_translate("MainWindow", "Exit"))

        # frame_2 item -edit

        self.label_6.setText(_translate("MainWindow", "Serial no:"))
        self.label_7.setText(_translate("MainWindow", "Item Name:"))
        self.label_8.setText(_translate("MainWindow", "Color:"))
        self.label_9.setText(_translate("MainWindow", "Company Name:"))
        self.label_10.setText(_translate("MainWindow", "Price:"))
        self.pushButton_4.setText(_translate("MainWindow", "Update"))
        self.pushButton_5.setText(_translate("MainWindow", "Exit"))


          # frame_3 item -delete

        self.label_11.setText(_translate("Dialog", "Serial no:"))
        self.label_12.setText(_translate("Dialog", "Item Name:"))
        self.label_13.setText(_translate("Dialog", "Color:"))
        self.label_14.setText(_translate("Dialog", "Company Name:"))
        self.label_15.setText(_translate("Dialog", "Price:"))
        self.pushButton_6.setText(_translate("Dialog", "Delete"))
        self.pushButton_7.setText(_translate("Dialog", "Exit"))


        # frame_4 sales -add

        self.label_16.setText(_translate("MainWindow", "Model no:"))
        self.label_17.setText(_translate("MainWindow", "Customer name:"))
        self.label_18.setText(_translate("MainWindow", "Address:"))
        self.label_19.setText(_translate("MainWindow", "Company Name:"))
        self.label_20.setText(_translate("MainWindow", "Price:"))
        self.pushButton_8.setText(_translate("MainWindow", "Save"))
        self.pushButton_9.setText(_translate("MainWindow", "Exit"))
        self.pushButton_10.setText(_translate("MainWindow", "ShowAll"))

        # frame_5 sales -delete

        self.label_21.setText(_translate("Dialog", "Model no:"))
        self.label_22.setText(_translate("Dialog", "Customer name:"))
        self.label_23.setText(_translate("Dialog", "Address:"))
        self.label_24.setText(_translate("Dialog", "Company Name:"))
        self.label_25.setText(_translate("Dialog", "Price:"))
        self.pushButton_11.setText(_translate("Dialog", "Delete"))
        self.pushButton_12.setText(_translate("Dialog", "Exit"))

        # frame_6 purchase -order

        self.label_26.setText(_translate("Dialog", "Dealer name:"))
        self.label_27.setText(_translate("Dialog", "Model name:"))
        self.label_28.setText(_translate("Dialog", "Company name:"))
        self.label_29.setText(_translate("Dialog", "Description:"))
        self.label_30.setText(_translate("Dialog", "Price:"))
        self.pushButton_13.setText(_translate("Dialog", "Save"))
        self.pushButton_14.setText(_translate("Dialog", "Exit"))
        self.label_31.setText(_translate("Dialog", "Quantity:"))
        self.label_32.setText(_translate("Dialog", "Total amount:"))
        self.pushButton_15.setText(_translate("Dialog", "ShowAll"))

        # frame_7 emp -add details

        self.label_33.setText(_translate("Dialog", "Employee id:"))
        self.label_34.setText(_translate("Dialog", "Designation:"))
        self.label_35.setText(_translate("Dialog", "Salary:"))
        self.label_36.setText(_translate("Dialog", "Experience:"))

        # self.label_37.setText(_translate("Dialog", "Date of Birth:"))

        self.label_38.setText(_translate("Dialog", "Name:"))
        self.label_39.setText(_translate("Dialog", "Age:"))
        self.label_40.setText(_translate("Dialog", "Address:"))

        # self.label_41.setText(_translate("Dialog", "Gender:"))
        # self.radioButton_1.setText(_translate("Dialog", "Male"))
        # self.radioButton_2.setText(_translate("Dialog", "Female")
        # )

        self.pushButton_16.setText(_translate("Dialog", "Save"))
        self.pushButton_17.setText(_translate("Dialog", "ShowAll"))
        self.pushButton_18.setText(_translate("Dialog", "Delete"))
        self.pushButton_19.setText(_translate("Dialog", "Update"))

        # frame_8 daily -add expense

        self.label_42.setText(_translate("Dialog", "Date:"))
        self.label_43.setText(_translate("Dialog", "Amount:"))
        self.label_44.setText(_translate("Dialog", "Details:"))
        self.pushButton_20.setText(_translate("Dialog", "Save"))
        self.pushButton_21.setText(_translate("Dialog", "ShowAll"))




        # frame_9 login -change passwords

        self.label_45.setText(_translate("Dialog", "User Name:"))
        self.label_46.setText(_translate("Dialog", "Old Password:"))
        self.label_47.setText(_translate("Dialog", "New Password:"))
        self.pushButton_22.setText(_translate("Dialog", "Change"))


        #frame_10 stock -item master
        # self.QTableView(_translate("MainWindow", ""))
        self.pushButton_23.setText(_translate("Dialog", "SHOW ALL STOCK ITEMS"))




    def showFrame1(self):
        self.frame.show()
        self.frame_2.hide()
        self.frame_3.hide()
        self.frame_4.hide()
        self.frame_5.hide()
        self.frame_6.hide()
        self.frame_7.hide()
        self.frame_8.hide()
        self.frame_8.hide()
        self.frame_9.hide()
        self.frame_10.hide()

    def showFrame2(self):
        self.frame_2.show()
        self.frame.hide()
        self.frame_3.hide()
        self.frame_4.hide()
        self.frame_5.hide()
        self.frame_6.hide()
        self.frame_7.hide()
        self.frame_8.hide()
        self.frame_9.hide()
        self.frame_10.hide()

    def showFrame3(self):
        self.frame_3.show()
        self.frame.hide()
        self.frame_2.hide()
        self.frame_4.hide()
        self.frame_5.hide()
        self.frame_6.hide()
        self.frame_7.hide()
        self.frame_8.hide()
        self.frame_9.hide()
        self.frame_10.hide()

    def showFrame4(self):
        self.frame_4.show()
        self.frame.hide()
        self.frame_2.hide()
        self.frame_3.hide()
        self.frame_5.hide()
        self.frame_6.hide()
        self.frame_7.hide()
        self.frame_8.hide()
        self.frame_9.hide()
        self.frame_10.hide()

    def showFrame5(self):
        self.frame_5.show()
        self.frame.hide()
        self.frame_2.hide()
        self.frame_3.hide()
        self.frame_4.hide()
        self.frame_6.hide()
        self.frame_7.hide()
        self.frame_8.hide()
        self.frame_9.hide()
        self.frame_10.hide()

    def showFrame6(self):
        self.frame_6.show()
        self.frame.hide()
        self.frame_2.hide()
        self.frame_3.hide()
        self.frame_4.hide()
        self.frame_5.hide()
        self.frame_7.hide()
        self.frame_8.hide()
        self.frame_9.hide()
        self.frame_10.hide()


    def showFrame7(self):
        self.frame_7.show()
        self.frame.hide()
        self.frame_2.hide()
        self.frame_3.hide()
        self.frame_4.hide()
        self.frame_5.hide()
        self.frame_6.hide()
        self.frame_8.hide()
        self.frame_9.hide()
        self.frame_10.hide()


    def showFrame8(self):
        self.frame_8.show()
        self.frame.hide()
        self.frame_2.hide()
        self.frame_3.hide()
        self.frame_4.hide()
        self.frame_5.hide()
        self.frame_6.hide()
        self.frame_7.hide()
        self.frame_9.hide()
        self.frame_10.hide()

    def showFrame9(self):
        self.frame_9.show()
        self.frame.hide()
        self.frame_2.hide()
        self.frame_3.hide()
        self.frame_4.hide()
        self.frame_5.hide()
        self.frame_6.hide()
        self.frame_7.hide()
        self.frame_8.hide()
        self.frame_10.hide()

    def showFrame10(self):
        self.frame_10.show()
        self.frame.hide()
        self.frame_2.hide()
        self.frame_3.hide()
        self.frame_4.hide()
        self.frame_5.hide()
        self.frame_6.hide()
        self.frame_7.hide()
        self.frame_8.hide()
        self.frame_9.hide()
        # print("Executed...")

        cursor.execute("SELECT * FROM Additems")

        self.tableWidget.setRowCount(cursor.rowcount)

        for row, form in enumerate(cursor):
            for col, item in enumerate(form):
                self.tableWidget.setItem(row, col, QTableWidgetItem(str(item)))

        # for e,d in enumerate(cursor):
        #     print(e,d)

        # tempList = []
        #
        # for row,col in enumerate(cursor):
        #     for x in col:
        #         tempList.append(x)
        #         for y in tempList:
        #             self.tableWidget.setItem(row, len(col), QTableWidgetItem(str(y)))



    def exec_query(self):
        x = self.lineEdit_2.text()
        y = self.lineEdit_3.text()
        z = self.lineEdit_4.text()

        query = "INSERT INTO Additems VALUES (%s,%s,%s,%s,%s)"

        cursor.execute(query, (self.lineEdit_1.text(), x, y, z, self.lineEdit_5.text()))

        print(self.lineEdit_1.text(), str(self.lineEdit_2.text()), str(self.lineEdit_3.text()),
              str(self.lineEdit_4.text()), self.lineEdit_5.text())

    def delete(self):
        query = "DELETE FROM Additems WHERE Serial = %s"
        cursor.execute(query, (int(self.lineEdit_11.text())))

    def edit(self):
        query = "UPDATE Additems SET Serial = %s, ItemName= %s,Color= %s,CompanyName= %s,Price= %s  WHERE Serial = %s"

        cursor.execute(query, (int(self.lineEdit_6.text()),self.lineEdit_7.text(),
                               self.lineEdit_8.text(),self.lineEdit_9.text(),int(self.lineEdit_10.text()), int(self.lineEdit_6.text())))

    def addsales(self):
        x = self.lineEdit_17.text()
        y = self.lineEdit_18.text()
        z = self.lineEdit_19.text()

        query = "INSERT INTO Addsales VALUES (%s,%s,%s,%s,%s)"

        cursor.execute(query, (self.lineEdit_16.text(), x, y, z, self.lineEdit_20.text()))

        print(self.lineEdit_16.text(), str(self.lineEdit_17.text()), str(self.lineEdit_18.text()),
              str(self.lineEdit_19.text()), self.lineEdit_20.text())

    def deletesales(self):

        query = "DELETE FROM Addsales WHERE Modelno = %s"
        cursor.execute(query, (int(self.lineEdit_21.text())))

    def showsales(self):
        cursor.execute("SELECT * FROM Addsales")

        for row in cursor:
            print(row)

    def addpurchase(self):
        x = self.lineEdit_27.text()
        y = self.lineEdit_28.text()
        z = self.lineEdit_29.text()
        w = self.lineEdit_30.text()
        v = self.lineEdit_31.text()

        query = "INSERT INTO Addpurchase VALUES (%s,%s,%s,%s,%s,%s,%s)"

        cursor.execute(query, (self.lineEdit_26.text(), x, y, z, w, v, self.lineEdit_32.text()))

        print(str(self.lineEdit_26.text()),self.lineEdit_27.text(), str(self.lineEdit_28.text()),
              str(self.lineEdit_29.text()), self.lineEdit_30.text(), self.lineEdit_31.text(), self.lineEdit_32.text())

    def showpurchase(self):
        cursor.execute("SELECT * FROM Addpurchase")
        for row in cursor:
            print(row)


    def addemployee(self):
        x = self.lineEdit_34.text()
        y = self.lineEdit_35.text()
        z = self.lineEdit_36.text()
        w = self.lineEdit_38.text()
        v = self.lineEdit_39.text()

        query = "INSERT INTO Addemployee VALUES (%s,%s,%s,%s,%s,%s,%s)"

        cursor.execute(query, (self.lineEdit_33.text(), x, y, z, w, v, self.lineEdit_40.text()))

        print(self.lineEdit_33.text(), str(self.lineEdit_34.text()), str(self.lineEdit_35.text()),
              str(self.lineEdit_36.text()), str(self.lineEdit_38.text()), self.lineEdit_39.text(), str(self.lineEdit_40.text()))

    def showsemployee(self):
        cursor.execute("SELECT * FROM Addemployee")

        for row in cursor:
            print(row)


    def deleteemployee(self):
        query = "DELETE FROM Addemployee WHERE 	Employeeid = %s"
        cursor.execute(query, (int(self.lineEdit_33.text())))

    def updateemployee(self):
        query = "UPDATE Addemployee SET Employeeid = %s, Designation= %s,Salary= %s,Experience= %s,Name= %s,Age= %s,Address= %s  WHERE Employeeid = %s"
        cursor.execute(query, (int(self.lineEdit_33.text()), self.lineEdit_34.text(),
                               self.lineEdit_35.text(), self.lineEdit_36.text(), self.lineEdit_38.text(),
                               int(self.lineEdit_39.text()), self.lineEdit_40.text(),int(self.lineEdit_33.text())))

    def adddailyexpense(self):
        x = self.lineEdit_43.text()

        query = "INSERT INTO Adddailyexpense VALUES (%s,%s,%s)"

        cursor.execute(query, (self.lineEdit_42.text(), x, self.lineEdit_44.text()))

        print(self.lineEdit_42.text(), self.lineEdit_43.text(), str(self.lineEdit_44.text()))

    def loginchange(self):
        x = self.lineEdit_46.text()
        query = "INSERT INTO  Loginchange VALUES (%s,%s,%s)"

        cursor.execute(query, (self.lineEdit_45.text(), x, self.lineEdit_47.text()))

        print(str(self.lineEdit_45.text()), str(self.lineEdit_46.text()), str(self.lineEdit_47.text()))

    def stockmaster(self):
        cursor.execute("SELECT * FROM Additems")
        print("\n")
        for currentQTableWidgetItem in self.tableWidget.selectedItems():
            print(currentQTableWidgetItem.row(), currentQTableWidgetItem.column(), currentQTableWidgetItem.text())

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
