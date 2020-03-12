#P09: Seleção
import pandas as pd  

#Importa a base de dados para um DataFrame
df_lojas = pd.read_csv('lojas.csv')

#gera um novo DataFrame contendo apenas as lojas do RJ
v = (df_lojas['uf']=='RJ') #gera a Series booleana
df_rj = df_lojas[v]        #filtra as linhas  

#gera um novo DataFrame contendo apenas as lojas do RJ c/ 50 ou mais funcionários
v = (df_lojas['uf']=='RJ') & (df_lojas['po']>=50) #gera a Series booleana
df_rj_grandes = df_lojas[v]                       #filtra as linhas

#imprime os DataFrames
print(df_rj) 
print('-------------------------------------------')
print(df_rj_grandes) 