# Form implementation generated from reading ui file 'c:\Users\aleva\OneDrive - Instituto Politecnico Nacional\Desktop\Documentos\PA_team\Avances1\Interfaz2.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(825, 547)
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 127);\n"
"")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridGroupBox = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.gridGroupBox.setGeometry(QtCore.QRect(90, 80, 311, 371))
        self.gridGroupBox.setStyleSheet("background-color: rgb(85, 170, 255);\n"
"background-color: rgb(170, 0, 0);")
        self.gridGroupBox.setObjectName("gridGroupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.gridGroupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.label_6 = QtWidgets.QLabel(parent=self.gridGroupBox)
        self.label_6.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.label_6.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 3, 0, 1, 1)
        self.cesferas = QtWidgets.QPlainTextEdit(parent=self.gridGroupBox)
        self.cesferas.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.cesferas.setObjectName("cesferas")
        self.gridLayout.addWidget(self.cesferas, 0, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(parent=self.gridGroupBox)
        self.label_7.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.label_7.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 1, 0, 2, 1)
        self.label_5 = QtWidgets.QLabel(parent=self.gridGroupBox)
        self.label_5.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.label_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 0, 1, 1)
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(parent=self.gridGroupBox)
        self.plainTextEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.gridLayout.addWidget(self.plainTextEdit_2, 1, 1, 1, 1)
        self.plainTextEdit_3 = QtWidgets.QPlainTextEdit(parent=self.gridGroupBox)
        self.plainTextEdit_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.plainTextEdit_3.setObjectName("plainTextEdit_3")
        self.gridLayout.addWidget(self.plainTextEdit_3, 3, 1, 1, 1)
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(500, 130, 191, 31))
        self.label.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(460, 190, 201, 51))
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"")
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(500, 340, 161, 71))
        self.pushButton.setStyleSheet("background-color: rgb(0, 170, 0);\n"
"font: 18pt \"Segoe UI\";")
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 825, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_6.setText(_translate("MainWindow", "Conteo general"))
        self.label_7.setText(_translate("MainWindow", "Cubos"))
        self.label_5.setText(_translate("MainWindow", "Esferas"))
        self.label.setText(_translate("MainWindow", "Estado del proceso:"))
        self.label_2.setText(_translate("MainWindow", "Funcionando o en paro"))
        self.pushButton.setText(_translate("MainWindow", "INICIO"))
