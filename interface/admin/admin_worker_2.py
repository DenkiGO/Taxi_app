from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QApplication
from PyQt6.QtCore import Qt
import image


class Ui_AdminWorker_2(object):
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
        self.label_9.setGeometry(QtCore.QRect(0, 191, 211, 61))
        self.label_9.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.label_9.setObjectName("label_9")
        self.pushButton = QtWidgets.QPushButton(parent=self.frame_2)
        self.pushButton.setGeometry(QtCore.QRect(0, 70, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Istok Web")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton {\n"
"    color: rgb(140, 153, 169);\n"
                                      "    font: bold;\n"
"    border: 0px;\n"
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
        self.pushButton_2.setGeometry(QtCore.QRect(0, 115, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Istok Web")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton {\n"
"    color: rgb(140, 153, 169);\n"
                                        "    font: bold;\n"
"    border: 0px;\n"
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
        self.pushButton_3.setGeometry(QtCore.QRect(0, 160, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Istok Web")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("QPushButton {\n"
"    color: rgb(140, 153, 169);\n"
                                        "    font: bold;\n"
"    border: 0px;\n"
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
                                        "    font: bold;\n"
"    border: 0px;\n"
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
                                        "    font: bold;\n"
"    border: 0px;\n"
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
                                        "    font: bold;\n"
"    border: 0px;\n"
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
        self.pushButton_8 = QtWidgets.QPushButton(parent=self.frame_2)
        self.pushButton_8.setGeometry(QtCore.QRect(0, 385, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Istok Web")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setStyleSheet("QPushButton {\n"
"    color: rgb(140, 153, 169);\n"
                                        "    font: bold;\n"
"    border: 0px;\n"
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
        self.pushButton_8.setObjectName("pushButton_8")
        self.label_18 = QtWidgets.QLabel(parent=self.frame_2)
        self.label_18.setGeometry(QtCore.QRect(40, 205, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Istok Web")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                    "    font: bold;\n"
"color: rgb(29, 29, 29);")
        self.label_18.setObjectName("label_18")
        self.frame_5 = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame_5.setGeometry(QtCore.QRect(219, 96, 604, 557))
        self.frame_5.setStyleSheet("border-radius: 10px;\n"
"background-color: rgb(13, 22, 23);")
        self.frame_5.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_5.setObjectName("frame_5")
        self.label_16 = QtWidgets.QLabel(parent=self.frame_5)
        self.label_16.setGeometry(QtCore.QRect(28, 10, 331, 31))
        font = QtGui.QFont()
        font.setFamily("Istok Web")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                    "    font: bold;\n"
"color: rgb(140, 153, 169);")
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(parent=self.frame_5)
        self.label_17.setGeometry(QtCore.QRect(28, 35, 551, 16))
        self.label_17.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.label_17.setObjectName("label_17")
        self.label_10 = QtWidgets.QLabel(parent=self.frame_5)
        self.label_10.setGeometry(QtCore.QRect(551, 20, 16, 16))
        self.label_10.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.label_10.setObjectName("label_10")
        self.label_19 = QtWidgets.QLabel(parent=self.frame_5)
        self.label_19.setGeometry(QtCore.QRect(28, 50, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Istok Web")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_19.setFont(font)
        self.label_19.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                    "    font: bold;\n"
"color: rgb(140, 153, 169);")
        self.label_19.setObjectName("label_19")
        self.lineEdit = QtWidgets.QLineEdit(parent=self.frame_5)
        self.lineEdit.setGeometry(QtCore.QRect(28, 80, 251, 35))
        font = QtGui.QFont()
        font.setFamily("Istok Web")
        font.setPointSize(13)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("color: rgb(140, 153, 169);\n"
"border-radius: 8px;\n"
"border: 1px solid rgb(140, 153, 169);\n"
"padding-left: 5px;")
        self.lineEdit.setObjectName("lineEdit")
        self.label_20 = QtWidgets.QLabel(parent=self.frame_5)
        self.label_20.setGeometry(QtCore.QRect(330, 50, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Istok Web")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_20.setFont(font)
        self.label_20.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                    "    font: bold;\n"
"color: rgb(140, 153, 169);")
        self.label_20.setObjectName("label_20")
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=self.frame_5)
        self.lineEdit_2.setGeometry(QtCore.QRect(330, 80, 241, 35))
        font = QtGui.QFont()
        font.setFamily("Istok Web")
        font.setPointSize(13)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("color: rgb(140, 153, 169);\n"
"border-radius: 8px;\n"
"border: 1px solid rgb(140, 153, 169);\n"
"padding-left: 5px;")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_21 = QtWidgets.QLabel(parent=self.frame_5)
        self.label_21.setGeometry(QtCore.QRect(28, 130, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Istok Web")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_21.setFont(font)
        self.label_21.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                    "    font: bold;\n"
"color: rgb(140, 153, 169);")
        self.label_21.setObjectName("label_21")
        self.lineEdit_3 = QtWidgets.QLineEdit(parent=self.frame_5)
        self.lineEdit_3.setGeometry(QtCore.QRect(28, 160, 251, 35))
        font = QtGui.QFont()
        font.setFamily("Istok Web")
        font.setPointSize(13)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setStyleSheet("color: rgb(140, 153, 169);\n"
"border-radius: 8px;\n"
"border: 1px solid rgb(140, 153, 169);\n"
"padding-left: 5px;")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_22 = QtWidgets.QLabel(parent=self.frame_5)
        self.label_22.setGeometry(QtCore.QRect(28, 200, 551, 16))
        self.label_22.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(parent=self.frame_5)
        self.label_23.setGeometry(QtCore.QRect(28, 210, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Istok Web")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_23.setFont(font)
        self.label_23.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                    "    font: bold;\n"
"color: rgb(140, 153, 169);")
        self.label_23.setObjectName("label_23")
        self.comboBox = QtWidgets.QComboBox(parent=self.frame_5)
        self.comboBox.setGeometry(QtCore.QRect(28, 240, 251, 35))
        font = QtGui.QFont()
        font.setFamily("Istok Web")
        font.setPointSize(13)
        self.comboBox.setFont(font)
        self.comboBox.setStyleSheet("QComboBox {\n"
"    border: 1px solid rgb(140, 153, 169);\n"
"    border-radius: 8px;\n"
"    color: rgb(140, 153, 169);\n"
"    text-align: center;\n"
"}\n"
"QComboBox::drop-down {\n"
"    border: 0px;\n"
"}\n"
"QComboBox::down-arrow {\n"
"    image: url(:/ico osn/ico str.png);\n"
"    margin-right: 15px;\n"
"}\n"
"QComboBox::on {\n"
"    border: 1px solid rgb(140, 153, 169)\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"    border: 1px solid rgb(140, 153, 169);\n"
"    selection-background-color: rgb(140, 153, 169);\n"
"    color: rgb(140, 153, 169);\n"
"    padding-left: 5px;\n"
"}")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_24 = QtWidgets.QLabel(parent=self.frame_5)
        self.label_24.setGeometry(QtCore.QRect(330, 210, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Istok Web")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_24.setFont(font)
        self.label_24.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                    "    font: bold;\n"
"color: rgb(140, 153, 169);")
        self.label_24.setObjectName("label_24")
        self.comboBox_2 = QtWidgets.QComboBox(parent=self.frame_5)
        self.comboBox_2.setGeometry(QtCore.QRect(330, 240, 241, 35))
        font = QtGui.QFont()
        font.setFamily("Istok Web")
        font.setPointSize(13)
        self.comboBox_2.setFont(font)
        self.comboBox_2.setStyleSheet("QComboBox {\n"
"    border: 1px solid rgb(140, 153, 169);\n"
"    border-radius: 8px;\n"
"    color: rgb(140, 153, 169);\n"
"    text-align: center;\n"
"}\n"
"QComboBox::drop-down {\n"
"    border: 0px;\n"
"}\n"
"QComboBox::down-arrow {\n"
"    image: url(:/ico osn/ico str.png);\n"
"    margin-right: 15px;\n"
"}\n"
"QComboBox::on {\n"
"    border: 1px solid rgb(140, 153, 169)\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"    border: 1px solid rgb(140, 153, 169);\n"
"    selection-background-color: rgb(140, 153, 169);\n"
"    color: rgb(140, 153, 169);\n"
"    padding-left: 5px;\n"
"}")
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.label_25 = QtWidgets.QLabel(parent=self.frame_5)
        self.label_25.setGeometry(QtCore.QRect(28, 280, 551, 16))
        self.label_25.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.label_25.setObjectName("label_25")
        self.label_26 = QtWidgets.QLabel(parent=self.frame_5)
        self.label_26.setGeometry(QtCore.QRect(28, 290, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Istok Web")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_26.setFont(font)
        self.label_26.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                    "    font: bold;\n"
"color: rgb(140, 153, 169);")
        self.label_26.setObjectName("label_26")
        self.lineEdit_4 = QtWidgets.QLineEdit(parent=self.frame_5)
        self.lineEdit_4.setGeometry(QtCore.QRect(28, 320, 251, 35))
        font = QtGui.QFont()
        font.setFamily("Istok Web")
        font.setPointSize(13)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setStyleSheet("color: rgb(140, 153, 169);\n"
"border-radius: 8px;\n"
"border: 1px solid rgb(140, 153, 169);\n"
"padding-left: 5px;")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.pushButton_10 = QtWidgets.QPushButton(parent=self.frame_5)
        self.pushButton_10.setGeometry(QtCore.QRect(28, 374, 251, 41))
        font = QtGui.QFont()
        font.setFamily("Istok Web")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setStyleSheet("QPushButton {\n"
"    color: rgb(29, 29, 29);\n"
                                         "    font: bold;\n"
"    border-radius: 8px;\n"
"    border: 1px sold rgb(140, 153, 169);\n"
"    background-color: rgb(202, 145, 0);\n"
"}\n"
"\n"
"QPushButton::pressed {\n"
"    background-color: rgba(202, 145, 0, 200);\n"
"}")
        self.pushButton_10.setObjectName("pushButton_10")
        self.label_27 = QtWidgets.QLabel(parent=self.frame_5)
        self.label_27.setGeometry(QtCore.QRect(370, 10, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Istok Web")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_27.setFont(font)
        self.label_27.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                    "    font: bold;\n"
"color: rgb(140, 153, 169);")
        self.label_27.setObjectName("label_27")
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
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/ico osn/admin img.png\"/></p></body></html>"))
        self.label_8.setText(_translate("MainWindow", "Роман Валерьевич"))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/ico osn/rect act.png\"/></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "       Активные заказы"))
        self.pushButton_2.setText(_translate("MainWindow", "       Чат"))
        self.pushButton_3.setText(_translate("MainWindow", "       Машины"))
        self.pushButton_4.setText(_translate("MainWindow", "       Клиенты"))
        self.pushButton_6.setText(_translate("MainWindow", "       Заказы"))
        self.pushButton_7.setText(_translate("MainWindow", "       Отзывы"))
        self.pushButton_8.setText(_translate("MainWindow", "       Заказать такси"))
        self.label_18.setText(_translate("MainWindow", "Сотрудники"))
        self.label_16.setText(_translate("MainWindow", "Грибан Денис Викторович"))
        self.label_17.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/ico osn/Line 2.png\"/></p></body></html>"))
        self.label_10.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/ico main/ico exit.png\"/></p></body></html>"))
        self.label_19.setText(_translate("MainWindow", "ФИО:"))
        self.label_20.setText(_translate("MainWindow", "Телефон:"))
        self.label_21.setText(_translate("MainWindow", "Пароль:"))
        self.label_22.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/ico osn/Line 2.png\"/></p></body></html>"))
        self.label_23.setText(_translate("MainWindow", "Должность:"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Номер"))
        self.comboBox.setItemText(1, _translate("MainWindow", "ФИО"))
        self.label_24.setText(_translate("MainWindow", "Права доступа:"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "Номер"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "ФИО"))
        self.label_25.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/ico osn/Line 2.png\"/></p></body></html>"))
        self.label_26.setText(_translate("MainWindow", "Гос. номер:"))
        self.pushButton_10.setText(_translate("MainWindow", "Сохранить"))
        self.label_27.setText(_translate("MainWindow", "+79224600125"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_AdminWorker_2()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
