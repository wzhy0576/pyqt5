# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from pictures import *

# Press the green button in the gutter to run the script.

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    # ui.label.setVisible(False)
    # ui.textEdit.setEnabled(False)
    MainWindow.show()
    sys.exit(app.exec_())
