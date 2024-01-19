from random import choice
from time import sleep

def log_erro():
    print('Valor selecionado está incorreto. Tente novamente.')
    sleep(2)

def selecionando_numero():

    numeros = [num for num in range(101)]
    selecionado = choice(numeros)

    return selecionado

def nivel_dificuldade():
        
    dificuldade = input('Escolha a dificuldade. Digite "f" para fácil e "d" para dificil: ').lower()

    return dificuldade
    

def tentando_acertar(selecionado):

    palpite = int(input('Tente advinhar o número: '))

    if palpite != selecionado:
        verificando_palpite(selecionado, palpite)
    else:
        print('Você acertou!')

    return palpite

def tentativas(dificuldade):

    tentativas = 0

    if dificuldade == 'f':
        tentativas += 10
    elif dificuldade == 'd':
        tentativas += 5
    else:
        log_erro()
        sleep(2)
        nivel_dificuldade()

    return tentativas

def verificando_palpite(selecionado, palpite):

    if palpite < selecionado:
        print('O valor escolhido está abaixo do número selecionado por mim.\nTente novamente!\n')
    elif palpite > selecionado:
        print('O valor selecionado está acima do número selecionado por mim.\nTente novamente!\n')
    else:
        print(f'Parabéns, você acertou! O número que escolhi foi {selecionado}')

def acaba_jogo():
    print('Obrigado por jogar!')

