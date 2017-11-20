# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'kbc_1.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
import pygame
import time

pygame.mixer.init()
bgMusic = pygame.mixer.Sound('sound_2.wav')
bgMusic.play(-1)

optionLock = pygame.mixer.Sound('optionLock.wav')

class Ui_MainWindow(QtWidgets.QMainWindow):
    options = [['Modi','Arvind','Yogi','Lalu'],
           ['Mumbai', 'Delhi', 'Lucknow', 'Goa'],
           ['Global Service Tax', 'Goods and Simple Tax', 'Goods and Services Tax', 'General Service Tax'],
           ['1000','200','50','400']]

    money = [1000,5000,10000,50000]

    answers = ['Modi','Delhi','Goods and Simple Tax',200,'Delhi']

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1181, 750)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1191, 741))
        self.frame.setStyleSheet("background-color: rgb(230, 230, 230);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.label_img = QtWidgets.QLabel(self.frame)
        self.label_img.setGeometry(QtCore.QRect(0, 0, 1191, 741))
        pixmap = QPixmap("kbc_.png")
        self.label_img.setPixmap(pixmap)

        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(80, 520, 231, 81))
        self.pushButton.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 0, 0);\n"
"border-radius: 20px;")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(900, 520, 231, 81))
        self.pushButton_2.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 0, 0);\n"
"border-radius: 20px;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(0, 0, 1191, 741))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setGeometry(QtCore.QRect(80, 230, 1051, 81))
        self.label.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_3.setGeometry(QtCore.QRect(90, 380, 211, 71))
        self.pushButton_3.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_4.setGeometry(QtCore.QRect(450, 380, 211, 71))
        self.pushButton_4.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_5.setGeometry(QtCore.QRect(90, 530, 211, 71))
        self.pushButton_5.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_6.setGeometry(QtCore.QRect(450, 530, 211, 71))
        self.pushButton_6.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";")
        self.pushButton_6.setObjectName("pushButton_6")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1181, 31))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.frame_2.hide()

        self.pushButton.clicked.connect(self.startGame)
        self.pushButton_2.clicked.connect(self.endGame)

        # self.pushButton_3.clicked.connect(self.selectAns)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Start Game"))
        self.pushButton_2.setText(_translate("MainWindow", "Exit Game"))
        self.printQues()


    def startGame(self):
        self.frame_2.show()
        bgMusic.stop()

    def endGame(self):
        quit()

    def printQues(self):
        _translate = QtCore.QCoreApplication.translate
        with open('ques.txt') as file:
            qs = file.readlines()
            for j in range(4):
                for i in range(4):
                    # print(qs[i])
                    # print(self.options[i])
                    self.label.setText(_translate("MainWindow", qs[j]))
                    self.pushButton_3.setText(_translate("MainWindow", self.options[i][0]))
                    self.pushButton_4.setText(_translate("MainWindow", self.options[i][1]))
                    self.pushButton_5.setText(_translate("MainWindow", self.options[i][2]))
                    self.pushButton_6.setText(_translate("MainWindow", self.options[i][3]))
                    break

        self.buttons = [self.pushButton_3, self.pushButton_4, self.pushButton_5, self.pushButton_6]

        for i in range(len(self.buttons)):
            self.buttons[i].clicked.connect(self.selectAns)

    def selectAns(self):
        optionLock.play(0)
        print("Inside CheckAns")
        ans = self.sender()
        print("Ans is",ans.text())
        time.sleep(2)
        if ans.text() == "Modi":
            self.rightAns()
        else:
            self.wrongAns()

    def rightAns(self):
        choice = QtWidgets.QMessageBox.information(self,"Congrats","Congratulations You Won")
        self.printQues()

    def wrongAns(self):
        choice = QtWidgets.QMessageBox.question(self, "Quit", "Sorry, Wrong Ans, Play Again",
                                             QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)

        if choice == QtWidgets.QMessageBox.Yes:
            self.startGame()
        else:
            sys.exit()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
