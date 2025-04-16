from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

try:
    url = "https://www.hankeds.com.br/prova/login.html" #Define a URL do site que será acessado.
    driver.get(url) #O driver 'recebe' a URL

    time.sleep(2)

    def digitar_lento(elemento, texto, delay=0.25): #Metodo para a digitação ocorrer com um delay de 0.25 segundos
        for letra in texto: elemento.send_keys(letra)
        time.sleep(delay)

    usuario = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "username"))) #
    senha = driver.find_element(By.ID, "password") #Encontra o elemento da senha 
    botao = driver.find_element(By.XPATH, "//button[contains(text(), 'Entrar')]") #Encontra o elemento do botão

    digitar_lento(usuario, "admin") #define o que será escrito no username
    time.sleep(1)
    digitar_lento(senha, "admin123456") #define o que será escrito na senha
    time.sleep(1)

    botao.click()
    time.sleep(4)

    if "destino.html" in driver.current_url: #Define que se for redirecionado para página destino.html, será exibido a mensagem no terminal
        print(" Teste passou: redirecionado corretamente.")
    else: #Define que se não for redirecionado para página destino.html, será exibido a mensagem no terminal
        print(" Teste falhou: redirecionamento não ocorreu.")

    time.sleep(5)

except Exception as e: #Define que caso de um erro não esperado, ele exibirá a mensagem.
    print(" Erro durante o teste:", str(e))

finally:
    driver.quit()