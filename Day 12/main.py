import functions

"""
Advinhe o número.

Neste projeto, um número de 0 a 100 será selecionado "randômicamente"
e o usuário deverá acertado. A cada tentativa, uma dica será impressa
ao usuário. Será possível escolher a dificuldade da rodada, sendo a
mais dificil a possibilidade de acerto com 5 tentativas. E a mais
fácil, com 10 tentativas.
"""

def advinhando():
    print('Bem vindo ao jogo da advinhação!\nEstou pensando em um número de 0 a 100.')
    functions.selecionando_numero()
    functions.dificuldade(functions.tentativas)
    functions.tentando_acertar(functions.selecionado, functions.tentativas)
    while functions.tentativas != 0:
        functions.verificando_palpite(functions.palpite, functions.selecionado, functions.tentativas)
    functions.acaba_jogo()

advinhando()
