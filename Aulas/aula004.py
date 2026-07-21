# ============= MANIPULANDO TEXTOS =============
# --> Fatiamento

frase = 'Curso em Vídeo Python'

print(frase[9]) # item que está na posição 9 (começa no 0)
print(frase[9:13]) # itens que começam no 9 e vão até o 13, mas ele não conta, então para no índice 12
print(frase[9:21:2]) # itens que começam no 9, vão até o 20 e pulando de 2 em 2 (step)
print(frase[9::2]) # itens que começam no 9, vão até o final e de 2 em 2

# -> Análise
print(len(frase)) # qual o comprimento do que está na frase, nesse caso mostra 21
print(frase.count('o')) # quantos o's tem na variável frase
print(frase.count('o', 0, 13)) # quantos o's tem começando no índice 0 até o 12
print(frase.find('deo')) # em qual índice começa 'deo' na variável
print(frase.find('Android')) # retorna -1 (não existe)
print('Curso' in frase) # se existe a palavra 'curso' na variável (True)

# --> Transformação

print(frase.replace('Python', 'Android')) # procura python na variável e, se achar, substitui por Android
print(frase.upper()) # deixa todas as letras maiúsculas
print(frase.lower()) # deixa todas as letras minúsculas
print(frase.capitalize()) # deixa todas as letras minúsculas mas deixa a primeira em maiúscula
print(frase.title()) # toda letra no começo da palavra fica em maiúscula (Curso Em Vídeo Android)

frase2 = '    Aprenda Python   '

print(frase2.strip()) # remove todos os espaços do início e do fim
print(frase2.rstrip()) # remove o espaço da direita/fim
print(frase2.lstrip()) # remove o espaço da esquerda/início

# -> Divisão

print(frase.split()) # onde tem espaço vai ser dividido em palavras independentes e cada palavra será colocada em uma lista (divide uma string em uma lista)

# -> Junção

print('-'.join(frase)) # junta todas as listas criadas pelo split e usa o hífen '-' (Curso-em-Vídeo-Android)