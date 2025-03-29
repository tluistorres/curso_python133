# Manipulação de arquivos -modo open.

manipulador = open('arquivo.txt') # O importante é o nome do arquivo.

manipulador = open('arquivo.txt', 'r', encoding='utf-8')
print(f'Método read():\n')
print(manipulador.read())

print(f'Método readline():\n')
print(manipulador.readline())
print(manipulador.readline())
print(manipulador.readline())
print(manipulador.readline())  

# Retoma uma linha por vez. Tendo que repeti o comando readline para cada rpóxima linha.

print(manipulador.readlines())   

# Comando readlines, fornece uma lista com entre [], com as quatros linhas, onde poderemos manipular como linhas.

try:
    manipulador = open('arquivo.txt', 'r', encoding='utf-8')
    for linha in manipulador:
        linha = linha.rstrip()    
        
        # Tira o espaço entre as linhas, mostra sem a quebra de linha.

        print(linha)
except IOError:
    print(f'Não foi possível abrir o arquivo')
else:
    manipulador.close()

try:
    manipulador = open('C:\\Users\\luist\OneDrive\\Documentos\\arquivo2.txt', 'r', encoding='utf-8')
    for linha in manipulador:
        linha = linha.rstrip()    
        
# Tira o espaço entre as linhas, mostra sem a quebra de linha.

        print(linha)
except IOError:
    print(f'Não foi possível abrir o arquivo')
else:
    manipulador.close()


# Vamos voltar pro código anterior. Vamos fazer uma busca.

texto = input('Qual termo deseja procurar no arquivo?')
try:
    manipulador = open('arquivo.txt', 'r', encoding='utf-8')
    for linha in manipulador:
        linha = linha.rstrip()   

# Tira o espaço entre as linhas, mostra sem a quebra de linha.

        if texto in linha:
            print('A strig foi encontrada!')
            print(linha)

except IOError:
    print(f'Não foi possível abrir o arquivo')
else:
   print('String não encontrada!')

Gravando e escrevendo num arquivo de texto - método write.

try:
    manipulador = open('arquivo.txt', 'w', encoding='utf-8') 
    
    # Bastas trocar o 'r' por 'w'.

    manipulador.write('Bóson Trinamentos\n')
    manipulador.write('Como criar um arquivo de texto com Python.')
except IOError:
    print(f'Não foi possível abrir o arquivo')
else:
    manipulador.close() 
    
# Agora é só visulazar  no arquivo que foi substituído o texto anterior.

# Adicionar um texto ao atual - trocar o 'w' por 'a' de appen, adicionar.

# texto = 'n\Python é usado em ciências de dados extensivamente.'
# try:
#     manipulador = open('arquivo.txt', 'a', encoding='utf-8') # Bastas trocar o 'r' por 'w'.
#     manipulador.write('\nPython é muito empregado em IA')
#     manipulador.write('\nInteligência Artificial veio pra ficar.') # Ajustar \n no início.
# except IOError:
#     print(f'Não foi possível abrir o arquivo')
# else:
#     manipulador.close() # Observa-se que não altera o texto anterior, só acrecentas as linhas novas.

# Poderíamos também acrescentar dessa foram.

texto = '\nPython é usado em ciências de dados extensivamente.'
try:
    manipulador = open('arquivo.txt', 'a', encoding='utf-8') 
    
# Bastas trocar o 'w' por 'a'.

    manipulador.write(texto)
except IOError:
    print(f'Não foi possível abrir o arquivo')
else:
    manipulador.close()
texto = '\nPython é usado em ciências de dados extensivamente.'

#####################################################################

# Criar e gravar o arquivo.

frutas = ['Morango\n', 'Uva\n', 'Caju\n', 'Amora\n', 'Framboesa\n', 'Graviola']
try:
    manipulador = open('frutas.dat', 'w', encoding='utf-8') 

# Bastas trocar o 'w' por 'a'.

    manipulador.writelines(frutas)  
    
# writelines de listas.

except IOError:
    print(f'Não foi possível abrir o arquivo')
else:
    manipulador.close()

# Lê o arquivo criado. Precisamos do comando 'r', lê porque 'w' só permite gravar.

try:
    manipulador = open('frutas.dat', 'r', encoding='utf-8')  
    
# Trocar o 'w' por 'r1'.

    print(manipulador.read())
except IOError:
    print(f'Não foi possível abrir o arquivo')
else:
    manipulador.close()

# Morango
# Uva
# Caju
# Amora
# Framboesa
# Graviola

#######################################################################

# Modos de abertura de arquivos:

# Exemplos:

# - open('arquivo.txt', 'r'): Abre o arquivo em modo de leitura.
# - open('arquivo.txt', 'w'): Abre o arquivo em modo de escrita.
# - open('arquivo.txt', 'a'): Abre o arquivo em modo de adição.
# - open('arquivo.txt', 'rb'): Abre o arquivo em modo binário.
# - open('arquivo.txt', 'r+'): Abre o arquivo em modo de atualização.

#- 'rb' abre o arquivo em modo binário para leitura (r + b).
#- 'b' abre o arquivo em modo binário, mas não especifica se é para leitura ou escrita. Nesse caso, o Python assume que é para leitura.

# Lembre-se de sempre fechar o arquivo após usar, para evitar problemas de segurança e desempenho. Você pode usar o método close() ou o gerenciador de contexto with para fechar o arquivo automaticamente.

# Abrindo aquivos. Caso exista, apaga e cria novo arquivo:

arquivo = open('números.txt', 'w')
for linha in range(1,101):  
    
# O for para gerar os números de linha, usando o método write.

    arquivo.write(f'{linha}\n')
arquivo.close() 

# Executar no programa. Se tudo ocorreu bem,nada aparecerá na tela. O programa cria um novo arquivo no diretório atual. Vamos no explorer e vericamos o arquivo criado.

# Abrindo, lendo e fechando um arquivo.

arquivo = open('números.txt', 'r')
for linha in arquivo.readlines():

# Gera uma lista em que cada elemento é uma linha do aruivo.

    print(linha)
arquivo.close() 

# Sempre que manipulamos arquivos, teremos uma abertura, operações e fechamento.
# Apaga o aquivo 'números.txt',e gera um novo arquivo com uma lista de elementos.

# Usando o comando "with", o arquivo é fechado como se tivéssemos chamado o comando "close".
# O uso do "with", também protege o arquivo de exceções que terminariam o nosso programa, protegendo o arquivo dentro do bloco.

with open('números.txt', 'r') as arquivo:
    for linha in arquivo.readlines():
        print(linha)

# Nesse código:

# - O arquivo é aberto implicitamente com with open().
# - O arquivo é lido linha por linha com readlines().
# - O arquivo é fechado automaticamente quando o bloco with é saído.

# Vantagens desse código:

# - Segurança: O arquivo é fechado automaticamente, mesmo que ocorra um erro.
# - Concisão: O código é mais conciso e fácil de ler.
# - Melhor prática: O uso de with é considerado uma melhor prática em Python.

# Em resumo, código é mais seguro, conciso e segue as melhores práticas de Python. É recomendado usar with open() em vez de abrir e fechar o arquivo explicitamente.

# Comando básicos de linhas no windows.

# Aqui estão alguns comandos de linha de comando no Windows:

# Comandos Básicos:

# 1. cd: Altera o diretório atual.
# 2. dir: Lista os arquivos e diretórios no diretório atual.
# 3. cls: Limpa a tela do console.
# 4. echo: Exibe uma mensagem na tela.
# 5. help: Exibe ajuda sobre um comando específico.

