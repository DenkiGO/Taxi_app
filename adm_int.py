import cl_int
from datetime import datetime
from interface.admin.admin_int import Ui_AdminInt
from interface.admin.admin_chat_1 import Ui_AdminChat_1
from interface.admin.admin_chat_2 import Ui_AdminChat_2
from interface.admin.admin_car_1 import Ui_AdminCar_1
from interface.admin.admin_car_2 import Ui_AdminCar_2
from interface.admin.admin_car_2_1 import Ui_AdminCar_2_1
from interface.admin.admin_car_3 import Ui_AdminCar_3
from interface.admin.admin_worker import Ui_AdminWorker
from interface.admin.admin_worker_1 import Ui_AdminWorker_1
from interface.admin.admin_worker_2 import Ui_AdminWorker_2
from interface.admin.admin_worker_add import Ui_AdminWorkerAdd
from interface.admin.admin_client_1 import Ui_AdminClient
from interface.admin.admin_order_1 import Ui_AdminOrder
from interface.admin.admin_car_2_2 import Ui_AdminCar_2_2
from interface.admin.admin_otz import Ui_AdminOtz
from mysql.connector import connect, Error
from config import host, user, password, db_name
from PyQt6.QtWidgets import QMainWindow, QLabel, QPushButton, QTextEdit, QFrame, QVBoxLayout, QWidget, QApplication, QSizePolicy
from PyQt6.QtCore import Qt, QPoint, QTimer, QRect
from PyQt6 import QtCore, QtGui
from PyQt6.QtGui import QMouseEvent, QFontMetrics
import random
import image

class Admin(QMainWindow):
    def __init__(self, phone_number):
        super().__init__()
        self.ui = Ui_AdminInt()
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
            self.name = " ".join(parts[1:])
            self.ui.label_8.setText(self.name)
        except Error as e:
            print(e)

        self.ui.pushButton.clicked.connect(self.openAdminChatList)
        self.ui.pushButton_2.clicked.connect(self.openAdCar)
        self.ui.pushButton_3.clicked.connect(self.openAdWorker)
        self.ui.pushButton_4.clicked.connect(self.openAdClient)
        self.ui.pushButton_6.clicked.connect(self.openAdOrder)
        self.ui.pushButton_7.clicked.connect(self.openAdOtz)
        self.ui.pushButton_8.clicked.connect(self.openClientWindow)

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

                        self.ui.verticalLayout.addWidget(frame)
        except Error as e:
            print(e)
        self.timer_upd.start(1000)

    def openClientWindow(self):
        self.client_window = cl_int.ZakCl(self.phone, 1)
        self.client_window.setGeometry(self.geometry())
        self.client_window.show()
        self.timer_upd.stop()
        self.timer.start(20)

    def openAdOtz(self):
        self.main_window = AdOtzList(self.phone, self.name, self.idworker)
        self.main_window.setGeometry(self.geometry())
        self.main_window.show()
        self.timer_upd.stop()
        self.timer.start(20)

    def openAdOrder(self):
        self.main_window = AdOrderList(self.phone, self.name, self.idworker)
        self.main_window.setGeometry(self.geometry())
        self.main_window.show()
        self.timer_upd.stop()
        self.timer.start(20)

    def openAdClient(self):
        self.main_window = AdClientList(self.phone, self.name, self.idworker)
        self.main_window.setGeometry(self.geometry())
        self.main_window.show()
        self.timer_upd.stop()
        self.timer.start(20)

    def openAdWorker(self):
        self.main_window = AdWorkList(self.phone, self.name, self.idworker)
        self.main_window.setGeometry(self.geometry())
        self.main_window.show()
        self.timer_upd.stop()
        self.timer.start(20)

    def openAdCar(self):
        self.main_window = AdmCarList(self.phone, self.name, self.idworker)
        self.main_window.setGeometry(self.geometry())
        self.main_window.show()
        self.timer_upd.stop()
        self.timer.start(20)

    def openAdminChatList(self):
        self.vodila_car_window = AdmChatList(self.phone, self.name, self.idworker)
        self.vodila_car_window.setGeometry(self.geometry())
        self.vodila_car_window.show()
        self.timer_upd.stop()
        self.timer.start(20)

    def hideWindow(self):
        self.close()


class AdmChatList(QMainWindow):
    def __init__(self, phone_number, name, id_worker):
        super().__init__()

        self.idworker = id_worker
        self.name = name
        self.phone = phone_number
        self.ui = Ui_AdminChat_1()
        self.ui.setupUi(self)

        self.ui.label_8.setText(name)

        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        try:
            with connect(
                    host=host,
                    user=user,
                    password=password,
                    database=db_name,
            ) as connection:
                cursor = connection.cursor()
                sql_query = "SELECT idchat, id_client, helper FROM chat WHERE id_worker = %s"
                cursor.execute(sql_query, (self.idworker,))
                records = cursor.fetchall()
                records.reverse()
                for record in records:
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
                    pushButton.clicked.connect(self.openAdChat)

                    self.ui.verticalLayout.addWidget(frame)
        except Error as e:
            print(e)

        self.ui.pushButton.clicked.connect(self.openAdmin)
        self.ui.pushButton_2.clicked.connect(self.openAdCar)
        self.ui.pushButton_3.clicked.connect(self.openAdWorker)
        self.ui.pushButton_4.clicked.connect(self.openAdClient)
        self.ui.pushButton_6.clicked.connect(self.openAdOrder)
        self.ui.pushButton_7.clicked.connect(self.openAdOtz)
        self.ui.pushButton_8.clicked.connect(self.openClientWindow)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.hideWindow)

    def openClientWindow(self):
        self.client_window = cl_int.ZakCl(self.phone, 1)
        self.client_window.setGeometry(self.geometry())
        self.client_window.show()
        self.timer.start(20)

    def openAdOtz(self):
        self.main_window = AdOtzList(self.phone, self.name, self.idworker)
        self.main_window.setGeometry(self.geometry())
        self.main_window.show()
        self.timer.start(20)

    def openAdOrder(self):
        self.main_window = AdOrderList(self.phone, self.name, self.idworker)
        self.main_window.setGeometry(self.geometry())
        self.main_window.show()
        self.timer.start(20)

    def openAdClient(self):
        self.main_window = AdClientList(self.phone, self.name, self.idworker)
        self.main_window.setGeometry(self.geometry())
        self.main_window.show()
        self.timer.start(20)

    def openAdWorker(self):
        self.main_window = AdWorkList(self.phone, self.name, self.idworker)
        self.main_window.setGeometry(self.geometry())
        self.main_window.show()
        self.timer.start(20)

    def openAdCar(self):
        self.main_window = AdmCarList(self.phone, self.name, self.idworker)
        self.main_window.setGeometry(self.geometry())
        self.main_window.show()
        self.timer.start(20)

    def openAdmin(self):
        self.ad_window = Admin(self.phone)
        self.ad_window.setGeometry(self.geometry())
        self.ad_window.show()
        self.timer.start(20)

    def mousePressEvent(self, event):
        self.oldPos = event.globalPosition()

    def mouseMoveEvent(self, event):
        delta = event.globalPosition() - self.oldPos
        self.move(int(self.x() + delta.x()), int(self.y() + delta.y()))
        self.oldPos = event.globalPosition()

    def openAdChat(self):
        sender = self.sender()
        self.main_window = AdminChat(self.phone, self.name, sender.text(), self.idworker)
        self.main_window.setGeometry(self.geometry())
        self.main_window.show()
        self.timer.start(20)

    def hideWindow(self):
        self.close()


