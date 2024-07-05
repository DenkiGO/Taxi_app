from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QApplication
from PyQt6.QtCore import Qt
import image


class Ui_ClientPod(object):
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
        self.label_6.setGeometry(QtCore.QRect(740, 53, 16, 21))
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
        self.label_9.setGeometry(QtCore.QRect(0, 236, 211, 61))
        self.label_9.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.label_9.setObjectName("label_9")
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
        self.pushButton_5 = QtWidgets.QPushButton(parent=self.frame_2)
        self.pushButton_5.setGeometry(QtCore.QRect(0, 70, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Istok Web")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("QPushButton {\n"
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
        self.pushButton_5.setObjectName("pushButton_5")
        self.label_12 = QtWidgets.QLabel(parent=self.frame_2)
        self.label_12.setGeometry(QtCore.QRect(40, 250, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Istok Web")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                    "    font: bold;\n"
"color: rgb(29, 29, 29);")
        self.label_12.setObjectName("label_12")
        self.pushButton_6 = QtWidgets.QPushButton(parent=self.frame_2)
        self.pushButton_6.setGeometry(QtCore.QRect(0, 115, 191, 31))
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
        self.frame_5 = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame_5.setGeometry(QtCore.QRect(219, 96, 604, 557))
        self.frame_5.setStyleSheet("border-radius: 10px;\n"
"background-color: rgb(13, 22, 23);")
        self.frame_5.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_5.setObjectName("frame_5")
        self.scrollArea = QtWidgets.QScrollArea(parent=self.frame_5)
        self.scrollArea.setGeometry(QtCore.QRect(23, 50, 581, 201))
        self.scrollArea.setStyleSheet("QScrollBar:vertical{\n"
"    background-color: #2A2929;\n"
"        width: 20px;\n"
"        margin: 15px 3px 15px 3px;\n"
"        border-radius: 4px;\n"
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
"    }\n"
"QScrollBar::add-line:vertical\n"
"    {\n"
"        margin: 3px 0px 3px 0px;\n"
"        border-image: url(:/qss_icons/rc/down_arrow_disabled.png);\n"
"        height: 10px;\n"
"        width: 10px;\n"
"        subcontrol-position: bottom;\n"
"        subcontrol-origin: margin;\n"
"    }\n"
"QScrollBar::sub-line:vertical:hover,QScrollBar::sub-line:vertical:on\n"
"    {\n"
"        height: 10px;\n"
"        width: 10px;\n"
"        subcontrol-position: top;\n"
"        subcontrol-origin: margin;\n"
"    }\n"
"QScrollBar::add-line:vertical:hover, QScrollBar::add-line:vertical:on\n"
"    {\n"
"        height: 10px;\n"
"        width: 10px;\n"
"        subcontrol-position: bottom;\n"
"        subcontrol-origin: margin;\n"
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
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, -305, 561, 506))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_3 = QtWidgets.QFrame(parent=self.scrollAreaWidgetContents)
        self.frame_3.setMinimumSize(QtCore.QSize(0, 40))
        self.frame_3.setStyleSheet("border-radius: 0px;")
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label_22 = QtWidgets.QLabel(parent=self.frame_3)
        self.label_22.setGeometry(QtCore.QRect(0, 30, 550, 16))
        self.label_22.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.label_22.setObjectName("label_22")
        self.label_20 = QtWidgets.QLabel(parent=self.frame_3)
        self.label_20.setGeometry(QtCore.QRect(0, 0, 311, 21))
        font = QtGui.QFont()
        font.setFamily("Istok Web")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_20.setFont(font)
        self.label_20.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(140, 153, 169);")
        self.label_20.setObjectName("label_20")
        self.pushButton = QtWidgets.QPushButton(parent=self.frame_3)
        self.pushButton.setGeometry(QtCore.QRect(0, 0, 541, 31))
        self.pushButton.setStyleSheet("color: rgba(13, 22, 23, 0);\n"
"background-color: rgb(255, 255, 255, 0);")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.label_10 = QtWidgets.QLabel(parent=self.frame_3)
        self.label_10.setGeometry(QtCore.QRect(510, 0, 16, 21))
        self.label_10.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.label_10.setObjectName("label_10")
        self.textEdit = QtWidgets.QTextEdit(parent=self.frame_3)
        self.textEdit.setGeometry(QtCore.QRect(0, 50, 541, 131))
        font = QtGui.QFont()
        font.setFamily("Istok Web")
        font.setPointSize(13)
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet("color: rgb(140, 153, 169);\n"
"\n"
"")
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.frame_3)
        self.frame_4 = QtWidgets.QFrame(parent=self.scrollAreaWidgetContents)
        self.frame_4.setMinimumSize(QtCore.QSize(0, 40))
        self.frame_4.setStyleSheet("border-radius: 0px;")
        self.frame_4.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_4.setObjectName("frame_4")
        self.label_23 = QtWidgets.QLabel(parent=self.frame_4)
        self.label_23.setGeometry(QtCore.QRect(0, 30, 550, 16))
        self.label_23.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.label_23.setObjectName("label_23")
        self.label_21 = QtWidgets.QLabel(parent=self.frame_4)
        self.label_21.setGeometry(QtCore.QRect(0, 0, 311, 21))
        font = QtGui.QFont()
        font.setFamily("Istok Web")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_21.setFont(font)
        self.label_21.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(140, 153, 169);")
        self.label_21.setObjectName("label_21")
        self.pushButton_4 = QtWidgets.QPushButton(parent=self.frame_4)
        self.pushButton_4.setGeometry(QtCore.QRect(0, 0, 541, 31))
        self.pushButton_4.setStyleSheet("color: rgba(13, 22, 23, 0);\n"
"background-color: rgb(255, 255, 255, 0);")
        self.pushButton_4.setText("")
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_11 = QtWidgets.QLabel(parent=self.frame_4)
        self.label_11.setGeometry(QtCore.QRect(510, 0, 16, 21))
        self.label_11.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.label_11.setObjectName("label_11")
        self.textEdit_2 = QtWidgets.QTextEdit(parent=self.frame_4)
        self.textEdit_2.setGeometry(QtCore.QRect(0, 50, 541, 131))
        font = QtGui.QFont()
        font.setFamily("Istok Web")
        font.setPointSize(13)
        self.textEdit_2.setFont(font)
        self.textEdit_2.setStyleSheet("color: rgb(140, 153, 169);\n"
"\n"
"")
        self.textEdit_2.setObjectName("textEdit_2")
        self.verticalLayout.addWidget(self.frame_4)
        self.frame_6 = QtWidgets.QFrame(parent=self.scrollAreaWidgetContents)
        self.frame_6.setMinimumSize(QtCore.QSize(0, 40))
        self.frame_6.setStyleSheet("border-radius: 0px;")
        self.frame_6.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_6.setObjectName("frame_6")
        self.label_24 = QtWidgets.QLabel(parent=self.frame_6)
        self.label_24.setGeometry(QtCore.QRect(0, 30, 550, 16))
        self.label_24.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.label_24.setObjectName("label_24")
        self.label_25 = QtWidgets.QLabel(parent=self.frame_6)
        self.label_25.setGeometry(QtCore.QRect(0, 0, 311, 21))
        font = QtGui.QFont()
        font.setFamily("Istok Web")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_25.setFont(font)
        self.label_25.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(140, 153, 169);")
        self.label_25.setObjectName("label_25")
        self.pushButton_7 = QtWidgets.QPushButton(parent=self.frame_6)
        self.pushButton_7.setGeometry(QtCore.QRect(0, 0, 541, 31))
        self.pushButton_7.setStyleSheet("color: rgba(13, 22, 23, 0);\n"
"background-color: rgb(255, 255, 255, 0);")
        self.pushButton_7.setText("")
        self.pushButton_7.setObjectName("pushButton_7")
        self.label_13 = QtWidgets.QLabel(parent=self.frame_6)
        self.label_13.setGeometry(QtCore.QRect(510, 0, 16, 21))
        self.label_13.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.label_13.setObjectName("label_13")
        self.textEdit_3 = QtWidgets.QTextEdit(parent=self.frame_6)
        self.textEdit_3.setGeometry(QtCore.QRect(0, 50, 541, 31))
        font = QtGui.QFont()
        font.setFamily("Istok Web")
        font.setPointSize(13)
        self.textEdit_3.setFont(font)
        self.textEdit_3.setStyleSheet("color: rgb(140, 153, 169);\n"
"\n"
"")
        self.textEdit_3.setObjectName("textEdit_3")
        self.verticalLayout.addWidget(self.frame_6)
        self.frame_7 = QtWidgets.QFrame(parent=self.scrollAreaWidgetContents)
        self.frame_7.setMinimumSize(QtCore.QSize(0, 40))
        self.frame_7.setStyleSheet("border-radius: 0px;")
        self.frame_7.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_7.setObjectName("frame_7")
        self.label_26 = QtWidgets.QLabel(parent=self.frame_7)
        self.label_26.setGeometry(QtCore.QRect(0, 30, 550, 16))
        self.label_26.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.label_26.setObjectName("label_26")
        self.label_27 = QtWidgets.QLabel(parent=self.frame_7)
        self.label_27.setGeometry(QtCore.QRect(0, 0, 311, 21))
        font = QtGui.QFont()
        font.setFamily("Istok Web")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_27.setFont(font)
        self.label_27.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(140, 153, 169);")
        self.label_27.setObjectName("label_27")
        self.pushButton_8 = QtWidgets.QPushButton(parent=self.frame_7)
        self.pushButton_8.setGeometry(QtCore.QRect(0, 0, 541, 31))
        self.pushButton_8.setStyleSheet("color: rgba(13, 22, 23, 0);\n"
"background-color: rgb(255, 255, 255, 0);")
        self.pushButton_8.setText("")
        self.pushButton_8.setObjectName("pushButton_8")
        self.label_16 = QtWidgets.QLabel(parent=self.frame_7)
        self.label_16.setGeometry(QtCore.QRect(510, 0, 16, 21))
        self.label_16.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.label_16.setObjectName("label_16")
        self.textEdit_4 = QtWidgets.QTextEdit(parent=self.frame_7)
        self.textEdit_4.setGeometry(QtCore.QRect(0, 50, 541, 41))
        font = QtGui.QFont()
        font.setFamily("Istok Web")
        font.setPointSize(13)
        self.textEdit_4.setFont(font)
        self.textEdit_4.setStyleSheet("color: rgb(140, 153, 169);\n"
"\n"
"")
        self.textEdit_4.setObjectName("textEdit_4")
        self.verticalLayout.addWidget(self.frame_7)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.label_14 = QtWidgets.QLabel(parent=self.frame_5)
        self.label_14.setGeometry(QtCore.QRect(31, 10, 251, 31))
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
        self.pushButton_9 = QtWidgets.QPushButton(parent=self.frame_5)
        self.pushButton_9.setGeometry(QtCore.QRect(31, 260, 541, 51))
        font = QtGui.QFont()
        font.setFamily("Istok Web")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setStyleSheet("QPushButton {\n"
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
        self.pushButton_9.setObjectName("pushButton_9")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton.clicked.connect(self.vop1)
        self.vp1 = 1
        self.pushButton_4.clicked.connect(self.vop2)
        self.vp2 = 1
        self.pushButton_7.clicked.connect(self.vop3)
        self.vp3 = 1
        self.pushButton_8.clicked.connect(self.vop4)
        self.vp4 = 1

    def exit(self, event):
        QApplication.quit()

    def vop1(self):
        self.vp1 += 1
        if self.vp1%2 == 0:
            self.frame_3.setMinimumSize(QtCore.QSize(0, 180))
        else:
            self.frame_3.setMinimumSize(QtCore.QSize(0, 40))

    def vop2(self):
        self.vp2 += 1
        if self.vp2%2 == 0:
            self.frame_4.setMinimumSize(QtCore.QSize(0, 130))
        else:
            self.frame_4.setMinimumSize(QtCore.QSize(0, 40))

    def vop3(self):
        self.vp3 += 1
        if self.vp3%2 == 0:
            self.frame_6.setMinimumSize(QtCore.QSize(0, 80))
        else:
            self.frame_6.setMinimumSize(QtCore.QSize(0, 40))

    def vop4(self):
        self.vp4 += 1
        if self.vp4%2 == 0:
            self.frame_7.setMinimumSize(QtCore.QSize(0, 80))
        else:
            self.frame_7.setMinimumSize(QtCore.QSize(0, 40))


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
        self.pushButton_2.setText(_translate("MainWindow", "       Отзывы"))
        self.pushButton_3.setText(_translate("MainWindow", "       История заказов"))
        self.pushButton_5.setText(_translate("MainWindow", "       Заказать такси"))
        self.label_12.setText(_translate("MainWindow", "Помощь"))
        self.pushButton_6.setText(_translate("MainWindow", "       Чат"))
        self.label_22.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/ico osn/Line 2.png\"/></p></body></html>"))
        self.label_20.setText(_translate("MainWindow", "Как формируется цена поездки?"))
        self.label_10.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/ico osn/ico str.png\"/></p></body></html>"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Istok Web\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Цена может меняться от базовой и слегка повышенной к повышенной и высокой. Факторы, из-за которых цена может вырасти, много, основные — количество свободных машин и желающих уехать на такси, расстояние и длительность поездки, дополнительные опции к заказу, платные дороги.</p></body></html>"))
        self.label_23.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/ico osn/Line 2.png\"/></p></body></html>"))
        self.label_21.setText(_translate("MainWindow", "Какие способы оплаты есть?"))
        self.label_11.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/ico osn/ico str.png\"/></p></body></html>"))
        self.textEdit_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Istok Web\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Если вы выбрали оплату картой, но она заблокирована или на ней не хватает денег, способ оплаты может автоматически переключиться на наличные.</p></body></html>"))
        self.label_24.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/ico osn/Line 2.png\"/></p></body></html>"))
        self.label_25.setText(_translate("MainWindow", "Можно исправить отзыв?"))
        self.label_13.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/ico osn/ico str.png\"/></p></body></html>"))
        self.textEdit_3.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Istok Web\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Обратитесь в поддержку, указав номер заказа.</p></body></html>"))
        self.label_26.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/ico osn/Line 2.png\"/></p></body></html>"))
        self.label_27.setText(_translate("MainWindow", "О скидочной карте"))
        self.label_16.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/ico osn/ico str.png\"/></p></body></html>"))
        self.textEdit_4.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Istok Web\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Процент скидки зависит от количества поездок.</p></body></html>"))
        self.label_14.setText(_translate("MainWindow", "Часто задаваемые вопросы:"))
        self.label_15.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/ico osn/Line 2.png\"/></p></body></html>"))
        self.pushButton_9.setText(_translate("MainWindow", "Чат с поддержкой"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_ClientPod()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
