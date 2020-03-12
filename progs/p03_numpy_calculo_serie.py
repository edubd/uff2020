#P03: Cálculo da série S = (1/1) + (3/2) + (5/3) + (7/4) + … + (99/50)
#     sem programar laço (computação vetorizada)
import numpy as np 

numerador   = np.arange(1,100,2)  #[1 3 5 ... 99]
denominador = np.arange(1,51)     #[1 2 3 ... 50]

S = sum(numerador / denominador)  # somatório de[1/1 3/2 5/3 ... 99/50]

print('* * * resposta: s = {:.2f}'.format(S))