class AdminChat(QMainWindow):
    def __init__(self, phone_number, name, id_chat, id_worker, ord=-1):
        super().__init__()

        self.idworker = id_worker
        self.name = name
        self.phone = phone_number
        self.ui = Ui_AdminChat_2()
        self.ui.setupUi(self)
        self.id_chat = id_chat
        self.order = ord

        self.ui.pushButton_10.clicked.connect(self.savemessage)
        self.ui.label_8.setText(name)

        try:
            with connect(
                    host=host,
                    user=user,
                    password=password,
                    database=db_name,
            ) as connection:
                cursor = connection.cursor()
                sql_query = "SELECT id_client, helper FROM chat WHERE id_worker = %s"
                cursor.execute(sql_query, (self.idworker,))
                result = cursor.fetchone()
                self.id_client = result[0]
                self.help = result[1]
        except Error as e:
            print(e)

        self.name_work = "Клиент"

        self.ui.label_10.mousePressEvent = self.openAdminChatList
        self.ui.pushButton.clicked.connect(self.openAdmin)
        self.ui.pushButton_2.clicked.connect(self.openAdCar)
        self.ui.pushButton_3.clicked.connect(self.openAdWorker)
        self.ui.pushButton_4.clicked.connect(self.openAdClient)
        self.ui.pushButton_6.clicked.connect(self.openAdOrder)
        self.ui.pushButton_7.clicked.connect(self.openAdOtz)
        self.ui.pushButton_8.clicked.connect(self.openClientWindow)

        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.timer_upd = QTimer(self)
        self.timer_upd.timeout.connect(self.update_message)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.hideWindow)
        self.update_message()

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
        insert_reviewers_query = """
                INSERT INTO message
                (sender, date_message, text, id_chat)
                VALUES ( %s, %s, %s, %s )
                """
        reviewers_records = [(self.idworker, current_datetime, text, self.id_chat)]
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

                    if int(record[0]) == self.idworker:
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

    def openClientWindow(self):
        self.client_window = cl_int.ZakCl(self.phone, 1)
        self.client_window.setGeometry(self.geometry())
        self.client_window.show()
        self.timer_upd.stop()
        self.timer.start(20)

    def openAdOtz(self):
        self.main_window = AdOtzList(self.phone, self.name, self.idworker)
        self.main_window.setGeometry(self.geometry())
        self.main_window.show()
        self.timer_upd.stop()
        self.timer.start(20)

    def openAdOrder(self):
        self.main_window = AdOrderList(self.phone, self.name, self.idworker)
        self.main_window.setGeometry(self.geometry())
        self.main_window.show()
        self.timer_upd.stop()
        self.timer.start(20)

    def openAdClient(self):
        self.main_window = AdClientList(self.phone, self.name, self.idworker)
        self.main_window.setGeometry(self.geometry())
        self.main_window.show()
        self.timer_upd.stop()
        self.timer.start(20)

    def openAdWorker(self):
        self.main_window = AdWorkList(self.phone, self.name, self.idworker)
        self.main_window.setGeometry(self.geometry())
        self.main_window.show()
        self.timer_upd.stop()
        self.timer.start(20)

    def openAdCar(self):
        self.main_window = AdmCarList(self.phone, self.name, self.idworker)
        self.main_window.setGeometry(self.geometry())
        self.main_window.show()
        self.timer_upd.stop()
        self.timer.start(20)

    def openAdmin(self):
        self.ad_window = Admin(self.phone)
        self.ad_window.setGeometry(self.geometry())
        self.ad_window.show()
        self.timer_upd.stop()
        self.timer.start(20)

    def openAdminChatList(self, event):
        self.vodila_car_window = AdmChatList(self.phone, self.name, self.idworker)
        self.vodila_car_window.setGeometry(self.geometry())
        self.vodila_car_window.show()
        self.timer_upd.stop()
        self.timer.start(20)

    def mousePressEvent(self, event):
        self.oldPos = event.globalPosition()

    def mouseMoveEvent(self, event):
        delta = event.globalPosition() - self.oldPos
        self.move(int(self.x() + delta.x()), int(self.y() + delta.y()))
        self.oldPos = event.globalPosition()

    def hideWindow(self):
        self.close()


class AdmCarList(QMainWindow):
    def __init__(self, phone_number, name, id_worker):
        super().__init__()

        self.idworker = id_worker
        self.name = name
        self.phone = phone_number
        self.ui = Ui_AdminCar_1()
        self.ui.setupUi(self)

        self.ui.label_8.setText(name)

        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        try:
            with connect(
                    host=host,
                    user=user,
                    password=password,
                    database=db_name,
            ) as connection:
                cursor = connection.cursor()
                sql_query = "SELECT * FROM car"
                cursor.execute(sql_query)
                records = cursor.fetchall()
                for record in records:
                    frame = QFrame(parent=self.ui.scrollAreaWidgetContents)
                    frame.setMinimumSize(QtCore.QSize(0, 55))
                    frame.setStyleSheet("border-radius: 0px;")
                    frame.setFrameShape(QFrame.Shape.StyledPanel)
                    frame.setFrameShadow(QFrame.Shadow.Raised)

                    label = QLabel(parent=frame)
                    label.setGeometry(QtCore.QRect(-2, 40, 551, 16))
                    label.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
                    label.setText("<html><head/><body><p><img src=\":/ico osn/Line 2.png\"/></p></body></html>")

                    label = QLabel(parent=frame)
                    label.setGeometry(QtCore.QRect(0, 0, 101, 21))
                    label.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                        "color: rgb(140, 153, 169);")
                    font = QtGui.QFont()
                    font.setFamily("Istok Web")
                    font.setPointSize(13)
                    font.setWeight(50)
                    label.setFont(font)
                    label.setText(f"{record[0]}")

                    label = QLabel(parent=frame)
                    label.setGeometry(QtCore.QRect(133, 0, 151, 21))
                    label.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                        "color: rgb(140, 153, 169);")
                    label.setFont(font)
                    label.setText(f"{record[1]}")

                    label = QLabel(parent=frame)
                    label.setGeometry(QtCore.QRect(300, 0, 91, 21))
                    label.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                        "color: rgb(140, 153, 169);")
                    label.setFont(font)
                    label.setText(f"{record[2]}")

                    label = QLabel(parent=frame)
                    label.setGeometry(QtCore.QRect(445, 0, 91, 21))
                    label.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                        "color: rgb(140, 153, 169);")
                    label.setFont(font)
                    label.setText(f"{record[3]}")

                    pushButton = QPushButton(parent=frame)
                    pushButton.setGeometry(QtCore.QRect(0, 0, 541, 61))
                    pushButton.setStyleSheet("color: rgba(13, 22, 23, 0);\n"
                                             "background-color: rgb(255, 255, 255, 0);")
                    pushButton.setText(f"{record[0]}")
                    pushButton.clicked.connect(self.openAdCar_2)

                    self.ui.verticalLayout.addWidget(frame)
        except Error as e:
            print(e)

        self.ui.pushButton_19.clicked.connect(self.openAddCar)
        self.ui.pushButton_9.clicked.connect(self.openAdService)
        self.ui.pushButton.clicked.connect(self.openAdmin)
        self.ui.pushButton_2.clicked.connect(self.openAdChat)
        self.ui.pushButton_3.clicked.connect(self.openAdWorker)
        self.ui.pushButton_4.clicked.connect(self.openAdClient)
        self.ui.pushButton_6.clicked.connect(self.openAdOrder)
        self.ui.pushButton_7.clicked.connect(self.openAdOtz)
        self.ui.pushButton_8.clicked.connect(self.openClientWindow)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.hideWindow)

    def openAddCar(self):
        self.main_window = AdmCar_2_2(self.phone, self.name, self.idworker)
        self.main_window.setGeometry(self.geometry())
        self.main_window.show()
        self.timer.start(20)

    def openClientWindow(self):
        self.client_window = cl_int.ZakCl(self.phone, 1)
        self.client_window.setGeometry(self.geometry())
        self.client_window.show()
        self.timer.start(20)

    def openAdOtz(self):
        self.main_window = AdOtzList(self.phone, self.name, self.idworker)
        self.main_window.setGeometry(self.geometry())
        self.main_window.show()
        self.timer.start(20)

    def openAdOrder(self):
        self.main_window = AdOrderList(self.phone, self.name, self.idworker)
        self.main_window.setGeometry(self.geometry())
        self.main_window.show()
        self.timer.start(20)

    def openAdClient(self):
        self.main_window = AdClientList(self.phone, self.name, self.idworker)
        self.main_window.setGeometry(self.geometry())
        self.main_window.show()
        self.timer.start(20)

    def openAdWorker(self):
        self.main_window = AdWorkList(self.phone, self.name, self.idworker)
        self.main_window.setGeometry(self.geometry())
        self.main_window.show()
        self.timer.start(20)

    def openAdChat(self):
        self.main_window = AdmChatList(self.phone, self.name, self.idworker)
        self.main_window.setGeometry(self.geometry())
        self.main_window.show()
        self.timer.start(20)

    def openAdmin(self):
        self.ad_window = Admin(self.phone)
        self.ad_window.setGeometry(self.geometry())
        self.ad_window.show()
        self.timer.start(20)

    def openAdService(self):
        self.main_window = AdmCar_2_1(self.phone, self.name, self.idworker)
        self.main_window.setGeometry(self.geometry())
        self.main_window.show()
        self.timer.start(20)

    def openAdCar_2(self):
        sender = self.sender()
        self.main_window = AdmCar_2(self.phone, self.name, self.idworker, sender.text())
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


