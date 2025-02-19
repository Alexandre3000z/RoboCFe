from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from utils.driverFunctions import *

import time

def enterSiget(driver):
    try:
        siget = locateByXpath(driver,30, '/html/body/my-app/div/div/div/app-home/section/div/div[2]/div/ul/li[1]')
        time.sleep(10)        
        siget.click()
        
    except:
        try:
            print('Possivel carregamento infinito siget, tentando novamente...')
            driver.refresh()
            time.sleep(5)
            siget = locateByXpath(driver,30, '/html/body/my-app/div/div/div/app-home/section/div/div[2]/div/ul/li[1]')
            time.sleep(10)        
            siget.click()
            time.sleep(10)
                
        except:
            raise Exception('O DTE está instável. tentar novamente mais tarde...')