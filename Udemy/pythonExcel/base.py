import pandas as pd
#df = pd.DataFrame({'nome':['Paulo','Samuel','Marta'],
 #                  'idade':[29,5,50]})
#print(df)
#print(df.idade.min())

#mudando o valor de um campo
#df.loc[0, 'nome'] = 'Joao'
#print(df)

#adicionando mais uma coluna na tabela do dataframe
#df['sexo'] = ['M','M','F']
#print(df)

#adicionando uma nova linha
#df = df.append({'nome':'Ana', 'idade':15, 'sexo':'F'}, ignore_index=True)
#print(df)

#Importando tabela do excell
import pandas as pd

pessoas = pd.read_excel("C:/Users/paulo/PycharmProjects/Cursoemvideo/Udemy/pythonExcel/caso_estudo.xlsx")
registros_covid = pd.read_excel("C:/Users/paulo/PycharmProjects/Cursoemvideo/Udemy/pythonExcel/caso_estudo.xlsx")