class AdmCar_2(QMainWindow):
    def __init__(self, phone_number, name, id_worker, id_car):
        super().__init__()

        self.idworker = id_worker
        self.name = name
        self.phone = phone_number
        self.id_car = id_car
        self.ui = Ui_AdminCar_2()
        self.ui.setupUi(self)

        self.ui.label_8.setText(name)

        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)

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

        try:
            with connect(
                    host=host,
                    user=user,
                    password=password,
                    database=db_name,
            ) as connection:
                cursor = connection.cursor()
                sql_query = "SELECT model FROM car WHERE idcar = %s"
                cursor.execute(sql_query, (self.id_car,))
                result = cursor.fetchone()
                self.model = result[0]
        except Error as e:
            print(e)

        self.ui.label_13.setText(f"{self.model}")
        self.ui.label_16.setText(f"{self.id_car}")

        self.ui.pushButton_5.clicked.connect(self.add_serv_car)
        self.ui.pushButton_9.clicked.connect(self.openAdCar_3)
        self.ui.label_20.mousePressEvent = self.openAdCar
        self.ui.pushButton.clicked.connect(self.openAdmin)
        self.ui.pushButton_2.clicked.connect(self.openAdChat)
        self.ui.pushButton_3.clicked.connect(self.openAdWorker)
        self.ui.pushButton_4.clicked.connect(self.openAdClient)
        self.ui.pushButton_6.clicked.connect(self.openAdOrder)
        self.ui.pushButton_7.clicked.connect(self.openAdOtz)
        self.ui.pushButton_8.clicked.connect(self.openClientWindow)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.hideWindow)

    def add_serv_car(self):
        current_datetime = datetime.now()
        price = self.ui.lineEdit.text()
        comment = self.ui.textEdit.toPlainText()
        id_service = self.ui.comboBox.currentText()
        insert_reviewers_query = """
                INSERT INTO service_rendered
                (id_car, id_service, date, price, comment, id_worker)
                VALUES ( %s, %s, %s, %s, %s, %s )
                """
        reviewers_records = [(self.id_car, id_service, current_datetime, price, comment, self.idworker)]
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
        self.ui.lineEdit.clear()
        self.ui.textEdit.clear()

    def openClientWindow(self):
        self.client_window = cl_int.ZakCl(self.phone, 1)
        self.client_window.setGeometry(self.geometry())
        self.client_window.show()
        self.timer.start(20)

    def openAdOtz(self):
        self.main_window = AdOtzList(self.phone, self.name, self.idworker)
        self.main_window.setGeometry(self.geometry())
        self.main_window.show()
        self.timer.start(20)

    def openAdOrder(self):
        self.main_window = AdOrderList(self.phone, self.name, self.idworker)
        self.main_window.setGeometry(self.geometry())
        self.main_window.show()
        self.timer.start(20)

    def openAdClient(self):
        self.main_window = AdClientList(self.phone, self.name, self.idworker)
        self.main_window.setGeometry(self.geometry())
        self.main_window.show()
        self.timer.start(20)

    def openAdWorker(self):
        self.main_window = AdWorkList(self.phone, self.name, self.idworker)
        self.main_window.setGeometry(self.geometry())
        self.main_window.show()
        self.timer.start(20)

    def openAdChat(self):
        self.main_window = AdmChatList(self.phone, self.name, self.idworker)
        self.main_window.setGeometry(self.geometry())
        self.main_window.show()
        self.timer.start(20)

    def openAdmin(self):
        self.ad_window = Admin(self.phone)
        self.ad_window.setGeometry(self.geometry())
        self.ad_window.show()
        self.timer.start(20)

    def openAdCar(self, event):
        self.main_window = AdmCarList(self.phone, self.name, self.idworker)
        self.main_window.setGeometry(self.geometry())
        self.main_window.show()
        self.timer.start(20)

    def openAdCar_3(self):
        self.main_window = AdmCar_3(self.phone, self.name, self.idworker, self.id_car)
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