# Comandos de Arquivos e Diretórios:

# 1. mkdir: Cria um novo diretório.
# 2. rmdir: Deleta um diretório vazio.
# 3. copy: Copia um arquivo.
# 4. move: Move um arquivo.
# 5. rename: Renomeia um arquivo.
# 6. del: Deleta um arquivo.

# Comandos de Rede:

# 1. ipconfig: Exibe as configurações de rede.
# 2. ping: Testa a conectividade com um servidor.
# 3. netstat: Exibe as estatísticas de rede.

# Comandos de Sistema:

# 1. shutdown: Desliga o computador.
# 2. restart: Reinicia o computador.
# 3. tasklist: Exibe a lista de processos em execução.
# 4. taskkill: Mata um processo em execução.

# Comandos de Segurança:

# 1. net user: Gerencia contas de usuário.
# 2. net localgroup: Gerencia grupos locais.
# 3. cacls: Exibe as permissões de acesso a um arquivo ou diretório.

# Comando type:

#- Sintaxe: type [nome_do_arquivo]
#- Descrição: Exibe o conteúdo de um arquivo de texto na tela.
#- Exemplo: type exemplo.txt

# O comando type é útil para visualizar rapidamente o conteúdo de um arquivo de texto sem precisar abrir um editor de texto.

# Vamos criar o diretório pai e filho:

import os

if not os.path.exists('pai'):
    os.mkdir('pai')

if not os.path.exists('pai/filho'):
    os.mkdir('pai/filho')  

# Cria o diretório "pai" e também o diretório "filho" dentro dele:

# Irá listar os diretórios e arquivos dentro do diretório atual, incluindo os diretórios "pai" e "filho" que foram criados.]

import os

if not os.path.exists('pai'):
    os.mkdir('pai')
    print("Diretório 'pai' criado com sucesso!")

if not os.path.exists('pai/filho'):
    os.mkdir('pai/filho')
    print("Diretório 'filho' criado com sucesso dentro do diretório 'pai'!")

print("Diretórios atuais:")
print(os.listdir())

# Diretórios atuais:
# ['.vscode', 'arquivo.txt', 'arquivos.py', 'dicionários.py', 'frutas.txt', 'listas.py', 'matemática.py', 'módulo_os_py', 'números.txt', 'os.py', 'pai', 'poo.py', 'projetos_py', 'recursos_finais.py', 'sets.py', 'strings.py', 'tempCodeRunnerFile.py', 'tempCodeRunnerFile.python', 'tuplas.py'].

# Parâmetros de linha de comando. Escrever programas que podem ser chamados de várias formas diferentes pela linha de comando, mas sem mudar o programa em si.
# Podemos acessar os parâmetros passados ao programa na linha de comando utilizando o módulo sys e trabalhando com listas argv.

import sys   

# O módulo sys fornece acesso a algumas variáveis e funções usadas ou mantidas pelo interpretador Python.

print(f'Números de parâmetros: {len(sys.argv)}')  

# Imprimindo o número de parâmetros:

for n,p in enumerate(sys.argv): 
    
# Imprimindo cada parâmetro.

    print(f'Parâmetro {n} = {p}')

# Aqui, estamos usando a função enumerate() que retorna uma lista de tuplas, onde cada tupla contém o índice e o valor do elemento na lista.
# No caso, estamos enumerando a lista sys.argv e imprimindo cada parâmetro com seu índice correspondente.

# Saída: 

# Números de parâmetros: 1
# Parâmetro 0 = c:\Users\luist\OneDrive\Documentos\curso_python\arquivos.py

# Exemplos opassando argumentos.

# Para passar um argumento para um script Python, você pode usar a linha de comando e adicionar o argumento após o nome do script.

# Exemplo 1: Passando um argumento simples:
# Suponha que você tenha um script chamado ola.py com o seguinte conteúdo:


import sys

print(f'Olá, {sys.argv[1]}!')  

# Argumento [0], 'Olá', adicionamos arg.[1], 'João'

# Para passar o argumento "João" para o script, você pode executar o seguinte comando na linha de comando:

# python ola.py João

# A saída será:

# Olá, João!

# Exemplo 2: Passando múltiplos argumentos:

# Suponha que você tenha um script chamado soma.py com o seguinte conteúdo:

import sys

if len(sys.argv) != 3:
    print("Erro: número de argumentos inválido.")
else:
    try:
        num1 = float(sys.argv[1])
        num2 = float(sys.argv[2])
        print(f'A soma de {num1} e {num2} é {num1 + num2}.')
    except ValueError:
        print("Erro: argumentos não são números.")

# Para passar os argumentos "10" e "20" para o script, você pode executar o seguinte comando na linha de comando:


# python soma.py 10 20

# A saída será:

# A soma de 10.0 e 20.0 é 30.0.

# No exemplo 1, sys.argv[0] é o nome do script (ola.py) e sys.argv[1] é o primeiro argumento passado (João).

# Se você quiser adicionar outro argumento, ele seria sys.argv[2].

# Então, se você executar o comando:

# python ola.py João 30

# E modificar o script para:

import sys

print(f'Olá, {sys.argv[1]}! Você tem {sys.argv[2]} anos.')

# A saída seria:

# Olá, João! Você tem 30 anos.

############################################################################################

# Geração de arquivos.

# Programa que gera dois arquivos com 500 linhas cada, distribuindo os números em pares e ímpares.

with open('ímpares.txt', 'w') as ímpares:
    with open('pares.txt', 'w') as pares:
        for n in range(0,1000):
            if n % 2 == 0:

                pares.write(f"{n}\n") # Incluimos o \n para indicar fim da linha.
                                      # Quando usamos a função print, esta inclui o \n automaticamente, salvo quando passamos o 'end=' como par
            else:

                ímpares.write(f'{n}\n')

# Para gravarmos em arquivos diferentes, utilizamos o if e dois arquivos abertos para escrita.

# with em uma só linha.

with open('ímpares.txt', 'w') as ímpares, open('pares.txt', 'w') as pares:
    for n in range(0,1000):
        if n % 2 == 0:
                pares.write(f"{n}\n")
        else:
                ímpares.write(f'{n}\n')

#######################################################################

# Leitura e escrita.

with open('múltiplos de 4.txt', 'w') as multiplos4:
    with open('pares.txt') as pares:
        for linha in pares.readlines():
            if int(linha) % 4 == 0:
                multiplos4.write(linha)

# Se rodarmos o programa e não deu erro, arquivosd gerados com suceso.

#######################################################################

# Processamento de um arquivo.

# O 1º passo é criarmos um arquivo. Vou cria no explore. Poderia ser criado com Python.
# Arquivo: 'entrada.txt' ou 'arquivo.dat', o importante é o nome do arquivo, e não a extensão do arquivo('txt).

LARGURA = 79

with open('entrada.txt') as entrada:
    for linha in entrada.readlines():
        if linha [0] == ';':
            continue             # Esta linha não deve ser impressa - continue.
        elif linha [0] == '>':
            print(linha[1:].rjust(LARGURA))
        elif linha [0] == '*':
            print(linha[1:].center(LARGURA))
        else:
            print(linha)

# Tem que acrescentar a este código o trecho seginte: with open('entrada.txt', encoding='utf-8') as entrada:

