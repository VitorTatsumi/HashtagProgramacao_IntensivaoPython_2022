import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split


#Atribuindo o arquivo à variável
tabela = pd.read_csv('advertising.csv')
print(tabela)
print(tabela.info())
#Cria a correlação da tabela
print(tabela.corr())

#Criar gráfico de calor
#Cmap muda a cor, deve selecionar o nome do estilo de cores
#Annot é o comdando que exibe as anotações no gráfico, os dados no caso
sns.heatmap(tabela.corr(), cmap='Wistia', annot=True)

#Exibir gráfico
plt.show()

#Separar a base de dados em 2
#Y é quem eu quero prever
#X é quem eu vou usar para a previsão
y = tabela['Vendas']
#Aspas duplas SEMPRE que for utilizar mais de uma coluna
x = tabela[["TV", "Radio","Jornal"]]

#Para se trabalhar com inteligência artificial é importante atentar-se à divisão da base de dados, separando cerca de 70% para treino da IA e 30% para utiliza-los em testes
#Separar agora a base de dados em 4 partições e definir 30% para dados de teste
#As variáveis devem ser passadas nessa ordem
#Random_state para definir a estaticidade da randomização, no caso limitada somente a 1 opção de randomização dos valores das variáveis
x_treino, x_teste, y_treino, y_teste = train_test_split(x, y, test_size = 0.3, random_state = 1)

#Importando inteligência artificial
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor 

#cria a inteligência artificial
modelo_regressaolinear = LinearRegression()
modelo_arvoredecisao = RandomForestRegressor()

#Treina os dois modelos de inteligência artificial
modelo_regressaolinear.fit(x_treino, y_treino)
modelo_arvoredecisao.fit(x_treino, y_treino)

#Fazer previsão nos testes

previsao_regressaolinear = modelo_regressaolinear.predict(x_teste)
previsao_arvoredecisao = modelo_arvoredecisao.predict(x_teste)

from sklearn.metrics import r2_score

print(r2_score(y_teste, previsao_regressaolinear))
print(r2_score(y_teste, previsao_arvoredecisao))
