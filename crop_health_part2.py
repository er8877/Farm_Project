from PyQt5 import QtCore, QtGui, QtWidgets
from crop_health_detection_class import crop_health_detection
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QMessageBox


class Ui_crop_health(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1070, 700)
        font = QtGui.QFont()
        font.setFamily("Sakkal Majalla")
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("QWidget{\n"
        "background-color: #D6EFD8\n"
        "}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(390, 30, 280, 80))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(22)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel{\n"
        "background-color:#1A5319;\n"
        "color:#D6EFD8;\n"
        "border: 4px solid #80AF81;\n"
        "border-radius:40px\n"
        "}")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pushButton_back = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_back.setGeometry(QtCore.QRect(50, 40, 141, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_back.setFont(font)
        self.pushButton_back.setStyleSheet("QPushButton{\n"
        "background-color:#1A5319;\n"
        "color:#D6EFD8;\n"
        "border: 4px solid #80AF81;\n"
        "border-radius:15px\n"
        "}\n"
        "\n"
        "QPushButton:hover{\n"
        "background-color: #508D4E;\n"
        "border: 4px solid #1A5319\n"
        "}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/door-open-out.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_back.setIcon(icon)
        self.pushButton_back.setObjectName("pushButton_back")
        self.listWidget_show_leaf_types = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_show_leaf_types.setGeometry(QtCore.QRect(80, 230, 256, 210))
        self.listWidget_show_leaf_types.setStyleSheet("QListWidget{\n"
        "background-color:#1A5319;\n"
        "color:#D6EFD8;\n"
        "border: 4px solid #80AF81;\n"
        "border-radius:20px;\n"
        "padding:5px;\n"
        "}")
        font = QtGui.QFont()
        font.setFamily("")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.listWidget_show_leaf_types.setFont(font)
        self.listWidget_show_leaf_types.setObjectName("listWidget_show_leaf_types")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(70, 163, 151, 51))
        font = QtGui.QFont()
        font.setFamily("Candara")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("QLabel{\n"
        "background-color:#1A5319;\n"
        "color:#D6EFD8;\n"
        "border: 4px solid #80AF81;\n"
        "border-radius:20px\n"
        "}")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(70, 490, 200, 51))
        font = QtGui.QFont()
        font.setFamily("Candara")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("QLabel{\n"
        "background-color:#1A5319;\n"
        "color:#D6EFD8;\n"
        "border: 4px solid #80AF81;\n"
        "border-radius:20px\n"
        "}")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.radioButton_healthy = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_healthy.setGeometry(QtCore.QRect(220, 560, 120, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Variable Small")
        font.setPointSize(12)
        self.radioButton_healthy.setFont(font)
        self.radioButton_healthy.setStyleSheet("QRadioButton{\n"
        "background-color:#1A5319;\n"
        "color:#D6EFD8;\n"
        "border: 4px solid #80AF81;\n"
        "border-radius:15px;\n"
        "padding : 7px\n"
        "}")
        self.radioButton_healthy.setObjectName("radioButton_healthy")
        self.radioButton_unhealthy = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_unhealthy.setGeometry(QtCore.QRect(80, 560, 140, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Variable Small")
        font.setPointSize(12)
        self.radioButton_unhealthy.setFont(font)
        self.radioButton_unhealthy.setStyleSheet("QRadioButton{\n"
        "background-color:#1A5319;\n"
        "color:#D6EFD8;\n"
        "border: 4px solid #80AF81;\n"
        "border-radius:15px;\n"
        "padding : 7px\n"
        "}")
        self.radioButton_unhealthy.setObjectName("radioButton_unhealthy")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(50, 140, 310, 530))
        self.label_5.setStyleSheet("QLabel{\n"
        "background-color:#80AF81;\n"
        "border-radius:20px\n"
        "}")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.pushButton_upload_photo = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_upload_photo.setGeometry(QtCore.QRect(430, 280, 131, 100))
        font = QtGui.QFont()
        font.setFamily("Candara")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_upload_photo.setFont(font)
        self.pushButton_upload_photo.setStyleSheet("QPushButton{\n"
        "background-color:#1A5319;\n"
        "color:#D6EFD8;\n"
        "border: 7px solid #80AF81;\n"
        "border-radius:50%\n"
        "}\n"
        "\n"
        "QPushButton:hover{\n"
        "background-color: #508D4E;\n"
        "border: 4px solid #1A5319\n"
        "}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/image-import.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_upload_photo.setIcon(icon1)
        self.pushButton_upload_photo.setObjectName("pushButton_upload_photo")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(480, 209, 190, 441))
        self.label_2.setStyleSheet("QLabel{\n"
        "background-color:#80AF81;\n"
        "border-radius:20px\n"
        "}")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_show_photo = QtWidgets.QLabel(self.centralwidget)
        self.label_show_photo.setGeometry(QtCore.QRect(570, 190, 470, 470))
        font = QtGui.QFont()
        font.setFamily("B Bardiya")
        font.setPointSize(17)
        font.setBold(False)
        font.setWeight(50)
        self.label_show_photo.setFont(font)
        self.label_show_photo.setStyleSheet("QLabel{\n"
        "background-color:#1A5319;\n"
        "color:#D6EFD8;\n"
        "border: 4px solid #80AF81;\n"
        "border-radius:20px\n"
        "}")
        self.label_show_photo.setText("")
        self.label_show_photo.setScaledContents(True)
        self.label_show_photo.setAlignment(QtCore.Qt.AlignCenter)
        self.label_show_photo.setObjectName("label_show_photo")
        self.pushButton_predict_model = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_predict_model.setGeometry(QtCore.QRect(430, 480, 131, 100))
        font = QtGui.QFont()
        font.setFamily("Candara")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_predict_model.setFont(font)
        self.pushButton_predict_model.setStyleSheet("QPushButton{\n"
        "background-color:#1A5319;\n"
        "color:#D6EFD8;\n"
        "border: 7px solid #80AF81;\n"
        "border-radius:50%\n"
        "}\n"
        "\n"
        "QPushButton:hover{\n"
        "background-color: #508D4E;\n"
        "border: 4px solid #1A5319\n"
        "}")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/tick.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_predict_model.setIcon(icon2)
        self.pushButton_predict_model.setObjectName("pushButton_predict_model")
        self.label_5.raise_()
        self.label.raise_()
        self.pushButton_back.raise_()
        self.listWidget_show_leaf_types.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.radioButton_healthy.raise_()
        self.radioButton_unhealthy.raise_()
        self.label_2.raise_()
        self.label_show_photo.raise_()
        self.pushButton_upload_photo.raise_()
        self.pushButton_predict_model.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.pushButton_upload_photo.clicked.connect(self.upload_photo)
        self.pushButton_predict_model.clicked.connect(self.extract_info)
        self.pushButton_back.clicked.connect(lambda: MainWindow.close())

    def upload_photo(self):
        self.img_address, _ = QFileDialog.getOpenFileName(self.centralwidget, "open_file", "E:",
                                                          "JPG Files(*.jpg);;PNG Files(*.png)") 
        self.label_show_photo.setPixmap(QtGui.QPixmap(self.img_address))  


    def show_msg(self, msg_text):
        msg = QMessageBox(self.centralwidget)
        msg.setIcon(QMessageBox.Critical)
        msg.setText(msg_text)
        msg.setWindowTitle("Error")
        msg.show()


    def extract_info(self):
        self.listWidget_show_leaf_types.clear()
        self.radioButton_healthy.setEnabled(True)
        self.radioButton_unhealthy.setEnabled(True)
        
        try:
                model = crop_health_detection(self.img_address)
                leaves_types, img_saved_name = model.get_leaves_types()
                self.listWidget_show_leaf_types.addItems(leaves_types)
                self.label_show_photo.setPixmap(QtGui.QPixmap(img_saved_name))
                
                predict_healthy = model.health_detect()
                if predict_healthy == "Healthy":
                        self.radioButton_unhealthy.setChecked(False)
                        self.radioButton_healthy.setChecked(True)
                        self.radioButton_unhealthy.setEnabled(False)
                else:
                        self.radioButton_healthy.setChecked(False)
                        self.radioButton_unhealthy.setChecked(True)
                        self.radioButton_healthy.setEnabled(False)
                        
        except:
                self.show_msg(msg_text="First of all you should upload your image!")


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "crop health detection"))
        self.label.setText(_translate("MainWindow", "Crop Health"))
        self.pushButton_back.setText(_translate("MainWindow", "Back"))
        self.label_3.setText(_translate("MainWindow", "Leaf Type : "))
        self.label_4.setText(_translate("MainWindow", "Health Detect : "))
        self.radioButton_healthy.setText(_translate("MainWindow", "Healthy"))
        self.radioButton_unhealthy.setText(_translate("MainWindow", "Unhealthy"))
        self.pushButton_upload_photo.setText(_translate("MainWindow", "Upload"))
        self.pushButton_predict_model.setText(_translate("MainWindow", "Extract"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_crop_health()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
