# Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato

print('\033[1;31;40m============== PROGRAMA ATLETA ==============\033[m')
jogador = dict()
jogador["gols"] = []

jogador["nome"] = input('Digite seu nome: ').strip()
jogador["qtd_partidas"] = int(input('Quantas partidas você jogou: '))

for indice in range(jogador["qtd_partidas"]):
    gols = int(input(f'Quantos gols você fez na {indice + 1}° partida? '))
    jogador["gols"].append(gols)
    
jogador["total_gols"] = sum(jogador["gols"])

print(f'''
      
    Nome: {jogador["nome"]}
    Partidas: {jogador["qtd_partidas"]}
    Gols por partida: {jogador["gols"]}
    Total de gols: {jogador["total_gols"]}

''')