# Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo e realize a contagem. Seu programa tem que realizar três contagens através da função criada: De 1 até 10, de 1 em 1. De 10 até 0, de 2 em 2. Uma contagem personalizada

from time import sleep

def contador(inicio, fim, passo):
    for cont in range(inicio, fim, passo):
        print(cont)

print('\033[1;31;40m============== PROGRAMA CONTADOR ==============\033[m')
print('Contando de 1 a 10 de 1 em 1')
sleep(2)
contador(1, 11, 1)
sleep(2)

print('Contando de 10 a 10 de 2 em 2')
sleep(2)
contador(10, -1, -2)
sleep(2)

print('Agora é sua vez!')
inicio = int(input('INÍCIO: '))
fim = int(input('FIM: '))
passo = int(input('PASSO: '))

if (passo == 0):
    passo = 1

if (inicio > fim):
    passo = -abs(passo) # deixa o passo negativo, fazendo a contagem ser pra trás
else:
    passo = abs(passo)

contador(inicio, fim, passo)