# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão

print('\033[1;31;40m============== PROGRAMA PA ==============\033[m')
primeiro_termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))

termo = primeiro_termo
print('Os 10 primeiros termos da PA são:')

for contador in range(10):
    print(termo)
    termo += razao