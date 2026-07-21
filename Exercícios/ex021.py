# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu

from random import randint
from time import sleep

computador = randint(0, 5)

print('============== PROGRAMA ADIVINHE ==============')
print('Espere, o computador está pensando...')
sleep(2)

print('Escolheu!\n')
adivinhe = int(input('Adivinhe o número que o computador escolheu (entre 0 e 5): '))

if (computador == adivinhe):
    print(f'Parabéns, você acertou! O número foi {computador}')
else:
    print(f'Não foi dessa vez :( O número escolhido pelo computador foi {computador}')