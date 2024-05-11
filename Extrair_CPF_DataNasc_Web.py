from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from datetime import datetime

# URL que será acessada para capturar CPF e Data de Nascimento
# Estes CPFs não são válidos, porém não são quentes, ou seja, não constar no site da RF - Receita Federal
# Sendo assim podem serem utilizados em um Ambiente de Stage ou Produção
# 'https://servicos.receita.fazenda.gov.br/Servicos/CPF/ConsultaSituacao/ConsultaPublica.asp'
url_cpf = 'https://geradorbrasileiro.com/pessoa'
driver = webdriver.Firefox()
driver.maximize_window()
driver.get(url_cpf)
time.sleep(5)

cont = 0
qtdeCPF = 50

with open("cpf_datanasc.csv", 'a+', newline="") as arquivo:
    while cont < qtdeCPF:
       # Botão Gerar Pessoa
        btn_gerar_pessoa = driver.find_element(By.XPATH,'/html/body/div/div[2]/div[1]/div[3]/div[2]/div/div/button')
        btn_gerar_pessoa.click()
        time.sleep(2)

        # CPF
        cpf = driver.find_element(By.ID, 'cpf').get_attribute('value')
        print('CPF: ', cpf)
        cpf = cpf.replace('.', '').replace('-', '')
        print('CPF: ', cpf, '\n')

        # Data de Nascimento
        data_nasc = driver.find_element(By.ID, 'dataNascimento').get_attribute('value')
        print('Data de Nascimento: ', data_nasc)
        # data = str(data_nasc)
        # data_nasc = data.strftime('%d%m%Y')
        date_object = datetime.strptime(data_nasc, '%d/%m/%Y').date()
        data_nasc = date_object.strftime('%d%m%Y')
        print('Data com a formatação e SEM AS BARRAS, para uso no cadastro: ', data_nasc, '\n')

        time.sleep(3)
        arquivo.write(cpf + ';' + data_nasc + ';\n')
        cont += 1
        print(cont, ". ", cpf + ';' + data_nasc, '\n')
        arquivo.flush()
        time.sleep(3)

arquivo.close()
driver.close()

