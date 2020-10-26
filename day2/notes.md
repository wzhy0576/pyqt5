# PyQt、PySide、PySide2这三者到底有什么区别？
https://blog.csdn.net/luoyayun361/article/details/99281515
https://www.learnpyqt.com/blog/pyqt5-vs-pyside2/

# document 
pyside2 : https://doc.qt.io/qtforpython/tutorials/index.html
pyqt5 : https://www.learnpyqt.com/
        http://zetcode.com/gui/pyqt5/
        https://build-system.fman.io/pyqt5-tutorial
        https://pythonspot.com/pyqt5/

# PyQt5 和 PySide2 兼容
import sys

if 'PyQt5' in sys.modules:
    from PyQt5 import QtGui, QtWidgets, QtCore
    from PyQt5.QtCore import pyqtSignal as Signal, pyqtSlot as Slot

else:
    from PySide2 import QtGui, QtWidgets, QtCore
    from PySide2.QtCore import Signal, Slot

# some examples
https://maicss.gitbooks.io/pyqt5/content/hello_world.html