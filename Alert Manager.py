#BIBLIOTECAS UTILIDAZAS
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from os import getenv
import AlertManager_Designer, sys, pymssql, webbrowser, time, threading, pygame.mixer, pygame.time
import _mssql, decimal, uuid

#DECLARAÇÃO DOS DADOS DO SERVIDOR DE BANCO DE DADOS DO WORKFLOW
serverWF = '172.16.1.96'
userWF = 'sa'
passwordWF = 'evt!123456'
databaseWF = 'WF_Utilidades'

class AlertManager_Window(QWidget, AlertManager_Designer.Ui_Form): 

    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.button_login.clicked.connect(self.login)        

    def login(self):
        if (self.usuarioExiste() == 'existe'):
            self.abrirChrome()
            thread1 = threading.Thread(target=self.habilitaSom)
            thread1.start()
            #self.habilitaSom()
            self.button_login.setEnabled(0)
            
    def habilitaSom(self):
        pygame.mixer.init(44100)
        music = pygame.mixer.music
        music.set_volume(1)
        music.load('C:\\AlertManager\\alarme1.mp3')
        while 1:
            #print(self.verificaAlarme())
            if (self.verificaAlarme() == 'comAlarmes'):
                music.play()
                music.fadeout(1000)
            else:
                music.stop()
            time.sleep(1)

##    def habilitaSom(self):
##        pygame.mixer.init(44100)
##        music = pygame.mixer.music
##        music.set_volume(1)
##        music.load('C:\\AlertManager\\alarme1.mp3')
##        while 1:
##            try:
##                music.play()
##                music.fadeout(1000)
##            except (self.verificaAlarme() == 'comAlarmes'):
##                music.stop()
##                print('Fim')
##            except Exception as e:
##                print('Teste Chinelo')
##                print(e)
##                print('Teste Chinelo')
##            except:
##                print('oi')
##            time.sleep(1)


        
    def usuarioExiste(self): #FUNÇÃO PARA VERIFICAR SE EXISTE O USUARIO NO BANCO DE DADOS DO WF
        username = self.text_username.text() #DECLARAÇÃO DA VARIAVEL
        if (username == "") or (username == " "): #VERIFICA SE O CAMPO DE USERNAME ESTA VAZIO
            self.popUpError('Erro! Digite um usuário válido') #EXIBE O POP UP DE ERRO
        else: #SE O CAMPO DO USERNAME NÃO ESTIVER VAZIO
            conn = pymssql.connect(server = serverWF, user = userWF, password = passwordWF, database = databaseWF) #ABRE A CONEXÃO COM O BANCO DE DADOS
            cursor = conn.cursor() #SELECIONA O CURSOR
            cursor.execute('SELECT Name FROM GalaxyUsers WHERE Name = %s', username) #EXECUTA O SELECT PROCURANDO O NOME DO USERNAME
            row = cursor.fetchone() #RETORNA A LINHA SELECIONADA
            conn.commit()
            conn.close() #FECHA CONEXÃO COM O BANCO DE DADOS
            if (row == None): #SE RETORNAR NONE, ENTÃO NÃO FOI ENCONTRADO O USUARIO
                self.popUpError('Usuário não encontrado no Banco de Dados') #EXIBE O POP UP DE ERRO
                return ('naoExiste')
            else: #LIBERA O ACESSO PARA O USUARIO
                self.popUpInformation('Acesso Liberado!') #EXIBE O POP UP DE INFORMAÇÃO
                return ('existe')

    def verificaAlarme(self):
        username = self.text_username.text() #DECLARAÇÃO DA VARIAVEL
        conn = pymssql.connect(server = serverWF, user = userWF, password = passwordWF, database = databaseWF) #ABRE A CONEXÃO COM O BANCO DE DADOS
        cursor = conn.cursor() #SELECIONA O CURSOR
        cursor.execute('SELECT Name FROM listaNaoAtendidosQtde WHERE Name = %s AND qtde > 0', username) #EXECUTA O SELECT PROCURANDO O NOME DO USERNAME
        row = cursor.fetchone() #RETORNA A LINHA SELECIONADA
        conn.commit()
        conn.close() #FECHA CONEXÃO COM O BANCO DE DADOS
        if (row == None):
            return ('semAlarmes')
        else:
            return ('comAlarmes')
        
    def abrirChrome(self):
        url = 'http://workflow02-evt:8000/EnterpriseConsole/BPMUITemplates/Default/Repository/Site/Login.aspx?_repo=BPM%20Repository%2002&_instanceName=EVERTICAL2&_provtext=Galaxy%20Users[EVERTICAL2]&_prov=galaxyuserprovider'
        webbrowser.open(url)

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

                     
def main():
    app = QApplication(sys.argv)
    app.setStyle('cleanlooks') #dá para alterar
    form = AlertManager_Window() #Nome da Classe lá em cima  
    form.show()
    #app.exec_()
    sys.exit(app.exec_())
  
if __name__ == '__main__': 
    main()
