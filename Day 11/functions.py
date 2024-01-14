from random import choice

def seleciona_cartas():
    '''
    Seleciona cartas de forma "randômica" para os jogadores.
    Se caso for a primeira rodada, duas cartas serão selecionadas
    para o jogador e uma para a máquina. Posteriormente, serão
    selecionadas apenas uma carta.

    Essa amostragem será com reposição, presumindo que em cassinos
    mais de uma baralho são utilizados.
    '''
    rodada = 1
    cartas = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    cartas_jogador = []
    cartas_maquina = []

    while sum(cartas_jogador) < 21 or sum(cartas_maquina) < 21:
        if rodada == 1:
            for i in range(2):
                cartas_jogador.append(choice(cartas))
            cartas_maquina.append(choice(cartas))
        else:
            cartas_jogador.append(choice(cartas))
            cartas_maquina.append(choice(cartas))

        

    return cartas_jogador, cartas_maquina


def mostra_cartas():
    cartas_jogador, cartas_maquina = seleciona_cartas()
    print(f'Suas cartas são: {cartas_jogador[0]}, {cartas_jogador[1]}')
    print(f'A primeira carta da máquina é: {cartas_maquina[0]}')