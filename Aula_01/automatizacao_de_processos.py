'''
O código tem a função de abrir automaticamente o navegador Google Chrome, colar um link específico e acessar uma das pastas, fazer o download do arquivo necessário e abri-lo no terminal. 
O código ainda está incompleto, pois ao final ainda é necessário automatizar o envio do arquivo atualizado através do Gmail.
'''
import pyautogui
import pyperclip
import time
import pandas

#Delay padrão em todas as ações do Pyautogui
pyautogui.PAUSE = 0.25
#Abrindo o Google Chrome
pyautogui.hotkey('win', 'r')
pyautogui.write('chrome.exe')
pyautogui.press('enter')
#O comando copy do pyperclip permite que seja copiado no momento atual o texto desejado
#O Pyautogui não consegue digitar caracteres especiais como ? utilizando o comando write, por isso, utiliza-se este macete onde é copiado o texto e colado 
pyperclip.copy('https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga')
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('enter')

time.sleep(2)
#Click em determinado campo da tela através dos parâmetros X/Y e informada a quantidade de clicks
pyautogui.click(x=405, y=269, clicks = 2)
time.sleep(2)
pyautogui.click(x=382, y=302, clicks= 1)
time.sleep(2)
pyautogui.click(x=1728, y=149, clicks = 1)
time.sleep(2)
pyautogui.click(x=1521, y=592, clicks = 1)
time.sleep(5)
pyautogui.click(x=1757, y=1002, clicks = 1)
time.sleep(3)

import pandas as pd

#Atribui o arquivo à uma variável e executa o comando para exibir
tabela = pd.read_excel(r'C:\Users\Vitor Tatsumi\Downloads\Vendas - Dez.xlsx')
pd.set_option('display.max_columns', None)
print(tabela)

'''
Macete para descobrir a posição do cursor do mouse:
time.sleep(5)
print(pyautogui.position())
'''
