# Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram no intervalo de 1 a 500

print('\033[1;31;40m============== PROGRAMA ÍMPARES + MULT 3 ==============\033[m')

soma = 0
for numero in range(1, 501):
    if (numero % 2 != 0 and  numero % 3 == 0):
        soma += numero
print(f'A soma de todos os números ímpares que são múltiplos de três é de {soma}')
print('---FIM---')