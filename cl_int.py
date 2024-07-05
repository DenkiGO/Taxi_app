import vod_int
import adm_int
from interface.client.client_int_2 import Ui_Client_int_2
from interface.client.client_int import Ui_Client_int
from interface.client.client_int_1 import Ui_Client_int_1
from interface.client.client_int_3 import Ui_Client_int_3
from interface.client.client_otz_ist import Ui_ClientOtzIst
from interface.client.client_ist_zak import Ui_ClientIstZak
from interface.client.client_ist_zak_1 import Ui_ClientZak_1
from interface.client.client_ist_zak_2 import Ui_ClientZak_2
from interface.client.client_chat_1 import Ui_ClientChatList
from interface.client.client_chat_2 import Ui_ClientChat
from interface.client.client_pod import Ui_ClientPod
from datetime import datetime
from mysql.connector import connect, Error
from config import host, user, password, db_name
from PyQt6.QtWidgets import QMainWindow, QLabel, QPushButton, QTextEdit, QFrame, QVBoxLayout, QWidget, QApplication, QSizePolicy
from PyQt6.QtCore import Qt, QPoint, QTimer, QRect
from PyQt6 import QtCore, QtGui
from PyQt6.QtGui import QMouseEvent, QFontMetrics
import random
import image

class ZakCl(QMainWindow):
    def __init__(self, phone_number, sotr=-1):
        super().__init__()

        self.ui = Ui_Client_int()
        self.ui.setupUi(self)
        self.phone = phone_number

        sql_query = "SELECT position FROM worker WHERE phone_worker = %s"

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
                if result:
                    if str(result[0]) == "Водитель":
                        self.id_worker = result[0]
                        self.ui.pushButton_6.clicked.connect(self.openVodilaWindow)
                    elif str(result[0]) == "Администратор":
                        self.id_worker = result[0]
                        self.ui.pushButton_6.clicked.connect(self.openAdminWindow)
                        self.ui.pushButton_6.setText("       Админ панель")
                else:
                    self.ui.pushButton_6.hide()
        except Error as e:
            print(e)

        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.ui.pushButton_5.clicked.connect(self.orderOn)
        self.ui.pushButton.clicked.connect(self.openChatList)
        self.ui.pushButton_4.clicked.connect(self.openClPod)

        client_phone = f"+{phone_number[0]} ({phone_number[1:4]}) {phone_number[4:7]}-{phone_number[7:9]}-{phone_number[9:]}"
        self.ui.label_8.setText(client_phone)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.hideWindow)
        self.ui.pushButton_2.clicked.connect(self.openZakIstOtz)
        self.ui.pushButton_3.clicked.connect(self.openZakIst)
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

    def openAdminWindow(self):
        self.admin_window = adm_int.Admin(self.phone)
        self.admin_window.setGeometry(self.geometry())
        self.admin_window.show()
        self.timer.start(20)

    def openVodilaWindow(self):
        self.vodila_window = vod_int.Vodila(self.phone)
        self.vodila_window.setGeometry(self.geometry())
        self.vodila_window.show()
        self.timer.start(20)

    def openZak_1(self):
        self.main_window = ZakCl_1(self.phone, self.id_order)
        self.main_window.setGeometry(self.geometry())
        self.main_window.show()
        self.timer.start(20)

    def openClPod(self):
        self.main_window = Clent_Pod(self.phone)
        self.main_window.setGeometry(self.geometry())
        self.main_window.show()
        self.timer.start(20)

    def openChatList(self):
        self.main_window_1 = ClChatList(self.phone)
        self.main_window_1.setGeometry(self.geometry())
        self.main_window_1.show()
        self.timer.start(20)

    def hideWindow(self):
        self.close()

    def openZakIstOtz(self):
        self.main_window = ZakClOtzIst(self.phone)
        self.main_window.setGeometry(self.geometry())
        self.main_window.show()
        self.timer.start(20)

    def openZakIst(self):
        self.main_window = ClIstZak(self.phone)
        self.main_window.setGeometry(self.geometry())
        self.main_window.show()
        self.timer.start(20)

    def orderOn(self):
        current_datetime = datetime.now()
        try:
            with connect(
                    host=host,
                    user=user,
                    password=password,
                    database=db_name
            ) as connection:
                with connection.cursor() as cursor:
                    result_args = cursor.callproc('creating_order', [self.id_client, self.ui.textEdit.toPlainText(), self.ui.textEdit_2.toPlainText(), random.randint(100, 1000), "Поиск", current_datetime, 0])
                    connection.commit()
                    self.id_order = result_args[-1]
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
        try:
            with connect(
                    host=host,
                    user=user,
                    password=password,
                    database=db_name,
            ) as connection:
                with connection.cursor() as cursor:
                    cursor.callproc('update_order_state', [self.id_order, "Отменен"])
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
        self.ui.pushButton_5.clicked.connect(self.openChatVod)
        self.ui.pushButton_6.clicked.connect(self.cancelOrder)

        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)

        try:
            with connect(
                    host=host,
                    user=user,
                    password=password,
                    database=db_name,
            ) as connection:
                cursor = connection.cursor()
                sql_query = "SELECT starting_address, final_address, price_order, id_client, id_work_shift, time, distance FROM order_client WHERE idorder_client = %s"
                cursor.execute(sql_query, (self.id_order,))
                result = cursor.fetchone()
                self.start_adr = result[0]
                self.final_adr = result[1]
                self.price = result[2]
                self.id_client = result[3]
                self.id_work_shift = result[4]
                self.pr_time = result[5]
                self.distance = result[6]
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
                with connection.cursor() as cursor:
                    result_args = cursor.callproc('get_worker_and_car_info', [self.id_work_shift, 0, 0, "", "", ""])
                    self.id_worker = result_args[1]
                    self.id_car = result_args[2]
                    self.new_full_name = result_args[3]
                    self.model_car = result_args[4]
                    self.color_car = result_args[5]
        except Error as e:
            print(e)
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
        self.list_all = [self.distance, self.price, self.model_car, self.id_car, self.pr_time, self.color_car, self.new_full_name.split()[0], self.start_adr, self.final_adr, self.id_worker]
        self.timer_upd_3 = QTimer(self)
        self.timer_upd_3.timeout.connect(self.updateZak)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.hideWindow)
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
                    if records[0] == "Завершен":
                        self.openZakClOtz()
                    else:
                        self.timer_upd_3.start(100)
        except Error as e:
            print(e)

    def cancelOrder(self):
        try:
            with connect(
                    host=host,
                    user=user,
                    password=password,
                    database=db_name,
            ) as connection:
                with connection.cursor() as cursor:
                    cursor.callproc('update_order_state', [self.id_order, "Отменен"])
                    connection.commit()
        except Error as e:
            print(e)
        self.openZak()

    def openChatVod(self):
        flag = False
        id_chat = 0
        try:
            with connect(
                    host=host,
                    user=user,
                    password=password,
                    database=db_name,
            ) as connection:
                cursor = connection.cursor()
                sql_query = "SELECT id_worker, idchat, state FROM chat WHERE id_client = %s"
                cursor.execute(sql_query, (self.id_client,))
                result = cursor.fetchall()
                for res in result:
                    if str(res[0]) == str(self.id_worker):
                        flag = True
                        id_chat = res[1]
                        if res[2] != "Активен":
                            cursor.callproc('update_chat_status', [id_chat, "Активен"])
                        break
        except Error as e:
            print(e)
        if flag == True:
            self.main_window = ClChat(self.phone, id_chat, self.id_client, self.id_order)
            self.main_window.setGeometry(self.geometry())
            self.main_window.show()
            self.timer_upd_3.stop()
            self.timer.start(20)
        else:
            current_datetime = datetime.now()
            try:
                with connect(
                        host=host,
                        user=user,
                        password=password,
                        database=db_name,
                ) as connection:
                    with connection.cursor() as cursor:
                        args = cursor.callproc('insert_chat', [current_datetime, self.id_client, "Нет", "Активен", self.id_worker, 0])
                        connection.commit()
                        id_chat = args[5]
            except Error as e:
                print(e)
            self.main_window = ClChat(self.phone, id_chat, self.id_client, self.id_order)
            self.main_window.setGeometry(self.geometry())
            self.main_window.show()
            self.timer_upd_3.stop()
            self.timer.start(20)

    def openZak(self):
        self.main_window = ZakCl(self.phone)
        self.main_window.setGeometry(self.geometry())
        self.main_window.show()
        self.timer_upd_3.stop()
        self.timer.start(20)

    def openZakClOtz(self):
        self.main_window = ZakClOtz(self.phone, self.id_order, self.list_all)
        self.main_window.setGeometry(self.geometry())
        self.main_window.show()
        self.timer_upd_3.stop()
        self.timer.start(20)

    def hideWindow(self):
        self.close()


