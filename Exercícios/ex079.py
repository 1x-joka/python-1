# Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante à função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico. Ex.: n = leiaInt('Digite um n')

def leiaInt(msg):
    while True:
        numero = input(msg)
        if (numero.isnumeric()):
            numero = int(numero)
            return numero
        else:
            print('ERRO digite um número')

n = leiaInt('Digite um n: ')
print(f'Você digiou {n}')