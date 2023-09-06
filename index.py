from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Electric(object):
    def setupUi(self, Electric):
        Electric.setObjectName("Electric")
        Electric.resize(900, 600)
        Electric.setMinimumSize(QtCore.QSize(900, 600))
        Electric.setMaximumSize(QtCore.QSize(900, 600))
        Electric.setStyleSheet("background-color: #1450A3")
        self.centralwidget = QtWidgets.QWidget(Electric)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 901, 111))
        self.label.setStyleSheet("Background-color: #191D88;\n"
                                 "font: 8pt \"ROG Fonts\";\n"
                                 "color: #fff;\n"
                                 "padding:100px;\n"
                                 "font-size: 20px;")
        self.label.setTextFormat(QtCore.Qt.PlainText)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(60, 180, 781, 41))
        self.lineEdit.setStyleSheet("background-color:#337CCF;\n"
                                "border:none;\n"
                                "border-radius:10px;\n"
                                "padding: 10px;\n"
                                "color: #fff;\n"
                                "font-size:15px;")

        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 145, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color:#fff;\n"
                                   "font-size:20px")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(60, 230, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color:#fff;\n"
                                   "font-size:20px")
        self.label_3.setObjectName("label_3")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(60, 270, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.radioButton.setFont(font)
        self.radioButton.setStyleSheet("font-size:15px;\n"
                                       "color:#fff;\n"
                                       "")
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(60, 310, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setStyleSheet("font-size:15px;\n"
                                         "color:#fff;\n"
                                         "")
        self.radioButton_2.setObjectName("radioButton_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(60, 360, 781, 51))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color:#FFC436;\n"
                                      "font-size:20px;\n"
                                      "border-radius:20px\n"
                                      "")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.calculate_bill) 
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(60, 460, 781, 91))
        self.plainTextEdit.setStyleSheet("background-color:#337CCF;\n"
                                         "padding:20px;\n"
                                         "border:none;\n"
                                         "border-radius:20px;\n"
                                         "color:#fff;\n"
                                         "font-size:30px")
        self.plainTextEdit.setPlainText("")
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(60, 420, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color:#fff;\n"
                                   "font-size:20px")
        self.label_4.setObjectName("label_4")
        Electric.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Electric)
        self.statusbar.setObjectName("statusbar")
        Electric.setStatusBar(self.statusbar)

        self.retranslateUi(Electric)
        QtCore.QMetaObject.connectSlotsByName(Electric)

    def retranslateUi(self, Electric):
        _translate = QtCore.QCoreApplication.translate
        Electric.setWindowTitle(_translate("Electric", "Eltrictials"))
        self.label.setText(_translate(
            "Electric", "Electricity Bill Estimation ( NON SUBSIDI )"))
        self.label_2.setText(_translate("Electric", "Tarif listrik per KwH"))
        self.label_3.setText(_translate("Electric", "Pilih Salah Satu"))
        self.radioButton.setText(_translate("Electric", "/ Hari"))
        self.radioButton_2.setText(_translate("Electric", "/ Bulanan"))
        self.pushButton.setText(_translate("Electric", "Calculate"))
        self.label_4.setText(_translate("Electric", "Output:"))

    def calculate_bill(self):
        input_text = self.lineEdit.text()
        if not input_text:
                self.plainTextEdit.setPlainText("Belum Diisi!")
                return

        tariff = float(input_text)
        
        if self.radioButton.isChecked():
                frequency = "Hari"
        elif self.radioButton_2.isChecked():
                frequency = "Bulanan"
        else:
                frequency = "Tidak dipilih!"

        if frequency == "Hari":
                result = tariff * 1352
        elif frequency == "Bulanan":
                result = tariff * 1352 * 30
        else:
                result = 0

        self.plainTextEdit.setPlainText(f"Biaya listrik per {frequency}:  Rp {result:.2f}")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Electric = QtWidgets.QMainWindow()
    ui = Ui_Electric()
    ui.setupUi(Electric)
    Electric.show()
    sys.exit(app.exec_())
