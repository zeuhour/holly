from PyQt5 import QtGui
from UA_Logic import Values, UAClient
from UA_Logic.Values import uaclient
from QT_View.UAMainWindow import Ui_MainWindow
from QT_View.IOlistDialog import Ui_IOlistinit
from QT_View.ClientDialog import Ui_Clientinit
from QT_View.beijing10shunkong import Ui_beijing10dialog
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QFileDialog
from PyQt5.QtGui import QTextCursor
from PyQt5.QtCore import QObject, pyqtSignal
from threading import Thread
from beijing10 import Logic, global_values

import os


class Stream(QObject):#输出流，打印至控件
    newText = pyqtSignal(str)
    def write(self, text):
        self.newText.emit(str(text))
        # 实时刷新界面
        QApplication.processEvents()

class ShowClientDlg(QDialog, Ui_Clientinit):#显示服务器设置窗体
    def __init__(self, parent=None):
        super(ShowClientDlg, self).__init__(parent)
        self.setupUi(self)
        self.Clientok.clicked.connect(self.clinit)
        self.ClientIP.setText(uaclient['ip'])
        self.Cunit.setText(uaclient['unit'])
        if uaclient['port'] != '':
            self.Clientport.setText(uaclient['port'])

    def clinit(self):
        Values.cl.goodcl = False
        if Values.cl.constatus:
            Values.cl.ClientDisconnect()
        uaclient['ip'] = self.ClientIP.text()
        uaclient['port'] = self.Clientport.text()
        uaclient['unit'] = self.Cunit.text()
        #UA创建服务器实例
        if(Values.cl.getclient(uaclient)):#初始化
            Values.cl.ClientConnect()
        if Values.cl.constatus:
            self.close()

class ShowIOlistDlg(QDialog, Ui_IOlistinit):#显示点表设置窗体
    def __init__(self, parent=None):
        super(ShowIOlistDlg, self).__init__(parent)
        self.setupUi(self)
        self.filesel.setCheckable(True)
        self.filesel.clicked.connect(lambda: self.click_find_file_path(self.filesel))#点击打开文件选择窗口
        self.IOlistok.accepted.connect(self.iolistinit)#确定按钮点击执行点表初始化

    def click_find_file_path(self, button):
        # 设置文件扩展名过滤，同一个类型的不同格式如xlsx和xls 用空格隔开
        filename, filetype = QFileDialog.getOpenFileName(self, "选择点表", "../",
                                                         "Excel Files (*.xls *.xlsx)")
        if button.text() == "..":
            if button.isChecked():
                self.excel_path = filename
                self.fileph.setText(filename)
                Values.filepath = filename
        button.toggle()

    def iolistinit(self):#调用UAClient方法
        try:
            Values.colnum = UAClient.getcolnm(self.excel_path)
        except Exception as e:
            print(e)
        if Values.filepath:
            self.close()

class showbeijing10dlg(QDialog, Ui_beijing10dialog):
    def __init__(self, parent=None):
        super(showbeijing10dlg, self).__init__(parent)
        self.setupUi(self)
        self.zhixing.clicked.connect(self.bj10soc)
        self.bei10jieshu.clicked.connect(self.endsoc)

    def bj10soc(self):
        Values.bcl.getclient(uaclient)  # 初始化
        Values.bcl.ClientConnect()
        global_values.socname = self.shiliming.toPlainText()
        global_values.dbunit = self.danyuan.toPlainText()
        soc = []
        unit = global_values.dbunit.replace(' ', '').split(',')  # 需赋值
        socname = global_values.socname.replace(' ', '').split(',')
        try:
            for i in range(len(unit)):
                soc.append(Logic.seqctrl())
                soc[i].unit_init(unit[i])
                soc[i].get_socnode(socname[i])
                soc[i].status_init()
                soc[i].seq_ctrl()
            Values.cl.rc_subnode()

        except Exception as e:
            print(e)
    def endsoc(self):
        try:
            Values.cl.unrcsub()
        except Exception as e:
            print(e)

