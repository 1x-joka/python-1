# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade: Até 9 anos MIRIM; Até 14 anos INFANTIL; Até 19 anos JUNIOR; Até 20 anos SÊNIOR; Acima MASTER

from datetime import date
ano_atual = date.today().year

print('\033[1;31;40m============== PROGRAMA NATAÇÃO ==============\033[m')
ano_nasc = int(input('Digite o ano de nascimento do atleta: '))
idade_atual = ano_atual - ano_nasc

if (idade_atual <= 9):
    print('Categoria MIRIM')
elif (idade_atual <= 14):
    print('Categoria INFANTIL')
elif (idade_atual <= 19):
    print('Categoria JÚNIOR')
elif (idade_atual <= 20):
    print('Categoria SÊNIOR')
else:
    print('Categoria MASTER')