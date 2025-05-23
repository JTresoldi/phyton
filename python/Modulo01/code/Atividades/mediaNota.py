'''
Peça uma nota de 0 a 10 e diga se o aluno foi aprovado (nota ≥ 7), recuperação (5 a 6.9) ou reprovado (< 5).
'''
nome = input("Bem vindo, para iniciar digite seu nome: ")
n1 = int(input("Digite a Nota 1: "))
n2 = int(input("Digite a Nota 2: "))
n3 = int(input("Digite a Nota 3: "))
n4 = int(input("Digite a Nota 4: "))

nota = (n1 + n2+ n3 + n4) / 4

if nota >= 7:
    print(nome, "sua média foi:", nota, "e você foi... APROVADO!")
elif nota >= 5 and nota <= 6.9:
    print(nome, "sua média foi:", nota, "e você foi... RECUPERAÇÃO")
elif nota <= 4.9:
    print(nome, "sua média foi:", nota, "e você foi... REPROVADO")
else:
    print("Nota invalida, refaça a digitação")