
import sys
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QWidget
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

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

        button = QPushButton('Solve Filter', self)
        button.setToolTip('Solve the equation for the low pass filter')
        button.move(100, 70)
        button.clicked.connect(self.on_click)

        self.show()
    
    @pyqtSlot()
    def on_click(self):
        print("Button CLicked")
        #do math here later
        #Add two input buttons for resistor and capacitor

def bttnstate(self):
    if self.solveButton.isChecked():
        print ("Button Pressed")
    else:
        print("Button Released")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())