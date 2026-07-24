# Melhore o jogo de adivinhar, onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer

from random import randint
from time import sleep

print('\033[1;31;40m============== PROGRAMA ADIVINHE ==============\033[m')
computador = randint(0, 10)
jogador = int(input('Adivinhe o número inteiro de 0 a 10 que vou pensar: '))
qtd_tentativas = 1 # caso o jogador acerte de primeira, contabiliza 1 tentativa

print('Pensando.')
sleep(1)
print('Pensando..')
sleep(1)
print('Pensando...')
sleep(1)

while (jogador != computador):
    jogador = int(input('Errou! Tente novamente: '))
    qtd_tentativas += 1
print(f'Parabéns! A quantidade total de tentativas foram {qtd_tentativas}')