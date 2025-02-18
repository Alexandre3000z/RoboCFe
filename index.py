#Importando navegador
from config.browserConfig import Chorme

#Importanto função de autenticação
from auth.validateAcess import authorize_access

#INTERFACE GRÁFICA
from Interface.front import startInterface
from Interface.app_state import app_state


acessValidator = authorize_access() #True or False



if acessValidator:
    startInterface()
    
    driver = Chorme()


