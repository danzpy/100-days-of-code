from time import sleep
from replit import clear
from art import logo
import functions

def blackjack():
    '''
    Nesse jogo cada carta possui um valor específico,
    e de acordo com a soma das cartas na mão do jogador
    é verificado a necessidade de pedir outra carta.
    Isso ocorre até que sua soma chegue a 21 pontos.
    '''

    inicio = input('Você gostaria de iniciar uma partida de Blackjack agora? Digite "s" para iniciar, ou "n" para encerrar a aplicação.\n').lower()

    if inicio == 'n':
        print('Aplicação encerrada.')
    elif inicio == 's':
        print(logo)
        functions.armazena_cartas(inicio=True, final=False)
        functions.mostra_cartas(functions.cartas_jogador, functions.cartas_maquina, inicio=True)
        functions.continua_jogando(functions.cartas_jogador, functions.cartas_maquina)
    else:
        print('Opção inválida.')
        sleep(2)
        blackjack()


blackjack()