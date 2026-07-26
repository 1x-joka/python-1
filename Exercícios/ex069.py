# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: Quantas pessoas foram cadastradas; A média de idade do grupo; Uma lista com todas as mulheres; Uma lista com todas as pessoas com idade acima da média

print('\033[1;31;40m============== PROGRAMA MANIPULANDO DADOS ==============\033[m')
dados = dict()
dados_lista = []
idade = []

while True:
    dados["nome"] = input('Digite o nome: ').strip()

    dados["sexo"] = input('Digite o sexo [M/F]: ').strip().upper()
    while (dados["sexo"] not in ('M', 'F')):
        print('Digite um sexo válido')
        dados["sexo"] = input('Digite o sexo novamente [M/F]: ').strip().upper()

    dados["idade"] = int(input('Digite sua idade: '))
    while (dados["idade"] <= 0):
        print('Digite uma idade válida')
        dados["idade"] = int(input('Digite novamente sua idade: '))

    dados_lista.append(dados.copy())
    idade.append(dados["idade"])

    escolha = input('Quer continuar? [S/N]: ').strip().upper()
    while (escolha not in ('S', 'N')):
        print('Digite uma escolha válida')
        escolha = input('Quer continuar? [S/N]: ').strip().upper()
    if (escolha == 'N'):
        break

media_idade = (sum(idade) / len(idade))

print(f'Foram cadastradas {len(dados_lista)} pessoas')
print(f'A média das idades é {media_idade:.1f}')
print('Mulheres cadastradas:')
for pessoa in dados_lista:
    if (pessoa["sexo"] == 'F'):
        print(f'Nome: {pessoa["nome"]} | Idade: {pessoa["idade"]}')

print('Pessoas com idade acima da média: ')
for pessoa in dados_lista:
    if (pessoa["idade"] > media_idade):
        print(f'Nome: {pessoa["nome"]} | Sexo: {pessoa["sexo"]} | Idade: {pessoa["idade"]}')