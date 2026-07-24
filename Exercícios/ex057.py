# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar. No final, mostre: Qual é o total gasto na compra; Quantos produtos custam mais de R$1000; Qual é o nome do produto mais barato

print('\033[1;31;40m============== PROGRAMA PRODUTOS ==============\033[m')
nome = ''
preco = 0
total = 0
qtd_mil = 0
escolha = ''
menor_preco = 0
nome_mais_barato = ''

while True:
    nome = input('Escreva o nome do produto: ')
    preco = float(input('Digite o preço do mesmo produto: R$'))
    while (preco < 0):
        print('Por favor, insira um preço real')
        preco = float(input('Digite o preço novamente: R$'))
    total += preco # adicionando depois da validação

    if (preco >= 1000):
        qtd_mil += 1

    if menor_preco == 0:
        menor_preco = preco
        nome_mais_barato = nome
    elif preco < menor_preco:
        menor_preco = preco
        nome_mais_barato = nome
    
    escolha = input('Deseja continuar [S/N]: ').strip().upper()
    while (escolha not in ('S', 'N')):
        print('Por favor, insira uma opção válida..')
        escolha = input('Deseja continuar [S/N]: ').strip().upper()
    if (escolha == 'N'):
        break
    
print(f'''

    Total gasto na compra: {total}
    {qtd_mil} produtos custam mais de R$1000,00
    O {nome_mais_barato} é o produto mais barato

''')