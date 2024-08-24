from data import MENU, resources, money

def valida_resposta(response, function_true, function_false):
    if response == 1:
        function_true()
    elif response == 2:
        function_false()
    else:
        print('\nResposta inválida. Tente novamente.')

def deseja_continuar():
    response = int(input('\nDeseja continuar? \n\nDigite 1 para sim.\nDigite 2 para não.\n\n'))
    return response

def agradece():
    print('\nObrigado por utilizar nossos serviços.')

def acoes_usuario():
    response = int(input('Bem vindo! Qual ação deseja realizar?\n\nDigite 1 para verificar o status da máquina.\nDigite 2 para solicitar sua bebida.\n\n'))
    return response

def tipo_cafe():
    response = input('Qual o café você deseja? (espresso/latte/cappuccino)\n\n')
    return response

def recursos():
    print(f'\nÁgua: {list(resources.values())[0]}ml')
    print(f'Leite: {list(resources.values())[1]}ml')
    print(f'Café: {list(resources.values())[2]}g')
    print(f'Dinheiro: ${money['value']}\n')

def main():
    resposta_acao = acoes_usuario()
    valida_resposta(resposta_acao, recursos, tipo_cafe)
    continua = deseja_continuar()
    valida_resposta(continua, recursos, agradece)

main()
