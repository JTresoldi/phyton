'''
Crie um programa que peça o nome e a senha do usuário e só permita continuar se a senha for "python123". Use while.
'''

nome = input("Digite seu nome:")
senha = ""

while senha != "python123":
    senha = input("Digite a senha: ")
    if senha != "python123":
        print("Senha incorreta. Tente novamente!")

print(f"Bem-vindo, {nome} você descobriu a senha!")