nome = "Joao"
idade = 26
profissao = "Programador"
linguagem = "Python"

print("Nome: %s Idade: %d" % (nome, idade))
print("Nome: {} Idade: {}" .format(nome, idade))
print("Nome: {1} Idade: {0}" .format(idade, nome))
print("Nome: {nome} Idade: {idade}" .format(nome=nome, idade=idade))

print(f"Nome: {nome} Idade: {idade}")
