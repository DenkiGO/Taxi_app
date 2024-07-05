from interface.vodila.vodila_int import Ui_VodilaInt
from interface.vodila.vodila_ist_obsl import Ui_VodCar
from interface.vodila.vodila_ist_obsl_ist import Ui_VodCarIst
from interface.vodila.vodila_int_on import Ui_VodilaInt_on
from interface.vodila.vodila_chat_1 import Ui_VodChatList
from interface.vodila.vodila_chat_2 import Ui_VodChat
from interface.vodila.vodila_ist_zak import Ui_VodIstZak
from interface.vodila.vodila_ist_zak_1 import Ui_VodIstZak_1
from interface.vodila.vodila_pod import Ui_VodilaPod
from interface.vodila.vodila_otz_ist import Ui_VodilaOtz
from datetime import datetime
from mysql.connector import connect, Error
from config import host, user, password, db_name
from PyQt6.QtWidgets import QMainWindow, QLabel, QPushButton, QTextEdit, QFrame, QVBoxLayout, QWidget, QApplication
from PyQt6.QtCore import Qt, QPoint, QTimer
from PyQt6 import QtCore, QtGui
from PyQt6.QtGui import QMouseEvent
import random
import image

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
                sql_query = "SELECT idworker, name_2, name_3 FROM worker WHERE phone_worker = %s"
                cursor.execute(sql_query, (self.phone,))
                result = cursor.fetchone()
                self.idworker = result[0]
                self.new_full_name = result[1] + " " + result[2]
            self.ui.label_8.setText(self.new_full_name)
        except Error as e:
            print(e)

        self.ui.pushButton_4.clicked.connect(self.openClientWindow)
        self.ui.pushButton_6.clicked.connect(self.openVodilaPod)
        self.ui.pushButton_2.clicked.connect(self.openVodilaCarWindow)
        self.ui.pushButton_3.clicked.connect(self.openVodilaZakIst)
        self.ui.pushButton.clicked.connect(self.openVodilaChatList)
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

    def openClientWindow(self):
        from cl_int import ZakCl
        self.client_window = ZakCl(self.phone, 1)
        self.client_window.setGeometry(self.geometry())
        self.client_window.show()
        self.timer.start(20)

    def openVodilaPod(self):
        self.vodila_car_window = VodPod(self.phone, self.new_full_name, self.idworker)
        self.vodila_car_window.setGeometry(self.geometry())
        self.vodila_car_window.show()
        self.timer.start(20)

    def openVodilaZakIst(self):
        self.vodila_car_window = VodIstZak(self.phone, self.new_full_name, self.idworker)
        self.vodila_car_window.setGeometry(self.geometry())
        self.vodila_car_window.show()
        self.timer.start(20)

    def openVodilaCarWindow(self):
        self.vodila_car_window = Vodila_Car(self.phone, self.new_full_name, self.idworker)
        self.vodila_car_window.setGeometry(self.geometry())
        self.vodila_car_window.show()
        self.timer.start(20)

    def openVodilaChatList(self):
        self.vodila_car_window = VodChatList(self.phone, self.new_full_name, self.idworker)
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
                sql_query = "SELECT idwork_shift FROM work_shift WHERE id_worker = %s"
                cursor.execute(sql_query, (self.idworker,))
                result = cursor.fetchone()
                self.id_work_shift = result[0]
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
                    cursor.callproc('update_order_worker', [sender.text(), "Выполнение", self.id_work_shift, self.list_check[int(sender.text())][0], self.list_check[int(sender.text())][1]])
                    connection.commit()
        except Error as e:
            print(e)

        self.vodila_car_window = VodilaIntOn(self.phone, sender.text())
        self.vodila_car_window.setGeometry(self.geometry())
        self.vodila_car_window.show()
        self.timer.start(30)


