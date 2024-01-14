'''
- Introdução ao módulo "random" e funções como "randint" e "random".
- Introdução à listas.
    1. Como utilizar o índex para encontrar elementos.
    2. Como adicionar elementos com a função "append()" ou "extend()".
    3. Como utilizar listas aninhadas.
'''

import random

print(random.randint(1, 10))

print(random.random())


lista = [1, 2, 3, 4, 5]

print(lista[2])

lista.append(6)

lista.extend([7, 8, 9])

lista_aninhada = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(lista_aninhada[1][2])
