from random import choice

cartas_jogador = []
cartas_maquina = []

def armazena_cartas(inicio=True):
    '''
    Armazena as cartas que foram selecionadas a uma
    lista. Se caso for a primeira rodada, duas cartas
    serão selecionadas para o jogador e uma para a máquina.
    Posteriormente, serão selecionadas apenas uma carta.
    '''

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

    Essa amostragem será com reposição, presumindo que em cassinos
    mais de uma baralho são utilizados.
    '''
    cartas = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    carta_selecionada = choice(cartas)

    return carta_selecionada

def mostra_cartas(cartas_jogador, cartas_maquina, inicio=True):
    '''
    Imprime as cartas que estão nas mãos dos jogadores.
    Se caso for a primeira rodada, a máquina receberá apenas
    uma carta. Nas demais rodadas, mais cartas serão apresentadas.

    '''

    if inicio:
        print(f'Suas cartas são: {cartas_jogador}')
        print(f'A primeira carta da máquina é: {cartas_maquina}')
    else:
        print(f'Suas cartas são: {cartas_jogador}')
        print(f'A mão da máquina é: {cartas_maquina}')


def acaba_jogo():
    '''
    Ao optar por não receber mais cartas, o resultado
    será impresso. Assim como o valor acumulado em ambas
    as mãos.
    '''

    agradecimento = print('Obrigado por jogar Blackjack!')

    return agradecimento

def continua_jogando(cartas_jogador, cartas_maquina):
    '''
    Ao optar por receber mais cartas, a mão será atualizada
    e será impressa para o jogador. Caso contrário, o resultado
    será impresso.
    '''

    opcao = input('Deseja continuar jogando? Digite "s" para sim, ou "n" para não.\n')
    while opcao == 's':
        armazena_cartas(inicio=False)
        mostra_cartas(cartas_jogador, cartas_maquina, inicio=False)
        opcao = input('Deseja continuar jogando? Digite "s" para sim, ou "n" para não.\n')
    if opcao == 'n':
        acaba_jogo()
