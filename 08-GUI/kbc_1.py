# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'kbc_1.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(QtWidgets.QMainWindow):
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
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(80, 520, 231, 81))
        self.pushButton.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 0, 0);\n"
"border-radius: 20px;")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(800, 520, 231, 81))
        self.pushButton_2.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 0, 0);\n"
"border-radius: 20px;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(0, 0, 1191, 691))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setGeometry(QtCore.QRect(80, 230, 751, 81))
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

        self.pushButton_3.clicked.connect(self.checkAns)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Start Game"))
        self.pushButton_2.setText(_translate("MainWindow", "Exit Game"))
        self.label.setText(_translate("MainWindow", "Who is the Prime Minister of India ?"))
        self.pushButton_3.setText(_translate("MainWindow", "Modi"))
        self.pushButton_4.setText(_translate("MainWindow", "Yogi"))
        self.pushButton_5.setText(_translate("MainWindow", "Rahul"))
        self.pushButton_6.setText(_translate("MainWindow", "Arvind"))

        self.buttons = [self.pushButton_3, self.pushButton_4, self.pushButton_5, self.pushButton_6]

        # for i in range(len(self.buttons)):
        #     self.buttons[i].clicked.connect(self.checkAns)


    def startGame(self):
        self.frame_2.show()

    def endGame(self):
        quit()

    def checkAns(self):
        print("Inside CheckAns")
        ans = self.sender()
        print("Ans is",ans.text())

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

