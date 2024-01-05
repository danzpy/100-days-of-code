# Para a execução desse script só foram utilizadas funções que foram apresentadas até o dia atual.

from random import choice, randint

print('Bem vindo ao gerador de senhas.')

letras = int(input('Quantas letras você deseja na sua senha?\n'))
simbolos = int(input('Quantos símbolos você deseja na sua senha?\n'))
num = int(input('Quantos números você deseja na sua senha?\n'))

letras_minusculas = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
letras_maiusculas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
simbolos_list = ['!', '#', '$', '%', '&', "'", '(', ')', '*', '+', '-', '/', ':', ';', '<', '=', '>', '@', '[', ']', '^', '_']

all_letters = []

for i in [letras_maiusculas, letras_minusculas]:
    all_letters.extend(i)

password = ''

for i in range(letras):
    password += choice(all_letters)
        
for i in range(num):
    password += choice(numeros)
            
for i in range(simbolos):
    password += choice(simbolos_list)


len_password = (letras+simbolos+num)
random_sequence = []

for i in range(4000): # Definindo um range "grande" para que seja possível preencher a random_sequence por completo.
    r = randint(0, len_password-1)
    if len(random_sequence) != (len_password):
        if r not in random_sequence:
            random_sequence.append(r)

random_order_password = ''

for i in random_sequence:
    random_order_password += password[i]

print(random_order_password)
