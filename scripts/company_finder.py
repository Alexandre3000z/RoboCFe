from Interface.app_state import app_state
import time

from utils.driverFunctions import *

def companyFinder(driver, companyCode):
    
    try:
        
        companyInput = locateByXpath(driver, 30, '/html/body/my-app/div/div/div/app-procuracao/div/form/div/div[1]/input')
        companyInput.send_keys(companyCode)
        
        time.sleep(3)
        
        selectCompany = findElementByXpath(driver, '/html/body/my-app/div/div/div/app-procuracao/div/div[2]/table/tbody/tr[1]')
        selectCompany.click()
        
        time.sleep(1)   
             
    except:
        print('A empresa não se encontra no DTE, criar procuração e tentar novamente.')
        return 