class VodilaIntOn(QMainWindow):
    def __init__(self, phone_number, idorder):
        super().__init__()
        self.ui = Ui_VodilaInt_on()
        self.ui.setupUi(self)
        self.phone = phone_number
        self.id_order = idorder

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

        self.ui.pushButton_9.clicked.connect(self.compliOrder)
        self.ui.pushButton_5.clicked.connect(self.openChatVod)

        self.ui.label_15.setText(f" • Расстояние: {self.distance} км.")
        self.ui.label_16.setText(f" • Цена: {self.price} ₽")
        self.ui.label_19.setText(f" • Машина: {self.model_car}")
        self.ui.label_20.setText(f" • Гос. номер: {self.id_car}")
        self.ui.label_17.setText(f" • Время ожидания: 5 мин.")
        self.ui.label_18.setText(f" • Примерное время: {self.pr_time} мин.")
        self.ui.label_21.setText(f" • Цвет авто.: {self.color_car}")
        self.ui.label_22.setText(f" • Водитель: {self.new_full_name.split()[0]}")
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.timer_upd = QTimer(self)
        self.timer_upd.timeout.connect(self.updateOrder)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.hideWindow)
        self.updateOrder()

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
                sql_query = "SELECT id_client, idchat, state FROM chat WHERE id_worker = %s"
                cursor.execute(sql_query, (self.id_worker,))
                result = cursor.fetchall()
                for res in result:
                    if str(res[0]) == str(self.id_client):
                        flag = True
                        id_chat = res[1]
                        if res[2] != "Активен":
                            cursor.callproc('update_chat_status', [id_chat, "Активен"])
                        break
        except Error as e:
            print(e)
        if flag == True:
            self.main_window = VodilaChat(self.phone, self.new_full_name, id_chat, self.id_worker, self.id_order)
            self.main_window.setGeometry(self.geometry())
            self.main_window.show()
            self.timer_upd.stop()
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
            self.main_window = VodilaChat(self.phone, self.new_full_name, id_chat, self.id_worker, self.id_order)
            self.main_window.setGeometry(self.geometry())
            self.main_window.show()
            self.timer_upd.stop()
            self.timer.start(20)

    def updateOrder(self):
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
                    if records[0] == "Отменен":
                        try:
                            with connect(
                                    host=host,
                                    user=user,
                                    password=password,
                                    database=db_name,
                            ) as connection:
                                cursor = connection.cursor()
                                sql_query = "SELECT id_client, idchat, state FROM chat WHERE id_worker = %s"
                                cursor.execute(sql_query, (self.id_worker,))
                                result = cursor.fetchall()
                                for res in result:
                                    if str(res[0]) == str(self.id_client):
                                        id_chat = res[1]
                                        if res[2] == "Активен":
                                            cursor.callproc('update_chat_status', [id_chat, "Закрыт"])
                                        break
                        except Error as e:
                            print(e)
                        self.openVodilaWindow()
                    else:
                        self.timer_upd.start(100)
        except Error as e:
            print(e)

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
        self.timer_upd.stop()
        self.timer.start(20)

    def compliOrder(self):
        try:
            with connect(
                    host=host,
                    user=user,
                    password=password,
                    database=db_name,
            ) as connection:
                with connection.cursor() as cursor:
                    cursor.callproc('update_order_state', [self.id_order, "Завершен"])
                    connection.commit()
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
                sql_query = "SELECT id_client, idchat, state FROM chat WHERE id_worker = %s"
                cursor.execute(sql_query, (self.id_worker,))
                result = cursor.fetchall()
                for res in result:
                    if str(res[0]) == str(self.id_client):
                        id_chat = res[1]
                        if res[2] == "Активен":
                            cursor.callproc('update_chat_status', [id_chat, "Закрыт"])
                            connection.commit()
                        break
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
        self.ui.pushButton.clicked.connect(self.openVodilaChatList)
        self.ui.pushButton_3.clicked.connect(self.openVodilaZakIst)
        self.ui.pushButton_4.clicked.connect(self.openClientWindow)
        self.ui.pushButton_6.clicked.connect(self.openVodilaPod)
        try:
            with connect(
                    host=host,
                    user=user,
                    password=password,
                    database=db_name,
            ) as connection:
                cursor = connection.cursor()
                sql_query = "SELECT idwork_shift, state FROM work_shift WHERE id_worker = %s"
                cursor.execute(sql_query, (self.id_worker,))
                result = cursor.fetchall()
                for res in result:
                    if res[1] == "Свободен":
                        self.id_work_shift = res[0]
                        break
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

    def openVodilaZakIst(self):
        self.vodila_car_window = VodIstZak(self.phone, self.name_worker, self.id_worker)
        self.vodila_car_window.setGeometry(self.geometry())
        self.vodila_car_window.show()
        self.timer.start(20)

    def openVodilaPod(self):
        self.vodila_car_window = VodPod(self.phone, self.name_worker, self.id_worker)
        self.vodila_car_window.setGeometry(self.geometry())
        self.vodila_car_window.show()
        self.timer.start(20)

    def openClientWindow(self):
        from cl_int import ZakCl
        self.client_window = ZakCl(self.phone, 1)
        self.client_window.setGeometry(self.geometry())
        self.client_window.show()
        self.timer.start(20)

    def openVodilaChatList(self):
        self.vodila_car_window = VodChatList(self.phone, self.name_worker, self.id_worker)
        self.vodila_car_window.setGeometry(self.geometry())
        self.vodila_car_window.show()
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
        try:
            with connect(
                    host=host,
                    user=user,
                    password=password,
                    database=db_name,
            ) as connection:
                with connection.cursor() as cursor:
                    cursor.callproc('insert_service_rendered', [self.id_car, id_service, current_datetime, price, comment, self.id_worker])
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
        self.ui.pushButton.clicked.connect(self.openVodilaChatList)
        self.ui.pushButton_3.clicked.connect(self.openVodilaZakIst)
        self.ui.pushButton_4.clicked.connect(self.openClientWindow)
        self.ui.pushButton_6.clicked.connect(self.openVodilaPod)

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

    def openVodilaZakIst(self):
        self.vodila_car_window = VodIstZak(self.phone, self.name, self.id_worker)
        self.vodila_car_window.setGeometry(self.geometry())
        self.vodila_car_window.show()
        self.timer.start(20)

    def openVodilaPod(self):
        self.vodila_car_window = VodPod(self.phone, self.name, self.id_worker)
        self.vodila_car_window.setGeometry(self.geometry())
        self.vodila_car_window.show()
        self.timer.start(20)

    def openClientWindow(self):
        from cl_int import ZakCl
        self.client_window = ZakCl(self.phone, 1)
        self.client_window.setGeometry(self.geometry())
        self.client_window.show()
        self.timer.start(20)

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

    def openVodilaChatList(self):
        self.vodila_car_window = VodChatList(self.phone, self.name, self.id_worker)
        self.vodila_car_window.setGeometry(self.geometry())
        self.vodila_car_window.show()
        self.timer.start(20)


