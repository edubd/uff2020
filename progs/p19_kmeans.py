#P19: kmeans
import pandas as pd    
import numpy as np    
from sklearn.cluster import KMeans    

#(1)-importa o CSV
df_smile = pd.read_csv('C:/CursoPython/smile.csv')
df_smile.columns = ["x","y"]

#(2)-Executa o kMeans sobre a base importada
print(df_smile.head())

#(3)-imprime um sumário das estatísticas de “x” e “y”
modelo = KMeans(n_clusters=4) #configura k=4

modelo.fit(df_smile) #executa o algoritmo

#retorna um vetor de inteiros com os ids dos clusters que foram
#associados a cada observação
#- como k=4, existem 4 clusters possíveis: 0, 1, 2 e 3
#- Ex.: grupos[0] = 2, sigifica que a primeira observação da base foi
# associada ao cluster 2
#- Sendo asisim, o tamanho (número de linhas) do vetor de clusters é
# igual ao da base de dados

grupos = modelo.labels_

#(4)-plota o gráfico
colormap = np.array(['red','green','blue','orange'])
df_smile.plot(kind="scatter",x="x",y="y", c=colormap[grupos])