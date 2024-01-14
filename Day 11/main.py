from time import sleep
from replit import clear
from art import logo
import functions

def blackjack():
    inicio = input('Você gostaria de iniciar uma partida de Blackjack agora? Digite "s" para iniciar, ou "n" para encerrar a aplicação.\n').lower()

    if inicio == 'n':
        print('Aplicação encerrada.')
    elif inicio == 's':
        print(logo)
        cartas_jogador, cartas_maquina, rodada = functions.seleciona_cartas()
        functions.mostra_cartas(cartas_jogador, cartas_maquina, rodada)
        functions.continua_jogando(cartas_jogador, cartas_maquina, rodada)
    else:
        print('Opção inválida.')
        sleep(2)
        blackjack()


blackjack()