class MainWindow(QMainWindow, Ui_MainWindow):#主窗体
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        sys.stdout = Stream(newText=self.onUpdateEdit)  # 输出流
        #主界面
        self.Clientset.triggered.connect(self.showClDlg)#菜单栏服务器设置响应事件
        self.IOlistset.setCheckable(True)
        self.IOlistset.triggered.connect(lambda : self.showIODlg(self.IOlistset))#菜单栏点表设置相应事件,lambda用于传递参数的函数
        self.AIwrite.clicked.connect(self.AIset)
        self.DIwrite.clicked.connect(self.DIset)
        self.read.clicked.connect(self.zread)
        self.write.clicked.connect(self.zwrite)
        self.crsub.clicked.connect(self.createsub)
        self.unsub.clicked.connect(self.unsubno)
        self.actionview.triggered.connect(self.printdock.show)
        self.dbunitchange.clicked.connect(self.changeunit)
        self.beijing10.triggered.connect(self.showb10soc)
        if not os.path.exists("./template"):
            os.mkdir("./template")
        t = Thread(target=Values.cl.keepalive)  # 服务连接守护线程，断开自动重连
        t.setDaemon(True)
        t.start()

    def createsub(self):
        try:
            t = Thread(target=UAClient.createallsub,args=(Values.cl,))
            t.start()
        except BaseException as e:
            print(e)

    def unsubno(self):
        try:
            t = Thread(target=Values.cl.unsub())
            t.start()
        except BaseException as e:
            print(e)

    def AIset(self):
        try:
            val = self.AInum.toPlainText()
            if val:
                UAClient.AIauto(Values.cl, val.strip())
            else:
                UAClient.AIauto(Values.cl, 'asc')
        except Exception as e:
            print(e)


    def DIset(self):
        cond = {}
        cna = self.IOlist1.currentText()
        val = self.Condition1.toPlainText()
        div = self.DInum.toPlainText()
        wit = self.Waittime.toPlainText()
        val2 = self.Condition2.toPlainText()

        if not wit:
            wit = 0
        cond[cna] = val
        if val2 != '':
            cond[self.IOlist2.currentText()] = val2
        try:
            t = Thread(target=UAClient.DIauto, args=(Values.cl, cond, div, wit,))
            t.start()
        except BaseException as e:
            print(e)

    def changeunit(self):
        Values.uaclient['unit'] = self.dbunitc.text()
        print('修改数据库单元：{}'.format(Values.uaclient['unit']))
        try:
            Values.cl.dbunit = self.dbunitc.text()
        except Exception as e:
            print(e)


    def zread(self):
        node = self.Node.toPlainText()
        att = self.attr.toPlainText()
        try:
            Values.cl.get_Value(node, att)
        except BaseException as e:
            print(e)

    def zwrite(self):
        node = self.Node.toPlainText()
        att = self.attr.toPlainText()
        val = self.value.toPlainText()
        try:
            if '.' in val:
                Values.cl.set_Value(node, att, float(val))
            else:
                Values.cl.set_Value(node, att, int(val))
        except BaseException as e:
            print(e)

    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        Values.winexit = False
        Values.cl.ClientDisconnect()
        Values.bcl.ClientDisconnect()
        # print('退出中......')
        # import time
        # time.sleep(1)
        # sys.exit(0)

    def showb10soc(self):
        dlg = showbeijing10dlg(self)
        dlg.exec_()

    def showClDlg(self):
        dlg = ShowClientDlg(self)
        dlg.exec_()
        self.dbunitc.setText(uaclient['unit'])

    def showIODlg(self, btn):
        dlg = ShowIOlistDlg(self)
        dlg.exec_()
        btn.toggle()
        if Values.colnum:#若关闭点表选择窗口后列码刷新成功，则添加至下拉列表
            self.IOlist1.clear()
            self.IOlist2.clear()
            self.IOlist1.addItems(Values.colnum.keys())
            self.IOlist2.addItems(Values.colnum.keys())

    def onUpdateEdit(self, text):
        cursor = self.OutText.textCursor()
        cursor.movePosition(QTextCursor.End)
        cursor.insertText(text)
        self.OutText.setTextCursor(cursor)
        self.OutText.ensureCursorVisible()


import sys
if __name__ == '__main__':
    app = QApplication(sys.argv)
    Main_ui = MainWindow()
    Main_ui.show()
    app.exec_()