class ZakClOtz(QMainWindow):
    def __init__(self, phone_number, id_order, list_all):
        super().__init__()

        self.ui = Ui_Client_int_3()
        self.ui.setupUi(self)
        self.phone = phone_number
        self.id_order = id_order
        self.list_all = list_all

        self.ui.pushButton.clicked.connect(self.openChatList)

        self.ui.label_40.mousePressEvent = self.openZak_1

        self.ui.label_27.setText(f"История заказа: #{self.id_order}")
        self.ui.label_31.setText(f"{self.list_all[7]}")
        self.ui.label_32.setText(f"{self.list_all[8]}")
        self.ui.label_15.setText(f" • Расстояние: {self.list_all[0]} км.")
        self.ui.label_16.setText(f" • Цена: {self.list_all[1]} ₽")
        self.ui.label_19.setText(f" • Машина: {self.list_all[2]}")
        self.ui.label_20.setText(f" • Гос. номер: {self.list_all[3]}")
        self.ui.label_17.setText(f" • Время ожидания: 5 мин.")
        self.ui.label_18.setText(f" • Примерное время: {self.list_all[4]} мин.")
        self.ui.label_21.setText(f" • Цвет авто.: {self.list_all[5]}")
        self.ui.label_22.setText(f" • Водитель: {self.list_all[6]}")

        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.ui.pushButton_5.clicked.connect(self.otz)
        self.ui.pushButton_3.clicked.connect(self.openZakIst)
        self.ui.pushButton_4.clicked.connect(self.openClPod)
        self.ui.pushButton_2.clicked.connect(self.openZakIstOtz)

        client_phone = f"+{phone_number[0]} ({phone_number[1:4]}) {phone_number[4:7]}-{phone_number[7:9]}-{phone_number[9:]}"
        self.ui.label_8.setText(client_phone)
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

    def otz(self):
        try:
            with connect(
                    host=host,
                    user=user,
                    password=password,
                    database=db_name,
            ) as connection:
                with connection.cursor() as cursor:
                    args = cursor.callproc('insert_feedback', [self.id_order, self.ui.ocenka, self.ui.textEdit.toPlainText(), self.phone, 0])
                    connection.commit()
                    self.id_order = args[4]
        except Error as e:
            print(e)
        self.openZak()

    def openZak_1(self, event):
        self.main_window = ZakCl(self.phone)
        self.main_window.setGeometry(self.geometry())
        self.main_window.show()
        self.timer.start(20)

    def openZak(self):
        self.main_window = ZakCl(self.phone)
        self.main_window.setGeometry(self.geometry())
        self.main_window.show()
        self.timer.start(20)

    def openClPod(self):
        self.main_window = Clent_Pod(self.phone)
        self.main_window.setGeometry(self.geometry())
        self.main_window.show()
        self.timer.start(20)

    def openZakIst(self):
        self.main_window = ClIstZak(self.phone)
        self.main_window.setGeometry(self.geometry())
        self.main_window.show()
        self.timer.start(20)

    def openZakIstOtz(self):
        self.main_window = ZakClOtzIst(self.phone)
        self.main_window.setGeometry(self.geometry())
        self.main_window.show()
        self.timer.start(20)

    def openChatList(self):
        self.main_window = ClChatList(self.phone)
        self.main_window.setGeometry(self.geometry())
        self.main_window.show()
        self.timer.start(20)


