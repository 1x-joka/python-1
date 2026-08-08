# Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro e o ano de nascimento de uma pessoa, retornando um valor literal indiciando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições

from datetime import date
ano_atual = date.today().year
def voto(ano_nasc):
    idade = ano_atual - ano_nasc
    return idade

print('\033[1;31;40m============== PROGRAMA ALISTAMENTO ==============\033[m')
ano_nasc = int(input('Digite o ano de nascimento: '))
idade = voto(ano_nasc)
print(f'Você tem {idade} anos')

if (idade < 16):
    print('VOTO NEGADO')
elif (idade < 18 or idade >= 70):
    print('VOTO OPCIONAL')
else:
    print('VOTO OBRIGATÓRIO')