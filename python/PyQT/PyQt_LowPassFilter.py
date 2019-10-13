
import sys

from scipy import signal

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, \
 QHBoxLayout, QVBoxLayout, QSizePolicy, QLabel, QMessageBox, \
 QGridLayout, QPushButton, QWidget, QLineEdit
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

import random

import math
pi = math.pi

class App(QWidget):
    def __init__(self):
        super().__init__()
        #setup the title and geometry of the GUI
        self.title = "Low Pass Filter"
        self.left = 200
        self.top = 200
        self.width = 1400
        self.height = 0.3 * self.width
        self.initUI()
        
    def initUI(self):
        self.bode = PlotCanvas(self, width=10, height=2)
        self.bode.move(0,0)

        #add "Solve Filter" button to execute filter solution
        solveButton = QPushButton('Solve Filter', self)
        solveButton.setToolTip('Solve the equation for the low pass filter')
        solveButton.move(100, 70)
        solveButton.resize(140,100)
        solveButton.clicked.connect(self.on_click)

        #add text boxes for resistor and capacitor values
        resLabel = QLabel()
        resLabel.setText('Resistor:')
        self.resistor = QLineEdit(resLabel)
        capLabel = QLabel()
        capLabel.setText('Capacitor:')
        self.capacitor = QLineEdit(capLabel)

        #setup the layout into a grid
        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(self.bode, 0, 0, 3, 2) #add plot to 0,0 with width 2, height 3
        grid.addWidget(self.resistor, 4, 0) #resistor box at row 4 column 0
        grid.addWidget(self.capacitor, 4, 1) #capacitor box at row 4 column 1
        grid.addWidget(solveButton, 5, 0) #solve button at row 5, column 0

        self.setLayout(grid)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setWindowTitle(self.title)

        self.show()
    
    @pyqtSlot()
    def on_click(self):#, resistor, capacitor):
        print(self.resistor.text())
        pole = 1 / (2* pi * float(self.resistor.text())* float(self.capacitor.text()))
        s1 = signal.ZerosPolesGain = ([],[pole],[1])
        w, mag, phase = signal.bode(s1)
        PlotCanvas(self, s1 = s1)
        print(pole)
        #do math here later
        #Add two input buttons for resistor and capacitor

class PlotCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100, s1 = signal.ZerosPolesGain([],[1],[1])):
        fig = Figure(figsize=(width, height), dpi=dpi)

        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self, QSizePolicy.Expanding, \
            QSizePolicy.Expanding)
        
        FigureCanvas.updateGeometry(self)
        self.bode_plot(s1)
    
    def plot(self):
        data = [random.random() for i in range (25)]
        ax = self.figure.add_subplot(111)
        ax.plot(data, 'r-')
        ax.set_title('Magnitude (dB) vs. Frequency [Hz]')
        self.draw

    def bode_plot(self, s1):
        w, mag, phase = signal.bode(s1)
        ax = self.figure.add_subplot(111)
        ax.semilogy(w, mag)
        ax.set_title('Magnitude (dB) vs. Frequency [Hz]')
        self.draw


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())