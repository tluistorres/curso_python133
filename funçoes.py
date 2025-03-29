# Funções:

def épar(x):
   return x % 2 == 0
print(épar(2))
print(épar(3))
print(épar(10)) 

def épar(x):
   return x % 2 == 0
def par_ou_ímpar(x):
   if épar(x):
      return "par"
   else:
      return "ímpar"
print(par_ou_ímpar(4))
print(par_ou_ímpar(5))

# Pesquisa em uma lista:

def pesquise(lista, valor):
   for x, e in enumerate(lista):
      if e == valor:
         return x
   return None
L = [10,20,25,30]
print(pesquise(L,25))
print(pesquise(L,27))

# Calculando a média dos valores de uma lista:

def soma(L):
   total = 0
   for e in L:
      total += e
   return total
def média(L):
   return soma(L / len(L))

# Poderia também ser assim:

def média(L):
   total = 0
   for e in L:
      total += e
   return total(L / len(L))

# Cálculo do fatorial:

def fatorial(n):
   fat = 1
   x = 1
   while x <= n:
      fat *= x
      x += 1
   return fat
print(4)


#######################################################################

# Variáveis locais e globais:

# Quando usamos funções, começamos a trabalhar com variáveis internas ou locais e com variáveis externas ou globais. 

# Variáveis Locais:

# - São declaradas dentro de uma função ou bloco de código.
# - Sua visibilidade e acessibilidade são limitadas ao escopo da função ou bloco.
# - São criadas e destruídas automaticamente quando a função ou bloco é executado.

# Variáveis Globais:

# - São declaradas fora de qualquer função ou bloco de código.
# - Sua visibilidade e acessibilidade são globais, ou seja, podem ser acessadas de qualquer parte do programa.
# - Persistem durante toda a execução do programa.

# Exemplos:

# - Variável local: 


# Variável Local:

def soma(a, b):
  resultado = a + b
  return resultado
print(soma(2, 3))  # Saída: 5
print(resultado)  # Erro: nome 'resultado' não definido


# Variável Global:

nome = 'João'
def imprime_nome():
  global nome
  print(nome)
imprime_nome()  # Saída: João
print(nome)  # Saída: João

# Boas Práticas
# - Use variáveis locais sempre que possível para evitar poluição do escopo global.
# - Use variáveis globais apenas quando necessário, como para configurar constantes ou compartilhar dados entre funções.

#######################################################################

# Funções recursivas:

# Funções recursivas são funções que se chamam a si mesmas durante sua execução. Elas são úteis para resolver problemas que podem ser divididos em subproblemas menores e semelhantes.

# Características de funções recursivas:

# 1. Chamada a si mesma: A função se chama a si mesma durante sua execução.
# 2. Condição de parada: A função deve ter uma condição de parada para evitar uma recursão infinita.
# 3. Subproblemas: A função divide o problema em subproblemas menores e semelhantes.

# Exemplo de função recursiva:

# Fatorial:

# O fatorial de um número é o produto de todos os números inteiros positivos menores ou iguais a ele.

# Fatorial

def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n - 1)


# Fibonacci

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


# Contagem Regressiva:

def contagem_regressiva(n):
    if n == 0:
        print("Fim!")
    else:
        print(n)
        contagem_regressiva(n - 1)


# Soma de Elementos de Lista:

def soma_lista(lista):
    if len(lista) == 1:
        return lista[0]
    else:
        return lista[0] + soma_lista(lista[1:])



# Chamada da função:

# console.log(fatorial(5)); // Saída: 120


# Vantagens e desvantagens de funções recursivas:

# Vantagens:

# - Solução elegante: Funções recursivas podem fornecer uma solução elegante e concisa para problemas complexos.
# - Divide e conquista: Funções recursivas dividem o problema em subproblemas menores e semelhantes, facilitando a resolução.

# Desvantagens:

# - Ineficiência: Funções recursivas podem ser ineficientes em termos de memória e tempo de execução, pois criam múltiplas instâncias da função.
# - Risco de estouro de pilha: Funções recursivas podem causar um estouro de pilha se a condição de parada não for alcançada.

# Quando usar funções recursivas:

# - Problemas de divisão e conquista: Funções recursivas são ideais para problemas que podem ser divididos em subproblemas menores e semelhantes.

# - Problemas com estrutura de árvore: Funções recursivas são úteis para problemas que envolvem estruturas de árvore, como árvores binárias.

# Lembre-se de que funções recursivas devem ser usadas com cautela e apenas quando necessário, pois podem ser ineficientes e causar problemas de estouro de pilha.

#######################################################################

# Validação:

# A validação é um processo importante em programação para garantir que os dados ou entradas sejam válidos e consistentes com as expectativas do programa.

# Tipos de Validação:

# 1. Validação de entrada: Verificar se os dados de entrada estão corretos e no formato esperado.
# 2. Validação de dados: Verificar se os dados armazenados ou processados estão corretos e consistentes.
# 3. Validação de formato: Verificar se os dados estão no formato esperado (por exemplo, data, hora, endereço, etc.).

# Técnicas de Validação:

# 1. Verificação de tipo: Verificar se o tipo de dado é compatível com o esperado.
# 2. Verificação de intervalo: Verificar se o valor está dentro de um intervalo válido.
# 3. Verificação de formato: Verificar se o formato do dado é compatível com o esperado.
# 4. Verificação de consistência: Verificar se os dados são consistentes entre si.

# Exemplos de Validação:

# 1. Validar um e-mail: Verificar se o e-mail está no formato correto (por exemplo, nome@dominio.com).
# 2. Validar uma data: Verificar se a data está no formato correto (por exemplo, DD/MM/AAAA) e se é uma data válida.
# 3. Validar um número de telefone: Verificar se o número de telefone está no formato correto (por exemplo, (XX) XXXX-XXXX) e se é um número válido.

# Linguagens de Programação e Validação:

# 1. Python: Utiliza bibliotecas como re para validação de formato e isinstance() para verificação de tipo.

# Validação de E-mail:

import re

def validar_email(email):
    padrão = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    if re.match(padrão, email):
        return True
    else:
        return False

email = "exemplo@gmail.com"
if validar_email(email):
    print("E-mail válido")
else:
    print("E-mail inválido")


# Validação de Data:

import datetime

def validar_data(data):
    try:
        datetime.datetime.strptime(data, "%d/%m/%Y")
        return True
    except ValueError:
        return False

data = "25/02/2022"
if validar_data(data):
    print("Data válida")
else:
    print("Data inválida")


# Validação de Número de Telefone:

import re

def validar_telefone(telefone):
    padrão = r"^\([0-9]{2}\) [0-9]{4}-[0-9]{4}$"
    if re.match(padrão, telefone):
        return True
    else:
        return False

telefone = "(11) 1234-5678"
if validar_telefone(telefone):
    print("Telefone válido")
else:
    print("Telefone inválido")


# Validação de Senha:

import re

def validar_senha(senha):
    padrão = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$"
    if re.match(padrão, senha):
        return True
    else:
        return False

senha = "Senha123!"
if validar_senha(senha):
    print("Senha válida")