with open('entrada.txt', encoding='utf-8') as entrada:
    for linha in entrada.readlines():
        if linha [0] == ';':
            continue             # Esta linha não deve ser impressa - continue.
        elif linha [0] == '>':
            print(linha[1:].rjust(LARGURA))
        elif linha [0] == '*':
            print(linha[1:].center(LARGURA))
        else:
            print(linha)

#######################################################################

# Exemplo de código para uma agenda de telefones em Python:

class Contato:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone

class Agenda:
    def __init__(self):
        self.contatos = []

    def adicionar_contato(self, nome, telefone):
        contato = Contato(nome, telefone)
        self.contatos.append(contato)
        print(f"Contato {nome} adicionado com sucesso!")

    def remover_contato(self, nome):
        for contato in self.contatos:
            if contato.nome == nome:
                self.contatos.remove(contato)
                print(f"Contato {nome} removido com sucesso!")
                return
        print(f"Contato {nome} não encontrado.")

    def buscar_contato(self, nome):
        for contato in self.contatos:
            if contato.nome == nome:
                print(f"Contato {nome} encontrado:")
                print(f"Telefone: {contato.telefone}")
                return
        print(f"Contato {nome} não encontrado.")

    def listar_contatos(self):
        print("Contatos:")
        for contato in self.contatos:
            print(f"{contato.nome}: {contato.telefone}")

def main():
    agenda = Agenda()

    while True:
        print("1. Adicionar contato")
        print("2. Remover contato")
        print("3. Buscar contato")
        print("4. Listar contatos")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Digite o nome do contato: ")
            telefone = input("Digite o telefone do contato: ")
            agenda.adicionar_contato(nome, telefone)
        elif opcao == "2":
            nome = input("Digite o nome do contato a remover: ")
            agenda.remover_contato(nome)
        elif opcao == "3":
            nome = input("Digite o nome do contato a buscar: ")
            agenda.buscar_contato(nome)
        elif opcao == "4":
            agenda.listar_contatos()
        elif opcao == "5":
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()

#######################################################################

# Geração de HTML5 - Criação de uma página inicial em Python.

with open('página.html', 'w', encoding='utf-8') as página:
    página.write('<!DOCTYPE html>\n')
    página.write('<html lang=\'pt-BR\'>\n')
    página.write('<head>\n')
    página.write('meta charset=\'utf-8\'>\n')
    página.write('<title>Título da página</title>\n')
    página.write('</head>\n')
    página.write('<body>\n')
    página.write('Olá mundo!')
    for linha in range(10):
        página.write(f'<p>{linha}</p>\n')
    página.write('</body>\n')
    página.write('</html>\n')

# O conteúdo inclui:

# - Um cabeçalho (head) com meta informações, como o conjunto de caracteres (UTF-8) e o título da página.
# - Um corpo (body) com um parágrafo que exibe a mensagem "Olá mundo!".
# - Um loop que escreve 10 parágrafos numerados.

# Para ver o resultado completo, você precisa abrir o arquivo página.html (ou renomeá-lo para index.html) em um navegador, como Google Chrome, Mozilla Firefox, etc.

# Isso ocorre porque o código Python está gerando um arquivo HTML, que precisa ser interpretado por um navegador para ser exibido corretamente.

# Se você executar o código Python novamente, ele irá substituir o conteúdo do arquivo página.html pelo novo conteúdo.

# Para ver o resultado, siga os passos:

# 1. Execute o código Python para gerar o arquivo página.html.
# 2. Abra o arquivo página.html em um navegador.
# 3. Você deve ver a página com o título "Título da página" e o conteúdo "Olá mundo!" seguido da lista numerada de 0 a 9.

# Se você quiser executar o código Python e ver o resultado sem precisar abrir o arquivo em um navegador, você pode usar a biblioteca webbrowser para abrir o arquivo automaticamente após a execução do código.

# Aqui está um exemplo:


# import webbrowser

# ... (código para gerar o arquivo página.html)

# webbrowser.open('página.html')

#######################################################################

# Python oferece recursos mais interesantes para trabalhar com strings , como aspas triplas que permitem escrever longos textos mais facilmente.

with open('página.html', 'w', encoding='utf-8') as página:
    página.write("""
<!DOCTYPE html>
<html lang="pt-BR>
<head>
<meta charset="utf-8">
<title>Título da Página</title>
</head>
<body>
Olá mundo tão desigual, uma loucura Total, cada um pensando "só em si", ou nos iguais!""")
    for linha in range(10):
        página.write(f'<p>{linha}</p>\n')
    página.write("""
</body>
</html>""")
    
# Geração de uma página web a partir de um dicionário.

filmes = {
    'drama': ['Cidadão kane', 'O Poderoso Chefão'],
    'comédia': ['Tempos Modernos', 'América Pie', 'Dr. Dollitle'],
    'policial': ['Chuva Negra', 'Desejo de Matar', 'Dfícil de Matar'],
    'guerra': ['Rambo','Platon', 'Tora!Tora!Tora!']
}

with open('filmes.html', 'w', encoding='utf-8') as página:
    página.write("""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<title>Filmes</title>
</head>
<body>""")
    for c, v in filmes.items():
        página.write(f'<h1>{c}</h1>\n')
        for e in v:
            página.write(f'<h2>{e}</h2>\n')
    página.write("""</body>
</html>""")
    
###########################################################################################################

# Arquivos e diretórios - como aprendemos a ler, criar e alterar arquivos, vamos aprender a listá-los, manipular diretórios, verificar o tamanho e a data de criação de arquivos em ddisco. Para isso precisamos que os programas saibam de onde estão sendo executados, ou seja, qual o diretório corrente. Utilizaremos a função: getcwd ( pegue o diretório atual, do módulo "os" para obter esse valor):

# Usar os comandos:

#>>> import os
#>>> os.getcwd()

# Podemos criar as pastas a,b,c e d usando o windows Explorer. oFinder ou outro utilitário.

# import os

# # Criar diretórios:

# os.mkdir('a')
# os.mkdir('b')
# os.mkdir('c')

# # Trocar de diretório:

# os.chdir('a')

# # Verificar o diretório atual:
# print(os.getcwd())

# # Voltar ao diretório anterior:

# os.chdir('..')

# # Verificar o diretório atual:

# print(os.getcwd())

# import os
# os.getcwd()
# print("Diretório atual:", os.getcwd())  # Saída: Diretório atual: C:\Users\luist\OneDrive\Documentos\curso_python

# try:
#     os.mkdir('a')
#     print("Diretório 'a' criado com sucesso!")
# except FileExistsError:
#     print("Diretório 'a' já existe!")

import os

diretorios = ['a', 'b', 'c', 'd', 'e', 'f']

for diretorio in diretorios:
    if not os.path.exists(diretorio):
        os.mkdir(diretorio)

print(os.getcwd())

# Para imprimir apenas os arquivos (e não os diretórios), você pode usar a função os.path.isfile():
import os

for item in os.listdir():
    if os.path.isfile(item): 
        print(item)

# Para imprimir apenas os diretórios, você pode usar a função os.path.isdir():

import os

for item in os.listdir():
    if os.path.isdir(item):
        print(item)


# Os diretórios são:

# 1. a
# 2. b
# 3. c
# 4. d
# 5. e
# 6. f
# 7. pai
# 8. projetos_py

# Esses são os diretórios listados no diretório atual:


# C:\Users\luist\OneDrive\Documentos\curso_python


# Os outros itens listados são arquivos, como:

