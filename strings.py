# Manipilação de strigs de caracteres de dados de textos que são sequências como as listas, tuplas,etc. São imutáveis, não podendo alterar, mas pode alterar o conteúdo da variável que contém a string.

nome = 'luis'
letra = nome[2]
print(letra)
print(len(letra))
print(len(nome))

# Pode ser concatenado:

nome = 'Estou aprendendo Python agora'
instrutor = 'luis'
print(nome + ' com ' + ' o ' + instrutor )

frase = ' Vamos aprender Python hoje! '
palavras = frase.split()
print(frase)                # Listas de strings: ['Vamos', 'aprender', 'Python', 'hoje!']

print(palavras[1])          # Ou utizar o laço for

for palavra in palavras:
    print(palavra)

for letra in frase:
    print(letra)  

# V
# a
# m
# o
# s
 
# a
# p
# r
# e
# n
# d
# e
# r
 
# P
# y
# t
# h
# o
# n
 
# h
# o
# j
# e
# !

# Fatiamento em listas ou tuplas

frase = 'Vamos aprender Python hoje!'
print(frase[2:6])               # Resultado -- mos
print(frase[7:19])              # Resultado --  prender Pyth
print(frase[-3:])               # Resultado -- je!

# Slice - utilizado para separar strings:

email = input('Digite seu endereço de email: ')
arroba = email.find('@')
print(arroba)
usuario = email[0:arroba]
dominio = email[arroba+1:]
print(usuario)
print(dominio)

# Digite seu endereço de email: exemplo@email.com
# 5
# exemplo
# email.com


# O que o código faz:

# 1. Pede ao usuário para digitar seu endereço de email.
# 2. Usa o método find() para encontrar a posição da arroba (@) no email.
# 3. Imprime a posição da arroba.
# 4. Usa fatiamento de strings (email[0:arroba]) para extrair o nome do usuário (tudo antes da arroba).
# 5. Usa fatiamento de strings (email[arroba+1:]) para extrair o domínio do email (tudo depois da arroba).
# 6. Imprime o nome do usuário e o domínio.

# Verificação se um caractere está dentro de uma string

produtos = 'carbonato de sódio e ódxido de zinco'
print('sódio' in produtos )        # True
print('magnésio' in produtos )     # False
print('magnésio' not in produtos ) # True

# Encontrar a sequência após uma sub-string ( clor ) e dá a posição

item = 'hipoclorito'
pos = item.find('clor')            # True
print(pos)                         # 4
pos = item.find('flu')             #-1 ( não tem ).
print(pos)

# Comando upper, lower, capitalize, titlo, replace.

objeto_celeste = 'galáxia espiral M31'
print(objeto_celeste.upper())      # Letras maiúsculas.
print(objeto_celeste.lower())      # Letras minúsculas.
print(objeto_celeste.capitalize()) # Somente a primeita letra do texto maiúscula.
print(objeto_celeste.title())      # As primeiras letras da palavra maiúscula.

# Substituindo a variável:  Comando replace.

suplemento = 'cloreto de magnésio'
n_suplemento = suplemento.replace('magnésio','zinco')
print(suplemento)                  # Substitui magnésio por zinco, criando nova variável
print(n_suplemento)

# Trabalhando com espaços em branco:

frase =  '       ômega3 é bom para a saúde      '  
print(frase)
print(frase.lstrip())              # Espaço em branco  à esquerda
print(frase.rstrip())              # Espaço em branco  à direita
print(frase.strip())               # Elimina espaços tanto à direita quanto ´esquerda

# E a saída será:

#  ômega3 é bom para a saúde 
# ômega3 é bom para a saúde 
#  ômega3 é bom para a saúde
# ômega3 é bom para a saúde


fruta = 'Abacate'

print(fruta.ljust(20, "-")) 
print(fruta.center(20, "-")) 
print(fruta.rjust(20)) 
print(fruta.center(20)) 
print(fruta.ljust(20))

# Alinhamento de texto para exibição:

# Um exemplo prático de formatação de strings!

# Aqui estão os métodos utilizados:

# - ljust(): alinha a string à esquerda e preenche com um caractere específico (nesse caso, -) até atingir a largura desejada.
# - center(): centraliza a string e preenche com um caractere específico (nesse caso, -) até atingir a largura desejada.
# - rjust(): alinha a string à direita e preenche com espaços até atingir a largura desejada.

# E aqui estão as saídas:


# Abacate-------------
# ------Abacate-------
#                   Abacate
#           Abacate          
# Abacate             

# Esses métodos são muito úteis para criar layouts e formatações personalizadas em strings, especialmente em títulos de tabelas, menus e outros elementos de interface de usuário.

# # Pré-fixos e sufixos

p = 'Boson Treinamentos'
print(p.startswith('B'))     # True
print(p.startswith('b'))     # False
print(p.endswith('s'))       # True
print(p.endswith('o'))       # False

# Docstrings - Servem documentos, trechos específicosdo código: módulos,classes, funções,tec.

texto = """
Docstring é uma espécie de documentação que podemos inserir dentro de um módulo, função ou classe no Python, entre outros locais.
        Respeita deslocamentos do texto e é multlinhas.

"""
print(texto)  # Não pode usar Docstring para comentários.
