# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ndviUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ndviDialog(object):
    def setupUi(self, ndviDialog):
        ndviDialog.setObjectName("ndviDialog")
        ndviDialog.resize(577, 282)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/ico/NDVI.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ndviDialog.setWindowIcon(icon)
        ndviDialog.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label = QtWidgets.QLabel(ndviDialog)
        self.label.setGeometry(QtCore.QRect(30, 20, 81, 31))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.quit = QtWidgets.QPushButton(ndviDialog)
        self.quit.setGeometry(QtCore.QRect(470, 230, 71, 31))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        self.quit.setFont(font)
        self.quit.setObjectName("quit")
        self.txtRedband = QtWidgets.QTextEdit(ndviDialog)
        self.txtRedband.setGeometry(QtCore.QRect(110, 20, 321, 31))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        self.txtRedband.setFont(font)
        self.txtRedband.setObjectName("txtRedband")
        self.txtNirRed = QtWidgets.QTextEdit(ndviDialog)
        self.txtNirRed.setGeometry(QtCore.QRect(110, 90, 321, 31))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        self.txtNirRed.setFont(font)
        self.txtNirRed.setObjectName("txtNirRed")
        self.label_2 = QtWidgets.QLabel(ndviDialog)
        self.label_2.setGeometry(QtCore.QRect(30, 90, 71, 31))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(ndviDialog)
        self.label_3.setGeometry(QtCore.QRect(30, 160, 71, 31))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.txtPath = QtWidgets.QTextEdit(ndviDialog)
        self.txtPath.setGeometry(QtCore.QRect(110, 160, 321, 31))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        self.txtPath.setFont(font)
        self.txtPath.setObjectName("txtPath")
        self.ok = QtWidgets.QPushButton(ndviDialog)
        self.ok.setGeometry(QtCore.QRect(370, 230, 71, 31))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        self.ok.setFont(font)
        self.ok.setObjectName("ok")
        self.redOpen = QtWidgets.QPushButton(ndviDialog)
        self.redOpen.setGeometry(QtCore.QRect(460, 20, 81, 31))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        self.redOpen.setFont(font)
        self.redOpen.setObjectName("redOpen")
        self.nirredOpen = QtWidgets.QPushButton(ndviDialog)
        self.nirredOpen.setGeometry(QtCore.QRect(460, 90, 81, 31))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        self.nirredOpen.setFont(font)
        self.nirredOpen.setObjectName("nirredOpen")
        self.pathOpen = QtWidgets.QPushButton(ndviDialog)
        self.pathOpen.setGeometry(QtCore.QRect(460, 160, 81, 31))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        self.pathOpen.setFont(font)
        self.pathOpen.setObjectName("pathOpen")
        self.label_4 = QtWidgets.QLabel(ndviDialog)
        self.label_4.setGeometry(QtCore.QRect(110, 60, 431, 16))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(ndviDialog)
        self.label_5.setGeometry(QtCore.QRect(110, 130, 381, 16))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(ndviDialog)
        self.label_6.setGeometry(QtCore.QRect(110, 200, 451, 16))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")

        self.retranslateUi(ndviDialog)
        QtCore.QMetaObject.connectSlotsByName(ndviDialog)

    def retranslateUi(self, ndviDialog):
        _translate = QtCore.QCoreApplication.translate
        ndviDialog.setWindowTitle(_translate("ndviDialog", "计算NDVI"))
        self.label.setText(_translate("ndviDialog", "红波段："))
        self.quit.setText(_translate("ndviDialog", "关  闭"))
        self.label_2.setText(_translate("ndviDialog", "近红外波段："))
        self.label_3.setText(_translate("ndviDialog", "输出路径："))
        self.ok.setText(_translate("ndviDialog", "计算NDVI值"))
        self.redOpen.setText(_translate("ndviDialog", "打开红波段"))
        self.nirredOpen.setText(_translate("ndviDialog", "打开红外波段"))
        self.pathOpen.setText(_translate("ndviDialog", "选择目录"))
        self.label_4.setText(_translate("ndviDialog", "<html><head/><body><p>注意：请选择红波段的.tif格式文件，一般为band4文件。</p></body></html>"))
        self.label_5.setText(_translate("ndviDialog", "注意：请选择近红外波段的.tif格式文件，一般为band5文件。"))
        self.label_6.setText(_translate("ndviDialog", "注意：请选择计算NDVI数值后的影像输出路径，文件会以ndvi_result.tif后缀命名。"))
import ndRc_rc