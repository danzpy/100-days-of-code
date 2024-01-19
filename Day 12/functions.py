from random import choice
from time import sleep

def log_erro():
    """
    Exibe uma mensagem de erro informando que o valor selecionado está incorreto.
    """
    print('Valor selecionado está incorreto. Tente novamente.')


def selecionando_numero():
    """
    Seleciona aleatoriamente um número entre 0 e 100.
    """
    numeros = [num for num in range(101)]
    selecionado = choice(numeros)
    return selecionado

def nivel_dificuldade():
    """
    Solicita ao usuário a escolha da dificuldade e retorna a escolha em letras minúsculas.
    """

    dificuldade = input('Escolha a dificuldade. Digite "f" para fácil e "d" para difícil: ').lower()
    return dificuldade

def tentando_acertar(selecionado):
    """
    Solicita ao usuário um palpite e verifica se o palpite é igual ao número selecionado.
    """
    palpite = int(input('Tente advinhar o número: '))

    if palpite != selecionado:
        verificando_palpite(selecionado, palpite)
    else:
        print('Você acertou!')

    return palpite

def tentativas(dificuldade):
    """
    Determina o número de tentativas com base na dificuldade escolhida.
    """
    tentativas = 0

    if dificuldade == 'f':
        tentativas += 10
    elif dificuldade == 'd':
        tentativas += 5
    else:
        log_erro()

    return tentativas

def verificando_palpite(selecionado, palpite):
    """
    Compara o palpite do usuário com o número selecionado e fornece feedback.
    """
    if palpite < selecionado:
        print('O valor escolhido está abaixo do número selecionado por mim.\nTente novamente!\n')
    elif palpite > selecionado:
        print('O valor escolhido está acima do número selecionado por mim.\nTente novamente!\n')
    else:
        print(f'Parabéns, você acertou! O número que escolhi foi {selecionado}')

def acaba_jogo():
    """
    Exibe uma mensagem de agradecimento por jogar.
    """
    print('Obrigado por jogar!')
