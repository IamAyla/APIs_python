#Projeto - Busca de CEP

##Consultando informações a partir do CEP
#Importando a lib necessária
import requests
import pandas as pd

#Recebendo input do cep
cep = input('Digite o CEP desejado: ')
cep = cep.replace('-', '').replace('.', '').replace(' ', '')

#Verificando se o cep atende ao requisito mínimo de números e realizando busca
if len(cep) == 8:
  link = f'https://viacep.com.br/ws/{cep}/json/'
  requisicao = requests.get(link)

  dic_requisicao = requisicao.json()

  uf = dic_requisicao['uf']
  cidade = dic_requisicao['localidade']
  bairro = dic_requisicao['bairro']
  rua = dic_requisicao['logradouro']
  num = dic_requisicao['complemento']
  print(f'{rua}, {num} - {bairro}, {cidade} - {uf}')

#Caso o número do CEP seja menor que 8:
else:
  print('CEP inválido')
  
##Busca do CEP a partir do endereço
#Recebendo os inputs necessários para a busca
uf = str(input('Qual o UF? ')).upper()
if len(uf) != 2: #a uf precisa ter dois dígitos para que a busca seja bem sucedida.
  print('Digite a sigla do UF com 2 dígitos.')

cidade = input('Qual a cidade? ')
rua = input('Qual a rua? ' )

#realizando busca
link = f'https://viacep.com.br/ws/{uf}/{cidade}/{rua}/json/'
requisicao = requests.get(link)
#verificando se a requisiçao foi bem sucedida
print(requisicao)

dic_requisicao = requisicao.json()

#Com as pandas, transformamos o dicionário em um dataframe e facilitamos a visualização
tabela = pd.DataFrame(dic_requisicao)
display(tabela)
