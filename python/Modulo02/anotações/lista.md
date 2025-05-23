***
# Listas em Python

### Criando listas
Listas em Python são coleções sequenciais e mutáveis que podem armazenar diversos tipos de objetos. Elas podem ser criadas usando o construtor list(), a função range(), ou simplesmente colocando valores separados por vírgulas dentro de colchetes []. Por serem mutáveis, você pode modificar seus elementos após a criação.

### Exemplo
    frutas = ["laranja", "maca", "uva"]

    frutas = []

    letras = list("python")
    #Cada letra se torna um argumento.

    numeros = list(range(10))
    #Cria um elemento para cada numero.

    carro = ["Ferrari", "F8", 4200000, 2020, 2900, "São Paulo", True]
***
### Lista aninhadas
Listas podem armazenar outras listas. Podendo criar estruturas bidimensionais (tabelas).
    matriz = [
        [1, "a", 2]
        ["b", 3, 4]
        [6, 5, "c"]
    ]

    matriz[0] # [1, "a", 3]
    matriz [0][0] # 1
    matriz [0][1] # 2
    matriz[-1][-1] # "c"
***
### Fatiamento
Podemos extrair um conjunto de valores de uma sequência. Basta passar o indice inial e/ou final para acessar o conjunto. Podemos informar quantas posições o cursor deve "pular".
    lista = ["p", "y", "t", "h", "o", "n"]
    
    lista[2:]  # ["t", "h", "o", "n"]
    lista[:2]  # ["p", "y"]
    lista[1:3] # ["y", "t"]
    lista[0:3:2] # ["p", "t"]
    lista[::]  # ["p", "y", "t", "h", "o", "n"]
    lista[::-1] # ["n", "o", "h", "t", "y", "p"]
***
### Iterar listas
Comumente utilizamos o comando **For** para percorrer os dados de uma lista.
    carros = ["gol", "celta", "palio"]

    for carro in carros:
        print(carro)
***
### Função enumerate
Para saber qual o indice do objeto dentro do laço **for**. Usamos a função **enumerate**
    carros = ["gol", "celta", "palio"]

    for carro in carros:
        print(f"{indice}:{carro}")
***
### Compreensão de listas
Oferece uma sintaxe mais curta quando deseja: Criar uma nova lista com base nos valores de uma lista existente (filtro) ou gerar uma nova lista aplicando alguma modificação nos elementos d eum lista existente.
    numero = [1, 30, 21, 2, 9, 65, 34]
    pares = []

    for numero in numeros:
        if numero % 2 == 0:
            pares.append(numero)

#### comprehension
    numero = [1, 30, 21, 2, 9, 65, 34]
    pares = [numero for numero in numeros if numero % 2 == 0]
***

### [].append
    lista = []

    lista.append(1)
    lista.append("Python")
    lsita.append([40, 30, 20])

    print(lsita) # [1, "Python", [40, 30, 20]]
***
### [].clear
    lsita = [1, "Python", [40, 30, 20]]

    print(lsita) # [1, "Python", [40, 30, 20]]

    lista.clear()

    print(lista) # []
***
### [].copy
    print(lsita) # [1, "Python", [40, 30, 20]]

    lista.copy()

    print(lsita) # [1, "Python", [40, 30, 20]]
***
### [].count
Usado para contar quantas vezes um objeto foi usado na sua lista.

    cores = ["vermelho", "azul", "verde", "azul"]

    cores.count("vermelho") # 1
    cores.count("azul") # 2
    cores.count("verde") # 1
***
### [].extend
    linguagens = ["python", "js", "c"]

    print(linguagens) # ["python", "js", "c"]

    linguagens.extend(["java", "csharp"])

    print(linguagens) # ["python", "js", "c", "java", "csharp"]
***
### [].index
    linguagens = ["python", "js", "c", "java", "csharp"]

    linguagens.index("java") # 3
    linguagens.index("python") # 0
***
### [].pop
Funciona igual um Pilha de itens, FILO

    linguagens = ["python", "js", "c", "java", "csharp"]

    linguanges.pop() # csharp
    linguanges.pop() # java
    linguanges.pop() # c
    linguanges.pop(0) # python
***
### [].remove
    linguagens = ["python", "js", "c", "java", "csharp"]

    linguagens.remove("c")

    print(linguagens) # ["python", "js", "java", "csharp"]
***
### [].reverse
    linguagens = ["python", "js", "c", "java", "csharp"]

    linguagens.reverse()

    print(linguagens) # ["csharp", "java", "c", "js", "python"]
***
### [].sort
    linguagens = ["python", "js", "c", "java", "csharp"]
    linguagens.sort() # ["c", "csharp", "java", "js", "python"]

    linguagens = ["python", "js", "c", "java", "csharp"]
    linguagens.sort(reverse=True) # ["python", "js", "java", "csharp", "c"]

    linguagens = ["python", "js", "c", "java", "csharp"]
    linguagens.sort(key=lambda x: len(x)) # ["c", "js", "java", "python", "csharp"]

    linguagens = ["python", "js", "c", "java", "csharp"]
    linguagens.sort(key=lambda x: len(x), reverse=True) # ["python", "csharp", "java", "js", "c"]
***
### len
Tira o tamanho das coisas

    linguagens = ["python", "js", "c", "java", "csharp"]

    len(linguagens) # 5
***
