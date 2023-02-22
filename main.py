from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


def dodaj():
    zmienna1 = liczba1.text()
    zmienna2 = liczba2.text()
    wynik = int(zmienna2)+int(zmienna1)
    label2.setText(str(wynik))
    print(zmienna1)
    print(zmienna2)
    print(wynik)



app = QApplication(sys.argv)
win = QMainWindow()
win.setGeometry(400, 400, 500, 300)
win.setWindowTitle("Prosty kalkulator v1")

label = QtWidgets.QLabel(win)
label.setText("Wynik")
label.adjustSize()
label.move(100, 100)

label2 = QtWidgets.QLabel(win)
label2.setText("Wynik")
label2.adjustSize()
label2.move(150, 100)

button = QtWidgets.QPushButton(win)
button.clicked.connect(dodaj)
button.setText("Dodaj")
button.move(100, 150)

liczba1 = QtWidgets.QLineEdit(win)
liczba1.move(300, 150)

liczba2 = QtWidgets.QLineEdit(win)
liczba2.move(300, 100)

win.show()
sys.exit(app.exec_())
