#P11: groupby()
import pandas as pd  

#(1)-Importa a base de dados para um DataFrame
df_lojas = pd.read_csv('lojas.csv')

#(2)-Gera uma variável "grouped" onde a chave é "uf" e a medida "po"
grupo_po_uf = df_lojas['po'].groupby(df_lojas['uf'])

#(3)-Computa agregados a partir da variável gerada
print('- Soma do PO, por UF: ',grupo_po_uf.sum())
print('-----------------------------------')
print('- Total de lojas, por UF:', grupo_po_uf.count())