from utils.driverFunctions import *

def company_finder_AmbSeg(driver, companyCode):
    
    try:
        # Aguarde a tabela carregar
        WebDriverWait(driver, 40).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="form1"]/table'))
        )
    
    except:
        print('O ambiente seguro está instável, tente novamente mais tarde...')
        return    

    #Lista das linhas
    linhas = driver.find_elements(By.XPATH, '//*[@id="form1"]/table/tbody/tr')
    
    for linha in linhas:
        celula = linha.find_element(By.XPATH, './td[1]')
        celulaNome = linha.find_element(By.XPATH, './td[2]') # Ajustar índice conforme necessário
        textoNome = celulaNome.text
        texto_da_celula = celula.text
        inscricaoEstadual = companyCode.lstrip('0')

        if(texto_da_celula == inscricaoEstadual):
            celula.click()
            print('Inscrição estadual: ',texto_da_celula,' Empresa: ', textoNome)
            break