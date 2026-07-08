# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto e 5% de aumento

print('================ PROGRAMA DESCONTO ================')
preco = float(input('Digite o preço do produto: '))
desconto = preco * 0.95
aumento = preco * 1.05

print(f'O preco atual, com desconto, é de R${desconto}.\nO preço atual, com aumento, é de R${aumento}')