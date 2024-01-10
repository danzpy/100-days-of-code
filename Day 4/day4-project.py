'''
Pedra, papel e tesoura

Também chamado em algumas regiões do Brasil de jokenpô,
é um jogo de mãos recreativo e simples para duas ou mais
pessoas, que não requer equipamentos nem habilidade.

Nesse jogo, os jogadores devem simultaneamente esticar a mão,
na qual cada um formou um símbolo (que significa pedra, papel ou tesoura).
Então, os jogadores comparam os símbolos para decidir quem ganhou, da seguinte forma:

Pedra ganha da tesoura (amassando-a ou quebrando-a).
Tesoura ganha do papel (cortando-o).
Papel ganha da pedra (embrulhando-a).
'''

from random import randint

opcao_aleatoria = randint(0, 2)
escolha_computador_str = None
escolha_computador_num = ''

sua_escolha = int(input('Vamos jogar "Jokenpô". O que você escolhe? 0 para "Pedra", 1 para "Papel" e 2 para "Tesoura"\n'))
sua_escolha_str = 'string'

if sua_escolha == 0:
    sua_escolha_str = 'Pedra'
elif sua_escolha == 1:
    sua_escolha_str = 'Papel'
elif sua_escolha == 2:
    sua_escolha_str = 'Tesoura'
else:
    print(f'Você digitou {sua_escolha}, valor indevido.')

if opcao_aleatoria == 0:
    escolha_computador_str = 'Pedra'
    escolha_computador_num = 0
elif opcao_aleatoria == 1:
    escolha_computador_str = 'Papel'
    escolha_computador_num = 1
else:
    escolha_computador_str = 'Tesoura'
    escolha_computador_num = 2

if (sua_escolha == 0 and escolha_computador_num == 1) or (sua_escolha == 1 and escolha_computador_num == 0) or (sua_escolha == 2 and escolha_computador_num == 1):
    print(f'Você escolheu {sua_escolha_str} e o computador escolheu {escolha_computador_str}. Parabéns, você ganhou!')
elif sua_escolha == opcao_aleatoria:
    print(f'Você escolheu {sua_escolha_str} e o computador escolheu {escolha_computador_str}. Ninguém ganhou!')
elif sua_escolha > 2 or sua_escolha < 0:
    print('Jogue novamente.')
else:
    print(f'Você escolheu {sua_escolha_str} e o computador escolheu {escolha_computador_str}. Você perdeu!')-1