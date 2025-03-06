# Manipilação de strigs de caracteres de dados de textos que são sequências como as listas, tiplas,etc. São imutáveis, não podendo alterar, mas pode alterar o conteúdo da variável que contém a string.

# nome = 'luis'
# letra = nome[2]
# print(letra)
# print(len(letra))
# print(len(nome))

# Pode ser concatenado

#nome = 'Estou aprendendo Python agora'
# instrutor = 'luis'
# print(nome + ' com ' + ' o ' + instrutor )

# frase = ' Vamos aprender Python hoje! '
# palavras = frase.split()
# print(frase) # Listas de strings


# print(palavras[1]) # Ou utizar o laço for

# for palavra in palavras:
#     print(palavra)

# for letra in frase:
#     print(letra)
# Fatiamento em listas ou tuplas

# frase = 'Vamos aprender Python hoje!'
# print(frase[2:6]) # Resultado -- mos
# print(frase[7:19]) # Resultado --  prender Pyth
# print(frase[-3:]) # Resultado -- je!

# Slice - utilizado para separar strings

# email = input('Digite seu endereço de email: ')
# arroba = email.find('@')
# print(arroba)
# usuario = email[0:arroba]
# dominio = email[arroba+1:]
# print(usuario)
# print(dominio)

# Verificação se um caractere está dentro de uma string

produtos = 'carbonato de sódio e ódxido de zinco'
print('sódio' in produtos ) # True
print('magnésio' in produtos ) # False
print('magnésio' not in produtos ) # True

# Encontrar a sequência após uma sub-string ( clor ) e dá a posição

item = 'hipoclorito'
pos = item.find('clor') # True
print(pos)              # 4
pos = item.find('flu')  # -1 ( não tem )
print(pos)

# Comando upper, lower, capitalize, titlo, replace.

objeto_celeste = 'galáxia espiral M31'
print(objeto_celeste.upper())     # Letras maiúsculas
print(objeto_celeste.lower())     # Letras minúsculas
print(objeto_celeste.capitalize())# Somente a primeita letra do texto maiúscula
print(objeto_celeste.title())     # As primeiras letras da palavra maiúscula

#Substituindo a variável# Comando replace

suplemento = 'cloreto de magnésio'
n_suplemento = suplemento.replace('magnésio','zinco')
print(suplemento) # Substitui magnésio por zinco, criando nova variável
print(n_suplemento)

# Trabalhando com espaços em branco

frase =  '       ômega3 é bom para a saúde      '  
print(frase)
print(frase.lstrip()) # Espaço em branco  à esquerda
print(frase.rstrip()) # Espaço em branco  à direita
print(frase.strip())  # Elimina espaços tanto à direita quanto ´esquerda

# Alinhamento de texto para exibição

fruta = 'Abacate'
print(fruta.ljust(20, "-"))  # Abacate-------------
print(fruta.center(20, "-")) # ------Abacate------- , Muito utilizado em títulos de Tabelas
print(fruta.rjust(20))      # 20 espaços no total e ajusta à direita (Menus)
print(fruta.center(20))     # 20 espaços e centraliza
print(fruta.ljust(20))      # Padrão ( Alina à esquerda )

# Pré-fixos e sufixos
p = 'Boson Treinamentos'
print(p.startswith('B')) # True
print(p.startswith('b')) # False
print(p.endswith('s'))   # True
print(p.endswith('o'))   # False

# Docstrings - Servem documentos, trechos específicosdo código: módulos,classes, funções,tec.

texto = """
Docstring é uma espécie de documentação que podemos inserir dentro de um módulo, função ou classe no Python, entre outros locais.
        Respeita deslocamentos do texto e é multlinhas.

"""
print(texto)  # Não pode usar Docstring para comnetários.
