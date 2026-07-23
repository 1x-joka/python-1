# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 - binário; 2 - octal; 3 - hexadecimal

print('\033[1;31;40m============== PROGRAMA BASE DE CONVERSÃO ==============\033[m')
numero = int(input('Digite um número inteiro: '))

escolha = int(input('''
    --- Escolha a base de conversão ---
    [1] - Binário
    [2] - Octal
    [3] - Hexadecimal
                    
DIGITE: '''))

if (escolha == 1):
    binario = bin(numero)[2:] # retirando o "0b"
    print(f'O número {numero} em binário fica {binario}')
elif (escolha == 2):
    octal = oct(numero)[2:] # retirando o "0o"
    print(f'O número {numero} em octal fica {octal}')
elif (escolha == 3):
    hexadecimal = hex(numero)[2:].upper() # retirando o "0x"
    print(f'O número {numero} em hexadecimal fica {hexadecimal}')
else:
    print('Digite uma opção válida')
print('---FIM---')