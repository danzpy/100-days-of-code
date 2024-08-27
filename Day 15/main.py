from data import MENU, resources, money

agua = resources['water']
leite = resources['milk']
cafe = resources['coffee']
dinheiro = money['value']

def primeira_pergunta():
    pergunta = int(input('O que você deseja?\n\nDigite 1 para report.\nDigite 2 para escolher sua bebida.\n\n'))

    if pergunta == 1:
        recursos()
        primeira_pergunta()
    elif pergunta == 2:
        tipo_cafe()
    elif pergunta == 'off':
        desliga()
    else:
        opcao_invalida()

def recursos():
    global agua, leite, cafe, dinheiro

    print(f'\nÁgua: {agua}ml')
    print(f'Leite: {leite}ml')
    print(f'Café: {cafe}g')
    print(f'Dinheiro: ${dinheiro}\n')

def tipo_cafe():
    global dinheiro, leite, agua, cafe
    
    tipo_cafe = input('\nQual o café você deseja? (espresso/latte/cappuccino)\n\n')

    if tipo_cafe in ['espresso', 'latte', 'capuccino']:
        qtd_leite = MENU[tipo_cafe]['ingredients']['milk']
        qtd_cafe = MENU[tipo_cafe]['ingredients']['coffee']
        qtd_agua = MENU[tipo_cafe]['ingredients']['water']

        if checa_suprimentos(qtd_cafe, qtd_leite, qtd_agua):
            if insira_moedas(tipo_cafe):
                print(f'Aqui está seu {tipo_cafe}, aproveite!\n')

                leite -= qtd_leite
                cafe -= qtd_cafe
                agua -= qtd_agua
    else:
        opcao_invalida()

    primeira_pergunta()

def checa_suprimentos(qtd_cafe, qtd_leite, qtd_agua):

    suficiente = True

    necessarios = [qtd_leite, qtd_cafe, qtd_agua]
    disponiveis = {'leite': leite, 'café': cafe, 'água': agua}

    for index in range(0, 3):
        if list(disponiveis.values())[index] < necessarios[index]:
            print(f'Não há {list(disponiveis.keys())[index]} disponível para ser utilizado.')
            suficiente = False

    return suficiente

def insira_moedas(tipo_cafe):
    global dinheiro

    preco_cafe = MENU[tipo_cafe]['cost']
    suficiente = True

    print('\nPor favor, insira as moedas.')
    um_cent = int(input('Quantas moedas de um centavo? '))
    cinco_cent = int(input('Quantas moedas de cinco centavos? '))
    dez_cents = int(input('Quantas moedas de dez centavos? '))
    vinte_cinco_cent = int(input('Quantas moedas de vinte e cinco centavos? '))

    total = (um_cent * 1 + cinco_cent * 5 + dez_cents * 10 + vinte_cinco_cent * 25) / 100
    
    if total > preco_cafe:
        troco = total - preco_cafe
        dinheiro += preco_cafe
        print(f'Aqui está seu troco: R${troco}')
    else:
        print('Você não possui dinheiro suficiente...')
        suficiente = False

    return suficiente

def agradece():
    print('\nObrigado por utilizar nossos serviços.')

def opcao_invalida():
    print('Opção inválida, tente novamente...')

def desliga():
    print('Desligando a máquina...')
    agradece()

primeira_pergunta()
