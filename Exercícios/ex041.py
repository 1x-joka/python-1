# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo

print('\033[1;31;40m============== PROGRAMA PRIMO ==============\033[m')
numero = int(input('Digite um número inteiro: '))

qtd_divisores = 0
for divisor in range(1, numero + 1):
    if (numero % divisor == 0):
        qtd_divisores += 1

if (qtd_divisores == 2):
    print('Ele é primo!')
else:
    print('Ele não é primo')