# Ao analisar o código proposto pela instrutora. Percebi que criei funções desnecessárias para o código. Sendo assim,
# pretendo refatorar este código no futuro.

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
    numero_selecionado = functions.selecionando_numero()
    print(numero_selecionado)
    dificuldade = functions.nivel_dificuldade()
    if not (dificuldade == 'f' or dificuldade == 'd'):
        functions.log_erro()
    else:
        tentativas_restantes = functions.tentativas(dificuldade)
        print(f'Você tem {tentativas_restantes} tentativas restantes!\n')
        palpite = functions.tentando_acertar(numero_selecionado)
        if palpite == numero_selecionado:
            functions.acaba_jogo()
        else:
            while tentativas_restantes != 0:
                tentativas_restantes -= 1
                print(f'Você tem {tentativas_restantes} tentativas restantes!\n')
                palpite = functions.tentando_acertar(numero_selecionado)
                if palpite == numero_selecionado:
                    break
            functions.acaba_jogo()

advinhando()
