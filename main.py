#py

import pyautogui
import time

pyautogui.alert('o código vai começar. nao use nada do seu computador.')
pyautogui.PAUSE = 0.5
#abrir o google drive no meu computador
pyautogui.press('winleft')
pyautogui.write('Firefox')
pyautogui.press('enter')
time.sleep(1)      #o código espera para rodar por 1 segundo enquanto o navegador abre

#localizar barra de tarefas
pyautogui.hotkey('ctrl','l')
pyautogui.write('https://drive.google.com/drive/my-drive')
time.sleep(1)
pyautogui.press('enter')

#entrar na minha área de trabalho/pasta do arquivo
pyautogui.hotkey('winleft', 'd')

#clicar no arquivo que eu quero fazer backup e arrasta-lo
pyautogui.moveTo(1810, 61)
pyautogui.mouseDown() #clica e segura o mouse - botao esquerdo
pyautogui.moveTo(1515,687)

#enquanto arrasto o arquivo, eu mudo pro google drive
pyautogui.hotkey('alt','tab')
time.sleep(1)
#largar o arquivo no google drive
pyautogui.mouseUp()  #solta o botao do mouse

#esperar 5 segundos
time.sleep(5)
pyautogui.alert('O código acabou de rodar. Pode usar o pc novamente.')

