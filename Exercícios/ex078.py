# Faça um programa que tenha uma função chamada ficha(), que receba dois: parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente

def ficha(nome = '', gols = 0):
    if (nome == ''):
        nome = '<desconhecido>'
    print(f'O jogador {nome} tem {gols} gols')

print('\033[1;31;40m============== PROGRAMA FICHA DE JOGADOR ==============\033[m')
nome = input('Digite o nome do jogador: ').strip()
gols = input('Digite a quantidade de gols: ')

if (gols.isnumeric()):
    gols = int(gols)
else:
    gols = 0

ficha(nome, gols)