class AdmCar_2_1(QMainWindow):
    def __init__(self, phone_number, name, id_worker):
        super().__init__()

        self.idworker = id_worker
        self.name = name
        self.phone = phone_number
        self.ui = Ui_AdminCar_2_1()
        self.ui.setupUi(self)

        self.ui.label_8.setText(name)

        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)

        try:
            with connect(
                    host=host,
                    user=user,
                    password=password,
                    database=db_name,
            ) as connection:
                cursor = connection.cursor()
                sql_query = "SELECT idservice, status FROM service"
                cursor.execute(sql_query)
                result = cursor.fetchall()
                for item in result:
                    if str(item[1]) != "1":
                        self.ui.comboBox_2.addItem(item[0])
        except Error as e:
            print(e)

        self.ui.pushButton_11.clicked.connect(self.del_service)
        self.ui.pushButton_10.clicked.connect(self.add_serv)

        self.ui.label_20.mousePressEvent = self.openAdCar
        self.ui.pushButton.clicked.connect(self.openAdmin)
        self.ui.pushButton_2.clicked.connect(self.openAdChat)
        self.ui.pushButton_3.clicked.connect(self.openAdWorker)
        self.ui.pushButton_4.clicked.connect(self.openAdClient)
        self.ui.pushButton_6.clicked.connect(self.openAdOrder)
        self.ui.pushButton_7.clicked.connect(self.openAdOtz)
        self.ui.pushButton_8.clicked.connect(self.openClientWindow)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.hideWindow)

    def add_serv(self):
        try:
            with connect(
                    host=host,
                    user=user,
                    password=password,
                    database=db_name,
            ) as connection:
                cursor = connection.cursor()
                sql_query = "INSERT INTO service (idservice, description, price) VALUES (%s, %s, %s)"
                cursor.execute(sql_query, (self.ui.lineEdit_2.text(), self.ui.textEdit.toPlainText(), self.ui.lineEdit.text()))
                connection.commit()
        except Error as e:
            print(e)
        self.ui.lineEdit_2.clear()
        self.ui.lineEdit.clear()
        self.ui.textEdit.clear()
        self.ui.comboBox_2.clear()
        try:
            with connect(
                    host=host,
                    user=user,
                    password=password,
                    database=db_name,
            ) as connection:
                cursor = connection.cursor()
                sql_query = "SELECT idservice, status FROM service"
                cursor.execute(sql_query)
                result = cursor.fetchall()
                for item in result:
                    if str(item[1]) != "1":
                        self.ui.comboBox_2.addItem(item[0])
        except Error as e:
            print(e)

    def del_service(self):
        ser = self.ui.comboBox_2.currentText()
        try:
            with connect(
                    host=host,
                    user=user,
                    password=password,
                    database=db_name,
            ) as connection:
                cursor = connection.cursor()
                sql_query = "UPDATE service SET status = %s WHERE idservice = %s"
                cursor.execute(sql_query, (1, ser))
                connection.commit()
        except Error as e:
            print(e)
        self.ui.comboBox_2.clear()
        try:
            with connect(
                    host=host,
                    user=user,
                    password=password,
                    database=db_name,
            ) as connection:
                cursor = connection.cursor()
                sql_query = "SELECT idservice, status FROM service"
                cursor.execute(sql_query)
                result = cursor.fetchall()
                for item in result:
                    if str(item[1]) != "1":
                        self.ui.comboBox_2.addItem(item[0])
        except Error as e:
            print(e)

    def openClientWindow(self):
        self.client_window = cl_int.ZakCl(self.phone, 1)
        self.client_window.setGeometry(self.geometry())
        self.client_window.show()
        self.timer.start(20)

    def openAdOtz(self):
        self.main_window = AdOtzList(self.phone, self.name, self.idworker)
        self.main_window.setGeometry(self.geometry())
        self.main_window.show()
        self.timer.start(20)

    def openAdOrder(self):
        self.main_window = AdOrderList(self.phone, self.name, self.idworker)
        self.main_window.setGeometry(self.geometry())
        self.main_window.show()
        self.timer.start(20)

    def openAdClient(self):
        self.main_window = AdClientList(self.phone, self.name, self.idworker)
        self.main_window.setGeometry(self.geometry())
        self.main_window.show()
        self.timer.start(20)

    def openAdWorker(self):
        self.main_window = AdWorkList(self.phone, self.name, self.idworker)
        self.main_window.setGeometry(self.geometry())
        self.main_window.show()
        self.timer.start(20)

    def openAdChat(self):
        self.main_window = AdmChatList(self.phone, self.name, self.idworker)
        self.main_window.setGeometry(self.geometry())
        self.main_window.show()
        self.timer.start(20)

    def openAdmin(self):
        self.ad_window = Admin(self.phone)
        self.ad_window.setGeometry(self.geometry())
        self.ad_window.show()
        self.timer.start(20)

    def openAdCar(self, event):
        self.main_window = AdmCarList(self.phone, self.name, self.idworker)
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


class AdmCar_2_2(QMainWindow):
    def __init__(self, phone_number, name, id_worker):
        super().__init__()

        self.idworker = id_worker
        self.name = name
        self.phone = phone_number
        self.ui = Ui_AdminCar_2_2()
        self.ui.setupUi(self)

        self.ui.label_8.setText(name)

        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)

        self.ui.pushButton_10.clicked.connect(self.add_car)
        self.ui.label_10.mousePressEvent = self.openAdCar

        self.ui.pushButton.clicked.connect(self.openAdmin)
        self.ui.pushButton_2.clicked.connect(self.openAdChat)
        self.ui.pushButton_3.clicked.connect(self.openAdWorker)
        self.ui.pushButton_4.clicked.connect(self.openAdClient)
        self.ui.pushButton_6.clicked.connect(self.openAdOrder)
        self.ui.pushButton_7.clicked.connect(self.openAdOtz)
        self.ui.pushButton_8.clicked.connect(self.openClientWindow)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.hideWindow)

    def add_car(self):
        try:
            with connect(
                    host=host,
                    user=user,
                    password=password,
                    database=db_name,
            ) as connection:
                cursor = connection.cursor()
                sql_query = "INSERT INTO car (idcar, model, color, state) VALUES (%s, %s, %s, %s)"
                cursor.execute(sql_query, (self.ui.lineEdit_3.text(), self.ui.lineEdit_4.text(), self.ui.lineEdit_2.text(), "Свободен"))
                connection.commit()
        except Error as e:
            print(e)
        self.ui.lineEdit_2.clear()
        self.ui.lineEdit_3.clear()
        self.ui.lineEdit_4.clear()

    def openClientWindow(self):
        self.client_window = cl_int.ZakCl(self.phone, 1)
        self.client_window.setGeometry(self.geometry())
        self.client_window.show()
        self.timer.start(20)

    def openAdOtz(self):
        self.main_window = AdOtzList(self.phone, self.name, self.idworker)
        self.main_window.setGeometry(self.geometry())
        self.main_window.show()
        self.timer.start(20)

    def openAdOrder(self):
        self.main_window = AdOrderList(self.phone, self.name, self.idworker)
        self.main_window.setGeometry(self.geometry())
        self.main_window.show()
        self.timer.start(20)

    def openAdClient(self):
        self.main_window = AdClientList(self.phone, self.name, self.idworker)
        self.main_window.setGeometry(self.geometry())
        self.main_window.show()
        self.timer.start(20)

    def openAdWorker(self):
        self.main_window = AdWorkList(self.phone, self.name, self.idworker)
        self.main_window.setGeometry(self.geometry())
        self.main_window.show()
        self.timer.start(20)

    def openAdChat(self):
        self.main_window = AdmChatList(self.phone, self.name, self.idworker)
        self.main_window.setGeometry(self.geometry())
        self.main_window.show()
        self.timer.start(20)

    def openAdmin(self):
        self.ad_window = Admin(self.phone)
        self.ad_window.setGeometry(self.geometry())
        self.ad_window.show()
        self.timer.start(20)

    def openAdCar(self, event):
        self.main_window = AdmCarList(self.phone, self.name, self.idworker)
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


