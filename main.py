# pip install pyautogui

# Passo 1: Abrir o sistema da empresa
    # Sistema: https://dlp.hashtagtreinamentos.com/python/intensivao/login
import pyautogui
import time
import pandas as pd

# cada comando pausa 3 milissegundos
pyautogui.PAUSE = 0.3

# abre navegador
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

# entrar no link
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(3)

# Passo 2: Fazer login
pyautogui.click(x=576, y=364)
pyautogui.write("pythonimpressionador@gmail.com")
pyautogui.press("tab")
pyautogui.write("Strong@.10%")
pyautogui.click(x=664, y=516)
time.sleep(3)

#Passo 3: Importar a base de dados dos produtos
tabela = pd.read_csv("produtos.csv")

print(tabela)

#Passo 5: Repetir o passo 4 até acabar todos os produtos
for linha in tabela.index:
    #Passo 4: Cadastrar produto
    pyautogui.click(x=606, y=257)
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")

    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    
    pyautogui.press("tab")

    pyautogui.press("enter")

    pyautogui.scroll(5000)