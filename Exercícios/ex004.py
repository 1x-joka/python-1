# Crie um algoritmo que leia um número, seu dobro, seu triplo e sua raiz quadrada

from math import sqrt

n = float(input('Digite um número: '))
print(f'''
    Seu dobro é {n * 2}
    Seu triplo é {n * 3}
    Seu sucessor é {n + 1}
    Seu antecessor é {n - 1}
    A raiz quadrada é {sqrt(n)}
''')

# SEM A BIBLIOTECA MATH
print(f'Raiz quadrada de {n} é {n ** (1/2)}') # entre parênteses pois o python interpretará como n ** 1 dividido por 2 depois