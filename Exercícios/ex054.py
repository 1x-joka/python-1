# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo

print('\033[1;31;40m============== PROGRAMA TABUADA REMAKE ==============\033[m')
numero = 0

while True:
    numero = int(input('Digite o valor que deseja saber a tabuada de 1 a 10: '))
    if (numero >= 0):
        for indice in range(1, 11):
            print(f'{numero} x {indice} = {numero * indice}')
    else:
        print('Valor negativo informado. Encerrando...')
        break
print('---FIM---')