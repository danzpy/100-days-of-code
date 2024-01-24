'''
to do:

DONE 1 - Separar dois filmes aleatórios. (Não pegar o mesmo filme nas duas escolhas)
2 - O Usuário deverá advinhar, se o segundo filme escolhido possui um rating maior que o primeiro.
3 - Caso acerte, outro filme será escolhido até que o usuário erre.
4 - A cada acerto, o usuário receberá um ponto.
5 - Os pontos serão impressos ao usuário

'''

from data import filmes
from random import choice
from random import randint

escolha_inicial = randint(0, 96)
escolha_resultante = list(range(0, escolha_inicial)) + list(range(escolha_inicial+1, 97))




