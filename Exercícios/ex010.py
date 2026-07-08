# Faça um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço, sabendo que o carro custa R$60 por dia e R$0.15 por Km rodado

print('================ PROGRAMA ALUGUEL DE CARROS ================')
qtd_km = float(input('Digite a quantidade de km percorridos: '))
aluguel_dias = int(input('Digite a quantidade de dias que o carro foi alugado: '))
preco_carro = (aluguel_dias * 60) + (0.15 * qtd_km)

print(f'O valor total a pagar é R${preco_carro} (valor diário: R${aluguel_dias * 60}. valor por km: R${qtd_km * 0.15})')