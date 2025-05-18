# Identação e Blocos
### A estética
Em resumo, identar código é uma forma de manter o código fonte legível e manutenível.  
Em Python o interpretador consegue determinar onde um bloco de comando ***inicia e onde ele termina.***
***
## Exemplo:
### Bloco em JAVA:
    void sacar(double valor) { Inicio do bloco
        if (this.saldo >= valor) { inicio do bloco
            this.saldo -= valor;
        } Fim do bloco
    } Fim do bloco

### Bloco em PYTHON:
    def sacar(self, valor: float) -> None: #Inicio do bloco do metodo
        if self.saldo >= valor: #Inicio do bloco if
            self.saldo -= valor
        #fim do bloco if
    #fim do bloco do metodo
***
# Estruturas condicionais
### O que são?
A estrutura condicional permite o desvio de fluxo de controle, quando determinadas expressões lógicas são atendidas.

### If, Else
    saldo = 2000.0
    saque = floar(input("Informe o valor do saque:"))

    if saldo >= saldo:
        print("Realizando saque!)
    else:
        print("Saldo insuficiente")

### if/ elif / else
Em alguns cenários queremos mais de dois desvios, para isso podemos utilizar a palavra reservada ***elif***. O elif é composto por uma nova expressão lógica, que será testada e caso retorne verdadeiro o bloco de código do elif será executado.

### Exemplo:
    opcao = int(input("Informe uma opção: [1] Sacar \n[2] Extrato: "))

    if opcao == 1:
        valor = float(input("Informe a quantidade para o saque: "))
        #...
    
    elif opcao ==2:
        print("Exibindo o extrato")

    else:
        sys.exit("Opção Invalida!")

***
### If aninhado
Podemos criar estruturas condicionais aninhadas, para isso basta adicionar estruturas if/elif/else dentro do bloco de código de estruturas if/elif/else

### Exemplo:
    if conta_normal:
        if saldo >= saque:
            print("Saque realizado com sucesso!")
        elif saque <= (saldo + cheque_especial):
            print("Saque realizado com uso do cheque especial!")
        else:
            print("Não foi possivel realizar o saque, saldo insuficiente!")
    elif conta_universitaria:
        if saldo >= salque:
            print("Saque realizado com sucesso!")
        else:
            print("Saldo insuficiente!")
***
### If ternário
O if ternário permite escrever uma condição em uma úinica linha. Ele é composto por três partes, a primeira parte é o retorno caso a expressão retorne verdadeiro, a segunda parte é a expressão lógica e a terceira parte é o retorno caso a expressão não seja atendida.
### Exemplo:
    status = "Sucesso" if saldo >= saque else "Falha"

    print(f"{satatus} ao realizar o saque!")
***
# Estruturas de Repetição
São estruturas utilizadas para repetir um trecho de código um determinado número de vezes.

### Exemplo sem repetição:
    #receba um numero e exiba os 2 numeros seguintes
    
    a = int(input("Informe um número inteiro:"))
    print(a)

    a += 1
    print(a)

    a += 1
    print(a)
***
### Comando For
O for é usado para percorrer um objeto iterável. Faz sentido usar for quando sabemos o númeors exato de vezes que o bloco dever ser executado.

    texto = input("Informe um texto: ")
    VOGAIS = "AEIOU"

    for letra in texto:
        if letra.upper() in VOGAIS:
            print(letra, end="")
    print() #add uma quebra de linha
***
### Função range
Range é uma função built-in do Python, usada para produzir uma sequencia den umeros inteiros a partir de um inicio (inclusivo) para um fim (exclusivo).  
Ela recebe 3 argumentos: stop (obrigatorio), star (opcional) e step (opcional).

    #range (stop) -> range object
    #range (start, stop[, step]) -> range object

    list(range(4))
    >>> [0, 1, 2, 3]
***
### Utilizando range com for
    for numero in range (0, 11):
        print(numero, end=" ")

    >>> 0 1 2 3 4 5 6 7 8 9 10

    #exibindo a tabuada do 5
    for numero in range (0, 51, 5):
        print(numero, end=" ")

    >>> 0 5 10 15 20 25 30 35 40 45 50 
***
### Comando while
O while é usado para repetir um bloco de código várias vezes. Faz sentido usar while quando não sabemos o numero exato de vezes que nosso bloco deve ser executado.

    opcao = -1 

    while opcao != 0:
        opcao = int(input("[1] Sacas \n[2] Extrato \n[0] Sair \n: "))

        if opcao ==1:
            print("Sacando...")
        elif opcao ==2:
            print("Exibindo o extrato...")

