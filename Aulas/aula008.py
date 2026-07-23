# # ============= ESTRUTURAS DE REPETIÇÕES/LAÇOS/ITERAÇÕES pt.1 =============
# -> FOR

for c in range(1, 7): # conta de 1 até 6
    print(c)
print('---FIM---')

for i in range(6, 0, -1): # -1 = indicando a iteração, o que vai acontecer no final do laço que nesse caso é tirar 1, começa no 6, vai até o 0 tirando 1
    print(i)
print('---ACABOU---')

for r in range(0, 7, 2): # de 0 a 6 pulando de 2 em 2
    print(r)
print('---TÉRMINO---')

inicio = int(input('Digite o início: '))
fim = int(input('Digite o fim: '))
passo = int(input('Digite o passo: '))
for cont in range(inicio, fim + 1, passo):
    print(cont)

soma = 0
for a in range(1, 4):
    numero = int(input(f'Digite o {a}° número: '))
    soma += numero
print(f'O somatório de todos os valores digitados foi de {soma}')