class VodChatList(QMainWindow):
    def __init__(self, phone_number, name, id_worker):
        super().__init__()

        self.id_worker = id_worker
        self.name_worker = name
        self.phone = phone_number
        self.ui = Ui_VodChatList()
        self.ui.setupUi(self)

        self.ui.label_8.setText(name)

        self.ui.pushButton_9.clicked.connect(self.openVodilaWindow)
        self.ui.pushButton_2.clicked.connect(self.openVodilaCarWindow)
        self.ui.pushButton_3.clicked.connect(self.openVodilaZakIst)
        self.ui.pushButton_4.clicked.connect(self.openClientWindow)
        self.ui.pushButton_6.clicked.connect(self.openVodilaPod)

        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        try:
            with connect(
                    host=host,
                    user=user,
                    password=password,
                    database=db_name,
            ) as connection:
                cursor = connection.cursor()
                sql_query = "SELECT idchat, id_client, helper, state FROM chat WHERE id_worker = %s"
                cursor.execute(sql_query, (self.id_worker,))
                records = cursor.fetchall()
                records.reverse()
                for record in records:
                    if record[-1] == "Активен":
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

                        if record[2] == "Да":
                            label.setText("Поддержка")
                        else:
                            label.setText(f"Клиент")

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

    def openVodilaZakIst(self):
        self.vodila_car_window = VodIstZak(self.phone, self.name_worker, self.id_worker)
        self.vodila_car_window.setGeometry(self.geometry())
        self.vodila_car_window.show()
        self.timer.start(20)

    def openVodilaPod(self):
        self.vodila_car_window = VodPod(self.phone, self.name_worker, self.id_worker)
        self.vodila_car_window.setGeometry(self.geometry())
        self.vodila_car_window.show()
        self.timer.start(20)

    def openClientWindow(self):
        from cl_int import ZakCl
        self.client_window = ZakCl(self.phone, 1)
        self.client_window.setGeometry(self.geometry())
        self.client_window.show()
        self.timer.start(20)

    def openVodilaCarWindow(self):
        self.vodila_car_window = Vodila_Car(self.phone, self.name_worker, self.id_worker)
        self.vodila_car_window.setGeometry(self.geometry())
        self.vodila_car_window.show()
        self.timer.start(20)

    def openVodilaWindow(self):
        self.vodila_window = Vodila(self.phone)
        self.vodila_window.setGeometry(self.geometry())
        self.vodila_window.show()
        self.timer.start(20)

    def openClChat(self):
        sender = self.sender()
        self.main_window = VodilaChat(self.phone, self.name_worker, sender.text(), self.id_worker)
        self.main_window.setGeometry(self.geometry())
        self.main_window.show()
        self.timer.start(20)

    def hideWindow(self):
        self.close()