else:
    print("Senha inválida")

#######################################################################

# Parâmetros opcionais:

# Em programação, parâmetros opcionais são parâmetros que podem ser omitidos quando uma função é chamada. Isso é útil quando você deseja fornecer valores padrão para alguns parâmetros, mas ainda permitir que o usuário os personalize.

# Exemplo em Python:

def saudacao(nome, mensagem="Olá"):
    print(f"{mensagem}, {nome}!")

saudacao("João")  # Saída: Olá, João!
saudacao("Maria", "Bem-vinda")  # Saída: Bem-vinda, Maria!


# Nesse exemplo, o parâmetro mensagem é opcional e tem um valor padrão de "Olá". Se o usuário não fornecer um valor para mensagem, o valor padrão será usado.

# Vantagens de parâmetros opcionais:

# - Flexibilidade: Parâmetros opcionais permitem que o usuário personalize a função sem ser obrigado a fornecer todos os parâmetros.
# - Legibilidade: Parâmetros opcionais podem tornar o código mais legível, pois não é necessário fornecer todos os parâmetros ao chamar a função.

# Desvantagens de parâmetros opcionais:

# - Complexidade: Parâmetros opcionais podem adicionar complexidade ao código, pois é necessário lidar com diferentes combinações de parâmetros.
# - Erros: Parâmetros opcionais podem levar a erros se o usuário não fornecer os parâmetros corretos.

# Boas práticas para usar parâmetros opcionais:

# - Use valores padrão: Forneça valores padrão para parâmetros opcionais para evitar erros.
# - Documente os parâmetros: Documente os parâmetros opcionais para que o usuário saiba quais parâmetros são obrigatórios e quais são opcionais.
# - Teste os parâmetros: Teste os parâmetros opcionais para garantir que a função funcione corretamente com diferentes combinações de parâmetros.

# Exemplo 1: Função com parâmetro opcional

def saudacao(nome, mensagem="Olá"):
    print(f"{mensagem}, {nome}!")

saudacao("João")  # Saída: Olá, João!
saudacao("Maria", "Bem-vinda")  # Saída: Bem-vinda, Maria!


# Exemplo 2: Função com múltiplos parâmetros opcionais

def imprimir_dados(nome, idade=None, cidade=None):
    print(f"Nome: {nome}")
    if idade:
        print(f"Idade: {idade}")
    if cidade:
        print(f"Cidade: {cidade}")

imprimir_dados("João", 30, "São Paulo")

# Saída:
# Nome: João
# Idade: 30
# Cidade: São Paulo

imprimir_dados("Maria", cidade="Rio de Janeiro")

# Saída:
# Nome: Maria
# Cidade: Rio de Janeiro


# Exemplo 3: Função com parâmetro opcional com valor padrão como lista

def imprimir_lista(nome, itens=[]):
    print(f"Nome: {nome}")
    print(f"Itens: {itens}")

imprimir_lista("João", [1, 2, 3])

# Saída:
# Nome: João
# Itens: [1, 2, 3]

imprimir_lista("Maria")

# Saída:
# Nome: Maria
# Itens: []


# Exemplo 4: Função com parâmetro opcional com valor padrão como dicionário

def imprimir_dicionario(nome, dados={}):
    print(f"Nome: {nome}")
    print(f"Dados: {dados}")

imprimir_dicionario("João", {"idade": 30, "cidade": "São Paulo"})

# Saída:
# Nome: João
# Dados: {'idade': 30, 'cidade': 'São Paulo'}

imprimir_dicionario("Maria"):

# Saída:
# Nome: Maria
# Dados: {}

#####################################################################

# Nomeando parâmetros:

# Em Python, é possível nomear parâmetros ao chamar uma função. Isso é útil quando você tem uma função com muitos parâmetros e deseja especificar quais parâmetros estão sendo passados.

# Exemplo:

def imprimir_dados(nome, idade, cidade):
    print(f"Nome: {nome}")
    print(f"Idade: {idade}")
    print(f"Cidade: {cidade}")

imprimir_dados(nome="João", idade=30, cidade="São Paulo")


# Nesse exemplo, estamos nomeando os parâmetros nome, idade e cidade ao chamar a função imprimir_dados.

# Vantagens de nomear parâmetros:

# - Legibilidade: Nomear parâmetros torna o código mais legível, pois é claro quais parâmetros estão sendo passados.

# - Flexibilidade: Nomear parâmetros permite que você passe os parâmetros em qualquer ordem.

# Exemplo com parâmetros nomeados em ordem diferente:

def imprimir_dados(nome, idade, cidade):
    print(f"Nome: {nome}")
    print(f"Idade: {idade}")
    print(f"Cidade: {cidade}")

imprimir_dados(cidade="São Paulo", idade=30, nome="João")


# Nesse exemplo, estamos passando os parâmetros em uma ordem diferente, mas ainda assim é claro quais parâmetros estão sendo passados.

# Parâmetros nomeados com valores padrão:

def imprimir_dados(nome, idade=30, cidade="São Paulo"):
    print(f"Nome: {nome}")
    print(f"Idade: {idade}")
    print(f"Cidade: {cidade}")

imprimir_dados(nome="João")


# Nesse exemplo, estamos nomeando o parâmetro nome e utilizando os valores padrão para os parâmetros idade e cidade.

#####################################################################

# Funções como parâmetro:

# Em Python, as funções podem receber parâmetros para realizar tarefas específicas. Os parâmetros são valores que são passados para a função quando ela é chamada.

# Sintaxe:

def nome_da_função(parâmetro1, parâmetro2, ...):
    
    # código da função


# Exemplo:

def saudacao(nome):
    print(f"Olá, {nome}!")

saudacao("João")  # Saída: Olá, João!


# Nesse exemplo, a função saudacão recebe um parâmetro nome e imprime uma saudação personalizada.

# Tipos de parâmetros:

# - Parâmetros posicionais: São parâmetros que são passados na ordem em que são definidos na função.
# - Parâmetros nomeados: São parâmetros que são passados com o nome do parâmetro seguido do valor.
# - Parâmetros padrão: São parâmetros que têm um valor padrão definido na função.

# Exemplo com parâmetros posicionais:

def imprimir_dados(nome, idade):
    print(f"Nome: {nome}")
    print(f"Idade: {idade}")

imprimir_dados("João", 30)


# Exemplo com parâmetros nomeados:

def imprimir_dados(nome, idade):
    print(f"Nome: {nome}")
    print(f"Idade: {idade}")

imprimir_dados(nome="João", idade=30)


# Exemplo com parâmetros padrão:

def imprimir_dados(nome, idade=30):
    print(f"Nome: {nome}")
    print(f"Idade: {idade}")

imprimir_dados("João")

######################################################################

# Empacotamento de parâmetro:

# Em Python, é possível empacotar parâmetros em uma função utilizando os operadores * e **. Isso permite que você passe uma quantidade variável de parâmetros para uma função.

# *Empacotamento de parâmetros posicionais com *:*

def imprimir_dados(*args):
    for arg in args:
        print(arg)

