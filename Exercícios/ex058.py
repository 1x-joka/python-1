# Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1

print('\033[1;31;40m============== PROGRAMA CAIXA ELETRÔNICO ==============\033[m')

valor = int(input('Digite o valor inteiro a ser sacado: R$'))
while (valor <= 0):
    print('Por favor, insira um valor válido...')
    valor = int(input('Digite novamente o valor inteiro a ser sacado: R$'))
    
notas50 = valor // 50
resto = valor % 50 # dinheiro que sobrou depois de já entregar a quantia de notas acima

notas20 = resto // 20
resto = resto % 20

notas10 = resto // 10
resto = resto % 10

notas1 = resto

print(f'''
    Total sacado: R${valor}

    Notas de R$50: {notas50}
    Notas de R$20: {notas20}
    Notas de R$10: {notas10}
    Notas de R$1: {notas1}
''')

print('---FIM---')