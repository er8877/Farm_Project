from PyQt5 import QtCore, QtGui, QtWidgets
import requests
import datetime

class Ui_weather_part(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.move(507, 195)
        MainWindow.resize(900, 600)
        MainWindow.setStyleSheet("background-color : black")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(310, 140, 340, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("QLineEdit{\n"
"background-color : rgb(170, 255, 255);\n"
"color : black;\n"
"border: 3px solid rgb(85, 0, 255);\n"
"border-radius : 18px\n"
"}\n"
"QLineEdit:hover{\n"
"background-color : rgb(170, 0, 255)\n"
"}")
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(350, 30, 231, 71))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel{\n"
"background -color : black;\n"
"color : rgb(170, 255, 255);\n"
"border : 2px solid rgb(170, 255, 255);\n"
"border-radius : 25px\n"
"}\n"
"")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(200, 120, 81, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("QLabel{\n"
"background -color : black;\n"
"color : rgb(170, 255, 255);\n"
"border : 2px solid rgb(170, 255, 255);\n"
"border-radius : 20px\n"
"}\n"
"")
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(680, 140, 150, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton{\n"
"background-color : black;\n"
"color : rgb(170, 255, 255);\n"
"border : 2px solid rgb(170, 255, 255);\n"
"border-radius : 20px\n"
"}\n"
"QPushButton:hover{\n"
"background-color : rgb(170, 255, 255);\n"
"color : rgb(0, 0, 0)\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(405, 207, 110, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("QLabel{\n"
"background -color : black;\n"
"color : rgb(170, 255, 255);\n"
"border : 2px solid rgb(170, 255, 255);\n"
"border-radius : 20px\n"
"}\n"
"")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(100, 280, 725, 280))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("QLabel{\n"
"background -color : black;\n"
"color : rgb(170, 255, 255);\n"
"border : 2px solid rgb(170, 255, 255);\n"
"border-radius : 20px;\n "
"}\n"
"")
        self.label_4.setText("")
        self.label_4.setAlignment(QtCore.Qt.AlignLeft)
        self.label_4.setObjectName("label_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


        self.pushButton.clicked.connect(lambda:self.get_weather())

    def celsius_fahrenheit(self, kelvin):
        celsius = kelvin - 273.15
        fahrenheit = celsius * (9 / 5) + 32
        return celsius, fahrenheit

    def get_weather(self):
        url = "http://api.openweathermap.org/data/2.5/weather?"
        Api_Key = open("api.txt", "r").read()
        city = self.lineEdit.text()
        alls = url + "appid=" + Api_Key + "&q=" + city
        response = requests.get(alls).json()

        temp_kelvin = response["main"]["temp"]
        temp_celsius, temp_fahrenheit = self.celsius_fahrenheit(temp_kelvin)
        feels_like_kelvin = response["main"]["feels_like"]
        feels_like_celsius, feels_like_fahrenheit = self.celsius_fahrenheit(feels_like_kelvin)
        wind_speed = response["wind"]["speed"]
        humidity = response["main"]["humidity"]
        description = response["weather"][0]["description"]
        sunrise_time = datetime.datetime.utcfromtimestamp(response["sys"]["sunrise"] + response["timezone"])
        sunset_time = datetime.datetime.utcfromtimestamp(response["sys"]["sunset"] + response["timezone"])
        self.label_4.setText(f"temp = {temp_celsius} C or {temp_fahrenheit} F \nFeels like = {feels_like_celsius}  or  {feels_like_fahrenheit}\nspeed of wind = {wind_speed}"
                             f" km/h\nhumidity = {humidity}%\nsunrise time = {sunrise_time}\nsunset time = {sunset_time}\ndescription = {description}")
        self.label_4.adjustSize()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "outlook of weather"))
        self.label.setText(_translate("MainWindow", "Weather App"))
        self.label_2.setText(_translate("MainWindow", "City : "))
        self.pushButton.setText(_translate("MainWindow", "Accept"))
        self.label_3.setText(_translate("MainWindow", "Result : "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_weather_part()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())