class VodilaChat(QMainWindow):
    def __init__(self, phone_number, name, id_chat, id_worker, ord=-1):
        super().__init__()

        self.id_worker = id_worker
        self.name_worker = name
        self.phone = phone_number
        self.ui = Ui_VodChat()
        self.ui.setupUi(self)
        self.id_chat = id_chat
        self.order = ord

        self.ui.pushButton_10.clicked.connect(self.savemessage)
        self.ui.label_8.setText(name)

        if str(ord) != "-1":
            self.ui.label_10.mousePressEvent = self.openZakVod_1
            self.ui.pushButton_9.clicked.connect(self.openZakVod)
        else:
            self.ui.label_10.mousePressEvent = self.openVodilaChatList
            self.ui.pushButton_9.clicked.connect(self.openVodilaWindow)
            self.ui.pushButton_2.clicked.connect(self.openVodilaCarWindow)
            self.ui.pushButton_3.clicked.connect(self.openVodilaZakIst)
            self.ui.pushButton_4.clicked.connect(self.openClientWindow)
            self.ui.pushButton_6.clicked.connect(self.openVodilaPod)

        try:
            with connect(
                    host=host,
                    user=user,
                    password=password,
                    database=db_name,
            ) as connection:
                cursor = connection.cursor()
                sql_query = "SELECT id_client, helper FROM chat WHERE idchat = %s"
                cursor.execute(sql_query, (self.id_chat,))
                result = cursor.fetchone()
                self.id_client = result[0]
                self.help = result[1]
        except Error as e:
            print(e)

        if self.help == "Да":
            self.name_work = "Поддержка"
        else:
            self.name_work = "Клиент"

        self.ui.label_14.setText(f"Чат: {self.name_work}")

        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.timer_upd = QTimer(self)
        self.timer_upd.timeout.connect(self.update_message)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.hideWindow)
        self.update_message()

    def openZakVod_1(self, event):
        self.vodila_car_window = VodilaIntOn(self.phone, self.order)
        self.vodila_car_window.setGeometry(self.geometry())
        self.vodila_car_window.show()
        self.timer.start(30)

    def openZakVod(self):
        self.vodila_car_window = VodilaIntOn(self.phone, self.order)
        self.vodila_car_window.setGeometry(self.geometry())
        self.vodila_car_window.show()
        self.timer.start(30)

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

    def savemessage(self):
        current_datetime = datetime.now()
        text = self.ui.textEdit.toPlainText()
        self.ui.textEdit.clear()
        try:
            with connect(
                    host=host,
                    user=user,
                    password=password,
                    database=db_name,
            ) as connection:
                with connection.cursor() as cursor:
                    cursor.callproc('insert_message', [self.id_worker, current_datetime, text, self.id_chat, 0])
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

                    if int(record[0]) == self.id_worker:
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
                        textEdit.setText(f"{record[1]}")
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

    def openVodilaZakIst(self):
        self.vodila_car_window = VodIstZak(self.phone, self.name_worker, self.id_worker)
        self.vodila_car_window.setGeometry(self.geometry())
        self.vodila_car_window.show()
        self.timer.start(20)

    def openVodilaPod(self):
        self.vodila_car_window = VodPod(self.phone, self.name_worker, self.id_worker)
        self.vodila_car_window.setGeometry(self.geometry())
        self.vodila_car_window.show()
        self.timer.start(20)

    def openClientWindow(self):
        from cl_int import ZakCl
        self.client_window = ZakCl(self.phone, 1)
        self.client_window.setGeometry(self.geometry())
        self.client_window.show()
        self.timer.start(20)

    def openVodilaCarWindow(self):
        self.vodila_car_window = Vodila_Car(self.phone, self.name_worker, self.id_worker)
        self.vodila_car_window.setGeometry(self.geometry())
        self.vodila_car_window.show()
        self.timer.start(20)

    def openVodilaChatList(self, event):
        self.vodila_car_window = VodChatList(self.phone, self.name_worker, self.id_worker)
        self.vodila_car_window.setGeometry(self.geometry())
        self.vodila_car_window.show()
        self.timer.start(20)

    def openVodilaWindow(self):
        self.vodila_window = Vodila(self.phone)
        self.vodila_window.setGeometry(self.geometry())
        self.vodila_window.show()
        self.timer.start(20)

    def mousePressEvent(self, event):
        self.oldPos = event.globalPosition()

    def mouseMoveEvent(self, event):
        delta = event.globalPosition() - self.oldPos
        self.move(int(self.x() + delta.x()), int(self.y() + delta.y()))
        self.oldPos = event.globalPosition()

    def hideWindow(self):
        self.close()


