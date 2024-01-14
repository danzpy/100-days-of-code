"""

Nesse dia tive introdução à função "print()". Foram abordados alguns conceitos básicos como

- utilização de double quotes para imprimir strings
- a utilização do \n para pular uma linha
- introdução a concatenação de strings

Também foram introduzidos os conceitos de variável e da função "input()"

"""

# Demonstrações da função "print()"

print("hello world")

print('aqui é a primeira linha\ne aqui, a segunda linha')

print('Olá' + ' ' + 'Daniel')


# Demonstrações da utilização de variáveis e da função "input()"

nome = input('Qual é seu nome? ')
print(nome)
frase = 'Este não é meu nome!'
nome = frase
print(nome)