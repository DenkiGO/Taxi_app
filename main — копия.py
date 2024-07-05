import sys
from interface.vhod import Ui_MainWindow
from interface.registr import Ui_Registr
from adm_int import Admin
from vod_int import Vodila
from cl_int import ZakCl
from datetime import datetime
from mysql.connector import connect, Error
from config import host, user, password, db_name
from PyQt6.QtWidgets import QMainWindow, QLabel, QPushButton, QTextEdit, QFrame, QVBoxLayout, QWidget, QApplication
from PyQt6.QtCore import Qt, QPoint, QTimer
from PyQt6 import QtCore, QtGui
from PyQt6.QtGui import QMouseEvent
import random
import image

try:
    with connect(
        host=host,
        user=user,
        password=password,
        database=db_name,
    ) as connection:
       print("OK!")
except Error as e:
    print(e)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)

        self.ui.label_5.setCursor(Qt.CursorShape.PointingHandCursor)
        self.ui.label_5.setMouseTracking(True)
        self.ui.label_5.mousePressEvent = self.minimizeApp

        self.ui.pushButton_2.clicked.connect(self.openRegisterWindow)
        self.ui.pushButton.clicked.connect(self.entrance)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.hideWindow)

    def mousePressEvent(self, event):
        self.oldPos = event.globalPosition()

    def mouseMoveEvent(self, event):
        delta = event.globalPosition() - self.oldPos
        self.move(int(self.x() + delta.x()), int(self.y() + delta.y()))
        self.oldPos = event.globalPosition()

    def minimizeApp(self, event):
        self.showMinimized()

    def openRegisterWindow(self):
        self.register_window = RegisterWindow()
        self.register_window.setGeometry(self.geometry())
        self.register_window.show()
        self.timer.start(20)

    def hideWindow(self):
        self.close()

    def openClientWindow(self):
        self.client_window = ZakCl(self.num_phone)
        self.client_window.setGeometry(self.geometry())
        self.client_window.show()
        self.timer.start(20)

    def openVodilaWindow(self):
        self.vodila_window = Vodila(self.num_phone)
        self.vodila_window.setGeometry(self.geometry())
        self.vodila_window.show()
        self.timer.start(20)

    def openAdminWindow(self):
        self.vodila_window = Admin(self.num_phone)
        self.vodila_window.setGeometry(self.geometry())
        self.vodila_window.show()
        self.timer.start(20)

    def entrance(self):
        num_phone = self.ui.lineEdit.text()
        self.num_phone = num_phone.replace("+", "")
        password_client = self.ui.lineEdit_2.text()
        try:
            with connect(
                    host=host,
                    user=user,
                    password=password,
                    database=db_name
            ) as connection:
                with connection.cursor() as cursor:
                    result_args = cursor.callproc('log_in', [self.num_phone, password_client, 0, 0])
                    is_registered = result_args[2]
                    client_position = result_args[3]
                    if str(is_registered) == "1":
                        if client_position == "Администратор":
                            self.openAdminWindow()
                        elif client_position == "Водитель":
                            self.openVodilaWindow()
                        else:
                            self.openClientWindow()
        except Error as e:
            print(e)


class RegisterWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_Registr()
        self.ui.setupUi(self)

        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)

        self.ui.label_5.mousePressEvent = self.minimizeApp

        self.ui.pushButton_2.clicked.connect(self.goBackToMainWindow)
        self.ui.pushButton.clicked.connect(self.reistr_on)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.hideWindow)

    def mousePressEvent(self, event):
        self.oldPos = event.globalPosition()

    def mouseMoveEvent(self, event):
        delta = event.globalPosition() - self.oldPos
        self.move(int(self.x() + delta.x()), int(self.y() + delta.y()))
        self.oldPos = event.globalPosition()

    def hideWindow(self):
        self.close()

    def minimizeApp(self, event):
        self.showMinimized()

    def goBackToMainWindow(self):
        self.main_window = MainWindow()
        self.main_window.setGeometry(self.geometry())
        self.main_window.show()
        self.timer.start(20)

    def reistr_on(self):
        num_phone = self.ui.lineEdit.text()
        num_phone = num_phone.replace("+", "")
        password_client = self.ui.lineEdit_2.text()
        try:
            with connect(
                    host=host,
                    user=user,
                    password=password,
                    database=db_name,
            ) as connection:
                with connection.cursor() as cursor:
                    result_args = cursor.callproc('register_client', [num_phone, password_client, 0])
                    is_registered = result_args[2]
                    connection.commit()
        except Error as e:
            print(e)
        if str(is_registered) == '1':
            self.goBackToMainWindow()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
