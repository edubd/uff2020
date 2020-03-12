#P08: Projeção
import pandas as pd  

#Importa a base de dados para um DataFrame
df_lojas = pd.read_csv('lojas.csv')

#gera um novo DataFrame apenas com a uf, po e salário (nesta ordem)
df_uf_po_sal = df_lojas[['uf','po','salario']]
print(df_uf_po_sal)           