# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre: Quantos números foram digitados; A lista de valores ordenada de forma decrescente; Se o valor 5 foi digitado e está ou não na lista

print('\033[1;31;40m============== PROGRAMA VERIFICAÇÃO ==============\033[m')
escolha = ''
numeros = list()

while True:
    num = float(input('Digite o número: '))
    numeros.append(num)

    escolha = input('Deseja continuar? [S/N]: ').strip().upper()
    if (escolha == 'N'):
        break
    
print(f'Foram digitados {len(numeros)} números')
numeros.sort(reverse=True)
print(f'A lista, em forma decrescente, é: {numeros}')
if (5 in numeros):
    print('O valor 5 foi digitado e está na lista!')
else:
    print('O valor 5 não foi digitado e não está na lista!')