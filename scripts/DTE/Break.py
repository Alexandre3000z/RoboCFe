from utils.driverFunctions import *

import keyboard, autoit, mouse


def passBreak(driver):
    
    # Aguarda até que a tecla Enter seja pressionada ou o botão esquerdo do mouse seja clicado
    while True:
        if keyboard.is_pressed("enter") or mouse.is_pressed("left"):
            break
    
    time.sleep(11)
    autoit.send('{ENTER}')
    time.sleep(5)
    autoit.send('{ENTER}')
    time.sleep(1)
    
    
    # Guarda o identificador da janela original
    original_window = driver.current_window_handle

    # Espera até que uma nova janela esteja aberta
    WebDriverWait(driver, 6).until(EC.number_of_windows_to_be(2))

    # Captura todos os identificadores de janelas abertas
    windows = driver.window_handles

    # Muda para a nova janela
    for window in windows:
        if window != original_window:
            driver.switch_to.window(window)
            break
    
    
    try:
        error = locateByXpath(driver,10,'//*[@id="modalMensagem"]/div/div/div[2]/div/div[2]/div/div/label')
        error.click()
    except:
        print('Sem avisos continuando')    