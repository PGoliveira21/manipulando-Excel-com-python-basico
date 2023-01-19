import pandas as pdd

#importando dados do excell
pessoas = pdd.read_excel('caso_estudo.xlsx', sheet_name='pessoas')
covid = pdd.read_excel('caso_estudo.xlsx', sheet_name='registros_covid')
print(covid)

#comando head imprime o cabeçalho o numero 5 indica a quantidade que eu quero
print(pessoas.head(5))

#comando tail imprime os ultimos dados
print(pessoas.tail(5))

#comando sample imprime aleatoriamente
print(pessoas.sample(5))

#comando describe te dar um resumo das suas colunas
print(pessoas.describe())

#criando filtros
print(pessoas[pessoas.idade>40]) #retorna todas as pessoas acima de 40 anos

print(pessoas[pessoas.idade>40].count()) #conta quantas pessoas e retorna com todos os campos

print(pessoas.id[pessoas.idade>40].count()) #conta quantas pessoas e retorna a quantidade de id´s

print(pessoas.nome[pessoas.idade==48])#retorna todos os nomes das pessoas com idade de 48

print(pessoas.idade[pessoas.sexo=='F'].mean())#calculando a media da idade das pessoas com sexo feminino

print(pessoas[pessoas.nome.str[0]=='A'])#retorna todos as pessoas que começam com a letra A

print(pessoas[pessoas.nome.str[0:3]=='Ana'])#retornando todas as anas

#comandos de agrupamento de dados
print(pessoas.groupby('sexo').mean())#agrupa o sexo feminino e o sexo masculino e calcula a media

print(pessoas.groupby('sexo').idade.mean())#agrupa o sexo feminino e o sexo masculino e calcula a media da idade de cada grupo

pessoas['inicial'] = pessoas.nome.str[0]#cria uma coluna com o nome do campo inicial e salva as letras iniciais nessa nova coluna
print(pessoas.groupby('inicial').idade.mean())#agrupa o campo inicial e calcula a media de idade de cada pessoa levando em consideração a letra inicial do nome


#COMANDO JOIN
print(pessoas.head(2))
print(covid.head(2))
pessoas = pessoas.set_index('id')#comando para trasformar o index em id
covid = covid.set_index('id')
print(pessoas.head(2))
print(covid.head(2))

df = pessoas.join(covid.set_index('id_pessoa'))#unifica a tabela pessoas e seta o index da tabela covid para ser id_pessoas
print(df.head(5))#imprime o novo dataframe ja com o campo severidade adicionado a tabela pessoas
df = df.fillna(0)#substitui os dados NaN para 0. nao e interessante termos dados NaN em tabelas
print(df.head(5))
print(df.groupby('severidade').idade.mean())# calcula a media de idade por agrupamento de severidade
#o segredo do join e garantir o correto index das tabelas

#NOVAS FEATURES
df['faixa_etaria'] = 'Jovem'#adicionando uma nova coluna com nome de faixa_etaria
df.loc[df.idade>24,'faixa_etaria'] = 'adulto'
df.loc[df.idade>45,'faixa_etaria'] = 'adulto2'#altera os dados do campo faixa etaria de acordo com a idade
print(df.head(5))
df.loc[df.severidade=='baixa','severidade'] = 1
df.loc[df.severidade=='alta','severidade'] = 2 #alterando os campos dentro de severidade
print(df.head(5))
df['severidade'] = df['severidade'].astype('int')#esse comando altera o tipo de dado da coluna severidade que antes era string para inteiro, isso e importante para utilizarmos o proximo comando groupby e calcularmos a media
print(df.groupby('faixa_etaria').mean())

#Função lambda simula um for mas em uma unica linha
print(df.idade.apply(lambda x: 100*x if x>30 else x).head(5))
#o comando a cima mostra todas as idades e aplica uma multiplicação de vezes 100 se idade for maior que 30
