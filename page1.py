# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'page1.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1055, 733)
        font = QtGui.QFont()
        font.setPointSize(19)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color: rgb(190, 225, 255)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_internship = QtWidgets.QLabel(self.centralwidget)
        self.label_internship.setGeometry(QtCore.QRect(10, 0, 1031, 61))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label_internship.setFont(font)
        self.label_internship.setAlignment(QtCore.Qt.AlignCenter)
        self.label_internship.setObjectName("label_internship")
        self.label_name = QtWidgets.QLabel(self.centralwidget)
        self.label_name.setGeometry(QtCore.QRect(40, 110, 171, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_name.setFont(font)
        self.label_name.setStyleSheet("background-color:rgb(255, 218, 30);\n"
"border-radius:20px;\n"
"border:2px solid rgba(0,0,0,0);\n"
"border-color:rgb(85, 85, 255)")
        self.label_name.setAlignment(QtCore.Qt.AlignCenter)
        self.label_name.setObjectName("label_name")
        self.label_age = QtWidgets.QLabel(self.centralwidget)
        self.label_age.setGeometry(QtCore.QRect(40, 210, 161, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_age.setFont(font)
        self.label_age.setStyleSheet("background-color:rgb(255, 218, 30);\n"
"border-radius:20px;\n"
"border:2px solid rgba(0,0,0,0);\n"
"border-color:rgb(85, 85, 255)")
        self.label_age.setAlignment(QtCore.Qt.AlignCenter)
        self.label_age.setObjectName("label_age")
        self.label_gender = QtWidgets.QLabel(self.centralwidget)
        self.label_gender.setGeometry(QtCore.QRect(40, 320, 161, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_gender.setFont(font)
        self.label_gender.setStyleSheet("background-color:rgb(255, 218, 30);\n"
"border-radius:20px;\n"
"border:2px solid rgba(0,0,0,0);\n"
"border-color:rgb(85, 85, 255)")
        self.label_gender.setAlignment(QtCore.Qt.AlignCenter)
        self.label_gender.setObjectName("label_gender")
        self.label_email_ID = QtWidgets.QLabel(self.centralwidget)
        self.label_email_ID.setGeometry(QtCore.QRect(40, 430, 161, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_email_ID.setFont(font)
        self.label_email_ID.setStyleSheet("background-color:rgb(255, 218, 30);\n"
"border-radius:20px;\n"
"border:2px solid rgba(0,0,0,0);\n"
"border-color:rgb(85, 85, 255)")
        self.label_email_ID.setAlignment(QtCore.Qt.AlignCenter)
        self.label_email_ID.setObjectName("label_email_ID")
        self.radioButton_input_male = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_input_male.setGeometry(QtCore.QRect(270, 320, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(19)
        self.radioButton_input_male.setFont(font)
        self.radioButton_input_male.setObjectName("radioButton_input_male")
        self.radioButton_input_female = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_input_female.setGeometry(QtCore.QRect(440, 320, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(19)
        self.radioButton_input_female.setFont(font)
        self.radioButton_input_female.setObjectName("radioButton_input_female")
        self.radioButton_input_other = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_input_other.setGeometry(QtCore.QRect(620, 320, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(19)
        self.radioButton_input_other.setFont(font)
        self.radioButton_input_other.setObjectName("radioButton_input_other")
        self.pushButton_next_page = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_next_page.setGeometry(QtCore.QRect(300, 560, 441, 91))
        font = QtGui.QFont()
        font.setPointSize(19)
        self.pushButton_next_page.setFont(font)
        self.pushButton_next_page.setStyleSheet("background-color:rgb(170, 170, 255);\n"
"border-radius:20px;\n"
"border:2px solid rgba(0,0,0,0);\n"
"border-color:rgb(85, 85, 255);")
        self.pushButton_next_page.setObjectName("pushButton_next_page")
        self.lineEdit_input_name = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_input_name.setGeometry(QtCore.QRect(270, 110, 691, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineEdit_input_name.setFont(font)
        self.lineEdit_input_name.setStyleSheet("background-color:rgb(255, 255, 255);\n"
"padding:5px;\n"
"border:2px solid rgba(0,0,0,0);\n"
"border-color:rgb(85, 85, 255)")
        self.lineEdit_input_name.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_input_name.setObjectName("lineEdit_input_name")
        self.lineEdit_input_age = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_input_age.setGeometry(QtCore.QRect(270, 210, 301, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineEdit_input_age.setFont(font)
        self.lineEdit_input_age.setStyleSheet("background-color:rgb(255, 255, 255);\n"
"border:2px solid rgba(0,0,0,0);\n"
"border-color:rgb(85, 85, 255)")
        self.lineEdit_input_age.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_input_age.setObjectName("lineEdit_input_age")
        self.lineEdit_input_email_ID = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_input_email_ID.setGeometry(QtCore.QRect(270, 430, 691, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineEdit_input_email_ID.setFont(font)
        self.lineEdit_input_email_ID.setStyleSheet("background-color:rgb(255, 255, 255);\n"
"padding:5px;\n"
"border:2px solid rgba(0,0,0,0);\n"
"border-color:rgb(85, 85, 255)")
        self.lineEdit_input_email_ID.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_input_email_ID.setObjectName("lineEdit_input_email_ID")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1055, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_internship.setText(_translate("MainWindow", "Internship💻"))
        self.label_name.setText(_translate("MainWindow", "Your name"))
        self.label_age.setText(_translate("MainWindow", "Age"))
        self.label_gender.setText(_translate("MainWindow", "Gender"))
        self.label_email_ID.setText(_translate("MainWindow", "Email ID"))
        self.radioButton_input_male.setText(_translate("MainWindow", "Male"))
        self.radioButton_input_female.setText(_translate("MainWindow", "Female"))
        self.radioButton_input_other.setText(_translate("MainWindow", "Other"))
        self.pushButton_next_page.setText(_translate("MainWindow", "Click to go to next page"))
        self.lineEdit_input_name.setPlaceholderText(_translate("MainWindow", "Type your name"))
        self.lineEdit_input_age.setPlaceholderText(_translate("MainWindow", "Type your age"))
        self.lineEdit_input_email_ID.setPlaceholderText(_translate("MainWindow", "Type your email id"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
