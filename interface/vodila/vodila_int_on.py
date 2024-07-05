from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QApplication
from PyQt6.QtCore import Qt
import image


class Ui_VodilaInt_on(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(830, 660)
        MainWindow.setStyleSheet("background-color: rgb(36, 36, 36);")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 830, 90))
        self.frame.setStyleSheet("background-color: rgba(9, 19, 21, 202);")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(parent=self.frame)
        self.label.setGeometry(QtCore.QRect(796, 11, 21, 16))
        self.label.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.label.setObjectName("label")
        self.label.setCursor(Qt.CursorShape.PointingHandCursor)
        self.label.setMouseTracking(True)
        self.label.mousePressEvent = self.exit
        self.label_2 = QtWidgets.QLabel(parent=self.frame)
        self.label_2.setGeometry(QtCore.QRect(761, 10, 21, 16))
        self.label_2.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.label_2.setObjectName("label_2")
        self.label_2.setCursor(Qt.CursorShape.PointingHandCursor)
        self.label_2.setMouseTracking(True)
        self.label_3 = QtWidgets.QLabel(parent=self.frame)
        self.label_3.setGeometry(QtCore.QRect(48, 43, 131, 41))
        self.label_3.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=self.frame)
        self.label_4.setGeometry(QtCore.QRect(789, 50, 21, 21))
        self.label_4.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(parent=self.frame)
        self.label_5.setGeometry(QtCore.QRect(774, 40, 16, 51))
        self.label_5.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(parent=self.frame)
        self.label_6.setGeometry(QtCore.QRect(740, 53, 21, 21))
        self.label_6.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(parent=self.frame)
        self.label_7.setGeometry(QtCore.QRect(680, 40, 41, 41))
        self.label_7.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(parent=self.frame)
        self.label_8.setGeometry(QtCore.QRect(510, 45, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Istok Web")
        font.setPointSize(13)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(140, 153, 169);")
        self.label_8.setObjectName("label_8")
        self.frame_2 = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(0, 90, 212, 570))
        self.frame_2.setStyleSheet("background-color: rgba(9, 19, 21, 202);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_9 = QtWidgets.QLabel(parent=self.frame_2)
        self.label_9.setGeometry(QtCore.QRect(0, 57, 211, 61))
        self.label_9.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(parent=self.frame_2)
        self.label_10.setGeometry(QtCore.QRect(40, 70, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Istok Web")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                    "   font: bold;\n"
"color: rgb(29, 29, 29);")
        self.label_10.setObjectName("label_10")
        self.pushButton = QtWidgets.QPushButton(parent=self.frame_2)
        self.pushButton.setGeometry(QtCore.QRect(0, 115, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Istok Web")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton {\n"
"    color: rgb(140, 153, 169);\n"
"    border: 0px;\n"
                                      "   font: bold;\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"    text-align: left;\n"
"}\n"
"\n"
"QPushButton::pressed {\n"
"    background-color: rgb(202, 145, 0);\n"
"    color: rgb(29, 29, 29);\n"
"    border-bottom-right-radius: 10px;\n"
"    border-top-right-radius: 10px;\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.frame_2)
        self.pushButton_2.setGeometry(QtCore.QRect(0, 160, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Istok Web")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton {\n"
"    color: rgb(140, 153, 169);\n"
"    border: 0px;\n"
                                        "   font: bold;\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"    text-align: left;\n"
"}\n"
"\n"
"QPushButton::pressed {\n"
"    background-color: rgb(202, 145, 0);\n"
"    color: rgb(29, 29, 29);\n"
"    border-bottom-right-radius: 10px;\n"
"    border-top-right-radius: 10px;\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.frame_2)
        self.pushButton_3.setGeometry(QtCore.QRect(0, 205, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Istok Web")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("QPushButton {\n"
"    color: rgb(140, 153, 169);\n"
"    border: 0px;\n"
                                        "   font: bold;\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"    text-align: left;\n"
"}\n"
"\n"
"QPushButton::pressed {\n"
"    background-color: rgb(202, 145, 0);\n"
"    color: rgb(29, 29, 29);\n"
"    border-bottom-right-radius: 10px;\n"
"    border-top-right-radius: 10px;\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(parent=self.frame_2)
        self.pushButton_4.setGeometry(QtCore.QRect(0, 250, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Istok Web")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("QPushButton {\n"
"    color: rgb(140, 153, 169);\n"
"    border: 0px;\n"
                                        "   font: bold;\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"    text-align: left;\n"
"}\n"
"\n"
"QPushButton::pressed {\n"
"    background-color: rgb(202, 145, 0);\n"
"    color: rgb(29, 29, 29);\n"
"    border-bottom-right-radius: 10px;\n"
"    border-top-right-radius: 10px;\n"
"}")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_6 = QtWidgets.QPushButton(parent=self.frame_2)
        self.pushButton_6.setGeometry(QtCore.QRect(0, 295, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Istok Web")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("QPushButton {\n"
"    color: rgb(140, 153, 169);\n"
"    border: 0px;\n"
                                        "   font: bold;\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"    text-align: left;\n"
"}\n"
"\n"
"QPushButton::pressed {\n"
"    background-color: rgb(202, 145, 0);\n"
"    color: rgb(29, 29, 29);\n"
"    border-bottom-right-radius: 10px;\n"
"    border-top-right-radius: 10px;\n"
"}")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(parent=self.frame_2)
        self.pushButton_7.setGeometry(QtCore.QRect(0, 340, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Istok Web")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet("QPushButton {\n"
"    color: rgb(140, 153, 169);\n"
"    border: 0px;\n"
                                        "   font: bold;\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"    text-align: left;\n"
"}\n"
"\n"
"QPushButton::pressed {\n"
"    background-color: rgb(202, 145, 0);\n"
"    color: rgb(29, 29, 29);\n"
"    border-bottom-right-radius: 10px;\n"
"    border-top-right-radius: 10px;\n"
"}")
        self.pushButton_7.setObjectName("pushButton_7")
        self.frame_3 = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(219, 96, 299, 84))
        self.frame_3.setStyleSheet("border-radius: 10px;\n"
"background-color: rgb(13, 22, 23);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label_12 = QtWidgets.QLabel(parent=self.frame_3)
        self.label_12.setGeometry(QtCore.QRect(16, 7, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Istok Web")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                    "   font: bold;\n"
"color: rgb(140, 153, 169);")
        self.label_12.setObjectName("label_12")
        self.label_23 = QtWidgets.QLabel(parent=self.frame_3)
        self.label_23.setGeometry(QtCore.QRect(16, 33, 261, 21))
        font = QtGui.QFont()
        font.setFamily("Istok Web")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_23.setFont(font)
        self.label_23.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(140, 153, 169);")
        self.label_23.setObjectName("label_23")
        self.frame_4 = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame_4.setGeometry(QtCore.QRect(524, 96, 299, 84))
        self.frame_4.setStyleSheet("border-radius: 10px;\n"
"background-color: rgb(13, 22, 23);")
        self.frame_4.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_4.setObjectName("frame_4")
        self.label_13 = QtWidgets.QLabel(parent=self.frame_4)
        self.label_13.setGeometry(QtCore.QRect(16, 7, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Istok Web")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                    "   font: bold;\n"
"color: rgb(140, 153, 169);")
        self.label_13.setObjectName("label_13")
        self.label_24 = QtWidgets.QLabel(parent=self.frame_4)
        self.label_24.setGeometry(QtCore.QRect(16, 33, 261, 21))
        font = QtGui.QFont()
        font.setFamily("Istok Web")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_24.setFont(font)
        self.label_24.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(140, 153, 169);")
        self.label_24.setObjectName("label_24")
        self.frame_5 = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame_5.setGeometry(QtCore.QRect(219, 186, 604, 161))
        self.frame_5.setStyleSheet("border-radius: 10px;\n"
"background-color: rgb(13, 22, 23);")
        self.frame_5.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_5.setObjectName("frame_5")
        self.label_14 = QtWidgets.QLabel(parent=self.frame_5)
        self.label_14.setGeometry(QtCore.QRect(16, 7, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Istok Web")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                    "   font: bold;\n"
"color: rgb(140, 153, 169);")
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(parent=self.frame_5)
        self.label_15.setGeometry(QtCore.QRect(16, 35, 231, 21))
        font = QtGui.QFont()
        font.setFamily("Istok Web")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(140, 153, 169);")
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(parent=self.frame_5)
        self.label_16.setGeometry(QtCore.QRect(16, 65, 231, 21))
        font = QtGui.QFont()
        font.setFamily("Istok Web")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(140, 153, 169);")
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(parent=self.frame_5)
        self.label_17.setGeometry(QtCore.QRect(322, 35, 231, 21))
        font = QtGui.QFont()
        font.setFamily("Istok Web")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_17.setFont(font)
        self.label_17.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(140, 153, 169);")
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(parent=self.frame_5)
        self.label_18.setGeometry(QtCore.QRect(322, 65, 231, 21))
        font = QtGui.QFont()
        font.setFamily("Istok Web")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_18.setFont(font)
        self.label_18.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(140, 153, 169);")
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(parent=self.frame_5)
        self.label_19.setGeometry(QtCore.QRect(16, 95, 231, 21))
        font = QtGui.QFont()
        font.setFamily("Istok Web")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_19.setFont(font)
        self.label_19.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(140, 153, 169);")
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(parent=self.frame_5)
        self.label_20.setGeometry(QtCore.QRect(16, 125, 231, 21))
        font = QtGui.QFont()
        font.setFamily("Istok Web")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_20.setFont(font)
        self.label_20.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(140, 153, 169);")
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(parent=self.frame_5)
        self.label_21.setGeometry(QtCore.QRect(322, 95, 231, 21))
        font = QtGui.QFont()
        font.setFamily("Istok Web")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_21.setFont(font)
        self.label_21.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(140, 153, 169);")
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(parent=self.frame_5)
        self.label_22.setGeometry(QtCore.QRect(322, 125, 231, 21))
        font = QtGui.QFont()
        font.setFamily("Istok Web")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_22.setFont(font)
        self.label_22.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(140, 153, 169);")
        self.label_22.setObjectName("label_22")
        self.label_11 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(219, 353, 611, 238))
        self.label_11.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"border-radius-bottom-right: 10px;")
        self.label_11.setObjectName("label_11")
        self.pushButton_5 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(219, 600, 299, 51))
        font = QtGui.QFont()
        font.setFamily("Istok Web")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("QPushButton {\n"
"    border: 0px;\n"
"    background-color: rgb(202, 145, 0);\n"
                                        "   font: bold;\n"
"    border-radius: 10px;\n"
"    color: rgb(29, 29, 29)\n"
"}\n"
"\n"
"QPushButton::pressed {\n"
"    background-color: rgba(202, 145, 0, 200);\n"
"}")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_9 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(524, 600, 299, 51))
        font = QtGui.QFont()
        font.setFamily("Istok Web")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setStyleSheet("QPushButton {\n"
"    border: 0px;\n"
"    background-color: rgb(202, 145, 0);\n"
                                        "   font: bold;\n"
"    border-radius: 10px;\n"
"    color: rgb(29, 29, 29)\n"
"}\n"
"\n"
"QPushButton::pressed {\n"
"    background-color: rgba(202, 145, 0, 200);\n"
"}")
        self.pushButton_9.setObjectName("pushButton_9")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def exit(self, event):
        QApplication.quit()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/ico main/ico exit.png\"/></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/ico main/ico sve.png\"/></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/logo/TAXI.png\"/></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/ico osn/ico col.png\"/></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/ico osn/Line 1.png\"/></p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/ico osn/ico str.png\"/></p></body></html>"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/ico osn/vodila im.png\"/></p></body></html>"))
        self.label_8.setText(_translate("MainWindow", "Роман Валерьевич"))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/ico osn/rect act.png\"/></p></body></html>"))
        self.label_10.setText(_translate("MainWindow", "Активные заказы"))
        self.pushButton.setText(_translate("MainWindow", "       Чат"))
        self.pushButton_2.setText(_translate("MainWindow", "       О машине"))
        self.pushButton_3.setText(_translate("MainWindow", "       История заказов"))
        self.pushButton_4.setText(_translate("MainWindow", "       Заказать такси"))
        self.pushButton_6.setText(_translate("MainWindow", "       Помощь"))
        self.pushButton_7.setText(_translate("MainWindow", "       Отзывы"))
        self.label_12.setText(_translate("MainWindow", "Откуда:"))
        self.label_23.setText(_translate("MainWindow", "ул. Мечникова, 81"))
        self.label_13.setText(_translate("MainWindow", "Куда:"))
        self.label_24.setText(_translate("MainWindow", "ул. Волкова, 8/1"))
        self.label_14.setText(_translate("MainWindow", "Детали заказа:"))
        self.label_15.setText(_translate("MainWindow", " • Расстояние: 2 км."))
        self.label_16.setText(_translate("MainWindow", " • Цена: 348 ₽"))
        self.label_17.setText(_translate("MainWindow", " • Время ожидания: 5 мин."))
        self.label_18.setText(_translate("MainWindow", " • Примерное время: 38 мин."))
        self.label_19.setText(_translate("MainWindow", " • Машина: LADA VESTA"))
        self.label_20.setText(_translate("MainWindow", " • Гос. номер: А000АА 196"))
        self.label_21.setText(_translate("MainWindow", " • Цвет авто.: Белый"))
        self.label_22.setText(_translate("MainWindow", " • Водитель: Алексей"))
        self.label_11.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/map/img map 2.png\"/></p></body></html>"))
        self.pushButton_5.setText(_translate("MainWindow", "Чат с клиентом"))
        self.pushButton_9.setText(_translate("MainWindow", "Завершить заказ"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_VodilaInt_on()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
