import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5 import uic

form_class = uic.loadUiType("main_window.ui")[0]


class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


if __name__ == '__main__' :
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()


# 기본 폼 실행
# class MyApp(QWidget):
#
#     def __init__(self):
#         super().__init__()
#
#         self.initUI()
#
#     def initUI(self):
#
#         self.setWindowTitle('My First Application')
#         self.move(300, 300)
#         self.resize(400, 200)
#         self.show()
#
#
# if __name__ == '__main__':
#
#     app = QApplication(sys.argv)
#     ex = MyApp()
#     sys.exit(app.exec_())
