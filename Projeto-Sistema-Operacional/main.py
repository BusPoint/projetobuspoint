# -*- coding: utf-8 -*-
from PyQt5 import uic, QtWidgets, QtCore
from PyQt5.QtCore import QTimer, QTime, Qt
from PyQt5.QtGui import *
import os
import subprocess

def capture_output_command():
    completed = subprocess.run(
        ['ls', '-1'],
        stdout=subprocess.PIPE,
    )
    print('returncode:', completed.returncode)
    print('Have {} bytes in stdout:\n{}'.format(
        len(completed.stdout),
        completed.stdout.decode('utf-8'))
    )

def py_xwininfo():
    winId = getCurrentWinId()
    print ('winId = %s' %winId)

def getCurrentWinId():
    cmd_1 = ['xprop', '-root']
    cmd_2 = ['awk', '/_NET_ACTIVE_WINDOW(WINDOW)/{print $NF}']
    p1 = subprocess.Popen(cmd_1, stdout = subprocess.PIPE)
    p2 = subprocess.Popen(cmd_2, stdin = p1.stdout, stdout=subprocess.PIPE)
    id = p2.communicate()[0]

    return id

def command_unix():
    print("popen4:")
    proc = subprocess.Popen(
        'cat -; echo "to stderr" 1>&2',
        shell=True,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    msg = "through stdin to stdout ".encode("utf-8")
    stdout_value, stderr_value = proc.communicate(msg)
    print("combined output:", repr(stdout_value.decode("utf-8")))
    print("stderr value   :", repr(stderr_value))

if __name__ == '__main__':
    py_xwininfo()
    command_unix()
    capture_output_command()
    
# Função para chamar a tela de linhas de ônibus.
def chama_segunda_tela():
    tela_lista.show()
    primeira_tela.hide()

# Funções da linha 1.
def chama_linha1():
    tela_linha1.show()
    tela_lista.hide()

def botao_voltar_linha1():
    tela_lista.show()
    tela_linha1.hide()

# Funções da linha 2.
def chama_linha2():
    tela_linha2.show()
    tela_lista.hide()

def botao_voltar_linha2():
    tela_lista.show()
    tela_linha2.hide()

# Funções da linha 3.
def chama_linha3():
    tela_linha3.show()
    tela_lista.hide()

def botao_voltar_linha3():
    tela_lista.show()
    tela_linha3.hide()

# Funções da linha 4.
def chama_linha4():
    tela_linha4.show()
    tela_lista.hide()

def botao_voltar_linha4():
    tela_lista.show()
    tela_linha4.hide()

# Funções da linha 5.
def chama_linha5():
    tela_linha5.show()
    tela_lista.hide()

def botao_voltar_linha5():
    tela_lista.show()
    tela_linha5.hide()

# Funções da linha 6.
def chama_linha6():
    tela_linha6.show()
    tela_lista.hide()

def botao_voltar_linha6():
    tela_lista.show()
    tela_linha6.hide()

# Funções da linha 7.
def chama_linha7():
    tela_linha7.show()
    tela_lista.hide()

def botao_voltar_linha7():
    tela_lista.show()
    tela_linha7.hide()

# Funções da linha 8.
def chama_linha8():
    tela_linha8.show()
    tela_lista.hide()

def botao_voltar_linha8():
    tela_lista.show()
    tela_linha8.hide()

# Funções da linha 9.
def chama_linha9():
    tela_linha9.show()
    tela_lista.hide()

def botao_voltar_linha9():
    tela_lista.show()
    tela_linha9.hide()

# Funções da linha 10.
def chama_linha10():
    tela_linha10.show()
    tela_lista.hide()

def botao_voltar_linha10():
    tela_lista.show()
    tela_linha10.hide()


# Função do relógio
def displayTime():
    currentTime = QTime.currentTime()

    displayText = currentTime.toString('hh:mm:ss')

    tela_linha1.label.setText(displayText)
    tela_linha2.label.setText(displayText)
    tela_linha3.label.setText(displayText)
    tela_linha4.label.setText(displayText)
    tela_linha5.label.setText(displayText)
    tela_linha6.label.setText(displayText)
    tela_linha7.label.setText(displayText)
    tela_linha8.label.setText(displayText)
    tela_linha9.label.setText(displayText)
    tela_linha10.label.setText(displayText)

# Cria o programa.
app = QtWidgets.QApplication([])


# Atribui as telas às variáveis.
tela_lista = uic.loadUi("tela_lista.ui")
primeira_tela = uic.loadUi("segunda_tela.ui")
tela_linha1 = uic.loadUi("ProjetoPython.ui")
tela_linha2 = uic.loadUi("linha2.ui")
tela_linha3 = uic.loadUi("linha3.ui")
tela_linha4 = uic.loadUi("linha4.ui")
tela_linha5 = uic.loadUi("linha5.ui")
tela_linha6 = uic.loadUi("linha6.ui")
tela_linha7 = uic.loadUi("linha7.ui")
tela_linha8 = uic.loadUi("linha8.ui")
tela_linha9 = uic.loadUi("linha9.ui")
tela_linha10 = uic.loadUi("linha10.ui")

# Mudar ícone de todas as janelas
primeira_tela.setWindowIcon(QIcon('bus.png'))
tela_lista.setWindowIcon(QIcon('bus.png'))
tela_linha1.setWindowIcon(QIcon('bus.png'))
tela_linha2.setWindowIcon(QIcon('bus.png'))
tela_linha3.setWindowIcon(QIcon('bus.png'))
tela_linha4.setWindowIcon(QIcon('bus.png'))
tela_linha5.setWindowIcon(QIcon('bus.png'))
tela_linha6.setWindowIcon(QIcon('bus.png'))
tela_linha7.setWindowIcon(QIcon('bus.png'))
tela_linha8.setWindowIcon(QIcon('bus.png'))
tela_linha9.setWindowIcon(QIcon('bus.png'))
tela_linha10.setWindowIcon(QIcon('bus.png'))

# Botão que chama a tela de linhas de ônibus.
primeira_tela.pushButton_2.clicked.connect(chama_segunda_tela)

# Botão que chama a tela da linha 1.
tela_lista.linha1.clicked.connect(chama_linha1)
tela_linha1.voltarButton.clicked.connect(botao_voltar_linha1)

# Botão que chama a tela da linha 2.
tela_lista.linha2.clicked.connect(chama_linha2)
tela_linha2.voltarButton.clicked.connect(botao_voltar_linha2)

# Botão que chama a tela da linha 3.
tela_lista.linha3.clicked.connect(chama_linha3)
tela_linha3.voltarButton.clicked.connect(botao_voltar_linha3)

# Botão que chama a tela da linha 4.
tela_lista.linha4.clicked.connect(chama_linha4)
tela_linha4.voltarButton.clicked.connect(botao_voltar_linha4)

# Botão que chama a tela da linha 5.
tela_lista.linha5.clicked.connect(chama_linha5)
tela_linha5.voltarButton.clicked.connect(botao_voltar_linha5)

# Botão que chama a tela da linha 6.
tela_lista.linha6.clicked.connect(chama_linha6)
tela_linha6.voltarButton.clicked.connect(botao_voltar_linha6)

# Botão que chama a tela da linha 7.
tela_lista.linha7.clicked.connect(chama_linha7)
tela_linha7.voltarButton.clicked.connect(botao_voltar_linha7)

# Botão que chama a tela da linha 8.
tela_lista.linha8.clicked.connect(chama_linha8)
tela_linha8.voltarButton.clicked.connect(botao_voltar_linha8)

# Botão que chama a tela da linha 9.
tela_lista.linha9.clicked.connect(chama_linha9)
tela_linha9.voltarButton.clicked.connect(botao_voltar_linha9)

# Botão que chama a tela da linha 10.
tela_lista.linha10.clicked.connect(chama_linha10)
tela_linha10.voltarButton.clicked.connect(botao_voltar_linha10)

timer = QTimer(tela_linha1)
timer.timeout.connect(displayTime)
timer.start(1000)

# Executa o programa.
primeira_tela.show()
app.exec()