'''
Peça 5 números e diga qual é o maior.
'''

print("Digite 5 números: ")
for i in range(1, 6):
    numero = int(input(f"Digite o {i} número: "))
    maiorNumero = numero
if numero > maiorNumero:
    maiorNumero = numero
    
print(f"O máior número é: {maiorNumero} ")