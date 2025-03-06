# Parecem com as listas, a diferença fundamental é que são imutáveis, o conteúdo não pode sermodificado depois que foi criada. São sequências de constantes, sendo mais aplicadas que as listas por ter algumas interações, podendo ter diferentes tipos de valores: ponto flutuante, inteiros, strings, boleanos, dicionários, tuplas, listas e caracteres.
# minha_tupla = (1,'Olá,3.14,True,[123]).

# tupla = (2,4,6,7.9)
# print(tupla)

# tupla = (2,4,6,7.9)
# tupla[1] = 5
# print(tupla) # Erro, não suporta colchetes, tem que ser entre chaves.

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

# Fazendo um slice.

halogenios = ('F','Cl','Br','I','At')

print(halogenios[0:2])    # ('F','Cl')
print(halogenios[ :3])    # ('F','Cl','Br')
print(halogenios[-2:0])   # (I','At')
print(halogenios[-3:0])

# Operador in.

print('Cl' in halogenios) # True
print('Fe' in halogenios) # Fase , são os boleanos, boll.
print(sum(t1))            # Somatório.
print(min(t1))
print(max(t1))            # Ate aqui similares as listas.

# Operação não disponíveis em tuplas: 
# .sort(classificar as tuplas); 
# .append(não poe anexar nomes, itens mudam a tupla);
# .reverse(não reverte);
# .pop(remover o último elemento).
# Pois as tuplas são imutáveis.

# Podemos utilizar o laço.

for elemento in elementos:
    print(f'Emementos químicos:  {elemento}')

# Podemos criar uma lista através de uma tupla.

grupo17 = list(halogenios)   # list. ( Transforma a tupla em uma lista).
print(grupo17)

# Outra maneira.

halogenios = ('F','Cl','Br','I','At')
halogenios_lista = [*halogenios]
print(halogenios_lista)  # Saída: ['F', 'Cl', 'Br', 'I', 'At']

# O asterisco * é um operador de "unpacking" (ou "desempacotamento") em Python.

#Quando você usa *halogenios, você está dizendo ao Python para     "desempacotar" os elementos da tupla halogenios e passá-los como argumentos separados para a lista. Em outras palavras, [*halogenios] é equivalente a:
# halogenios_lista = [halogenios[0], halogenios[1], halogenios[2], halogenios[3], halogenios[4]]. 
# O operador *, você pode fazer isso de forma mais concisa e elegante.
# Esse operador é muito útil em muitas situações, como:

# - Desempacotar argumentos de uma função;
# - Criar listas ou tuplas a partir de outras sequências;
# - Mesclar listas ou tuplas.

#  Podemos cria uma tupla a partir de uma lista.

grupo17 = ['He','Ne','Ar','Xe','Kp','Rn']
alcalinos = tuple(grupo17)   # Comando tuple.
print(alcalinos)   

# ('He', 'Ne', 'Ar', 'Xe', 'Kp', 'Rn')
# O comando tuple() cria uma nova tupla a partir dos elementos da lista, mantendo a mesma ordem.
# Além disso, você também pode usar o comando tuple() para transformar outras sequências, como strings ou conjuntos, em tuplas.

# Exemplos:

# string = "hello"
# tupla_string = tuple(string)
# print(tupla_string)  # Saída: ('h', 'e', 'l', 'l', 'o')

# conjunto = {1, 2, 3, 4, 5}
# tupla_conjunto = tuple(conjunto)
# print(tupla_conjunto)  # Saída: (1, 2, 3, 4, 5)

print(type(alcalinos))  # <class 'tuple'>

# Não podemos ordenar os elementos de uma tupla.

print(sorted(alcalinos))  # Põe em ordem alfabética ou crescente.
print(sorted(alcalinos, reverse=True))  # Caso queira ordenar a lista em ordem decrescente, pode-se usar o parâmetro reverse=True no comando sorted():


# Quando você faz print(alcalinos.sort()), você está tentando imprimir o resultado do método sort(), que é None. Isso não é o que você espera, pois você quer imprimir a lista ordenada.
# Para imprimir a lista ordenada, você deve chamar o método sort() separadamente e depois imprimir a lista:
