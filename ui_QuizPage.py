# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\zachk\OneDrive\Documents\College\Spring 2023\CIS4914\MusGator\QuizPage.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LearnPage(object):
    def setupUi(self, LearnPage):
        LearnPage.setObjectName("LearnPage")
        LearnPage.resize(849, 600)
        LearnPage.setMinimumSize(QtCore.QSize(800, 600))
        LearnPage.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.centralwidget = QtWidgets.QWidget(LearnPage)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.pageLayout = QtWidgets.QVBoxLayout()
        self.pageLayout.setContentsMargins(15, 15, 15, 15)
        self.pageLayout.setObjectName("pageLayout")
        self.buttonsLayout = QtWidgets.QHBoxLayout()
        self.buttonsLayout.setContentsMargins(0, 20, 0, 20)
        self.buttonsLayout.setSpacing(0)
        self.buttonsLayout.setObjectName("buttonsLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.buttonsLayout.addItem(spacerItem)
        self.learnButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.learnButton.sizePolicy().hasHeightForWidth())
        self.learnButton.setSizePolicy(sizePolicy)
        self.learnButton.setMinimumSize(QtCore.QSize(150, 40))
        self.learnButton.setMaximumSize(QtCore.QSize(300, 60))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.learnButton.setFont(font)
        self.learnButton.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 1px solid black;\n"
"border-radius: 15%;")
        self.learnButton.setObjectName("learnButton")
        self.buttonsLayout.addWidget(self.learnButton)
        spacerItem1 = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.buttonsLayout.addItem(spacerItem1)
        self.quizButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.quizButton.sizePolicy().hasHeightForWidth())
        self.quizButton.setSizePolicy(sizePolicy)
        self.quizButton.setMinimumSize(QtCore.QSize(150, 40))
        self.quizButton.setMaximumSize(QtCore.QSize(300, 60))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.quizButton.setFont(font)
        self.quizButton.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 1px solid black;\n"
"border-radius: 15%;")
        self.quizButton.setObjectName("quizButton")
        self.buttonsLayout.addWidget(self.quizButton)
        spacerItem2 = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.buttonsLayout.addItem(spacerItem2)
        self.progressButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progressButton.sizePolicy().hasHeightForWidth())
        self.progressButton.setSizePolicy(sizePolicy)
        self.progressButton.setMinimumSize(QtCore.QSize(150, 40))
        self.progressButton.setMaximumSize(QtCore.QSize(300, 60))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.progressButton.setFont(font)
        self.progressButton.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 1px solid black;\n"
"border-radius: 15%;")
        self.progressButton.setObjectName("progressButton")
        self.buttonsLayout.addWidget(self.progressButton)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.buttonsLayout.addItem(spacerItem3)
        self.buttonsLayout.setStretch(0, 1)
        self.buttonsLayout.setStretch(1, 1)
        self.buttonsLayout.setStretch(3, 1)
        self.buttonsLayout.setStretch(5, 1)
        self.buttonsLayout.setStretch(6, 1)
        self.pageLayout.addLayout(self.buttonsLayout)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(60)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pageLayout.addWidget(self.label)
        self.pageLayout.setStretch(0, 1)
        self.pageLayout.setStretch(1, 5)
        self.gridLayout.addLayout(self.pageLayout, 0, 0, 1, 1)
        LearnPage.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(LearnPage)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 849, 22))
        self.menubar.setObjectName("menubar")
        LearnPage.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(LearnPage)
        self.statusbar.setObjectName("statusbar")
        LearnPage.setStatusBar(self.statusbar)

        self.retranslateUi(LearnPage)
        QtCore.QMetaObject.connectSlotsByName(LearnPage)

    def retranslateUi(self, LearnPage):
        _translate = QtCore.QCoreApplication.translate
        LearnPage.setWindowTitle(_translate("LearnPage", "MusGator"))
        self.learnButton.setText(_translate("LearnPage", "Learn"))
        self.quizButton.setText(_translate("LearnPage", "Quiz"))
        self.progressButton.setText(_translate("LearnPage", "Progress"))
        self.label.setText(_translate("LearnPage", "Quiz Page"))
