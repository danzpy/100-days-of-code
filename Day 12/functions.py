from random import choice
from time import sleep

def log_erro():
    print('Valor selecionado está incorreto. Tente novamente.')
    sleep(2)

def selecionando_numero():

    numeros = [num for num in range(101)]
    selecionado = choice(numeros)

    return selecionado

def tentando_acertar(tentativas, selecionado):

    print(f'Você tem {tentativas} tentativas restantes para advinhar o número.')
    palpite = int(input('Tente advinhar o número: '))

    if palpite != selecionado and tentativas != 0:
        verificando_palpite(palpite, selecionado, tentativas)
    elif palpite != selecionado and tentativas == 0:
        acaba_jogo()
    else:
        print('Você acertou!')


def nivel_dificuldade():
    
    tentativas = 0

    dificuldade = input('Escolha a dificuldade. Digite "f" para fácil e "d" para dificil: ').lower()
    tentativas()

    return dificuldade

def tentativas():

    tentativas = 0
    
    dificuldade = nivel_dificuldade()

    if dificuldade == 'f':
        tentativas += 10
    elif dificuldade == 'd':
        tentativas += 5
    else:
        log_erro()
        sleep(2)
        nivel_dificuldade()

    print(f'Você tem {tentativas} tentativas disponíveis!')
    
    return tentativas



def errou_palpite(tentativas_restantes):

    tentativas_restantes -= 1
    sleep(1)
    tentando_acertar(tentativas)

def verificando_palpite(palpite, selecionado, tentativas):

    if palpite < selecionado and selecionado - palpite > 50:
        print('O valor escolhido está muito abaixo do número selecionado por mim.\nTente novamente!')
        errou_palpite(tentativas)
    elif palpite < selecionado and selecionado - palpite < 50:
        print('O valor selecionado está abaixo do número selecionado por mim.')
        errou_palpite(tentativas)
    elif palpite > selecionado and palpite - selecionado > 50:
        print('O valor escolhido está muito acima do número selecionado por mim.\nTente novamente!')
    elif palpite > selecionado and palpite - selecionado < 50:
        print('O valor escolhido está acima do número selecionado por mim.\nTente novamente!')
    else:
        print(f'Parabéns, você acertou! O número que escolhi foi {selecionado}')


def acaba_jogo():
    print('Sua tentativas acabaram. Obrigado por jogar!')

