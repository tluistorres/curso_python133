# Dicionários permitem armazenar em pares: chave: valor.
# São similares a arrays em outras linguagens, não permitem itens duplicados, mas podem ser de qualquer tipo.
# Os dicionários permitem acesso rápido aos valores associados às chaves.
# Os dicionários são mutáveis, o que significa que você pode adicionar, remover ou modificar pares de chave-valor.

# Vamos criar um dicionário para armazenar um elemento químico.

elemento = {                    # As chaves são imutáveis.
    'Z': 3,
    'nome': 'Lítio',
    'grupo': 'Metais Alcalinos',
    'densidade': 0.534
}

print(f'Elemento: {elemento['nome']}')
print(f'Densidade: {elemento["densidade"]}')
print(f'O dicionário possui {len(elemento)} elementos')

# Atualizar uma entrada.

elemento['grupo'] = 'Alcalinos' # Trocar 'Metais Alcalinos' por 'Alcalinos'.
print(elemento)

# Adicionar uma entrada.

elemento['período'] = 1
print(elemento)

# Exclusão de ítens em dicionários.

del elemento['período']
print(elemento)

# # Apagar todo o conteúdo do dicionário.

# elemento.clear()
# print(elemento)

# # Apagar totalmente o dicionário.

# del elemento
# print(elemento)

# Retorna os ítens apagados do dicionários.

print(elemento.items())  # Os items é uma lista de tuplas: dict_items([('Z', 3), ('nome', 'Lítio'), ('grupo', 'Alcalinos'), ('densidade', 0.534)])

# Laço for: mostra as tuplas separadas, ficando mais fácil de acessar as informações.

for i in elemento.items():
    print(i)

# ('Z', 3)
('nome', 'Lítio')
('grupo', 'Alcalinos')
('densidade', 0.534)

# Método keys ´mostra somente as chaves.

print(elemento.keys())
for i in elemento.keys():
    print(i)

# Z
# nome
# grupo
# densidade

# Pode tabém mudar para valores.

print(elemento.values())
for i in elemento.values():
    print(i)

# dict_values([3, 'Lítio', 'Alcalinos', 0.534])
# 3
# Lítio
# Alcalinos
# 0.534

# Desempacotar as chaves e valores.

for i, j in elemento.items():
    print(f'{i}: {j}')

# nome: Lítio
# grupo: Alcalinos
# densidade: 0.534