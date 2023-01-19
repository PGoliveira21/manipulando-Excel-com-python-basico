
#Listas em python
nome = ['Ana','Paulo','Samuel']
idades = [20,30,10,11]

#Tuplas em python valores nao sao alterados depois de declarados
sexo = ('M','F','O')

#Dicionario em python geralmente contem valores dentro de uma variavel chave, nao e tabular
cadastro = {'nomes': nome,
            'idades': idades,
            'cidades':['A','B','C']}

print(cadastro['nomes'][2])

#estrutura de repetição
for nome in nome:
    print(nome)

for idade in idades:
    if idade%2==0: print(idade)

#imprime ate o valor nove
for i in range(0,10):
    print(i)

#estrutura while faça enquanto
i = 0
idade = idades[i]
while idade <= 10:
    print(idade)
    i += 1
    idade = idades[i]

#comandos inline contando ate 100
print([i for i in range(0,101)])
#contando de dois em dois
print([2*i for i in range(0,101)])
#somando todos os valores de 0 a 100
print(sum([i if i%2==0 else 0 for i in range(0,101)]))

#/////////////////////////////////////////////////////////////////////////////////////////////
#importando a função
import funcao as mf
print(mf.faixaIdade(15))


