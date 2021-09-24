from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton,QMessageBox
from PyQt5.Qt import Qt
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtPrintSupport import *


from telalogin1 import Ui_Dialog
from cadra import Ui_MainWindow

class Inicio(QDialog):

    def __init__(self, *args, **argvs):
        super(Inicio, self).__init__(*args, **argvs)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButton_2.clicked.connect(self.botao_ir_Cadastro)
        self.ui.pushButton.clicked.connect(self.botao_login)


    def botao_ir_Cadastro(self):
        self.tela = Cadrastro()
        self.tela.show()
        return self.close()

    def botao_login(self):
        return self.usuario_password()

    def usuario_password(self):
        self.usuario = self.ui.lineEdit.text()
        self.senha = self.ui.lineEdit_2.text()
        with open("senhas.txt", "r") as arquivo:

            ler = arquivo.read()

            if self.usuario == "" and self.senha == "":
                msg = QMessageBox()
                msg.setWindowTitle("Error")
                msg.setText("Informe algo")
                msg.Icon(QMessageBox.Warning)

                iniciar = msg.exec_()

            elif self.usuario in ler and self.senha in ler:
                msg = QMessageBox()
                msg.setWindowTitle("Logado")
                msg.setText("Logado com sucesso")
                msg.Icon(QMessageBox.Information)

                iniciar = msg.exec_()

            else:
                print("Nao e igual")


class Cadrastro(QMainWindow):

    def __init__(self, *args, **argvs):
        super().__init__(*args, **argvs)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.botao)

    def botao(self):
        return self.registrar()

    def registrar(self):
        gmail = self.ui.lineEdit.text()
        senha = self.ui.lineEdit_2.text()
        senha_confirmar = self.ui.lineEdit_3.text()

        if senha == "" and senha_confirmar == "" and gmail == "":
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("Informe o Gmail e a senha")
            msg.Icon(QMessageBox.Warning)
            start = msg.exec_()

        elif senha != senha_confirmar:
            msg = QMessageBox()
            msg.setWindowTitle("Error senhas diferente")
            msg.setText("Senhas diferente")
            msg.Icon(QMessageBox.Critical)

            iniciar = msg.exec_()
        elif senha_confirmar == senha:
            with open("senhas.txt", "a+") as arquivo:
                arquivo.write((gmail) + "\n" + (senha) + "\n" + (senha_confirmar) + "\n")
                print("Cadrastrado com sucesso")
                self.tela_retornar = Inicio()
                self.tela_retornar.show()
                self.close()

        else:
            print("Error tente novamente mais tarde! ")





if __name__ == "__main__":
    import os, sys
    app = QApplication(sys.argv)
    window = Inicio()
    window.show()
    sys.exit(app.exec_())