# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o

print('\033[1;31;40m============== PROGRAMA PARES ==============\033[m')

soma_par = 0
qtd_par = 0
for indice in range(1, 7):
    numero = int(input(f'Digite o {indice}° número inteiro: '))

    if (numero % 2 == 0):
        soma_par += numero
        qtd_par += 1
print(f'Você digitou {qtd_par} números pares e a soma entre eles foi {soma_par}')