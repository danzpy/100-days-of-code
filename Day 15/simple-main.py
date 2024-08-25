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
    else:
        print('Opção inválida. Tente novamente')

def recursos():
    global agua, leite, cafe, dinheiro

    print(f'\nÁgua: {agua}ml')
    print(f'Leite: {leite}ml')
    print(f'Café: {cafe}g')
    print(f'Dinheiro: ${dinheiro}\n')

def tipo_cafe():
    global dinheiro, leite, agua, cafe
    
    tipo_cafe = input('\nQual o café você deseja? (espresso/latte/cappuccino)\n\n')

    preco_cafe = MENU[tipo_cafe]['cost']
    qtd_leite = MENU[tipo_cafe]['ingredients']['milk']
    qtd_cafe = MENU[tipo_cafe]['ingredients']['coffee']
    qtd_agua = MENU[tipo_cafe]['ingredients']['water']

    dinheiro += preco_cafe
    total = insira_moedas()
    
    checa_suprimentos(preco_cafe, qtd_cafe, qtd_leite, qtd_agua, total)

    leite -= qtd_leite
    cafe -= qtd_cafe
    agua -= qtd_agua

def checa_suprimentos(preco, qtd_cafe, qtd_leite, qtd_agua, inserido):

    necessarios = [preco, qtd_leite, qtd_cafe, qtd_agua]
    disponiveis = {'dinheiro': inserido, 'leite': leite, 'café': cafe, 'água': agua}

    for index in range(0, 4):
        if list(disponiveis.values())[index] < necessarios[index]:
            print(f'{list(disponiveis.keys())[index]} -> Necessário ({necessarios[index]}) / Disponível {list(disponiveis.values())[index]}')
            print(f'Não há {list(disponiveis.keys())[index]} disponível para ser utilizado.')

def insira_moedas():
    global dinheiro

    print('\nPor favor, insira as moedas.')
    um_cent = int(input('Quantas moedas de um centavo? '))
    cinco_cent = int(input('Quantas moedas de cinco centavos? '))
    dez_cents = int(input('Quantas moedas de dez centavos? '))
    vinte_cinco_cent = int(input('Quantas moedas de vinte e cinco centavos? '))

    total = (um_cent * 1 + cinco_cent * 5 + dez_cents * 10 + vinte_cinco_cent * 25) / 100
    troco = total - dinheiro

    print(f'Aqui está seu troco: R${troco}')

    return total

def agradece():
    print('\nObrigado por utilizar nossos serviços.')

primeira_pergunta()
