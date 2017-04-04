from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from os import getenv
import AlertManager_Designer, sys, pymssql

serverWF = '172.16.1.96'
userWF = 'sa'
passwordWF = 'evt!123456'
databaseWF = 'WF_Utilidades'


class AlertManager_Window(QWidget, AlertManager_Designer.Ui_Form):

    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.button_login.clicked.connect(self.login)
        
    def usuarioExiste(self): #FUNÇÃO PARA VERIFICAR SE EXISTE O USUARIO NO BANCO DE DADOS DO WF

        username = self.text_username.text() #DECLARAÇÃO DA VARIAVEL

        if (username == "") or (username == " "): #VERIFICA SE O CAMPO DE USERNAME ESTA VAZIO
            self.popUpError('Erro! Digite um usuário válido') #EXIBE O POP UP DE ERRO
        else: #SE O CAMPO DO USERNAME NÃO ESTIVER VAZIO
            conn = pymssql.connect(server = serverWF, user = userWF, password = passwordWF, database = databaseWF) #ABRE A CONEXÃO COM O BANCO DE DADOS
            cursor = conn.cursor() #SELECIONA O CURSOR
            cursor.execute('SELECT Name FROM GalaxyUsers WHERE Name = %s', username) #EXECUTA O SELECT PROCURANDO O NOME DO USERNAME
            row = cursor.fetchone() #RETORNA A LINHA SELECIONADA
            if (row == None): #SE RETORNAR NONE, ENTÃO NÃO FOI ENCONTRADO O USUARIO
               self.popUpError('Usuário não encontrado no Bando de Dados') #EXIBE O POP UP DE ERRO
            else: #LIBERA O ACESSO PARA O USUARIO
                self.popUpInformation('Liberou o acesso do usuário') #EXIBE O POP UP DE INFORMAÇÃO        
            conn.commit()
            conn.close() #FECHA CONEXÃO COM O BANCO DE DADOS
            
            
    def popUpError(self, text): #FUNÇÃO DE POP UP DE ERRO
        
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText(text)
        msg.setWindowTitle('Erro')
        msg.exec_()

    def popUpInformation(self, text): #FUNÇÃO DE POP DE INFORMAÇÃO
        
        msg = QMessageBox()
        msg.setText(text)
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle(' ')
        msg.exec_()

    def login(self): #FUNÇÃO PRINCIPAL DE LOGIN
        
        self.usuarioExiste() #CHAMA A FUNÇÃO DE CONFIRMAÇÃO DE USUARIO
                     
def main():
    app = QApplication(sys.argv)
    app.setStyle('cleanlooks') #dá para alterar
    form = AlertManager_Window() #Nome da Classe lá em cima  
    form.show()
    app.exec_()
  
if __name__ == '__main__': 
    main()
