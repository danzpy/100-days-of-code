'''
Leilão secreto

Neste script, você poderá inserir um nome e o valor do lance em dicionários.
Após a rodada de lances se encerrar, o programa irá imprimir o vencedor,
cujo valor do lance foi o mais alto.

'''

from replit import clear


log_lances = []
valores_lances = []

continua = True

print('Bem vindo ao leilão!')
while continua == True:

    info = {}
    info['nome'] = input('Qual é seu nome?\n')
    info['lance'] = float(input('Qual é o valor do seu lance?\nR$'))

    log_lances.append(info)
    valores_lances.append(info['lance'])

    opcao = int(input('Existem outros apostadores? Digite "1" para continuar, ou "0" para encerrar as apostas.\n'))
    if opcao == 1:
        continua = True
        clear()
    elif opcao == 0:
        continua = False
        clear()

maior_lance = max(valores_lances)

for dict in log_lances:
    if dict['lance'] == maior_lance:
        vencedor = dict['nome']
        print(f'O vencedor do leilão foi {vencedor} com o lance de R${maior_lance:.2f}')