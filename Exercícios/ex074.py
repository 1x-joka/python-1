# Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é maior

def maior(* numero):
    maior_numero = numero[0]
    for valor in numero:
        if (valor > maior_numero):
            maior_numero = valor
    print(f'Os valores digitados foram: {numero}')
    print(f'O maior foi {maior_numero}')

print('\033[1;31;40m============== PROGRAMA CONTADOR ==============\033[m')
numero = 0
numeros = list()

while True:
    numero = float(input('Digite um número: '))
    numeros.append(numero)
    escolha = input('Quer continuar? [S/N]: ').strip().upper()

    while (escolha not in ('S', 'N')):
        print('Por favor, escolha correto!')
        escolha = input('Quer continuar? [S/N]: ').strip().upper()
    
    if (escolha == 'N'):
        break

maior(* numeros) # chama todos os valores digitados na lista