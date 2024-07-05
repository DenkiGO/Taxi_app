from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QApplication
from PyQt6.QtCore import Qt
import image


class Ui_Registr(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(830, 660)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 831, 661))
        self.label.setObjectName("label")
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(243, 207, 344, 246))
        self.frame.setStyleSheet("background-color: rgba(0, 0, 0, 107);\n"
"border-radius: 12px;\n"
"border: 1px solid rgba(83, 83, 83, 124);")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.label_2 = QtWidgets.QLabel(parent=self.frame)
        self.label_2.setGeometry(QtCore.QRect(61, 18, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Istok Web")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: none;\n"
"border: 0px;\n"
"font: bold;\n"
"color: white;\n"
"")
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(parent=self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(43, 72, 258, 39))
        font = QtGui.QFont()
        font.setFamily("Istok Web")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color: rgba(255, 255, 255, 178);\n"
"border-radius: 8px;\n"
"font: bold;\n"
"border: 1px solid rgba(0, 0, 0, 114);\n"
"color: rgb(66, 66, 66);\n"
"padding-left: 22px;")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setMaxLength(12)
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(43, 130, 258, 39))
        font = QtGui.QFont()
        font.setFamily("Istok Web")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("background-color: rgba(255, 255, 255, 178);\n"
"border-radius: 8px;\n"
"font: bold;\n"
"border: 1px solid rgba(0, 0, 0, 114);\n"
"color: rgb(66, 66, 66);\n"
"padding-right: 43px;\n"
"padding-left: 22px;")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setMaxLength(30)
        self.pushButton = QtWidgets.QPushButton(parent=self.frame)
        self.pushButton.setGeometry(QtCore.QRect(43, 184, 161, 39))
        font = QtGui.QFont()
        font.setFamily("Istok Web")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton {\n"
"    background-color: rgba(255, 199, 0, 206);\n"
"    border-radius: 8px;\n"
"font: bold;\n"
"    color: rgb(255, 255, 255, 188);\n"
"}\n"
"\n"
"QPushButton::pressed {\n"
"    background-color: rgb(255, 199, 0);\n"
"    color: white;\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.label_3 = QtWidgets.QLabel(parent=self.frame)
        self.label_3.setGeometry(QtCore.QRect(260, 70, 41, 41))
        self.label_3.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"border: 0px;")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=self.frame)
        self.label_4.setGeometry(QtCore.QRect(260, 130, 41, 41))
        self.label_4.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"border: 0px;")
        self.label_4.setObjectName("label_4")
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(210, 190, 91, 16))
        font = QtGui.QFont()
        font.setFamily("Istok Web")
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"border: 0px;\n"
"color: white;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(750, 10, 21, 21))
        self.label_5.setObjectName("label_5")
        self.label_5.setCursor(Qt.CursorShape.PointingHandCursor)
        self.label_5.setMouseTracking(True)
        self.label_6 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(790, 10, 21, 21))
        self.label_6.setObjectName("label_6")
        self.label_6.setCursor(Qt.CursorShape.PointingHandCursor)
        self.label_6.setMouseTracking(True)
        self.label_6.mousePressEvent = self.exit
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def exit(self, event):
        QApplication.quit()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/fon/fon 1.png\"/></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "РЕГИСТРАЦИЯ"))
        self.pushButton.setText(_translate("MainWindow", "Зарегистрироваться"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/ico/ico 1.png\"/></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/ico/ico 2.png\"/></p></body></html>"))
        self.pushButton_2.setText(_translate("MainWindow", "Есть аккаунт?"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/ico main/ico sve.png\"/></p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/ico main/ico exit.png\"/></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Registr()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
