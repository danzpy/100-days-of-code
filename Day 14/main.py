'''
to do:

DONE - Separar dois filmes aleatórios. (Não pegar o mesmo filme nas duas escolhas)
DONE - O Usuário deverá advinhar, se o segundo filme escolhido possui um rating maior que o primeiro.
- Caso acerte, outro filme será escolhido até que o usuário erre.
- A cada acerto, o usuário receberá um ponto.
- Os pontos serão impressos ao usuário

'''

from art import vs, logo
from data import filmes
from random import choice, randint
from replit import clear

numero_inicial = randint(0, 96)
escolha_inicial = filmes[numero_inicial]
lista_resultante = list(range(0, numero_inicial)) + list(range(numero_inicial + 1, 97))
numero_resultante = choice(lista_resultante)
escolha_resultante = filmes[numero_resultante]

#isso pode ser uma função na qual o parâmetro é a apresentacao
apresentacao_inicial = f'Compare a opção A:\n{escolha_inicial["Breve descrição"]} Seu título é "{escolha_inicial["Nome do filme"]}" e foi lançado no ano de {escolha_inicial["Ano de lançamento"]}.'
apresentacao_final = f'Contra a opção B:\n{escolha_resultante["Breve descrição"]} Seu título é "{escolha_resultante["Nome do filme"]}" e foi lançado no ano de {escolha_resultante["Ano de lançamento"]}.'

clear()
print(f'{logo}\n')
print(apresentacao_inicial)
print(f'{vs}\n')
print(apresentacao_final)
melhor = input('\nCom base no rating IMDB, qual filme é o melhor? Digite "a" ou "b"\n').lower()

# validar se é possível criar uma função, valores muito repetitivos
if melhor == 'a':
    if escolha_resultante['rating'] > escolha_inicial['rating']:
        print(f'Você errou! O rating do filme "{escolha_resultante["Nome do filme"]}" é {escolha_resultante["rating"]}. Já o rating da outra opção é {escolha_inicial["rating"]}.')
    else:
        print(f'Você acertou! O rating do filme "{escolha_resultante["Nome do filme"]}" é {escolha_resultante["rating"]}. Já o rating da outra opção é {escolha_inicial["rating"]}.')
elif melhor == 'b':
    if escolha_inicial['rating'] > escolha_resultante['rating']:
        print(f'Você errou! O rating do filme "{escolha_resultante["Nome do filme"]}" é {escolha_resultante["rating"]}. Já o rating da outra opção é {escolha_inicial["rating"]}.')
    else:
        print(f'Você acertou! O rating do filme "{escolha_resultante["Nome do filme"]}" é {escolha_resultante["rating"]}. Já o rating da outra opção é {escolha_inicial["rating"]}.')
else:
    print('Opção inválida')




