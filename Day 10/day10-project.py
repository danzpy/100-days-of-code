from art import logo
from replit import clear
import functions



def calculadora():
    continua = True

    print(logo)
    inicial = float(input('Digite um número:\n'))

    operacoes = {
        '+': functions.adicao,
        '-': functions.subtracao,
        '*': functions.multiplicacao,
        '/': functions.divisao
    }

    while continua:
        operador = input('Defina um operador (+, -, *, /):\n')
        secundario = float(input('Qual é o próximo valor?\n'))

        if operador not in ('+', '-', '*', '/'):
            print('Operador invalido.')
        else:
            calculo = operacoes[operador]
            resultado = round(calculo(inicial, secundario), 3)

            print(f'\n{inicial} {operador} {secundario} = {resultado}\n')

        opcao_continuar = input(f'Digite "c" para continuar calculando com o resultado obtido ({resultado}).\nDigite "n" para começar uma nova operação.\nDigite "e" para sair encerrar a calculadora.\n').lower()
        if opcao_continuar == 'c':
            inicial = resultado
        elif opcao_continuar == 'n':
            clear()
            calculadora()
        elif opcao_continuar == 'e':
            print('Obrigado por utilizar a calculadora.')
            continua = False
        else:
            print('Opção escolhida não é reconhecida. Obrigado por utilizar a calculadora')
            continua = False

calculadora()