imprimir_dados("João", 30, "São Paulo")


# Nesse exemplo, a função imprimir_dados recebe uma quantidade variável de parâmetros posicionais, que são armazenados na tupla args.

# *Empacotamento de parâmetros nomeados com **:*

def imprimir_dados(**kwargs):
    for chave, valor in kwargs.items():
        print(f"{chave}: {valor}")

imprimir_dados(nome="João", idade=30, cidade="São Paulo")


# Nesse exemplo, a função imprimir_dados recebe uma quantidade variável de parâmetros nomeados, que são armazenados no dicionário kwargs.

# Empacotamento de parâmetros posicionais e nomeados:

def imprimir_dados(*args, **kwargs):
    for arg in args:
        print(arg)
    for chave, valor in kwargs.items():
        print(f"{chave}: {valor}")

imprimir_dados("João", 30, cidade="São Paulo")


# Nesse exemplo, a função imprimir_dados recebe uma quantidade variável de parâmetros posicionais e nomeados.

# Desempacotamento de parâmetros:

def imprimir_dados(nome, idade, cidade):
    print(f"Nome: {nome}")
    print(f"Idade: {idade}")
    print(f"Cidade: {cidade}")

dados = ["João", 30, "São Paulo"]
imprimir_dados(*dados)


# Nesse exemplo, a lista dados é desempacotada e passada como parâmetros posicionais para a função imprimir_dados.

######################################################################

# Funções Lambda:

# Podemos criar funções simples, sem nome, chamadas de funções "lambda".

# Função lambda que recebe um valor e retorna o dobro dele:

# a = lambda x: x*2
# print(a(3))

# # Função lambda que recebe mais de um parâmetro:

# aumento = lambda a, b: (a*b / 100)
# aumento(100, 5)

# Funções lambda são utilizadas quando o código da função é muito simples ou utilizado poucas vezes. Algumas funções da biblioteca padrão do Python também permitem que funções sejam passadas como parâmetros, como no caso do método 'sort' de listas, que recebe um parâmetro "key" que recebe o elemento e deve retornar a chave a utilizar para  a ordenação.

# L = ['A','b','C','d','E']
# L.sort()
# L
# # Saída:

# # ['A','C','E','b','d']

# L.sort(key=lambda k: k.lower())
# L
# Saída:
# ['A','b','C','d','E']

#####################################################################

# Exceções:

# São situações inesperadas em nosso código ou apenas algo que não tratamos diretamente no programa. Como exemplos: valueError, quando tentamos converter uma letra em número, e IndexError, quando tentamos acessar o elemento de lista além de seu tamnho. Essas são exceções da biblioteca-padrão do Python, mas podemos também criar nossas próprias exceções.

# O bloco responsável por tratar exceções é o  "try":

# nomes = ["Ana","Carlos","Maria"]
# for tentativa in range(3):
#     try:
#         i = int(input("Digite o índice que quer imprimir:"))
#         print(nomes[i])
#     except ValueError:
#         print("Digite um número!")
#     except IndentationError:
#         print("Valor inválido, digite entre 0 e 2")

# Vams agora modificar a declaração except e darmos um nome para a exceção, no caso "e":

# nomes = ["Ana","Carlos","Maria"]
# for tentativa in range(3):
#     try:
#         i = int(input("Digite o índice que quer imprimir:"))
#         print(nomes[i])
#     except Exception as e:
#         print(f"Algo de errado aconteceu: {e} ")

# O mesmo bloco "try" pode conter várias declarações except. Além disso, o bloco try pode ter uma declaração "finaly". Ao declararmos um bloco co 'finaly', estamos dizendo: execute este bloco, mesmo que aconteça uma exceção, com ou sem tratamento.

# Uma versão do mesmo programa, mas que trata apenas a exceção valueError:

# nomes = ["Ana","Carlos","Maria"]
# for tentativa in range(3):
#     try:
#         i = int(input("Digite o índice que quer imprimir:"))
#         print(nomes[i])
#     except ValueError:
#         print("Digite um número!")
#     finally:
#         print(f"Tentativa {tentativa + 1} ")

# Exceções são um recurso bem popular em várias linguagens de programação. Sua maior vantagemmé separar uma execução mormal de uma execução anorma.Usando exceções, evitamos retornar e verificar cpodigos de erro a cada chamada de função, centralizando o tratamento de erros do bloco em um só lugar e facilitando o tratamento em si.

# Podemos também gerar exceções usando a isntrução raise:

# nomes = ["Ana","Carlos","Maria"]
# for tentativa in range(3):
#     try:
#         i = int(input("Digite o índice que quer imprimir:"))
#         print(nomes[i])
#     except ValueError:
#         print("Digite um número!")
#         raise
#     finally:
#         print("Sempre o finally é executado ")
# saída:

# Digite o índice que quer imprimir:2
# Maria
# Tentativa 1
# Digite o índice que quer imprimir:1
# Carlos
# Tentativa 2
# Digite o índice que quer imprimir:abc
# Digite um número!
# Tentativa 3
# Digite o índice que quer imprimir:
# Digite um número!
# Sempre o finally é executado
# Traceback (most recent call last):

# Outro exemplo com função:

# def épar(n):
#     try:
#         return n % 2
#     finally:
#         print('Executado antes de retornar')

# Utilizando raise, podemos tmbém criar nossas próprias exceções:

# def épar(n):
#     try:
#         return n % 2
#     except Exception:
#         raise ValueError("Valor inválido")
    
# O blpco "try" também possui uma decalração "else", assim com "while" e o "for". A declaração "else" é executada apenas se não houver exceção no "try" e pode ser combinada com "except" e "finally", assim como usada separadamente:

# while True:
#     try:
#         v = int(input("Digite um número inteiro (o sai):"))
#         if v == 0:
#             break
#     except Exception:
#         print("Valor inválido! Redigite")
#     else:
#         print("Parabens, nenhuma exceção")
#     finally:
#         print("Executando sempre, mesmo com break")

# Saída:

# Digite um número inteiro (o sai):2
# Parabens, nenhuma exceção
# Executando sempre, mesmo com break
# Digite um número inteiro (o sai):100
# Parabens, nenhuma exceção
# Executando sempre, mesmo com break

###########################################################################

# Módulos:

# Depois de criarmos várias funções, os nossos programas ficaram muito grandes. Precisamos armazenar nossas funções em outros arquivos e de alguma forma usá-las, sem precisar reescrevê-las, ou pior, copiar e colar.

# Python resolve o problema com módulos. Todo arquivo .py é um módulo, podendo ser importado com o comando "import".

# Vamos criar dois programas: um chamado de "entrada.py" e soma.py:

# Módulo de entrada: criar arquivo - "entrada.py".

# def valida_inteiro(mensagem, mínimo, máximo):
#     while True:
#         try:
#             v = int(input(mensagem))
#             if v >= mínimo and v <= máximo:
#                 return v
#             else:
#                 print(f"Digite um valor entre {mínimo} e {máximo}")
#         except ValueError:
#             print("Você deve digitar um número inteiro")


# Módulo soma ( soma.py) que importa entrada:

