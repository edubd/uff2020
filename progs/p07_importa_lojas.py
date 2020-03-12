#P07: Importação de CSV padrão para DataFrame
import pandas as pd  

#(1)-Importa a base de dados para um DataFrame
df_lojas = pd.read_csv('lojas.csv')
print(df_lojas) 
          
#(2)-mostra o total de linhas e colunas
print('------------------------------------')           
num_linhas = df_lojas.shape[0]
num_colunas = df_lojas.shape[1]
print("número de linhas: ", num_linhas)
print("número de colunas: ", num_colunas)    

#(3)-primeiras linhas - head()
print('------------------------------------')           
print("primeiras linhas\n: ", df_lojas.head())

#(4)-últimas linhas - tail()
print('------------------------------------')           
print("primeiras linhas\n: ", df_lojas.tail())