class AdmCar_3(QMainWindow):
    def __init__(self, phone_number, name, id_worker, id_car):
        super().__init__()

        self.idworker = id_worker
        self.name = name
        self.phone = phone_number
        self.id_car = id_car
        self.ui = Ui_AdminCar_3()
        self.ui.setupUi(self)

        self.ui.label_8.setText(name)

        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        try:
            with connect(
                    host=host,
                    user=user,
                    password=password,
                    database=db_name,
            ) as connection:
                with connection.cursor() as cursor:
                    sql_query = "SELECT idservice_rendered, id_service, date, price, comment, id_worker, idservice_rendered FROM service_rendered WHERE id_car = %s"
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
                    label.setGeometry(QtCore.QRect(0, 30, 201, 21))
                    label.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                        "color: rgb(140, 153, 169);")
                    label.setFont(font)
                    label.setText(f"{record[2]}")

                    label = QLabel(parent=frame)
                    label.setGeometry(QtCore.QRect(0, 60, 201, 21))
                    label.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                        "color: rgb(140, 153, 169);")
                    label.setFont(font)
                    try:
                        with connect(
                                host=host,
                                user=user,
                                password=password,
                                database=db_name,
                        ) as connection:
                            cursor = connection.cursor()
                            sql_query = "SELECT full_name_worker FROM worker WHERE idworker = %s"
                            cursor.execute(sql_query, (record[5],))
                            result = cursor.fetchone()
                            full_name_worker = result[0]
                            parts = full_name_worker.split()
                        self.name_1 = " ".join(parts[1:])
                    except Error as e:
                        print(e)
                    label.setText(f"{self.name_1}")

                    textEdit = QTextEdit(parent=frame)
                    textEdit.setGeometry(QtCore.QRect(222, 0, 231, 81))
                    font = QtGui.QFont()
                    font.setFamily("Istok Web")
                    font.setPointSize(13)
                    textEdit.setFont(font)
                    textEdit.setStyleSheet("color: rgb(140, 153, 169);")
                    textEdit.setText(f"{record[4]}")

                    pushButton = QPushButton(parent=frame)
                    pushButton.setGeometry(QtCore.QRect(0, 0, 541, 91))
                    pushButton.setStyleSheet("color: rgba(13, 22, 23, 0);\n"
                                             "background-color: rgb(255, 255, 255, 0);")
                    pushButton.setText(f"{record[6]}")
                    # pushButton.clicked.connect(self.openAdCar_2)

                    self.ui.verticalLayout.addWidget(frame)
        except Error as e:
            print(e)

        self.ui.label_20.mousePressEvent = self.openAdCar
        self.ui.pushButton_2.clicked.connect(self.openAdChat)
        self.ui.pushButton_3.clicked.connect(self.openAdWorker)
        self.ui.pushButton_4.clicked.connect(self.openAdClient)
        self.ui.pushButton_6.clicked.connect(self.openAdOrder)
        self.ui.pushButton_7.clicked.connect(self.openAdOtz)
        self.ui.pushButton_8.clicked.connect(self.openClientWindow)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.hideWindow)

    def openClientWindow(self):
        self.client_window = cl_int.ZakCl(self.phone, 1)
        self.client_window.setGeometry(self.geometry())
        self.client_window.show()
        self.timer.start(20)

    def openAdOtz(self):
        self.main_window = AdOtzList(self.phone, self.name, self.idworker)
        self.main_window.setGeometry(self.geometry())
        self.main_window.show()
        self.timer.start(20)

    def openAdOrder(self):
        self.main_window = AdOrderList(self.phone, self.name, self.idworker)
        self.main_window.setGeometry(self.geometry())
        self.main_window.show()
        self.timer.start(20)

    def openAdClient(self):
        self.main_window = AdClientList(self.phone, self.name, self.idworker)
        self.main_window.setGeometry(self.geometry())
        self.main_window.show()
        self.timer.start(20)

    def openAdWorker(self):
        self.main_window = AdWorkList(self.phone, self.name, self.idworker)
        self.main_window.setGeometry(self.geometry())
        self.main_window.show()
        self.timer.start(20)

    def openAdChat(self):
        self.main_window = AdmChatList(self.phone, self.name, self.idworker)
        self.main_window.setGeometry(self.geometry())
        self.main_window.show()
        self.timer.start(20)

    def openAdmin(self):
        self.ad_window = Admin(self.phone)
        self.ad_window.setGeometry(self.geometry())
        self.ad_window.show()
        self.timer.start(20)

    def openAdCar(self, event):
        self.main_window = AdmCarList(self.phone, self.name, self.idworker)
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


class AdWorkList(QMainWindow):
    def __init__(self, phone_number, name, id_worker):
        super().__init__()

        self.idworker = id_worker
        self.name = name
        self.phone = phone_number
        self.ui = Ui_AdminWorker()
        self.ui.setupUi(self)

        self.ui.label_8.setText(name)

        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        try:
            with connect(
                    host=host,
                    user=user,
                    password=password,
                    database=db_name,
            ) as connection:
                with connection.cursor() as cursor:
                    sql_query = "SELECT * FROM worker"
                    cursor.execute(sql_query)
                    records = cursor.fetchall()
                    records.reverse()
                for record in records:
                    frame = QFrame(parent=self.ui.scrollAreaWidgetContents)
                    frame.setMinimumSize(QtCore.QSize(0, 70))
                    frame.setStyleSheet("border-radius: 0px;")
                    frame.setFrameShape(QFrame.Shape.StyledPanel)
                    frame.setFrameShadow(QFrame.Shadow.Raised)

                    label = QLabel(parent=frame)
                    label.setGeometry(QtCore.QRect(-2, 30, 551, 16))
                    label.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
                    label.setText("<html><head/><body><p><img src=\":/ico osn/Line 2.png\"/></p></body></html>")
                    label = QLabel(parent=frame)
                    label.setGeometry(QtCore.QRect(0, 0, 241, 21))
                    label.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                        "color: rgb(140, 153, 169);")
                    font = QtGui.QFont()
                    font.setFamily("Istok Web")
                    font.setPointSize(13)
                    font.setWeight(50)
                    label.setFont(font)
                    label.setText(f"{record[1]}")
                    label = QLabel(parent=frame)
                    label.setGeometry(QtCore.QRect(250, 0, 151, 21))
                    label.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                        "color: rgb(140, 153, 169);")
                    label.setFont(font)
                    label.setText(f"+{record[2]}")

                    label = QLabel(parent=frame)
                    label.setGeometry(QtCore.QRect(415, 0, 131, 21))
                    label.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                        "color: rgb(140, 153, 169);")
                    label.setFont(font)
                    try:
                        with connect(
                                host=host,
                                user=user,
                                password=password,
                                database=db_name,
                        ) as connection:
                            cursor = connection.cursor()
                            sql_query = "SELECT title_position FROM position WHERE idposition = %s"
                            cursor.execute(sql_query, (record[4],))
                            result1 = cursor.fetchone()
                    except Error as e:
                        print(e)
                    label.setText(f"{result1[0]}")

                    pushButton = QPushButton(parent=frame)
                    pushButton.setGeometry(QtCore.QRect(0, 0, 541, 31))
                    pushButton.setStyleSheet("color: rgba(13, 22, 23, 0);\n"
                                             "background-color: rgb(255, 255, 255, 0);")
                    pushButton.setText(f"{record[0]}")
                    pushButton.clicked.connect(self.openAdWorker_1)

                    self.ui.verticalLayout.addWidget(frame)
        except Error as e:
            print(e)

        self.ui.pushButton_10.clicked.connect(self.openAdWorkerAdd)
        self.ui.pushButton.clicked.connect(self.openAdmin)
        self.ui.pushButton_2.clicked.connect(self.openAdChat)
        self.ui.pushButton_3.clicked.connect(self.openAdCar)
        self.ui.pushButton_4.clicked.connect(self.openAdClient)
        self.ui.pushButton_6.clicked.connect(self.openAdOrder)
        self.ui.pushButton_7.clicked.connect(self.openAdOtz)
        self.ui.pushButton_8.clicked.connect(self.openClientWindow)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.hideWindow)

    def openClientWindow(self):
        self.client_window = cl_int.ZakCl(self.phone, 1)
        self.client_window.setGeometry(self.geometry())
        self.client_window.show()
        self.timer.start(20)

    def openAdOtz(self):
        self.main_window = AdOtzList(self.phone, self.name, self.idworker)
        self.main_window.setGeometry(self.geometry())
        self.main_window.show()
        self.timer.start(20)

    def openAdOrder(self):
        self.main_window = AdOrderList(self.phone, self.name, self.idworker)
        self.main_window.setGeometry(self.geometry())
        self.main_window.show()
        self.timer.start(20)

    def openAdClient(self):
        self.main_window = AdClientList(self.phone, self.name, self.idworker)
        self.main_window.setGeometry(self.geometry())
        self.main_window.show()
        self.timer.start(20)

    def openAdCar(self):
        self.main_window = AdmCarList(self.phone, self.name, self.idworker)
        self.main_window.setGeometry(self.geometry())
        self.main_window.show()
        self.timer.start(20)

    def openAdChat(self):
        self.main_window = AdmChatList(self.phone, self.name, self.idworker)
        self.main_window.setGeometry(self.geometry())
        self.main_window.show()
        self.timer.start(20)

    def openAdmin(self):
        self.ad_window = Admin(self.phone)
        self.ad_window.setGeometry(self.geometry())
        self.ad_window.show()
        self.timer.start(20)

    def openAdWorker_1(self):
        sender = self.sender()
        self.main_window = AdWork_1(self.phone, self.name, self.idworker, sender.text())
        self.main_window.setGeometry(self.geometry())
        self.main_window.show()
        self.timer.start(20)

    def openAdWorkerAdd(self):
        self.main_window = AdWorkAdd(self.phone, self.name, self.idworker)
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


