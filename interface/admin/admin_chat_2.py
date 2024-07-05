from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QApplication
from PyQt6.QtCore import Qt
import image


class Ui_AdminChat_2(object):
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
        self.label_9.setGeometry(QtCore.QRect(0, 100, 211, 61))
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
        self.pushButton_2.setGeometry(QtCore.QRect(0, 160, 191, 31))
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
        self.pushButton_3.setGeometry(QtCore.QRect(0, 205, 191, 31))
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
        self.label_11 = QtWidgets.QLabel(parent=self.frame_2)
        self.label_11.setGeometry(QtCore.QRect(40, 115, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Istok Web")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                    "    font: bold;\n"
"color: rgb(29, 29, 29);")
        self.label_11.setObjectName("label_11")
        self.frame_5 = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame_5.setGeometry(QtCore.QRect(219, 96, 604, 557))
        self.frame_5.setStyleSheet("border-radius: 10px;\n"
"background-color: rgb(13, 22, 23);")
        self.frame_5.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_5.setObjectName("frame_5")
        self.label_14 = QtWidgets.QLabel(parent=self.frame_5)
        self.label_14.setGeometry(QtCore.QRect(31, 14, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Istok Web")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                    "    font: bold;\n"
"color: rgb(140, 153, 169);")
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(parent=self.frame_5)
        self.label_15.setGeometry(QtCore.QRect(31, 40, 541, 16))
        self.label_15.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.label_15.setObjectName("label_15")
        self.label_10 = QtWidgets.QLabel(parent=self.frame_5)
        self.label_10.setGeometry(QtCore.QRect(558, 23, 16, 16))
        self.label_10.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.label_10.setObjectName("label_10")
        self.frame_4 = QtWidgets.QFrame(parent=self.frame_5)
        self.frame_4.setGeometry(QtCore.QRect(31, 60, 541, 421))
        self.frame_4.setStyleSheet("border: 1px solid rgb(140, 153, 169);\n"
"border-radius: 0px;\n"
"border-top-right-radius: 8px;\n"
"border-top-left-radius: 8px;")
        self.frame_4.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_4.setObjectName("frame_4")
        self.scrollArea = QtWidgets.QScrollArea(parent=self.frame_4)
        self.scrollArea.setGeometry(QtCore.QRect(0, 0, 541, 421))
        self.scrollArea.setStyleSheet("QScrollBar:vertical{\n"
"    background-color: #2A2929;\n"
"        width: 0px;\n"
"        margin: 15px 3px 15px 3px;\n"
"        border-radius: 4px;\n"
"    border: 0px;\n"
"}\n"
"QScrollBar::handle:vertical\n"
"    {\n"
"        background-color: rgb(140, 153, 169);         /* #605F5F; */\n"
"        border-radius: 4px;\n"
"    }\n"
"QScrollBar::sub-line:vertical\n"
"    {\n"
"        margin: 3px 0px 3px 0px;\n"
"        border-image: url(:/qss_icons/rc/up_arrow_disabled.png);\n"
"        height: 10px;\n"
"        width: 10px;\n"
"        subcontrol-position: top;\n"
"        subcontrol-origin: margin;\n"
"    border: 0px;\n"
"\n"
"    }\n"
"QScrollBar::add-line:vertical\n"
"    {\n"
"        margin: 3px 0px 3px 0px;\n"
"        border-image: url(:/qss_icons/rc/down_arrow_disabled.png);\n"
"        height: 10px;\n"
"        width: 10px;\n"
"        subcontrol-position: bottom;\n"
"        subcontrol-origin: margin;\n"
"    border: 0px;\n"
"\n"
"    }\n"
"QScrollBar::sub-line:vertical:hover,QScrollBar::sub-line:vertical:on\n"
"    {\n"
"        height: 10px;\n"
"        width: 10px;\n"
"        subcontrol-position: top;\n"
"        subcontrol-origin: margin;\n"
"    border: 0px;\n"
"    }\n"
"QScrollBar::add-line:vertical:hover, QScrollBar::add-line:vertical:on\n"
"    {\n"
"        height: 10px;\n"
"        width: 10px;\n"
"        subcontrol-position: bottom;\n"
"        subcontrol-origin: margin;\n"
"    border: 0px;\n"
"    }\n"
"\n"
"    QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical\n"
"    {\n"
"        background: none;\n"
"    }\n"
"\n"
"    QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
"    {\n"
"        background: none;\n"
"    }")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 539, 419))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_3 = QtWidgets.QFrame(parent=self.scrollAreaWidgetContents)
        self.frame_3.setMinimumSize(QtCore.QSize(0, 100))
        self.frame_3.setStyleSheet("border-radius: 0px;\n"
"border: 0px;")
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label_13 = QtWidgets.QLabel(parent=self.frame_3)
        self.label_13.setGeometry(QtCore.QRect(495, 0, 25, 25))
        self.label_13.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.label_13.setObjectName("label_13")
        self.label_31 = QtWidgets.QLabel(parent=self.frame_3)
        self.label_31.setGeometry(QtCore.QRect(460, 5, 31, 21))
        font = QtGui.QFont()
        font.setFamily("Istok Web")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_31.setFont(font)
        self.label_31.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(140, 153, 169);")
        self.label_31.setObjectName("label_31")
        self.label_32 = QtWidgets.QLabel(parent=self.frame_3)
        self.label_32.setGeometry(QtCore.QRect(410, 5, 51, 21))
        font = QtGui.QFont()
        font.setFamily("Istok Web")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_32.setFont(font)
        self.label_32.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(140, 153, 169);")
        self.label_32.setObjectName("label_32")
        self.textEdit_2 = QtWidgets.QTextEdit(parent=self.frame_3)
        self.textEdit_2.setGeometry(QtCore.QRect(270, 30, 251, 61))
        font = QtGui.QFont()
        font.setFamily("Istok Web")
        font.setPointSize(12)
        self.textEdit_2.setFont(font)
        self.textEdit_2.setStyleSheet("border: 1px solid rgb(140, 153, 169);\n"
"background-color: rgb(140, 153, 169);\n"
"border-radius: 8px;\n"
"color: rgb(29, 29, 29);")
        self.textEdit_2.setObjectName("textEdit_2")
        self.verticalLayout.addWidget(self.frame_3)
        self.frame_6 = QtWidgets.QFrame(parent=self.scrollAreaWidgetContents)
        self.frame_6.setMinimumSize(QtCore.QSize(0, 100))
        self.frame_6.setStyleSheet("border-radius: 8px;\n"
"border: 0px;")
        self.frame_6.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_6.setObjectName("frame_6")
        self.label_16 = QtWidgets.QLabel(parent=self.frame_6)
        self.label_16.setGeometry(QtCore.QRect(0, 0, 25, 25))
        self.label_16.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.label_16.setObjectName("label_16")
        self.label_33 = QtWidgets.QLabel(parent=self.frame_6)
        self.label_33.setGeometry(QtCore.QRect(33, 5, 151, 21))
        font = QtGui.QFont()
        font.setFamily("Istok Web")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_33.setFont(font)
        self.label_33.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(140, 153, 169);")
        self.label_33.setObjectName("label_33")
        self.label_34 = QtWidgets.QLabel(parent=self.frame_6)
        self.label_34.setGeometry(QtCore.QRect(200, 5, 51, 21))
        font = QtGui.QFont()
        font.setFamily("Istok Web")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_34.setFont(font)
        self.label_34.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(140, 153, 169);")
        self.label_34.setObjectName("label_34")
        self.textEdit_3 = QtWidgets.QTextEdit(parent=self.frame_6)
        self.textEdit_3.setGeometry(QtCore.QRect(0, 30, 251, 61))
        font = QtGui.QFont()
        font.setFamily("Istok Web")
        font.setPointSize(12)
        self.textEdit_3.setFont(font)
        self.textEdit_3.setStyleSheet("border: 1px solid rgb(140, 153, 169);\n"
"background-color: rgb(202, 145, 0);\n"
"border-radius: 8px;\n"
"color: rgb(29, 29, 29);")
        self.textEdit_3.setObjectName("textEdit_3")
        self.verticalLayout.addWidget(self.frame_6)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.textEdit = QtWidgets.QTextEdit(parent=self.frame_5)
        self.textEdit.setGeometry(QtCore.QRect(31, 480, 541, 51))
        font = QtGui.QFont()
        font.setFamily("Istok Web")
        font.setPointSize(11)
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet("border: 1px solid rgb(140, 153, 169);\n"
"border-radius: 0px;\n"
"border-bottom-right-radius: 8px;\n"
"border-bottom-left-radius: 8px;\n"
"color: rgb(140, 153, 169);\n"
"padding-right: 113px;")
        self.textEdit.setObjectName("textEdit")
        self.pushButton_10 = QtWidgets.QPushButton(parent=self.frame_5)
        self.pushButton_10.setGeometry(QtCore.QRect(440, 480, 131, 51))
        font = QtGui.QFont()
        font.setFamily("Istok Web")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setStyleSheet("QPushButton {\n"
"    color: rgb(29, 29, 29);\n"
                                         "    font: bold;\n"
"    border: 0px;\n"
"    background-color:  rgb(140, 153, 169);\n"
"    border-radius: 0px;\n"
"    border-bottom-right-radius: 8px;\n"
"}\n"
"\n"
"QPushButton::pressed {\n"
"    background-color: rgb(202, 145, 0);\n"
"}")
        self.pushButton_10.setObjectName("pushButton_10")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.label_10.setCursor(Qt.CursorShape.PointingHandCursor)
        self.label_10.setMouseTracking(True)

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
        self.pushButton_2.setText(_translate("MainWindow", "       Машины"))
        self.pushButton_3.setText(_translate("MainWindow", "       Сотрудники"))
        self.pushButton_4.setText(_translate("MainWindow", "       Клиенты"))
        self.pushButton_6.setText(_translate("MainWindow", "       Заказы"))
        self.pushButton_7.setText(_translate("MainWindow", "       Отзывы"))
        self.pushButton_8.setText(_translate("MainWindow", "       Заказать такси"))
        self.label_11.setText(_translate("MainWindow", "Чат"))
        self.label_14.setText(_translate("MainWindow", "Чат: Клиент"))
        self.label_15.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/ico osn/Line 2.png\"/></p></body></html>"))
        self.label_10.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/ico main/ico exit.png\"/></p></body></html>"))
        self.label_13.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/chat/img_chat.png\"/></p></body></html>"))
        self.label_31.setText(_translate("MainWindow", "Вы"))
        self.label_32.setText(_translate("MainWindow", "21:41"))
        self.textEdit_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Istok Web\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">sssssssssssssssssssssssssssssssssssssssssssssssssss</p></body></html>"))
        self.label_16.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/chat/img_chat.png\"/></p></body></html>"))
        self.label_33.setText(_translate("MainWindow", "Поддержка"))
        self.label_34.setText(_translate("MainWindow", "21:41"))
        self.textEdit_3.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Istok Web\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">sssssssssssssssssssssssssssssssssssssssssssssssssss</p></body></html>"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Istok Web\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.pushButton_10.setText(_translate("MainWindow", "Отправить"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_AdminChat_2()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
