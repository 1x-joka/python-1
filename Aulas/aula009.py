# # ============= ESTRUTURAS DE REPETIÇÕES/LAÇOS/ITERAÇÕES pt.2 =============
# -> WHILE
# -> Diferença de WHILE e FOR: while não tem limite (ex.: sistema de cadastro: você não sabe quantas pessoas vão se cadastrar, portanto não tem o segundo "argumento" do for, usa-se WHILE)

c = 1
while (c <= 10):
    print(c)
    c += 1


'''

--- Maneira de fazer com while ---
for cont in range(1, 11):
    print(cont)

'''

n = 1
resposta = 'S'
while (resposta == 'S'):
    n = int(input('Digite um número inteiro: '))
    resposta = input('Quer continuar? [S/N] ').upper()