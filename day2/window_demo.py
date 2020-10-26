# This is a sample window demo implements by python code

import sys
from PyQt5.QtWidgets import *


app = QApplication(sys.argv)
window = QWidget()   #获取窗口对象
window.resize(500, 500)  #窗口大小
#window.move(300, 300)  #窗口位置
#窗口居中
screen = QDesktopWidget().screenGeometry()
size = window.geometry()
window.move(int((screen.width() - size.width()) / 2), int((screen.height() - size.height()) / 2))

window.setWindowTitle('window demo')  #窗口标题
window.show() #窗口显示
sys.exit(app.exec_())
