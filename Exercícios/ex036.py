# Crie um programa que mostre na tela todos os números pares que estão entre 1 e 50

print('\033[1;31;40m============== PROGRAMA PARES ==============\033[m')

for numero in range(1, 51):
    if (numero % 2 == 0):
        print(f'PAR: {numero}')
print('---FIM---')

# Maneira simplificada

for numero2 in range(2, 51, 2):
    print(numero2)
print('---FIM---')