# from entrada import valida_inteiro
# L = []
# for x in range(10):
#     L.append(valida_inteiro("Digite um número:", 0,20))
# print(f"Soma: {sum(L)}")

# Conflitos de nomes pode ocorrer quando dois ou mais módulos definem funções com nomes idênticos. Nesse caso, utilizamos a notação de chamada "módulo.função" que resolve o conflito, pois a combinação do nome do módulo com o nome da função é única.

# Outra construção que não deve ser utilizada é "from entrada import*". Neste caso estaríamos importando todas as definições do módulo entrada, e não apenas a função valida_inteiro.

#####################################################################

# Números aleatórios: randômicos ou aleatórios.É interessanta para trabalharmos com jogos:

import random
for x in range(10):
    print(random.randint(1,100))

import random
n = random.randint(1,10)
x =int(input("Escolha um número entre 1 e 10:"))
if x == n:
    print("Você acertou!")
else:
    print("Você errou!")

# Alterar o programa de forma que o usuário tenha três chances de acerta o número. O programa termina se o usuário acertar ou errar três vezes.

# Podemos também gerar números aleatórios fracionários ou de ponto flutuante com a função "random". A função random não recebe parâmetros e retorna valores entre 0 e 1.

# import random
# for x in range(10):
#    print(random.uniform(15,25))  

# Para obter valores fracionários dentro de uma determinada faixa, podemos usar a função "uniform:".
# Saída:

# 24.155620281972862
# 15.78469575767695
# 20.584163980685716
# 24.740758127224048
# 18.016862624663105
# 20.22351618996678
# 22.08817786808197
# 23.073420122579144
# 17.641146216642102
# 21.34605402237593

# Poderemos utilizar a função "sample" para escolher elementos aleatórios dentro de uma lista.

# Vejamos como gerar os números de um cartão de jogo de loto:

# import random
# print(random.sample(range(1,101), 6))

# Saída: [69, 56, 46, 38, 29, 73]

# Se quisermos embaralhar osw elementos de uma lista, podemos utilizar a função " shuffle".

# import random
# a = list(range(1,11))
# random.shuffle(a)
# print(a)

# Saída: [7, 3, 6, 5, 1, 2, 9, 4, 8, 10]

# Altere o jogo da forca - Programa 7.2. Escolaha a palavra a advinhar utilizando números aleatórios.

# Jogo alienígena:

import random
MAX_TENTATIVAS = 3
árvore = random.randint(1,100)
print("Um alienígena está escondido atrás de uma árvore")
print("Cada árvore foi numerada  de 1 a 100.")
print("Você tem 3 tentativas para adivinhar em que árvore")
print("O alienígena se esconde.")
print("Árvore")
for tentativa in range(1, MAX_TENTATIVAS + 1):
   palpite = int(input(f"Árvore {tentativa}/{MAX_TENTATIVAS}: "))
   if palpite == árvore:
      print("Você acertou na {tentativa}\u00AA tentativa")
      break
   elif palpite > árvore:
      print("Muito alto")
   else:
      print("Muito baixo")
else:
   print("Você não conseguiu acertar.")
   print(f"O alienígena estava na árvore {árvore}")

# Ex 8.17 - Modifique o jogo do alienígena. Crie uma variável que represente a vida do jogador, começando com 100. A partida termina quando você encontrar o alienígena ou quando a vida acabar ( <=0). A cada erro, diminuia a vida por um valor aleatório entre 5 e 20, representando um ataque do alienígena. Tirando a parte do jogo que limita o número de tentativas e deixar apenas a vida do jogador ou do alien´gena decidirem quando a partida termina. Exiba a vida do jogador antes de perguntar a próxima árvore.

# Ex 8.18 - Melhore o programa perguntando ao jogador o nível de dificuldade desejado. No modo fácil, a vida começa com 100 e o alienígena pode causar entre 5 e 20 de dano, como anteriormente. No modo médio, a vida começa com 80 e o alienígena pode causar danos entre 10 e 25. Já no modo difícil, a vida começa com 75 e o alienígena causa danos entre 20 e 30. Adicione mensagens e caracteres para deixar o jogo mais divertido.

# Podemos utilizar uma pesquisa binária para tentar encontrar o alienígena com 7 tentativas. 

# Os números aleatórios são uma ferramenta importante em muitas áreas, como estatística, simulação, modelagem e jogos.

# Módulo random:

# Em Python, o módulo random fornece uma maneira fácil de gerar números aleatórios.

# Importando o módulo:

# Para usar o módulo random, você precisa importá-lo:

# import random:

# Funções principais
# Aqui estão algumas das funções mais comuns do módulo random:

# - random(): Retorna um número aleatório entre 0 e 1.
# - uniform(a, b): Retorna um número aleatório entre a e b.
# - randint(a, b): Retorna um número aleatório entre a e b, incluindo a e b.
# - choice(seq): Retorna um elemento aleatório de uma sequência (list, tuple, string, etc.).
# - shuffle(seq): Embaralha os elementos de uma sequência.

# Exemplos:

# Aqui estão alguns exemplos de como usar o módulo random:

import random

# Gerar um número aleatório entre 0 e 1:

print(random.random())

# Gerar um número aleatório entre 1 e 10:

print(random.uniform(1, 10))

# Gerar um número aleatório entre 1 e 10, incluindo 1 e 10:

print(random.randint(1, 10))

# Escolher um elemento aleatório de uma lista:

frutas = ['maçã', 'banana', 'laranja']
print(random.choice(frutas))

# Embaralhar os elementos de uma lista:

numeros = [1, 2, 3, 4, 5]
random.shuffle(numeros)
print(numeros)

#####################################################################

# Função "type".

# Para tratar diferentemente tipos de dados, precisamos de uma função que nos informa de que tipo é uma variável. 

# A função "type" retrona o tipo de uma variável, função ou objeto em Python.

# A função type() em Python é usada para determinar o tipo de um objeto. Ela retorna o tipo do objeto como um objeto type.

#Sintaxe:

# A sintaxe da função type() é:

# type(objeto)

# Onde:

# - objeto é o objeto cujo tipo você deseja determinar.

# Exemplos:

# Aqui estão alguns exemplos de como usar a função type():

# Verifique o tipo de uma variável inteira: 

x = 5
print(type(x))  # Saída: <class 'int'>

# Verifique o tipo de uma variável string:

y = "Olá, mundo!"
print(type(y))  # Saída: <class 'str'>

# Verifique o tipo de uma lista:

z = [1, 2, 3]
print(type(z))  # Saída: <class 'list'>

# Verifique o tipo de um dicionário:

w = {"nome": "João", "idade": 30}
print(type(w))  # Saída: <class 'dict'>

# Uso comum: 

# A função type() é usada com frequência para:

# - Verificar se um objeto é de um tipo específico.
# - Determinar o tipo de um objeto desconhecido.
# - Realizar operações condicionais com base no tipo de um objeto.

# Dica:

# Você também pode usar a função isinstance() para verificar se um objeto é de um tipo específico. A diferença é que isinstance() também verifica se o objeto é uma instância de uma classe que herda do tipo especificado. Por exemplo:

