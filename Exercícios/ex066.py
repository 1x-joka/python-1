# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado

from time import sleep
from random import randint
print('\033[1;31;40m============== PROGRAMA DADOS ==============\033[m')
jogadas = dict()
jogador1 = randint(0, 6)
jogador2 = randint(0, 6)
jogador3 = randint(0, 6)
jogador4 = randint(0, 6)
jogadas['Jogador 1'] = jogador1
jogadas['Jogador 2'] = jogador2
jogadas['Jogador 3'] = jogador3
jogadas['Jogador 4'] = jogador4

ranking = sorted(jogadas.items(), key=lambda item: item[1], reverse=True) # key=lambda item: item[1] = ordene usando o segundo elemento da tupla (o valor do dado)

print(f'Jogador 1: {jogador1}')
sleep(1)
print(f'Jogador 2: {jogador2}')
sleep(1)
print(f'Jogador 3: {jogador3}')
sleep(1)
print(f'Jogador 4: {jogador4}')
sleep(1)

for posicao, jogador in enumerate(ranking, start=1):
    print(f'{posicao}° lugar: {jogador[0]} com {jogador[1]}')