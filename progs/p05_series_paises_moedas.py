#P05: Series de países e moedas
import pandas as pd  

#(1)-criação da Series onde índices=siglas de países e valores=nome da moeda
siglas = ['BR','FR','UK','IT','US']
moedas = ['Real','Euro','Libra','Euro','Dólar']
s2 = pd.Series(moedas,index=siglas)

print('-------------------------------------------')
print('s2:') 
print(s2) 

#(2)-podemos utilizar os rótulos para indexar 
print('-------------------------------------------')
print(s2['UK'])           #'Libra'
print('\n') 
print(s2[['BR','IT']])    #['BR':'Real', 'IT':'Euro']
print('\n') 
print(s2[1:3])            #['FR':'Euro', 'UK':'Libra']
print('\n') 
print('BR' in s2)         #True
print('AR' in s2)         #False

#(3)-As propriedades values e index retornam, respectivamente, os valores 
#    e índices da Series, respectivamente
print('-------------------------------------------')
print(s2.values)          #['Real' 'Euro' 'Libra' 'Euro' 'Dólar']
print(s2.index)           #Index(['BR', 'FR', 'UK', 'IT', 'US'], dtype='object')
