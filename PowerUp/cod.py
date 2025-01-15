import pyautogui
import time
import pandas as pd
import dados

pyautogui.PAUSE = 0.5

# Passo 1: Abrir o sistema da empresa
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
time.sleep(3)
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

time.sleep(2)

# Passo 2: Fazer o login
pyautogui.click(x=496, y=374)
#inserindo email
pyautogui.write(dados.USER)
pyautogui.press("tab")
#inserindo senha
pyautogui.write(dados.PASSWORD)
pyautogui.press("tab")
#inserindo logando
pyautogui.press("enter")

# Passo 3: Importar a base de dados dos produtos
tabela = pd.read_csv(r"C:\Users\isado\Documents\Jornada Python\PowerUp\produtos.csv")
print(tabela)

time.sleep(2)

# Passo 4: Cadastrar 1 produto
#Primeiro produto sempre é aconselhado cadastrar manualmente

#index = linhas
for linha in tabela.index:

    pyautogui.click(x=603, y=262)

    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")

    marca = tabela.loc[linha, "marca"]
    pyautogui.write(str(marca))
    pyautogui.press("tab")

    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(str(tipo))
    pyautogui.press("tab")

    categoria = tabela.loc[linha, "categoria"]
    pyautogui.write(str(categoria))
    pyautogui.press("tab")

    preco_unitario = tabela.loc[linha, "preco_unitario"]
    pyautogui.write(str(preco_unitario))
    pyautogui.press("tab")

    custo = tabela.loc[linha, "custo"]
    pyautogui.write(str(custo))
    pyautogui.press("tab")

    obs = str(tabela.loc[linha, "obs"])

    if obs != "nan":
        pyautogui.write(obs)

    pyautogui.press("tab")

    pyautogui.press("enter") #para cadastrar

    #numero positivo = scroll pra cima
    #numero negativo scroll pra baixo
    pyautogui.scroll(10000)

# Passo 5: Repetir o passo 4 até acabar todos os produtos