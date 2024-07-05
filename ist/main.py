import sys
from interface.vhod import Ui_MainWindow
from interface.registr import Ui_Registr
from interface.client.client_int import Ui_Client_int
from interface.client.client_int_1 import Ui_Client_int_1
from interface.vodila.vodila_int import Ui_VodilaInt
from interface.vodila.vodila_ist_obsl import Ui_VodCar
from interface.vodila.vodila_ist_obsl_ist import Ui_VodCarIst
from interface.vodila.vodila_int_on import Ui_VodilaInt_on
from interface.client.client_int_2 import Ui_Client_int_2
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

    def entrance(self):
        num_phone = self.ui.lineEdit.text()
        self.num_phone = num_phone.replace("+", "")
        password_client = self.ui.lineEdit_2.text()
        sql_query = "SELECT * FROM client WHERE phone_client = %s AND password_client = %s"
        try:
            with connect(
                    host=host,
                    user=user,
                    password=password,
                    database=db_name,
            ) as connection:
                cursor = connection.cursor()
                cursor.execute(sql_query, (self.num_phone, password_client))
                result = cursor.fetchall()
                if result:
                    sql_query = "SELECT * FROM worker WHERE phone_worker = %s"
                    cursor.execute(sql_query, (self.num_phone,))
                    result1 = cursor.fetchall()
                    if result1:
                        self.openVodilaWindow()
                    else:
                        self.openClientWindow()
                else:
                    print("Пользователь не найден.")
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
        insert_reviewers_query = """
        INSERT INTO client
        (phone_client, password_client)
        VALUES ( %s, %s )
        """
        reviewers_records = [(num_phone, password_client)]
        try:
            with connect(
                    host=host,
                    user=user,
                    password=password,
                    database=db_name,
            ) as connection:
                with connection.cursor() as cursor:
                    cursor.executemany(insert_reviewers_query,
                                       reviewers_records)
                    connection.commit()
            self.goBackToMainWindow()
        except Error as e:
            print(e)
        print(num_phone, password_client)


class ZakCl(QMainWindow):
    def __init__(self, phone_number):
        super().__init__()

        self.ui = Ui_Client_int()
        self.ui.setupUi(self)
        self.phone = phone_number

        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.ui.pushButton_5.clicked.connect(self.orderOn)

        client_phone = f"+{phone_number[0]} ({phone_number[1:4]}) {phone_number[4:7]}-{phone_number[7:9]}-{phone_number[9:]}"
        self.ui.label_8.setText(client_phone)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.hideWindow)
        sql_query = "SELECT idclient FROM client WHERE phone_client = %s"
        try:
            with connect(
                    host=host,
                    user=user,
                    password=password,
                    database=db_name,
            ) as connection:
                cursor = connection.cursor()
                cursor.execute(sql_query, (self.phone,))
                result = cursor.fetchone()
                self.id_client = result[0]
        except Error as e:
            print(e)

    def mousePressEvent(self, event):
        self.oldPos = event.globalPosition()

    def mouseMoveEvent(self, event):
        delta = event.globalPosition() - self.oldPos
        self.move(int(self.x() + delta.x()), int(self.y() + delta.y()))
        self.oldPos = event.globalPosition()

    def openZak_1(self):
        self.main_window = ZakCl_1(self.phone, self.id_order)
        self.main_window.setGeometry(self.geometry())
        self.main_window.show()
        self.timer.start(20)

    def hideWindow(self):
        self.close()

    def orderOn(self):
        current_datetime = datetime.now()
        insert_reviewers_query = """
                INSERT INTO order_client
                (id_client, starting_address, final_address, price_order, state, date_order)
                VALUES ( %s, %s, %s, %s, %s, %s )
                """
        reviewers_records = [(self.id_client, self.ui.textEdit.toPlainText(), self.ui.textEdit_2.toPlainText(), random.randint(100, 1000), "Поиск", current_datetime)]
        try:
            with connect(
                    host=host,
                    user=user,
                    password=password,
                    database=db_name,
            ) as connection:
                with connection.cursor() as cursor:
                    cursor.executemany(insert_reviewers_query,
                                       reviewers_records)
                    connection.commit()
                    self.id_order = cursor.lastrowid
        except Error as e:
            print(e)
        self.openZak_1()


