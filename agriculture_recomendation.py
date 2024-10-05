from PyQt5 import QtCore, QtGui, QtWidgets
from keras.models import Sequential
from keras.layers import BatchNormalization, Dense, Dropout
import tensorflow as tf
import numpy as np
import pandas as pd
from keras.optimizers import Adam
from sklearn.preprocessing import MinMaxScaler

class Ui_agriculture_recomendation(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(850, 650)
        MainWindow.setStyleSheet("QWidget{\n"
        "background-color:rgb(199, 249, 204)\n"
        "}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(260, 20, 391, 61))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel{\n"
        "background-color:rgb(128, 237, 153);\n"
        "color:rgb(34, 87, 122);\n"
        "border:2px solid rgb(34, 87, 122);\n"
        "border-radius:20px;\n"
        "padding:10px\n"
        "}")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pushButton_back = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_back.setGeometry(QtCore.QRect(20, 20, 100, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_back.setFont(font)
        self.pushButton_back.setStyleSheet("QPushButton{\n"
        "background-color:rgb(128, 237, 153);\n"
        "color:rgb(34, 87, 122);\n"
        "border:2px solid rgb(34, 87, 122);\n"
        "border-radius:20px\n"
        "}\n"
        "\n"
        "QPushButton:hover{\n"
        "background-color:rgb(34, 87, 122);\n"
        "color:rgb(87, 204, 153);\n"
        "border:2px solid rgb(128, 237, 153);\n"
        "}")
        self.pushButton_back.setObjectName("pushButton_back")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(70, 125, 250, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("QLabel{\n"
        "background-color:rgb(128, 237, 153);\n"
        "color:rgb(34, 87, 122);\n"
        "border:2px solid rgb(34, 87, 122);\n"
        "border-radius:20px\n"
        "}")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(70, 200, 250, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("QLabel{\n"
        "background-color:rgb(128, 237, 153);\n"
        "color:rgb(34, 87, 122);\n"
        "border:2px solid rgb(34, 87, 122);\n"
        "border-radius:20px\n"
        "}")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(70, 274, 250, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("QLabel{\n"
        "background-color:rgb(128, 237, 153);\n"
        "color:rgb(34, 87, 122);\n"
        "border:2px solid rgb(34, 87, 122);\n"
        "border-radius:20px\n"
        "}")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(70, 347, 250, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("QLabel{\n"
        "background-color:rgb(128, 237, 153);\n"
        "color:rgb(34, 87, 122);\n"
        "border:2px solid rgb(34, 87, 122);\n"
        "border-radius:20px\n"
        "}")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.doubleSpinBox_nitrogen = QtWidgets.QSpinBox(self.centralwidget)
        self.doubleSpinBox_nitrogen.setGeometry(QtCore.QRect(420, 120, 130, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.doubleSpinBox_nitrogen.setFont(font)
        self.doubleSpinBox_nitrogen.setStyleSheet("QSpinBox{\n"
        "background-color:rgb(128, 237, 153);\n"
        "color:rgb(34, 87, 122);\n"
        "border:2px solid rgb(34, 87, 122);\n"
        "border-radius:10px;\n"
        "padding-left:10px\n"
        "}\n"
        "\n"
        "QDoubleSpinBox:hover{\n"
        "background-color:rgb(34, 87, 122);\n"
        "color:rgb(128, 237, 153);\n"
        "border:5px solid rgb(128, 237, 153);\n"
        "}")
        self.doubleSpinBox_nitrogen.setObjectName("doubleSpinBox_nitrogen")
        self.doubleSpinBox_phosphorous = QtWidgets.QSpinBox(self.centralwidget)
        self.doubleSpinBox_phosphorous.setGeometry(QtCore.QRect(420, 195, 130, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.doubleSpinBox_phosphorous.setFont(font)
        self.doubleSpinBox_phosphorous.setStyleSheet("QSpinBox{\n"
        "background-color:rgb(128, 237, 153);\n"
        "color:rgb(34, 87, 122);\n"
        "border:2px solid rgb(34, 87, 122);\n"
        "border-radius:10px;\n"
        "padding-left:10px\n"
        "}\n"
        "\n"
        "QDoubleSpinBox:hover{\n"
        "background-color:rgb(34, 87, 122);\n"
        "color:rgb(128, 237, 153);\n"
        "border:5px solid rgb(128, 237, 153);\n"
        "}")
        self.doubleSpinBox_phosphorous.setObjectName("doubleSpinBox_phosphorous")
        self.doubleSpinBox_potassium = QtWidgets.QSpinBox(self.centralwidget)
        self.doubleSpinBox_potassium.setGeometry(QtCore.QRect(420, 267, 130, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.doubleSpinBox_potassium.setFont(font)
        self.doubleSpinBox_potassium.setStyleSheet("QSpinBox{\n"
        "background-color:rgb(128, 237, 153);\n"
        "color:rgb(34, 87, 122);\n"
        "border:2px solid rgb(34, 87, 122);\n"
        "border-radius:10px;\n"
        "padding-left:10px\n"
        "}\n"
        "\n"
        "QDoubleSpinBox:hover{\n"
        "background-color:rgb(34, 87, 122);\n"
        "color:rgb(128, 237, 153);\n"
        "border:5px solid rgb(128, 237, 153);\n"
        "}")
        self.doubleSpinBox_potassium.setObjectName("doubleSpinBox_potassium")
        self.doubleSpinBox_temp = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox_temp.setGeometry(QtCore.QRect(420, 340, 130, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.doubleSpinBox_temp.setFont(font)
        self.doubleSpinBox_temp.setStyleSheet("QDoubleSpinBox{\n"
        "background-color:rgb(128, 237, 153);\n"
        "color:rgb(34, 87, 122);\n"
        "border:2px solid rgb(34, 87, 122);\n"
        "border-radius:10px;\n"
        "padding-left:10px\n"
        "}\n"
        "\n"
        "QDoubleSpinBox:hover{\n"
        "background-color:rgb(34, 87, 122);\n"
        "color:rgb(128, 237, 153);\n"
        "border:5px solid rgb(128, 237, 153);\n"
        "}")
        self.doubleSpinBox_temp.setObjectName("doubleSpinBox_temp")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(70, 420, 250, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("QLabel{\n"
        "background-color:rgb(128, 237, 153);\n"
        "color:rgb(34, 87, 122);\n"
        "border:2px solid rgb(34, 87, 122);\n"
        "border-radius:20px\n"
        "}")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.doubleSpinBox_humidity = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox_humidity.setGeometry(QtCore.QRect(420, 415, 130, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.doubleSpinBox_humidity.setFont(font)
        self.doubleSpinBox_humidity.setStyleSheet("QDoubleSpinBox{\n"
        "background-color:rgb(128, 237, 153);\n"
        "color:rgb(34, 87, 122);\n"
        "border:2px solid rgb(34, 87, 122);\n"
        "border-radius:10px;\n"
        "padding-left:10px\n"
        "}\n"
        "\n"
        "QDoubleSpinBox:hover{\n"
        "background-color:rgb(34, 87, 122);\n"
        "color:rgb(128, 237, 153);\n"
        "border:5px solid rgb(128, 237, 153);\n"
        "}")
        self.doubleSpinBox_humidity.setObjectName("doubleSpinBox_humidity")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(70, 493, 250, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("QLabel{\n"
        "background-color:rgb(128, 237, 153);\n"
        "color:rgb(34, 87, 122);\n"
        "border:2px solid rgb(34, 87, 122);\n"
        "border-radius:20px\n"
        "}")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.doubleSpinBox_ph = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox_ph.setGeometry(QtCore.QRect(420, 490, 130, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.doubleSpinBox_ph.setFont(font)
        self.doubleSpinBox_ph.setStyleSheet("QDoubleSpinBox{\n"
        "background-color:rgb(128, 237, 153);\n"
        "color:rgb(34, 87, 122);\n"
        "border:2px solid rgb(34, 87, 122);\n"
        "border-radius:10px;\n"
        "padding-left:10px\n"
        "}\n"
        "\n"
        "QDoubleSpinBox:hover{\n"
        "background-color:rgb(34, 87, 122);\n"
        "color:rgb(128, 237, 153);\n"
        "border:5px solid rgb(128, 237, 153);\n"
        "}")
        self.doubleSpinBox_ph.setObjectName("doubleSpinBox_ph")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(70, 570, 250, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("QLabel{\n"
        "background-color:rgb(128, 237, 153);\n"
        "color:rgb(34, 87, 122);\n"
        "border:2px solid rgb(34, 87, 122);\n"
        "border-radius:20px\n"
        "}")
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.doubleSpinBox_rainfall = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox_rainfall.setGeometry(QtCore.QRect(420, 565, 130, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.doubleSpinBox_rainfall.setFont(font)
        self.doubleSpinBox_rainfall.setStyleSheet("QDoubleSpinBox{\n"
        "background-color:rgb(128, 237, 153);\n"
        "color:rgb(34, 87, 122);\n"
        "border:2px solid rgb(34, 87, 122);\n"
        "border-radius:10px;\n"
        "padding-left:10px\n"
        "}\n"
        "\n"
        "QDoubleSpinBox:hover{\n"
        "background-color:rgb(34, 87, 122);\n"
        "color:rgb(128, 237, 153);\n"
        "border:5px solid rgb(128, 237, 153);\n"
        "}")
        self.doubleSpinBox_rainfall.setObjectName("doubleSpinBox_rainfall")
        self.pushButton_process_data = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_process_data.setGeometry(QtCore.QRect(660, 190, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_process_data.setFont(font)
        self.pushButton_process_data.setStyleSheet("QPushButton{\n"
        "background-color:rgb(128, 237, 153);\n"
        "color:rgb(34, 87, 122);\n"
        "border:2px solid rgb(34, 87, 122);\n"
        "border-radius:50%\n"
        "}\n"
        "\n"
        "QPushButton:hover{\n"
        "background-color:rgb(34, 87, 122);\n"
        "color:rgb(87, 204, 153);\n"
        "border:2px solid rgb(128, 237, 153);\n"
        "}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./icons/tick-red.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_process_data.setIcon(icon)
        self.pushButton_process_data.setObjectName("pushButton_process_data")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(620, 310, 190, 65))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("QLabel{\n"
        "background-color:rgb(128, 237, 153);\n"
        "color:rgb(34, 87, 122);\n"
        "border:2px solid rgb(34, 87, 122);\n"
        "border-radius:20px\n"
        "}")
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.label_show_result = QtWidgets.QLabel(self.centralwidget)
        self.label_show_result.setGeometry(QtCore.QRect(620, 380, 190, 60))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_show_result.setFont(font)
        self.label_show_result.setStyleSheet("QLabel{\n"
        "background-color:rgb(128, 237, 153);\n"
        "color:rgb(34, 87, 122);\n"
        "border:2px solid rgb(34, 87, 122);\n"
        "border-radius:20px\n"
        "}")
        self.label_show_result.setText("")
        self.label_show_result.setAlignment(QtCore.Qt.AlignCenter)
        self.label_show_result.setObjectName("label_show_result")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.doubleSpinBox_nitrogen.setMaximum(300)
        self.doubleSpinBox_ph.setMaximum(300)
        self.doubleSpinBox_phosphorous.setMaximum(300)
        self.doubleSpinBox_potassium.setMaximum(300)
        self.doubleSpinBox_rainfall.setMaximum(600)




        self.pushButton_process_data.clicked.connect(self.recomend_product)
        self.pushButton_back.clicked.connect(lambda: MainWindow.close())
        

        df = pd.read_csv("./Crop_recommendation.csv")
        unique_labels1 = np.unique(df['label'])
        self.unique_labels1=list(unique_labels1)
        self.model = Sequential()
        self.model.add(Dense(60, activation="relu", input_dim=7))
        self.model.add(Dense(100, activation="relu"))
        self.model.add(Dense(120, activation="relu"))
        self.model.add(Dropout(0.5))
        self.model.add(Dense(150, activation="relu"))
        self.model.add(Dense(200, activation="relu"))
        self.model.add(Dropout(0.5))
        self.model.add(Dense(210, activation="relu"))
        self.model.add(Dense(len(self.unique_labels1), activation="linear"))
        self.model.compile(loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True), optimizer=Adam(learning_rate=0.001), metrics=['accuracy'])
        self.model.load_weights("./recommend_product.h5")

        self.preprocess = MinMaxScaler()


    def recomend_product(self):

        feautres_list = [self.doubleSpinBox_nitrogen, self.doubleSpinBox_phosphorous, self.doubleSpinBox_potassium,
                         self.doubleSpinBox_temp, self.doubleSpinBox_humidity, self.doubleSpinBox_ph, self.doubleSpinBox_rainfall]
        vals = np.array([])
        for box in feautres_list:
                vals = np.append(vals, box.value())
        
        arr_new = np.array([vals, [85, 58, 41, 21.770462, 80.319644, 7.038096, 226.655537], 
        [12, 78, 56, 22.222, 45.33, 56.2124, 63.211]])
        arr_new = self.preprocess.fit_transform(arr_new)
        
        # arr_new = np.array(vals).reshape(1, -1)
        # arr_new = self.preprocess.fit_transform(arr_new)

        arr_pred = self.model.predict(arr_new, verbose=0)
        pred_val = self.unique_labels1[np.argmax(arr_pred[0])]
        self.label_show_result.setText(pred_val.capitalize())




    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Agriculture Recomendation"))
        self.label.setText(_translate("MainWindow", "Agriculture Recomendation"))
        self.pushButton_back.setText(_translate("MainWindow", "Back"))
        self.label_2.setText(_translate("MainWindow", "Ratio of Nitrogen :"))
        self.label_3.setText(_translate("MainWindow", "Ratio of Phosphorous :"))
        self.label_4.setText(_translate("MainWindow", "Ratio of Potassium :"))
        self.label_5.setText(_translate("MainWindow", "Temperature :"))
        self.label_6.setText(_translate("MainWindow", "Humidity : "))
        self.label_7.setText(_translate("MainWindow", "Ph value of the soil :"))
        self.label_8.setText(_translate("MainWindow", "Rainfall in mm : "))
        self.pushButton_process_data.setText(_translate("MainWindow", "Done"))
        self.label_9.setText(_translate("MainWindow", "Recomended\nproduct : "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_agriculture_recomendation()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
