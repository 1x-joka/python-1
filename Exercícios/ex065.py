# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela

print('\033[1;31;40m============== PROGRAMA MÉDIA ==============\033[m')
dados_aluno = {}

dados_aluno['nome'] = input('Escreva o nome do aluno: ')
dados_aluno['media'] = float(input(f'Digite a média de {dados_aluno["nome"]}: '))

if (dados_aluno['media'] <= 5):
    dados_aluno['situacao'] = 'Reprovado!'
else:
    dados_aluno['situacao'] = 'Aprovado!'

print(f'{dados_aluno["nome"]} tem média de {dados_aluno["media"]} com situação {dados_aluno["situacao"]}')
print(dados_aluno)

for chave, valor in dados_aluno.items():
    print(f'{chave} = {valor}') # cada chave com seu respectivo valor