# - arquivo.txt
# - arquivos.py
# - controle_agenda_telefone.py
# - dicionários.py
# - entrada.txt
# - filmes.html
# - frutas.txt
# - listas.py
# - matemática.py
# - módulo_os_py
# - múltiplos de 4.txt
# - números.txt
# - ola.html
# - os.py
# - pares.txt
# - poo.py
# - página.html
# - recursos_finais.py
# - sets.py
# - strings.py
# - tempCodeRunnerFile.py
# - tempCodeRunnerFile.python
# - tuplas.py
# - ímpares.txt

# import os
# os.makedirs('Avô/pai/filho')  
# os.makedirs('Avô/mãe/filha') # Abrir o Explorer do windows pra vê os diretórios criados.

# A função mkedir cria apenas um diretório de cada vez. Se precisar criar um diretório, sabendo ou não se os superiores foram criados, use a função makedirs, que cria todos os diretórios intermediários de uma só vez.

# Podemos mudar o nome de um diretório ou arquivo, ou seja, renomeá-los.

# import os
# os.mkdir("Teste")
# os.rename("Teste", "novo_teste") # Mudar o nome, ou seja, renomeà-lo.
# os.makedirs('Avô/pai/filho') # Criando diretórios.
# os.makedirs('Avô/mãe/filho') 
# os.rename('Avô/pai/filho') # Rename também pode ser utilizado para mover arquivos.

# # Criar um arquivo e o fecha imediatamente.

# open('moribundo.txt', 'w').close() # Criando um arquivo.
# os.mkdir('vago') # Cria o diretório.
# os.rmdir('vago') # Apaga o diretório.
# os.remove('moribundo.txt') # Apaga um arquivo.



# Aqui está uma representação em fluxograma da estrutura de diretórios:


#                                       +---------------+
#                                       |  Avô (C:)    |
#                                       +---------------+
#                                              |
#                                              |
#                                              v
#                                       +---------------+
#                                       |  Pai (Users)  |
#                                       +---------------+
#                                              |
#                                              |
#                                              v
#                                       +---------------+
#                                       |  Mãe (luist)  |
#                                       +---------------+
#                                              |
#                                              |
#                                              v
#                                       +---------------+
#                                       |  Filho (OneDrive)|
#                                       +---------------+
#                                              |
#                                              |
#                                              v
#                                       +---------------+
#                                       |  Filha (Documentos)|
#                                       +---------------+
#                                              |
#                                              |
#                                              v
#                                       +---------------+
#                                       |  Neto (curso_python)|
#                                       +---------------+
#                                              |
#                                              |
#                                              v
#                                       +---------------+
#                                       |  Bisnetos (a, b, c, ...)|
#                                       +---------------+


# Nesse fluxograma:

# - O "Avô" é o diretório raiz (C:).
# - O "Pai" é o diretório "Users".
# - A "Mãe" é o diretório "luist".
# - O "Filho" é o diretório "OneDrive".
# - A "Filha" é o diretório "Documentos".
# - O "Neto" é o diretório "curso_python".
# - Os "Bisnetos" são os diretórios "a", "b", "c", etc. dentro de "curso_python".

# Podemos solicitar uma listagem de todos os arquivos e diretórios usando a função listdir.

import os
print(os.listdir('.')) # O ponto . significa o diretório atual.
print(os.listdir('Avô'))
print(os.listdir('Avô/Pai'))
print(os.listdir('Avô/Mãe'))

#######################################################################################

# Módulo os.path - traz várias outras funções que vvamos utilizar para obter mais informações sobre arquivos em disco.

import os
import os.path
for a in os.listdir('.'):
    if os.path.isdir(a):
        print(f'{a}/')
    elif os.path.isfile(a):
        print(a)

# Verificação se é um diretório ou arquivo já existe.

import os.path
if os.path.exists('z'):
    print('Odiretório z existe.')
else:
    print('O diretório não existe.')

# Verificação se um diretório ou arquivo existe.

import os.path
if os.path.exists('matemática.py'):
    print('O diretório matemática.py existe!')
else:
    print('O diretório matemática não existe!')

# # Verificação se um diretório ou um arquivo.

import os

caminho = r'C:\Users\luist\OneDrive\Documentos\curso_python'

if os.path.isdir(caminho):
    print(f'{caminho} é um diretório.')
elif os.path.isfile(caminho):
    print(f'{caminho} é um arquivo.')
else:
    print(f'{caminho} não é um diretório ou arquivo.')

# o Python está procurando o diretório "curso_python" no diretório atual do script, e não no diretório raiz do sistema.

# Se você quiser verificar se o diretório "curso_python" existe no diretório "C:\Users\luist\OneDrive\Documentos\cuurso_python", você precisa fornecer o caminho completo:

import os

caminho = r'C:\Users\luist\OneDrive\Documentos\curso_python'

if os.path.isdir(caminho):
    print(f'{caminho} é um diretório.')
elif os.path.isfile(caminho):
    print(f'{caminho} é um arquivo.')
else:
    print(f'{caminho} não é um diretório ou arquivo.')

# Usando True e False para verificar se um caminho é um diretório ou arquivo.


import os

caminho = r'C:\Users\luist\OneDrive\Documentos\curso_python'

diretorio = os.path.isdir(caminho)
arquivo = os.path.isfile(caminho)

print(f'Diretório: {diretorio}')
print(f'Arquivo: {arquivo}')

# Propriedades de um arquivo.

import os
import os.path
import time
import sys

nome = sys.argv[0]

print(f'Nome : {nome}')
print(f'Tamanho : {os.path.getsize(nome)}')
print(f'Criado : {time.ctime(os.path.getctime(nome))}')
print(f'Modificado : {time.ctime(os.path.getmtime(nome))}')
print(f'Acessado : {time.ctime(os.path.getatime(nome))}')

# Um pouco sobre o tempo - o módulo 'time' traz várias funções para manipular o tempo. Uma delas foi apresentatada na seção anterior: 'time.ctime', que converte um valor em segundos após 01/07/1970 em strig. Temos também a função 'gmtime' que retorna uma tupla com componentes do tempos eparados em elementos.

import time
agora = time.time()
agora

# Saida: 
# Tamanho : 29935
# Criado : Sat Mar  1 17:15:00 2025
# Modificado : Tue Mar  4 07:16:59 2025
# Acessado : Tue Mar  4 07:17:06 2025

time.ctime(agora)

# Saída:
# Tamanho : 30097
# Criado : Sat Mar  1 17:15:00 2025
# Modificado : Tue Mar  4 07:20:05 2025
# Acessado : Tue Mar  4 07:20:07 2025

agora2 = time.localtime()
agora2

# Saída:
# Tamanho : 30097
# Criado : Sat Mar  1 17:15:00 2025
# Modificado : Tue Mar  4 07:20:05 2025
# Acessado : Tue Mar  4 07:20:07 2025

time.gmtime(agora)

# Saída:
# Tamanho : 30456
# Criado : Sat Mar  1 17:15:00 2025
# Modificado : Tue Mar  4 07:24:57 2025
# Acessado : Tue Mar  4 07:25:50 2025

# Elementos da tupla retornada por gmtime():

