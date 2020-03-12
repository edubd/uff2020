#P17: Limpeza
import pandas as pd  

#(1)-Importa a base de dados para um DataFrame
df_lojas = pd.read_csv('lojas.csv')

#(2)-Exibe o nome fantasia original. Veja que o atributo foi importado com
#    espaços em branco à direita
print('fantasia – valores originalmente importados:')
print(df_lojas['fantasia'].values)

#(3)-Utiliza o apply para remover os espaços em branco
df_lojas['fantasia'] = df_lojas['fantasia'].apply(str.rstrip)

#(4)-Agora os espaços em branco não existem mais
print('--------------------------------------------')
print('fantasia – valores após a limpeza dos espaços em branco:')
print(df_lojas['fantasia'].values)
