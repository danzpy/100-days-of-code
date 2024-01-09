alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

palavra = input('Digite a sua mensagem:\n').lower()
numero = int(input('Escolha o número chave\n'))


palavras = palavra.split(' ')

def encripta(encriptando=palavras):

    palavra_encriptada = ''

    for palavra in palavras:
        for letra in palavra:
            for iter in range(len(alfabeto)):
                if letra == alfabeto[iter]:
                    recomeca = (iter + numero) - 26
                    if recomeca >= 0:
                        letra_encriptada = alfabeto[recomeca]
                        palavra_encriptada += letra_encriptada
                    else:
                        letra_encriptada = alfabeto[iter + numero]
                        palavra_encriptada += letra_encriptada

        if len(palavras) >= 2:
            palavra_encriptada += ' '

    print(palavra_encriptada)

def decripta(decriptando=palavras):

    palavra_decriptada = ''

    for palavra in palavras:
        for letra in palavra:
            for iter in range(len(alfabeto)):
                if letra == alfabeto[iter]:
                    letra_decriptada = alfabeto[iter - numero]
                    palavra_decriptada += letra_decriptada

        if len(palavras) >= 2:
            palavra_decriptada += ' '        

    print(palavra_decriptada)



opcao = int(input('Para encriptar essa mensagem, digite "1". Para decriptar, digite "2"\n'))
while opcao != 1 or opcao != 2:
    if opcao == 1:
        encripta(encriptando=palavras)
        break
    elif opcao == 2:
        decripta(decriptando=palavras)
        break
    else:
        print(f'A opção {opcao} não está disponível. Tente novamente.')
        opcao = int(input('Para encriptar essa mensagem, digite "1". Para decriptar, digite "2"\n'))