x = 5
print(isinstance(x, int))  # Saída: True

# Para verificar se o tipo de uma variável equivale a outro tipo, utilizaremos a função "isistance".

import types
def diz_o_tipo(a):
   if isinstance(a, str):
      return "string"
   elif isinstance(a, list):
      return "Lista"
   elif isinstance(a, dict):
      return "Dicionário"
   elif isinstance(a, int):
      return "Número inteiro"
   elif isinstance(a, float):
      return "Número decimal"
   elif isinstance(a, types.FunctionType):
      return "Função"
   elif isinstance(a, types.BuiltinFunctionType):
      return "Função interna"
   else:
      print(diz_o_tipo(10))
      print(diz_o_tipo(10.5))
      print(diz_o_tipo("Alô"))
      print(diz_o_tipo([1,2,3]))
      print(diz_o_tipo({"a": 1, "b": 50}))
      print(diz_o_tipo(print))
      print(diz_o_tipo(None))

# Imagiene uma lista onde seus elementos podem ser do tipo string ou listas:

L = ["a", ["b", "c", "d"], "e"]
for x in L:
   if isinstance(x, str):
      print(x)
   else:
      print("Lista:", end="")
   for z in x:
      print(f" {z}", end="")
      print()

# Imprimindo uma lista de inteiros com múltiplos níveis:

def imprime_listas(lista, nível=0):
   for x in lista:
      if isinstance(x, int):
         print(f"{x:{nível * 2}}")
      else:
         imprime_listas(x, nível + 1)

imprime_listas([1, [2,3,4], [5,6, [7,8,8]], 10])

# Saída:

# 1
#  2
#  3
#  4
#  5
#  6
#    7
#    8
#    8
# 10

##########################################################################

# List Comprehensions: uma sintaxe capaz de especificar como os elementos de uma lista devem ser criados.

# As "list comprehensions" em Python são uma forma concisa de criar listas a partir de iteráveis, como listas ou tuplas.

# Sintaxe: 

# A sintaxe para criar uma lista usando "list comprehensions" é:

# [expressão for variável in iterável]

# Onde:

# - expressão é a expressão que é avaliada para cada elemento do iterável.
# - variável é a variável que itera sobre o iterável.

# Exemplo:

# Aqui está um exemplo de como criar uma lista de quadrados de números:

# Crie uma lista de números:

numeros = [1, 2, 3, 4, 5]

# Crie uma lista de quadrados de números:

quadrados = [n**2 for n in numeros]

# Imprima a lista de quadrados:

print(quadrados)


# Nesse exemplo, a lista quadrados é criada com a expressão n**2 para cada elemento n da lista numeros. A saída será:

# [1, 4, 9, 16, 25]

# Outros exemplos:

# Aqui estão alguns outros exemplos de como usar "list comprehensions":

# - Crie uma lista de números pares:

pares = [n for n in range(1, 11) if n % 2 == 0]
print(pares)

# - Crie uma lista de letras do alfabeto:


alfabeto = [letra for letra in 'abcdefghijklmnopqrstuvwxyz']
print(alfabeto)

L = [x for x in range(10)]
print(L)

# Saída: [0,1,2,3,4,5,6,7,8,9]

# Podemos também usar list comprehensions com outras listas:

Z = [x * 2 for x in [0,1,2,3]]
print(Z)  # Saida:  [0, 2, 4, 6]

# Podemos também usar list comprehensions para criar listas mais complexas, nos quais os elementos é uma tupla:

Y = [(x, x * 2) for x in [1,2,3]]
print(Y)  # Saída: [(1, 2), (2, 4), (3, 6)]

z = [s.upper() for s in "abcdef"]
print(z)  # Saída: ['A', 'B', 'C', 'D', 'E', 'F']

# Outro recurso da list comprehensions é a capacidade de filtar utilizando um if interno:

pares = [x for x in range(10) if x%2 ==0]
print(pares)  # Saída: [0, 2, 4, 6, 8]

d = [(y,x) for x,y in [(4,3),(1,2),(8,9)]] # Inverte os elementos de cada tupla
print(d)  

# Saída: [(3, 4), (2, 1), (9, 8)] 

# Um exemplo de desempacotamento mais complexo:

j = [(x, y) for x, *y in [(4,2,3), (5,1,2), (7,8,9)]]
print(j)  # Desempacota o 1º elemento "x" e os restantes em y.

# Saída: [(4, [2, 3]), (5, [1, 2]), (7, [8, 9])]

# Podemos também chamar funções:

import math
I = [math.sqrt(z) for z in range(0,10)]
print(I) 

# Saída: [0.0, 1.0, 1.4142135623730951, 1.7320508075688772, 2.0, 2.23606797749979, 2.449489742783178, 2.6457513110645907, 2.8284271247461903, 3.0]

H = [z for z in range(0,10) if math.sqrt(z) % 1 ==0]
print(H) #  Saída: 0, 1, 4, 9]

#####################################################################

# Geradores:

# Os geradores (generators) em Python são uma forma de criar iteráveis que produzem valores em tempo de execução, sem armazenar todos os valores em memória.

# Características dos geradores:

# - Produzem valores em tempo de execução: Os geradores produzem valores apenas quando são solicitados, o que pode ser útil para lidar com grandes conjuntos de dados.
# - Não armazenam todos os valores em memória: Os geradores não armazenam todos os valores em memória, o que pode ser útil para lidar com grandes conjuntos de dados.
# - São iteráveis: Os geradores são iteráveis, o que significa que podem ser usados em loops for e em outras funções que aceitam iteráveis.

# Criando geradores:

# Existem duas formas principais de criar geradores em Python:

# 1. Funções geradoras: As funções geradoras são funções que contêm a palavra-chave yield em vez de return. Quando uma função geradora é chamada, ela retorna um gerador.
# 2. Expressões geradoras: As expressões geradoras são expressões que usam a sintaxe (expressão for variável in iterável) para criar um gerador.

# Exemplos de geradores:

# Aqui estão alguns exemplos de geradores:

# - Função geradora que produz números:

def gerador_numeros():
    for i in range(10):
        yield i

for numero in gerador_numeros():
    print(numero)


# - Expressão geradora que produz quadrados:


gerador_quadrados = (i**2 for i in range(10))

for quadrado in gerador_quadrados:
    print(quadrado)

# Aqui está um exemplo de um gerador que produz a sequência de Fibonacci:

def gerador_fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Crie um gerador de Fibonacci:

fibonacci = gerador_fibonacci()

# Imprima os primeiros 10 números da sequência de Fibonacci:

for _ in range(10):
    print(next(fibonacci))


# Nesse exemplo, o gerador gerador_fibonacci produz a sequência de Fibonacci infinita. A função next() é usada para obter o próximo número da sequência.

# A saída desse exemplo será:


0
1
1
2
3
5
8
13
21
34


# Essa é a sequência de Fibonacci até o décimo número. O gerador pode continuar produzindo números indefinidamente.

