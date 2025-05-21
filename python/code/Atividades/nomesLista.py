'''
Peça ao usuário 5 nomes e guarde numa lista. Depois, imprima todos em maiúsculas.
'''

nomes = []
print("Digite os nomes: ")

for i in range(5):
    nome = input(f"Digite o {i + 1}º nome: ")
    nomes.append(nome)

print("\nOs nomes da lista são: ")
for nome_na_lista in nomes:
    print(nome_na_lista.upper())