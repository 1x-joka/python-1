# Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela um mensagem: O primeiro valor é maior, o segundo valor é maior, não existe valor maior ou menor, os dois são iguais

print('\033[1;31;40m============== PROGRAMA MAIOR MENOR ==============\033[m')
n1 = int(input('Digite o primeiro número inteiro: '))
n2 = int(input('Digite o segundo número inteiro: '))

if n1 > n2:
    print('O primeiro valor é maior')
elif n2 > n1:
    print('O segundo valor é maior')
else:
    print('Não existe valor maior ou menor, os dois são iguais')

# não precisa daquele "menor/maior = n1" pois são apenas 2 números, se fosse mais de 2 sim