# Aqui está o exemplo do gerador gerador_fibonacci que utiliza um loop while para gerar a sequência de Fibonacci até que o valor atual seja maior ou igual ao valor de fim:

def gerador_fibonacci(fim):
    a, b = 0, 1
    while a < fim:
        yield a
        a, b = b, a + b


# Crie um gerador de Fibonacci que vai até 30:

fibonacci = gerador_fibonacci(30)

# Imprima os números da sequência de Fibonacci:

for numero in fibonacci:
    print(numero)


# Nesse exemplo, o gerador gerador_fibonacci utiliza um loop while para gerar a sequência de Fibonacci até que o valor atual seja maior ou igual ao valor de fim. O gerador então produz os números da sequência de Fibonacci até que o valor atual seja maior ou igual ao valor de fim.

# A saída desse exemplo será:

0
1
1
2
3
5
8
13
21
34
55
89

# Mudando o yield para "b":

def gerador_fibonacci(fim):
    a, b = 0, 1
    while a < fim:
        yield b
        a, b = b, a + b


# Crie um gerador de Fibonacci que vai até 100:

fibonacci = gerador_fibonacci(30)

# Imprima os números da sequência de Fibonacci:



# Crie um gerador de Fibonacci que vai até 100:

fibonacci = gerador_fibonacci(30)

# Imprima os números da sequência de Fibonacci:

for numero in fibonacci:
    print(numero)

# A saída desse gerador seria:

# 1, 1, 2, 3, 5, 8, 13, 21, ... (até que o valor atual seja maior ou igual a fim)

# Observe que o gerador está produzindo os valores da sequência de Fibonacci, mas começando a partir do segundo termo (1) em vez do primeiro termo (0). Isso ocorre porque o gerador está usando yield b em vez de yield a.


# Essa é a sequência de Fibonacci até que o valor atual seja maior ou igual a 30.

# Vantagens dos geradores:

# Os geradores têm várias vantagens, incluindo:

# - Eficiência de memória: Os geradores não armazenam todos os valores em memória, o que pode ser útil para lidar com grandes conjuntos de dados.
# - Flexibilidade: Os geradores podem ser usados em uma variedade de contextos, incluindo loops for e funções que aceitam iteráveis.

# Desvantagens dos geradores:

# Os geradores também têm algumas desvantagens, incluindo:

# - Complexidade: Os geradores podem ser mais difíceis de entender e usar do que outras estruturas de dados.
# - Limitações: Os geradores têm algumas limitações, incluindo a impossibilidade de acessar elementos anteriores após terem sido gerados.


# ###################################################################

# # Generator Comprehensions:

# As "generator comprehensions" em Python são uma forma concisa de criar geradores (generators) a partir de iteráveis, como listas ou tuplas.

# Sintaxe:

# A sintaxe para criar um gerador usando "generator comprehensions" é:

# (expressão for variável in iterável)

# Onde:

# - expressão é a expressão que é avaliada para cada elemento do iterável.
# - variável é a variável que itera sobre o iterável.

# Exemplo:

# Aqui está um exemplo de como criar um gerador usando "generator comprehensions":

# Crie uma lista de números:

numeros = [1, 2, 3, 4, 5]

# Crie um gerador que produz os quadrados dos números:

quadrados = (n**2 for n in numeros)

# Imprima os valores produzidos pelo gerador:

for valor in quadrados:
    print(valor)

# Nesse exemplo, o gerador quadrados é criado com a expressão n**2 para cada elemento n da lista numeros. O gerador produz os valores 1, 4, 9, 16 e 25, que são os quadrados dos números da lista.

# Outros exemplos:

# Aqui estão alguns outros exemplos de como usar "generator comprehensions":

# - Crie um gerador que produz os números pares de 1 a 10:

pares = (n for n in range(1, 11) if n % 2 == 0)
for valor in pares:
    print(valor)

# - Crie um gerador que produz as letras do alfabeto:


alfabeto = (letra for letra in 'abcdefghijklmnopqrstuvwxyz')
for letra in alfabeto:
    print(letra)


##########################################################################

# Dict Comprehensions:

# As "dict comprehensions" em Python são uma forma concisa de criar dicionários a partir de iteráveis, como listas ou tuplas.

# Sintaxe:

# A sintaxe para criar um dicionário usando "dict comprehensions" é:

# {chave: valor for variável in iterável}

# Onde:

# - chave é a chave do dicionário.
# - valor é o valor associado à chave.
# - variável é a variável que itera sobre o iterável.

# Exemplo:

# Aqui está um exemplo de como criar um dicionário usando "dict comprehensions":


# Crie uma lista de números:

numeros = [1, 2, 3, 4, 5]

# Crie um dicionário com os números como chaves e seus quadrados como valores:

quadrados = {n: n**2 for n in numeros}

# Imprima o dicionário:

print(quadrados)


# Nesse exemplo, o dicionário quadrados é criado com os números da lista numeros como chaves e seus quadrados como valores.

# Outros exemplos:

# Aqui estão alguns outros exemplos de como usar "dict comprehensions":

# - Crie um dicionário com as letras do alfabeto como chaves e seus códigos ASCII como valores:


alfabeto = {letra: ord(letra) for letra in 'abcdefghijklmnopqrstuvwxyz'}
print(alfabeto)


# - Crie um dicionário com os números de 1 a 10 como chaves e seus fatores como valores:

fatores = {n: [i for i in range(1, n+1) if n % i == 0] for n in range(1, 11)}
print(fatores)


# Vejamos como gerar um dicionário simples:

{chave: valor * 2 for chave, valor in {"a": 1, "b":2}.items()}


##########################################################################

# Set Comprehensions:

# As "set comprehensions" em Python são uma forma concisa de criar conjuntos (sets) a partir de iteráveis, como listas ou tuplas.

# Sintaxe:

# A sintaxe para criar um conjunto usando "set comprehensions" é:

# {expressão for variável in iterável}


# Onde:

# - expressão é a expressão que é avaliada para cada elemento do iterável.
# - variável é a variável que itera sobre o iterável.

# Exemplo:

# Aqui está um exemplo de como criar um conjunto usando "set comprehensions":


# Crie uma lista de números:

numeros = [1, 2, 2, 3, 4, 4, 5]

# Crie um conjunto com os números da lista:

conjunto_numeros = {n for n in numeros}

# Imprima o conjunto:

print(conjunto_numeros)


# Nesse exemplo, o conjunto conjunto_numeros é criado com os números da lista numeros, sem repetições.

# Outros exemplos:

# Aqui estão alguns outros exemplos de como usar "set comprehensions":

# - Crie um conjunto com as letras do alfabeto:


alfabeto = {letra for letra in 'abcdefghijklmnopqrstuvwxyz'}
print(alfabeto)


# - Crie um conjunto com os números pares de 1 a 10:


pares = {n for n in range(1, 11) if n % 2 == 0}
print(pares)

{x for x in [9,2,1,3,6,9] if x % 3 == 0}  # Saida: {9,3,6}

# Explicação:

