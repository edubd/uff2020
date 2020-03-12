#P04: Estatísticas sobre matrizes + Axis
import numpy as np

#cria a matriz “notas”
notas = np.array([9.8, 7.2, 8.0, 5.3, 4.0, 3.5, 5.5, 8.1, 7.2, 7.8, 7.5, 6.5])
notas = notas.reshape((4,3))

#imprime a matriz e gera as estatísticas
print('notas: ', notas) 

print('média geral: ', notas.mean()) 
print('média de cada prova: ', notas.mean(axis=0)) 
print('média de cada aluno: ', notas.mean(axis=1)) 

print('maior nota geral: ', notas.max()) 
print('maior nota de cada prova: ', notas.max(axis=0))
print('maior nota de cada aluno: ', notas.max(axis=1))