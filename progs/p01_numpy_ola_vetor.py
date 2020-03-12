#P01: Olá Vetor NumPy! 
import numpy as np #importa a biblioteca, renomeando-a para np

#Criamos um vetor a partir de uma lista
vet_notas = np.array([7.8, 8.5, 10.0, 9.2, 5.0, 8.5, 6.4, 8.6, 7.5, 9.0])

print('vet_notas = ', vet_notas) #imprime o vetor
print('type(vet_notas) = ', type(vet_notas)) #imprime o tipo (ndarray) 
print('vet_notas.dtype = ', vet_notas.dtype) #prop. "dtype" – tipo dado (float64)
print('vet_notas.ndim = ', vet_notas.ndim)   #prop. "ndim" – num. dimensões (1)
print('vet_notas.shape = ', vet_notas.shape) #prop. "shape" – num posições (10)

#indexação básica
print('-------------------------------------------')
print('primeiro elemento = ', vet_notas[0])               #indexação
print('último elemento = ', vet_notas[len(vet_notas)-1])  #indexação 
print('3o e 4o elementos = ', vet_notas[2:4])              #fatiamento

#modifica a nota do quarto aluno
vet_notas[3] = 9.5

#imprime o novo vetor
print('-------------------------------------------')
print('vet_notas novo = ', vet_notas)