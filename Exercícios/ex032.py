# Refaça o exercício dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado: Equilátero, Isósceles ou Escaleno

print('\033[1;31;40m============== PROGRAMA TRIÂNGULO REMAKE ==============\033[m')

reta1 = float(input('Digite o comprimento da primeira reta: '))
reta2 = float(input('Digite o comprimento da segunda reta: '))
reta3 = float(input('Digite o comprimento da terceira reta: '))

if (reta1 < (reta2 + reta3)) and (reta2 < (reta1 + reta3)) and (reta3 < (reta1 + reta2)):
    print('É possível se formar um triângulo!')
    if (reta1 == reta2 == reta3):
        print('O triângulo é equilátero')
    elif (reta1 == reta2 != reta3 or reta1 == reta3 != reta2 or reta2 == reta3 != reta1):
        print('O triângulo é isósceles')
    else:
        print('O triângulo é escaleno')
else:
    print('Não é possível se formar um triângulo!')