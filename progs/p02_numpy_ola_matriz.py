#P02: Olá Matriz NumPy! 
import numpy as np 

m = np.arange(7,13) #cria o vetor [7,8,9,10,11,12]
m = m.reshape((2,3))    #transforma-o em uma matriz 2x3

print('m = ', m)             #imprime a matriz
print('type(m) = ', type(m)) #imprime o tipo (ndarray) 
print('m.dtype = ',m.dtype)  #prop. "dtype" – tipo do dado (int32 ou int64)
print('m.ndim = ',m.ndim)    #prop. "ndim" – número de dimensões (2)
print('m.shape = ',m.shape)  #propriedade "shape" – tot linhas x tot cols (2,3)

#indexação e fatiamento básicos
print('-------------------------------------------')
print('m[0,1] = ', m[0,1])       #[8] => (célula da 1a linha, 2a coluna)
print('m[1,:] = ', m[1,:])       #[10 11 12] => (toda 2a linha)
print('m[:,2] = ', m[:,2])       #[9 12] => (toda 3a coluna)
print('m[-1,-2:] = ', m[-1,-2:]) #[11 12] => (última linha, 2 últ. colunas)

#modifica o valor da célula [1,2] (2a linha, 3a coluna)
m[1,2] = 999
print('-------------------------------------------')
print('m nova = ', m) #imprime a nova matriz