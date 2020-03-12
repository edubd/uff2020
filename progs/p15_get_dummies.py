#P15: get_dummies()
import pandas as pd  

#(1)-Importa a base de dados para um DataFrame
df_lojas = pd.read_csv('lojas.csv')

#(2)-gera k atributos binários a partir do atributo “uf”
dummies = pd.get_dummies(df_lojas['uf'], prefix="uf")
df_lojas = df_lojas.join(dummies)

#(3)-Projeta o nome fantasia, a uf e os novos atributos
print(df_lojas[['fantasia','uf','uf_RJ','uf_SP','uf_MG','uf_RS']])