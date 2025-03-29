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


import webbrowser

... (código para gerar o arquivo página.html)

webbrowser.open('página.html')

########################################################################

Python oferece recursos mais interesantes para trabalhar com strings , como aspas triplas que permitem escrever longos textos mais facilmente.

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
    