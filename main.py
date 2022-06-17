from os import listdir
from selenium import webdriver
import pyautogui as bot
import time

def listar_arquivos(caminho=None):
    lista_arqs = [arq for arq in listdir(caminho)]
    return lista_arqs


if __name__ == '__main__':
    #definir pasta a ser feito upload...
    caminho = '/users/usuario/code/compress_images/in/'
    arquivos = listar_arquivos(caminho=caminho)
    print(arquivos)

    #altera caminho para usar no upload de arquivos
    caminho = caminho.replace("/", "\\")

    # inicia navegador
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--disable-application-cache")
    navegador = webdriver.Chrome(chrome_options=chrome_options)
    navegador.get('https://tinypng.com/')
    time.sleep(5)
    #

    # inicia upload baseado na lista de arquivos
    for i in range(len(arquivos)):
        navegador.find_element_by_xpath('//*[@id="top"]/section/div[1]/section/figure').click()
        time.sleep(2)
        bot.typewrite(f'c:{caminho}{arquivos[i]}')
        time.sleep(2)
        bot.press("enter")
        time.sleep(2)


    navegador.find_element_by_xpath('//*[@id="zip"]/button').click()
    time.sleep(10)
    navegador.close()