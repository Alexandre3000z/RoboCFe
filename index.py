from config.browserConfig import Chorme


#INTERFACE GRÁFICA
from Interface.front import executarFront
from Interface.app_state import app_state

driver = Chorme()

driver.get('https://portal-dte.sefaz.ce.gov.br/#/home')


