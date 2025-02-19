#Utils
from utils.CompanyFormater import formatCompanyCode
from utils.csvReader import readCSV

#Importando navegador
from config.browserConfig import Chorme

#Importanto função de autenticação
from auth.validateAcess import authorize_access

#INTERFACE GRÁFICA
from Interface.front import startInterface
from Interface.app_state import app_state

#Scripts todos os passos
from scripts.start import startProcess
from scripts.company_finder import companyFinder
from scripts.sigetWindow import enterSiget
from scripts.searchCsv import downloadCsvAut,downloadCsvCancel

import time
import os

from classes.CFElist import cfe_list

downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")

acessValidator = authorize_access() #True or False


try:
    if acessValidator:
        startInterface()
        
        driver = Chorme()
        
        startProcess(driver)
        
        formatedCode = formatCompanyCode(app_state.inscricao_estadual)
        
        companyFinder(driver, formatedCode)
        
        enterSiget(driver)
        
        responseAut = downloadCsvAut(driver)
        if responseAut == True:
            readCSV(downloads_path, 'Autorizados')
            
        responseCancel = downloadCsvCancel(driver)
        if responseCancel == True:
            readCSV(downloads_path, 'Cancelados')
        
        print(cfe_list.totalList)
        print(len(cfe_list.totalList))
        
        
        time.sleep(1000)
    else:
        raise Exception('Chave de acesso inválida, por gentileza, fale com seu administrador...')

except Exception as e:
    print(f'Erro: {e}')