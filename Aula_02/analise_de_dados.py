import pandas as pd
import plotly.express as px

#Lê arquivo CSV
tabela = pd.read_csv('telecom_users.csv')
print(tabela)

# Axis é o parâmetro da tabela (linha/coluna)
# Axis = 0 para linha
# Axis = 1 para coluna
# O comando drop exclui um elemento da tabela
tabela = tabela.drop("Unnamed: 0", axis = 1)
print(tabela)
#Exibe as informações da tabela
print(tabela.info())
# Está transformando a variável tabela em numérica
# Parâmetro Coerce, de coagir, forçar. Então caso haja algum erro, ele irá forçar a execução
tabela['TotalGasto'] = pd.to_numeric(tabela['TotalGasto'], errors='coerce')
print(tabela.info())

'''
tabela = tabela.dropna(how='all', axis = 0)
tabela = tabela.dropna(how='any', axis=1)
print(tabela)
print(tabela.info())
'''

#Valores da coluna específica 
print(tabela['Churn'].value_counts())
#Exibição do conteúdo da coluna formatado em porcentagem
print(tabela['Churn'].value_counts(normalize=True).map('{:.1%}'.format))

#Biblioteca para construção e exibição de gráficos
#import plotly.express as px 

for coluna in tabela.columns:
    #Cria o gráfico
    grafico = px.histogram(tabela, x=coluna, color='Churn')
    #Exibe o gráfico
    grafico.show()
