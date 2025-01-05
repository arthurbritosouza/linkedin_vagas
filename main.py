# %%
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

#caminho atual da pasta
dir_path = os.getcwd()

#configurar o navegador
options = Options()

#salva o loguin
options.add_argument(r"user-data-dir=" + os.path.join(dir_path, "conta/linkedin"))

#permite controlar o navegador
driver = webdriver.Chrome(options=options)

#acessar o site definido
driver.get("https://www.linkedin.com/jobs/")
time.sleep(4)


# %%
#acha o campo de pesquisa
campo_pesquisa = WebDriverWait(driver, 20).until(
    EC.visibility_of_element_located((By.XPATH, "//input[@aria-label='Pesquisar cargo, competência ou empresa']"))
)
campo_pesquisa.click()

#pesquisa a informação enviada
pesquisa = input("faça uma pesquisa de vagas e pressione enter: ")
campo_pesquisa.send_keys(pesquisa)
campo_pesquisa.send_keys(Keys.RETURN)
time.sleep(6)



# %%
#seleciona a data dos anuncios
data_anuncio = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="searchFilter_timePostedRange"]')))
data_anuncio.click()
time.sleep(2)


data_resultado = driver.find_elements(By.CSS_SELECTOR, ".t-14.t-black--light.t-normal")
input_resultato = int(input("Digite 1 se quer as vagas do último mês, 2 da última semana, 3 para as 24 horas: "))
if input_resultato == 1:
    data_resultado[1].click()
elif input_resultato == 2:
    data_resultado[2].click()
elif input_resultato == 3:
    data_resultado[3].click()
time.sleep(1)

exibir_resultado = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, ".artdeco-button.artdeco-button--2.artdeco-button--primary.ember-view.ml2"))
)
exibir_resultado.click()
time.sleep(3)




# %%
# print(len(empresa_elemento))


# %%
# empresa_elemento = driver.find_elements(By.CLASS_NAME, "PvaypIWSSzaYekZGVDZTENtvQwtUaxUmatY ")[8]
# print(empresa_elemento.text)
url = driver.find_elements(By.CLASS_NAME, "PvaypIWSSzaYekZGVDZTENtvQwtUaxUmatY")[8]
url_vaga = url.get_attribute("href")
print(url_vaga)

# %%
vagas = driver.find_elements(By.CSS_SELECTOR, ".flex-grow-1.artdeco-entity-lockup__content.ember-view")[0:5]
for i in vagas:
    i.click()
    sobre_vaga = driver.find_element(By.XPATH, '/html/body/div[5]/div[3]/div[4]/div/div/main/div/div[2]/div[2]/div/div[2]/div/div[1]/div/div[4]/article/div/div[1]/div').text

    empresa_elemento = driver.find_elements(By.CLASS_NAME, "PvaypIWSSzaYekZGVDZTENtvQwtUaxUmatY")[8]
    nome_empresa = empresa_elemento.text
    link_empresa = empresa_elemento.get_attribute("href")
    
    url = driver.find_elements(By.CLASS_NAME, "PvaypIWSSzaYekZGVDZTENtvQwtUaxUmatY")[8]
    url_vaga = url.get_attribute("href")
    
    #printo as informações
    print(f"Sobre o vaga: {sobre_vaga} \n")
    print(f"Nome da empresa: {nome_empresa} \n")
    print(f"Titulo da vaga: {i.text} \n")
    print(f"Link do perfil da empresa: {link_empresa} \n")
    print(f"Link da vaga: {url_vaga} \n\n\n")
    time.sleep(1)
    
    time.sleep(5)

driver.quit()
