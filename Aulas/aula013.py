# ============= FUNÇÕES pt.1 =============

def linha():
    print('-' * 50)

print('Curso em Vídeo')
linha()
print('Aprenda Python')
linha()
print('Gustavo Guanabara')
linha()

def titulo(mensagem):
    print('-' * 50)
    print(mensagem)
    print('-' * 50)

titulo('Olá') # Esse texto é enviado para o parâmetro da função titulo (mensagem) e devolvido na tela com o que está dentro da função já substituído

def soma(a, b):
    s = a + b
    print(f'{a} + {b} = {s}')

soma(4, 5)

def soma2(c, d):
    return c + d
resultado = soma2(40, 50)
print(resultado)
print(soma2(15, 10))

def contador(* num): # '*' parametro = aceita quantos parâmetros você definir quando for chamar ela
    print(num)

contador(1, 2, 3)
contador(10, 9)
contador(0)

def contador2(* numero):
    for valor in numero:
        print(valor)
    tamanho = len(numero)
    print(f'{tamanho} números foram digitados')
    print('---FIM---')

contador2(200, 450)

def dobra(lista):
    pos = 0
    while (pos < len(lista)):
        lista[pos] *= 2 # dobrando em si cada valor da lista
        pos += 1 # faz avançar uma posição na lista (sai do 1° número e vai pro 2°)

valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)

def soma3(* numeros2):
    soma = 0
    for valor in numeros2:
        soma += valor
    print(f'Somando os valores {numeros2}, a soma é {soma}')