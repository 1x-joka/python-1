# Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e o outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial

def fatorial(numero, show=False):
    resultado = 1

    for c in range(numero, 0, -1):
        if show:
            if c > 1:
                print(f'{c} x ', end='')
            else:
                print(f'{c} = ', end='')

        resultado *= c

    return resultado

print('\033[1;31;40m============== PROGRAMA FATORIAL ==============\033[m')
num = int(input('Digite um número: '))
mostrar = input('Mostrar o cálculo? [S/N] ').strip().upper()

if mostrar == 'S':
    print(fatorial(num, True))
else:
    print(fatorial(num))