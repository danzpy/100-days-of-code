'''
Jogo da forca

O jogo da forca é um jogo em que o jogador tem que acertar
qual é a palavra proposta, tendo como dica o número de
letras e o tema ligado à palavra. A cada letra errada,
é desenhado uma parte do corpo do enforcado. O jogo
termina ou com o acerto da palavra ou com o término
do preenchimento das partes corpóreas do enforcado.
'''

from random import choice

palavras = ["casa", "carro", "trabalho", "escola", "amigo", "familia", "comida", "agua", "cidade", "rua", "livro", "computador", "telefone",
                    "jogo", "musica", "filme", "tv", "cama", "mesa", "cadeira", "porta", "janela", "parede", "teto", "chao", "luz", "noite", "dia",
                      "sol", "chuva", "neve", "vento", "calor", "frio", "quente", "frio", "doce", "salgado", "amargo", "sabor", "cheiro", "som",
                        "silencio", "riso", "choro", "correr", "andar", "pular", "dancar", "cantar", "falar", "ouvir", "ver", "tocar", "sentir",
                          "pensar", "saber", "aprender", "ensinar", "comprar", "vender", "dar", "receber", "comecar", "terminar", "abrir",
                            "fechar", "subir", "descer", "entrar", "sair", "acordar", "dormir", "comer", "beber", "rir", "sonhar", "viver",
                              "morrer", "ganhar", "perder", "amor", "odio", "alegria", "tristeza", "medo", "coragem", "paz", "guerra",
                                "verdade", "mentira", "bem", "mal"]

palavra_aleatoria = choice(palavras)

print('')

display = []

for letra in palavra_aleatoria:
    display.append('_')

a = ' |‾‾‾|'
b = ['     |', ' O   |']
c = ['     |', ' |   |', '/|   |', '/|\  |']
d = ['     |', '/    |', '/ \  |']
e = '     |'
f = '======'

pare_o_jogo = False
vidas = 6

while pare_o_jogo == False:

    palavra = ''
    for letra in display:
        palavra += letra + ' '

    print(f'\n{palavra}\n')

    if vidas == 6:
        print(f'{a}\n{b[0]}\n{c[0]}\n{d[0]}\n{e}\n{f}\n\n')

    if vidas != 0:
        letra_escolhida = input('Escolha uma letra\n')
        print('\n\n\n\n\n\n')

    if letra_escolhida not in palavra_aleatoria:
        vidas -= 1

    for position in range(len(palavra_aleatoria)):
        if palavra_aleatoria[position] == letra_escolhida:
            display[position] = letra_escolhida

   
    if vidas == 5:
        print(f'{a}\n{b[1]}\n{c[0]}\n{d[0]}\n{e}\n{f}\n\n')
    elif vidas == 4:
        print(f'{a}\n{b[1]}\n{c[1]}\n{d[0]}\n{e}\n{f}\n\n')
    elif vidas == 3:
        print(f'{a}\n{b[1]}\n{c[2]}\n{d[0]}\n{e}\n{f}\n\n')
    elif vidas == 2:
        print(f'{a}\n{b[1]}\n{c[3]}\n{d[0]}\n{e}\n{f}\n\n')
    elif vidas == 1:
        print(f'{a}\n{b[1]}\n{c[3]}\n{d[1]}\n{e}\n{f}\n\n')
    else:
        print(f'{a}\n{b[1]}\n{c[3]}\n{d[2]}\n{e}\n{f}\n\n')

     
    if vidas == -1 or '_' not in display:
        pare_o_jogo = True
    else:
        pare_o_jogo = 0

if '_' not in display:
    print('Você ganhou!\n')
else:
    print('Você perdeu.\n')

