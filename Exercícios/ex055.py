# Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo

from time import sleep
from random import randint

print('\033[1;31;40m============== PROGRAMA PAR OU ÍMPAR ==============\033[m')
qtd_vitorias = numero = soma = 0
resultado = ''

while True:
    jogador = input('P/I: ').strip().upper()
    if (jogador == 'P' or jogador == 'I'):
        numero = int(input('Digite um número inteiro: '))
        computador = randint(0, 10)
        soma = computador + numero

        if (soma % 2 == 0):
            resultado = 'PAR'
        else:
            resultado = 'IMPAR'

        if (soma % 2 == 0 and jogador == 'P'):
            print(f'O computador escolheu {computador} e a soma deu {soma}, que é {resultado}')
            qtd_vitorias += 1
        elif (soma % 2 != 0 and jogador == 'I'):
            print(f'O computador escolheu {computador} e a soma deu {soma}, que é {resultado}')
            qtd_vitorias += 1
        else:
            print(f'O computador escolheu {computador} e a soma deu {soma}, que é {resultado}')
            break
    else:
        print('Escolha uma opção válida!')
        continue # faz o while voltar para o início sem finalizar (break)
print(f'Você ganhou {qtd_vitorias} seguidas!')
print(f'---FIM---')