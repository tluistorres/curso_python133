# Parecem com as listas, a diferença fundamental é que são imutáveis, o conteúdo não pode ser modificado depois que foi criada. São sequências de constantes, sendo mais aplicadas que as listas por ter algumas interações, podendo ter diferentes tipos de valores: ponto flutuante, inteiros, strings, boleanos, dicionários, tuplas, listas e caracteres.


minha_tupla = (1,'Olá', 3.14, True, [123])
tupla = (2,4,6,7.9)
print(tupla)

# As tuplas em Python são estruturas de dados que podem armazenar valores de diferentes tipos, incluindo:

# - Inteiros (1, 2, 3, etc.)
# - Strings ('Olá', 'Hello', etc.)
# - Números flutuantes (3.14, -0.5, etc.)
# - Valores booleanos (True, False)
# - Listas ([1, 2, 3], ['a', 'b', 'c'], etc.)
# - Outros tipos de dados, como dicionários, conjuntos, etc.

# E é importante notar que, embora as tuplas possam armazenar valores de diferentes tipos, elas são imutáveis, ou seja, não podem ser modificadas após sua criação.

tupla = (2,4,6,7.9)
tupla[1] = 5
print(tupla) # Erro, não suporta colchetes, tem que ser entre chaves.

halogenios = ('F','Cl','Br','I','At')
print(halogenios) 
print(len(halogenios))
print(halogenios[3])
print(halogenios[-2])

halogenios = ('F','Cl','Br','I','At')
gases_nobres = ('He','Ne','Ar','Xe','Kp','Rn')
elementos = halogenios + gases_nobres
print(elementos)

t1 = (1,2,4,5,6,5,7,5,1,80,5)
print(t1.count(5))  # Quantas vezes aparece o 5.

# Fazendo um slice:

# As tuplas em Python também suportam operações de slice (fatia), que permitem extrair partes de uma tupla.

# A sintaxe para fazer slice em uma tupla é semelhante à lista:

# tupla[start:stop:step]

# Onde:

# - start: O índice inicial da fatia (inclusive).
# - stop: O índice final da fatia (exclusive).
# - step: O passo da fatia (opcional).

# Exemplos:

minha_tupla = (1, 2, 3, 4, 5)

print(minha_tupla[:2])    # Saída: (1, 2)     #Extrair os dois primeiros elementos.

print(minha_tupla[-2:])   # Saída: (4, 5)    # Extrair os dois últimos elementos.

print(minha_tupla[1:4])   # Saída: (2, 3, 4) # Extrair os elementos do índice 1 ao 3.

print(minha_tupla[::-1])  # Saída: (5, 4, 3, 2, 1) # Extrair todos os elementos, mas em ordem reversa.

halogenios = ('F','Cl','Br','I','At')

print(halogenios[0:2])    # ('F','Cl')
print(halogenios[ :3])    # ('F','Cl','Br')
print(halogenios[-2:0])   # (I','At')
print(halogenios[-3:0])

# Operador in.

print('Cl' in halogenios) # True.
print('Fe' in halogenios) # False , são os boleanos, boll.
print(sum(t1))            # Somatório.
print(min(t1))            # Tem que definir os elementos de t1.
print(max(t1))            # Até aqui similares as listas.

grupo17 = list(halogenios)# list. (Transforma a tupla em uma lista).
print(grupo17)

# Outra maneira:

halogenios = ('F','Cl','Br','I','At')
halogenios_lista = [*halogenios]
print(halogenios_lista)  # Saída: ['F', 'Cl', 'Br', 'I', 'At']

# O asterisco * é um operador de "unpacking" (ou "desempacotamento") em Python.

# Quando você usa *halogenios, você está dizendo ao Python para "desempacotar" os elementos da tupla halogenios e passá-los como argumentos separados para a lista. Em outras palavras, [*halogenios] é equivalente a:

halogenios_lista = [halogenios[0], halogenios[1], halogenios[2], halogenios[3], halogenios[4]]

# O operador *, você pode fazer isso de forma mais concisa e elegante.
# Esse operador é muito útil em muitas situações, como:

# - Desempacotar argumentos de uma função;
# - Criar listas ou tuplas a partir de outras sequências;
# - Mesclar listas ou tuplas.

