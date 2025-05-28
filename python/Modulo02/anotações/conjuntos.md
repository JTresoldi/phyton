***
# Conjuntos
### Objetivo geral
Entender o funcionamento da estrutura de dados **set**
***

## Criando sets
Um set é uma coleção que nao possui objetos repetidos, usamos sets para representar conjuntos matematicos ou **eliminar** itens duplicas de um iteravel.  
***obs**: Não confiar na ordem que ele te devolve,*

### Exemplo
    set([1, 2, 3, 1, 3, 4]) # {1, 2, 3, 4}

    set ("abacaxi) #{"b", "a", "c", "x", "i"}

    set(("Palio", "gol", "celta", "palio")) #{ "gol", "celta", "palio"}

### Acessando os dados
Conjuntos não suportam indexação e nem fatiamento, caso queira acessar os seus valores é necessario converter o conjunto para lista.

    numeros = {1, 2, 3, 2}

    numeros = list(numeros)

    numeros[0]

### Iterar conjuntos
A forma mais comum para percorrer os dados de um conjunto é utilizando o comando **for**

    carros = ("gol", "celta", "palio")

    for carro in carros:
        print(carro)

### Função enumerate
Quando necessario saber qual o indice do objeto dentro do laço **for**. Usamos a função **enumerate**.

    for indice, carro in enumerate(carros):
        print(f"{indice}: {carro}")
***

# Métodos da classe set
### {}.union 
Une as listas

    conjunto_a = {1, 2}
    conjunto_b = {3, 4}

    conjunto_a.union(conjunto_b) #{1, 2, 3, 4}

### {}.intersection
Mostra os iguais

    conjunto_a = {1, 2, 3}
    conjunto_b = {2, 3, 4}

        conjunto_a.union(conjunto_b) #{2, 3}

### {}.difference
Mostra os diferentes

    conjunto_a = {1, 2, 3}
    conjunto_b = {2, 3, 4}

    conjunto_a.difference(conjunto_b) #{1}
    conjunto_b.difference(conjunto_a) #{4}

### {}. symmetric_difference
Todos os elementos que nao estão na intersecção

    conjunto_a = {1, 2, 3}
    conjunto_b = {2, 3, 4}

    conjunto_a.symmetric_difference(conjunto_b) #{1, 4}

### {}.issubset
verifica se todos os elementos de um conjunto estão contidos em outro conjunto. Retorna True se for um subconjunto, False caso contrário.

    conjunto_a = {1, 2, 3}
    conjunto_b = {4, 1, 2, 5, 6, 3}

    conjunto_a.issubset(conjunto_b) # True
    conjunto_b.issubset(conjunto_a) # False

### {}.issuperset
verifica se um conjunto contém todos os elementos de outro conjunto. Retorna True se for um superconjunto (ou seja, se o primeiro conjunto for maior ou igual e contiver todos os elementos do segundo), False caso contrário.

    conjunto_a = {1, 2, 3}
    conjunto_b = {4, 1, 2, 5, 6, 3}

    conjunto_a.issubset(conjunto_b) # False
    conjunto_b.issubset(conjunto_a) # True

### {}.isdisjoint
verifica se dois conjuntos não têm nenhum elemento em comum. Retorna True se os conjuntos não compartilharem nenhum elemento (ou seja, a interseção deles é vazia), False caso contrário.

    conjunto_a = {1, 2, 3, 4, 5}
    conjunto_b = {6, 7, 8, 9}
    conjunto_c = {1, 0}

    conjunto_a.isdisjoint(conjunto_b) # True
    conjunto_a.isdisjoint(conjunto_c) # False

### {}.add
Adicionar um elemento.

    sorteio = {1, 23}

    sorteio.add(25) # {1, 23, 25}
    sorteio.add(42) # {1, 23, 25, 42}
    sorteio.add(25) # {1, 23, 25, 42}

### {}.clear
Limpar/Apagar o set

    sorteio = {1, 23}

    sorteio #{1, 23}
    sorteio.clear()
    sorteio #{}

### {}.copy
Copiar seu set

    sorteio = {1, 23}

    sorteio #{1, 23}
    sorteio.copy()
    sorteio #{1, 23}

### {}.discard
Discartar um valor

    numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

    numeros # {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}
    numeros.discard(1)
    numeros.discard(45)
    numeros # {2, 3, 4, 5, 6, 7, 8, 9, 0}

### {}.pop
 remove e retorna um elemento arbitrário (normalmente o último) de um conjunto. Se o conjunto estiver vazio, ele gera um erro KeyError.

     numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

    numeros # {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}
    numeros.pop() # 0
    numeros.pop() # 1
    numeros # {2, 3, 4, 5, 6, 7, 8, 9, 0} 

### {}.remove
remove um elemento específico de um conjunto. Se o elemento não estiver presente no conjunto, ele gera um erro KeyError.

    numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

    numeros # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
    numeros.remove(0) # 0
    numeros # {1, 2, 3, 4, 5, 6, 7, 8, 9}

### len
 retorna o número de itens (ou elementos) em um objeto. Pode ser usado com strings, listas, tuplas, dicionários, conjuntos, etc.

 ### in
 em Python é um operador de associação que verifica se um valor está presente em uma sequência ou coleção. Ele retorna True se o valor for encontrado, e False caso contrário.

