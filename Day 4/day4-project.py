from random import randint

random_option = randint(0, 2)
computer_choice_str = None
computer_choice_number = 'string'

your_choice = int(input('Vamos jogar "Jokenpô". O que você escolhe? 0 para "Pedra", 1 para "Papel" e 2 para "Tesoura"\n'))
your_choice_str = 'string'

if your_choice == 0:
    your_choice_str = 'Pedra'
elif your_choice == 1:
    your_choice_str = 'Papel'
elif your_choice == 2:
    your_choice_str = 'Tesoura'
else:
    print(f'Você digitou {your_choice}, valor indevido.')

if random_option == 0:
    computer_choice_str = 'Pedra'
    computer_choice_number = 0
elif random_option == 1:
    computer_choice_str = 'Papel'
    computer_choice_number = 1
else:
    computer_choice_str = 'Tesoura'
    computer_choice_number = 2

if (your_choice == 0 and computer_choice_number == 1) or (your_choice == 1 and computer_choice_number == 0) or (your_choice == 2 and computer_choice_number == 1):
    print(f'Você escolheu {your_choice_str} e o computador escolheu {computer_choice_str}. Parabéns, você ganhou!')
elif your_choice == random_option:
    print(f'Você escolheu {your_choice_str} e o computador escolheu {computer_choice_str}. Ninguém ganhou!')
elif your_choice > 2 or your_choice < 0:
    print('Jogue novamente.')
else:
    print(f'Você escolheu {your_choice_str} e o computador escolheu {computer_choice_str}. Você perdeu!')-1