class ZakCl_1(QMainWindow):
    def __init__(self, phone_number, id_order):
        super().__init__()

        self.ui = Ui_Client_int_1()
        self.ui.setupUi(self)
        self.phone = phone_number
        self.id_order = id_order

        self.ui.pushButton_6.clicked.connect(self.cancelOrder)
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)

        client_phone = f"+{phone_number[0]} ({phone_number[1:4]}) {phone_number[4:7]}-{phone_number[7:9]}-{phone_number[9:]}"
        self.ui.label_8.setText(client_phone)
        self.timer_upd_2 = QTimer(self)
        self.timer_upd_2.timeout.connect(self.updateZak)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.hideWindow)
        self.updateZak()

    def mousePressEvent(self, event):
        self.oldPos = event.globalPosition()

    def mouseMoveEvent(self, event):
        delta = event.globalPosition() - self.oldPos
        self.move(int(self.x() + delta.x()), int(self.y() + delta.y()))
        self.oldPos = event.globalPosition()

    def cancelOrder(self):
        update_query = """
            UPDATE order_client
            SET state = %s
            WHERE idorder_client = %s
        """
        try:
            with connect(
                    host=host,
                    user=user,
                    password=password,
                    database=db_name,
            ) as connection:
                with connection.cursor() as cursor:
                    cursor.execute(update_query, ("Отменен", self.id_order))
                    connection.commit()
        except Error as e:
            print(e)
        self.openZak()

    def updateZak(self):
        try:
            with connect(
                    host=host,
                    user=user,
                    password=password,
                    database=db_name,
            ) as connection:
                with connection.cursor() as cursor:
                    sql_query = "SELECT state FROM order_client WHERE idorder_client = %s"
                    cursor.execute(sql_query, (self.id_order,))
                    records = cursor.fetchone()
                    if records[0] == "Выполнение":
                        self.openZakCl_2()
                    else:
                        self.timer_upd_2.start(100)
        except Error as e:
            print(e)

    def openZak(self):
        self.main_window = ZakCl(self.phone)
        self.main_window.setGeometry(self.geometry())
        self.main_window.show()
        self.timer_upd_2.stop()
        self.timer.start(20)

    def openZakCl_2(self):
        self.main_window = ZakCl_2(self.phone, self.id_order)
        self.main_window.setGeometry(self.geometry())
        self.main_window.show()
        self.timer_upd_2.stop()
        self.timer.start(20)

    def hideWindow(self):
        self.close()


class ZakCl_2(QMainWindow):
    def __init__(self, phone_number, id_order):
        super().__init__()

        self.ui = Ui_Client_int_2()
        self.ui.setupUi(self)
        self.phone = phone_number
        self.id_order = id_order

        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)

        try:
            with connect(
                    host=host,
                    user=user,
                    password=password,
                    database=db_name,
            ) as connection:
                cursor = connection.cursor()
                sql_query = "SELECT starting_address, final_address, price_order, id_client, id_car, id_worker, time, distance FROM order_client WHERE idorder_client = %s"
                cursor.execute(sql_query, (self.id_order,))
                result = cursor.fetchone()
                self.start_adr = result[0]
                self.final_adr = result[1]
                self.price = result[2]
                self.id_client = result[3]
                self.id_car = result[4]
                self.id_work = result[5]
                self.pr_time = result[6]
                self.distance = result[7]
                self.ui.label_23.setText(self.start_adr)
                self.ui.label_24.setText(self.final_adr)
        except Error as e:
            print(e)
        try:
            with connect(
                    host=host,
                    user=user,
                    password=password,
                    database=db_name,
            ) as connection:
                cursor = connection.cursor()
                sql_query = "SELECT full_name_worker FROM worker WHERE idworker = %s"
                cursor.execute(sql_query, (self.id_work,))
                result = cursor.fetchone()
                full_name_worker = result[0]
                parts = full_name_worker.split()
            self.new_full_name = " ".join(parts[1:])
        except Error as e:
            print(e)
        try:
            with connect(
                    host=host,
                    user=user,
                    password=password,
                    database=db_name,
            ) as connection:
                cursor = connection.cursor()
                sql_query = "SELECT model, color FROM car WHERE id_worker = %s"
                cursor.execute(sql_query, (self.id_work,))
                result = cursor.fetchone()
                self.color_car = result[1]
                self.model_car = result[0]
        except Error as e:
            print(e)
        print(self.id_work)
        client_phone = f"+{phone_number[0]} ({phone_number[1:4]}) {phone_number[4:7]}-{phone_number[7:9]}-{phone_number[9:]}"
        self.ui.label_8.setText(client_phone)
        self.ui.label_15.setText(f" • Расстояние: {self.distance} км.")
        self.ui.label_16.setText(f" • Цена: {self.price} ₽")
        self.ui.label_19.setText(f" • Машина: {self.model_car}")
        self.ui.label_20.setText(f" • Гос. номер: {self.id_car}")
        self.ui.label_17.setText(f" • Время ожидания: 5 мин.")
        self.ui.label_18.setText(f" • Примерное время: {self.pr_time} мин.")
        self.ui.label_21.setText(f" • Цвет авто.: {self.color_car}")
        self.ui.label_22.setText(f" • Водитель: {self.new_full_name.split()[0]}")
        self.timer_upd_2 = QTimer(self)
        self.timer_upd_2.timeout.connect(self.updateZak)
        self.updateZak()

    def mousePressEvent(self, event):
        self.oldPos = event.globalPosition()

    def mouseMoveEvent(self, event):
        delta = event.globalPosition() - self.oldPos
        self.move(int(self.x() + delta.x()), int(self.y() + delta.y()))
        self.oldPos = event.globalPosition()

    def updateZak(self):
        try:
            with connect(
                    host=host,
                    user=user,
                    password=password,
                    database=db_name,
            ) as connection:
                with connection.cursor() as cursor:
                    sql_query = "SELECT state FROM order_client WHERE idorder_client = %s"
                    cursor.execute(sql_query, (self.id_order,))
                    records = cursor.fetchone()
                    if records[0] == "Выполнение":
                        pass
                    else:
                        self.timer_upd_2.start(100)
        except Error as e:
            print(e)

