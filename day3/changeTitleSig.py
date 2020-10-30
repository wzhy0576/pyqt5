import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):

        super(MainWindow, self).__init__(*args, **kwargs)


        self.windowTitleChanged.connect(self.onWindowTitleChange)
        # 当遇到信号“windowTitleChanged”时自动call槽函数“self.onWindowTitleChange”
        self.setWindowTitle("My Awesome App")


        self.windowTitleChanged.connect(lambda x: self.my_custom_fn())
        self.setWindowTitle("test1")
        self.setWindowTitle("test2")

        # note : signal<-->slot 信号/槽 对其后所有符合条件的触发动作都生效

        label = QLabel("THIS IS AWESOME!!!")
        label.setAlignment(Qt.AlignCenter)

        self.setCentralWidget(label)




    # 打印窗口标题
    def onWindowTitleChange(self, s):
        print(s)

    # SLOT: This has default parameters and can be called without a value
    def my_custom_fn(self, a="HELLLO!", b=5):
        print(a, b)

    # 重写事件“右键单击窗口”的响应为“打印文本”
    def contextMenuEvent(self, event):
        print("Context menu event!")

        # 打印文本之后调用父类原本的响应方法
        super(MainWindow, self).contextMenuEvent(event)

    # 阻塞所有事件
    # def event(self, e):
        # e.accept()

    # def contextMenuEvent(self, event):
        # event.accept()
        # event.ignore()



app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()