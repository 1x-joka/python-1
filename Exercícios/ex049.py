# Refaça o exercício da PA, lendo o primeiro termo e a razão da PA, mostrando os 10 primeiros termos da progressão usando a estrutura WHILE

print('\033[1;31;40m============== PROGRAMA PA ==============\033[m')

primeiro_termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão da PA: '))

contador = 1
termo = primeiro_termo

while contador <= 10:
    print(termo, end=' -> ')
    termo += razao
    contador += 1

print('---FIM---')