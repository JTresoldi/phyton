# Bem-Vindo ao sistema de anotações de python do João, aqui vamos ver os comandos basicos para lembrar mais tarde de como usa-los.

### Print -> Mostrar algo na tela
    print ("Olá, Mundo!")

### Como guardar variaveis no sistema, a linguagem ja identifica qual tipo de variavel vai armazenar.
    name = "João"   # String  
    age = 26        # Int  
    altura = 1.90   # Float  
    verdade = True  # Booleano

### If e Else -> Como utilizar na linguagem
    idade = 18

    if idade >= 18:
        print("Maior de idade!")
    else:
        print("Menor de idade!")
        
## Repetição: While e For
### While -> Enquanto a condição for verdadeira
    contador = 0
    while contador < 3:
        print("Contando:", contador)
        contador += 1

### For -> Para cada item da lista
    nomes = ["João", "Amanda", "Minato", "Sebastian"]
    for nome in nomes: 
        print("Olá,", nome)
    
### Função
    def saudacao(nome):
        print("Bom dia,", nome)
    
saudacao("Rafael")

### Inputs -> Recebendo dados inseridos pelo usuário
    nome = input("Qual é o seu nome?")
    idade = int(input("Qual é a sua idade?"))

    print("Olá,", nome, "vc tem ", idade, "anos!")

### Função de maior ou menor de idade, aqui usamos if else para determinar se e maior ou menor, e aprendemos sobre inputs do tipo 'int' e 'string'
    def mairodeidade():
        nome = input("Qual é o seu nome?")
        idade = int(input("Qual é a sua idade?"))

        if idade >= 18:
            maioroumenor = "Maior de idade"
        else:
            maioroumenor = "Menor de idade"

        print("Olá,", nome, "você tem ", idade, "anos")
        print("Você é", maioroumenor,)

### Lista de coisas
    frutas = ["Maça", "Banana", "Uva"]
    print(frutas[0])

### Dicionario -> Tipo um cadastro
    pessoa = {
        "nome": "Lucas", 
        "idade": 30
    }
print(pessoa["nome"])

### Exemplo calculadora
    def somar(a, b):
        return a + b
    n1 = float(input("Digite o primeiro numero: "))  
    n2 = float(input("Digite o segundo numero: "

    resultado = somar(n1, n2)
    print("Resultado:", resultado)

