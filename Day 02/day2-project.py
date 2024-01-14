print('Bem-vindo a calculadora de gorjetas!')
bill = float(input('Qual o valor total da conta? R$'))
perc_tip = int(input('Qual a porcentagem da gorjeta? Digite apenas o valor (sem o %)'))
peoples = int(input('Quantas pessoas irão dividir a conta? '))

perc_tip_convertion = perc_tip / 100
total_bill = bill * (1 + perc_tip_convertion)
should_pay = total_bill / peoples

print(f'Cada pessoa deverá pagar: R${round(should_pay, 2)}')
