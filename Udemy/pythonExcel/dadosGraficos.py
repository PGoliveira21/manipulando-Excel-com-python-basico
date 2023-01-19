import matplotlib.pyplot as plt #importando um modulo dentro do pai plot
import pandas as pd
df = pd.read_excel('leitura.xlsx', sheet_name='dados')
print(df.head(5))

#Criando grafico
x = df.tempo
y = df.temperatura
plt.plot(x,y)
plt.show()#imprimindo o grafico
#grafico de barras
#normalmente ele e bom para categorias entao iremos plotar periodo e temperatura, mas antes e necessario
#agrupar os dados de temperatura
d = df.groupby('periodo').mean()
print(d)#retorna a media de todos os campos da tela e o agrupamento de periodo
d = df.groupby('periodo').temperatura.mean()
print(d)#retorna a media so de temperatura depois de agrupar os periodos
#depois precisamos acessar so o periodo usando index e depois os valores usando values para gerarmos o grafico de barras
x = df.groupby('periodo').temperatura.mean().index
y = df.groupby('periodo').temperatura.mean().values
plt.bar(x,y)
plt.show()

#grafico de boxplot
df.boxplot()
plt.show()
df.boxplot('temperatura')#pegando so a temperatura para gerar o grafico
plt.show()
#o boxplot mostra a mediana e os quartis que sao uma divisao de 25% 50% e 75% dos dados, geralmente
#as bolinhas que aparecem nos dados sao um problema que sao denominadas outlines, voce pode retira-lo
#fazer uma media entre o intervalo e etc cabe a voce definir isso.
#para acessar esse dado podemos utilizar o comando a baixo fazendo um filtro dentro de df
print(df[df.temperatura == df.temperatura.min()])

#grafico de Histograma com uma curva de distribuição de probabilidade, devemos istalar a biblioteca seaborn
import seaborn as sns
sns.distplot(df.umidade)
plt.show()





