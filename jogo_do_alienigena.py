# jogo alienígena_1

# import random

# vida_jogador = 100
# árvore = random.randint(1, 100)

# print("Um alienígena está escondido atrás de uma árvore")
# print("Cada árvore foi numerada de 1 a 100.")
# print("Você precisa encontrar o alienígena antes que sua vida acabe.")

# while vida_jogador > 0:
#     print(f"\nVida: {vida_jogador}")
#     palpite = int(input("Árvore: "))

#     if palpite == árvore:
#         print("Você acertou! Você encontrou o alienígena.")
#         break
#     elif palpite > árvore:
#         print("Muito alto")
#     else:
#         print("Muito baixo")

#     # Diminui a vida do jogador por um valor aleatório entre 5 e 20:

#     vida_perdida = random.randint(5, 20)
#     vida_jogador -= vida_perdida
#     print(f"O alienígena atacou! Você perdeu {vida_perdida} pontos de vida.")

# else:
#     print("Você não conseguiu encontrar o alienígena. Sua vida acabou.")
#     print(f"O alienígena estava na árvore {árvore}")

##########################################################################

# Jogoa alienígena_2

import random

print("*********************************")
print("* Bem-vindo ao Jogo do Alienígena_2! *")
print("*********************************")

print("Escolha o nível de dificuldade:")
print("1 - Fácil")
print("2 - Médio")
print("3 - Difícil")

dificuldade = int(input("Digite o número do nível de dificuldade: "))

if dificuldade == 1:
    vida_jogador = 100
    dano_minimo = 5
    dano_maximo = 20
    print("Você escolheu o nível fácil. Boa sorte!")
elif dificuldade == 2:
    vida_jogador = 80
    dano_minimo = 10
    dano_maximo = 25
    print("Você escolheu o nível médio. Prepare-se para o desafio!")
elif dificuldade == 3:
    vida_jogador = 75
    dano_minimo = 20
    dano_maximo = 30
    print("Você escolheu o nível difícil. Você é um verdadeiro guerreiro!")
else:
    print("Nível de dificuldade inválido. Jogo encerrado.")
    exit()

árvore = random.randint(1, 100)

print("\nUm alienígena está escondido atrás de uma árvore")
print("Cada árvore foi numerada de 1 a 100.")
print("Você precisa encontrar o alienígena antes que sua vida acabe.")

while vida_jogador > 0:
    print(f"\nVida: {vida_jogador}")
    palpite = int(input("Árvore: "))

    if palpite == árvore:
        print("Você acertou! Você encontrou o alienígena.")
        break
    elif palpite > árvore:
        print("Muito alto")
    else:
        print("Muito baixo")

    # Diminui a vida do jogador por um valor aleatório entre dano_minimo e dano_maximo:

    dano = random.randint(dano_minimo, dano_maximo)
    vida_jogador -= dano
    print(f"O alienígena atacou! Você perdeu {dano} pontos de vida.")

else:
    print("Você não conseguiu encontrar o alienígena. Sua vida acabou.")
    print(f"O alienígena estava na árvore {árvore}")