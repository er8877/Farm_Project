from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector
from mysql import connector


def connect_db():
    connect2 = mysql.connector.connect(
        host='localhost', 
        user='root', 
        database='farmer_db'
        )
    return connect2


def id_maker_shopping():
    con=connect_db()
    cursor=con.cursor()
    db_prompt='''SELECT `id` FROM `shopping list` WHERE id=(SELECT Max(id) FROM `shopping list` )'''
    cursor.execute(db_prompt)
    current_id=cursor.fetchall()
    return current_id[0][0]+1


def select_subjects(your_subject):
    con = connect_db()
    cursor4 = con.cursor()
    prompt = """SELECT * FROM `subject_items`"""
    cursor4.execute(prompt)
    get_data = cursor4.fetchall()
    for t in get_data:
        if t[1] == your_subject:
            return t[0]


def insert_product_data(product_name, numbers, img_blob, subject_id):        
    con = connect_db()
    cursor = con.cursor()
    d_id = id_maker_shopping()
    query = """INSERT INTO `shopping list`(id, name, number, img_path, user_id, subject_id, buy_status)VALUES(%s, %s, %s, %s, %s, %s, %s)"""
    val = (d_id, product_name, numbers, img_blob, u_id, subject_id, 1)
    print(product_name)
    cursor.execute(query, val)
    con.commit()
    con.close()



def update_data(table_name, column_name1, column_name2, new_val, before_val):
    connect = connect_db()
    curser5 = connect.cursor()
    query14 = f'''UPDATE {table_name} SET {column_name1}=%s WHERE {column_name2}=%s'''
    val = (new_val, before_val)
    curser5.execute(query14, val)
    connect.commit()
    connect.close()