class ZakClOtzIst(QMainWindow):
    def __init__(self, phone_number):
        super().__init__()

        self.ui = Ui_ClientOtzIst()
        self.ui.setupUi(self)
        self.phone = phone_number

        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.ui.pushButton_3.clicked.connect(self.openZakIst)
        self.ui.pushButton_6.clicked.connect(self.openChatList)

        client_phone = f"+{phone_number[0]} ({phone_number[1:4]}) {phone_number[4:7]}-{phone_number[7:9]}-{phone_number[9:]}"
        self.ui.label_8.setText(client_phone)
        self.ui.pushButton_5.clicked.connect(self.openZak)
        self.ui.pushButton_4.clicked.connect(self.openClPod)

        try:
            with connect(
                    host=host,
                    user=user,
                    password=password,
                    database=db_name,
            ) as connection:
                cursor = connection.cursor()
                sql_query = "SELECT idclient FROM client WHERE phone_client = %s"
                cursor.execute(sql_query, (self.phone,))
                result = cursor.fetchone()
                self.client_id = result[0]
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
                sql_query = "SELECT id_order, score, text FROM feedback WHERE id_client = %s"
                cursor.execute(sql_query, (self.client_id,))
                records = cursor.fetchall()
                records.reverse()
                for record in records:
                    frame = QFrame(parent=self.ui.scrollAreaWidgetContents)
                    frame.setMinimumSize(QtCore.QSize(0, 100))
                    frame.setStyleSheet("border-radius: 0px;")
                    frame.setFrameShape(QFrame.Shape.StyledPanel)
                    frame.setFrameShadow(QFrame.Shadow.Raised)

                    if record[1] >= 1:
                        label = QLabel(parent=frame)
                        label.setGeometry(QtCore.QRect(420, 0, 20, 20))
                        label.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
                        label.setText("<html><head/><body><p><img src=\":/zv/zvmin_on.png\"/></p></body></html>")
                        if record[1] >= 2:
                            label = QLabel(parent=frame)
                            label.setGeometry(QtCore.QRect(445, 0, 20, 20))
                            label.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
                            label.setText("<html><head/><body><p><img src=\":/zv/zvmin_on.png\"/></p></body></html>")
                            if record[1] >= 3:
                                label = QLabel(parent=frame)
                                label.setGeometry(QtCore.QRect(470, 0, 20, 20))
                                label.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
                                label.setText(
                                    "<html><head/><body><p><img src=\":/zv/zvmin_on.png\"/></p></body></html>")
                                if record[1] >= 4:
                                    label = QLabel(parent=frame)
                                    label.setGeometry(QtCore.QRect(495, 0, 20, 20))
                                    label.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
                                    label.setText(
                                        "<html><head/><body><p><img src=\":/zv/zvmin_on.png\"/></p></body></html>")
                                    if record[1] == 5:
                                        label = QLabel(parent=frame)
                                        label.setGeometry(QtCore.QRect(520, 0, 20, 20))
                                        label.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
                                        label.setText(
                                            "<html><head/><body><p><img src=\":/zv/zvmin_on.png\"/></p></body></html>")
                                    else:
                                        label = QLabel(parent=frame)
                                        label.setGeometry(QtCore.QRect(520, 0, 20, 20))
                                        label.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
                                        label.setText(
                                            "<html><head/><body><p><img src=\":/zv/zvmin.png\"/></p></body></html>")
                                else:
                                    label = QLabel(parent=frame)
                                    label.setGeometry(QtCore.QRect(495, 0, 20, 20))
                                    label.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
                                    label.setText(
                                        "<html><head/><body><p><img src=\":/zv/zvmin.png\"/></p></body></html>")
                                    label = QLabel(parent=frame)
                                    label.setGeometry(QtCore.QRect(520, 0, 20, 20))
                                    label.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
                                    label.setText(
                                        "<html><head/><body><p><img src=\":/zv/zvmin.png\"/></p></body></html>")
                            else:
                                label = QLabel(parent=frame)
                                label.setGeometry(QtCore.QRect(470, 0, 20, 20))
                                label.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
                                label.setText(
                                    "<html><head/><body><p><img src=\":/zv/zvmin.png\"/></p></body></html>")
                                label = QLabel(parent=frame)
                                label.setGeometry(QtCore.QRect(495, 0, 20, 20))
                                label.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
                                label.setText(
                                    "<html><head/><body><p><img src=\":/zv/zvmin.png\"/></p></body></html>")
                                label = QLabel(parent=frame)
                                label.setGeometry(QtCore.QRect(520, 0, 20, 20))
                                label.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
                                label.setText(
                                    "<html><head/><body><p><img src=\":/zv/zvmin.png\"/></p></body></html>")
                        else:
                            label = QLabel(parent=frame)
                            label.setGeometry(QtCore.QRect(445, 0, 20, 20))
                            label.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
                            label.setText("<html><head/><body><p><img src=\":/zv/zvmin.png\"/></p></body></html>")
                            label = QLabel(parent=frame)
                            label.setGeometry(QtCore.QRect(470, 0, 20, 20))
                            label.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
                            label.setText(
                                "<html><head/><body><p><img src=\":/zv/zvmin.png\"/></p></body></html>")
                            label = QLabel(parent=frame)
                            label.setGeometry(QtCore.QRect(495, 0, 20, 20))
                            label.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
                            label.setText(
                                "<html><head/><body><p><img src=\":/zv/zvmin.png\"/></p></body></html>")
                            label = QLabel(parent=frame)
                            label.setGeometry(QtCore.QRect(520, 0, 20, 20))
                            label.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
                            label.setText(
                                "<html><head/><body><p><img src=\":/zv/zvmin.png\"/></p></body></html>")
                    else:
                        label = QLabel(parent=frame)
                        label.setGeometry(QtCore.QRect(420, 0, 20, 20))
                        label.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
                        label.setText("<html><head/><body><p><img src=\":/zv/zvmin.png\"/></p></body></html>")
                        label = QLabel(parent=frame)
                        label.setGeometry(QtCore.QRect(445, 0, 20, 20))
                        label.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
                        label.setText("<html><head/><body><p><img src=\":/zv/zvmin.png\"/></p></body></html>")
                        label = QLabel(parent=frame)
                        label.setGeometry(QtCore.QRect(470, 0, 20, 20))
                        label.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
                        label.setText("<html><head/><body><p><img src=\":/zv/zvmin.png\"/></p></body></html>")
                        label = QLabel(parent=frame)
                        label.setGeometry(QtCore.QRect(495, 0, 20, 20))
                        label.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
                        label.setText("<html><head/><body><p><img src=\":/zv/zvmin.png\"/></p></body></html>")
                        label = QLabel(parent=frame)
                        label.setGeometry(QtCore.QRect(520, 0, 20, 20))
                        label.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
                        label.setText("<html><head/><body><p><img src=\":/zv/zvmin.png\"/></p></body></html>")

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

                    try:
                        with connect(
                                host=host,
                                user=user,
                                password=password,
                                database=db_name,
                        ) as connection:
                            cursor = connection.cursor()
                            sql_query = "SELECT date FROM order_client WHERE idorder_client  = %s"
                            cursor.execute(sql_query, (record[0],))
                            result = cursor.fetchone()
                            self.date_order = result[0]
                    except Error as e:
                        print(e)

                    label = QLabel(parent=frame)
                    label.setGeometry(QtCore.QRect(0, 50, 171, 21))
                    label.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                        "color: rgb(140, 153, 169);")
                    label.setFont(font)
                    label.setText(f"{self.date_order}")

                    textEdit = QTextEdit(parent=frame)
                    textEdit.setGeometry(QtCore.QRect(172, 0, 231, 81))
                    font = QtGui.QFont()
                    font.setFamily("Istok Web")
                    font.setPointSize(13)
                    textEdit.setFont(font)
                    textEdit.setStyleSheet("color: rgb(140, 153, 169);")
                    textEdit.setText(f"{record[2]}")
                    textEdit.setReadOnly(True)
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

    def openZak(self):
        self.main_window = ZakCl(self.phone)
        self.main_window.setGeometry(self.geometry())
        self.main_window.show()
        self.timer.start(20)

    def openZakIst(self):
        self.main_window = ClIstZak(self.phone)
        self.main_window.setGeometry(self.geometry())
        self.main_window.show()
        self.timer.start(20)

    def openChatList(self):
        self.main_window = ClChatList(self.phone)
        self.main_window.setGeometry(self.geometry())
        self.main_window.show()
        self.timer.start(20)

    def openClPod(self):
        self.main_window = Clent_Pod(self.phone)
        self.main_window.setGeometry(self.geometry())
        self.main_window.show()
        self.timer.start(20)

    def hideWindow(self):
        self.close()

