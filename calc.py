import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QButtonGroup, QPushButton, QGroupBox,
QHBoxLayout, QVBoxLayout, QTextEdit, QLineEdit, QLabel, QMessageBox, QRadioButton, QCheckBox, QSystemTrayIcon, QMenu)
from PyQt5.QtGui import QIntValidator, QIcon, QPixmap
import random
import ctypes

def convert_base():
    num = num1.text()
    to_base = to_base1.text()
    from_base = from_base1.text()
    if isinstance(num, str):
        n = int(num, from_base)
    else:
        n = int(num)
    print(num, to_base, from_base)

    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    if n < to_base:
        return alphabet[n]
    else:
        return n // to_base, to_base + alphabet[n % to_base]
    finnum.setText(str(n))

# Создание окна
app = QApplication([])
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID('очень уникальная строка')
app.setWindowIcon(QIcon('1.png')) #
app.setStyle('Fusion')
main_win = QWidget()
main_win.setWindowIcon(QIcon('key.png')) #
main_win.setFixedSize(400, 350)
main_win.setWindowTitle('Генератор паролей')

#
num1 = QLineEdit()
from_base1 = QLineEdit()
to_base1 = QLineEdit()
num1.setPlaceholderText('Число')
from_base1.setPlaceholderText('Из СС')
to_base1.setPlaceholderText('В СС')

start = QPushButton('Перевести')
finnum = QTextEdit()

tip = QLabel()
tip.setFixedWidth(15)
pic = QPixmap('info.png')
tip.setGeometry(10, 10, 300, 300)
tip.setPixmap(pic)


#tip.setToolTip('Каким считается хороший пароль? \n'
#               '- Длиной от 8 символов и выше. \n'
 #              '- Имеющий большие и маленькие буквы. \n'
  #             '- Содержащий в себе цифры. \n'
   #            '- Имеющий хотя бы один спец. символ: $%#@. \n'
    #           '- Желательно без повторяющихся символов.')

# Создание layout
layout_main = QVBoxLayout()
layoutH = QHBoxLayout()
layoutHbutton = QHBoxLayout()
layoutVopt = QVBoxLayout()
layoutHoptions = QHBoxLayout()
layoutHoptions2 = QHBoxLayout()

options = QGroupBox()
options.setTitle('Выберите опции:')

options.setLayout(layoutVopt)


main_win.setLayout(layout_main)
layout_main.addLayout(layoutH)
layout_main.addWidget(options, alignment=Qt.AlignCenter)
layout_main.addLayout(layoutHbutton)
layout_main.addWidget(finnum, alignment=Qt.AlignCenter)
layout_main.addWidget(tip)
#
# layoutH.addWidget(welcome, alignment=Qt.AlignCenter)
layoutHbutton.addWidget(start, alignment=Qt.AlignCenter)
#
layoutVopt.addLayout(layoutHoptions)
layoutVopt.addLayout(layoutHoptions2)
layoutHoptions.addWidget(from_base1, alignment=Qt.AlignCenter)
layoutHoptions.addWidget(to_base1, alignment=Qt.AlignCenter)
layoutHoptions2.addWidget(num1, alignment=Qt.AlignCenter)


main_win.setLayout(layout_main)

start.clicked.connect(convert_base)

main_win.show()
app.exec_()