# - O conjunto é criado a partir da lista [9, 2, 1, 3, 6, 9].
# - A condição if x % 3 == 0 é aplicada a cada elemento da lista.
# - Os elementos que satisfazem a condição (ou seja, os números que são múltiplos de 3) são incluídos no conjunto.
# - O conjunto resultante contém os elementos 9, 3 e 6, que são os números da lista que são múltiplos de 3.

##########################################################################

# Map e Zip:

# Um padrão de código é gerar uma lista com o resultado de uma função aplicada a outra lista. Ao utilizarmaos a função "map", a função a ser aplicada é passada primeiro parâmetro e a lista ou iterável a aplicá-lamem seguida.

def map_1(função, valores):
   retorno = []
   for v in valores:
      retorno.append(função(v))
   return retorno

# Vejamos um exemplo em que passamos uma função "lambda" como parâmetro, seguida de uma lista com três números:

map_1(lambda x: x/2, [1,2,3])

list(map(lambda x: x/2, [1,2,3]))

# A função "map" é capar de combinar várias listas, passando um elemento de cada para a função:

list(map(lambda a, b: a + b, [1,2,3], [4,5,6]))
print(list)  # [5,6,7]

# Modificar o exemplo anterior para retornar uma tupla com os parâmetros, para ficar mais claro:

list(map(lambda a, b: (a,b), [1,2,3], [4,5,6]))
print(list)  # [(1,4),(2,5),(3,6)]

# Outra função que nos permite combinar duas ou mais listas, uma a outra: zip:

zip([1,2,3], [4,5,6])   # <zip object at 0x000001DA87A02400>

list(zip([1,2,3], [4,5,6]))   # [(1,4),(2,5),(3,6)] - Expandindo com list.

# Se a lista têm tamanhos diferentes, o resultado é a combinação dos elementos com o da menor lista:

list(zip([1,2], [4,5,6])) # [(1,4),(2,5)]

# Vamos implementar nossa função map_2, usando "zip" para ser mais parecida com "map" do Python:

def map_2(função, *valores):
   retorno = []
   for v in zip(*valores):
      retorno.append(função(*v))
   return retorno

map_2(lambda a, b: (a,b), [1,2,3], [4,5,6])  # [(1,4),(2,5),(3,6)] 

# Vamos escrever map_3 para retornar um gerador, como na função map do Python.

def map_3(função, *valores):
   for v in zip(*valores):
      yield função(*v)

map_3(lambda a, b: (a,b), [1,2,3], [4,5,6])

map_3(lambda a, b: (a,b), [1,2,3], [4,5,6])
# <zip object at 0x000001DA87A02400>


list(map_3(lambda a, b: (a,b), [1,2,3], [4,5,6])) # [(1,4),(2,5),(3,6)] 

# O uso do gerador permitiu que retirássemos a criação da lista de dentro da função amp_3. Caso precisemos desses tipos de construções, lembrar de "map" e zip.

# Com o uso de comprehensions, o uso de "map" se tornou raro em Python. A sintaxe de commprehensions é mais clara e permite a criação de estruturas diferentes, não apenas listas, mas conjuntos, dicionários e mesmo geradores. Por exemplo:

[e for e in zip([1,2,3], [4,5,6])]

# Ou:

list(zip([1,2,3], [4,5,6]))

#####################################################################

# Reduce: a função reduce quase foi retirada do Python, mas finalmente foi preservada no módulo "functools", teremos que importá-la.

from functools import reduce
reduce(min, [2,1,9,4])
reduce(max, [2,1,9,4])

import operator
reduce(operator.add, [1,2,3])  # somamos os elementos da lista: 6

# Tabela - funções definidas no módulo operator:

# | Função | Operador | Função operator |
# | --- | --- | --- |
# | Adição | + | add(x, y) |
# | Subtração | - | sub(x, y) |
# | Multiplicação | * | mul(x, y) |
# | Divisão | / | truediv(x, y) |
# | Divisão inteira | // | floordiv(x, y) |
# | Módulo | % | mod(x, y) |
# | Potência | ** | pow(x, y) |
# | Igualdade | == | eq(x, y) |
# | Desigualdade | != | ne(x, y) |
# | Menor que | < | lt(x, y) |
# | Menor ou igual a | <= | le(x, y) |
# | Maior que | > | gt(x, y) |
# | Maior ou igual a | >= | ge(x, y) |
# | Negação | not | not_(x) |
# | Conjunção | and | and_(x, y) |
# | Disjunção | or | or_(x, y) |
# | Deslocamento à esquerda | << | lshift(x, y) |
# | Deslocamento à direita | >> | rshift(x, y) |
# | Bit a bit AND | & | and_(x, y) |
# | Bit a bit OR | | | or_(x, y) |
# | Bit a bit XOR | ^ | xor(x, y) |

# O módulo operator em Python fornece funções que correspondem às operações matemáticas e de comparação. Aqui estão algumas das funções definidas no módulo operator:

# Operações Matemáticas
# - add(x, y): Retorna a soma de x e y.
# - sub(x, y): Retorna a subtração de y de x.
# - mul(x, y): Retorna o produto de x e y.
# - truediv(x, y): Retorna a divisão de x por y.
# - floordiv(x, y): Retorna a divisão de x por y, arredondando para baixo.
# - mod(x, y): Retorna o resto da divisão de x por y.
# - pow(x, y): Retorna x elevado à potência y.

# Operações de Comparação
# - eq(x, y): Retorna True se x for igual a y.
# - ne(x, y): Retorna True se x não for igual a y.
# - lt(x, y): Retorna True se x for menor que y.
# - le(x, y): Retorna True se x for menor ou igual a y.
# - gt(x, y): Retorna True se x for maior que y.
# - ge(x, y): Retorna True se x for maior ou igual a y.

# Operações Lógicas
# - not_(x): Retorna o valor lógico negado de x.
# - and_(x, y): Retorna True se ambos x e y forem verdadeiros.
# - or_(x, y): Retorna True se pelo menos um de x ou y for verdadeiro.

# Operações de Atribuição
# - iadd(x, y): Retorna a soma de x e y e atribui o resultado a x.
# - isub(x, y): Retorna a subtração de y de x e atribui o resultado a x.
# - imul(x, y): Retorna o produto de x e y e atribui o resultado a x.
# - itruediv(x, y): Retorna a divisão de x por y e atribui o resultado a x.
# - ifloordiv(x, y): Retorna a divisão de x por y, arredondando para baixo, e atribui o resultado a x.
# - imod(x, y): Retorna o resto da divisão de x por y e atribui o resultado a x.
# - ipow(x, y): Retorna x elevado à potência y e atribui o resultado a x.

# Operações de Deslocamento de Bits
# - lshift(x, y): Retorna o valor de x deslocado para a esquerda por y bits.
# - rshift(x, y): Retorna o valor de x deslocado para a direita por y bits.

# Operações de Bit a Bit:

# - and_(x, y): Retorna o resultado da operação de bit a bit AND entre x e y.
# - or_(x, y): Retorna o resultado da operação de bit a bit OR entre x e y.
# - xor(x, y): Retorna o resultado da operação de bit a bit XOR entre x e y.


