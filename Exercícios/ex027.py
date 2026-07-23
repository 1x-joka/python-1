# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa irá perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar. Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado

print('============== PROGRAMA EMPRÉSTIMO P/ CASA ==============')
valor = float(input('Digite o valor da casa: R$'))
salario = float(input('Digite o salário do comprador: R$'))
duracao = int(input('Digite em quantos anos ele pretende pagar: '))

prestacao_mensal = valor / (duracao * 12) # duracao * 12: quantidade de meses

if (prestacao_mensal > (salario * 0.3)):
    print('Não foi possível executar a prestação!')
else:
    print(f'O valor mensal a pagar é de R${prestacao_mensal}')