class ClIstZak(QMainWindow):
    def __init__(self, phone_number):
        super().__init__()

        self.ui = Ui_ClientIstZak()
        self.ui.setupUi(self)
        self.phone = phone_number

        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.ui.pushButton_7.clicked.connect(self.openZakIstOtz)
        self.ui.pushButton_5.clicked.connect(self.openZak)
        self.ui.pushButton_6.clicked.connect(self.openChatList)
        self.ui.pushButton_4.clicked.connect(self.openClPod)

        client_phone = f"+{phone_number[0]} ({phone_number[1:4]}) {phone_number[4:7]}-{phone_number[7:9]}-{phone_number[9:]}"
        self.ui.label_8.setText(client_phone)

        try:
            with connect(
                    host=host,
                    user=user,
                    password=password,
                    database=db_name,
            ) as connection:
                cursor = connection.cursor()
                sql_query = "SELECT idclient FROM client WHERE phone_client = %s"
                cursor.execute(sql_query, (self.phone,))
                result = cursor.fetchone()
                self.client_id = result[0]
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
                sql_query = "SELECT idorder_client, starting_address, final_address, price_order, date, state FROM order_client WHERE id_client = %s"
                cursor.execute(sql_query, (self.client_id,))
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

                    textEdit = QTextEdit(parent=frame)
                    textEdit.setGeometry(QtCore.QRect(152, 0, 131, 81))
                    font = QtGui.QFont()
                    font.setFamily("Istok Web")
                    font.setPointSize(13)
                    textEdit.setFont(font)
                    textEdit.setStyleSheet("color: rgb(140, 153, 169);")
                    textEdit.setText(f"{record[1]}")

                    textEdit = QTextEdit(parent=frame)
                    textEdit.setGeometry(QtCore.QRect(310, 0, 131, 81))
                    font = QtGui.QFont()
                    font.setFamily("Istok Web")
                    font.setPointSize(13)
                    textEdit.setFont(font)
                    textEdit.setStyleSheet("color: rgb(140, 153, 169);")
                    textEdit.setText(f"{record[2]}")

                    label = QLabel(parent=frame)
                    label.setGeometry(QtCore.QRect(470, 0, 91, 21))
                    label.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                        "color: rgb(140, 153, 169);")
                    font = QtGui.QFont()
                    font.setFamily("Istok Web")
                    font.setPointSize(13)
                    font.setWeight(50)
                    label.setFont(font)
                    label.setText(f"{record[3]} ₽")

                    label = QLabel(parent=frame)
                    label.setGeometry(QtCore.QRect(0, 35, 111, 21))
                    label.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                        "color: rgb(140, 153, 169);")
                    label.setFont(font)
                    label.setText(f"{str(record[4]).split()[0]}")

                    label = QLabel(parent=frame)
                    label.setGeometry(QtCore.QRect(0, 60, 111, 21))
                    label.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                        "color: rgb(140, 153, 169);")
                    label.setFont(font)
                    label.setText(f"{str(record[4]).split()[1]}")

                    pushButton = QPushButton(parent=frame)
                    pushButton.setGeometry(QtCore.QRect(0, 0, 541, 91))
                    pushButton.setStyleSheet("color: rgba(13, 22, 23, 0);\n"
                                                  "background-color: rgb(255, 255, 255, 0);")
                    pushButton.setText(f"{record[0]}")
                    if record[-1] == "Завершен":
                        pushButton.clicked.connect(self.clickZak)
                    self.ui.verticalLayout.addWidget(frame)
        except Error as e:
            print(e)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.hideWindow)

    def clickZak(self):
        sender = self.sender()
        self.order = sender.text()
        try:
            with connect(
                    host=host,
                    user=user,
                    password=password,
                    database=db_name,
            ) as connection:
                cursor = connection.cursor()
                sql_query = "SELECT text FROM feedback WHERE id_order = %s"
                cursor.execute(sql_query, (self.order,))
                result = cursor.fetchone()
                if result:
                    self.openZak_2()
                else:
                    self.openZak_1()
        except Error as e:
            print(e)
            self.openZak_1()

    def hideWindow(self):
        self.close()

    def mousePressEvent(self, event):
        self.oldPos = event.globalPosition()

    def mouseMoveEvent(self, event):
        delta = event.globalPosition() - self.oldPos
        self.move(int(self.x() + delta.x()), int(self.y() + delta.y()))
        self.oldPos = event.globalPosition()

    def openZakIstOtz(self):
        self.main_window = ZakClOtzIst(self.phone)
        self.main_window.setGeometry(self.geometry())
        self.main_window.show()
        self.timer.start(20)

    def openChatList(self):
        self.main_window = ClChatList(self.phone)
        self.main_window.setGeometry(self.geometry())
        self.main_window.show()
        self.timer.start(20)

    def openZak(self):
        self.main_window = ZakCl(self.phone)
        self.main_window.setGeometry(self.geometry())
        self.main_window.show()
        self.timer.start(20)

    def openClPod(self):
        self.main_window = Clent_Pod(self.phone)
        self.main_window.setGeometry(self.geometry())
        self.main_window.show()
        self.timer.start(20)

    def openZak_1(self):
        self.main_window = ClIst_1(self.phone, self.order)
        self.main_window.setGeometry(self.geometry())
        self.main_window.show()
        self.timer.start(20)

    def openZak_2(self):
        self.main_window = ClIst_2(self.phone, self.order)
        self.main_window.setGeometry(self.geometry())
        self.main_window.show()
        self.timer.start(20)


