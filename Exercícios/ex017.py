# Crie um programa que leia o nome de uma cidade e mostre se ela começa ou não com SANTO

print('============== PROGRAMA CIDADE ==============')
cidade = input('Digite o nome de uma cidade: ').strip().upper()

if (cidade.split()[0] == 'SANTO'):
    print('A cidade começa com santo!')
else:
    print('A cidade NÃO começa com santo!')