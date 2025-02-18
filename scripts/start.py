from Interface.app_state import app_state
import time

from utils.driverFunctions import *

def startProcess(driver):
    
    driver.get('https://portal-dte.sefaz.ce.gov.br/#/index')
    
    time.sleep(5)
    
    certificadoDigital = locateByXpath(driver, 30, '/html/body/my-app/div/div/div/app-index/div/div/div[2]/div[1]/div/div/a[1]/div')
    certificadoDigital.click()
    
    time.sleep(3)
     
    certificadoSelect = locateByXpath(driver, 30, '/html/body/my-app/div/div/div/app-certificado/div/ul/li/button')
    certificadoSelect.click()
    
    try:
        
        profile = locateByXpath(driver, 30, '/html/body/my-app/div/div/div/app-perfil/div/div[1]/table/tbody/tr/td[1]')
        profile.click()
        
    except:
        print('Carregamento infinito detectado, corrigindo...')
        driver.refresh()
        
        time.sleep(3)
        
        certificadoSelect = locateByXpath(driver, 30, '/html/body/my-app/div/div/div/app-certificado/div/ul/li/button')
        certificadoSelect.click()
        
        time.sleep(3)
        
        profile = locateByXpath(driver, 30, '/html/body/my-app/div/div/div/app-perfil/div/div[1]/table/tbody/tr/td[1]')
        profile.click()
    
    time.sleep(1)

    enterButton = locateByXpath(driver, 30, '/html/body/my-app/div/div/div/app-perfil/div/div[2]/button[2]')
    enterButton.click()