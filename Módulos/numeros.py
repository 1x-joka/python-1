# UTILIZANDO MÓDULOS

import uteis
# from uteis import fatorial, dobro, triplo --> não recomendado pelo próprio Python pois pode ter ambiguidades, caso você tenha em outro arquivo uma função fatorial pode dar incompatibilidades
num = int(input('Digite um valor: '))
fat = uteis.fatorial(num)

print(f'O fatorial de {num} é {fat}')
print(f'O dobro de {num} é {uteis.dobro(num)}')
print(f'O triplo de {num} é {uteis.triplo(num)}')