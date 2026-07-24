# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto

print('\033[1;31;40m============== PROGRAMA SEXO ==============\033[m')
sexo = 'M'

while (sexo != 'M' or sexo != 'F'):
    sexo = input('Digite o sexo [M/F]: ').upper()
    if (sexo == 'M' or sexo == 'F'):
        break
print('---CADASTRADO!---')