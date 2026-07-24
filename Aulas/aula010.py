# # ============= ESTRUTURAS DE REPETIÇÕES/LAÇOS/ITERAÇÕES pt.2 =============
# -> INTERROMPENDO REPETIÇÕES WHILE

numero = s = 0
while True: # opera o que estiver dentro para sempre, ou seja, tem que ter uma condição de encerramento (break)
    numero = int(input('Digite um número inteiro: '))
    if (numero == 999):
        break
    else:
        s += numero
print(f'A soma dos números digitados foi {s}')