class Vodila(QMainWindow):
    def __init__(self, phone_number):
        super().__init__()
        self.ui = Ui_VodilaInt()
        self.ui.setupUi(self)
        self.phone = phone_number
        self.list_check = {}
        try:
            with connect(
                    host=host,
                    user=user,
                    password=password,
                    database=db_name,
            ) as connection:
                cursor = connection.cursor()
                sql_query = "SELECT idworker, full_name_worker FROM worker WHERE phone_worker = %s"
                cursor.execute(sql_query, (phone_number,))
                result = cursor.fetchone()
                self.idworker = result[0]
                full_name_worker = result[1]
                parts = full_name_worker.split()
            self.new_full_name = " ".join(parts[1:])
            self.ui.label_8.setText(self.new_full_name)
        except Error as e:
            print(e)

        self.ui.pushButton_2.clicked.connect(self.openVodilaCarWindow)
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.timer_upd = QTimer(self)
        self.timer_upd.timeout.connect(self.updateListOrder)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.hideWindow)
        self.updateListOrder()

    def mousePressEvent(self, event):
        self.oldPos = event.globalPosition()

    def mouseMoveEvent(self, event):
        delta = event.globalPosition() - self.oldPos
        self.move(int(self.x() + delta.x()), int(self.y() + delta.y()))
        self.oldPos = event.globalPosition()

    def updateListOrder(self):
        try:
            with connect(
                    host=host,
                    user=user,
                    password=password,
                    database=db_name,
            ) as connection:
                with connection.cursor() as cursor:
                    sql_query = "SELECT starting_address, idorder_client FROM order_client WHERE state = %s"
                    cursor.execute(sql_query, ("Поиск",))
                    records = cursor.fetchall()
                    children = self.ui.scrollAreaWidgetContents.findChildren(QWidget)
                    for child in children:
                        child.deleteLater()
                    for record in records:
                        if record[1] not in self.list_check.keys():
                            self.list_check[record[1]] = [random.randint(2, 13), round(random.uniform(0.5, 6), 2)]

                        frame = QFrame(parent=self.ui.scrollAreaWidgetContents)
                        frame.setMinimumSize(QtCore.QSize(0, 70))
                        frame.setStyleSheet("border-radius: 0px;")
                        frame.setFrameShape(QFrame.Shape.StyledPanel)
                        frame.setFrameShadow(QFrame.Shadow.Raised)

                        label = QLabel(parent=frame)
                        label.setGeometry(QtCore.QRect(-2, 40, 551, 16))
                        label.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
                        label.setText("<html><head/><body><p><img src=\":/ico osn/Line 2.png\"/></p></body></html>")

                        label = QLabel(parent=frame)
                        label.setGeometry(QtCore.QRect(0, 0, 200, 21))
                        label.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                            "color: rgb(140, 153, 169);")
                        font = QtGui.QFont()
                        font.setFamily("Istok Web")
                        font.setPointSize(13)
                        font.setWeight(50)
                        label.setFont(font)
                        label.setText(f"{record[0]}")

                        label = QLabel(parent=frame)
                        label.setGeometry(QtCore.QRect(172, 0, 81, 21))
                        label.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                            "color: rgb(140, 153, 169);")
                        font = QtGui.QFont()
                        font.setFamily("Istok Web")
                        font.setPointSize(13)
                        font.setWeight(50)
                        label.setFont(font)
                        label.setText(f"{self.list_check[record[1]][0]} мин.")

                        label = QLabel(parent=frame)
                        label.setGeometry(QtCore.QRect(432, 0, 101, 21))
                        label.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                            "color: rgb(140, 153, 169);")
                        font = QtGui.QFont()
                        font.setFamily("Istok Web")
                        font.setPointSize(13)
                        font.setWeight(50)
                        label.setFont(font)
                        label.setText(f"{self.list_check[record[1]][1]} км.")

                        button = QPushButton(parent=frame)
                        button.setGeometry(QtCore.QRect(0, 0, 536, 70))
                        button.setStyleSheet("color: rgb(13, 22, 23);\nbackground-color: rgba(255, 255, 255, 0)")
                        button.setText(f"{record[1]}")
                        button.clicked.connect(self.openOrderClient)

                        self.ui.verticalLayout.addWidget(frame)
        except Error as e:
            print(e)
        self.timer_upd.start(1000)

    def hideWindow(self):
        self.close()

    def openVodilaCarWindow(self):
        self.vodila_car_window = Vodila_Car(self.phone, self.new_full_name, self.idworker)
        self.vodila_car_window.setGeometry(self.geometry())
        self.vodila_car_window.show()
        self.timer.start(20)

    def openOrderClient(self):
        sender = self.sender()
        try:
            with connect(
                    host=host,
                    user=user,
                    password=password,
                    database=db_name,
            ) as connection:
                cursor = connection.cursor()
                sql_query = "SELECT idcar, model, color FROM car WHERE id_worker = %s"
                cursor.execute(sql_query, (self.idworker,))
                result = cursor.fetchone()
                self.id_car = result[0]
                self.color_car = result[2]
                self.model_car = result[1]
        except Error as e:
            print(e)
        update_query = """
            UPDATE order_client
            SET state = %s,
                id_worker = %s,
                id_car = %s,
                time = %s,
                distance = %s
            WHERE idorder_client = %s
        """
        try:
            with connect(
                    host=host,
                    user=user,
                    password=password,
                    database=db_name,
            ) as connection:
                with connection.cursor() as cursor:
                    cursor.execute(update_query, ("Выполнение", self.idworker, self.id_car, self.list_check[int(sender.text())][0], self.list_check[int(sender.text())][1], sender.text()))
                    connection.commit()
        except Error as e:
            print(e)

        self.vodila_car_window = VodilaIntOn(self.phone, sender.text(), self.id_car, self.list_check, self.model_car, self.color_car)
        self.vodila_car_window.setGeometry(self.geometry())
        self.vodila_car_window.show()
        self.timer.start(30)