#  Podemos cria uma tupla a partir de uma lista.

grupo17 = ['He','Ne','Ar','Xe','Kp','Rn']
alcalinos = tuple(grupo17)              # Comando tuple.
print(alcalinos)   

print(sorted(alcalinos))                # Põe em ordem alfabética ou crescente.
print(sorted(alcalinos, reverse=True))  # Caso queira ordenar a lista em ordem decrescente, pode-se usar o parâmetro reverse=True no comando sorted():

# Quando você faz print(alcalinos.sort()), você está tentando imprimir o resultado do método sort(), que é None. Isso não é o que você espera, pois você quer imprimir a lista ordenada.
# Para imprimir a lista ordenada, você deve chamar o método sort() separadamente e depois imprimir a lista:

# Para imprimir uma lista ordenada, é necessário chamar o método sort() separadamente antes de imprimir a lista. Aqui está um exemplo:


minha_lista = [5, 2, 8, 1, 9]
minha_lista.sort()
print(minha_lista)  # Saída: [1, 2, 5, 8, 9]


# Ou, se você quiser usar a função sorted(), pode fazer assim:

minha_lista = [5, 2, 8, 1, 9]
print(sorted(minha_lista))  # Saída: [1, 2, 5, 8, 9]

minha_tupla = (5, 2, 8, 1, 9)
tupla_ordenada = tuple(sorted(minha_tupla))
print(tupla_ordenada)  # Saída: (1, 2, 5, 8, 9)

# Nesse exemplo:

# 1. A função sorted() é usada para ordenar os elementos da tupla em ordem crescente.
# 2. O resultado da ordenação é uma lista.
# 3. A função tuple() é usada para converter a lista ordenada de volta para uma tupla.

# Operação não disponíveis em tuplas: 

# .sort(classificar as tuplas); 
# .append(não pode anexar nomes, itens mudam a tupla);
# .reverse(não reverte);
# .pop(remover o último elemento).
# Pois as tuplas são imutáveis.

# Podemos utilizar o laço.

for elemento in elementos:
    print(f'Emementos químicos:  {elemento}')

# Exemplo 1: Usando o laço for:

minha_tupla = (1, 2, 3, 4, 5)
for elemento in minha_tupla:
    print(elemento)

# Exemplo 2: Usando o laço while:

minha_tupla = (1, 2, 3, 4, 5)
i = 0
while i < len(minha_tupla):
    print(minha_tupla[i])
    i += 1

# Exemplo 3: Usando o laço for com enumerate:

minha_tupla = (1, 2, 3, 4, 5)
for i, elemento in enumerate(minha_tupla):
    print(f"Índice {i}: {elemento}")

# Podemos criar uma lista através de uma tupla.

# Existem várias maneiras de transformar uma tupla em uma lista em Python:

# 1. Usando a função list():

minha_tupla = (1, 2, 3, 4, 5)
minha_lista = list(minha_tupla)
print(minha_lista)                # Saída: [1, 2, 3, 4, 5]

# 2. Usando o método [*tupla]:

minha_tupla = (1, 2, 3, 4, 5)
minha_lista = [*minha_tupla]
print(minha_lista)                # Saída: [1, 2, 3, 4, 5]


# 3. Usando um laço for:

minha_tupla = (1, 2, 3, 4, 5)
minha_lista = []
for elemento in minha_tupla:
    minha_lista.append(elemento)
print(minha_lista)                # Saída: [1, 2, 3, 4, 5]



# ('He', 'Ne', 'Ar', 'Xe', 'Kp', 'Rn')
# O comando tuple() cria uma nova tupla a partir dos elementos da lista, mantendo a mesma ordem.
# Além disso, você também pode usar o comando tuple() para transformar outras sequências, como strings ou conjuntos, em tuplas.

# Exemplos:

string = "hello"
tupla_string = tuple(string)
print(tupla_string)                # Saída: ('h', 'e', 'l', 'l', 'o')

conjunto = {1, 2, 3, 4, 5}
tupla_conjunto = tuple(conjunto)
print(tupla_conjunto)  # Saída: (1, 2, 3, 4, 5)

print(type(alcalinos))  # <class 'tuple'>

# Não podemos ordenar os elementos de uma tupla.


