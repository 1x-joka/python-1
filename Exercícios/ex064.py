# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta

print('\033[1;31;40m============== PROGRAMA PARÊNTESES ==============\033[m')

expressao = input('Digite a expressão desejada: ').strip()
parenteses = [] # guarda os parênteses que foram abertos mas não foram fechados

for simbolo in expressao:
    if (simbolo == '('):
        parenteses.append('(')
    elif (simbolo == ')'):
        if (len(parenteses) > 0): # a lista não está vazia, existe um '(' para fechar
            parenteses.pop()
        else:
            parenteses.append(')')
            break

if (len(parenteses) == 0): # depois de analisar toda a expressão, a lista ficou vazia?
    print('A expressão está com os parênteses corretos!')
else:
    print('A expressão está com os parênteses incorretos!')