# 1. tm_year: O ano (por exemplo, 2025).
# 2. tm_mon: O mês (por exemplo, 3 para março).
# 3. tm_mday: O dia do mês (por exemplo, 4).
# 4. tm_hour: A hora (por exemplo, 12).
# 5. tm_min: O minuto (por exemplo, 30).
# 6. tm_sec: O segundo (por exemplo, 0).
# 7. tm_wday: O dia da semana (por exemplo, 0 para segunda-feira).
# 8. tm_yday: O dia do ano (por exemplo, 64).
# 9. tm_isdst: Um valor que indica se o horário de verão está em vigor (por exemplo, 0 para não ou 1 para sim.

# Exibindo os componentes da data e hora.

# agora = time.localtime()
# print(f'Ano: {agora.tm_year}')
# print(f'Mês: {agora.tm_mon}')
# print(f'Dia: {agora.tm_mday}')
# print(f'Hora: {agora.tm_hour}')
# print(f'Minuto: {agora.tm_min}')
# print(f'Segundo: {agora.tm_sec}')
# print(f'Dia da semana: {agora.tm_wday}')
# print(f'Dia do ano: {agora.tm_yday}')
# print(f'Horário de verão: {agora.tm_isdst}')

# Saídda:
# Ano: 2025
# Mês: 3
# Dia: 4
# Hora: 7
# Minuto: 42
# Segundo: 49
# Dia da semana: 1
# Dia do ano: 63
# Horário de verão: 0

# Códigos de formatação de strtime:

# Códigos de formatação mais comuns usados com a função strftime():

# Data
# - %Y: Ano com quatro dígitos (por exemplo, 2025)
# - %y: Ano com dois dígitos (por exemplo, 25)
# - %m: Mês como um número inteiro (por exemplo, 03)
# - %b: Mês abreviado (por exemplo, Mar)
# - %B: Mês completo (por exemplo, Março)
# - %d: Dia do mês como um número inteiro (por exemplo, 04)
# - %j: Dia do ano como um número inteiro (por exemplo, 064)

# Hora
# - %H: Hora em formato 24 horas (por exemplo, 14)
# - %I: Hora em formato 12 horas (por exemplo, 02)
# - %p: AM/PM
# - %M: Minuto como um número inteiro (por exemplo, 30)
# - %S: Segundo como um número inteiro (por exemplo, 00)
# - %f: Microsegundos como um número inteiro (por exemplo, 000000)

# Dia da Semana
# - %w: Dia da semana como um número inteiro (por exemplo, 1)
# - %a: Dia da semana abreviado (por exemplo, Seg)
# - %A: Dia da semana completo (por exemplo, Segunda-feira)

# Outros
# - %c: Data e hora completa (por exemplo, Seg 04 Mar 2025 14:30:00)
# - %x: Data completa (por exemplo, 04/03/2025)
# - %X: Hora completa (por exemplo, 14:30:00)
# - %%: Caractere de porcentagem literal (por exemplo, %).

import time
agora = time.localtime()
print(time.strftime('%a %d/%m/%y %H:%M', agora))

# Saída:

# Tue 04/03/25 07:57

print(time.strftime('Hoje é o %j dia do ano de %Y', agora))

# Hoje é o 063 dia do ano de 2025

print(time.strftime('%b %d/%m/%y %H:%M', agora))

# Mar 04/03/25 08:06

# Se precisar converter uma tupla em segundos, utilize a função "timegm"  do módulo calendar.

import calendar

# Tue 04/03/25 08:16
# Hoje é o 063 dia do ano de 2025
# Mar 04/03/25 08:16

import time
data_hora = time.localtime()
print(data_hora)

# Saída:

# time.struct_time(tm_year=2025, tm_mon=3, tm_mday=4, tm_hour=8, tm_min=19, tm_sec=9, tm_wday=1, tm_yday=63, tm_isdst=0).

# Usos de caminhos.

# import os.path
# caminho = 'i/j/k'
# os.path.abspath(caminho)
# print(os.path.abspath(caminho)) # C:\Users\luist\OneDrive\Documentos\curso_python\i\j\k
# os.path.basename(caminho)
# os.path.dirname(caminho)
# os.path.split(caminho)
# os.path.splitext('arquivo.txt')
# os.path.splitdrive('C:/Windows')

# import os.path
# os.path.join("C:", "Ddados", "programas")

#######################################################################

# Pathlib - outra forma de navegar nos diretórios e arquivos com um programa em Python utilizando a pathlib.É a forma mais moderna e orientada a objetos. A pathlib não considera os caminhos como strings, mas como objetos que podem ser manipulados e combinados.

import pathlib
from pathlib import Path
caminho = Path('C:/Users/luist/OneDrive/Documentos/curso_python313')
caminho          # C:\Users\luist\OneDrive\Documentos\curso_python313.

caminho = Path('C:/Users/luist/OneDrive/Documentos/curso_python313')
print(caminho.exists())  # True
print(caminho.is_dir())   # True
print(caminho.is_file())   # False

caminho = Path('C:/Users/luist/OneDrive/Documentos/curso_python313')
caminho_pai = caminho/ "pai"
caminho_pai


# Para executar o comando como administrador no Windows 10/11, basta:

# 1. Clique com o botão direito no ícone do PowerShell ou do Prompt de Comando no menu Iniciar.
# 2. Selecione "Executar como administrador".
# 3. Confirme que deseja executar o comando como administrador.

# Um recurso interessante de Path é que eles podem ser combinados mais facilmente que com strigs.

import pathlib
from pathlib import Path
caminho = Path('C:/Users/luist/OneDrive/Documentos/curso_python313')
caminho          # C:\Users\luist\OneDrive\Documentos\curso_python313.

caminho = Path('C:/Users/luist/OneDrive/Documentos/curso_python313')
print(caminho.exists())  # True
print(caminho.is_dir())   # True
print(caminho.is_file())   # False

# ('C:\\', 'Users', 'luist', 'OneDrive', 'Documentos', 'curso_python313', 'pai')
# Essa tupla contém cada parte do caminho, desde a raiz (C:\\) até o último diretório (pai).

# O objeto caminho_pai representa o caminho para o diretório "pai" dentro do diretório curso_python313, que é:
# C:\Users\luist\OneDrive\Documentos\curso_python313\pai 

caminho = Path('C:/Users/luist/OneDrive/Documentos/curso_python313')
caminho_pai = caminho/ "pai"
caminho_pai
print(caminho_pai)
caminho_pai.parts
print(caminho_pai.parts) 
caminho_pai.drive  
print(caminho_pai.drive)  # 'c:' - # No Windows, podemos usar a propriedade drive para exibir apenas a letra do disco.
str(caminho_pai)   # Um objeto path pode ser transformado em string usandddo a fução str.
print(caminho_pai) # C:\Users\luist\OneDrive\Documentos\curso_python313\pai
caminho = Path('C:/Users/luist/OneDrive/Documentos/curso_python313')
caminho.is_file()
print(caminho.is_file())   # False. A pathlib também pode ser usado com arquivos.

# Comando suffix utilizado para arquivos:

caminho.suffix
print(caminho.suffix) 

# O atributo suffix do objeto Path retorna a extensão do arquivo. No entanto, como o caminho aponta para um diretório (curso_python313), não há uma extensão de arquivo para retornar. Quando se trabalha com diretórios, o suffix geralmente retorna uma string vazia (''), pois diretórios não têm extensões.

# Tecnicamente, o suffix pode ser usado com qualquer objeto Path, independentemente de ser um arquivo ou diretório. Se você tiver um objeto Path que aponta para um arquivo, o suffix retornará a extensão do arquivo.

caminho =Path('/tmp/arquivo.txt.gz')
caminho.suffix
print(caminho.suffixes)  # ['.txt', '.gz']

