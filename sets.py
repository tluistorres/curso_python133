# São coleções de valores não ordenados para armazenar múltiplos ítens não duplicados dentro de um objeto. Não consegue modificar os ítens de um set, podemos adicionar elementos dentro de um set de qualquer tipo. Os elementos em um set não têm uma ordem específica.

# Operações com Sets:

# 1. Adicionar elemento: add(elemento);
# 2. Remover elemento: remove(elemento) ou discard(elemento);
# 3. Verificar se um elemento existe: in;
# 4. União de sets: union(set2) ou |;
# 5. Interseção de sets: intersection(set2) ou &;
# 6. Diferença de sets: difference(set2) ou -.

# Exemplo de uso de Sets:

# Criar um set:

meu_set = {1, 2, 3, 4, 5}

# Adicionar um elemento:

meu_set.add(6)
print(meu_set)          # {1, 2, 3, 4, 5, 6}

# Remover um elemento:

meu_set.remove(4)
print(meu_set)          # {1, 2, 3, 5, 6}

# Verificar se um elemento existe:

print(3 in meu_set)    # True

# União de sets:

outro_set = {4, 5, 6, 7, 8}
print(meu_set.union(outro_set))         # {1, 2, 3, 4, 5, 6, 7, 8}

# Interseção de sets:

print(meu_set.intersection(outro_set))  # {5, 6}

# Diferença de sets:

print(meu_set.difference(outro_set))    # {1, 2, 3}

planeta_anão = {'Plutão','Ceres','Eris','Makemak'} 
print(planeta_anão)
print(len(planeta_anão))
print('Ceres' in planeta_anão)
print('Lua' in planeta_anão)
print( 'Lua' not in planeta_anão)

# E a saída será:


# {1, 2, 3}
# {'Plutão', 'Ceres', 'Eris', 'Makemake'}
# 4
# True
# False
# True

# As operações realizadas:

# - difference(): retorna um conjunto com os elementos que estão no conjunto meu_set mas não no conjunto outro_set.
# - len(): retorna o número de elementos no conjunto planeta_anão.
# - in: verifica se um elemento está presente no conjunto planeta_anão.
# - not in: verifica se um elemento não está presente no conjunto planeta_anão.

# {'Ceres', 'Plutão', 'Makemak', 'Eris'} # A ordem é aleatória. Cada vez que rodar o código muda a ordem.

# Interação com conjunto - laço for.

for astro in planeta_anão:
   print(astro.upper())            # Letras maiúsculas.
    
for astro in planeta_anão:
   print(astro.upper(), end=' ')   # end para não mudar de linha.

# Podemos criar conjuntos através de uma lista( função interna chamada de set):

astros = ['Plutão','Ceres','Eris','Makemak']  # Criada uma lista.
print(astros, end= '')
astros_set = set(astros)  
print(astros_set)          # Em conjuntos cada vez que rodamos o código, altera a sequência dos elementos do conjunto(sequêcia aleatória).

# ['Plutão', 'Ceres', 'Eris', 'Makemake'] {'Plutão', 'Ceres', 'Eris', 'Makemake'}

# Comparação entre conjuntos:

astro1 = {'Plutão','Ceres','Eris','Makemak'}
astro2 = {'Plutão','Ceres','Eris','Makemak', 'Lua','Mercúrio'}
print(astro1 != astro2)
print(astro1 == astro2)
print(astro1 | astro2)               # União de conjuntos.
print(astro1.union(astro2)) 
print(astro1 & astro2)                # Intersecção de conjuntos.
print(astro1.intersection(astro2))
 
# E a saída será:


# True
# False
# {'Plutão', 'Ceres', 'Eris', 'Makemake', 'Lua', 'Mercúrio'}
# {'Plutão', 'Ceres', 'Eris', 'Makemake', 'Lua', 'Mercúrio'}
# {'Plutão', 'Ceres', 'Eris', 'Makemake'}
# {'Plutão', 'Ceres', 'Eris', 'Makemake'}


# As operações realizadas:

# - !=: verifica se os conjuntos são diferentes.
# - ==: verifica se os conjuntos são iguais.
# - |: retorna a união dos conjuntos.
# - union(): retorna a união dos conjuntos (método).
# - &: retorna a intersecção dos conjuntos.
# - intersection(): retorna a intersecção dos conjuntos (método).


# Diferença simétrica de conjuntos:

astro1 = {'Plutão', 'Ceres', 'Eris', 'Makemake', 'Urano', 'Marte', 'Sol', 'Terra'}
astro2 = {'Plutão', 'Ceres', 'Eris', 'Makemake', 'Lua', 'Mercúrio'}

print(astro1 ^ astro2)
print(astro1.symmetric_difference(astro2))


# E a saída será:


# {'Urano', 'Marte', 'Sol', 'Terra', 'Lua', 'Mercúrio'}
# {'Urano', 'Marte', 'Sol', 'Terra', 'Lua', 'Mercúrio'}


# O que aconteceu:

# - Usamos o operador ^ para calcular a diferença simétrica entre os conjuntos astro1 e astro2.
# - Usamos o método symmetric_difference() para calcular a diferença simétrica entre os conjuntos astro1 e astro2.
# - Ambos os métodos retornam um conjunto com os elementos que estão em apenas um dos conjuntos, mas não em ambos.

# Adicionar um elemento a um conjunto:

astro1.add('Urano')
astro1.add('Marte')
astro1.add('Sol')
astro1.add('Terra')
print(astro1)              # A ordem é aleatória, características dos conjuntos.

# E a saída será:

# {'Plutão', 'Ceres', 'Eris', 'Makemake', 'Urano', 'Marte', 'Sol', 'Terra'}

# Para remover um elemento do conjunto:

astro1.remove('Sol')
print(astro1)              # Como 'Saturno não está no conjunton dá erro.

astro1.discard('Urano')
astro1.pop()               # Elima um elemento aleatório do cojunto. ótimo para jogos.
astro1.clear()             # Limpa todo o conjunto.
