#Importando navegador
from config.browserConfig import Chorme

#Importanto função de autenticação
from auth.validateAcess import authorize_access

#INTERFACE GRÁFICA
from Interface.front import startInterface
from Interface.app_state import app_state

#Scripts todos os passos
from scripts.start import startProcess


acessValidator = authorize_access() #True or False



if acessValidator:
    startInterface()
    
    driver = Chorme()
    
    startProcess(driver)

else:
    print('Chave de acesso inválida, por gentileza, fale com seu administrador...')

numero_formatado = f"{app_state.inscricao_estadual[:2]}.{app_state.inscricao_estadual[2:5]}.{app_state.inscricao_estadual[5:8]}-{app_state.inscricao_estadual[8]}"