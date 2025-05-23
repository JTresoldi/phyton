***
# Strings e Fatiamento
### Maiúscula, minúscula e título
    curso = "pYtHon"

    print(curso.upper())
    >>> PYTHON

    print(curso.lower())
    >>> python

    print(curso.tittle())
    >>> Python
***
### Eliminando espaçõs em branco
    curso = "   Python "

    print(curso.strip())
    >>> "Python"

    print(curso.lstrip())
    >>> "Python "

    print(curso.rstrip())
    >>> "   Python"
***
### Junções e centralização
    curso = "Python"

    print(curso.center(10, "#"))
    >>> "##Python##"

No primeiro argumento vc coloca quantos caracteres quer.
No segundo argumento (opcional) é o caracter que vc quer colocar, caso esteja em branco sera preenchido por espaço.

    print(".".join(curso))
    >>> "P.y.t.h.o.n"

Ele passa item por item, e coloca o caracter que vc escolheu.
***

# Interpolação de variáveis

### Old Style '%'
    nome = "João"
    idade = 26
    profissao = "Programador"
    linguagem = "Python"

    print("Olá, me chamo %s. Eu tenho %d anos de idade, trabalho como %s e estou matriculado no curso de %s." % (nome, idade, profssao, linguagem)) 

    >>> Olá, me chamo João. Eu tenho 26 anos de idade, trabalho como Programador e estou matriculado no curso de Python.

### Método format
    nome = "João"
    idade = 26
    profissao = "Programador"
    linguagem = "Python"

    print("Olá, me chamo {}. Eu tenho {} anos de idade, trabalho como {} e estou matriculado no curso de {}." .format (nome, idade, profssao, linguagem)) 

    print("Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}." .format (nome=nome, idade=idade, profssao=profissao, linguagem=linguagem))
    
    print("Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}." .format(**pessoa))

### Fomatar com f-string
    PI = 3.14159

    print(f"Valor de PI: {PI:.2f}")
    >>> "Valor de PI: 3.14"

    print(f"Valor de PI: {PI:10.2f}")
    >>> "Valor de PI:           3.14"

***
# Fatiamento
Fatiamento de string é uma tecnica utilizada para retornar substrings (partes da string original), informando inicio (start), fim (stop) e passo (step): [star:stop[, step]]

    print(nome[0])
    >>> "J"
    print(nome[:5])
    >>> "Joao"
    print(nome[5:])
    >>> "Pedro Tresoldi
    print(nome[5:10:14])
    >>>  "P"
    print(nome[:])
    >>> "Joao Pedro Tresoldi
    print(nome[::-1])
    >>> idloserT ordeP oaoJ
***

# Strings de Multiplas Linhas
São definidas informando 3 aspas simples ou duplas durante a atribuição. Elas podem ocupar varias linhas do codigo, e todos os espaços em brancopo são incluidos na string final.

    nome = "Joao"

    mensagem = f"""
    Ola meu nome e {nome}
    Eu estou aprendendo Python
    """

    >>>
    Ola meu nome e Joao
    Eu estou aprendendo Python

    mensagem = f'''
        Ola meu nome e {nome},
      Eu estou aprendendo Python.
           Essa mensagem tem diferentes recuos.
    '''
    >>> Ola meu nome e {nome},
      Eu estou aprendendo Python.
           Essa mensagem tem diferentes recuos.