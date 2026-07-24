# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag)

print('\033[1;31;40m============== PROGRAMA 999 REMAKE ==============\033[m')
numero = 0
soma = 0
qtd_numeros = 0

while True:
    numero = int(input('Digite um número inteiro: '))
    if (numero != 999):
        soma += numero
        qtd_numeros += 1
    else:
        break
print(f'''

    A soma dos números digitados foi {soma}
    A quantidade de números digitados foi {qtd_numeros}

''')
print('---FIM---')