# Crie um programa que faça o computador jogar Jokenpô com você

from random import choice
from time import sleep

print('\033[1;31;40m============== PROGRAMA JOKENPÔ ==============\033[m')
escolhas = ['PEDRA', 'PAPEL', 'TESOURA']
computador = choice(escolhas)

usuario = input('''

    -- Vamos jogar! --
         Pedra
         Papel
        Tesoura
                
ESCREVA: ''').strip().upper()

print('Computador pensando...')
sleep(2)

if (usuario == computador):
    print('Empate')
elif (usuario == 'PEDRA' and computador == 'PAPEL'):
    print(f'Você perdeu :( O computador escolheu {computador}')
elif (usuario == 'PEDRA' and computador == 'TESOURA'):
    print(f'Você ganhou! O computador escolheu {computador}')
elif (usuario == 'PAPEL' and computador == 'PEDRA'):
    print(f'Você ganhou! O computador escolheu {computador}')
elif (usuario == 'PAPEL' and computador == 'TESOURA'):
    print(f'Você perdeu :( O computador escolheu {computador}')
elif (usuario == 'TESOURA' and computador == 'PAPEL'):
    print(f'Você ganhou! O computador escolheu {computador}')
elif (usuario == 'TESOURA' and computador == 'PEDRA'):
    print(f'Você perdeu :( O computador escolheu {computador}')
else:
    print('Escolha uma das opções acima!')
print('---FIM---')