class ClIst_1(QMainWindow):
    def __init__(self, phone_number, id_order):
        super().__init__()

        self.ui = Ui_ClientZak_1()
        self.ui.setupUi(self)
        self.phone = phone_number
        self.id_order = id_order
        self.order = id_order
        self.ui.label_10.mousePressEvent = self.openZakIst
        self.ui.pushButton_5.clicked.connect(self.otz)
        self.ui.pushButton_4.clicked.connect(self.openClPod)
        self.ui.pushButton_2.clicked.connect(self.openZakIstOtz)
        self.ui.pushButton.clicked.connect(self.openChatList)
        self.ui.pushButton_6.clicked.connect(self.openZak)

        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)

        client_phone = f"+{phone_number[0]} ({phone_number[1:4]}) {phone_number[4:7]}-{phone_number[7:9]}-{phone_number[9:]}"
        self.ui.label_8.setText(client_phone)
        self.ui.label_27.setText(f"История заказа: #{self.order}")

        try:
            with connect(
                    host=host,
                    user=user,
                    password=password,
                    database=db_name,
            ) as connection:
                cursor = connection.cursor()
                sql_query = "SELECT starting_address, final_address, price_order, id_client, id_work_shift, time, distance FROM order_client WHERE idorder_client = %s"
                cursor.execute(sql_query, (self.id_order,))
                result = cursor.fetchone()
                self.start_adr = result[0]
                self.final_adr = result[1]
                self.price = result[2]
                self.id_client = result[3]
                self.id_work_shift = result[4]
                self.pr_time = result[5]
                self.distance = result[6]
                self.ui.label_31.setText(self.start_adr)
                self.ui.label_32.setText(self.final_adr)
        except Error as e:
            print(e)
        try:
            with connect(
                    host=host,
                    user=user,
                    password=password,
                    database=db_name,
            ) as connection:
                with connection.cursor() as cursor:
                    result_args = cursor.callproc('get_worker_and_car_info', [self.id_work_shift, 0, 0, "", "", ""])
                    self.id_worker = result_args[1]
                    self.id_car = result_args[2]
                    self.new_full_name = result_args[3]
                    self.model_car = result_args[4]
                    self.color_car = result_args[5]
        except Error as e:
            print(e)

        self.ui.label_15.setText(f" • Расстояние: {self.distance} км.")
        self.ui.label_16.setText(f" • Цена: {self.price} ₽")
        self.ui.label_19.setText(f" • Машина: {self.model_car}")
        self.ui.label_20.setText(f" • Гос. номер: {self.id_car}")
        self.ui.label_17.setText(f" • Время ожидания: 5 мин.")
        self.ui.label_18.setText(f" • Примерное время: {self.pr_time} мин.")
        self.ui.label_21.setText(f" • Цвет авто.: {self.color_car}")
        self.ui.label_22.setText(f" • Водитель: {self.new_full_name.split()[0]}")

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.hideWindow)

    def otz(self):
        try:
            with connect(
                    host=host,
                    user=user,
                    password=password,
                    database=db_name,
            ) as connection:
                with connection.cursor() as cursor:
                    args = cursor.callproc('insert_feedback', [self.id_order, self.ui.ocenka, self.ui.textEdit.toPlainText(), self.phone, 0])
                    connection.commit()
                    self.id_order = args[4]
        except Error as e:
            print(e)
        self.openZak_2()

    def mousePressEvent(self, event):
        self.oldPos = event.globalPosition()

    def mouseMoveEvent(self, event):
        delta = event.globalPosition() - self.oldPos
        self.move(int(self.x() + delta.x()), int(self.y() + delta.y()))
        self.oldPos = event.globalPosition()

    def hideWindow(self):
        self.close()

    def openZak_2(self):
        self.main_window = ClIst_2(self.phone, self.order)
        self.main_window.setGeometry(self.geometry())
        self.main_window.show()
        self.timer.start(20)

    def openClPod(self):
        self.main_window = Clent_Pod(self.phone)
        self.main_window.setGeometry(self.geometry())
        self.main_window.show()
        self.timer.start(20)

    def openZakIst(self, event):
        self.main_window = ClIstZak(self.phone)
        self.main_window.setGeometry(self.geometry())
        self.main_window.show()
        self.timer.start(20)

    def openZakIstOtz(self):
        self.main_window = ZakClOtzIst(self.phone)
        self.main_window.setGeometry(self.geometry())
        self.main_window.show()
        self.timer.start(20)

    def openChatList(self):
        self.main_window = ClChatList(self.phone)
        self.main_window.setGeometry(self.geometry())
        self.main_window.show()
        self.timer.start(20)

    def openZak(self):
        self.main_window = ZakCl(self.phone)
        self.main_window.setGeometry(self.geometry())
        self.main_window.show()
        self.timer.start(20)


class ClIst_2(QMainWindow):
    def __init__(self, phone_number, id_order):
        super().__init__()

        self.ui = Ui_ClientZak_2()
        self.ui.setupUi(self)
        self.phone = phone_number
        self.id_order = id_order

        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)

        self.ui.label_10.mousePressEvent = self.openZakIst
        self.ui.pushButton_4.clicked.connect(self.openClPod)
        self.ui.pushButton_2.clicked.connect(self.openZakIstOtz)
        self.ui.pushButton.clicked.connect(self.openChatList)
        self.ui.pushButton_6.clicked.connect(self.openZak)

        client_phone = f"+{phone_number[0]} ({phone_number[1:4]}) {phone_number[4:7]}-{phone_number[7:9]}-{phone_number[9:]}"
        self.ui.label_8.setText(client_phone)
        self.ui.label_27.setText(f"История заказа: #{self.id_order}")

        try:
            with connect(
                    host=host,
                    user=user,
                    password=password,
                    database=db_name,
            ) as connection:
                cursor = connection.cursor()
                sql_query = "SELECT starting_address, final_address, price_order, id_client, id_work_shift, time, distance FROM order_client WHERE idorder_client = %s"
                cursor.execute(sql_query, (self.id_order,))
                result = cursor.fetchone()
                self.start_adr = result[0]
                self.final_adr = result[1]
                self.price = result[2]
                self.id_client = result[3]
                self.id_work_shift = result[4]
                self.pr_time = result[5]
                self.distance = result[6]
                self.ui.label_31.setText(self.start_adr)
                self.ui.label_32.setText(self.final_adr)
        except Error as e:
            print(e)

        try:
            with connect(
                    host=host,
                    user=user,
                    password=password,
                    database=db_name,
            ) as connection:
                with connection.cursor() as cursor:
                    result_args = cursor.callproc('get_worker_and_car_info', [self.id_work_shift, 0, 0, "", "", ""])
                    self.id_worker = result_args[1]
                    self.id_car = result_args[2]
                    self.new_full_name = result_args[3]
                    self.model_car = result_args[4]
                    self.color_car = result_args[5]
        except Error as e:
            print(e)

        self.ui.label_15.setText(f" • Расстояние: {self.distance} км.")
        self.ui.label_16.setText(f" • Цена: {self.price} ₽")
        self.ui.label_19.setText(f" • Машина: {self.model_car}")
        self.ui.label_20.setText(f" • Гос. номер: {self.id_car}")
        self.ui.label_17.setText(f" • Время ожидания: 5 мин.")
        self.ui.label_18.setText(f" • Примерное время: {self.pr_time} мин.")
        self.ui.label_21.setText(f" • Цвет авто.: {self.color_car}")
        self.ui.label_22.setText(f" • Водитель: {self.new_full_name.split()[0]}")

        try:
            with connect(
                    host=host,
                    user=user,
                    password=password,
                    database=db_name,
            ) as connection:
                cursor = connection.cursor()
                sql_query = "SELECT score, text FROM feedback WHERE id_order = %s"
                cursor.execute(sql_query, (self.id_order,))
                records = cursor.fetchone()
                self.score = int(records[0])
                self.text = records[1]
        except Error as e:
            print(e)

        self.ui.textEdit.setText(f"{self.text}")

        if self.score >= 1:
            self.ui.label_11.setText("<html><head/><body><p><img src=\":/zv/zv_on.png\"/></p></body></html>")
            if self.score >= 2:
                self.ui.label_12.setText("<html><head/><body><p><img src=\":/zv/zv_on.png\"/></p></body></html>")
                if self.score >= 3:
                    self.ui.label_13.setText("<html><head/><body><p><img src=\":/zv/zv_on.png\"/></p></body></html>")
                    if self.score >= 4:
                        self.ui.label_25.setText(
                            "<html><head/><body><p><img src=\":/zv/zv_on.png\"/></p></body></html>")
                        if self.score == 5:
                            self.ui.label_26.setText(
                                "<html><head/><body><p><img src=\":/zv/zv_on.png\"/></p></body></html>")

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

    def openZakIst(self, event):
        self.main_window = ClIstZak(self.phone)
        self.main_window.setGeometry(self.geometry())
        self.main_window.show()
        self.timer.start(20)

    def openClPod(self):
        self.main_window = Clent_Pod(self.phone)
        self.main_window.setGeometry(self.geometry())
        self.main_window.show()
        self.timer.start(20)

    def openZakIstOtz(self):
        self.main_window = ZakClOtzIst(self.phone)
        self.main_window.setGeometry(self.geometry())
        self.main_window.show()
        self.timer.start(20)

    def openChatList(self):
        self.main_window = ClChatList(self.phone)
        self.main_window.setGeometry(self.geometry())
        self.main_window.show()
        self.timer.start(20)

    def openZak(self):
        self.main_window = ZakCl(self.phone)
        self.main_window.setGeometry(self.geometry())
        self.main_window.show()
        self.timer.start(20)


