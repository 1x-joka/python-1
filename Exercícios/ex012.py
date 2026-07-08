# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido

import random

print('============== PROGRAMA APAGAR QUADRO ==============')
nome1 = input('Digite o nome do primeiro aluno: ')
nome2 = input('Digite o nome do segundo aluno: ')
nome3 = input('Digite o nome do terceiro aluno: ')
nome4 = input('Digite o nome do quarto aluno: ')

todos_alunos = [nome1, nome2, nome3, nome4]

escolhido = random.choice(todos_alunos)
print(f'O aluno escolhido para apagar o quadro é {escolhido}')