import pandas as pd
import numpy as np

pessoas = pd.read_excel('caso_estudo.xlsx', sheet_name='pessoas')
print(pessoas)

#convertendo o new frame de resposta para array
pessoas = np.array(pessoas)
print(pessoas)#dataframe convertido em pessoas entao indiretamente utilizo o numpy para ler o excell
print(pessoas[:,3])#pegando todas as idades do array na ultima coluna

print(np.sum(pessoas[:,3]))#somando todos os valores da coluna 3 e imprimindo no console

#FILTROS
print(pessoas[pessoas[:,1]=='Caio Pereira'])#retornando todos os dados caso seja encontrado o nome na coluna 1
print(pessoas[pessoas[:,2]=='M'])#retorna todas as pessoas do sexo masculino
print(pessoas[pessoas[:,2]=='M',3])#retorna todas as idades das pessoas do sexo masculino
print(np.sum((pessoas[pessoas[:,2]=='M',3])))#retorna a soma de todas as idades das pessoas do sexo masculino





