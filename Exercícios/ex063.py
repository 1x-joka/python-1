# Crie um programa que vai ler números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas

print('\033[1;31;40m============== PROGRAMA PAR ÍMPAR ==============\033[m')
numeros = list()
numeros_pares = list()
numeros_impares = []
escolha = ''

while True:
    num = float(input('Digite um número: '))
    numeros.append(num)
    if (num % 2 == 0):
        numeros_pares.append(num)
    else:
        numeros_impares.append(num)

    escolha = input('Quer continuar? [S/N]: ').strip().upper()
    if (escolha == 'N'):
        break
    
print(f'''

    Lista geral: {numeros}
    Lista Pares: {numeros_pares}
    Lista Ímpares: {numeros_impares}

''')