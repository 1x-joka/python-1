# Crie um programa que leia o nome completo de uma pessoa e mostre: o nome com letras maiúsculas e minúsculas, quantas letras tem no nome (sem considerar espaços) e quantas letras tem o primeiro nome

print('============== PROGRAMA MANIPULAÇÃO DO NOME ==============')
nome = input('Digite seu nome completo: ').strip()
nome_sem_espaco = nome.replace(" ", "")

print(f'''
    1 - Seu nome todo maiúsculo é {nome.upper()}
    2 - Seu nome todo minúsculo é {nome.lower()}
    3 - Seu nome tem {len(nome_sem_espaco)} letras
    4 - Seu primeiro nome tem {len(nome.split()[0])} letras 
''')

# nome.split()[0] divide cada frase (nome) em listas e pega a 1°