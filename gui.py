from PyQt5.QtCore import QDateTime, Qt, QTimer
from PyQt5.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateTimeEdit,
        QDial, QDialog, QGridLayout, QGroupBox, QHBoxLayout, QLabel, QLineEdit,
        QProgressBar, QPushButton, QRadioButton, QScrollBar, QSizePolicy,
        QSlider, QSpinBox, QStyleFactory, QTableWidget, QTabWidget, QTextEdit,
        QVBoxLayout, QWidget)

from PyQt5.QtWidgets import *

app = QApplication([])

w = QWidget()
w.resize(540, 360)
textBox = QPlainTextEdit(w)
textBox.move(250, 120)
textBox.setPlainText("Do you want to go to the movies with me and Joe")
title = QLabel("Welcome to WurdPlay", w)
title.move(280, 80)

def on_button_clicked1(self):
    textBox.setPlainText("Who's Joe")

def on_button_clicked2():
    textBox.setPlainText("Jo momma")

def on_button_clicked3():
    textBox.setPlainText("You selected UpDown")


button1 = QPushButton("Taboo", w)
button2 = QPushButton("Extra", w)
button3 = QPushButton("Up Down", w)
button1.move(20, 80)
button2.move(20, 120)
button3.move(20, 160)
w.show()


button1.show()
button2.show()
button3.show()
title.show()

button1.clicked.connect(on_button_clicked1)
button2.clicked.connect(on_button_clicked2)
button3.clicked.connect(on_button_clicked3)

app.exec_()