# O arquivo tem duas extensões: .txt e .gz.
# A extensão .txt indica que o arquivo é um texto.
# A extensão .gz indica que o arquivo foi compactado usando o algoritmo de compactação Gzip.
# Então, o arquivo arquivo.txt.gz é um arquivo de texto que foi compactado usando Gzip.
# A ordem das extensões é importante:
# - .txt indica o tipo de arquivo (texto)
# - .gz indica que o arquivo foi compactado

# Gzip é um algoritmo de compactação de dados sem perda, amplamente utilizado para reduzir o tamanho de arquivos e facilitar a transferência de dados.
# Gzip é especialmente útil para:
# - Compactar arquivos de texto, como logs, documentos e código-fonte
# - Reduzir o tamanho de arquivos de dados, como imagens e áudio
# - Aumentar a velocidade de transferência de dados pela internet
# Gzip é um algoritmo de compactação lossless, o que significa que os dados compactados podem ser restaurados para o seu estado original sem perda de informações.

# Usando o pathlib para mudar o nome de um arquivo:

# import pathlib

# arquivo = pathlib.Path('arquivo_velho.txt') # Cria um arquivo para depois renomeá-lo .  
# arquivo.touch()   # Cria o 'arquivo_velho.txt'.
 
# if arquivo.exists():  # Verifique se o arquivo existe.
#     novo_nome = arquivo.rename('arquivo_novo.txt')  # Renomeie o arquivo.
#     print(f"Arquivo renomeado para {novo_nome}")
# else:
#     print("Arquivo não encontrado")
    
# Serve também para mudar a extnsão do arquivo(no objeto, não no disco):

arquivo = pathlib.Path('arquivo_novo.txt')
novo_arquivo = arquivo.with_suffix('.zp')
print(novo_arquivo)  # Saída: arquivo_novo.zp.

# O Path também pode ser usada para abrir arquivos:

with Path('arquivo.txt').open() as f:
    print(f.read) # <built-in method read of _io.TextIOWrapper object at 0x000001710FEB6420>.

with Path('arquivo.txt').open(encoding='utf-8') as f:
    print(f.read())  

# Bóson Trinamentos
# Como criar um arquivo de texto com Python.
# Python é usado em ciências de dados extensivamente.

#######################################################################

# Para executar o comando como administrador no Windows 10/11, basta:

# 1. Clique com o botão direito no ícone do PowerShell ou do Prompt de Comando no menu Iniciar.
# 2. Selecione "Executar como administrador".
# 3. Confirme que deseja executar o comando como administrador.

#######################################################################

# Visita a todos os diretórios recursivamente

import os

caminho = r'C:\Users\luist\OneDrive\Documentos\curso_python313'

for raiz, diretórios, arquivos in os.walk(caminho):
    print('\ncaminho:', raiz)
    print('Diretórios:', diretórios)
    print('Arquivos:', arquivos)
    for d in diretórios:
        print(f' {d}/')
    for f in arquivos:
        print(f' {f}')
    print(f'{len(diretórios)} diretório(s), {len(arquivos)} arquivo(s)')

# Saída:

# caminho: C:\Users\luist\OneDrive\Documentos\curso_python313
# Diretórios: ['.vscode', 'a', 'Avô', 'b', 'c', 'd', 'e', 'f', 'novo_teste', 'pai', 'projetos_py', 'Teste']
# Arquivos: ['arquivo.txt', 'arquivos.py', 'arquivo_novo.txt', 'arquivo_velho.txt', 'controle_agenda_telefone.py', 'dicionários.py', 'entrada.txt', 'filmes.html', 'frutas.txt', 'listas.py', 'matemática.py', 'módulo_os.py', 'múltiplos de 4.txt', 'números.txt', 'ola.html', 'os.py', 'pares.txt', 'poo.py', 'página.html', 'recursos_finais.py', 'sets.py', 'strings.py', 'tempCodeRunnerFile.py', 'tempCodeRunnerFile.python', 'teste_programas.py', 'tuplas.py', 'ímpares.txt']
#  .vscode/
#  a/
#  Avô/
#  b/
#  c/
#  d/
#  e/
#  f/
#  novo_teste/
#  pai/
#  projetos_py/
#  Teste/
#  arquivo.txt
#  arquivos.py
#  arquivo_novo.txt
#  arquivo_velho.txt
#  controle_agenda_telefone.py
#  dicionários.py
#  entrada.txt
#  filmes.html
#  frutas.txt
#  listas.py
#  matemática.py
#  módulo_os.py
#  múltiplos de 4.txt
#  números.txt
#  ola.html
#  os.py
#  pares.txt
#  poo.py
#  página.html
#  recursos_finais.py
#  sets.py
#  strings.py
#  tempCodeRunnerFile.py
#  tempCodeRunnerFile.python
#  teste_programas.py
#  tuplas.py
#  ímpares.txt
# 12 diretório(s), 27 arquivo(s)

# caminho: C:\Users\luist\OneDrive\Documentos\curso_python313\.vscode
# Diretórios: []
# Arquivos: ['settings.json']
#  settings.json
# 0 diretório(s), 1 arquivo(s)

# caminho: C:\Users\luist\OneDrive\Documentos\curso_python313\a
# Diretórios: []
# Arquivos: []
# 0 diretório(s), 0 arquivo(s)

# caminho: C:\Users\luist\OneDrive\Documentos\curso_python313\Avô
# Diretórios: ['mãe', 'pai']
# Arquivos: []
#  mãe/
#  pai/
# 2 diretório(s), 0 arquivo(s)

# caminho: C:\Users\luist\OneDrive\Documentos\curso_python313\Avô\mãe
# Diretórios: ['filha']
# Arquivos: []
#  filha/
# 1 diretório(s), 0 arquivo(s)

# caminho: C:\Users\luist\OneDrive\Documentos\curso_python313\Avô\mãe\filha
# Diretórios: []
# Arquivos: []
# 0 diretório(s), 0 arquivo(s)

# caminho: C:\Users\luist\OneDrive\Documentos\curso_python313\Avô\pai
# Diretórios: ['filho']
# Arquivos: []
#  filho/
# 1 diretório(s), 0 arquivo(s)

# caminho: C:\Users\luist\OneDrive\Documentos\curso_python313\Avô\pai\filho
# Diretórios: []
# Arquivos: []
# 0 diretório(s), 0 arquivo(s)

# caminho: C:\Users\luist\OneDrive\Documentos\curso_python313\b
# Diretórios: []
# Arquivos: []
# 0 diretório(s), 0 arquivo(s)

# caminho: C:\Users\luist\OneDrive\Documentos\curso_python313\c
# Diretórios: []
# Arquivos: []
# 0 diretório(s), 0 arquivo(s)

# caminho: C:\Users\luist\OneDrive\Documentos\curso_python313\d
# Diretórios: []
# Arquivos: []
# 0 diretório(s), 0 arquivo(s)

# caminho: C:\Users\luist\OneDrive\Documentos\curso_python313\e
# Diretórios: []
# Arquivos: []
# 0 diretório(s), 0 arquivo(s)

# caminho: C:\Users\luist\OneDrive\Documentos\curso_python313\f
# Diretórios: []
# Arquivos: []
# 0 diretório(s), 0 arquivo(s)

# caminho: C:\Users\luist\OneDrive\Documentos\curso_python313\novo_teste
# Diretórios: []
# Arquivos: []
# 0 diretório(s), 0 arquivo(s)

