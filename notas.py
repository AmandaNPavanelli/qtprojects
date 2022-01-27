# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets

### Função da janela principal 
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")


### Função do spinBox - Direcionador de Módulos        
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(360, 0, 50, 32))
        self.spinBox.setObjectName("spinBox")
### lineEdit 2 - Disciplina 1 
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(240, 40, 171, 32))
        self.lineEdit_2.setObjectName("lineEdit_2")
### lineEdit 3 - Disciplina 2
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(240, 80, 171, 32))
        self.lineEdit_3.setObjectName("lineEdit_3")
### lineEdit 4 - Disciplina 3         
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(240, 120, 171, 32))
        self.lineEdit_4.setObjectName("lineEdit_4")
### Label - Título (Módulo)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(290, 10, 57, 18))
        self.label.setObjectName("label")
### lineEdit 5 - Nota 1
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(430, 40, 51, 32))
        self.lineEdit_5.setObjectName("lineEdit_5")
### lineEdit 6 - Nota 2
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(430, 80, 51, 32))
        self.lineEdit_6.setObjectName("lineEdit_6")
### lineEdit 7 - Nota 3
        self.lineEdit_7 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_7.setGeometry(QtCore.QRect(430, 120, 51, 32))
        self.lineEdit_7.setObjectName("lineEdit_7")
### Push Buton 1 - Limpar Janela 
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(90, 40, 88, 34))
        self.pushButton.setObjectName("pushButton")
### Push Button 2 - Disciplinas e Notas  
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(90, 80, 88, 34))
        self.pushButton_2.setObjectName("pushButton_2")
### Push Button 3 - Desligar
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(90, 120, 88, 34))
        self.pushButton_3.setObjectName("pushButton_3")
########################################################################
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 30))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
########################################################################

### Ações dos Push Buttons
        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(self.lineEdit_2.clear)
        self.pushButton.clicked.connect(self.lineEdit_3.clear)
        self.pushButton.clicked.connect(self.lineEdit_4.clear)
        self.pushButton.clicked.connect(self.lineEdit_7.clear)
        self.pushButton.clicked.connect(self.lineEdit_5.clear)
        self.pushButton.clicked.connect(self.lineEdit_6.clear)
        self.pushButton.clicked.connect(self.spinBox.clear)
        self.pushButton_2.clicked.connect(self.Qmodulo)
        self.pushButton_3.clicked.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
########################################################################
    def Qmodulo(self):
        modulo = self.spinBox.value()
        if (modulo == 1):
            self.lineEdit_2.setText("Negócio eletrônico")
            self.lineEdit_5.setText("83.0")
            self.lineEdit_3.setText("Algoritmos e Lógica")
            self.lineEdit_6.setText("90.6")
            self.lineEdit_4.setText("Técnicas de Programação")
            self.lineEdit_7.setText("87.5")
        elif (modulo == 2):
            self.lineEdit_2.setText("Estrutura de Dados")
            self.lineEdit_5.setText("90.0")
            self.lineEdit_3.setText("Cálculo")
            self.lineEdit_6.setText("92.0")
            self.lineEdit_4.setText("Gestão Empreendedora")
            self.lineEdit_7.setText("79.0")
        elif (modulo == 3):
            self.lineEdit_2.setText("AP de Sistemas")
            self.lineEdit_5.setText("88.3")
            self.lineEdit_3.setText("Prog Orientada a Objetos")
            self.lineEdit_6.setText("99.0")
            self.lineEdit_4.setText("NULL")
            self.lineEdit_7.setText("NULL")
        elif (modulo == 4):
            self.lineEdit_2.setText("Banco de Dados")
            self.lineEdit_5.setText("82.2")
            self.lineEdit_3.setText("Redes de Computadores")
            self.lineEdit_6.setText("99")
            self.lineEdit_4.setText("NULL")
            self.lineEdit_7.setText("NULL")
        elif (modulo == 5):
            self.lineEdit_2.setText("Prog Python")
            self.lineEdit_5.setText("99.0")
            self.lineEdit_3.setText("Engenharia de Software")
            self.lineEdit_6.setText("90")
            self.lineEdit_4.setText("NULL")
            self.lineEdit_7.setText("NULL")
        else:
            self.lineEdit_2.setText("Módulo errado")
            self.lineEdit_5.setText("0")
            self.lineEdit_3.setText("Me Limpe e ...")
            self.lineEdit_6.setText("0")
            self.lineEdit_4.setText("Tente De Novo!")
            self.lineEdit_7.setText("0")


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Módulo"))
        self.pushButton.setText(_translate("MainWindow", "Limpar"))
        self.pushButton_2.setText(_translate("MainWindow", "Notas"))
        self.pushButton_3.setText(_translate("MainWindow", "Desligar"))

########################################################################
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

### Mandy END
