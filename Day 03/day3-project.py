print("*******************************************************************************")
print("          |                   |                  |                     |")
print(" _________|________________.=\"\"_;=.______________|_____________________|_______")
print("|                   |  ,-\"_,=\"\"     `\"=.|                  |")
print("|___________________|__\"=._o`\"-._        `\"=.______________|___________________")
print("          |                `\"=._o`\"=._      _`\"=._                     |")
print(" _________|_____________________:=._o \"=._.\"_.-=\"'\"=.__________________|_______")
print("|                   |    __.--\" , ; `\"=._o.\" ,-\"\"\"-._ \".   |")
print("|___________________|_._\"  ,. .` ` `` ,  `\"-._\"-._   \". '__|___________________")
print("          |           |o`\"=._` , \"` `; .\". ,  \"-._\"-._; ;              |")
print(" _________|___________| ;`-.o`\"=._; .\" ` '`.\"\\` . \"-._ /_______________|_______")
print("|                   | |o;    `\"-.o`\"=._``  '` \" ,__.--o;   |")
print("|___________________|_| ;     (#) `-.o `\"=.`_.--\"_o.-; ;___|___________________")
print("____/______/______/___|o;._    \"      `\".o|o_.--\"    ;o;____/______/______/____")
print("/______/______/______/_=._o--._        ; | ;        ; ;/______/______/______/_")
print("____/______/______/______/__\"=._o--._   ;o|o;     _._;o;____/______/______/____")
print("/______/______/______/______/____\"=._o._; | ;_.--\"o.--\"_/______/______/______/_")
print("____/______/______/______/______/_____=o|o_.--\"\"___/______/______/______/____")
print("/______/______/______/______/______/______/______/______/______/______/________")
print("*******************************************************************************")

print('Bem-vindo à Ilha do Tesouro!')
print('Sua missão é encontrar o tesouro perdido.')
road = input('Você está no meio da praia, o que deseja fazer? Para ir até a floresta, digite "F". Para ir até o vulcão, digite "V". ')

if road == 'F':
    airplane = input('Você encontra destroços de um avião, preso em uma árvore. Você deseja subi-la e investigar os destroços? Digite "S" para sim e "N" para não. ')
    if airplane == "S":
        airplane_choice1 = input('Você percebe que está anoitecendo, mas visualiza um papel úmido, em um local de difícil acesso. Parece ser um mapa. Deseja voltar para a floresta? "S" ou "N" ')
        if airplane_choice1 == 'N':
            print('Ao tentar alcançar o vestígio de papel, você acaba preso em uma armadilha. Infelizmente, você não sobreviveu.')
        else:
            airplane_choice2 = input('Deseja ir até o vulcão? Ou procurar o tesouro pela praia? "V" para vulcão "P" para praia. ')
            if airplane_choice2 == 'V':
                volcano_choice = input('Você encontra uma caverna escondida perto do vulcão. Deseja entrar? "S" para sim, "N" para não. ')
                if volcano_choice == 'S':
                    print('Parabéns! Você encontrou o tesouro escondido na caverna do vulcão! 🎉')
                else:
                    print('Você decide não entrar na caverna e acaba se perdendo na floresta. Infelizmente, você não sobreviveu.')
            else:
                beach_choice = input('Você encontra uma garrafa com uma mensagem na praia. Deseja abrir? "S" para sim, "N" para não. ')
                if beach_choice == 'S':
                    print('A mensagem na garrafa é um mapa do tesouro! Mas ao seguir o mapa, você cai em uma armadilha. Infelizmente, você não sobreviveu.')
                else:
                    print('Você decide não abrir a garrafa e acaba se perdendo na praia. Infelizmente, você não sobreviveu.')
    else:
        print('Você decide não subir na árvore e continua a explorar a floresta. De repente, você encontra uma trilha. Infelizmente, a trilha leva a um precipício e você não sobreviveu.')
else:
    volcano = input('Você chega ao pé do vulcão. Há uma trilha que leva ao topo. Deseja subir? "S" para sim, "N" para não. ')
    if volcano == 'S':
        volcano_choice = input('Você encontra uma caverna no topo do vulcão. Deseja entrar? "S" para sim, "N" para não. ')
        if volcano_choice == 'S':
            print('Ao entrar na caverna, o vulcão entra em erupção. Infelizmente, você não sobreviveu.')
        else:
            print('Você decide não entrar na caverna e acaba se perdendo na montanha. Infelizmente, você não sobreviveu.')
    else:
        beach_choice = input('Você encontra uma garrafa com uma mensagem na praia. Deseja abrir? "S" para sim, "N" para não. ')
        if beach_choice == 'S':
            print('A mensagem na garrafa é um mapa do tesouro! Mas ao seguir o mapa, você cai em uma armadilha. Infelizmente, você não sobreviveu.')
        else:
            print('Você decide não abrir a garrafa e acaba se perdendo na praia. Infelizmente, você não sobreviveu.')



