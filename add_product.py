from PyQt5 import QtCore, QtGui, QtWidgets
import time
from mysql import connector
 

class Ui8(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 650)
        MainWindow.setStyleSheet("QWidget{\n"
        "background-color:rgb(255, 209, 185)\n"
        "}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(340, 10, 281, 71))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("QLabel{\n"
        "background-color: none;\n"
        "color:rgb(93, 93, 140);\n"
        "border:none;\n"
        "}")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.pushButton_back = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_back.setGeometry(QtCore.QRect(770, 20, 120, 50))
        font = QtGui.QFont()
        font.setFamily("Myriad Pro")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.pushButton_back.setFont(font)
        self.pushButton_back.setStyleSheet("QPushButton{\n"
        "background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:0, y2:1, stop:0.238095 rgba(191, 153, 255, 255), stop:0.693694 rgba(255, 151, 255, 255));\n"
        "color:rgb(93, 93, 140);\n"
        "border:3px solid rgb(95, 95, 143);\n"
        "border-radius:20px\n"
        "}\n"
        "\n"
        "QPushButton:hover{\n"
        "background-color:rgb(125, 255, 255);\n"
        "}\n"
        "\n"
        "QPushButton::pressed{\n"
        "background-color: rgb(0, 170, 255);\n"
        "}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./icons/door-open-out.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_back.setIcon(icon)
        self.pushButton_back.setObjectName("pushButton_back")
        self.lineEdit_product = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_product.setGeometry(QtCore.QRect(270, 140, 450, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_product.setFont(font)
        self.lineEdit_product.setStyleSheet("QLineEdit{\n"
        "background-color: rgb(185, 185, 255);\n"
        "color:rgb(72, 72, 108);\n"
        "border:2px solid rgb(100, 100, 150);\n"
        "border-radius:20px\n"
        "}\n"
        "QLineEdit:hover{\n"
        "background-color:rgb(170, 255, 255)\n"
        "}")
        self.lineEdit_product.setText("")
        self.lineEdit_product.setObjectName("lineEdit_product")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(50, 132, 210, 51))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI Semilight")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("QLabel{\n"
        "background-color: none;\n"
        "color:rgb(93, 93, 140);\n"
        "border:none;\n"
        "}")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(60, 225, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI Semilight")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("QLabel{\n"
        "background-color: none;\n"
        "color:rgb(93, 93, 140);\n"
        "border:none;\n"
        "}")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.SpinBox_value = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.SpinBox_value.setGeometry(QtCore.QRect(270, 223, 200, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.SpinBox_value.setFont(font)
        self.SpinBox_value.setStyleSheet("QDoubleSpinBox{\n"
        "background-color:rgb(185, 185, 255);\n"
        "color:rgb(75, 75, 113);\n"
        "border:2px solid rgb(100, 100, 150);\n"
        "border-top-left-radius:20px;\n"
        "border-bottom-left-radius:20px\n"
        "}\n"
        "\n"
        "QDoubleSpinBox:hover{\n"
        "background-color:rgb(170, 255, 255)\n"
        "}\n"
        "\n"
        "QDoubleSpinBox::up-button{\n"
        "background-color:rgb(80, 80, 121);\n"
        "border:1px solid rgb(170, 170, 255);\n"
        "}\n"
        "\n"
        "QDoubleSpinBox::down-button{\n"
        "background-color:rgb(80, 80, 121);\n"
        "border:1px solid rgb(170, 170, 255);\n"
        "}")
        self.SpinBox_value.setObjectName("SpinBox_value")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(510, 223, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI Semilight")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("QLabel{\n"
        "background-color: none;\n"
        "color:rgb(93, 93, 140);\n"
        "border:none;\n"
        "}")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.comboBox_unit = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_unit.setGeometry(QtCore.QRect(650, 223, 191, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox_unit.setFont(font)
        self.comboBox_unit.setStyleSheet("QComboBox{\n"
        "background-color:rgb(190, 190, 255);\n"
        "color:rgb(94, 94, 141);\n"
        "border:2px solid rgb(100, 100, 150);\n"
        "border-top-left-radius:20px;\n"
        "border-bottom-left-radius:20px\n"
        "}\n"
        "\n"
        "QComboBox:hover{\n"
        "background-color: rgb(170, 255, 255);\n"
        "}")
        self.comboBox_unit.setObjectName("comboBox_unit")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(70, 330, 280, 50))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI Semilight")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("QLabel{\n"
        "background-color: none;\n"
        "color:rgb(93, 93, 140);\n"
        "border:none;\n"
        "}")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.SpinBox_removed = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.SpinBox_removed.setGeometry(QtCore.QRect(400, 330, 211, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.SpinBox_removed.setFont(font)
        self.SpinBox_removed.setStyleSheet("QDoubleSpinBox{\n"
        "background-color:rgb(185, 185, 255);\n"
        "color:rgb(75, 75, 113);\n"
        "border:2px solid rgb(100, 100, 150);\n"
        "border-top-left-radius:20px;\n"
        "border-bottom-left-radius:20px\n"
        "}\n"
        "\n"
        "QDoubleSpinBox:hover{\n"
        "background-color:rgb(170, 255, 255)\n"
        "}\n"
        "\n"
        "QDoubleSpinBox::up-button{\n"
        "background-color:rgb(80, 80, 121);\n"
        "border:1px solid rgb(170, 170, 255);\n"
        "}\n"
        "\n"
        "QDoubleSpinBox::down-button{\n"
        "background-color:rgb(80, 80, 121);\n"
        "border:1px solid rgb(170, 170, 255);\n"
        "}")
        self.SpinBox_removed.setObjectName("SpinBox_removed")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(30, 440, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI Semilight")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("QLabel{\n"
        "background-color: none;\n"
        "color:rgb(93, 93, 140);\n"
        "border:none;\n"
        "}")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.comboBox_day = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_day.setGeometry(QtCore.QRect(730, 445, 121, 51))
        self.comboBox_day.setStyleSheet("QComboBox{\n"
        "background-color:rgb(190, 190, 255);\n"
        "color:rgb(94, 94, 141);\n"
        "border:2px solid rgb(100, 100, 150);\n"
        "border-top-left-radius:20px;\n"
        "border-bottom-left-radius:20px\n"
        "}\n"
        "\n"
        "QComboBox:hover{\n"
        "background-color: rgb(170, 255, 255);\n"
        "}")
        self.comboBox_day.setFont(QtGui.QFont("", 12))
        self.comboBox_day.setObjectName("comboBox_day")
        self.comboBox_month = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_month.setGeometry(QtCore.QRect(490, 445, 121, 51))
        self.comboBox_month.setStyleSheet("QComboBox{\n"
        "background-color:rgb(190, 190, 255);\n"
        "color:rgb(94, 94, 141);\n"
        "border:2px solid rgb(100, 100, 150);\n"
        "border-top-left-radius:20px;\n"
        "border-bottom-left-radius:20px\n"
        "}\n"
        "\n"
        "QComboBox:hover{\n"
        "background-color: rgb(170, 255, 255);\n"
        "}")
        self.comboBox_month.setObjectName("comboBox_month")
        self.comboBox_year = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_year.setGeometry(QtCore.QRect(240, 445, 121, 51))
        self.comboBox_year.setStyleSheet("QComboBox{\n"
        "background-color:rgb(190, 190, 255);\n"
        "color:rgb(94, 94, 141);\n"
        "border:2px solid rgb(100, 100, 150);\n"
        "border-top-left-radius:20px;\n"
        "border-bottom-left-radius:20px\n"
        "}\n"
        "\n"
        "QComboBox:hover{\n"
        "background-color: rgb(170, 255, 255);\n"
        "}")
        self.comboBox_year.setCurrentText("")
        self.comboBox_year.setObjectName("comboBox_year")
        self.pushButton_back_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_back_3.setGeometry(QtCore.QRect(380, 560, 260, 50))
        font = QtGui.QFont()
        font.setFamily("Myriad Pro")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.pushButton_back_3.setFont(font)
        self.pushButton_back_3.setStyleSheet("QPushButton{\n"
        "background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:0, y2:1, stop:0.238095 rgba(191, 153, 255, 255), stop:0.693694 rgba(255, 151, 255, 255));\n"
        "color:rgb(75, 75, 113);\n"
        "border:3px solid rgb(95, 95, 143);\n"
        "border-radius:20px\n"
        "}\n"
        "\n"
        "QPushButton:hover{\n"
        "background-color:rgb(125, 255, 255);\n"
        "}\n"
        "\n"
        "QPushButton::pressed{\n"
        "background-color: rgb(0, 170, 255);\n"
        "}")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("./icons/document-word-tick.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_back_3.setIcon(icon2)
        self.pushButton_back_3.setObjectName("pushButton_back_3")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.comboBox_month.setFont(QtGui.QFont("  ", 12))
        self.comboBox_year.setFont(QtGui.QFont("  ", 12))
        
        self.pushButton_back_3.clicked.connect(self.add_product)
        self.pushButton_back.clicked.connect(lambda:MainWindow.hide())

        for d in range(1800, 2024):
            self.comboBox_year.addItem(f"{d}")
        for k in range(1, 13):
            self.comboBox_month.addItem(f"{k}")
        for cx in range(1, 32):
            self.comboBox_day.addItem(f"{cx}")

        self.comboBox_unit.addItem("Kg")
        self.comboBox_unit.addItem("g")
        self.comboBox_unit.addItem("Ton")
        self.comboBox_unit.addItem("Liter")
        self.comboBox_unit.addItem("Cm")
        self.comboBox_unit.addItem("m")
        
        
        
    def add_product(self):
        product = self.lineEdit_product.text()
        total_val = self.SpinBox_value.value()
        removed = self.SpinBox_removed.value()
        unit = self.comboBox_unit.currentText()
        date = f"{self.comboBox_year.currentText()}/{self.comboBox_month.currentText()}/{self.comboBox_day.currentText()}"
        all_datas = (product, total_val, unit, removed, date)
        
        mydb4 = connector.connect(host="localhost", user="root", database="farmer_db")
        cursor4 = mydb4.cursor()
        query4 = """INSERT INTO add_product(product_Name, total_value , unit, removed , date)VALUES(%s, %s, %s, %s, %s)"""
        cursor4.execute(query4, all_datas)
        mydb4.commit()
        cursor4.close()
        
        self.lineEdit_product.clear()
        self.SpinBox_value.clear()
        self.SpinBox_removed.clear()
        
        time.sleep(2)
        
        successful_msg = QtWidgets.QMessageBox(self.centralwidget)
        successful_msg.setText("Your product recorded successfully!")
        successful_msg.setIcon(QtWidgets.QMessageBox.Information)
        successful_msg.show()
        successful_msg.exec_()
        



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Add product"))
        self.label_2.setText(_translate("MainWindow", "Add Product"))
        self.pushButton_back.setText(_translate("MainWindow", "Back >"))
        self.label_3.setText(_translate("MainWindow", "The Product : "))
        self.label_4.setText(_translate("MainWindow", "Total Value :"))
        self.label_5.setText(_translate("MainWindow", "Unit : "))
        self.label_6.setText(_translate("MainWindow", "How Much Removed : "))
        self.label_7.setText(_translate("MainWindow", "Date :"))
        self.pushButton_back_3.setText(_translate("MainWindow", "submit information"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui8()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