class Ui15(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 650)
        MainWindow.setStyleSheet("QWidget{\n"
        "background-color:rgb(255, 209, 185)\n"
        "}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(380, 10, 171, 71))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(28)
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
        self.texboxt_show_product = QtWidgets.QTextEdit(self.centralwidget)
        self.texboxt_show_product.setGeometry(QtCore.QRect(30, 180, 401, 350))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.texboxt_show_product.setFont(font)
        self.texboxt_show_product.setStyleSheet("QTextEdit{\n"
        "background-color:rgb(205, 205, 255);\n"
        "color:rgb(87, 87, 131);\n"
        "border:2px solid rgb(105, 105, 158);\n"
        "border-radius:22px\n"
        "}\n"
        "QTextEdit:hover{\n"
        "background-color:rgb(170, 255, 255)\n"
        "}")
        self.texboxt_show_product.setObjectName("texboxt_show_product")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(110, 110, 261, 61))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI Semilight")
        font.setPointSize(18)
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
        self.pushButton_back = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_back.setGeometry(QtCore.QRect(760, 10, 110, 50))
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
        self.pushButton_back.setObjectName("pushButton_back")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(600, 80, 210, 51))
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
        self.comboBox_product = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_product.setGeometry(QtCore.QRect(580, 140, 240, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox_product.setFont(font)
        self.comboBox_product.setStyleSheet("QComboBox{\n"
        "background-color:rgb(190, 190, 255);\n"
        "color:rgb(94, 94, 141);\n"
        "border:2px solid rgb(125, 125, 188);\n"
        "border-top-left-radius:20px;\n"
        "border-bottom-left-radius:20px\n"
        "}\n"
        "\n"
        "QComboBox:hover{\n"
        "background-color: rgb(170, 255, 255);\n"
        "}")
        self.comboBox_product.setObjectName("comboBox_product")
        self.pushButton_product = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_product.setGeometry(QtCore.QRect(610, 210, 200, 50))
        font = QtGui.QFont()
        font.setFamily("Myriad Pro Light")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.pushButton_product.setFont(font)
        self.pushButton_product.setStyleSheet("QPushButton{\n"
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
        self.pushButton_product.setObjectName("pushButton_product")
        self.comboBox_property = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_property.setGeometry(QtCore.QRect(580, 383, 240, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox_property.setFont(font)
        self.comboBox_property.setStyleSheet("QComboBox{\n"
        "background-color:rgb(190, 190, 255);\n"
        "color:rgb(94, 94, 141);\n"
        "border:2px solid rgb(125, 125, 188);\n"
        "border-top-left-radius:20px;\n"
        "border-bottom-left-radius:20px\n"
        "}\n"
        "\n"
        "QComboBox:hover{\n"
        "background-color: rgb(170, 255, 255);\n"
        "}")
        self.comboBox_property.setObjectName("comboBox_property")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(600, 323, 210, 51))
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
        self.pushButton_property = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_property.setGeometry(QtCore.QRect(610, 523, 200, 50))
        font = QtGui.QFont()
        font.setFamily("Myriad Pro Light")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.pushButton_property.setFont(font)
        self.pushButton_property.setStyleSheet("QPushButton{\n"
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
        self.pushButton_property.setObjectName("pushButton_property")
        self.lineEdit_value = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_value.setGeometry(QtCore.QRect(580, 443, 240, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_value.setFont(font)
        self.lineEdit_value.setStyleSheet("QLineEdit{\n"
        "background-color: rgb(185, 185, 255);\n"
        "color:rgb(72, 72, 108);\n"
        "border:2px solid rgb(111, 111, 167);\n"
        "border-radius:20px\n"
        "}\n"
        "QLineEdit:hover{\n"
        "background-color:rgb(170, 255, 255)\n"
        "}")
        self.lineEdit_value.setText("")
        self.lineEdit_value.setObjectName("lineEdit_value")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(470, 440, 131, 51))
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
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.texboxt_show_product.setReadOnly(True)
        
        mydb4 = connector.connect(host="localhost", user="root", database="farmer_db")
        curser4 = mydb4.cursor()
        query4 = """SELECT product_Name FROM add_product"""
        curser4.execute(query4)
        get = curser4.fetchall()
        for item in get:
            for i in item:
                self.comboBox_product.addItem(f"{i}")

        self.pushButton_product.clicked.connect(self.choose_product)
        self.pushButton_back.clicked.connect(lambda: MainWindow.hide())
        self.pushButton_property.clicked.connect(self.change_property)
        
        self.properties = ["product_name", "total_value", "unit", "removed", "date"]
        self.comboBox_property.addItems(self.properties)
        
        
        
    def change_property(self):
        mydb5 = connector.connect(host="localhost", user="root", database="farmer_db")
        curser5 = mydb5.cursor()
        query5 = """SELECT * FROM add_product WHERE product_name=%s"""
        value1 = (self.comboBox_product.currentText(), )
        curser5.execute(query5, value1)
        get_data4 = curser5.fetchall()
        curser5.close()
        d = []
        for jk in get_data4:
            for k in jk: 
                d.append(k)
        
        f = None
        if self.comboBox_property.currentText() == "product_name":
            f = d[0]
        if self.comboBox_property.currentText() == "total_value":
            f = d[1]
        if self.comboBox_property.currentText() == "unit":
            f = d[2]
        if self.comboBox_property.currentText() == "removed":
            f = d[3]
        if self.comboBox_property.currentText() == "date":
            f = d[4]

        if self.comboBox_property.currentText() == "total_value":
            update_info = update_data("add_product", "total_value", "product_Name", self.lineEdit_value.text(), d[0])

        if self.comboBox_property.currentText() == "unit":
            update_info = update_data("add_product", "unit", "product_Name", self.lineEdit_value.text(), d[0])

        if self.comboBox_property.currentText() == "removed":
            update_info = update_data("add_product", "removed", "product_Name", self.lineEdit_value.text(), d[0])

        if self.comboBox_property.currentText() == "product_name":
            update_info = update_data("add_product", "product_Name", "date", self.lineEdit_value.text(), d[4])
 
        mydb6 = connector.connect(host="localhost", user="root", database="farmer_db")
        curser6 = mydb6.cursor() 
        query6 = """SELECT * FROM add_product WHERE product_name=%s"""
        curser6.execute(query6, (self.comboBox_product.currentText(), ))
        get_data6 = curser6.fetchall()
        curser6.close()

        index = 0
        self.texboxt_show_product.clear()
        for i in get_data6:
            for b in i:
                self.texboxt_show_product.append(f"{self.title_list[index]}{b}\n")
                index += 1     
        
        
        
    def choose_product(self):

        self.texboxt_show_product.clear()
        mydb4 = connector.connect(host="localhost", user="root", database="farmer_db")
        curser4 = mydb4.cursor()
        query4 = """SELECT * FROM add_product WHERE product_Name=%s"""
        self.val = (self.comboBox_product.currentText(), )
        curser4.execute(query4, self.val)
        get_data = curser4.fetchall()
        curser4.close()
        self.ib = 0
        self.title_list = ["Product_Name : ", "Total Value : ", "Unit : ", "Removed : ", "Date : "]

        for i in get_data:
            for n in i:
                self.texboxt_show_product.append(f"{self.title_list[self.ib]}{n}\n")
                self.ib += 1
        
        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "change values"))
        self.label_2.setText(_translate("MainWindow", "Store"))
        self.texboxt_show_product.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
        "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
        "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
        "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "Product Property : "))
        self.pushButton_back.setText(_translate("MainWindow", "Back >"))
        self.label_3.setText(_translate("MainWindow", "The Product : "))
        self.pushButton_product.setText(_translate("MainWindow", "Accept Product"))
        self.label_5.setText(_translate("MainWindow", "The Property : "))
        self.pushButton_property.setText(_translate("MainWindow", "Accept Property"))
        self.label_6.setText(_translate("MainWindow", "Value : "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui15()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
