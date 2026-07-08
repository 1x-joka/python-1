# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia os nomes dos quatro e mostre a ordem sorteada

import random

print('============== PROGRAMA APAGAR QUADRO ==============')
nome1 = input('Digite o nome do primeiro aluno: ')
nome2 = input('Digite o nome do segundo aluno: ')
nome3 = input('Digite o nome do terceiro aluno: ')
nome4 = input('Digite o nome do quarto aluno: ')

todos_alunos = [nome1, nome2, nome3, nome4]
random.shuffle(todos_alunos) # embaralhando os alunos

print(f'''
    O primeiro aluno é {todos_alunos[0]}
    O segundo aluno é {todos_alunos[1]}
    O terceiro aluno é {todos_alunos[2]}
    O quarto aluno é {todos_alunos[3]}
''')