class VodilaIntOn(QMainWindow):
    def __init__(self, phone_number, idorder, idcar, param_list, model, color):
        super().__init__()
        self.ui = Ui_VodilaInt_on()
        self.ui.setupUi(self)
        self.phone = phone_number
        self.id_order = idorder
        self.id_car = idcar
        self.list_check = param_list
        self.model_car = model
        self.color_car = color
        self.ui.pushButton_9.clicked.connect(self.compliOrder)
        try:
            with connect(
                    host=host,
                    user=user,
                    password=password,
                    database=db_name,
            ) as connection:
                cursor = connection.cursor()
                sql_query = "SELECT idworker, full_name_worker FROM worker WHERE phone_worker = %s"
                cursor.execute(sql_query, (phone_number,))
                result = cursor.fetchone()
                self.idworker = result[0]
                full_name_worker = result[1]
                parts = full_name_worker.split()
            self.new_full_name = " ".join(parts[1:])
            self.ui.label_8.setText(self.new_full_name)
        except Error as e:
            print(e)
        try:
            with connect(
                    host=host,
                    user=user,
                    password=password,
                    database=db_name,
            ) as connection:
                cursor = connection.cursor()
                sql_query = "SELECT starting_address, final_address, price_order, id_client FROM order_client WHERE idorder_client = %s"
                cursor.execute(sql_query, (self.id_order,))
                result = cursor.fetchone()
                self.start_adr = result[0]
                self.final_adr = result[1]
                self.price = result[2]
                self.id_client = result[3]
                self.ui.label_23.setText(self.start_adr)
                self.ui.label_24.setText(self.final_adr)
        except Error as e:
            print(e)
        self.ui.label_15.setText(f" • Расстояние: {self.list_check[int(self.id_order)][1]} км.")
        self.ui.label_16.setText(f" • Цена: {self.price} ₽")
        self.ui.label_19.setText(f" • Машина: {self.model_car}")
        self.ui.label_20.setText(f" • Гос. номер: {self.id_car}")
        self.ui.label_17.setText(f" • Время ожидания: 5 мин.")
        self.ui.label_18.setText(f" • Примерное время: {random.randint(10, 40)} мин.")
        self.ui.label_21.setText(f" • Цвет авто.: {self.color_car}")
        self.ui.label_22.setText(f" • Водитель: {self.new_full_name.split()[0]}")
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.hideWindow)

    def hideWindow(self):
        self.close()

    def mousePressEvent(self, event):
        self.oldPos = event.globalPosition()

    def mouseMoveEvent(self, event):
        delta = event.globalPosition() - self.oldPos
        self.move(int(self.x() + delta.x()), int(self.y() + delta.y()))
        self.oldPos = event.globalPosition()

    def openVodilaWindow(self):
        self.vodila_window = Vodila(self.phone)
        self.vodila_window.setGeometry(self.geometry())
        self.vodila_window.show()
        self.timer.start(20)

    def compliOrder(self):
        update_query = """
            UPDATE order_client
            SET state = %s
            WHERE idorder_client = %s
        """
        try:
            with connect(
                    host=host,
                    user=user,
                    password=password,
                    database=db_name,
            ) as connection:
                with connection.cursor() as cursor:
                    cursor.execute(update_query, ("Завершен", self.id_order))
                    connection.commit()
        except Error as e:
            print(e)
        self.openVodilaWindow()

