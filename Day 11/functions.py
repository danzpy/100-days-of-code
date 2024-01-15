from random import choice

cartas_jogador = []
cartas_maquina = []

def armazena_cartas(inicio=True):

    if inicio:
        for i in range(2):
            cartas_jogador.append(seleciona_cartas())
        cartas_maquina.append(seleciona_cartas())
    else:
        cartas_maquina.append(seleciona_cartas())
        cartas_jogador.append(seleciona_cartas())
            
def seleciona_cartas():
    '''
    Seleciona cartas de forma "randômica" para os jogadores.
    Se caso for a primeira rodada, duas cartas serão selecionadas
    para o jogador e uma para a máquina. Posteriormente, serão
    selecionadas apenas uma carta.

    Essa amostragem será com reposição, presumindo que em cassinos
    mais de uma baralho são utilizados.
    '''
    cartas = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    carta_selecionada = choice(cartas)

    return carta_selecionada

def mostra_cartas(cartas_jogador, cartas_maquina, inicio=True):
    if inicio:
        print(f'Suas cartas são: {cartas_jogador}')
        print(f'A primeira carta da máquina é: {cartas_maquina}')
    else:
        print(f'Suas cartas são: {cartas_jogador}')
        print(f'A mão da máquina é: {cartas_maquina}')


def acaba_jogo():

    agradecimento = print('Obrigado por jogar Blackjack!')

    return agradecimento

def continua_jogando(cartas_jogador, cartas_maquina):

    opcao = input('Deseja continuar jogando? Digite "s" para sim, ou "n" para não.\n')
    while opcao == 's':
        armazena_cartas(inicio=False)
        mostra_cartas(cartas_jogador, cartas_maquina, inicio=False)
        opcao = input('Deseja continuar jogando? Digite "s" para sim, ou "n" para não.\n')
    if opcao == 'n':
        acaba_jogo()
