from data import MENU, resources, money

def opcoes_resposta(response, opt1, opt2):
    if response == 1:
        opt = opt1()
    elif response == 2:
        opt = opt2()
    else:
        print('\nResposta inválida. Tente novamente.')
    
    return opt

def valida_resposta(response, desejavel, opt1, opt2):
    if response == desejavel or response in (list(response)):
        print(response)
        opt1()
    else:
        opt2()

def deseja_continuar():
    response = int(input('\nDeseja continuar? \n\nDigite 1 para sim.\nDigite 2 para não.\n\n'))
    return response

def agradece():
    print('\nObrigado por utilizar nossos serviços.')

def acoes_usuario():
    response = int(input('Bem vindo! Qual ação deseja realizar?\n\nDigite 1 para verificar o status da máquina.\nDigite 2 para solicitar sua bebida.\n\n'))
    return response

def tipo_cafe():
    response = input('\nQual o café você deseja? (espresso/latte/cappuccino)\n\n')
    return response

def recursos():
    print(f'\nÁgua: {list(resources.values())[0]}ml')
    print(f'Leite: {list(resources.values())[1]}ml')
    print(f'Café: {list(resources.values())[2]}g')
    print(f'Dinheiro: ${money['value']}\n')

def insira_moedas():
    print('Por favor, insira as moedas.')
    um_cent = int(input('Quantas moedas de um centavo? '))
    cinco_cent = int(input('Quantas moedas de cinco centavos? '))
    dez_cents = int(input('Quantas moedas de dez centavos? '))
    vinte_cinco_cent = int(input('Quantas moedas de vinte e cinco centavos? '))

    total = um_cent * 1 + cinco_cent * 5 + dez_cents * 10 + vinte_cinco_cent * 25
    print(f'{total} inseridos')


def main():
    resposta_acao = acoes_usuario()
    resposta = opcoes_resposta(resposta_acao, recursos, tipo_cafe)
    valida_resposta(resposta, None, deseja_continuar, insira_moedas)

main()