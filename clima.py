# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets

### Função da Janela Principal 
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
### Label         
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 20, 211, 41))
        self.label.setObjectName("label")
### Line Edit 1 - Imprime o resultado 
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(330, 20, 381, 81))
        self.textEdit.setObjectName("textEdit")
### Push Button 1 - Resultado      
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 140, 88, 34))
        self.pushButton.setObjectName("pushButton")
### Push Button 2 - Limpar 
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(180, 140, 88, 34))
        self.pushButton_2.setObjectName("pushButton_2")
### Push Button 3 - Desligar        
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(590, 140, 91, 41))
        self.pushButton_3.setObjectName("pushButton_3")
### Line Edit 2 - Campo para digitar o valor 
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(210, 20, 113, 41))
        self.lineEdit_2.setObjectName("lineEdit_2")
##############################################################################        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 30))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
##############################################################################        

### Ações dos Push Buttons 
        self.retranslateUi(MainWindow)
        self.pushButton_2.clicked.connect(self.textEdit.clear)
        self.pushButton_3.clicked.connect(MainWindow.close)
        self.pushButton_2.clicked.connect(self.lineEdit_2.clear)
        self.pushButton.clicked.connect(self.tempo)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
### Funções 
    def tempo(self):
       temp = self.lineEdit_2.text()
       temp = float(temp)
       if (35 > temp > 30):
         self.textEdit.setText('Está muito quente, fique em casa por favor!')
       elif (temp < 15):
         self.textEdit.setText('Não se esqueça da blusa de frio, poderá esfriar bastante!')
       elif (temp >= 35):
         self.textEdit.setText('Procure um lugar refrigerado e permaneça nele, pois a tendência é esquentar muito mais!')
       else:
         self.textEdit.setText('Fique por sua conta, a temperatura está agradável o suficiente!')







    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Digite a Temperatura em Celsius"))
        self.pushButton.setText(_translate("MainWindow", "Resultado"))
        self.pushButton_2.setText(_translate("MainWindow", "Limpar"))
        self.pushButton_3.setText(_translate("MainWindow", "Desligar"))

##############################################################################        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

### Mandy END    
