
import sys

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, \
 QHBoxLayout, QVBoxLayout, QSizePolicy, QLabel, QMessageBox, QPushButton, QWidget
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

import random

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = "Low Pass Filter"
        self.left = 200
        self.top = 200
        self.width = 500
        self.height = 500
        self.initUI()
        
    def initUI(self):
        m = PlotCanvas(self, width=5, height=4)
        m.move(0,0)

        solveButton = QPushButton('Solve Filter', self)
        solveButton.setToolTip('Solve the equation for the low pass filter')
        solveButton.move(100, 70)
        solveButton.resize(140,100)
        solveButton.clicked.connect(self.on_click)

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(m)
        hbox.addWidget(solveButton)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setWindowTitle(self.title)

        self.show()
    
    @pyqtSlot()
    def on_click(self):
        print("Button Clicked")
        #do math here later
        #Add two input buttons for resistor and capacitor

class PlotCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)

        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self, QSizePolicy.Expanding, \
            QSizePolicy.Expanding)
        
        FigureCanvas.updateGeometry(self)
        self.plot()
    
    def plot(self):
        data = [random.random() for i in range (25)]
        ax = self.figure.add_subplot(111)
        ax.plot(data, 'r-')
        ax.set_title('Magnitude (dB) vs. Frequency [Hz]')
        self.draw



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())