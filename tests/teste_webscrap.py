#webdriver: é o controle da tela no navegador. Responsável por cliques, navegações, etc.  
#service: dentro do webdriver, é quem fala direta e especificamente com o Google Chrome  
#By: responsável pelas buscas no HTML
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#Padrão de inicialização
service = Service()
options = webdriver.ChromeOptions()
options.add_experimental_option(
     "prefs",
     {"plugins.always_open_pdf_externally": True}
)

# Aqui o ChromeDriver é iniciado, retorna esse objeto "driver" para controle do navegador
driver = webdriver.Chrome(service=service, options=options)

driver.maximize_window() #maximiza a tela

url = 'https://suap.ifsp.edu.br/'
driver.get(url)

wait = WebDriverWait(driver, 20)

#função para o clique
def click(xpath):
     element = wait.until(
          EC.element_to_be_clickable((By.XPATH, xpath))
     )
     element.click()

def login ():
     username = "mudar-para-sua-matricula" #MUDAR PARA RODAR
     password = "mudar-para-sua-senha" #MUDAR PARA RODAR
     
     #preencher matrícula 
     username_field = wait.until(
          EC.element_to_be_clickable((By.XPATH, '//input[@id="id_username"]'))
     )

     username_field.clear()
     username_field.send_keys(username) 

     #preencher senha
     password_field = wait.until(
          EC.element_to_be_clickable((By.XPATH, '//input[@id="id_password"]'))
     )

     password_field.clear()
     password_field.send_keys(password) 

     #botão enviar
     click('//input[@type="submit" and @value="Acessar"]')

login()

#Abrindo o perfil
click('//div[contains(@class, "photo-circle")]')

#Abrindo dropdown de documentos
click('//a[contains(@class, "default")]')

#Selecionando Carteirinha
click('//a[normalize-space()="Comprovante de Dados Acadêmicos"]')


#Encerra o navegador
input("Pressione Enter para fechar...")
driver.quit()