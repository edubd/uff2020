#P12: boxplot
import pandas as pd  

#(1)-Importa a base de dados para um DataFrame
df_lojas = pd.read_csv('lojas.csv')

#(2)-Gera o boxplot
boxplot = df_lojas.boxplot(column=['salario'], showmeans=True)
