# UTILIZANDO PACOTES

from uteis.numeros import * # importando tudo, caso queira funções específicas basta adicioná-las na frente do import

num = int(input('Digite um valor: '))
fat = fatorial(num)

print(f'O fatorial de {num} é {fat}')
print(f'O dobro de {num} é {dobro(num)}')
print(f'O triplo de {num} é {triplo(num)}')