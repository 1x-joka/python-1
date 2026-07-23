# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa mostre: A média de idade do grupo; Qual é o nome do homem mais velho; Quantas mulheres têm menos de 20 anos

print('\033[1;31;40m============== PROGRAMA GRUPO ==============\033[m')
idades = []
qtd_mulheres_vinte = 0
nome_homem_velho = ''
idade_homem_velho = 0

for pessoas in range(1, 5):
    nome = input(f'Digite o nome da {pessoas}° pessoa: ')
    idade = int(input(f'Digite a idade da {pessoas}° pessoa: '))
    sexo = input(f'Digite o sexo (M/F) da {pessoas}° pessoa: ')
    idades.append(idade)

    if (sexo == 'F' and idade < 20):
        qtd_mulheres_vinte += 1

    if (sexo == 'M' and idade > idade_homem_velho):
        idade_homem_velho = idade
        nome_homem_velho = nome

print(f'''

    Média das idades: {sum(idades) / len(idades)}
    Nome do homem mais velho: {nome_homem_velho}
    Quantidade de mulheres -20 anos: {qtd_mulheres_vinte}

''')
print('---FIM---')