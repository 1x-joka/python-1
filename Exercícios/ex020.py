# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente

print('============== PROGRAMA ORGANIZAÇÃO DE NOME ==============')
nome = input('Digite seu nome completo: ').strip()

print(f'''
    Primeiro nome: {nome.split()[0]}
    Último nome: {nome.split()[-1]}
''')