class VodIstZak(QMainWindow):
    def __init__(self, phone_number, name, id_worker):
        super().__init__()
        self.id_worker = id_worker
        self.name_worker = name
        self.ui = Ui_VodIstZak()
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
                sql_query = "SELECT idwork_shift FROM work_shift WHERE id_worker = %s"
                cursor.execute(sql_query, (self.id_worker,))
                self.list_shift_work = []
                records = cursor.fetchall()
                for res in records:
                    self.list_shift_work.append(res[0])
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
                sql_query = "SELECT idorder_client, starting_address, final_address, price_order, date, id_work_shift FROM order_client"
                cursor.execute(sql_query)
                records = cursor.fetchall()
                records.reverse()
                for record in records:
                    if record[-1] in self.list_shift_work:
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
                        pushButton.clicked.connect(self.openZak_1)
                        self.ui.verticalLayout.addWidget(frame)
        except Error as e:
            print(e)

        self.ui.pushButton_9.clicked.connect(self.openVodilaWindow)
        self.ui.pushButton.clicked.connect(self.openVodilaChatList)
        self.ui.pushButton_2.clicked.connect(self.openVodilaCarWindow)
        self.ui.pushButton_4.clicked.connect(self.openClientWindow)
        self.ui.pushButton_6.clicked.connect(self.openVodilaPod)

        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.hideWindow)

    def openVodilaZakIst(self):
        self.vodila_car_window = VodIstZak(self.phone, self.name_worker, self.id_worker)
        self.vodila_car_window.setGeometry(self.geometry())
        self.vodila_car_window.show()
        self.timer.start(20)

    def openVodilaPod(self):
        self.vodila_car_window = VodPod(self.phone, self.name_worker, self.id_worker)
        self.vodila_car_window.setGeometry(self.geometry())
        self.vodila_car_window.show()
        self.timer.start(20)

    def openClientWindow(self):
        from cl_int import ZakCl
        self.client_window = ZakCl(self.phone, 1)
        self.client_window.setGeometry(self.geometry())
        self.client_window.show()
        self.timer.start(20)

    def openVodilaCarWindow(self):
        self.vodila_car_window = Vodila_Car(self.phone, self.name_worker, self.id_worker)
        self.vodila_car_window.setGeometry(self.geometry())
        self.vodila_car_window.show()
        self.timer.start(20)

    def openVodilaChatList(self):
        self.vodila_car_window = VodChatList(self.phone, self.name_worker, self.id_worker)
        self.vodila_car_window.setGeometry(self.geometry())
        self.vodila_car_window.show()
        self.timer.start(20)

    def openVodilaWindow(self):
        self.vodila_window = Vodila(self.phone)
        self.vodila_window.setGeometry(self.geometry())
        self.vodila_window.show()
        self.timer.start(20)

    def openZak_1(self):
        sender = self.sender()
        self.order = sender.text()
        self.main_window = VodZak_1(self.phone, self.name_worker, self.id_worker, self.order)
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


