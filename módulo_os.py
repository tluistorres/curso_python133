# Módulo os.py - gerenciamento de arquivos.
py
import os
os.name               # 'nt'  aparece se for o windowa.
os.getcwd()           # Indica o diretório atual que está aberto.
os.curdir             # O valor de os.curdir é '.', que é o caractere que representa o diretório atual em muitos sistemas operacionais.
                      # print(os.curdir)  # Imprime '.'
print(os.path.join(os.curdir, 'arquivo.txt'))  # Imprime './arquivo.txt'

os.listdir('C:\\')    # Lista meus diretórios para saber o que tem na raiz.
os.chdir('C:\\')      # Mudar de diretório.
os.getcwd()           # Obter o diretório. Raiz do sistema.
os.mkdir('projetos_python')  # os.mkdir(path). Onde path é o caminho do diretório que  você     deseja criar / os.mkdir("/caminho/para/novo_diretorio")
os.listdir()          # Visualiza os diretórios, inclusive o diretório criado.
os.chdir('projetos_python')  # Entra dentro do diretório(pasta) para trabalhar.
                             # - chdir(): é uma função do módulo 'os' que muda o diretório atual para o diretório especifica - 'projetos_python': é o nome do diretório para o qual você deseja mudar.

# Criar pastas fora do diretório atual sem sair 'projetos_python'
os.getcwd()           
pasta_nova = 'projetos_py'
pasta_pai = 'c:\\'

# Vamos juntar o caminho - (path + join). O Python irá criar um caminho completo que une o diretório pai com o diretório ou arquivo novo. Ex:. projetos_python, o caminho_completo será /home/user/projetos_python.

caminho_completo = os.path.join(pasta_pai, pasta_nova)  # 1º pai, 2º pasta a ser adicionada.
print(caminho_completo)    # C:\'projetos_python'
os.mkdir(caminho_completo) # os.mkdir(): é uma função do módulo 'os' que cria um novo diretório.
os.listdir()               # Verifica onde o diretório foi criado.

# Renomear uma pasta.

os.rename('C:\\workspace', 'C:\\projetos_py')  # python renomear_diretorio.py

# Remover uma pasta.

os.rmdir('C:\\workspace\\América')

os.path.basename(os.getcwd())  # Verifica o nome do arquivo a partir do comando completo. 'Teste'
os.path.dirname(os.getcwd())   # Para saber onde está o diretótio ou arquivo. 'C:\\'

# Criar diretórios de forma recursiva - cria vários diretórios dentro de uma pasta.

novas_pastas = 'América\\Brasil\\Alagoas'
caminho = os.path.join(pasta_pai, novas_pastas)
print(caminho)               # C:\Users\luist\OneDrive\Documents\workspace\América\Brasil\Alagoas
os.makedirs(caminho)         # Cria as pastas e verifica no Meu Computador as pastas criadas.
os.path.exists('C:workspace\\América')   # Verifica se o caminho existe.

# Verificação.

os.path.isfile('C:Teste') # True ou False  # Existe a pasta 'Teste' ? Path quer dizer caminho.
os.path.isdir('C;\\Tese') # True ou False.

# Para criar um arquivo por ex dentro do workspace.

manipulador = open('arq.txt', 'x')   # Criar o arquivo.
manipulador.close()                  # Apóa cria o arquivo, fecha.
os.listdir()

# Estudos que servem para excluir arquivos txt, copiar aququivos que são imagens e renomear arquivos em massa. Grandes quantidades.

arquivo = os.path.basename('C\\workspace\\arq.txt') # Como você gravou o arquivo ?
print(arquivo)   # Resposta: arq.txt ou poderia ser também (arq.data).

# Podemos realizar operação em massa dentro de um arquivo, dividindo o nome de sua respectica extensão.

os.path.splitext(arquivo)  # Resposts: ('arq', '.txt') - Divide o nome de sua extenão. Muito útil, muito mesmo. Podemos excluir, criar, renomear os arquivos em massa, utilizando s=este tipo de técnica(splitext). Arwquivos imagens.

# Para remover arquivo.

os.remove('arq.txt')
os.listdir()          # Verifica que foi removido.

# Verificar se uma pasta existe.

os.path.exists('C:\\Teste\\workspace')  # True ou False.

# Verificar se é um diretório.

os.path.isdir('C:\\Teste\\workspace')   # True ou False.

# Verificar se é um arquivo.

os.path.isfile('C:\\Teste\\workspace')  # True ou False.

# Módulo pathlib(Biblioteca)

import pathlib   # Módulo pathlib - https://docs.python.org/3/library/pathlib.html

caminho = pathlib.path()
caminho.cwd()            # windowsPath('C:/workepace') Mostra que estamos nowindows.
                         # É uma biblioteca alaternativa ao os.
os.rmdir('C:\\'Teste')   # Remove o arquivo.
os.listdir()    # Mostra que o arquivo foi removido.


# Módulo shutil(Biblioteca) - https://docs.python.org/3/library/shutil.html
# Caso queira remover em definitivo a pasta.

import shutil
shutil.rmtree('C:\\Teste')  # Cuidado pra não remover pastas que não queira.
os.listdir('C:\\')  # Não vai apoarecer o arquivo 'Teste'.

# Renomear um arquivo dentro de uma pasta. 
# Criar uma pasta teste.
# Novo documento de texto - Mouse Direito - nomear o arquivo abc123 - copia os aqruivo e cola quantas vezes for necessário. Vamos renomear tudo de uma só vez, usando o Python.

*********************************************************************************************

# Crianado programa no scrip em Python para criar e numerar arquivos em massa.

import os

os.chdir('C:\\Teste') # Vamos criar uma pasta no explorer com vários arquivos para seree nomeados. Podemos também criar o arquivo 'Teste' no vScode seguindo os passos anteriores.

#  Criar uma pasta teste.
# Novo documento de texto - Mouse Direito - nomear o arquivo abc123 - copia os aqruivo e cola quantas vezes for necessário. Vamos renomear tudo de uma só vez, usando o Python.

print(f'Diretório atual: {os.getcwd()}')

padrão_nome = input('Qual o padrão de nomes de arquivos a usar (sem etnensão?)')
for contador,arq in enumerate(os.listdir()): # fazer a numeração com um ídice.
    if os.path.isfile(arq):                 # Se for arquivos ? Numerá-los.
        nome_arq, exten_arq = os.path.splitext(arq)# Separar nome da extensão, usando o splitext.
        nome_arq = padrão_nome + '' + str(contador+1) ou seria contador + 1 ?
        nome_novo = f'{nome_arq}{exten_arq}'
        os.rename(arq, nome_novo)    # nome-novo será digitado pelo usuário. Sug. Dados.
print(f'\nArquivos  renomeados.')    # Próximo passo é rodar o script.

#Rodar no Terminal

Diretório atual:C:\Teste
Qual o padrão de nomes de arquivos a usar(sem extensão)? Dados -Enter.
Arquivos renomeados.

# O passo seguinte é verificar como ficou os arquivos renomeaddos.

# Manipulação de arquivos de Textos. Como criar e abri arquivos com Python.

