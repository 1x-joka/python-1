# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos

print('\033[1;31;40m============== PROGRAMA PESO ==============\033[m')
pesos = []

for pessoas in range(1, 6):
    peso = float(input(f'Digite o peso, em kg, da {pessoas}° pessoa: '))
    pesos.append(peso)

print(f'''

    Maior peso: {max(pesos)}
    Menor peso: {min(pesos)}

''')
print('---FIM---')