class ClChatList(QMainWindow):
    def __init__(self, phone_number):
        super().__init__()

        self.ui = Ui_ClientChatList()
        self.ui.setupUi(self)
        self.phone = phone_number

        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)

        self.ui.pushButton_5.clicked.connect(self.openZak)
        self.ui.pushButton_2.clicked.connect(self.openZakIstOtz)
        self.ui.pushButton_3.clicked.connect(self.openZakIst)
        self.ui.pushButton_4.clicked.connect(self.openClPod)

        client_phone = f"+{phone_number[0]} ({phone_number[1:4]}) {phone_number[4:7]}-{phone_number[7:9]}-{phone_number[9:]}"
        self.ui.label_8.setText(client_phone)

        try:
            with connect(
                    host=host,
                    user=user,
                    password=password,
                    database=db_name,
            ) as connection:
                cursor = connection.cursor()
                sql_query = "SELECT idclient FROM client WHERE phone_client = %s"
                cursor.execute(sql_query, (self.phone,))
                result = cursor.fetchone()
                self.id_client = result[0]
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
                sql_query = "SELECT idchat, id_worker, helper, state FROM chat WHERE id_client = %s"
                cursor.execute(sql_query, (self.id_client,))
                records = cursor.fetchall()
                records.reverse()
                for record in records:
                    if record[3] == "Активен":
                        frame = QFrame(parent=self.ui.scrollAreaWidgetContents)
                        frame.setMinimumSize(QtCore.QSize(0, 100))
                        frame.setStyleSheet("border-radius: 0px;")
                        frame.setFrameShape(QFrame.Shape.StyledPanel)
                        frame.setFrameShadow(QFrame.Shadow.Raised)

                        label = QLabel(parent=frame)
                        label.setGeometry(QtCore.QRect(-2, 60, 551, 16))
                        label.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
                        label.setText("<html><head/><body><p><img src=\":/ico osn/Line 2.png\"/></p></body></html>")

                        label = QLabel(parent=frame)
                        label.setGeometry(QtCore.QRect(0, 0, 131, 21))
                        label.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                            "color: rgb(140, 153, 169);")
                        font = QtGui.QFont()
                        font.setFamily("Istok Web")
                        font.setPointSize(13)
                        font.setWeight(50)
                        label.setFont(font)

                        try:
                            with connect(
                                    host=host,
                                    user=user,
                                    password=password,
                                    database=db_name,
                            ) as connection:
                                cursor = connection.cursor()
                                sql_query = "SELECT name_2, name_3 FROM worker WHERE idworker = %s"
                                cursor.execute(sql_query, (record[1],))
                                result = cursor.fetchone()
                                self.new_full_name = result[0] + " " + result[1]
                        except Error as e:
                            print(e)

                        if record[2] == "Да":
                            label.setText("Поддержка")
                        else:
                            label.setText(f"{self.new_full_name.split()[0]}")

                        textEdit = QTextEdit(parent=frame)
                        textEdit.setGeometry(QtCore.QRect(150, 0, 271, 61))
                        font = QtGui.QFont()
                        font.setFamily("Istok Web")
                        font.setPointSize(13)
                        textEdit.setFont(font)
                        textEdit.setStyleSheet("color: rgb(140, 153, 169);")
                        try:
                            with connect(
                                    host=host,
                                    user=user,
                                    password=password,
                                    database=db_name,
                            ) as connection:
                                cursor = connection.cursor()
                                sql_query = "SELECT text, date_message FROM message WHERE id_chat = %s"
                                cursor.execute(sql_query, (record[0],))
                                r = cursor.fetchall()
                                r.reverse()
                                if len(r) == 0:
                                    message = " "
                                    formatted_time = " "
                                else:
                                    message = r[0][0]
                                    time_part = str(r[0][1]).split()[1]
                                    time_only = time_part.split(":")[:2]
                                    formatted_time = ":".join(time_only)
                        except Error as e:
                            print(e)
                        if len(message) > 45:
                            message = message[:45] + "..."
                        textEdit.setText(f"{message}")

                        label = QLabel(parent=frame)
                        label.setGeometry(QtCore.QRect(465, 0, 71, 21))
                        label.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                            "color: rgb(140, 153, 169);")
                        font = QtGui.QFont()
                        font.setFamily("Istok Web")
                        font.setPointSize(13)
                        font.setWeight(50)
                        label.setFont(font)
                        label.setText(f"{formatted_time}")

                        pushButton = QPushButton(parent=frame)
                        pushButton.setGeometry(QtCore.QRect(0, 0, 541, 61))
                        pushButton.setStyleSheet("color: rgba(13, 22, 23, 0);\n"
                                                      "background-color: rgb(255, 255, 255, 0);")
                        pushButton.setText(f"{record[0]}")
                        pushButton.clicked.connect(self.openClChat)

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

    def openClChat(self):
        sender = self.sender()
        self.main_window = ClChat(self.phone, sender.text(), self.id_client)
        self.main_window.setGeometry(self.geometry())
        self.main_window.show()
        self.timer.start(20)

    def openZak(self):
        self.main_window = ZakCl(self.phone)
        self.main_window.setGeometry(self.geometry())
        self.main_window.show()
        self.timer.start(20)

    def openChatList(self, event):
        self.main_window_1 = ClChatList(self.phone)
        self.main_window_1.setGeometry(self.geometry())
        self.main_window_1.show()
        self.timer.start(20)

    def openZakIstOtz(self):
        self.main_window = ZakClOtzIst(self.phone)
        self.main_window.setGeometry(self.geometry())
        self.main_window.show()
        self.timer.start(20)

    def openZakIst(self):
        self.main_window = ClIstZak(self.phone)
        self.main_window.setGeometry(self.geometry())
        self.main_window.show()
        self.timer.start(20)

    def openClPod(self):
        self.main_window = Clent_Pod(self.phone)
        self.main_window.setGeometry(self.geometry())
        self.main_window.show()
        self.timer.start(20)

    def hideWindow(self):
        self.close()


