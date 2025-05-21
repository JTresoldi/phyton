'''
Crie um programa que peça o nome e a idade do usuário e exiba uma mensagem de boas-vindas. 
Peça o ano de nascimento do usuário e calcule a idade atual.
'''

nome = input("Olá pessoa, para começarmos digite o seu nome:")
nasc = int(input("Agora digite o ano que você nasceu:"))

idade = 2025 - nasc

print(nome, "você tem:", idade)

if idade >= 18:
    print("Você PODE tirar a CNH!")
else: 
    print("Você ainda NÃO pode tirar a CNH!")