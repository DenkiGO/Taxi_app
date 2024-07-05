from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QApplication, QMainWindow, QProgressBar, QPushButton, QVBoxLayout, QWidget
from PyQt6.QtCore import Qt, QTimer
import image


class Ui_Client_int_1(object):
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
                                    "    font: bold;\n"
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
                                      "    font: bold;\n"
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
                                        "    font: bold;\n"
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
                                        "    font: bold;\n"
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
                                        "    font: bold;\n"
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
        self.frame_5 = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame_5.setGeometry(QtCore.QRect(219, 96, 604, 557))
        self.frame_5.setStyleSheet("border-radius: 10px;\n"
"background-color: rgb(13, 22, 23);")
        self.frame_5.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_5.setObjectName("frame_5")
        self.progressBar = QtWidgets.QProgressBar(parent=self.frame_5)
        self.progressBar.setGeometry(QtCore.QRect(71, 80, 461, 43))
        self.progressBar.setStyleSheet("QProgressBar {\n"
"    border: 1px solid rgb(140, 153, 169);;\n"
"    border-radius: 8px;\n"
                                       "    font: bold;\n"
"    background-color: rgb(13, 22, 23);\n"
"    color: rgba(13, 22, 23, 0)\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: rgb(202, 145, 0); \n"
"    border-radius: 8px;\n"
"}")
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.progressBar.setMinimum(0)
        self.progressBar.setMaximum(100)
        self.progress_value = 0
        self.pushButton_5 = QtWidgets.QPushButton(parent=self.frame_5)
        self.progressBar.setValue(self.progress_value)
        self.pushButton_5.setGeometry(QtCore.QRect(71, 130, 461, 31))
        font = QtGui.QFont()
        font.setFamily("Istok Web")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("color: rgb(202, 145, 0);\nfont: bold;")
        self.pushButton_5.setObjectName("pushButton_5")

        self.pushButton_6 = QtWidgets.QPushButton(parent=self.frame_5)
        self.pushButton_6.setGeometry(QtCore.QRect(21, 490, 561, 51))
        font = QtGui.QFont()
        font.setFamily("Istok Web")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("QPushButton {\n"
                                        "    border: 0px;\n"
                                        "    font: bold;\n"
                                        "    background-color: rgb(202, 145, 0);\n"
                                        "    border-radius: 10px;\n"
                                        "    color: rgb(29, 29, 29)\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton::pressed {\n"
                                        "    background-color: rgba(202, 145, 0, 200);\n"
                                        "}")
        self.pushButton_6.setObjectName("pushButton_5")
        # self.pushButton_6.clicked.connect(self.start_progress)

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_progress)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.start_progress()

    def start_progress(self):
        self.progress_value = 0
        self.progressBar.setValue(self.progress_value)
        self.timer.start(30)

    def stop_progress(self):
        self.timer.stop()

    def update_progress(self):
        self.progress_value += 1
        if self.progress_value > 100:
            self.progress_value = 0
        self.progressBar.setValue(self.progress_value)

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
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/ico osn/user image.png\"/></p></body></html>"))
        self.label_8.setText(_translate("MainWindow", "+7 (922) 000-00-00"))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/ico osn/rect act.png\"/></p></body></html>"))
        self.label_10.setText(_translate("MainWindow", "Заказать такси"))
        self.pushButton.setText(_translate("MainWindow", "       Чат"))
        self.pushButton_2.setText(_translate("MainWindow", "       Отзывы"))
        self.pushButton_3.setText(_translate("MainWindow", "       История заказов"))
        self.pushButton_4.setText(_translate("MainWindow", "       Помощь"))
        self.pushButton_5.setText(_translate("MainWindow", "Ищем машину"))
        self.pushButton_6.setText(_translate("MainWindow", "Отменить заказ"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Client_int_1()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
