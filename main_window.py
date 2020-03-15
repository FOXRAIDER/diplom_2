# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(320, 480)
        MainWindow.setMinimumSize(QtCore.QSize(320, 480))
        MainWindow.setMaximumSize(QtCore.QSize(320, 480))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 320, 480))
        self.label.setMinimumSize(QtCore.QSize(320, 480))
        self.label.setMaximumSize(QtCore.QSize(320, 480))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("background_2.jpg"))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 420, 320, 80))
        self.label_2.setMinimumSize(QtCore.QSize(320, 80))
        self.label_2.setMaximumSize(QtCore.QSize(320, 60))
        self.label_2.setStyleSheet("background-color: rgb(220, 220, 220);\n"
"border-style: solid;\n"
"border-width:1px;\n"
"border-radius: 15px;")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.compress = QtWidgets.QPushButton(self.centralwidget)
        self.compress.setGeometry(QtCore.QRect(0, 420, 80, 40))
        self.compress.setAutoFillBackground(False)
        self.compress.setStyleSheet("border-style: solid;\n"
"border-width: 2px;\n"
"")
        self.compress.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("close.png"), QtGui.QIcon.Active, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap("close.png"), QtGui.QIcon.Selected, QtGui.QIcon.Off)
        self.compress.setIcon(icon)
        self.compress.setIconSize(QtCore.QSize(48, 48))
        self.compress.setAutoRepeat(False)
        self.compress.setDefault(False)
        self.compress.setFlat(False)
        self.compress.setObjectName("compress")
        self.decompress = QtWidgets.QPushButton(self.centralwidget)
        self.decompress.setGeometry(QtCore.QRect(80, 420, 80, 40))
        self.decompress.setStyleSheet("border-style: solid;\n"
"border-width: 0px 1px 0px 1px;\n"
"border-color: #000;\n"
"")
        self.decompress.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("open.png"), QtGui.QIcon.Active, QtGui.QIcon.Off)
        self.decompress.setIcon(icon1)
        self.decompress.setIconSize(QtCore.QSize(48, 48))
        self.decompress.setObjectName("decompress")
        self.settings = QtWidgets.QPushButton(self.centralwidget)
        self.settings.setGeometry(QtCore.QRect(160, 420, 80, 40))
        self.settings.setStyleSheet("border-style: solid;\n"
"border-width: 2px;\n"
"")
        self.settings.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("settings.png"), QtGui.QIcon.Active, QtGui.QIcon.Off)
        self.settings.setIcon(icon2)
        self.settings.setIconSize(QtCore.QSize(42, 42))
        self.settings.setObjectName("settings")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(240, 420, 80, 40))
        self.pushButton_4.setStyleSheet("border-style: solid;\n"
"border-width: 0px 0px 0px 1px;\n"
"border-color: black;\n"
"")
        self.pushButton_4.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("about.png"), QtGui.QIcon.Active, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon3)
        self.pushButton_4.setIconSize(QtCore.QSize(42, 42))
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(0, 460, 80, 20))
        self.label_3.setTextFormat(QtCore.Qt.PlainText)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(80, 460, 80, 20))
        self.label_4.setStyleSheet("border-style: solid;\n"
"border-width: 0px 1px 0px 1px;\n"
"border-color:black;")
        self.label_4.setTextFormat(QtCore.Qt.RichText)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(160, 460, 80, 20))
        self.label_5.setTextFormat(QtCore.Qt.RichText)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(240, 460, 80, 20))
        self.label_6.setStyleSheet("border-style: solid;\n"
"border-color: black;\n"
"border-width: 0px 0px 0px 1px;")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(65, 90, 200, 50))
        self.label_7.setStyleSheet("font-size: 48px;\n"
"color: rgb(225,225,225);\n"
"font-family: Сomic Sans MS;")
        self.label_7.setTextFormat(QtCore.Qt.PlainText)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(40, 330, 240, 30))
        self.label_8.setStyleSheet("font-size:12px;\n"
"color: white;")
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "Архивировать"))
        self.label_4.setText(_translate("MainWindow", "Распаковать"))
        self.label_5.setText(_translate("MainWindow", "Настройки"))
        self.label_6.setText(_translate("MainWindow", "О программе"))
        self.label_7.setText(_translate("MainWindow", "Начнем?"))
