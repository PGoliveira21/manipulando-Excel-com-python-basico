import numpy as np
a = np.array([10,20,30])
print(a)

print(a[0:2])

#Criando um array multidimrnsional
a = np.array([[10,20,30],[100,200,300]])
print(a)

print(a[0,2])#retorna o valor dentro do array multidimenssional na linha 0 posição 2
print(a.mean())#retorna a media dos valores dentro do array
print(a.mean(0))#retorna a media dos valores da primeira linha dentro do array

#e muito importante definir tamanhos de matrizes antes de anotar valores nela
a = np.zeros([2,2])
print(a)

a[0,1] = 3 #esse comando adiciona o valor 3 na linha 0 e coluna 1
print(a)

a = np.ones([4,3])#criando matriz linear de 1uns
print(a)




