#P06: Olá DataFrame
import pandas as pd  

#(1)-Há várias maneiras de construir DataFrames. 
#    No exemplo abaixo, o fazemos a partir de um dicionário de listas
dados = {'nome': ['Alex','Carlos','Jane','Rakesh','Elis','Isabel','Andres'],
         'idade': [50,21,55,37,18,42,33],
         'sal': [5000,2000,3500,6500,2000,4500,3500],
         'uf': ['RJ','RJ','SP','SP','RJ','MG','SP']}

df_pessoas = pd.DataFrame(dados)

print('(1)-DataFrame original\n')
print(df_pessoas)           #imprime todo o DataFrame

#(2)-Atribui nomes para os índices (método index) 
#    e modifica os nomes das colunas (método columns)
#    (agora sim vai ficar com o formato igual ao da Figura 22)
print('-------------------------------------------')
print('(2)-DataFrame com novos nomes de índices e colunas\n')
df_pessoas.index = ['P1','P2','P3','P4','P5','P6','P7']
df_pessoas.columns = ['nome','idade','salario','uf']
print(df_pessoas)           

#(3)-INDEXAÇÃO 
#[3.1]-Uma LINHA inteira pode ser recuperada pelo seu rótulo ou posição, 
#      através dos métodos “loc” e “iloc”, respectivamente
print('-------------------------------------------')
print('(3)-Indexação de linhas, colunas e células\n')
print(df_pessoas.loc['P5'])   #recupera a linha com rótulo 'P5' (Elis)
print('\n')  
print(df_pessoas.iloc[0]) #recupera a linha na posição 0 (primeira linha - Alex)

#[3.2]-Uma COLUNA inteira pode ser recuperada como uma Series 
#      utilizando a notação estilo “dicionário” ou estilo “atributo”. 
#      A Series retornada terá o mesmo índice do DataFrame 
print('-------------------------------------------')
print(df_pessoas['idade'])   #recupera a coluna “idade” (notação “dicionário”)
print('\n')  
print(df_pessoas.nome)       #recupera a coluna “nome” (notação “atributo”)

#[3.3]-Uma CÉLULA pode ser recuperada de diferentes formas.
#      Abaixo, utilizamos os métodos “iloc” e “loc” novamente
print('-------------------------------------------')
print(df_pessoas.iloc[4][2])           #posição da linha + posição da coluna     
print(df_pessoas.iloc[4]['salario'])   #posição da linha + rótulo da coluna
print(df_pessoas.loc['P5'][2])         #rótulo da linha  + posição da coluna
print(df_pessoas.loc['P5']['salario']) #rótulo da linha  + rótulo da coluna
