'''
Peça um número e diga se ele é par ou ímpar.
'''

print("Descubra se o número é par ou impar!")
num = float(input("Digite um numero: "))

if num % 2 == 0:
    print("O numero", num, "é PAR!")
else:
    print("O numero", num, "é IMPAR!")