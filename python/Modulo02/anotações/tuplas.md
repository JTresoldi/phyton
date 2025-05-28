***
# Tuplas
Tuplas são estruturas de dados muito parecidas com listas, a diferença é que tuplas são imutáveis enquanto listas sao mutáveis.   
Podemos criar tuplas atraves da classe **tuple**, ou colocando valores separados por virugla de parenteses.

## Exemplo
    frutas = ("laranja", "pera", "uva",)

    letras = tuple("python")

    numeros = tuple([1, 2, 3, 4])

    pais = ("Brasil",)

## Acesso direto
A tupla é uma sequencia, podemos acessar seus dados utilizando indices.  
Contamos o indice de determinada sequencia a partir do zero.

    frutas = ("laranja", "pera", "uva",)
    frutas[0] # laranja
    frutas[2] # uva

## Tuplas aninhadas
Podem armazenar todos os tipos de objetos, podemos ter tuplas que armazenam outras tuplas.
***

# Métodos da classe tuple
A baixo os metodos possiveis na tuple:  
* ( ).count
* ( ).index
* ( ).len

