# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e a condição de pagamento: À vista no dinheiro/cheque: 10% de desconto; À vista no cartão: 5% de desconto; Em até 2x no cartão: preço normal; 3x ou mais no cartão: 20% de juros

print('\033[1;31;40m============== PROGRAMA DESCONTO ==============\033[m')
preco = float(input('Digite o preço do produto: R$'))

metodo = int(input('''
                   
    -- Escolha o método de pagamento--
    [1] - À vista no dinheiro/cheque
    [2] - À vista no cartão
    [3] - Em até 2x no cartão
    [4] - 3x ou mais no cartão   
                   
DIGITE: '''))

if (metodo == 1):
    valor_atual = preco * 0.90
    print(f'O valor a pagar é de R${valor_atual}')
elif (metodo == 2):
    valor_atual = preco * 0.95
    print(f'O valor a pagar é de R${valor_atual}')
elif (metodo == 3):
    print(f'O valor a pagar é de R${preco}')
elif (metodo == 4):
    valor_atual = preco * 1.20
    print(f'O valor a pagar é de R${valor_atual}')
else:
    print('Escolha um método válido!')
print('---FIM---')