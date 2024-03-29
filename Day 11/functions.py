from random import choice

cartas_jogador = []
cartas_maquina = []

def armazena_cartas(cartas_jogador, cartas_maquina, inicio, final):
    '''
    Armazena as cartas que foram selecionadas a uma
    lista. Se caso for a primeira rodada, duas cartas
    serão selecionadas ambos os jogadores.
    Posteriormente, serão selecionadas apenas uma carta para o jogador
    principal.

    Caso o jogador defina não receber mais cartas, a máquina receberá
    mais cartas até que a somatória da mão seja menor que 17 pontos.
    '''

    if inicio:
        for i in range(2):
            cartas_jogador.append(seleciona_cartas())
            cartas_maquina.append(seleciona_cartas())
            troca_cartas(cartas_jogador, cartas_maquina)
    elif final:
        while sum(cartas_maquina) < 17:
            cartas_maquina.append(seleciona_cartas())
            troca_cartas(cartas_jogador, cartas_maquina)
    else:
        cartas_jogador.append(seleciona_cartas())
        troca_cartas(cartas_jogador, cartas_maquina)


def troca_cartas(cartas_jogador, cartas_maquina):
    '''
    Quando o usuário receber um 11 (equivalente ao ás) e possuir
    mais de 21 pontos. Esse valor será substituido por 1 ponto.
    '''

    if sum(cartas_jogador) > 21 and 11 in cartas_jogador:
        cartas_jogador.remove(11)
        cartas_jogador.append(1)
    elif sum(cartas_maquina) > 21 and 11 in cartas_maquina:
        cartas_maquina.remove(11)
        cartas_maquina.append(1)

            
def seleciona_cartas():
    '''
    Seleciona cartas de forma "randômica" para os jogadores.

    Essa amostragem será com reposição, presumindo que em cassinos
    mais de uma baralho são utilizados.
    '''
    cartas = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    carta_selecionada = choice(cartas)

    return carta_selecionada

def mostra_cartas(cartas_jogador, cartas_maquina, final=False):
    '''
    Imprime as cartas que estão nas mãos dos jogadores.
    Se caso for a primeira rodada, será impressa apenas a
    primeira carta da mão da máquina.
    Quando o jogador principal decidir não receber mais cartas,
    a mão da máquina será exibida.

    '''

    if not final:
        print(f'Suas cartas são: {cartas_jogador}')
        print(f'A primeira carta da máquina é: {cartas_maquina[0]}')
    else:
        print(f'Suas cartas são: {cartas_jogador}')
        print(f'A mão da máquina é: {cartas_maquina}')


def checa_pontos(cartas_jogador, cartas_maquina):
    '''
    Checa as possibilidades de vitória ou derrota dos jogadores.
    '''
    if sum(cartas_jogador) == 21:
        print(f'Parabéns, Você ganhou! Você possui {sum(cartas_jogador)} pontos, enquanto a máquina possui apenas {sum(cartas_maquina)} -> {cartas_maquina}.')
    elif sum(cartas_maquina) == 21:
        print(f'Você perdeu! A máquina atingiu {sum(cartas_maquina)}.')
    elif sum(cartas_jogador) > 21:
        print(f'Você atingiu {sum(cartas_jogador)} pontos, e consequentemente perdeu!')
    elif sum(cartas_maquina) > 21:
        print(f'Parabéns, você ganhou! A máquina atingiu {sum(cartas_maquina)} pontos.')
    elif sum(cartas_jogador) == sum(cartas_maquina):
        print(f'Ambos possuem {sum(cartas_jogador)} pontos, o jogo termina com um empate.')
    elif sum(cartas_jogador) > sum(cartas_maquina):
        print(f'Parabéns, Você ganhou! Você possui {sum(cartas_jogador)} pontos, enquanto a máquina possui apenas {sum(cartas_maquina)}.')
    elif sum(cartas_jogador) < sum(cartas_maquina):
        print(f'Você atingiu {sum(cartas_jogador)} pontos. O vencedor foi a máquina, com {sum(cartas_maquina)}')




def continua_jogando(cartas_jogador, cartas_maquina):
    '''
    Ao optar por receber mais cartas, a mão será atualizada
    e será impressa para o jogador. Caso contrário, o resultado
    será impresso.
    '''
    opcao = input('Deseja continuar jogando? Digite "s" para sim, ou "n" para não.\n').lower()
    while opcao == 's':
        armazena_cartas(cartas_jogador, cartas_maquina, inicio=False, final=False)
        mostra_cartas(cartas_jogador, cartas_maquina, final=False)
        if sum(cartas_jogador) == 21 or sum(cartas_maquina) == 21:
            acaba_jogo()
            break
        elif sum(cartas_jogador) > 21 or sum(cartas_maquina) > 21:
            acaba_jogo()
            break
        elif sum(cartas_maquina) < 21 or sum(cartas_jogador) < 21:
            opcao = input('Deseja continuar jogando? Digite "s" para sim, ou "n" para não.\n').lower()
        else:
            acaba_jogo()
            break
    if opcao == 'n':
        armazena_cartas(cartas_jogador, cartas_maquina, inicio=False, final=True)
        mostra_cartas(cartas_jogador, cartas_maquina, final=True)
        acaba_jogo()


def acaba_jogo():
    '''
    Ao optar por não receber mais cartas, o resultado
    será impresso. Assim como o valor acumulado em ambas
    as mãos.
    '''
    checa_pontos(cartas_jogador, cartas_maquina)
    agradecimento = print('Obrigado por jogar Blackjack!')

    return agradecimento