#Importando navegador
from config.browserConfig import Chorme

#Importanto função de autenticação
from auth import validateAcess

#INTERFACE GRÁFICA
from Interface.front import executarFront
from Interface.app_state import app_state

acessValidator = validateAcess()

driver = Chorme()

driver.get('https://portal-dte.sefaz.ce.gov.br/#/home')