# caminho: C:\Users\luist\OneDrive\Documentos\curso_python313\pai
# Diretórios: ['filho']
# Arquivos: []
#  filho/
# 1 diretório(s), 0 arquivo(s)

# caminho: C:\Users\luist\OneDrive\Documentos\curso_python313\pai\filho
# Diretórios: []
# Arquivos: []
# 0 diretório(s), 0 arquivo(s)

# caminho: C:\Users\luist\OneDrive\Documentos\curso_python313\projetos_py
# Diretórios: []
# Arquivos: []
# 0 diretório(s), 0 arquivo(s)

# caminho: C:\Users\luist\OneDrive\Documentos\curso_python313\Teste
# Diretórios: []
# Arquivos: []
# 0 diretório(s), 0 arquivo(s)

# O código está funcionando corretamente e listando todos os diretórios e arquivos dentro do caminho especificado.

# Você pode ver que o código está mostrando:

# - O caminho atual
# - Os diretórios dentro do caminho atual
# - Os arquivos dentro do caminho atual
# - O número de diretórios e arquivos dentro do caminho atual

# O código também está recursivamente listando os diretórios e arquivos dentro dos subdiretórios.

# Data e hora.

from datetime import date, time, datetime, timedelta

# Criar uma data.

data_atual = date.today()
print(data_atual)

# Criar uma hora.

hora_atual = time(12, 30, 0)
print(hora_atual)

# Criar uma data e hora.

data_hora_atual = datetime.now()
print(data_hora_atual)

# Somar um intervalo de tempo.

data_hora_futura = data_hora_atual + timedelta(days=30)
print(data_hora_futura)

# Formatar uma data e hora.

data_hora_formatada = data_hora_atual.strftime("%d/%m/%Y %H:%M:%S")
print(data_hora_formatada)

# 04/03/2025 14:49:33

from datetime import date, datetime # Criar uma data

data_atual = date.today()
print("Dia:", data_atual.day)
print("Mês:", data_atual.month)
print("Ano:", data_atual.year)

# Dia: 4
# Mês: 3
# Ano: 2025

# Formatar a hora, minuto, segundo e microssegundos:

from datetime import datetime

data_hora_atual = datetime.now()
data_hora_formatada = data_hora_atual.strftime("%d/%m/%Y %H:%M:%S.%f")
print("Data e hora formatada:", data_hora_formatada)

# Data e hora formatada: 04/03/2025 15:09:26.819369

# O tipo datetime permite permite acessar a hora, minutos, segundos e os microssegundos, idependetemente.

from datetime import datetime

momento = datetime.now()

print("Hora:", momento.hour)
print("Minuto:", momento.minute)
print("Segundo:", momento.second)
print("Microssegundo:", momento.microsecond)

# Hora: 15
# Minuto: 17
# Segundo: 2
# Microssegundo: 992440

# Dia da semana:

from datetime import datetime

momento = datetime.now()
dia_semana = momento.weekday()

print("Dia da semana:", dia_semana) # Dia da semana: 1

# O weekday() retorna um número inteiro que representa o dia da semana, onde:

# - 0 = Segunda-feira
# - 1 = Terça-feira
# - 2 = Quarta-feira
# - 3 = Quinta-feira
# - 4 = Sexta-feira
# - 5 = Sábado
# - 6 = Domingo

# Para obter um valor mais compatível com o que usamos no Brasil:

from datetime import datetime

momento = datetime.now()
dia_semana = momento.isoweekday()

print("Dia da semana:", dia_semana)  # Dia da semana: 2

# A saída será um número inteiro entre 1 e 7, representando o dia da semana:

# - 1 = Segunda-feira
# - 2 = Terça-feira
# - 3 = Quarta-feira
# - 4 = Quinta-feira
# - 5 = Sexta-feira
# - 6 = Sábado
# - 7 = Domingo

from datetime import datetime

momento = datetime.now()
data_hora_iso = momento.isoformat()

print("Data e hora ISO:", data_hora_iso)

# Data e hora ISO: 2025-03-04T15:34:24.804196.
# Esse código usa o método isoformat() da classe datetime para converter a data e hora atual em uma string no formato ISO 8601, muito utilizada na web e principalmente para converter data e hora em string que retorna numa string no formato ISO8601.

from datetime import datetime

momento = datetime.now()
data_hora_iso = momento.isoformat()

print("Data e hora atual ISO:", data_hora_iso)

# Data e hora atual ISO: 2025-03-04T15:44:20.508749.

from datetime import datetime

ano = 202
mes = 3
dia = 4  

momento = datetime(ano, mes, dia)
data_hora_iso = momento.isoformat()
print("Data e hora ISO:", data_hora_iso)

# Data e hora atual ISO: 2025-03-04T15:46:55.299952
# Data e hora ISO: 0202-03-04T00:00:00

from datetime import datetime

# Esse código criará um objeto datetime com a data de 31 de dezembro de 2030 e a converterá para o formato ISO 8601.

ano = 2030
mes = 12
dia = 31

momento = datetime(ano, mes, dia)
data_iso = momento.date().isoformat()
print("Data futura ISO:", data_hora_iso)

from datetime import datetime

# Data e hora atual
momento = datetime.now()
data_hora_iso = momento.isoformat()
print("Data e hora atual ISO:", data_hora_iso)

# Data futura.

ano = 2030
mes = 12
dia = 31
momento_futuro = datetime(ano, mes, dia)
data_futura_iso = momento_futuro.isoformat()
print("Data futura ISO:", data_futura_iso)

# Data e hora atual ISO: 2025-03-04T15:54:03.586337
# Data futura ISO: 2030-12-31T00:00:00

momento -= timedelta(minutes=30)
print("Data e hora após subtrair 30 minutos ISO:", momento.isoformat())

# Data e hora atual ISO: 2025-03-04T15:58:52.000649
# Data futura ISO: 2030-12-31T00:00:00
# Data e hora após subtrair 30 minutos ISO: 2025-03-04T15:28:52.000649

from datetime import datetime as dt
print(datetime.now())

# 2025-03-04 16:04:36.295906

from datetime import datetime

agora = datetime.now()
tupla_data_hora = (agora.year, agora.month, agora.day, agora.hour, agora.minute, agora.second, agora.microsecond)
print(tupla_data_hora)

# 2025-03-04 16:11:33.707084
# (2025, 3, 4, 16, 11, 33, 707247)

# Fusos horários:


from datetime import datetime
import pytz

nova_iorque = pytz.timezone("America/New_York")
sao_paulo = pytz.timezone("America/Sao_Paulo")
tokio = pytz.timezone("Asia/Tokyo")
brasília = pytz.timezone("America/Sao_Paulo")
recife = pytz.timezone("America/Recife")
rio_branco = pytz.timezone("America/Rio_Branco")

agora = datetime.now(pytz.utc)

print("Agora em:")
print("Nova Iorque ", agora.astimezone(nova_iorque))
print("São Paulo ", agora.astimezone(sao_paulo))
print("Tóquio ", agora.astimezone(tokio))
print("Brasília ", agora.astimezone(brasília))
print("Recife ", agora.astimezone(recife))
print("Rio Branco ", agora.astimezone(rio_branco))

