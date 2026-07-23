# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade: Se ele ainda vai se alistar no serviço militar; Se é hora de se alistar; Se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou passou do prazo

from datetime import date
ano_atual = date.today().year

print('\033[1;31;40m============== PROGRAMA ALISTAMENTO ==============\033[m')
ano_nasc = int(input('Digite o ano de nascimento do jovem: '))
tempo = ano_atual - ano_nasc

if (tempo == 18):
    print('É hora de se alistar! O jovem tem 18 anos exatos')
elif (tempo < 18):
    print(f'O jovem tem {tempo} anos. Não pode se alistar, espere {18 - tempo} anos')
elif (tempo > 18):
    print(f'O jovem tem {tempo} anos. Já passou da hora de se alistar, se passaram {tempo - 18} anos')

# caso o jovem faça 18 anos nesse ano, ficaria 0 anos, mas para especificar os dias seria preciso de dia, mes e ano