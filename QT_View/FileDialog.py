from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_FileSel(object):
    def setupUi(self):
        self.fileDialog.setWindowTitle("标题")  # 设置对话框标题
        fileDialog.setFileMode(QFileDialog.AnyFile)  # 设置能打开文件的格式
        fileDialog.setDirectory(r'D:\01MyCode\01DemoCode\pyqt5_widgets\img')  # 设置默认打开路径
        fileDialog.setNameFilter("Images (*.png *.xpm *.jpg)")  # 按文件名过滤
        file_path = fileDialog.exec()  # 窗口显示，返回文件路径
        if file_path and fileDialog.selectedFiles():
            print("选择文件成功：{}".format(fileDialog.selectedFiles()[0]))