# Agora em:
# Nova Iorque  2025-03-04 16:03:07.366257-05:00
# São Paulo  2025-03-04 18:03:07.366257-03:00
# Tóquio  2025-03-05 06:03:07.366257+09:00
# Brasília  2025-03-04 18:03:07.366257-03:00
# Recife  2025-03-04 18:03:07.366257-03:00
# Rio Branco  2025-03-04 16:03:07.366257-05:00

import zoneinfo
for zona in sorted(zoneinfo.available_timezones()):
    print(zona)

#######################################################################

# Arquivos JSON:

# JSON (JavaScript Object Notation) é um formato de arquivo leve e fácil de ler que é usado para armazenar e trocar dados entre sistemas.

# Arquivos JSON são compostos por pares de chave-valor, arrays e objetos, que são facilmente legíveis por humanos e máquinas.

# Aqui estão algumas características principais dos arquivos JSON:

# - Formato de texto simples
# - Fácil de ler e escrever
# - Pode ser usado para armazenar dados estruturados
# - É independente de linguagem de programação

# Arquivos JSON são amplamente usados em:

# - Desenvolvimento web
# - APIs (Application Programming Interfaces)
# - Armazenamento de dados
# - Configuração de aplicativos

# No Python, você pode trabalhar com arquivos JSON usando a biblioteca json, que é incluída na biblioteca padrão do Python.

# Você pode usar a biblioteca json para:

# - Ler e escrever arquivos JSON
# - Converter dados Python para JSON
# - Converter JSON para dados Python

import json

dados = {                  # Dados a serem escritos no arquivo JSON.
    "nome": "João",
    "idade": 30,
    "cidade": "São Paulo"
}

with open("dados.json", "w") as arquivo:  # Escrever os dados no arquivo JSON.
    json.dump(dados, arquivo)

with open("dados.json", "r") as arquivo:  # Ler os dados do arquivo JSON.
    dados_lidos = json.load(arquivo)

print(dados_lidos)   # {'nome': 'João', 'idade': 30, 'cidade': 'São Paulo'}

# - Adicionar mais dados ao dicionário
# - Usar diferentes tipos de dados (como listas ou booleanos)
# - Ler e escrever arquivos JSON mais complexos.

# Lendo um arquivo JSON.

import json
from pathlib import Path
with Path("dados.json").open() as arquivo:
    dados = json.load(arquivo)
print(dados["nome"])
print(dados["valores"])

# Abrindom uma arquivo JSON e usando os dados

import json
from pathlib import Path
with Path("lista.json").open(encoding='utf-8') as arquivo:
    turma = json.load[arquivo]
for aluno in turma:
    print('Nome:', aluno['nome'])
    print('Notas:', aluno['notas'])
    print('Média:', sum(aluno['notas']) / len(aluno['notas']))
    print()

# Criando uma tabela de preço:

import json
from pathlib import Path

tabela_de_preços = {}
print('Criador da tabela de preços')
print('Digite um nome de produto em branco para terminar')

while True:
    produto = input('Nome do produto:')
    if produto.strip() == '':
        break
    preço = input('Preço:')
    tabela_de_preços[produto] = preço

print('\nTabela de Preços:')
for produto, preço in tabela_de_preços.items():
    print(f'{produto}: R${preço}')

with Path('Preços.json').open('w', encoding='utf-8') as arquivo:
    json.dump(tabela_de_preços, arquivo)

#######################################################################

# Arquivos binários:  O código salva a imagem como um arquivo binário no formato BMP, com a extensão ".bin".

from PIL import Image

img = Image.new('RGB', (100, 100))     # Criar uma imagem vazia com 100x100 pixels.
for x in range(100):                   
    for y in range(100):               # Definir os pixels da imagem.
        img.putpixel((x, y), (x, y, 0)) 
img.save('imagem.bin', 'BMP')          

# Salvar a imagem como um arquivo binário.

# Um código Python que utiliza a biblioteca Pillow para criar uma imagem RGB de 100x100 pixels e, em seguida, imprime os valores hexadecimais dos pixels da imagem.

from PIL import Image

img = Image.new('RGB', (100, 100))

for x in range(100):
    for y in range(100):
        img.putpixel((x, y), (x, y, 0))

print("Valores hexadecimais da imagem:")
for x in range(100):
    for y in range(100):
        r, g, b = img.getpixel((x, y))
        hex_valor = f"#{r:02x}{g:02x}{b:02x}"
        print(hex_valor, end=" ")
    print()

# Criando uma imagem em formato binário:

imagem_em_hexa = """
42 4d
46 00 00 00
00 00
00 00 
36 00 00 00
28 00 00 00 
02 00 00 00
02 00 00 00
01 00
18 00
00 00 00 00
10 00 00 00
13 0b 00 00
13 0b 00 00
00 00 00 00
00 00 00 00 
00 00 FF
FF FF FF
00 00
FF 00 00
00 FF 00
00 00"""

imagem_bytes = bytes.fromhex(imagem_em_hexa)

with open('imagem.bmp', 'w') as f:
    f.write(imagem_bytes)

# Para saber onde se encontra o arquivo salvo: 'imagem.bmp'.

import os
print(os.getcwd())

# Um exemplo de código Python que cria um arquivo BMP a partir de um desenho simples:

import struct

ARQUIVO = 'imagem_python.bmp'  # Defina o nome do arquivo.

LARGURA = 256                  # Defina as dimensões da imagem.
ALTURA = 256

cabecalho = struct.pack('BBIIIIII',  # 14 bytes
                           0x42, 0x4d,  # BM
                           LARGURA * ALTURA * 3 + 54,  # tamanho do arquivo
                           54,  # offset para o início da imagem
                           40,  # tamanho do cabeçalho DIB
                           LARGURA, ALTURA, 24)  # planos e bits por pixel
corpo = bytearray()        # Crie o corpo da imagem.
for y in range(ALTURA):
    for x in range(LARGURA):          # Desenhe um quadrado vermelho no centro da imagem
        if 100 <= x <= 156 and 100 <= y <= 156:
            corpo.extend((255, 0, 0))  # vermelho
        else:
            corpo.extend((0, 0, 0))  # preto

with open(ARQUIVO, 'wb') as f:       # Grave o arquivo
    f.write(cabecalho)
    f.write(corpo)

# Este código cria um arquivo BMP chamado imagem_python.bmp com uma imagem de 256x256 pixels, contendo um quadrado vermelho no centro.
# O que é binário?
# O sistema numérico binário  usa o número 2 como sua base (raiz). Como um sistema numérico de base 2, consiste em apenas dois números: 0 e 1. 


# Hex para tabela de conversão binária
# Hex	Binário
# 0  	0
# 1	    1
# 2	    10
# 3  	11
# 4	    100
# 5	    101
# 6	    110
# 7  	111
# 8	   1000
# 9	   1001
# UMA  1010
# B	   1011
# C	   1100
# D	   1101
# E	   1110
# F	   1111
# 10   10.000
# 20   100000
# 40   1000000
# 80   10000000
# 100  100000000

# Programa 9.18: Visualizador de arquivos em formato binário:

import sys
import itertools
def imprime_bytes(imagem, bytes_por_linha=16):
    for b in itertools.batched(imagem, bytes_por_linha):
        hex_view = " ".join([f"{v:02x} for v in b"])
        tview = "".join([chr(v) if chr(v).isprintable() else "." for v in b])
        print(f"{hex_view} {"" * 3 * (bytes_por_linha - len(b))}{tview}")
if __name__ == "__main__":
    with open(sys.argv[1], "rb") as f:
        imagem = f.read( )
    imprime_bytes(imagem)