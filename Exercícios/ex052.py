# Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores

import math

print('\033[1;31;40m============== PROGRAMA MÉDIA, MAIOR E MENOR ==============\033[m')

numero = 0
numeros = []
resposta = 'S'

while (resposta == 'S'):
    numero = int(input('Digite um valor inteiro: '))
    resposta = input('Quer continuar [S/N]: ').upper()
    numeros.append(numero)
print(f'''

    A média entre os valores digitados é {sum(numeros) / len(numeros)}
    O maior valor foi {max(numeros)}
    O menor valor foi {min(numeros)}

''')