# Poderíamos ter implementado os exemplos com as funções min e max diretamente.

max(*[2,1,9,4])  # 9
min(*[2,1,9,4])  # 1

sum([2,1,9,4])   # 16

##########################################################################

# Filter:

# É outra função vinda da programação funcional. Pode ser utilizada para selecionar ou filtrar quais elementos de um lista ou iterável (tuplas, conjuntos etc). Filter recebe uma função como primeiro parâmetro e um iterável a filtrar. Apenas os valores em que a função retorna True são incluídas no gerador retornando.

# A função filter() em Python é uma função integrada que permite filtrar elementos de uma sequência (como uma lista, tupla ou string) com base em uma condição específica.

# Sintaxe:

# A sintaxe da função filter() é:


# filter(função, sequência)


# Onde:

# - função é uma função que define a condição para filtrar os elementos.
# - sequência é a sequência de elementos que você deseja filtrar.

# Exemplo:

# Aqui está um exemplo de como usar a função filter():


# Defina uma lista de números:

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Defina uma função que verifica se um número é par:

def é_par(x):
    return x % 2 == 0

# Use a função filter() para filtrar os números pares:

numeros_pares = list(filter(é_par, numeros))

# Imprima a lista de números pares:

print(numeros_pares)


# Nesse exemplo, a função é_par() é usada para filtrar os números pares da lista numeros. O resultado é uma nova lista numeros_pares que contém apenas os números pares.

# Outros exemplos:

# Aqui estão alguns outros exemplos de como usar a função filter():

# - Filtrar strings que começam com uma letra específica:


palavras = ["maçã", "banana", "abacate", "ameixa"]
palavras_com_a = list(filter(lambda x: x.startswith("a"), palavras))
print(palavras_com_a)


# - Filtrar números que são maiores que um valor específico:


numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numeros_maiores_que_5 = list(filter(lambda x: x > 5, numeros))
print(numeros_maiores_que_5)


# Vamos filtar apenas os números pares de uma lista:

list(filter(lambda a: a % 2 == 0, [5,6,9,2,10]))

# Poderia ser também assim:

[a for a in [5,6,9,2,10] if a % 2 == 0]

#########################################################################

# Aplicação parcial de funções:

# A aplicação parcial de funções é uma técnica que permite aplicar uma função a alguns de seus argumentos, retornando uma nova função que espera os argumentos restantes.

# Função partial do módulo functools:

import functools

def soma(a, b, c):
    return a + b + c

soma_parcial = functools.partial(soma, 1, 2)
print(soma_parcial(3))  # Saída: 6


# Nesse exemplo, a função soma é aplicada parcialmente com os argumentos 1 e 2, retornando uma nova função soma_parcial que espera apenas o argumento c.

# Aplicação parcial de funções com lambda:

soma = lambda a, b, c: a + b + c
soma_parcial = lambda c: soma(1, 2, c)
print(soma_parcial(5))  # Saída: 8


# Nesse exemplo, a função soma é definida como uma expressão lambda e, em seguida, é aplicada parcialmente com os argumentos 1 e 2, retornando uma nova função lambda soma_parcial que espera apenas o argumento c.

# Vantagens da aplicação parcial de funções:

# - Reutilização de código: A aplicação parcial de funções permite reutilizar código, reduzindo a duplicação de esforço.

# - Flexibilidade: A aplicação parcial de funções fornece flexibilidade, permitindo que você aplique funções a diferentes conjuntos de argumentos.

# - Legibilidade: A aplicação parcial de funções pode melhorar a legibilidade do código, tornando-o mais fácil de entender e manter.

#########################################################################

# Funções matemáticas:

# Funções Aritméticas:

# - Soma: a + b
# - Subtração: a - b
# - Multiplicação: a * b
# - Divisão: a / b
# - Módulo: a % b (resto da divisão)

# Funções de Potência:

# - Potência: a ** b (a elevado à potência de b)
# - Raiz Quadrada: math.sqrt(a)

# Funções Trigonométricas:

# - Sen: math.sin(a)
# - Cos: math.cos(a)
# - Tan: math.tan(a)
# - Asin: math.asin(a)
# - Acos: math.acos(a)
# - Atan: math.atan(a)

# Funções Exponenciais:

# - Exponencial: math.exp(a)
# - Logaritmo Natural: math.log(a)
# - Logaritmo na Base 10: math.log10(a)

# Funções de Rounding:

# - Arredondamento para Baixo: math.floor(a)
# - Arredondamento para Cima: math.ceil(a)
# - Arredondamento para o Mais Próximo: round(a)

# Funções de Número Aleatório:

# - Número Aleatório entre 0 e 1: random.random()
# - Número Aleatório entre a e b: random.uniform(a, b)
# - Número Aleatório Inteiro entre a e b: random.randint(a, b)

# Exemplo 1: Função de soma

def soma(a, b):
    return a + b

print(soma(2, 3))  # Saída: 5


# Exemplo 2: Função de potência

def potencia(a, b):
    return a ** b

print(potencia(2, 3))  # Saída: 8


# Exemplo 3: Função de raiz quadrada

import math

def raiz_quadrada(a):
    return math.sqrt(a)

print(raiz_quadrada(16))  # Saída: 4.0


# Exemplo 4: Função de seno

import math

def seno(a):
    return math.sin(a)

print(seno(math.pi/2))  # Saída: 1.0


# Exemplo 5: Função de exponencial

import math

def exponencial(a):
    return math.exp(a)

print(exponencial(2))  # Saída: 7.38905609893065


# Exemplo 6: Função de logaritmo natural

import math

def logaritmo_natural(a):
    return math.log(a)

print(logaritmo_natural(10))  # Saída: 2.302585092994046


# Exemplo 7: Função de arredondamento

import math

def arredondamento(a):
    return math.floor(a)

print(arredondamento(3.7))  # Saída: 3


# Exemplo 8: Função de número aleatório

import random

def numero_aleatorio():
    return random.random()

print(numero_aleatorio())  # Saída: um número aleatório entre 0 e 1

#########################################################################

#  Operador Walrus(Morsa):

# O operador Walrus, também conhecido como operador de atribuição de expressão, é um recurso novo do Python, introduzido na versão 3.8. Ele permite atribuir um valor a uma variável dentro de uma expressão.

# Sintaxe:

# variavel := expressao

# Exemplo:

if (n := len(my_list)) > 5:
    print(f"Lista tem {n} elementos")


# Nesse exemplo, o operador Walrus atribui o valor da expressão len(my_list) à variável n e, em seguida, compara o valor de n com 5.

# Vantagens:

# - Redução de código: O operador Walrus pode reduzir a quantidade de código necessário para realizar uma tarefa.

# - Melhoria da legibilidade: Ele pode tornar o código mais legível, pois elimina a necessidade de atribuir um valor a uma variável em uma linha separada.

# Exemplos adicionais:

# - Laço while:

while (line := input("Digite uma linha: ")) != "":
    print(line)

# - Laço for:

for (i := 0) in range(10):
    print(i)

# - Condição if:

if (x := 5) > 10:
    print("x é maior que 10")

######################################################################

