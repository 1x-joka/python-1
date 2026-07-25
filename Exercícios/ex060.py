# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente

print('\033[1;31;40m============== PROGRAMA CRESCENTE ==============\033[m')
numeros = []
escolha = ''

while True:
    num = float(input('Digite um número: '))
    if (num not in numeros):
        numeros.append(num)
        print('Cadastro feito!')
    else:
        print(f'O número {num} já está na lista.')

    escolha = input('Deseja continuar? [S/N]: ').strip().upper()
    if (escolha == 'N'):
        print('Encerrando...')
        break
    else:
        continue

numeros.sort() # deixa em ordem crescente antes de entrar no print, pois senão retornará None
print(f'''

    Lista: {numeros}
    Lista em ordem crescente: {numeros}

''')