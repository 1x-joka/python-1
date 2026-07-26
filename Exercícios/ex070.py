# Aprimore o exercício 068 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador

print('\033[1;31;40m============== PROGRAMA ATLETA REMAKE ==============\033[m')
jogadores = dict()
jogadores_lista = list()
jogadores["gols"] = list()

while True:
    jogadores["nome"] = input('Escreva seu nome: ').strip()
    jogadores["qtd_partidas"] = int(input('Quantas partidas você jogou: '))

    # Verificando se as partidas não foram negativas
    while (jogadores["qtd_partidas"] < 0):
        print('Digite uma quantidade maior ou igual a 0!')
        jogadores["qtd_partidas"] = int(input('Quantas partidas você jogou: '))

    # Conta de quantos gols em cada partida e no total
    for indice in range(jogadores["qtd_partidas"]):
        gols = int(input(f'Quantos gols você fez na {indice + 1}° partida? '))
        
        # Verificando se o usuário não inseriu uma quantidade negativa de gols
        while (gols < 0):
            print('Digite uma quantidade válida!')
            gols = int(input(f'Quantos gols você fez na {indice + 1}° partida? '))
        jogadores["gols"].append(gols)
    jogadores["total_gols"] = sum(jogadores["gols"])

    jogadores_lista.append(jogadores.copy())
    jogadores["gols"].clear() # Para não misturar todos os gols na mesma lista
    
    # Flag do While True
    escolha = input('Quer continuar? [S/N]: ').strip().upper()
    while (escolha not in ('S', 'N')):
        print('Digite uma escolha válida!')
        escolha = input('Quer continuar? [S/N]: ').strip().upper()
    if (escolha == 'N'):
        break

print('-' * 60)
print(f'{"COD":<5}{"NOME":<15}{"GOLS":<20}{"TOTAL"}')
print('-' * 60)

for indice, jogador in enumerate(jogadores_lista):
    print(f'{indice:<5}{jogador["nome"]:<15}{str(jogador["gols"]):<20}{jogador["total_gols"]}')
print('-' * 60)

while True:
    codigo = input('Digite o código do jogador que deseja ver (999 encerra): ')
    
    # Verificando se o código digitado foi um número mesmo
    while not (codigo.isdigit()):
        print('Digite um código válido')
        codigo = input('Digite o código do jogador que deseja ver (999 encerra): ')
    codigo = int(codigo)

    if (codigo == 999):
        break

    # Verificando se o código digitado é negativo ou maior do que tem de jogadores na lista que veio do dicionário
    if ((codigo < 0) or (codigo >= len(jogadores_lista))):
        print('Digite um código válido!')
    else:
        print(f'\n== LEVANTAMENTO DO JOGADOR {jogadores_lista[codigo]["nome"]} ==')

        for partida, gols in enumerate(jogadores_lista[codigo]["gols"], start=1):
            print(f'Na {partida}ª partida fez {gols} gol(s).')

print('---FIM---')