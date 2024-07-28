# pip install pandas openpyxl numpy

import pyautogui
from time import sleep
import pandas

# Entrar no navegador
# Acessar e logar no site (https://dlp.hashtagtreinamentos.com/python/intensivao/login)
# Preencher Formulario

def preencher_campo(item):
    pyautogui.press("tab")
    cod = tabela.loc[linha, item]
    
    if item == "obs":
        if cod != "Nan":
            pyautogui.write("")
    else:
        pyautogui.write(str(cod))

pyautogui.PAUSE = 0.5 # comando de pausa antes de cada codigo pyautogui

# Entrar no navegador
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
pyautogui.hotkey("ctrl", "n")

#Acessar e logar site
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
sleep(3)
pyautogui.press("tab")
pyautogui.hotkey("ctrl", "a")
pyautogui.write("clarabranches@gmail.com")
pyautogui.press("tab")
pyautogui.write("clara123")
pyautogui.press("tab")
pyautogui.press("enter")

# Preencher Formulario - codigo,marca,tipo,categoria,preco_unitario,custo,obs
sleep(2)
tabela = pandas.read_csv("produtos.csv")
for linha in tabela.index:
    preencher_campo("codigo")
    preencher_campo("marca")
    preencher_campo("tipo")
    preencher_campo("categoria")
    preencher_campo("preco_unitario")
    preencher_campo("custo")
    preencher_campo("obs")

    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.press("f5")