class VodZak_1(QMainWindow):
    def __init__(self, phone_number, name, id_worker, order_1):
        super().__init__()
        self.id_worker = id_worker
        self.name_worker = name
        self.ui = Ui_VodIstZak_1()
        self.ui.setupUi(self)
        self.phone = phone_number
        self.id_order = order_1
        self.list_check = {}

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
                if records:
                    self.score = int(records[0])
                    self.text = records[1]
                    self.ui.textEdit.setText(f"{self.text}")

                    if self.score >= 1:
                        self.ui.label_12.setText(
                            "<html><head/><body><p><img src=\":/zv/zv_on.png\"/></p></body></html>")
                        if self.score >= 2:
                            self.ui.label_13.setText(
                                "<html><head/><body><p><img src=\":/zv/zv_on.png\"/></p></body></html>")
                            if self.score >= 3:
                                self.ui.label_25.setText(
                                    "<html><head/><body><p><img src=\":/zv/zv_on.png\"/></p></body></html>")
                                if self.score >= 4:
                                    self.ui.label_26.setText(
                                        "<html><head/><body><p><img src=\":/zv/zv_on.png\"/></p></body></html>")
                                    if self.score == 5:
                                        self.ui.label_33.setText(
                                            "<html><head/><body><p><img src=\":/zv/zv_on.png\"/></p></body></html>")
                else:
                    self.ui.textEdit.clear()
        except Error as e:
            print(e)

        self.ui.label_10.mousePressEvent = self.openVodilaZakIst
        self.ui.pushButton_9.clicked.connect(self.openVodilaWindow)
        self.ui.pushButton.clicked.connect(self.openVodilaChatList)
        self.ui.pushButton_2.clicked.connect(self.openVodilaCarWindow)
        self.ui.pushButton_4.clicked.connect(self.openClientWindow)
        self.ui.pushButton_6.clicked.connect(self.openVodilaPod)

        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.hideWindow)

    def openVodilaZakIst(self, event):
        self.vodila_car_window = VodIstZak(self.phone, self.name_worker, self.id_worker)
        self.vodila_car_window.setGeometry(self.geometry())
        self.vodila_car_window.show()
        self.timer.start(20)

    def openVodilaPod(self):
        self.vodila_car_window = VodPod(self.phone, self.name_worker, self.id_worker)
        self.vodila_car_window.setGeometry(self.geometry())
        self.vodila_car_window.show()
        self.timer.start(20)

    def openClientWindow(self):
        from cl_int import ZakCl
        self.client_window = ZakCl(self.phone, 1)
        self.client_window.setGeometry(self.geometry())
        self.client_window.show()
        self.timer.start(20)

    def openVodilaCarWindow(self):
        self.vodila_car_window = Vodila_Car(self.phone, self.name_worker, self.id_worker)
        self.vodila_car_window.setGeometry(self.geometry())
        self.vodila_car_window.show()
        self.timer.start(20)

    def openVodilaChatList(self):
        self.vodila_car_window = VodChatList(self.phone, self.name_worker, self.id_worker)
        self.vodila_car_window.setGeometry(self.geometry())
        self.vodila_car_window.show()
        self.timer.start(20)

    def openVodilaWindow(self):
        self.vodila_window = Vodila(self.phone)
        self.vodila_window.setGeometry(self.geometry())
        self.vodila_window.show()
        self.timer.start(20)

    def mousePressEvent(self, event):
        self.oldPos = event.globalPosition()

    def mouseMoveEvent(self, event):
        delta = event.globalPosition() - self.oldPos
        self.move(int(self.x() + delta.x()), int(self.y() + delta.y()))
        self.oldPos = event.globalPosition()

    def hideWindow(self):
        self.close()


