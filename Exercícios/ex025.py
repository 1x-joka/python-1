# Faça um programa que leia três números e mostre qual é o maior e o menor

print('============== PROGRAMA 3 NÚMEROS ==============')
n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
n3 = float(input('Digite o terceiro número: '))
menor = n1

# Procurando o menor
if n2 < menor:
    menor = n2
if n3 < menor:
    menor = n3
print(f'O menor número digitado foi o {menor}')

maior = n1

# Procurando o maior
if n2 > maior:
    maior = n2
if n3 > maior:
    maior = n3
print(f'O maior número digitado foi o {maior}')

# Forma simplificada de tudo
maior2 = max(n1, n2, n3)
menor2 = min(n1, n2, n3)
print(f'O menor número digitado foi o {menor2}')
print(f'O maior número digitado foi o {maior2}')