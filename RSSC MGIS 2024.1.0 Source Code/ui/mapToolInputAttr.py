# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mapToolInputAttr.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 268)
        Dialog.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.attrsLayout = QtWidgets.QVBoxLayout()
        self.attrsLayout.setObjectName("attrsLayout")
        self.verticalLayout.addLayout(self.attrsLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.add = QtWidgets.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setFamily("幼圆")
        self.add.setFont(font)
        self.add.setObjectName("add")
        self.horizontalLayout.addWidget(self.add)
        self.cancel = QtWidgets.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setFamily("幼圆")
        self.cancel.setFont(font)
        self.cancel.setObjectName("cancel")
        self.horizontalLayout.addWidget(self.cancel)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "属性编辑"))
        self.add.setText(_translate("Dialog", "确  认"))
        self.cancel.setText(_translate("Dialog", "取  消"))