class Vodila_Car(QMainWindow):
    def __init__(self, phone_number, name, id_worker):
        super().__init__()

        self.id_worker = id_worker
        self.name_worker = name
        self.phone = phone_number
        self.ui = Ui_VodCar()
        self.ui.setupUi(self)

        self.ui.label_8.setText(name)

        self.ui.comboBox.currentTextChanged.connect(self.changeService)

        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.ui.pushButton_5.clicked.connect(self.openVodilaWindow)
        self.ui.pushButton_2.clicked.connect(self.saveInfoCar)
        self.ui.pushButton_9.clicked.connect(self.openVodilaCarIst)
        try:
            with connect(
                    host=host,
                    user=user,
                    password=password,
                    database=db_name,
            ) as connection:
                cursor = connection.cursor()
                sql_query = "SELECT idcar, model FROM car WHERE id_worker = %s"
                cursor.execute(sql_query, (self.id_worker,))
                result = cursor.fetchone()
                self.id_car = result[0]
                self.model_car = result[1]
        except Error as e:
            print(e)
        self.ui.label_13.setText(self.model_car)
        self.ui.label_16.setText(self.id_car)
        try:
            with connect(
                    host=host,
                    user=user,
                    password=password,
                    database=db_name,
            ) as connection:
                cursor = connection.cursor()
                sql_query = "SELECT idservice FROM service"
                cursor.execute(sql_query)
                result = cursor.fetchall()
                for item in result:
                    self.ui.comboBox.addItem(item[0])
        except Error as e:
            print(e)
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

    def changeService(self, value):
        try:
            with connect(
                    host=host,
                    user=user,
                    password=password,
                    database=db_name,
            ) as connection:
                cursor = connection.cursor()
                sql_query = "SELECT price FROM service WHERE idservice = %s"
                cursor.execute(sql_query, (value,))
                result = cursor.fetchone()
                if result[0] != None:
                    self.ui.lineEdit.setText(f"{result[0]}")
                else:
                    self.ui.lineEdit.clear()
        except Error as e:
            print(e)

    def openVodilaWindow(self):
        self.vodila_window = Vodila(self.phone)
        self.vodila_window.setGeometry(self.geometry())
        self.vodila_window.show()
        self.timer.start(20)

    def openVodilaCarIst(self):
        self.vodilacarist_window = Vodila_CarIst(self.name_worker, self.id_car, self.phone, self.id_worker)
        self.vodilacarist_window.setGeometry(self.geometry())
        self.vodilacarist_window.show()
        self.timer.start(20)

    def saveInfoCar(self):
        current_datetime = datetime.now()
        price = self.ui.lineEdit.text()
        comment = self.ui.textEdit.toPlainText()
        id_service = self.ui.comboBox.currentText()
        insert_reviewers_query = """
                INSERT INTO service_rendered
                (id_car, id_service, date, price, comment, id_worker)
                VALUES ( %s, %s, %s, %s, %s, %s )
                """
        reviewers_records = [(self.id_car, id_service, current_datetime, price, comment, self.id_worker)]
        try:
            with connect(
                    host=host,
                    user=user,
                    password=password,
                    database=db_name,
            ) as connection:
                with connection.cursor() as cursor:
                    cursor.executemany(insert_reviewers_query,
                                       reviewers_records)
                    connection.commit()
        except Error as e:
            print(e)
        self.ui.ok()
        self.ui.textEdit.clear()
        self.ui.lineEdit.clear()


