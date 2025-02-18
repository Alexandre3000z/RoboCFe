from Interface.app_state import app_state

def startProcess(driver):
    
    numero_formatado = f"{app_state.inscricao_estadual[:2]}.{app_state.inscricao_estadual[2:5]}.{app_state.inscricao_estadual[5:8]}-{app_state.inscricao_estadual[8]}"
    driver.get('https://portal-dte.sefaz.ce.gov.br/#/index')
    print(numero_formatado)