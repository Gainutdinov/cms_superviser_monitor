# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'shell_ui.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(541, 309)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 2, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setEnabled(False)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 2, 0, 1, 1)
        self.secWaiting = QtWidgets.QLCDNumber(self.centralwidget)
        self.secWaiting.setEnabled(False)
        self.secWaiting.setFrameShadow(QtWidgets.QFrame.Plain)
        self.secWaiting.setObjectName("secWaiting")
        self.gridLayout.addWidget(self.secWaiting, 1, 0, 1, 2)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton_2.clicked['bool'].connect(lambda: self.pushButton_2.setDisabled(True))
        self.pushButton_2.clicked['bool'].connect(lambda: self.pushButton.setEnabled(True))
        self.pushButton.clicked['bool'].connect(lambda: self.pushButton.setDisabled(True))
        self.pushButton.clicked['bool'].connect(lambda: self.pushButton_2.setEnabled(True))
        self.pushButton.clicked['bool'].connect(lambda: self.secWaiting.setDisabled(True))
        self.pushButton_2.clicked['bool'].connect(lambda: self.secWaiting.setEnabled(True))
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Interactive alert"))
        self.pushButton_2.setText(_translate("MainWindow", "Start watching attribute"))
        self.pushButton.setText(_translate("MainWindow", "Stop monitoring attribute"))

