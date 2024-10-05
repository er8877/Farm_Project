
from PyQt5 import QtCore, QtGui, QtWidgets
from add_product import Ui8
import time
import mysql.connector
from mysql import connector
from store_change_field import Ui15

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



class Ui7(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 650)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, -30, 901, 731))
        self.label.setText("")
        self.movie = QtGui.QMovie("images/ferma_ai_5.gif")
        self.label.setMovie(self.movie)
        self.movie.start()
        self.label.setScaledContents(True)
        self.label.setOpenExternalLinks(False)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(640, 10, 181, 61))
        font = QtGui.QFont()
        font.setFamily("Myriad Pro Light")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("QLabel{\n"
        "background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:0, y2:1, stop:0.238095 rgba(191, 153, 255, 255), stop:0.693694 rgba(255, 151, 255, 255));\n"
        "color:rgb(93, 93, 140);\n"
        "border:3px solid rgb(95, 95, 143);\n"
        "border-radius:30px\n"
        "}")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 70, 200, 51))
        font = QtGui.QFont()
        font.setFamily("Myriad Pro")
        font.setPointSize(16)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton{\n"
        "background-color:qlineargradient(spread:repeat, x1:1, y1:0, x2:0, y2:1, stop:0.238095 rgba(191, 153, 255, 255), stop:0.693694 rgba(255, 151, 255, 255));\n"
        "color:rgb(95, 95, 143);\n"
        "border:3px solid rgb(95, 95, 143);\n"
        "border-radius:20px\n"
        "}\n"
        "\n"
        "QPushButton:hover{\n"
        "background-color:rgb(125, 255, 255);\n"
        "color:rgb(114, 114, 171);\n"
        "}\n"
        "\n"
        "QPushButton::pressed{\n"
        "background-color: rgb(0, 170, 255);\n"
        "color:rgb(170, 255, 255)\n"
        "}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./icons/database-property.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 10, 120, 50))
        font = QtGui.QFont()
        font.setFamily("Myriad Pro")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton{\n"
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
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("./icons/door-open-out.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 130, 180, 50))
        font = QtGui.QFont()
        font.setFamily("Myriad Pro")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("QPushButton{\n"
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
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("./icons/box.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon2)
        self.pushButton_3.setObjectName("pushButton_3")
        MainWindow.setCentralWidget(self.centralwidget)
        
        self.movies = QtGui.QMovie("ferma_ai_5.gif")
        self.label.setMovie(self.movies)
        self.movies.start()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.pushButton_2.clicked.connect(lambda:MainWindow.hide())
        self.pushButton_3.clicked.connect(self.open_add_product)
        self.pushButton.clicked.connect(self.open_change_values)
        
        


    def open_add_product(self):
        self.win5 = QtWidgets.QMainWindow()
        self.ui5 = Ui8()
        self.ui5.setupUi(self.win5)
        self.win5.show()
        
        
        
    def open_change_values(self):
        self.win6 = QtWidgets.QMainWindow()
        self.ui6 = Ui15()
        self.ui6.setupUi(self.win6)
        self.win6.show()         



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "store"))
        self.label_2.setText(_translate("MainWindow", "Store"))
        self.pushButton.setText(_translate("MainWindow", "Change Values"))
        self.pushButton_2.setText(_translate("MainWindow", "< Back"))
        self.pushButton_3.setText(_translate("MainWindow", "Add Product"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui7()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
