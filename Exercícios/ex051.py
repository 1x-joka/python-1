# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag)

print('\033[1;31;40m============== PROGRAMA 999 ==============\033[m')
numero = 0
qtd_numeros = 0
soma = 0

while (numero != 999):
    numero = int(input('Digite um número: '))
    if (numero != 999):
        qtd_numeros += 1
        soma += numero
    else:
        print('Encerrando o programa...')
print(f'''

    Soma entre os números: {soma}
    Quantidade de números digitados: {qtd_numeros}

''')
print('---FIM---')