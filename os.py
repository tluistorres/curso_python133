import os
os.chdir('C:\\Teste')
print(f'Diretório atual: {os.getcwd()}')

padrão_nome = input('Qual o padrão de nomes de arquivos a usar (sem a extensão)?')

contador = 1
for arq in os.listdir():
    if os.path.isfile(arq):
        nome_arq, exten_arq = os.path.splitext(arq)
        nome_arq = padrão_nome + '' + str(contador)
        nome_novo = f'{nome_arq}{exten_arq}'
        os.rename(arq, nome_novo)

print(f'\nArquivos renomeados.')


        