from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
import cv2
import torch
import torchvision.transforms as transforms
from transformers import AutoModelForImageClassification
from PIL import Image

class Ui_detect_fruit(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 670)
        MainWindow.setStyleSheet("QWidget{\n"
        "background-color:rgb(202, 125, 249)\n"
        "}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(380, 15, 181, 61))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic Medium")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel{\n"
        "background-color:rgb(248, 150, 216);\n"
        "border: 2px solid rgb(87, 0, 130);\n"
        "border-radius:27px;\n"
        "}")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 140, 460, 460))
        self.label_2.setStyleSheet("QLabel{\n"
        "background-color:rgb(86, 69, 146);\n"
        "border:2px solid rgb(248, 150, 216);\n"
        "border-radius:30px;\n"
        "}")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_show_pic = QtWidgets.QLabel(self.centralwidget)
        self.label_show_pic.setGeometry(QtCore.QRect(60, 170, 400, 400))
        self.label_show_pic.setStyleSheet("QLabel{\n"
        "background-color:rgb(86, 69, 146);\n"
        "border:2px solid rgb(248, 150, 216);\n"
        "border-radius:10px;\n"
        "}")
        self.label_show_pic.setText("")
        self.label_show_pic.setObjectName("label_show_pic")
        self.pushButton_detect = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_detect.setGeometry(QtCore.QRect(750, 40, 101, 101))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Variable Display Semib")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_detect.setFont(font)
        self.pushButton_detect.setStyleSheet("QPushButton{\n"
        "background-color:rgb(86, 69, 146);\n"
        "color:rgb(248, 150, 216);\n"
        "border:2px solid rgb(248, 150, 216);\n"
        "border-radius:50%;\n"
        "}\n"
        "\n"
        "QPushButton:hover{\n"
        "background-color:rgb(248, 150, 216);\n"
        "color:rgb(86, 69, 146);\n"
        "border: 2px solid rgb(87, 0, 130);\n"
        "}")
        self.pushButton_detect.setObjectName("pushButton_detect")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(620, 200, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Traditional Arabic")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("QLabel{\n"
        "background-color:rgb(248, 150, 216);\n"
        "border: 2px solid rgb(87, 0, 130);\n"
        "border-radius:20px;\n"
        "}")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.checkBox_apple = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_apple.setGeometry(QtCore.QRect(680, 280, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.checkBox_apple.setFont(font)
        self.checkBox_apple.setStyleSheet("QCheckBox{\n"
        "background-color:rgb(86, 69, 146);\n"
        "color:rgb(248, 150, 216);\n"
        "border:2px solid rgb(248, 150, 216);\n"
        "border-radius:15px;\n"
        "padding:7px"
        "}")
        self.checkBox_apple.setObjectName("checkBox_apple")
        self.checkBox_pear = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_pear.setGeometry(QtCore.QRect(680, 380, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.checkBox_pear.setFont(font)
        self.checkBox_pear.setStyleSheet("QCheckBox{\n"
        "background-color:rgb(86, 69, 146);\n"
        "color:rgb(248, 150, 216);\n"
        "border:2px solid rgb(248, 150, 216);\n"
        "border-radius:15px;\n"
        "padding:7px"
        "}")
        self.checkBox_pear.setObjectName("checkBox_pear")
        self.checkBox_pomegranat = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_pomegranat.setGeometry(QtCore.QRect(680, 470, 190, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.checkBox_pomegranat.setFont(font)
        self.checkBox_pomegranat.setStyleSheet("QCheckBox{\n"
        "background-color:rgb(86, 69, 146);\n"
        "color:rgb(248, 150, 216);\n"
        "border:2px solid rgb(248, 150, 216);\n"
        "border-radius:15px;\n"
        "padding:7px"
        "}")
        self.checkBox_pomegranat.setObjectName("checkBox_pomegranat")
        self.checkBox_raddish = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_raddish.setGeometry(QtCore.QRect(680, 560, 120, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.checkBox_raddish.setFont(font)
        self.checkBox_raddish.setStyleSheet("QCheckBox{\n"
        "background-color:rgb(86, 69, 146);\n"
        "color:rgb(248, 150, 216);\n"
        "border:2px solid rgb(248, 150, 216);\n"
        "border-radius:15px;\n"
        "padding:7px"
        "}")
        self.checkBox_raddish.setObjectName("checkBox_raddish")
        self.pushButton_open_file = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_open_file.setGeometry(QtCore.QRect(497, 140, 120, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Variable Display Semib")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_open_file.setFont(font)
        self.pushButton_open_file.setStyleSheet("QPushButton{\n"
        "background-color:rgb(86, 69, 146);\n"
        "color:rgb(248, 150, 216);\n"
        "border:2px solid rgb(248, 150, 216);\n"
        "border-radius:7px;\n"
        "}\n"
        "\n"
        "QPushButton:hover{\n"
        "background-color:rgb(248, 150, 216);\n"
        "color:rgb(86, 69, 146);\n"
        "border: 2px solid rgb(87, 0, 130);\n"
        "}")
        self.pushButton_open_file.setObjectName("pushButton_open_file")
        self.pushButton_back = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_back.setGeometry(QtCore.QRect(30, 25, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Variable Display Semib")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_back.setFont(font)
        self.pushButton_back.setStyleSheet("QPushButton{\n"
        "background-color:rgb(86, 69, 146);\n"
        "color:rgb(248, 150, 216);\n"
        "border:2px solid rgb(248, 150, 216);\n"
        "border-radius:7px;\n"
        "}\n"
        "\n"
        "QPushButton:hover{\n"
        "background-color:rgb(248, 150, 216);\n"
        "color:rgb(86, 69, 146);\n"
        "border: 2px solid rgb(87, 0, 130);\n"
        "}")
        self.pushButton_back.setObjectName("pushButton_back")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton_detect.clicked.connect(self.detect_fruit)
        self.pushButton_open_file.clicked.connect(self.open_file)
        self.pushButton_back.clicked.connect(lambda: MainWindow.hide())

        self.label_show_pic.setScaledContents(True)

        self.list_of_checkboxes = {"apple" : self.checkBox_apple, "pear" : self.checkBox_pomegranat, "pomegranate" : self.checkBox_pomegranat, "raddish" : self.checkBox_raddish}



    def open_file(self):
        global img
        file_name, _ = QFileDialog.getOpenFileName(self.centralwidget, 'Open File', "E:", 'All Files (*.*);;JPG Files (*.jpg)')
        if file_name:
                self.label_show_pic.setPixmap(QtGui.QPixmap(file_name))
                img = cv2.imread(file_name)
                return img



    def detect_fruit(self):
        read_img = img
        model = AutoModelForImageClassification.from_pretrained("jazzmacedo/fruits-and-vegetables-detector-36")

        # Get the list of labels from the model's configuration
        labels = list(model.config.id2label.values())

        # Define the preprocessing transformation
        preprocess = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
        ])

        image = cv2.cvtColor(read_img, cv2.COLOR_BGR2RGB)
        pil_image = Image.fromarray(image)  # Convert NumPy array to PIL image
        input_tensor = preprocess(pil_image).unsqueeze(0)

        # Run the image through the model
        outputs = model(input_tensor)


        # Get the predicted label index
        predicted_idx = torch.argmax(outputs.logits, dim=1).item()

        # Get the predicted label text
        predicted_label = labels[predicted_idx]

        for check in self.list_of_checkboxes.values():
             check.setChecked(False)

        checkbox = self.list_of_checkboxes[predicted_label]
        checkbox.setChecked(True)


        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Detect Fruits"))
        self.label.setText(_translate("MainWindow", "Detect Fruits"))
        self.pushButton_detect.setText(_translate("MainWindow", "Detect"))
        self.label_3.setText(_translate("MainWindow", "Detected : "))
        self.checkBox_apple.setText(_translate("MainWindow", "Apple"))
        self.checkBox_pear.setText(_translate("MainWindow", "Pear"))
        self.checkBox_pomegranat.setText(_translate("MainWindow", "Pomegranate"))
        self.checkBox_raddish.setText(_translate("MainWindow", "Raddish"))
        self.pushButton_open_file.setText(_translate("MainWindow", "Open File"))
        self.pushButton_back.setText(_translate("MainWindow", "Back"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_detect_fruit()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
