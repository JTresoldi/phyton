maior_idade = 18
idade_especial = 17

#idade = int(input("Informe a sua idade:"))
idade = 19

if idade >= 18:
    print("Maior de idade, pode tirar a CNH")
elif idade == idade_especial:
    print("Pode fazer as aulas teoricas, mas nao as praticas.")
else:
    print("Não pode tirar CNH")
