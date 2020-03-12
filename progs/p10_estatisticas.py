#P10: Estatísticas Básicas
import pandas as pd  

#(1)-Importa a base de dados para um DataFrame
df_lojas = pd.read_csv('lojas.csv')

#(2)-Estatísticas básicas da variável “salario” (numérica)
print('- Estatísticas da variável salário: ')
print('média        : {:.2f}'.format(df_lojas['salario'].mean()))
print('mediana      : {:.2f}'.format(df_lojas['salario'].median()))
print('variância    : {:.2f}'.format(df_lojas['salario'].var()))
print('desvio padrão: {:.2f}'.format(df_lojas['salario'].std()))

#(3)-Estatísticas básicas da variável “uf” (categórica)
print('\n- Estatísticas da variável uf: ')
print('moda: ', df_lojas['uf'].mode()) 
print('domínio: ', df_lojas['uf'].unique())#retorna todas as categorias distintas
print('freq. das categorias:') 
print(df_lojas['uf'].value_counts()) #retorna a freq. de cada categoria
