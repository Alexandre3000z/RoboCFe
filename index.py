#Importando navegador
from config.browserConfig import Chorme

#Importanto função de autenticação
from auth import validateAcess

#INTERFACE GRÁFICA
from Interface.front import startInterface
from Interface.app_state import app_state


acessValidator = validateAcess() #True or False

driver = Chorme()




