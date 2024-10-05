from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QMovie
from crop_health_part2 import Ui_crop_health
import subprocess
from agriculture_recomendation import Ui_agriculture_recomendation
from detect_fruit import Ui_detect_fruit
from store_enter_page import Ui7
from weather_part_daily import Ui_weather_part


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 650)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-10, 0, 1010, 660))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("img&icons/depositphotos_100265018-stock-illustration-farm-field-vector-illustration2.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(500, 30, 170, 80))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("QLabel{\n"
        "background-color:rgb(37, 67, 75);\n"
        "color: rgb(207, 241, 127);\n"
        "border: 5px solid rgb(207, 241, 127);\n"
        "border-radius:40px\n"
        "}")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(320, -10, 190, 180))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("img&icons/745.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        
        self.movie_3 = QMovie("img&icons/giphy.gif")
        self.label_gif2 = QtWidgets.QLabel(self.centralwidget)
        self.label_gif2.setGeometry(QtCore.QRect(190, 300, 150, 150))
        self.label_gif2.setText("")
        self.label_gif2.setMovie(self.movie_3)
        self.label_gif2.setScaledContents(True)
        self.label_gif2.setObjectName("label_gif2")
        self.movie_3.start()
        
        self.movie_2 = QMovie("img&icons/flower.gif")
        self.label_gif3 = QtWidgets.QLabel(self.centralwidget)
        self.label_gif3.setGeometry(QtCore.QRect(800, 380, 110, 120))
        self.label_gif3.setText("")
        self.label_gif3.setMovie(self.movie_2)
        self.label_gif3.setScaledContents(True)
        self.label_gif3.setObjectName("label_gif3")
        self.movie_2.start()
        
        self.movie_1 = QMovie("img&icons/giphy (3).gif")
        self.label_gif1 = QtWidgets.QLabel(self.centralwidget)
        self.label_gif1.setGeometry(QtCore.QRect(450, 250, 160, 170))
        self.label_gif1.setText("")
        self.label_gif1.setMovie(self.movie_1)
        self.label_gif1.setScaledContents(True)
        self.label_gif1.setObjectName("label_gif1")
        self.movie_1.start()
        
        self.pushButton_close = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_close.setGeometry(QtCore.QRect(80, 30, 130, 51))
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(12)
        self.pushButton_close.setFont(font)
        self.pushButton_close.setStyleSheet("QPushButton{\n"
        "background-color:rgb(37, 67, 75);\n"
        "color: rgb(207, 241, 127);\n"
        "border: 2px solid rgb(207, 241, 127);\n"
        "border-radius:20px;\n"
        "padding:7px\n"
        "}\n"
        "\n"
        "QPushButton:hover{\n"
        "background-color: rgb(207, 241, 127);\n"
        "color:rgb(37, 67, 75);\n"
        "border:2px solid rgb(37, 67, 75);\n"
        "}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img&icons/door-open-out.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_close.setIcon(icon)
        self.pushButton_close.setObjectName("pushButton_close")
        self.pushButton_store = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_store.setGeometry(QtCore.QRect(280, 450, 130, 70))
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(12)
        self.pushButton_store.setFont(font)
        self.pushButton_store.setStyleSheet("QPushButton{\n"
        "background-color:rgb(37, 67, 75);\n"
        "color: rgb(207, 241, 127);\n"
        "border: 2px solid rgb(207, 241, 127);\n"
        "border-radius:20px;\n"
        "padding:7px\n"
        "}\n"
        "\n"
        "QPushButton:hover{\n"
        "background-color: rgb(207, 241, 127);\n"
        "color:rgb(37, 67, 75);\n"
        "border:2px solid rgb(37, 67, 75);\n"
        "}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("img&icons/store-label.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_store.setIcon(icon1)
        self.pushButton_store.setObjectName("pushButton_store")
        self.pushButton_detect_fruit = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_detect_fruit.setGeometry(QtCore.QRect(440, 450, 130, 70))
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(12)
        self.pushButton_detect_fruit.setFont(font)
        self.pushButton_detect_fruit.setStyleSheet("QPushButton{\n"
        "background-color:rgb(37, 67, 75);\n"
        "color: rgb(207, 241, 127);\n"
        "border: 2px solid rgb(207, 241, 127);\n"
        "border-radius:20px;\n"
        "padding:7px\n"
        "}\n"
        "\n"
        "QPushButton:hover{\n"
        "background-color: rgb(207, 241, 127);\n"
        "color:rgb(37, 67, 75);\n"
        "border:2px solid rgb(37, 67, 75);\n"
        "}")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("img&icons/fruit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_detect_fruit.setIcon(icon2)
        self.pushButton_detect_fruit.setObjectName("pushButton_detect_fruit")
        self.pushButton_agri_recommend = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_agri_recommend.setGeometry(QtCore.QRect(280, 530, 131, 70))
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(12)
        self.pushButton_agri_recommend.setFont(font)
        self.pushButton_agri_recommend.setStyleSheet("QPushButton{\n"
        "background-color:rgb(37, 67, 75);\n"
        "color: rgb(207, 241, 127);\n"
        "border: 2px solid rgb(207, 241, 127);\n"
        "border-radius:20px;\n"
        "padding:7px\n"
        "}\n"
        "\n"
        "QPushButton:hover{\n"
        "background-color: rgb(207, 241, 127);\n"
        "color:rgb(37, 67, 75);\n"
        "border:2px solid rgb(37, 67, 75);\n"
        "}")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("img&icons/organic-product.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_agri_recommend.setIcon(icon3)
        self.pushButton_agri_recommend.setFlat(False)
        self.pushButton_agri_recommend.setObjectName("pushButton_agri_recommend")
        self.pushButton_crop_health = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_crop_health.setGeometry(QtCore.QRect(440, 530, 130, 70))
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(12)
        self.pushButton_crop_health.setFont(font)
        self.pushButton_crop_health.setStyleSheet("QPushButton{\n"
        "background-color:rgb(37, 67, 75);\n"
        "color: rgb(207, 241, 127);\n"
        "border: 2px solid rgb(207, 241, 127);\n"
        "border-radius:20px;\n"
        "padding:7px\n"
        "}\n"
        "\n"
        "QPushButton:hover{\n"
        "background-color: rgb(207, 241, 127);\n"
        "color:rgb(37, 67, 75);\n"
        "border:2px solid rgb(37, 67, 75);\n"
        "}")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("img&icons/leaf (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_crop_health.setIcon(icon4)
        self.pushButton_crop_health.setObjectName("pushButton_crop_health")
        self.pushButton_game = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_game.setGeometry(QtCore.QRect(110, 450, 130, 70))
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(12)
        self.pushButton_game.setFont(font)
        self.pushButton_game.setStyleSheet("QPushButton{\n"
        "background-color:rgb(37, 67, 75);\n"
        "color: rgb(207, 241, 127);\n"
        "border: 2px solid rgb(207, 241, 127);\n"
        "border-radius:20px;\n"
        "padding:7px\n"
        "}\n"
        "\n"
        "QPushButton:hover{\n"
        "background-color: rgb(207, 241, 127);\n"
        "color:rgb(37, 67, 75);\n"
        "border:2px solid rgb(37, 67, 75);\n"
        "}")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("img&icons/joystick.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_game.setIcon(icon5)
        self.pushButton_game.setObjectName("pushButton_game")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(80, 430, 520, 190))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("QLabel{\n"
        "background-color:rgb(207, 241, 127);\n"
        "color: rgb(207, 241, 127);\n"
        "border: 3px solid rgb(37, 67, 75);\n"
        "border-radius:50px\n"
        "}")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.pushButton_weather = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_weather.setGeometry(QtCore.QRect(110, 530, 130, 70))
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(12)
        self.pushButton_weather.setFont(font)
        self.pushButton_weather.setStyleSheet("QPushButton{\n"
        "background-color:rgb(37, 67, 75);\n"
        "color: rgb(207, 241, 127);\n"
        "border: 2px solid rgb(207, 241, 127);\n"
        "border-radius:20px;\n"
        "padding:7px\n"
        "}\n"
        "\n"
        "QPushButton:hover{\n"
        "background-color: rgb(207, 241, 127);\n"
        "color:rgb(37, 67, 75);\n"
        "border:2px solid rgb(37, 67, 75);\n"
        "}")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("img&icons/weather.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_weather.setIcon(icon6)
        self.pushButton_weather.setObjectName("pushButton_weather")
        self.label.raise_()
        self.label_3.raise_()
        self.label_2.raise_()
        self.label_gif2.raise_()
        self.label_gif3.raise_()
        self.pushButton_close.raise_()
        self.label_gif1.raise_()
        self.label_4.raise_()
        self.pushButton_game.raise_()
        self.pushButton_store.raise_()
        self.pushButton_weather.raise_()
        self.pushButton_agri_recommend.raise_()
        self.pushButton_detect_fruit.raise_()
        self.pushButton_crop_health.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.pushButton_close.clicked.connect(lambda: MainWindow.close())
        self.pushButton_crop_health.clicked.connect(self.open_crop_health)
        self.pushButton_game.clicked.connect(self.open_game)
        self.pushButton_agri_recommend.clicked.connect(self.open_agri_recommend)
        self.pushButton_detect_fruit.clicked.connect(self.open_detect_fruit)
        self.pushButton_store.clicked.connect(self.open_store)
        self.pushButton_weather.clicked.connect(self.open_weather_part)
        
        
    def open_crop_health(self):
        self.win1 = QtWidgets.QMainWindow()
        self.ui1 = Ui_crop_health()
        self.ui1.setupUi(self.win1)
        self.win1.show()
        
        
        
    def open_game(self):
        subprocess.Popen(r"Tractor_game/output/game_code.exe")
        
        
        
    def open_agri_recommend(self):
        self.win2 = QtWidgets.QMainWindow()
        self.ui2 = Ui_agriculture_recomendation()
        self.ui2.setupUi(self.win2)
        self.win2.show()
        
        
        
    def open_detect_fruit(self):
        self.win3 = QtWidgets.QMainWindow()
        self.ui3 = Ui_detect_fruit()
        self.ui3.setupUi(self.win3)
        self.win3.show()
     
        
            
    def open_store(self):
        self.win4 = QtWidgets.QMainWindow()
        self.ui4 = Ui7()
        self.ui4.setupUi(self.win4)
        self.win4.show()



    def open_weather_part(self):
        self.win5 = QtWidgets.QMainWindow()
        self.ui5 = Ui_weather_part()
        self.ui5.setupUi(self.win5)
        self.win5.show()
        
        
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "main page"))
        self.label_2.setText(_translate("MainWindow", "Farm"))
        self.pushButton_close.setText(_translate("MainWindow", "Close"))
        self.pushButton_store.setText(_translate("MainWindow", "Store"))
        self.pushButton_detect_fruit.setText(_translate("MainWindow", "Detect\n"
        "Fruits"))
        self.pushButton_agri_recommend.setText(_translate("MainWindow", "Product\n"
        "Offer"))
        self.pushButton_crop_health.setText(_translate("MainWindow", "Crop\n"
        "Health"))
        self.pushButton_game.setText(_translate("MainWindow", "Game"))
        self.label_4.setText(_translate("MainWindow", "Farm"))
        self.pushButton_weather.setText(_translate("MainWindow", "Weather"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
