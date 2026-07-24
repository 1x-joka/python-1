# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre: Quantas pessoas tem mais de 18 anos; Quantos homens foram cadastrados; Quantas mulheres tem menos de 20 anos

print('\033[1;31;40m============== PROGRAMA CADASTRO ==============\033[m')
qtd_maioridade = 0
qtd_homens = 0
qtd_mulheres_vinte = 0
escolha = ''

while True:
    idade = int(input('Digite a idade: '))
    while idade <= 0:
        print('Por favor, insira uma idade válida!')
        idade = int(input('Digite a idade: '))

    sexo = input('Digite o sexo [M/F]: ').strip().upper()
    while sexo not in ('M', 'F'):
        print('Sexo inválido!')
        sexo = input('Digite o sexo [M/F]: ').strip().upper()

    if idade >= 18:
        qtd_maioridade += 1

    if sexo == 'M':
        qtd_homens += 1

    if sexo == 'F' and idade < 20:
        qtd_mulheres_vinte += 1

    escolha = input('Deseja continuar [S/N]? ').strip().upper()
    while escolha not in ('S', 'N'):
        print('Resposta inválida!')
        escolha = input('Deseja continuar [S/N]? ').strip().upper()

    if escolha == 'N':
        break

print(f'''

    Quantidade de pessoas com 18 anos ou mais: {qtd_maioridade}
    Quantidade de homens cadastrados: {qtd_homens}
    Quantidade de mulheres com menos de 20 anos: {qtd_mulheres_vinte}

''')
print('---FIM---')