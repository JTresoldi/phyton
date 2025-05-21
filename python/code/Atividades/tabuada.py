'''
Mostre os números de 1 a 10 usando for.
'''
for num in range(1, 11):
    print(num, end=" ")

'''
Peça um número e mostre a tabuada dele de 1 a 10.
'''
numero = int(input("\nEscolha um numero de 1 a 10 para ver a tabuada dele:"))
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
print("============================")

