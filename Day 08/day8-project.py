'''
Cifra de César

Em criptografia, a Cifra de César, também conhecida como cifra de troca,
código de César ou troca de César, é uma das mais simples e conhecidas
técnicas de criptografia. É um tipo de cifra de substituição na qual
cada letra do texto é substituída por outra, que se apresenta no
alfabeto abaixo dela um número fixo de vezes. Por exemplo,
com uma troca de três posições, A seria substituído por
D, B se tornaria E, e assim por diante.
'''

alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

palavra = input('Digite a sua mensagem:\n').lower()
numero = int(input('Escolha o número chave\n'))
opcao = int(input('Para ecriptar essa mensagem, digite "1". Para decriptar, digite "2"\n'))

def caesar(msg=palavra, num=numero, opc=opcao):

    palavra_resultante = ''

    for caractere in palavra:
        if caractere in alfabeto:
            for iter in range(len(alfabeto)):
                if caractere == alfabeto[iter]:
                    if opcao == 1:
                        indice = (iter + numero) % 26
                        palavra_resultante += alfabeto[indice]
                    elif opcao == 2:
                        indice = (iter - numero) % 26
                        palavra_resultante += alfabeto[indice]
                    else:
                        print(f'Escolha inválida. Inicie o programa novamente.')
        else:
            palavra_resultante += caractere

    print(f'{palavra_resultante}\n')


caesar()

continua = bool(int(input('Deseja digitar outra mensagem? Digite "1" para sim, "0" para não.\n')))

while continua:
    if continua:
        palavra = input('Digite a sua mensagem:\n').lower()
        numero = int(input('Escolha o número chave\n'))
        opcao = int(input('Para ecriptar essa mensagem, digite "1". Para decriptar, digite "2"\n'))
        caesar()
        continua = bool(int(input('Deseja digitar outra mensagem? Digite "1" para sim, "0" para não.\n')))