class AdWork_1(QMainWindow):
    def __init__(self, phone_number, name, id_worker, idwork):
        super().__init__()

        self.idworker = id_worker
        self.name = name
        self.phone = phone_number
        self.idwork = idwork
        self.ui = Ui_AdminWorker_1()
        self.ui.setupUi(self)

        self.ui.label_8.setText(name)

        self.ui.pushButton_13.clicked.connect(self.openAdWorker_2)

        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)

        try:
            with connect(
                    host=host,
                    user=user,
                    password=password,
                    database=db_name,
            ) as connection:
                cursor = connection.cursor()
                sql_query = "SELECT * FROM worker WHERE idworker = %s"
                cursor.execute(sql_query, (self.idwork,))
                result = cursor.fetchone()
                self.name_1 = result[1]
                self.phone_wr = result[2]
        except Error as e:
            print(e)

        self.ui.label_16.setText(f"+{self.name_1}")
        self.ui.label_24.setText(f"+{self.phone_wr}")

        self.ui.label_10.mousePressEvent = self.openAdWorker
        self.ui.pushButton.clicked.connect(self.openAdmin)
        self.ui.pushButton_2.clicked.connect(self.openAdChat)
        self.ui.pushButton_3.clicked.connect(self.openAdCar)
        self.ui.pushButton_4.clicked.connect(self.openAdClient)
        self.ui.pushButton_6.clicked.connect(self.openAdOrder)
        self.ui.pushButton_7.clicked.connect(self.openAdOtz)
        self.ui.pushButton_8.clicked.connect(self.openClientWindow)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.hideWindow)

    def openClientWindow(self):
        self.client_window = cl_int.ZakCl(self.phone, 1)
        self.client_window.setGeometry(self.geometry())
        self.client_window.show()
        self.timer.start(20)

    def openAdOtz(self):
        self.main_window = AdOtzList(self.phone, self.name, self.idworker)
        self.main_window.setGeometry(self.geometry())
        self.main_window.show()
        self.timer.start(20)

    def openAdOrder(self):
        self.main_window = AdOrderList(self.phone, self.name, self.idworker)
        self.main_window.setGeometry(self.geometry())
        self.main_window.show()
        self.timer.start(20)

    def openAdClient(self):
        self.main_window = AdClientList(self.phone, self.name, self.idworker)
        self.main_window.setGeometry(self.geometry())
        self.main_window.show()
        self.timer.start(20)

    def openAdCar(self):
        self.main_window = AdmCarList(self.phone, self.name, self.idworker)
        self.main_window.setGeometry(self.geometry())
        self.main_window.show()
        self.timer.start(20)

    def openAdChat(self):
        self.main_window = AdmChatList(self.phone, self.name, self.idworker)
        self.main_window.setGeometry(self.geometry())
        self.main_window.show()
        self.timer.start(20)

    def openAdmin(self):
        self.ad_window = Admin(self.phone)
        self.ad_window.setGeometry(self.geometry())
        self.ad_window.show()
        self.timer.start(20)

    def openAdWorker(self, event):
        self.main_window = AdWorkList(self.phone, self.name, self.idworker)
        self.main_window.setGeometry(self.geometry())
        self.main_window.show()
        self.timer.start(20)

    def openAdWorker_2(self):
        self.main_window = AdWork_2(self.phone, self.name, self.idworker, self.idwork)
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


class AdWork_2(QMainWindow):
    def __init__(self, phone_number, name, id_worker, idwork):
        super().__init__()

        self.id_worker = id_worker
        self.name_worker = name
        self.phone = phone_number
        self.idwork = idwork
        self.ui = Ui_AdminWorker_2()
        self.ui.setupUi(self)

        self.ui.label_8.setText(name)

        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)

        try:
            with connect(
                    host=host,
                    user=user,
                    password=password,
                    database=db_name,
            ) as connection:
                cursor = connection.cursor()
                sql_query = "SELECT * FROM worker WHERE idworker = %s"
                cursor.execute(sql_query, (self.idwork))
                result = cursor.fetchone()
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


class AdWorkAdd(QMainWindow):
    def __init__(self, phone_number, name, id_worker):
        super().__init__()

        self.idworker = id_worker
        self.name = name
        self.phone = phone_number
        self.ui = Ui_AdminWorkerAdd()
        self.ui.setupUi(self)

        self.ui.label_8.setText(name)

        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)

        self.ui.pushButton_10.clicked.connect(self.add_worker)

        self.ui.label_10.mousePressEvent = self.openAdWorker
        self.ui.pushButton.clicked.connect(self.openAdmin)
        self.ui.pushButton_2.clicked.connect(self.openAdChat)
        self.ui.pushButton_3.clicked.connect(self.openAdCar)
        self.ui.pushButton_4.clicked.connect(self.openAdClient)
        self.ui.pushButton_6.clicked.connect(self.openAdOrder)
        self.ui.pushButton_7.clicked.connect(self.openAdOtz)
        self.ui.pushButton_8.clicked.connect(self.openClientWindow)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.hideWindow)

    def add_worker(self):
        number = self.ui.lineEdit.text()
        try:
            with connect(
                    host=host,
                    user=user,
                    password=password,
                    database=db_name,
            ) as connection:
                cursor = connection.cursor()
                sql_query = "SELECT idclient, password_client FROM client WHERE phone_client = %s"
                cursor.execute(sql_query, (number))
                result = cursor.fetchone()
                self.id_cl = result[0]
                self.ps = result[1]
        except Error as e:
            print(e)
        name_1, name_2, name_3 = self.ui.lineEdit_2.text().split()
        try:
            with connect(
                    host=host,
                    user=user,
                    password=password,
                    database=db_name,
            ) as connection:
                cursor = connection.cursor()
                sql_query = "INSERT INTO worker (idworker, name_1, name_2, name_3, phone_worker, password_worker, id_position, active) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
                cursor.execute(sql_query, (self.id_cl, name_1, name_2, name_3, number, self.ps, self.ui.comboBox.currentText(), "Да"))
                connection.commit()
        except Error as e:
            print(e)

    def openClientWindow(self):
        self.client_window = cl_int.ZakCl(self.phone, 1)
        self.client_window.setGeometry(self.geometry())
        self.client_window.show()
        self.timer.start(20)

    def openAdOtz(self):
        self.main_window = AdOtzList(self.phone, self.name, self.idworker)
        self.main_window.setGeometry(self.geometry())
        self.main_window.show()
        self.timer.start(20)

    def openAdOrder(self):
        self.main_window = AdOrderList(self.phone, self.name, self.idworker)
        self.main_window.setGeometry(self.geometry())
        self.main_window.show()
        self.timer.start(20)

    def openAdClient(self):
        self.main_window = AdClientList(self.phone, self.name, self.idworker)
        self.main_window.setGeometry(self.geometry())
        self.main_window.show()
        self.timer.start(20)

    def openAdCar(self):
        self.main_window = AdmCarList(self.phone, self.name, self.idworker)
        self.main_window.setGeometry(self.geometry())
        self.main_window.show()
        self.timer.start(20)

    def openAdChat(self):
        self.main_window = AdmChatList(self.phone, self.name, self.idworker)
        self.main_window.setGeometry(self.geometry())
        self.main_window.show()
        self.timer.start(20)

    def openAdmin(self):
        self.ad_window = Admin(self.phone)
        self.ad_window.setGeometry(self.geometry())
        self.ad_window.show()
        self.timer.start(20)

    def openAdWorker(self, event):
        self.main_window = AdWorkList(self.phone, self.name, self.idworker)
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


