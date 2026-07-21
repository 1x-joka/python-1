# Faça um programa que leia uma frase pelo teclado e mostre: quantas vezes aparece a letra 'A', em que posição ela aparece a primeira vez e em que posição ela aparece a última vez

print('============== PROGRAMA "A" ==============')
frase = input('Digite uma frase: ').strip()

print(f'''
    1 - A letra "A" aparece {frase.count("A")} vezes
    2 - A primeira letra "A" fica na posição {frase.find("A") + 1}
    3 - A última letra "A" fica na posição {frase.rfind("A") + 1}
''')