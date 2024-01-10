# Para a execução desse script só foram utilizadas funções que foram apresentadas até o dia atual.

'''
Gerador de senhas

Neste script você poderá gerar uma senha através de "inputs" fornecidos.
'''

from random import choice, randint

print('Bem vindo ao gerador de senhas.')

letras = int(input('Quantas letras você deseja na sua senha?\n'))
simbolos = int(input('Quantos símbolos você deseja na sua senha?\n'))
num = int(input('Quantos números você deseja na sua senha?\n'))

letras_minusculas = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
letras_maiusculas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
simbolos_list = ['!', '#', '$', '%', '&', "'", '(', ')', '*', '+', '-', '/', ':', ';', '<', '=', '>', '@', '[', ']', '^', '_']

todas_as_letras = []

for i in [letras_maiusculas, letras_minusculas]:
    todas_as_letras.extend(i)

senha = ''

for i in range(letras):
    senha += choice(todas_as_letras)
        
for i in range(num):
    senha += choice(numeros)
            
for i in range(simbolos):
    senha += choice(simbolos_list)


len_senha = (letras+simbolos+num)
sequencia_aleatoria = []

for i in range(4000): # Definindo um range "grande" para que seja possível preencher a random_sequence por completo.
    r = randint(0, len_senha-1)
    if len(sequencia_aleatoria) != (len_senha):
        if r not in sequencia_aleatoria:
            sequencia_aleatoria.append(r)

senha_com_ordem_aleatoria = ''

for i in sequencia_aleatoria:
    senha_com_ordem_aleatoria += senha[i]

print(senha_com_ordem_aleatoria)