class Vodila_CarIst(QMainWindow):
    def __init__(self, name, id_car, phone, id_worker):
        super().__init__()

        self.name = name
        self.id_worker = id_worker
        self.phone = phone
        self.id_car = id_car
        self.ui = Ui_VodCarIst()
        self.ui.setupUi(self)

        self.ui.label_8.setText(name)
        self.ui.label_19.mousePressEvent = self.openVodilaCarWindow
        self.ui.pushButton_5.clicked.connect(self.openVodilaWindow)
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        try:
            with connect(
                    host=host,
                    user=user,
                    password=password,
                    database=db_name,
            ) as connection:
                with connection.cursor() as cursor:
                    sql_query = "SELECT idservice_rendered, id_service, date, price, comment FROM service_rendered WHERE id_car = %s"
                    cursor.execute(sql_query, (id_car,))
                    records = cursor.fetchall()
                    records.reverse()
                for record in records:
                    frame = QFrame(parent=self.ui.scrollAreaWidgetContents)
                    frame.setMinimumSize(QtCore.QSize(0, 100))
                    frame.setStyleSheet("border-radius: 0px;")
                    frame.setFrameShape(QFrame.Shape.StyledPanel)
                    frame.setFrameShadow(QFrame.Shadow.Raised)

                    label = QLabel(parent=frame)
                    label.setGeometry(QtCore.QRect(-2, 85, 551, 16))
                    label.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
                    label.setText("<html><head/><body><p><img src=\":/ico osn/Line 2.png\"/></p></body></html>")
                    label = QLabel(parent=frame)
                    label.setGeometry(QtCore.QRect(0, 0, 81, 21))
                    label.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(140, 153, 169);")
                    font = QtGui.QFont()
                    font.setFamily("Istok Web")
                    font.setPointSize(13)
                    font.setWeight(50)
                    label.setFont(font)
                    label.setText(f"#{record[0]}")
                    label = QLabel(parent=frame)
                    label.setGeometry(QtCore.QRect(92, 0, 111, 21))
                    label.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                        "color: rgb(140, 153, 169);")
                    label.setFont(font)
                    label.setText(f"{record[1]}")
                    label = QLabel(parent=frame)
                    label.setGeometry(QtCore.QRect(472, 0, 81, 21))
                    label.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                        "color: rgb(140, 153, 169);")
                    label.setFont(font)
                    label.setText(f"{record[3]}")
                    label = QLabel(parent=frame)
                    label.setGeometry(QtCore.QRect(0, 50, 201, 21))
                    label.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                        "color: rgb(140, 153, 169);")
                    label.setFont(font)
                    label.setText(f"{record[2]}")

                    textEdit = QTextEdit(parent=frame)
                    textEdit.setGeometry(QtCore.QRect(222, 0, 231, 81))
                    font = QtGui.QFont()
                    font.setFamily("Istok Web")
                    font.setPointSize(13)
                    textEdit.setFont(font)
                    textEdit.setStyleSheet("color: rgb(140, 153, 169);")
                    textEdit.setText(f"{record[4]}")
                    self.ui.verticalLayout.addWidget(frame)
        except Error as e:
            print(e)
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

    def openVodilaWindow(self):
        self.vodila_window = Vodila(self.phone)
        self.vodila_window.setGeometry(self.geometry())
        self.vodila_window.show()
        self.timer.start(20)

    def openVodilaCarWindow(self, event):
        self.vodila_car_window = Vodila_Car(self.phone, self.name, self.id_worker)
        self.vodila_car_window.setGeometry(self.geometry())
        self.vodila_car_window.show()
        self.timer.start(20)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
