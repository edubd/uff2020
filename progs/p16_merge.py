#P16: junção de DataFrames
import pandas as pd    

#(1)-importa os CSVs
df_emps = pd.read_csv('emps.csv')
df_lojas = pd.read_csv('lojas.csv')

print('Empresas: '); print(df_emps)
print('------------------------------------------------')
print('Lojas: '); print(df_lojas)
print('------------------------------------------------')

#(2)-Combina os Arquivos

#2.1 INNER JOIN
c1 = pd.merge(df_emps, df_lojas, how='inner', on='raiz')
print('resultado do INNER JOIN: ')
print(c1)
print('------------------------------------------------')

#2.2 LEFT JOIN
c2 = pd.merge(df_emps, df_lojas, how='left', on='raiz')
print('resultado do LEFT JOIN: ')
print(c2)
print('------------------------------------------------')

#2.3 FULL OUTER JOIN
c3 = pd.merge(df_emps, df_lojas, how='outer', on='raiz')
print('resultado do FULL OUTER JOIN: ')
print(c3)
print('------------------------------------------------')
