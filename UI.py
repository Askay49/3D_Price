from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 480)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 500, 480))
        self.widget.setStyleSheet("background-color: rgb(79, 93, 107);\n"
"border-radius:20px;\n"
"border-style: solid;\n"
"border-width: 3px;\n"
"border-color: rgb(62, 70, 79);")
        self.widget.setObjectName("widget")
        self.label_result_output = QtWidgets.QLabel(self.widget)
        self.label_result_output.setGeometry(QtCore.QRect(310, 380, 180, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_result_output.setFont(font)
        self.label_result_output.setStyleSheet("background-color: rgb(85, 170, 255);\n"
"border-radius:10px;\n"
"border-style: solid;\n"
"border-width: 3px;\n"
"border-color: rgb(62, 70, 79);")
        self.label_result_output.setAlignment(QtCore.Qt.AlignCenter)
        self.label_result_output.setObjectName("label_result_output")
        self.label_price_printer = QtWidgets.QLabel(self.widget)
        self.label_price_printer.setGeometry(QtCore.QRect(20, 260, 210, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_price_printer.setFont(font)
        self.label_price_printer.setStyleSheet("background-color: rgb(85, 170, 255);\n"
"border-width: 0px;")
        self.label_price_printer.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_price_printer.setObjectName("label_price_printer")
        self.lineEdit_time_m = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_time_m.setGeometry(QtCore.QRect(405, 140, 85, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_time_m.setFont(font)
        self.lineEdit_time_m.setStyleSheet("background-color: rgb(85, 170, 255);\n"
"border-radius:10px;\n"
"border-style: solid;\n"
"border-width: 3px;\n"
"border-color: rgb(62, 70, 79);")
        self.lineEdit_time_m.setText("")
        self.lineEdit_time_m.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_time_m.setObjectName("lineEdit_time_m")
        self.label_header = QtWidgets.QLabel(self.widget)
        self.label_header.setGeometry(QtCore.QRect(10, 10, 480, 70))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_header.setFont(font)
        self.label_header.setStyleSheet("background-color: rgb(85, 170, 255);\n"
"border-radius:20px;\n"
"border-style: solid;\n"
"border-width: 3px;\n"
"border-color: rgb(62, 70, 79);")
        self.label_header.setAlignment(QtCore.Qt.AlignCenter)
        self.label_header.setObjectName("label_header")
        self.lineEdit_ratio = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_ratio.setGeometry(QtCore.QRect(310, 340, 180, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_ratio.setFont(font)
        self.lineEdit_ratio.setStyleSheet("background-color: rgb(85, 170, 255);\n"
"border-radius:10px;\n"
"border-style: solid;\n"
"border-width: 3px;\n"
"border-color: rgb(62, 70, 79);")
        self.lineEdit_ratio.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_ratio.setObjectName("lineEdit_ratio")
        self.lineEdit_price_energy = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_price_energy.setGeometry(QtCore.QRect(310, 220, 180, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_price_energy.setFont(font)
        self.lineEdit_price_energy.setStyleSheet("background-color: rgb(85, 170, 255);\n"
"border-radius:10px;\n"
"border-style: solid;\n"
"border-width: 3px;\n"
"border-color: rgb(62, 70, 79);")
        self.lineEdit_price_energy.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_price_energy.setObjectName("lineEdit_price_energy")
        self.label_ratio = QtWidgets.QLabel(self.widget)
        self.label_ratio.setGeometry(QtCore.QRect(20, 340, 225, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_ratio.setFont(font)
        self.label_ratio.setStyleSheet("background-color: rgb(85, 170, 255);\n"
"border-width: 0px;")
        self.label_ratio.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_ratio.setObjectName("label_ratio")
        self.Button_result = QtWidgets.QPushButton(self.widget)
        self.Button_result.setGeometry(QtCore.QRect(190, 430, 120, 35))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Button_result.setFont(font)
        self.Button_result.setStyleSheet("background-color: rgb(85, 170, 255);\n"
"border-radius:10px;\n"
"border-style: solid;\n"
"border-width: 3px;\n"
"border-color: rgb(62, 70, 79);")
        self.Button_result.setObjectName("Button_result")
        self.label_time = QtWidgets.QLabel(self.widget)
        self.label_time.setGeometry(QtCore.QRect(20, 140, 130, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_time.setFont(font)
        self.label_time.setStyleSheet("background-color: rgb(85, 170, 255);\n"
"border-width: 0px;")
        self.label_time.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_time.setObjectName("label_time")
        self.lineEdit_price_fl = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_price_fl.setGeometry(QtCore.QRect(310, 180, 180, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_price_fl.setFont(font)
        self.lineEdit_price_fl.setStyleSheet("background-color: rgb(85, 170, 255);\n"
"border-radius:10px;\n"
"border-style: solid;\n"
"border-width: 3px;\n"
"border-color: rgb(62, 70, 79);")
        self.lineEdit_price_fl.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_price_fl.setObjectName("lineEdit_price_fl")
        self.lineEdit_mass = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_mass.setGeometry(QtCore.QRect(310, 100, 180, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_mass.setFont(font)
        self.lineEdit_mass.setStyleSheet("background-color: rgb(85, 170, 255);\n"
"border-radius:10px;\n"
"border-style: solid;\n"
"border-width: 3px;\n"
"border-color: rgb(62, 70, 79);")
        self.lineEdit_mass.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_mass.setObjectName("lineEdit_mass")
        self.label_price_energy = QtWidgets.QLabel(self.widget)
        self.label_price_energy.setGeometry(QtCore.QRect(20, 220, 275, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_price_energy.setFont(font)
        self.label_price_energy.setStyleSheet("background-color: rgb(85, 170, 255);\n"
"border-width: 0px;")
        self.label_price_energy.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_price_energy.setObjectName("label_price_energy")
        self.lineEdit_time_h = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_time_h.setGeometry(QtCore.QRect(310, 140, 85, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_time_h.setFont(font)
        self.lineEdit_time_h.setStyleSheet("background-color: rgb(85, 170, 255);\n"
"border-radius:10px;\n"
"border-style: solid;\n"
"border-width: 3px;\n"
"border-color: rgb(62, 70, 79);")
        self.lineEdit_time_h.setText("")
        self.lineEdit_time_h.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_time_h.setObjectName("lineEdit_time_h")
        self.label_price_fl = QtWidgets.QLabel(self.widget)
        self.label_price_fl.setGeometry(QtCore.QRect(20, 180, 200, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_price_fl.setFont(font)
        self.label_price_fl.setStyleSheet("background-color: rgb(85, 170, 255);\n"
"border-width: 0px;")
        self.label_price_fl.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_price_fl.setObjectName("label_price_fl")
        self.label_mass = QtWidgets.QLabel(self.widget)
        self.label_mass.setGeometry(QtCore.QRect(20, 100, 130, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_mass.setFont(font)
        self.label_mass.setStyleSheet("background-color: rgb(85, 170, 255);\n"
"border-width: 0px;")
        self.label_mass.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_mass.setObjectName("label_mass")
        self.label_power = QtWidgets.QLabel(self.widget)
        self.label_power.setGeometry(QtCore.QRect(20, 300, 220, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_power.setFont(font)
        self.label_power.setStyleSheet("background-color: rgb(85, 170, 255);\n"
"border-width: 0px;")
        self.label_power.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_power.setObjectName("label_power")
        self.lineEdit_power = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_power.setGeometry(QtCore.QRect(310, 300, 180, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_power.setFont(font)
        self.lineEdit_power.setStyleSheet("background-color: rgb(85, 170, 255);\n"
"border-radius:10px;\n"
"border-style: solid;\n"
"border-width: 3px;\n"
"border-color: rgb(62, 70, 79);")
        self.lineEdit_power.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_power.setObjectName("lineEdit_power")
        self.label_result = QtWidgets.QLabel(self.widget)
        self.label_result.setGeometry(QtCore.QRect(20, 380, 140, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_result.setFont(font)
        self.label_result.setStyleSheet("background-color: rgb(85, 170, 255);\n"
"border-width: 0px;")
        self.label_result.setObjectName("label_result")
        self.lineEdit_price_printer = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_price_printer.setGeometry(QtCore.QRect(310, 260, 180, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_price_printer.setFont(font)
        self.lineEdit_price_printer.setStyleSheet("background-color: rgb(85, 170, 255);\n"
"border-radius:10px;\n"
"border-style: solid;\n"
"border-width: 3px;\n"
"border-color: rgb(62, 70, 79);")
        self.lineEdit_price_printer.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_price_printer.setObjectName("lineEdit_price_printer")
        self.frame_labels = QtWidgets.QFrame(self.widget)
        self.frame_labels.setGeometry(QtCore.QRect(10, 95, 290, 320))
        self.frame_labels.setStyleSheet("background-color: rgb(85, 170, 255);\n"
"border-radius:10px;\n"
"border-style: solid;\n"
"border-width: 3px;\n"
"border-color: rgb(62, 70, 79);")
        self.frame_labels.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_labels.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_labels.setObjectName("frame_labels")
        self.Button_exit = QtWidgets.QPushButton(self.widget)
        self.Button_exit.setGeometry(QtCore.QRect(20, 430, 35, 35))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Button_exit.setFont(font)
        self.Button_exit.setStyleSheet("background-color: rgb(255, 80, 89);\n"
"border-radius:10px;\n"
"border-style: solid;\n"
"border-width: 3px;\n"
"border-color: rgb(62, 70, 79);")
        self.Button_exit.setObjectName("Button_exit")
        self.frame_labels.raise_()
        self.label_result_output.raise_()
        self.label_price_printer.raise_()
        self.lineEdit_time_m.raise_()
        self.label_header.raise_()
        self.lineEdit_ratio.raise_()
        self.lineEdit_price_energy.raise_()
        self.label_ratio.raise_()
        self.Button_result.raise_()
        self.label_time.raise_()
        self.lineEdit_price_fl.raise_()
        self.lineEdit_mass.raise_()
        self.label_price_energy.raise_()
        self.lineEdit_time_h.raise_()
        self.label_price_fl.raise_()
        self.label_mass.raise_()
        self.label_power.raise_()
        self.lineEdit_power.raise_()
        self.label_result.raise_()
        self.lineEdit_price_printer.raise_()
        self.Button_exit.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.lineEdit_mass, self.lineEdit_time_h)
        MainWindow.setTabOrder(self.lineEdit_time_h, self.lineEdit_time_m)
        MainWindow.setTabOrder(self.lineEdit_time_m, self.lineEdit_price_fl)
        MainWindow.setTabOrder(self.lineEdit_price_fl, self.lineEdit_price_energy)
        MainWindow.setTabOrder(self.lineEdit_price_energy, self.lineEdit_price_printer)
        MainWindow.setTabOrder(self.lineEdit_price_printer, self.lineEdit_power)
        MainWindow.setTabOrder(self.lineEdit_power, self.lineEdit_ratio)
        MainWindow.setTabOrder(self.lineEdit_ratio, self.Button_result)
        MainWindow.setTabOrder(self.Button_result, self.Button_exit)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "3D_Price"))
        self.label_result_output.setText(_translate("MainWindow", "0 руб"))
        self.label_price_printer.setText(_translate("MainWindow", "Цена 3D принтера, руб"))
        self.lineEdit_time_m.setPlaceholderText(_translate("MainWindow", "Минут"))
        self.label_header.setText(_translate("MainWindow", "Введите параметры:"))
        self.label_ratio.setText(_translate("MainWindow", "Коэффициент сложности"))
        self.Button_result.setText(_translate("MainWindow", "Рассчитать"))
        self.label_time.setText(_translate("MainWindow", "Время печати"))
        self.label_price_energy.setText(_translate("MainWindow", "Цена электроэнергии, руб/час"))
        self.lineEdit_time_h.setPlaceholderText(_translate("MainWindow", "Часов"))
        self.label_price_fl.setText(_translate("MainWindow", "Цена пластика, руб/кг"))
        self.label_mass.setText(_translate("MainWindow", "Вес модели,гр"))
        self.label_power.setText(_translate("MainWindow", "Мощность принтера, Вт"))
        self.label_result.setText(_translate("MainWindow", "Итоговая цена:"))
        self.Button_exit.setText(_translate("MainWindow", "X"))
