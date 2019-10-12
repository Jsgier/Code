
import sys

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, \
        QVBoxLayout, QSizePolicy, QLabel, QMessageBox, QPushButton, QWidget
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

import random

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = "Low Pass Filter"
        self.left = 10
        self.top = 10
        self.width = 320
        self.height = 200
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        m = PlotCanvas(self, width=5, height=4)
        m.move(0,0)

        button = QPushButton('Solve Filter', self)
        button.setToolTip('Solve the equation for the low pass filter')
        button.move(100, 70)
        button.resize(140,100)
        button.clicked.connect(self.on_click)

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