class VodPod(QMainWindow):
    def __init__(self, phone_number, name, id_worker):
        super().__init__()
        self.name_worker = name
        self.id_worker = id_worker
        self.ui = Ui_VodilaPod()
        self.ui.setupUi(self)
        self.phone = phone_number

        self.ui.pushButton_11.clicked.connect(self.openChatPod)
        self.ui.pushButton_4.clicked.connect(self.openClientWindow)
        self.ui.pushButton_5.clicked.connect(self.openVodilaZakIst)
        self.ui.pushButton_2.clicked.connect(self.openVodilaCarWindow)
        self.ui.pushButton.clicked.connect(self.openVodilaChatList)
        self.ui.pushButton_9.clicked.connect(self.openVodilaWindow)

        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.hideWindow)

    def openChatPod(self):
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
                sql_query = "SELECT helper, idchat FROM chat WHERE id_client = %s"
                cursor.execute(sql_query, (self.id_worker,))
                result = cursor.fetchall()
                for res in result:
                    if res[0] == "Да":
                        flag = True
                        id_chat = res[1]
                        break
        except Error as e:
            print(e)
        if flag == True:
            self.main_window = VodilaChat(self.phone, self.name_worker, id_chat, self.id_worker)
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
                        args = cursor.callproc('insert_chat', [current_datetime, self.id_worker, "Да", "Активен", 1, 0])
                        connection.commit()
                        id_chat = args[5]
            except Error as e:
                print(e)
            self.main_window = VodilaChat(self.phone, self.name_worker, id_chat, self.id_worker)
            self.main_window.setGeometry(self.geometry())
            self.main_window.show()
            self.timer.start(20)

    def openVodilaCarWindow(self):
        self.vodila_car_window = Vodila_Car(self.phone, self.name_worker, self.id_worker)
        self.vodila_car_window.setGeometry(self.geometry())
        self.vodila_car_window.show()
        self.timer.start(20)

    def openClientWindow(self):
        from cl_int import ZakCl
        self.client_window = ZakCl(self.phone, 1)
        self.client_window.setGeometry(self.geometry())
        self.client_window.show()
        self.timer.start(20)

    def openVodilaZakIst(self):
        self.vodila_car_window = VodIstZak(self.phone, self.name_worker, self.id_worker)
        self.vodila_car_window.setGeometry(self.geometry())
        self.vodila_car_window.show()
        self.timer.start(20)

    def openVodilaChatList(self):
        self.vodila_car_window = VodChatList(self.phone, self.name_worker, self.id_worker)
        self.vodila_car_window.setGeometry(self.geometry())
        self.vodila_car_window.show()
        self.timer.start(20)

    def openVodilaWindow(self):
        self.vodila_window = Vodila(self.phone)
        self.vodila_window.setGeometry(self.geometry())
        self.vodila_window.show()
        self.timer.start(20)

    def mousePressEvent(self, event):
        self.oldPos = event.globalPosition()

    def mouseMoveEvent(self, event):
        delta = event.globalPosition() - self.oldPos
        self.move(int(self.x() + delta.x()), int(self.y() + delta.y()))
        self.oldPos = event.globalPosition()

    def hideWindow(self):
        self.close()

