# Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior

from random import randint
from time import sleep as intervalo

def sorteia():
    for num in range(5):
        numeros_sorteados.append(randint(0, 10))
    print(f'A lista dos sorteados é: {numeros_sorteados}')

def somaPar():
    soma = 0

    for numero in numeros_sorteados:
        if (numero % 2 == 0):
            soma += numero
    print(f'A soma dos pares é {soma}')

print('\033[1;31;40m============== PROGRAMA SORTEIA / PAR ==============\033[m')
numeros_sorteados = list()

print('Sorteando...')
intervalo(2)

sorteia()
somaPar()