class AdClientList(QMainWindow):
    def __init__(self, phone_number, name, id_worker):
        super().__init__()

        self.idworker = id_worker
        self.name = name
        self.phone = phone_number
        self.ui = Ui_AdminClient()
        self.ui.setupUi(self)

        self.ui.label_8.setText(name)

        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        try:
            with connect(
                    host=host,
                    user=user,
                    password=password,
                    database=db_name,
            ) as connection:
                with connection.cursor() as cursor:
                    sql_query = "SELECT * FROM client"
                    cursor.execute(sql_query)
                    records = cursor.fetchall()
                    records.reverse()
                for record in records:
                    frame = QFrame(parent=self.ui.scrollAreaWidgetContents)
                    frame.setMinimumSize(QtCore.QSize(0, 40))
                    frame.setStyleSheet("border-radius: 0px;")
                    frame.setFrameShape(QFrame.Shape.StyledPanel)
                    frame.setFrameShadow(QFrame.Shadow.Raised)

                    label = QLabel(parent=frame)
                    label.setGeometry(QtCore.QRect(-2, 30, 551, 16))
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
                    label.setText(f" #{record[0]}")
                    label = QLabel(parent=frame)
                    label.setGeometry(QtCore.QRect(160, 0, 151, 21))
                    label.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                        "color: rgb(140, 153, 169);")
                    label.setFont(font)
                    label.setText(f"+{record[1]}")

                    pushButton = QPushButton(parent=frame)
                    pushButton.setGeometry(QtCore.QRect(0, 0, 541, 31))
                    pushButton.setStyleSheet("color: rgba(13, 22, 23, 0);\n"
                                             "background-color: rgb(255, 255, 255, 0);")
                    pushButton.setText(f"{record[0]}")
                    # pushButton.clicked.connect(self.openAdWorker_1)

                    self.ui.verticalLayout.addWidget(frame)
        except Error as e:
            print(e)

        self.ui.pushButton.clicked.connect(self.openAdmin)
        self.ui.pushButton_2.clicked.connect(self.openAdChat)
        self.ui.pushButton_3.clicked.connect(self.openAdCar)
        self.ui.pushButton_11.clicked.connect(self.openAdWorker)
        self.ui.pushButton_6.clicked.connect(self.openAdOrder)
        self.ui.pushButton_7.clicked.connect(self.openAdOtz)
        self.ui.pushButton_8.clicked.connect(self.openClientWindow)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.hideWindow)

    def openClientWindow(self):
        self.client_window = cl_int.ZakCl(self.phone, 1)
        self.client_window.setGeometry(self.geometry())
        self.client_window.show()
        self.timer.start(20)

    def openAdOtz(self):
        self.main_window = AdOtzList(self.phone, self.name, self.idworker)
        self.main_window.setGeometry(self.geometry())
        self.main_window.show()
        self.timer.start(20)

    def openAdOrder(self):
        self.main_window = AdOrderList(self.phone, self.name, self.idworker)
        self.main_window.setGeometry(self.geometry())
        self.main_window.show()
        self.timer.start(20)

    def openAdWorker(self):
        self.main_window = AdWorkList(self.phone, self.name, self.idworker)
        self.main_window.setGeometry(self.geometry())
        self.main_window.show()
        self.timer.start(20)

    def openAdCar(self):
        self.main_window = AdmCarList(self.phone, self.name, self.idworker)
        self.main_window.setGeometry(self.geometry())
        self.main_window.show()
        self.timer.start(20)

    def openAdChat(self):
        self.main_window = AdmChatList(self.phone, self.name, self.idworker)
        self.main_window.setGeometry(self.geometry())
        self.main_window.show()
        self.timer.start(20)

    def openAdmin(self):
        self.ad_window = Admin(self.phone)
        self.ad_window.setGeometry(self.geometry())
        self.ad_window.show()
        self.timer.start(20)

    def mousePressEvent(self, event):
        self.oldPos = event.globalPosition()

    def mouseMoveEvent(self, event):
        delta = event.globalPosition() - self.oldPos
        self.move(int(self.x() + delta.x()), int(self.y() + delta.y()))
        self.oldPos = event.globalPosition()

    def hideWindow(self):
        self.close()


