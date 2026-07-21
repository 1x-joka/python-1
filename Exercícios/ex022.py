# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada km acima do limite


print('============== PROGRAMA MULTA ==============')
velocidade = float(input('Digite a velocidade do carro (em km/h): '))

if (velocidade > 80):
    multa = (velocidade - 80) * 7
    print(f'Você foi multado! O valor a pagar será de R${multa:.2f}')
else:
    print('Não foi multado!')