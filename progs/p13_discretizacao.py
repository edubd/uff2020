#P12: Discretização
import pandas as pd  

#(1)-Define uma função para discretizar o PO
def discretiza_po(po):
    if po == 0: return "0";
    elif po <= 10: return "1-10";
    elif po <= 50: return "11-50";
    elif po > 50: return ">50"
    else: return "desconhecido";

#(2)-Importa a base de dados para um DataFrame
df_lojas = pd.read_csv('lojas.csv')

#(3)-Cria a coluna “fx_po”
df_lojas['faixa_po'] = df_lojas['po'].apply(discretiza_po)

#(4)-Projeta o nome fantasia, o PO e a faixa de PO
print(df_lojas[['fantasia','po','faixa_po']])

#(5)-Após a discretização, podemos remover o ‘po’ se quisermos
df_lojas = df_lojas.drop(columns=['po'])
print('-----------------------------------')

print('DataFrame após a exclusão do “po”')
print(df_lojas)