# Crie um programa que leia dois valores e mostre um menu na tela: [1] Somar [2] Multiplicar [3] Maior [4] Novos Números [5] Sair do Programa. Seu programa deverá realizar a operação solicitada em cada caso

print('\033[1;31;40m============== PROGRAMA OPERAÇÕES ==============\033[m')
numero1 = int(input('Digite o primeiro número: '))
numero2 = int(input('Digite o segundo número: '))
escolha = 0

while (escolha != 5):
    escolha = int(input('''

    [1] - Soma
    [2] - Multiplicar
    [3] - Maior
    [4] - Novos Números
    [5] - Sair do Programa

    '''))

    if (escolha == 1):
        soma = numero1 + numero2
        print(f'A soma dos números digitados foi {soma}')
    elif (escolha == 2):
        mult = numero1 * numero2
        print(f'A multiplicação dos números digitados foi {mult}')
    elif (escolha == 3):
        print(f'O maior número digitado foi o {max(numero1, numero2)}')
    elif (escolha == 4):
        numero1 = int(input('Digite o primeiro número: '))
        numero2 = int(input('Digite o segundo número: '))
    elif (escolha == 5):
        print('Encerrando o programa...')
    else:
        print('Opção inválida, escolha novamente.')