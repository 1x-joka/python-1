# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar (US$1,00 = R$3,27)

print('================ PROGRAMA CONVERSÃO ================')
real = float(input('Informe quantos reais você tem: R$'))
dolar = real / 3.27

print(f'Com R${real} você pode ter US${dolar}')