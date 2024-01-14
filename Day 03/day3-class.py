'''
- Foram abordados as estruturas condicionais "if", "elif" e "else".
- Como utilizar estruturas condicionais aninhadas e múltiplas condições.
- Como utilizar operadores matemáticos "==", ">", "<=", "+=".. etc.
- Como utilizar operadores lógicos "AND" e "OR"

'''

nota = 85
frequencia = 95
if nota >= 70:
    if frequencia >= 75:
        print("Aprovado")
    else:
        print("Reprovado por frequência")
else:
    print("Reprovado por nota")


x = 10
y = 20
if x == y:
    print("x é igual a y")
elif x > y:
    print("x é maior que y")
else:
    print("x é menor ou igual a y")
x += y

print(f"Novo valor de x: {x}")


a = True
b = False
if a and b:
    print("Ambos a e b são verdadeiros")
elif a or b:
    print("Pelo menos um entre a e b é verdadeiro")
else:
    print("Nem a nem b são verdadeiros")


