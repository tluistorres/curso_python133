# São sequência mais comum que tuplas, dicionários, strings e setes.
# Representam uma sequência de valores.
# Sintaxe: nome_lista = [valors].

# notas = [5,7,8,10]
# print(notas)
# n1 = [5,7,8,10]
# n2 = [6,6,10,8]
# valores = n1 + n2
# print(valores)         # Podemos concatenar listas.
# print(type(valores))   # Tipo do objeto. <class 'list'>
# print(valores[4])      # 6
# print(valores[-1])
# print(valores[-2]))

n1 = [5,7,8,10]
n2 = [6,6,10,8]

valores = n1 + n2
valores[2] = 10
print(valores)
# Posição slice - serve para acesar valores de uma lista.

print(valores[0:4])   # [5,7,10,10]
print(valores[0: ])   # Exibe todos os valores.
print(valores[ :4])   # [5,7,10,10]
print(valores[-2: ])  # [10,8], os dois últimos da lista.
print(len(valores))   # Quantidade de valores.
print(sorted(valores))# Ordenas os valores da lista sem modificar.
print(sorted(valores,reverse=True)) # Inverte em ordem decrescente.
print(sum(valores)) # Somatório de listas.
print(min(valores))
print(max(valores))

# Acrescenta valores a lista - append.
valores.append(20)   # Primeiro manda acrescentar valor a lista.
print(valores)
valores.pop()        # Remove o último elemento.
print(valores)
valores.pop(3)       # Remove o elemento 3 da lista.
print(valores)
valores.insert(5,80) # Na posição 5, insere o elemento 21.
print(valores)

print(12 in valores) # False
print(80 in valores) # True
print("a" in valores)# False

# Pode criar uma lista de strigs.

# planetas = ['Mercúrio','Vênus','Marte','Saturno']
# print(planetas)
# for planeta in planetas:
#     print(planeta)          # "docs.python.org"

# Lista de bebidas.

bebidas = []
for i in range(5):
    print(f'Digite uma bebida favorita: ')
    bebida = input()
    bebidas.append(bebida)

print(f'\nBebidas escolhidas: ')
for bebida in bebidas:
    print(bebida)

bebidas.sort()  # Classifica e ordena automaticamente em orfem alfabética.

print(f'\nSaúde!')

