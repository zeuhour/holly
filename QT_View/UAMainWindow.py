# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'f:\UA_AutoTestTool\QT_View\UAMainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1008, 796)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 351, 121))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(90, 90, 151, 20))
        self.label_8.setObjectName("label_8")
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(30, 58, 54, 12))
        self.label_7.setObjectName("label_7")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(20, 18, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Algerian")
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.AIwrite = QtWidgets.QPushButton(self.frame)
        self.AIwrite.setGeometry(QtCore.QRect(260, 58, 75, 23))
        self.AIwrite.setObjectName("AIwrite")
        self.AInum = QtWidgets.QTextEdit(self.frame)
        self.AInum.setGeometry(QtCore.QRect(90, 48, 141, 31))
        self.AInum.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.AInum.setObjectName("AInum")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(370, 20, 501, 91))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_9 = QtWidgets.QLabel(self.frame_2)
        self.label_9.setGeometry(QtCore.QRect(290, 40, 16, 16))
        self.label_9.setObjectName("label_9")
        self.attr = QtWidgets.QTextEdit(self.frame_2)
        self.attr.setGeometry(QtCore.QRect(230, 30, 61, 31))
        self.attr.setObjectName("attr")
        self.value = QtWidgets.QTextEdit(self.frame_2)
        self.value.setGeometry(QtCore.QRect(310, 30, 61, 31))
        self.value.setObjectName("value")
        self.Node = QtWidgets.QTextEdit(self.frame_2)
        self.Node.setGeometry(QtCore.QRect(60, 20, 161, 71))
        self.Node.setObjectName("Node")
        self.label_10 = QtWidgets.QLabel(self.frame_2)
        self.label_10.setGeometry(QtCore.QRect(0, 0, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Algerian")
        font.setPointSize(11)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.write = QtWidgets.QPushButton(self.frame_2)
        self.write.setGeometry(QtCore.QRect(440, 30, 51, 31))
        self.write.setObjectName("write")
        self.read = QtWidgets.QPushButton(self.frame_2)
        self.read.setGeometry(QtCore.QRect(380, 30, 51, 31))
        self.read.setObjectName("read")
        self.label_11 = QtWidgets.QLabel(self.frame_2)
        self.label_11.setGeometry(QtCore.QRect(10, 40, 41, 16))
        self.label_11.setObjectName("label_11")
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(10, 130, 631, 131))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.Condition1 = QtWidgets.QTextEdit(self.frame_3)
        self.Condition1.setGeometry(QtCore.QRect(80, 80, 141, 31))
        self.Condition1.setObjectName("Condition1")
        self.label_2 = QtWidgets.QLabel(self.frame_3)
        self.label_2.setGeometry(QtCore.QRect(10, 0, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Algerian")
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.DIwrite = QtWidgets.QPushButton(self.frame_3)
        self.DIwrite.setGeometry(QtCore.QRect(550, 60, 75, 23))
        self.DIwrite.setObjectName("DIwrite")
        self.IOlist1 = QtWidgets.QComboBox(self.frame_3)
        self.IOlist1.setGeometry(QtCore.QRect(80, 31, 141, 31))
        self.IOlist1.setObjectName("IOlist1")
        self.label_3 = QtWidgets.QLabel(self.frame_3)
        self.label_3.setGeometry(QtCore.QRect(20, 40, 54, 12))
        self.label_3.setObjectName("label_3")
        self.IOlist2 = QtWidgets.QComboBox(self.frame_3)
        self.IOlist2.setGeometry(QtCore.QRect(240, 30, 141, 31))
        self.IOlist2.setObjectName("IOlist2")
        self.Waittime = QtWidgets.QTextEdit(self.frame_3)
        self.Waittime.setGeometry(QtCore.QRect(450, 80, 81, 31))
        self.Waittime.setObjectName("Waittime")
        self.label_4 = QtWidgets.QLabel(self.frame_3)
        self.label_4.setGeometry(QtCore.QRect(20, 90, 54, 12))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.frame_3)
        self.label_5.setGeometry(QtCore.QRect(400, 40, 54, 12))
        self.label_5.setObjectName("label_5")
        self.Condition2 = QtWidgets.QTextEdit(self.frame_3)
        self.Condition2.setGeometry(QtCore.QRect(240, 80, 141, 31))
        self.Condition2.setObjectName("Condition2")
        self.label_6 = QtWidgets.QLabel(self.frame_3)
        self.label_6.setGeometry(QtCore.QRect(390, 90, 54, 12))
        self.label_6.setObjectName("label_6")
        self.DInum = QtWidgets.QTextEdit(self.frame_3)
        self.DInum.setGeometry(QtCore.QRect(450, 30, 81, 31))
        self.DInum.setObjectName("DInum")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(890, 20, 81, 81))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_12 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Algerian")
        font.setPointSize(10)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.verticalLayout.addWidget(self.label_12)
        self.crsub = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.crsub.setObjectName("crsub")
        self.verticalLayout.addWidget(self.crsub)
        self.unsub = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.unsub.setObjectName("unsub")
        self.verticalLayout.addWidget(self.unsub)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 116, 1011, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(343, 0, 20, 121))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(870, 0, 16, 121))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(0, 250, 1011, 16))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(890, 140, 81, 91))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_13 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_2.addWidget(self.label_13)
        self.dbunitc = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.dbunitc.setObjectName("dbunitc")
        self.verticalLayout_2.addWidget(self.dbunitc)
        self.dbunitchange = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.dbunitchange.setObjectName("dbunitchange")
        self.verticalLayout_2.addWidget(self.dbunitchange)
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setGeometry(QtCore.QRect(630, 120, 20, 141))
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.baowen = QtWidgets.QTextEdit(self.centralwidget)
        self.baowen.setGeometry(QtCore.QRect(650, 140, 211, 71))
        self.baowen.setObjectName("baowen")
        self.line_6 = QtWidgets.QFrame(self.centralwidget)
        self.line_6.setGeometry(QtCore.QRect(863, 120, 31, 141))
        self.line_6.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.jiexi = QtWidgets.QPushButton(self.centralwidget)
        self.jiexi.setGeometry(QtCore.QRect(780, 220, 75, 23))
        self.jiexi.setObjectName("jiexi")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1008, 23))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        self.menu_3 = QtWidgets.QMenu(self.menubar)
        self.menu_3.setObjectName("menu_3")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.printdock = QtWidgets.QDockWidget(MainWindow)
        self.printdock.setStyleSheet("background-color: rgb(221, 221, 221);")
        self.printdock.setObjectName("printdock")
        self.dockWidgetContents_2 = QtWidgets.QWidget()
        self.dockWidgetContents_2.setObjectName("dockWidgetContents_2")
        self.gridLayout = QtWidgets.QGridLayout(self.dockWidgetContents_2)
        self.gridLayout.setObjectName("gridLayout")
        self.OutText = QtWidgets.QTextBrowser(self.dockWidgetContents_2)
        self.OutText.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.OutText.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.OutText.setObjectName("OutText")
        self.gridLayout.addWidget(self.OutText, 0, 0, 1, 1)
        self.printdock.setWidget(self.dockWidgetContents_2)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(8), self.printdock)
        self.Clientset = QtWidgets.QAction(MainWindow)
        self.Clientset.setObjectName("Clientset")
        self.IOlistset = QtWidgets.QAction(MainWindow)
        self.IOlistset.setObjectName("IOlistset")
        self.actionview = QtWidgets.QAction(MainWindow)
        self.actionview.setObjectName("actionview")
        self.beijing10 = QtWidgets.QAction(MainWindow)
        self.beijing10.setObjectName("beijing10")
        self.modeledit = QtWidgets.QAction(MainWindow)
        self.modeledit.setObjectName("modeledit")
        self.modelexec = QtWidgets.QAction(MainWindow)
        self.modelexec.setObjectName("modelexec")
        self.actionclear = QtWidgets.QAction(MainWindow)
        self.actionclear.setObjectName("actionclear")
        self.printdock.raise_()
        self.menu.addAction(self.Clientset)
        self.menu.addAction(self.IOlistset)
        self.menu_2.addAction(self.actionview)
        self.menu_2.addAction(self.actionclear)
        self.menu_3.addAction(self.beijing10)
        self.menu_3.addAction(self.modeledit)
        self.menu_3.addAction(self.modelexec)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "测试工具"))
        self.label_8.setText(_translate("MainWindow", "填写为固定值，不填写递增"))
        self.label_7.setText(_translate("MainWindow", "目标值："))
        self.label.setText(_translate("MainWindow", "AI写值："))
        self.AIwrite.setText(_translate("MainWindow", "确定"))
        self.AInum.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_9.setText(_translate("MainWindow", " ="))
        self.attr.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">PV</p></body></html>"))
        self.label_10.setText(_translate("MainWindow", "直接读写："))
        self.write.setText(_translate("MainWindow", "写"))
        self.read.setText(_translate("MainWindow", "读"))
        self.label_11.setText(_translate("MainWindow", "实例名："))
        self.label_2.setText(_translate("MainWindow", "DI写值："))
        self.DIwrite.setText(_translate("MainWindow", "确定"))
        self.label_3.setText(_translate("MainWindow", "点表列名："))
        self.Waittime.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "筛选条件："))
        self.label_5.setText(_translate("MainWindow", "目标值："))
        self.label_6.setText(_translate("MainWindow", "等待时间："))
        self.label_12.setText(_translate("MainWindow", "DO点监听："))
        self.crsub.setText(_translate("MainWindow", "监听"))
        self.unsub.setText(_translate("MainWindow", "取消"))
        self.label_13.setText(_translate("MainWindow", "数据库单元："))
        self.dbunitchange.setText(_translate("MainWindow", "确定"))
        self.jiexi.setText(_translate("MainWindow", "报文"))
        self.menu.setTitle(_translate("MainWindow", "文件"))
        self.menu_2.setTitle(_translate("MainWindow", "视图"))
        self.menu_3.setTitle(_translate("MainWindow", "自动返校"))
        self.printdock.setWindowTitle(_translate("MainWindow", "输出"))
        self.Clientset.setText(_translate("MainWindow", "服务器设置"))
        self.IOlistset.setText(_translate("MainWindow", "点表设置"))
        self.actionview.setText(_translate("MainWindow", "输出信息框"))
        self.beijing10.setText(_translate("MainWindow", "北京10顺控"))
        self.modeledit.setText(_translate("MainWindow", "模板编辑"))
        self.modelexec.setText(_translate("MainWindow", "模板执行"))
        self.actionclear.setText(_translate("MainWindow", "clear"))
