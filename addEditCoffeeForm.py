# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addEditCoffeeForm.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow2(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 500)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(14)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.info = QtWidgets.QLabel(self.centralwidget)
        self.info.setGeometry(QtCore.QRect(10, 0, 591, 41))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(15)
        self.info.setFont(font)
        self.info.setText("")
        self.info.setAlignment(QtCore.Qt.AlignCenter)
        self.info.setObjectName("info")
        self.save = QtWidgets.QPushButton(self.centralwidget)
        self.save.setGeometry(QtCore.QRect(225, 370, 150, 45))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(15)
        self.save.setFont(font)
        self.save.setStyleSheet("QPushButton {\n"
"background-color: white;border: 2px solid #B47747; border-radius: 8px;\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: Ton;border: 2px solid #B47747; border-radius: 8px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: BISQUE;border: 2px solid #B47747; border-radius: 8px;\n"
"}")
        self.save.setObjectName("save")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 50, 211, 41))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.title = QtWidgets.QTextEdit(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(220, 50, 361, 41))
        self.title.setStyleSheet("background-color: white;border: 2px solid BISQUE; border-radius: 8px;")
        self.title.setObjectName("title")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 100, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.roast = QtWidgets.QTextEdit(self.centralwidget)
        self.roast.setGeometry(QtCore.QRect(220, 100, 361, 41))
        self.roast.setStyleSheet("background-color: white;border: 2px solid BISQUE; border-radius: 8px;")
        self.roast.setObjectName("roast")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 150, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(15)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.ground = QtWidgets.QTextEdit(self.centralwidget)
        self.ground.setGeometry(QtCore.QRect(220, 150, 361, 41))
        self.ground.setStyleSheet("background-color: white;border: 2px solid BISQUE; border-radius: 8px;")
        self.ground.setObjectName("ground")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 200, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(15)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.taste = QtWidgets.QTextEdit(self.centralwidget)
        self.taste.setGeometry(QtCore.QRect(220, 200, 361, 41))
        self.taste.setStyleSheet("background-color: white;border: 2px solid BISQUE; border-radius: 8px;")
        self.taste.setObjectName("taste")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 250, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(15)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.price = QtWidgets.QTextEdit(self.centralwidget)
        self.price.setGeometry(QtCore.QRect(220, 250, 361, 41))
        self.price.setStyleSheet("background-color: white;border: 2px solid BISQUE; border-radius: 8px;")
        self.price.setObjectName("price")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(10, 300, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(15)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.volume = QtWidgets.QTextEdit(self.centralwidget)
        self.volume.setGeometry(QtCore.QRect(220, 300, 361, 41))
        self.volume.setStyleSheet("background-color: white;border: 2px solid BISQUE; border-radius: 8px;")
        self.volume.setObjectName("volume")
        self.info_2 = QtWidgets.QLabel(self.centralwidget)
        self.info_2.setGeometry(QtCore.QRect(0, 420, 591, 41))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(15)
        self.info_2.setFont(font)
        self.info_2.setText("")
        self.info_2.setAlignment(QtCore.Qt.AlignCenter)
        self.info_2.setObjectName("info_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.save.setText(_translate("MainWindow", "Сохранить"))
        self.label.setText(_translate("MainWindow", "Название сорта кофе:"))
        self.label_2.setText(_translate("MainWindow", "Степень обжарки:"))
        self.label_3.setText(_translate("MainWindow", "Молотый/в зернах:"))
        self.label_4.setText(_translate("MainWindow", "Описание вкуса:"))
        self.label_5.setText(_translate("MainWindow", "Цена:"))
        self.label_6.setText(_translate("MainWindow", "Объём упаковки:"))
