'''
- Foram abordados os tipos de dados presentes em Python. Sendo que é possível verifica-los através da função "type()".
- Para alterar tipos de dados é possível utilizar funções como "int()", "str()" ou "float()".
- Para alterar o número de casas decimais, é possível utilizar a função "round()".
- Foram introduzidos os operadores matemáticos "+", "-", "*", "/", "//"..
- Como utilizar f'strings e quais suas vantagens

'''

type(8)

type(7.4)

type('String')

type(True)


var1 = 8.0

var2 = int(var1)

var3 = str(var2)

var4 = 3


print(var1 + var2)
print(var3 + var3)
print(var1 / var2)
print(var1 // var2)
print(var1 * var2)
print(var1 % var2)
print(var1 / var4)
print(round(var1 / var4))


print(f'A variável 1 ({var1}) é do tipo float.\nJá a var2 ({var2}) é do tipo int.\nA última variável, var3 ({var3}) é uma string.')