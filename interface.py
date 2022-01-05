'''
This file uses PyQt5 to create an interface to get and display the coefficients, using text entry boxes and buttons.
'''


import sys
import PyQt5
from PyQt5 import QtGui
from PyQt5.QtWidgets import *

class MainWindow(QMainWindow):
    def __init__(self, parent = None):
        super().__init__(parent)

        self.setWindowTitle("Clepsh-Gordan Coefficient finder")
        self.setFixedSize(400, 300)
        self.setWindowIcon(QtGui.QIcon("icon.png"))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


