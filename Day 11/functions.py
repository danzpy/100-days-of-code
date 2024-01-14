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

    if rodada == 1:
        for i in range(2):
            cartas_jogador.append(choice(cartas))
        cartas_maquina.append(choice(cartas))
    else:
        cartas_jogador.append(choice(cartas))
        cartas_maquina.append(choice(cartas))
        rodada += 1

    return cartas_jogador, cartas_maquina, rodada

def mostra_cartas(cartas_jogador, cartas_maquina, rodada):
    if rodada == 1:
        print(f'Suas cartas são: {cartas_jogador}')
        print(f'A primeira carta da máquina é: {cartas_maquina}')
        rodada += 1
    else:
        print(f'Suas cartas são: {cartas_jogador}')
        print(f'A mão da máquina é: {cartas_maquina}')     
    print(f'A rodada no mostra cartas é {rodada}')

def continua_jogando(cartas_jogador, cartas_maquina, rodada):

    continua = True

    opcao = input('Deseja continuar jogando? Digite "s" para sim, ou "n" para não.\n')
    if opcao == 's':
        
        mostra_cartas(cartas_jogador, cartas_maquina, rodada)
        print(f'A rodada no continua jogando é {rodada}')
    
    return continua
