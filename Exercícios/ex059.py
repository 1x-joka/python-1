# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista

print('\033[1;31;40m============== PROGRAMA MAIOR MENOR ==============\033[m')
numeros = []

for indice in range(1, 6):
    numeros.append(float(input(f'Digite o {indice}° número na lista: ')))

print(f'''

    Lista: {numeros}
    Maior valor: {max(numeros)}
    Menor valor: {min(numeros)}
    Posição do maior valor: {numeros.index(max(numeros)) + 1}
    Posição do menor valor: {numeros.index(min(numeros)) + 1}

''')
print('---FIM---')