'''
This file uses PyQt5 to create an interface to get and display the coefficients, using text entry boxes and buttons.
'''


import sys
import PyQt5
from PyQt5 import QtGui
from PyQt5.QtWidgets import *


from query import query

class MainWindow(QMainWindow):
    def __init__(self, parent = None):
        super().__init__(parent)

        self.setWindowTitle("Clepsh-Gordan Coefficient finder")
        self.setFixedSize(400, 100)
        self.setWindowIcon(QtGui.QIcon("icon.png"))
        self.generalLayout = QVBoxLayout()
        self._centralWidget = QWidget(self)
        self.setCentralWidget(self._centralWidget)
        self._centralWidget.setLayout(self.generalLayout)
        self._createTextbox()
        self._createResultLabel()
        self._createGetButton()

    def _createTextbox(self):
        self.textj1 = QLineEdit()
        self.textj2 = QLineEdit()
        self.textm1 = QLineEdit()
        self.textm2 = QLineEdit()
        self.textJ = QLineEdit()
        self.textM = QLineEdit()
        boxes = [self.textj1, self.textj2, self.textm1, self.textm2, self.textJ, self.textM]
        labels = ['j_1', 'j_2', 'm_1','m_2', 'J', 'M']
        layout  = QGridLayout()
        for i in range(len(boxes)):
            layout.addWidget(QLabel(labels[i], self), 0, i)
            layout.addWidget(boxes[i], 1, i)
        self.generalLayout.addLayout(layout)
    
    def _createResultLabel(self):
        output = "?"
        self.result = QLabel(f"Clepsh-Gordan Coefficient: {output}")
    
    def _createGetButton(self):
        self.button = QPushButton("GET")
        layout = QGridLayout()
        layout.addWidget(self.button, 0, 0)
        layout.addWidget(self.result, 0, 1)
        self.generalLayout.addLayout(layout)

        self.button.clicked.connect(self.onClick)

    def onClick(self):
        j1 = self.textj1.text()
        j2 = self.textj2.text()
        m1 = self.textm1.text()
        m2 = self.textm2.text()
        J = self.textJ.text()
        M = self.textM.text()

        result = query(j1, j2, m1, m2, J, M)
        if result[0] == '-':
            self.result.setText(F'Clepsh-Gordan Coefficient: -√{result[1:]}')

        else:
            self.result.setText(F'Clepsh-Gordan Coefficient: √{result}')
                            

        



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