class ClChat(QMainWindow):
    def __init__(self, phone_number, id_chat, id_client, order=-1):
        super().__init__()
        self.ui = Ui_ClientChat()
        self.ui.setupUi(self)
        self.phone = phone_number
        self.id_chat = id_chat
        self.id_client = id_client
        self.id_order = order

        if self.id_order != -1:
            self.ui.label_10.mousePressEvent = self.openZakCl_2
            self.ui.pushButton_5.clicked.connect(self.openZakCl_2)
        else:
            self.ui.label_10.mousePressEvent = self.openChatList
            self.ui.pushButton_5.clicked.connect(self.openZak)
            self.ui.pushButton_2.clicked.connect(self.openZakIstOtz)
            self.ui.pushButton_3.clicked.connect(self.openZakIst)
            self.ui.pushButton_4.clicked.connect(self.openClPod)

        try:
            with connect(
                    host=host,
                    user=user,
                    password=password,
                    database=db_name,
            ) as connection:
                cursor = connection.cursor()
                sql_query = "SELECT id_worker, helper FROM chat WHERE idchat = %s"
                cursor.execute(sql_query, (self.id_chat,))
                result = cursor.fetchone()
                self.id_worker = result[0]
                self.help = result[1]
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
                sql_query = "SELECT name_2, name_3 FROM worker WHERE idworker = %s"
                cursor.execute(sql_query, (self.id_worker,))
                result = cursor.fetchone()
                self.new_full_name = result[0] + " " + result[1]
        except Error as e:
            print(e)

        if self.help == "Да":
            self.name_work = "Поддержка"
        else:
            self.name_work = self.new_full_name.split()[0]

        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)

        self.ui.label_14.setText(f"Чат: {self.name_work}")
        self.ui.pushButton_6.clicked.connect(self.savemessage)
        client_phone = f"+{phone_number[0]} ({phone_number[1:4]}) {phone_number[4:7]}-{phone_number[7:9]}-{phone_number[9:]}"
        self.ui.label_8.setText(client_phone)
        self.timer_upd = QTimer(self)
        self.timer_upd.timeout.connect(self.update_message)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.hideWindow)
        self.update_message()

    def savemessage(self):
        current_datetime = datetime.now()
        text = self.ui.textEdit.toPlainText()
        self.ui.textEdit.clear()
        if len(text) != 0:
            try:
                with connect(
                        host=host,
                        user=user,
                        password=password,
                        database=db_name,
                ) as connection:
                    with connection.cursor() as cursor:
                        cursor.callproc('insert_message', [self.id_client, current_datetime, text, self.id_chat, 0])
                        connection.commit()
            except Error as e:
                print(e)
            self.update_message()

    def update_message(self):
        children = self.ui.scrollAreaWidgetContents.findChildren(QWidget)
        for child in children:
            child.deleteLater()
        try:
            with connect(
                    host=host,
                    user=user,
                    password=password,
                    database=db_name,
            ) as connection:
                cursor = connection.cursor()
                sql_query = "SELECT sender, text, date_message FROM message WHERE id_chat = %s"
                cursor.execute(sql_query, (self.id_chat,))
                records = cursor.fetchall()
                records.reverse()
                for record in records:
                    frame = QFrame(parent=self.ui.scrollAreaWidgetContents)
                    self.perenos(record[1])
                    sz = 100 + 20 * (self.line)
                    frame.setMinimumSize(QtCore.QSize(0, sz))
                    frame.setStyleSheet("border-radius: 0px;\n"
                                        "border: 0px;")
                    frame.setFrameShape(QFrame.Shape.StyledPanel)
                    frame.setFrameShadow(QFrame.Shadow.Raised)

                    if int(record[0]) == self.id_client:
                        label = QLabel(parent=frame)
                        label.setGeometry(QtCore.QRect(495, 0, 25, 25))
                        label.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
                        label.setText("<html><head/><body><p><img src=\":/chat/img_chat.png\"/></p></body></html>")

                        label = QLabel(parent=frame)
                        label.setGeometry(QtCore.QRect(460, 5, 31, 21))
                        label.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                            "color: rgb(140, 153, 169);")
                        font = QtGui.QFont()
                        font.setFamily("Istok Web")
                        font.setPointSize(12)
                        font.setWeight(50)
                        label.setFont(font)
                        label.setText("Вы")

                        label = QLabel(parent=frame)
                        label.setGeometry(QtCore.QRect(410, 5, 51, 21))
                        label.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                            "color: rgb(140, 153, 169);")
                        font = QtGui.QFont()
                        font.setFamily("Istok Web")
                        font.setPointSize(12)
                        font.setWeight(50)
                        label.setFont(font)
                        time_part = str(record[2]).split()[1]
                        time_only = time_part.split(":")[:2]
                        formatted_time = ":".join(time_only)
                        label.setText(formatted_time)

                        textEdit = QTextEdit(parent=frame)
                        textEdit.setText(f"{record[1]}")
                        size = 35 + 25 * (self.line)
                        textEdit.setGeometry(QtCore.QRect(270, 30, 251, size))
                        font = QtGui.QFont()
                        font.setFamily("Istok Web")
                        font.setPointSize(13)
                        textEdit.setFont(font)
                        textEdit.setStyleSheet(
                            "background-color: rgb(140, 153, 169);\n"
                            "border-radius: 8px;\n"
                            "padding-right: 10px;\n"
                            "padding-left: 10px;\n"
                            "color: rgb(29, 29, 29);")
                    else:
                        label = QLabel(parent=frame)
                        label.setGeometry(QtCore.QRect(0, 0, 25, 25))
                        label.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
                        label.setText("<html><head/><body><p><img src=\":/chat/img_chat.png\"/></p></body></html>")

                        label = QLabel(parent=frame)
                        label.setGeometry(QtCore.QRect(33, 5, 151, 21))
                        label.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                            "color: rgb(140, 153, 169);")
                        font = QtGui.QFont()
                        font.setFamily("Istok Web")
                        font.setPointSize(12)
                        font.setWeight(50)
                        label.setFont(font)
                        label.setText(self.name_work)

                        label = QLabel(parent=frame)
                        label.setGeometry(QtCore.QRect(200, 5, 51, 21))
                        label.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                            "color: rgb(140, 153, 169);")
                        font = QtGui.QFont()
                        font.setFamily("Istok Web")
                        font.setPointSize(12)
                        font.setWeight(50)
                        label.setFont(font)
                        time_part = str(record[2]).split()[1]
                        time_only = time_part.split(":")[:2]
                        formatted_time = ":".join(time_only)
                        label.setText(formatted_time)

                        textEdit = QTextEdit(parent=frame)
                        size = 35 + 25 * (self.line)
                        textEdit.setText(f"{record[1]}")
                        textEdit.setGeometry(QtCore.QRect(0, 30, 251, size))
                        font = QtGui.QFont()
                        font.setFamily("Istok Web")
                        font.setPointSize(13)
                        textEdit.setFont(font)
                        textEdit.setStyleSheet(
                            "background-color: rgb(202, 145, 0);\n"
                            "border-radius: 8px;\n"
                            "padding-right: 10px;\n"
                            "padding-left: 10px;\n"
                            "color: rgb(29, 29, 29);")
                    self.ui.verticalLayout.addWidget(frame)
        except Error as e:
            print(e)
        self.timer_upd.start(1000)

    def perenos(self, text):
        count = 0
        self.line = 0
        for word in text.split():
            count_word = 0
            for i in range(len(word)):
                count += 1
                count_word += 1
                if count == 19:
                    self.line += 1
                    count = count_word
        if self.line > 1:
            self.line -= 1

    def openZakCl_2(self, event=1):
        self.main_window = ZakCl_2(self.phone, self.id_order)
        self.main_window.setGeometry(self.geometry())
        self.main_window.show()
        self.timer.start(20)

    def openZak(self):
        self.main_window = ZakCl(self.phone)
        self.main_window.setGeometry(self.geometry())
        self.main_window.show()
        self.timer.start(20)

    def openChatList(self, event):
        self.main_window_1 = ClChatList(self.phone)
        self.main_window_1.setGeometry(self.geometry())
        self.main_window_1.show()
        self.timer_upd.stop()
        self.timer.start(20)

    def openZakIstOtz(self):
        self.main_window = ZakClOtzIst(self.phone)
        self.main_window.setGeometry(self.geometry())
        self.main_window.show()
        self.timer.start(20)

    def openZakIst(self):
        self.main_window = ClIstZak(self.phone)
        self.main_window.setGeometry(self.geometry())
        self.main_window.show()
        self.timer.start(20)

    def openClPod(self):
        self.main_window = Clent_Pod(self.phone)
        self.main_window.setGeometry(self.geometry())
        self.main_window.show()
        self.timer.start(20)

    def mousePressEvent(self, event):
        self.oldPos = event.globalPosition()

    def mouseMoveEvent(self, event):
        delta = event.globalPosition() - self.oldPos
        self.move(int(self.x() + delta.x()), int(self.y() + delta.y()))
        self.oldPos = event.globalPosition()

    def hideWindow(self):
        self.close()


