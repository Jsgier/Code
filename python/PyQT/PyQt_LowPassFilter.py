from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QtWidgets

app = QApplication([]) #one instance necessary in all PyQT applications
widgets = QtWidgets
app.setStyle('Fusion')
label = QLabel('Hello World!')
label.show()

#Add a 'solve' button
solveButton = QPushButton('Filter Solved')
app.exec_()