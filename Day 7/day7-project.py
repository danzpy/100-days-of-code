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

#print(palavra_aleatoria)
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

stop_the_game = False
lifes = 6

while stop_the_game == False:

    palavra = ''
    for letra in display:
        palavra += letra + ' '

    print(f'\n{palavra}\n')

    if lifes == 6:
        print(f'{a}\n{b[0]}\n{c[0]}\n{d[0]}\n{e}\n{f}\n\n')

    if lifes != 0:
        letra_escolhida = input('Escolha uma letra\n')
        print('\n\n\n\n\n\n')

    if letra_escolhida not in palavra_aleatoria:
        lifes -= 1

    for position in range(len(palavra_aleatoria)):
        if palavra_aleatoria[position] == letra_escolhida:
            display[position] = letra_escolhida

   
    if lifes == 5:
        print(f'{a}\n{b[1]}\n{c[0]}\n{d[0]}\n{e}\n{f}\n\n')
    elif lifes == 4:
        print(f'{a}\n{b[1]}\n{c[1]}\n{d[0]}\n{e}\n{f}\n\n')
    elif lifes == 3:
        print(f'{a}\n{b[1]}\n{c[2]}\n{d[0]}\n{e}\n{f}\n\n')
    elif lifes == 2:
        print(f'{a}\n{b[1]}\n{c[3]}\n{d[0]}\n{e}\n{f}\n\n')
    elif lifes == 1:
        print(f'{a}\n{b[1]}\n{c[3]}\n{d[1]}\n{e}\n{f}\n\n')
    else:
        print(f'{a}\n{b[1]}\n{c[3]}\n{d[2]}\n{e}\n{f}\n\n')

     
    if lifes == -1 or '_' not in display:
        stop_the_game = True
    else:
        stop_the_game = 0

if '_' not in display:
    print('Você ganhou!\n')
else:
    print('Você perdeu.\n')

