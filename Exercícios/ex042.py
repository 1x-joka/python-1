# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores

from datetime import date
ano_atual = date.today().year

print('\033[1;31;40m============== PROGRAMA MAIORIDADE ==============\033[m')
qtd_maiores = 0
qtd_menores = 0

for ano in range(1, 8):
    ano_nasc = int(input(f'Digite o ano de nascimento da {ano}° pessoa: '))

    if (ano_atual - ano_nasc >= 18):
        qtd_maiores += 1
    else:
        qtd_menores += 1

print(f'''
    
    {qtd_maiores} pessoas já são maiores de idade
    {qtd_menores} pessoas ainda são menores de idade

''')
print('---FIM---')