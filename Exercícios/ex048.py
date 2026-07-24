# Faça um programa que leia um número qualquer e mostre o seu fatorial

from math import factorial

numero = int(input('Digite um número inteiro: '))

if (numero < 0):
    print('Não existe fatorial de número negativo')
else:
    print(f'O fatorial é {factorial(numero)}')

# Maneira com WHILE

numero2 = int(input('Digite um número inteiro: '))
fatorial = 1
contador = numero2

while contador > 1:
    fatorial *= contador
    contador -= 1

print(f'O fatorial é {fatorial}')