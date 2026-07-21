# Crie um programa que leia o nome de uma pessoa e diga se ela tem SILVA no nome

print('============== PROGRAMA SILVA ==============')
nome = input('Digite seu nome completo: ').strip().upper()

if ('SILVA' in nome):
    print('O sobrenome TEM silva')
else:
    print('O sobrenome NÃO tem silva')