***
# Operadores Aritmétricos Python

### Adição
    print(1 + 1)
    >>> 2

### Subtração
    print(10 - 2)
    >>> 8

### Multiplicação
    print(4 * 3)
    >>> 12

### Divisão
    print(12 / 3)
    >>> 4.0

### Divisão Inteira
    print(12 // 2)
    >>> 6

### Módulo
Resto da dvisão   

    print(10 % 3)
    >>> 1

### Exponenciação
    print(2 ** 3)
    >>> 8

***
# Operadores de Comparação
### Igualdade 
    saldo = 450
    saque = 200

    print(saldo == saque)
    >>> False

### Diferença
    saldo = 450
    saque = 200

    print(saldo != saque)
    >>> True

### Maior que / maior ou igual
    saldo = 450
    saque = 200

    print(saldo > saque)
    >>> True

    print(saldo >= saque)
    >>> True

### Menor que / menor ou igual
    saldo = 450
    saque = 200

    print(saldo <>> saque)
    >>> False

    print(saldo <=> saque)
    >>> False

***
# Operadores de atribuição
### Atribuição Simples
    saldo = 500

    print(saldo)
    >>> 500

### Atribuição com Adição
    saldo = 500
    saldo += 200

    print(saldo)
    >>> 700

### Atribuição com Subtração
    saldo = 500
    saldo -= 200

    print(saldo)
    >>> 300

### Atribuição com Multiplicação
    saldo = 500
    saldo *= 2

    print(saldo)
    >>> 1000

### Atribuição com Divisão
    saldo = 500
    saldo /= 5

    print(saldo)
    >>> 100.0

    saldo = 500
    saldo //= 5

    print(saldo)
    >>> 100

### Atribuição com Módulo
    saldo = 500
    saldo %= 480

    print(saldo)
    >>> 20

### Atribuição com exponenciação
    saldo = 80
    saldo **= 2

    print(saldo)
    >>> 6400

***
# Operadores Lógicos
### Operador 'E' - 'AND'
    saldo = 1000
    saque = 200
    limite = 100

    saldo >= saque and saque <= limite
    >>> False

### Operador 'OU' - 'OR'
    saldo = 1000
    saque = 200
    limite = 100

    saldo >= saque or saque <= limite
    >>> True

### Operador 'Negação' - 'NOT'
    contatos_emergencia = []

    not 1000 > 1500
    >>> True

    not contatos_emergencia
    >>> True

    not "Saque 1500;"
    >>> False

    not ""
    >>> True

### Parênteses
    saldo = 1000
    saque = 200
    limite = 100
    conta_especial = True

    saldo >= saque and saque <= limite or conta_especial and saldo >= saque
    >>> True

    (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)
    >>> True

***
# Operadores de Identidade
São operadores utilizados para comparar se os dois objetos testados ocupam a mesma posição na memória.  

### Exemplo:
    curso = "Curso de Python"
    nome_curso = curso
    saldo, limite = 200, 200

    curso is nome_curso
    >>> True

    curso is not nome_curso
    >>> False

    saldo is limite
    >>> True

*** 
# Operadores de Associação
São operadores utilizados para verificar se um objeto está presente em uma sequência.   

### Exemplo:
    curso = "Curso de Python"
    frutas = ["laranja", "uva", "limão"]
    saques = [1500, 100]

    "Python" in curso
    >>> True

    "maça" not in frutas
    >>> True

    200 in saques
    >>> False

Lembrando que o comparador de associação é Case Sensitive, então capslook faz diferença.