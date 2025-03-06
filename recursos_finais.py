# Algoritmo para trocar valores entre duas variáveis.

var1 = 12
var2 = 31

# aux = var1
# var1 = var2
# var2 = aux

# Em Python não precisa fazer isso.

# var2, var1 = var1, var2

# print(f' var1: {var1}, var2: {var2}')

# Operador Condicional Ternário. Verificar quais dos ddois é menores.

# var1 = 12
# var2 = 31

# menor = var1 if var1 < var2 else var2 
# print(f'Menor valor: {menor}')

# Podemos fazendo uma tupla.

# var1 = 60
# var2 = 31

# menor = var1 if var1 < var2 else var2 
# print(f'Menor valor: {menor}')
# print(f'Menor valor: {(var2,  var1)[var1 < var2]}')

# Generators - serão gerados um a um, ocrrendo uma economia de dados.

# valores = [1,3,4,5,6,78,9]
# quadrados = (item**2 for item in valores)
# print(quadrados)
# for valor in quadrados:
#     print(valor)

# <generator object <genexpr> at 0x0000025BA664A5A0>
# 1
# 9
# 16
# 25
# 36
# 6084
# 81

# Função enumerate().
# É uma função de interação. Uma sequência qualquer de listas, tuplas, dicionários, retornando os elementos e seus números de índices simultaneamente no formato de tuplas (índece,item), de forma separada ou em conjunto.

# bebidas = ['Café', 'Chá','Água','Suco', 'Refrigerante']
# for i, item in enumerate(bebidas):  # Pode ser uma tupla, um dicionário. No caso é uma Lista.
#     print(f'Índice: {i + 1}, Item: {item}') # Caso queira que o índece comece com e não zero.

# Índice: 0, Item: Café
# Índice: 1, Item: Chá
# Índice: 2, Item: Água
# Índice: 3, Item: Suco
# Índice: 4, Item: Refrigerante

# Índice: 1, Item: Café
# Índice: 2, Item: Chá
# Índice: 3, Item: Água
# Índice: 4, Item: Suco
# Índice: 5, Item: Refrigerante

# temperaturas = [-1,10,5,-3,8,4,-2,-5,7]
# total = 0

# for i, t in enumerate(temperaturas):
#     if t < 0:
#         print(f'A temperatura em {i} é negativa, com {t}ºC.')

# Gerenciamento de contexto com with. Serve para encapsular e tornar código menor para executar uma função, código mais limpo.

# try:
#     a = open('furtas.dat', 'r', encoding='utf-8')
#     print(a.read())
# except IOError:
#     print(f'Não foi possível abrir o arquivo')  # Abrir um arquivo e visualizar o conteúdo.
# else:
#     a.close()

try:
    with open('furtas.dat', 'r', encoding='utf-8') as a:
        print(a.read())
except FileNotFoundError:
    print(f"O arquivo 'furtas.dat' não foi encontrado.")
except OSError as e:
    print(f"Ocorreu um erro ao abrir o arquivo: {e}")