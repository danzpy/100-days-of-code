'''
Como funcionam dicionários.
Como utilizar dicionários aninhados com listas ou outros dicionários.
'''

# Criando um dicionário
dict = {
    'nome': 'Daniel',
    'idade': 27,
    'cidade': 'São Paulo'
}

# Acessando uma chave
print(dict['nome'])

# Criando uma chave e atribuindo um valor.
dict['email'] = 'daniel.leonssio@hotmail.com'

print(dict)

# Criando uma chave e atribuindo uma lista ao valor.
dict['frutas_favoritas'] = ['Abacaxi', 'Banana', 'Uva']

print(dict)

lista_com_dicionario = [dict]

print(lista_com_dicionario[0]['nome'])