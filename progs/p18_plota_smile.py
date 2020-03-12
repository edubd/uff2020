#P18: desenha smile
import pandas as pd    

#(1)-importa os CSVs
df_smile = pd.read_csv('smile.csv')
df_smile.columns = ["x","y"]

#(2)-imprime as primeiras linhas (só para checar...)
print(df_smile.head())

#(3)-imprime um sumário das estatísticas de “x” e “y”
print(df_smile.describe())

#(4)-plota o gráfico
df_smile.plot(kind="scatter",x="x",y="y")