class AdOrderList(QMainWindow):
    def __init__(self, phone_number, name, id_worker):
        super().__init__()

        self.idworker = id_worker
        self.name = name
        self.phone = phone_number
        self.ui = Ui_AdminOrder()
        self.ui.setupUi(self)

        self.ui.label_8.setText(name)

        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        try:
            with connect(
                    host=host,
                    user=user,
                    password=password,
                    database=db_name,
            ) as connection:
                with connection.cursor() as cursor:
                    sql_query = "SELECT * FROM order_client"
                    cursor.execute(sql_query)
                    records = cursor.fetchall()
                    records.reverse()
                for record in records:
                    frame = QFrame(parent=self.ui.scrollAreaWidgetContents)
                    frame.setMinimumSize(QtCore.QSize(0, 70))
                    frame.setStyleSheet("border-radius: 0px;")
                    frame.setFrameShape(QFrame.Shape.StyledPanel)
                    frame.setFrameShadow(QFrame.Shadow.Raised)

                    label = QLabel(parent=frame)
                    label.setGeometry(QtCore.QRect(-2, 50, 551, 16))
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
                    label.setText(f"#{record[0]}")
                    label = QLabel(parent=frame)
                    label.setGeometry(QtCore.QRect(160, 0, 151, 21))
                    label.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                        "color: rgb(140, 153, 169);")
                    label.setFont(font)
                    try:
                        with connect(
                                host=host,
                                user=user,
                                password=password,
                                database=db_name,
                        ) as connection:
                            cursor = connection.cursor()
                            sql_query = "SELECT phone_client FROM client WHERE idclient = %s"
                            cursor.execute(sql_query, (record[1],))
                            result_1 = cursor.fetchone()
                            label.setText(f"+{result_1[0]}")
                    except Error as e:
                        print(e)

                    label = QLabel(parent=frame)
                    label.setGeometry(QtCore.QRect(330, 0, 131, 21))
                    label.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                        "color: rgb(140, 153, 169);")
                    label.setFont(font)
                    try:
                        with connect(
                                host=host,
                                user=user,
                                password=password,
                                database=db_name,
                        ) as connection:
                            cursor = connection.cursor()
                            sql_query = "SELECT phone_worker FROM worker WHERE idworker = %s"
                            cursor.execute(sql_query, (record[3],))
                            result_1 = cursor.fetchone()
                            if result_1:
                                label.setText(f"+{result_1[0]}")
                            else:
                                label.setText("Нет")
                    except Error as e:
                        print(e)

                    label = QLabel(parent=frame)
                    label.setGeometry(QtCore.QRect(472, 0, 51, 21))
                    label.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                        "color: rgb(140, 153, 169);")
                    font = QtGui.QFont()
                    font.setFamily("Istok Web")
                    font.setPointSize(13)
                    font.setWeight(50)
                    label.setFont(font)
                    label.setText(f"{record[6]} ₽")

                    label = QLabel(parent=frame)
                    label.setGeometry(QtCore.QRect(0, 30, 191, 21))
                    label.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                        "color: rgb(140, 153, 169);")
                    font = QtGui.QFont()
                    font.setFamily("Istok Web")
                    font.setPointSize(13)
                    font.setWeight(50)
                    label.setFont(font)
                    label.setText(f"{record[8]}")

                    pushButton = QPushButton(parent=frame)
                    pushButton.setGeometry(QtCore.QRect(0, 0, 541, 31))
                    pushButton.setStyleSheet("color: rgba(13, 22, 23, 0);\n"
                                             "background-color: rgb(255, 255, 255, 0);")
                    pushButton.setText(f"{record[0]}")
                    # pushButton.clicked.connect(self.openAdWorker_1)

                    self.ui.verticalLayout.addWidget(frame)
        except Error as e:
            print(e)

        self.ui.pushButton.clicked.connect(self.openAdmin)
        self.ui.pushButton_2.clicked.connect(self.openAdChat)
        self.ui.pushButton_3.clicked.connect(self.openAdCar)
        self.ui.pushButton_11.clicked.connect(self.openAdWorker)
        self.ui.pushButton_10.clicked.connect(self.openAdClient)
        self.ui.pushButton_7.clicked.connect(self.openAdOtz)
        self.ui.pushButton_8.clicked.connect(self.openClientWindow)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.hideWindow)

    def openClientWindow(self):
        self.client_window = cl_int.ZakCl(self.phone, 1)
        self.client_window.setGeometry(self.geometry())
        self.client_window.show()
        self.timer.start(20)

    def openAdOtz(self):
        self.main_window = AdOtzList(self.phone, self.name, self.idworker)
        self.main_window.setGeometry(self.geometry())
        self.main_window.show()
        self.timer.start(20)

    def openAdClient(self):
        self.main_window = AdClientList(self.phone, self.name, self.idworker)
        self.main_window.setGeometry(self.geometry())
        self.main_window.show()
        self.timer.start(20)

    def openAdWorker(self):
        self.main_window = AdWorkList(self.phone, self.name, self.idworker)
        self.main_window.setGeometry(self.geometry())
        self.main_window.show()
        self.timer.start(20)

    def openAdCar(self):
        self.main_window = AdmCarList(self.phone, self.name, self.idworker)
        self.main_window.setGeometry(self.geometry())
        self.main_window.show()
        self.timer.start(20)

    def openAdChat(self):
        self.main_window = AdmChatList(self.phone, self.name, self.idworker)
        self.main_window.setGeometry(self.geometry())
        self.main_window.show()
        self.timer.start(20)

    def openAdmin(self):
        self.ad_window = Admin(self.phone)
        self.ad_window.setGeometry(self.geometry())
        self.ad_window.show()
        self.timer.start(20)

    def mousePressEvent(self, event):
        self.oldPos = event.globalPosition()

    def mouseMoveEvent(self, event):
        delta = event.globalPosition() - self.oldPos
        self.move(int(self.x() + delta.x()), int(self.y() + delta.y()))
        self.oldPos = event.globalPosition()

    def hideWindow(self):
        self.close()


class AdOtzList(QMainWindow):
    def __init__(self, phone_number, name, id_worker):
        super().__init__()
        self.name = name
        self.idworker = id_worker
        self.ui = Ui_AdminOtz()
        self.ui.setupUi(self)
        self.phone = phone_number

        try:
            with connect(
                    host=host,
                    user=user,
                    password=password,
                    database=db_name,
            ) as connection:
                cursor = connection.cursor()
                sql_query = "SELECT order_id, score, text FROM feedback"
                cursor.execute(sql_query)
                records = cursor.fetchall()
                records.reverse()
                for record in records:

                    frame = QFrame(parent=self.ui.scrollAreaWidgetContents_2)
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
                            sql_query = "SELECT date_order FROM order_client WHERE idorder_client  = %s"
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
                    self.ui.verticalLayout_2.addWidget(frame)
        except Error as e:
            print(e)

        self.ui.pushButton.clicked.connect(self.openAdmin)
        self.ui.pushButton_2.clicked.connect(self.openAdChat)
        self.ui.pushButton_3.clicked.connect(self.openAdCar)
        self.ui.pushButton_11.clicked.connect(self.openAdWorker)
        self.ui.pushButton_10.clicked.connect(self.openAdClient)
        self.ui.pushButton_12.clicked.connect(self.openAdOrder)
        self.ui.pushButton_8.clicked.connect(self.openClientWindow)

        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.hideWindow)

    def openClientWindow(self):
        self.client_window = cl_int.ZakCl(self.phone, 1)
        self.client_window.setGeometry(self.geometry())
        self.client_window.show()
        self.timer.start(20)

    def openAdOrder(self):
        self.main_window = AdOrderList(self.phone, self.name, self.idworker)
        self.main_window.setGeometry(self.geometry())
        self.main_window.show()
        self.timer.start(20)

    def openAdClient(self):
        self.main_window = AdClientList(self.phone, self.name, self.idworker)
        self.main_window.setGeometry(self.geometry())
        self.main_window.show()
        self.timer.start(20)

    def openAdWorker(self):
        self.main_window = AdWorkList(self.phone, self.name, self.idworker)
        self.main_window.setGeometry(self.geometry())
        self.main_window.show()
        self.timer.start(20)

    def openAdCar(self):
        self.main_window = AdmCarList(self.phone, self.name, self.idworker)
        self.main_window.setGeometry(self.geometry())
        self.main_window.show()
        self.timer.start(20)

    def openAdChat(self):
        self.main_window = AdmChatList(self.phone, self.name, self.idworker)
        self.main_window.setGeometry(self.geometry())
        self.main_window.show()
        self.timer.start(20)

    def openAdmin(self):
        self.ad_window = Admin(self.phone)
        self.ad_window.setGeometry(self.geometry())
        self.ad_window.show()
        self.timer.start(20)

    def mousePressEvent(self, event):
        self.oldPos = event.globalPosition()

    def mouseMoveEvent(self, event):
        delta = event.globalPosition() - self.oldPos
        self.move(int(self.x() + delta.x()), int(self.y() + delta.y()))
        self.oldPos = event.globalPosition()

    def hideWindow(self):
        self.close()