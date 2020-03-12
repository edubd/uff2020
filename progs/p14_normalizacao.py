#P14: Normalização
import pandas as pd  

#(1)-Importa a base de dados para um DataFrame
df_lojas = pd.read_csv('lojas.csv')

#(2)-Normaliza o “salario”
sal_max = max(df_lojas['salario'])
sal_min = min(df_lojas['salario'])
df_lojas['sal_norm'] = (df_lojas['salario'] - sal_min) / (sal_max - sal_min)

#(3)-Normaliza o “po”
po_max = max(df_lojas['po'])
po_min = min(df_lojas['po'])
df_lojas['po_norm'] = (df_lojas['po'] - po_min) / (po_max - po_min)

#(4)-Após a normalização, remove os atributos originais
df_lojas = df_lojas.drop(columns=['po','salario'])

#(5)-Imprime o DataFrame transformado
print('-----------------------------------')
print('DataFrame após a normalização das variáveis numéricas')
print(df_lojas)
