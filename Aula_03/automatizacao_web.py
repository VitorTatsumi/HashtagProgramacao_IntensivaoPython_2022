#Chromedriver precisa estar na mesma pasta que o Python 
#Dica: Olhar no caminho do erro
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from datetime import date

#Abrir navegador
navegador = webdriver.Chrome()

#Ir para determinado site 
navegador.get('https://www.google.com/')
#Digitar determinado texto através do sendkeys no local determinado através do xpath
#Para encontrar o XPATH -> Clicar com o botão direito na tela -> Clicar em Inspecionar elemento -> Clicar na setinha e selecionar o elemento - > Clicar em Copy e Copy XPath
navegador.find_element('xpath', '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys('Cotação dólar')
navegador.find_element('xpath', '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]').send_keys(Keys.ENTER)
#Pega o elemento específico, neste caso o data-value
cotacao_dolar = navegador.find_element('xpath', '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')
print(cotacao_dolar)

#Cotação do euro
navegador.get('https://www.google.com/')
navegador.find_element('xpath', '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys('Cotação euro')
navegador.find_element('xpath', '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]').send_keys(Keys.ENTER)
cotacao_euro = navegador.find_element('xpath', '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')
print(cotacao_euro)

#Cotação do ouro
navegador.get('https://www.melhorcambio.com/ouro-hoje')
cotacao_ouro = navegador.find_element('xpath', '//*[@id="comercial"]').get_attribute('value')
#Como o resultado do valor Ouro possui vírgulas, será utilizado o replace para substituir o conteúdo
cotacao_ouro = cotacao_ouro.replace(',', '.')
print(cotacao_ouro)

#Fechar navegador
navegador.quit()

#Lê o arquivo Excel e adiciona à variável tabela como uma matriz
tabela = pd.read_excel('Produtos.xlsx')
print(tabela)

#Modifica na coluna Cotação todos os valores que forem Dólar na coluna Moeda
#Dica de ouro: Modifica um valor especifico numa tabela
tabela.loc[tabela['Moeda'] == 'Dólar','Cotação'] = float(cotacao_dolar)
tabela.loc[tabela['Moeda'] == 'Euro','Cotação'] = float(cotacao_euro)
tabela.loc[tabela['Moeda'] == 'Ouro','Cotação'] = float(cotacao_ouro)
print(tabela)

#Calcular os valores
tabela['Preço de Compra'] = (tabela['Preço Original'] * tabela['Cotação'])
tabela['Preço de Venda'] = (tabela['Preço de Compra'] * tabela['Margem'])
print(tabela)

#Cria um arquivo Excel atualizado com todas as informações
#Index como False para que não seja exibida a primeira coluna com informações inúteis
tabela.to_excel('Produtos Novo.xlsx', index=False)
