# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'beijing10shunkong.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_beijing10dialog(object):
    def setupUi(self, beijing10dialog):
        beijing10dialog.setObjectName("beijing10dialog")
        beijing10dialog.resize(717, 305)
        self.label = QtWidgets.QLabel(beijing10dialog)
        self.label.setGeometry(QtCore.QRect(50, 60, 71, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(beijing10dialog)
        self.label_2.setGeometry(QtCore.QRect(50, 140, 71, 31))
        self.label_2.setObjectName("label_2")
        self.shiliming = QtWidgets.QTextEdit(beijing10dialog)
        self.shiliming.setGeometry(QtCore.QRect(130, 60, 511, 31))
        self.shiliming.setObjectName("shiliming")
        self.danyuan = QtWidgets.QTextEdit(beijing10dialog)
        self.danyuan.setGeometry(QtCore.QRect(130, 140, 511, 31))
        self.danyuan.setObjectName("danyuan")
        self.zhixing = QtWidgets.QPushButton(beijing10dialog)
        self.zhixing.setGeometry(QtCore.QRect(460, 220, 75, 23))
        self.zhixing.setObjectName("zhixing")
        self.bei10jieshu = QtWidgets.QPushButton(beijing10dialog)
        self.bei10jieshu.setGeometry(QtCore.QRect(560, 220, 75, 23))
        self.bei10jieshu.setObjectName("bei10jieshu")

        self.retranslateUi(beijing10dialog)
        QtCore.QMetaObject.connectSlotsByName(beijing10dialog)

    def retranslateUi(self, beijing10dialog):
        _translate = QtCore.QCoreApplication.translate
        beijing10dialog.setWindowTitle(_translate("beijing10dialog", "北京10号线顺控"))
        self.label.setText(_translate("beijing10dialog", "顺控实例名：\n"
"以逗号分割"))
        self.label_2.setText(_translate("beijing10dialog", "数据库单元：\n"
"与实例名对应"))
        self.zhixing.setText(_translate("beijing10dialog", "执行"))
        self.bei10jieshu.setText(_translate("beijing10dialog", "结束"))