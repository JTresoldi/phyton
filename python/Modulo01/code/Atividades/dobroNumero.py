'''
Proposta:
Crie uma função chamada dobro(numero) que retorna o dobro do número. Teste com um número digitado pelo usuário.
'''

def dobro(numero):
    resultado = numero * 2
    return resultado

num = int(input("Digite um número: "))
valor = dobro(num)
print(f"O dobro de {num} é: {valor}")