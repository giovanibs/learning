from datetime import datetime
import shutil
import subprocess
import pyautogui
import os
from time import time, sleep

wdir = os.getcwd()
pasta_entrada = 'entrada'
pasta_processando = 'processando'
pasta_finalizado = 'finalizado'

def copy2clip(txt):
    cmd='echo '+txt.strip()+'|clip'
    return subprocess.check_call(cmd, shell=True)

def click_cor(cor):
    if cor == "amarelo":
        pyautogui.click(985, 60, clicks=2, interval=0.5)       # coord funcionam apenas com a janela maximizada
    elif cor == "azul":
        pyautogui.click(1025, 60, clicks=2, interval=0.5)
    else: # "vermelho"
        pyautogui.click(940, 60, clicks=2, interval=0.5)

def click_forma(forma):
    if forma == "circulo":
        pyautogui.click(485, 65)       # coord funcionam apenas com a janela maximizada
    elif forma == "retangulo":
        pyautogui.click(505, 65)
    else: # "triangulo"
        pyautogui.click(565, 65)

for filename in os.listdir(pasta_entrada):
    file_src = os.path.join(pasta_entrada, filename)
    is_txt = os.path.splitext(filename)[1] == '.txt'
    
    if is_txt: shutil.move(file_src, pasta_processando)

sleep(1)

for filename in os.listdir(pasta_processando):
    file_src = os.path.join(pasta_processando, filename)
    forma = ''
    cor = ''
    ts = datetime.now()
    #FileRead, OutputVar, % A_LoopFileFullPath
    with open(file_src) as f:
        input = f.read()
        forma = input.split(';')[0]
        cor = input.split(';')[1]

    mspaint = 'valida\mspaint.png'
    pyautogui.click(mspaint)
    sleep(2)
    click_forma(forma)
    sleep(0.5)
    pyautogui.click('valida\preenchimento.png')
    sleep(0.5)
    pyautogui.click('valida\cor_solida.png')
    sleep(0.5)
    pyautogui.click('valida\cor2.png')
    sleep(0.5)
    click_cor(cor)
    sleep(0.5)
    pyautogui.moveTo(15, 155)
    pyautogui.drag(100, 100)
    pyautogui.move(50, 50)
    pyautogui.click()

    valida_desenho = os.path.join(wdir, 'valida', f'{forma}_{cor}.png')    
    try:
        coord_desenho = pyautogui.locateOnScreen(valida_desenho)
        print('Desenho validado')
    except pyautogui.ImageNotFoundException:
        print('Imagem não encontrada')
    except:
        print('Ocorreu algum erro na validação da imagem')

    if coord_desenho:
        pasta_output = ts.strftime(r'%Y-%m-%d %H-%M-%S')
        new_dir = os.path.join(wdir, pasta_finalizado, pasta_output)
        os.makedirs(new_dir)
        new_file_name = os.path.join(new_dir, f'{forma}_{cor}.png')
        print(f'Salvando desenho em:\n{new_file_name}')
        pyautogui.press('F12')
        
        #copy_to_clipboard(new_file_name)
        copy2clip(new_file_name)
        sleep(2)
        pyautogui.hotkey('ctrl', 'v')
        sleep(0.5)
        pyautogui.press('enter')
        sleep(2)
        pyautogui.hotkey('alt', 'F4')

        # move arquivo txt
        shutil.move(file_src, new_dir)