class Clent_Pod(QMainWindow):
    def __init__(self, phone_number):
        super().__init__()

        self.ui = Ui_ClientPod()
        self.ui.setupUi(self)
        self.phone = phone_number

        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)

        self.ui.pushButton_5.clicked.connect(self.openZak)
        self.ui.pushButton_6.clicked.connect(self.openChatList)
        self.ui.pushButton_2.clicked.connect(self.openZakIstOtz)
        self.ui.pushButton_3.clicked.connect(self.openZakIst)
        self.ui.pushButton_9.clicked.connect(self.openChatPod)

        client_phone = f"+{phone_number[0]} ({phone_number[1:4]}) {phone_number[4:7]}-{phone_number[7:9]}-{phone_number[9:]}"
        self.ui.label_8.setText(client_phone)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.hideWindow)

    def openZak(self):
        self.main_window = ZakCl(self.phone)
        self.main_window.setGeometry(self.geometry())
        self.main_window.show()
        self.timer.start(20)

    def openChatList(self):
        self.main_window_1 = ClChatList(self.phone)
        self.main_window_1.setGeometry(self.geometry())
        self.main_window_1.show()
        self.timer.start(20)

    def openZakIstOtz(self):
        self.main_window = ZakClOtzIst(self.phone)
        self.main_window.setGeometry(self.geometry())
        self.main_window.show()
        self.timer.start(20)

    def openZakIst(self):
        self.main_window = ClIstZak(self.phone)
        self.main_window.setGeometry(self.geometry())
        self.main_window.show()
        self.timer.start(20)

    def openChatPod(self):
        flag = False
        id_chat = 0
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
        try:
            with connect(
                    host=host,
                    user=user,
                    password=password,
                    database=db_name,
            ) as connection:
                cursor = connection.cursor()
                sql_query = "SELECT helper, idchat FROM chat WHERE id_client = %s"
                cursor.execute(sql_query, (self.id_client,))
                result = cursor.fetchall()
                for res in result:
                    if res[0] == "Да":
                        flag = True
                        id_chat = res[1]
                        break
        except Error as e:
            print(e)
        if flag == True:
            self.main_window = ClChat(self.phone, id_chat, self.id_client)
            self.main_window.setGeometry(self.geometry())
            self.main_window.show()
            self.timer.start(20)
        else:
            current_datetime = datetime.now()
            try:
                with connect(
                        host=host,
                        user=user,
                        password=password,
                        database=db_name,
                ) as connection:
                    with connection.cursor() as cursor:
                        args = cursor.callproc('insert_chat', [current_datetime, self.id_client, "Да", "Активен", 1, 0])
                        connection.commit()
                        id_chat = args[5]
            except Error as e:
                print(e)
            self.main_window = ClChat(self.phone, id_chat, self.id_client)
            self.main_window.setGeometry(self.geometry())
            self.main_window.show()
            self.timer.start(20)

    def mousePressEvent(self, event):
        self.oldPos = event.globalPosition()

    def mouseMoveEvent(self, event):
        delta = event.globalPosition() - self.oldPos
        self.move(int(self.x() + delta.x()), int(self.y() + delta.y()))
        self.oldPos = event.globalPosition()

    def hideWindow(self):
        self.close()