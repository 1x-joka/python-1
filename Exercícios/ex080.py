# Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações: quantidade de notas, a maior nota, a menor nota, a média da turma e a situação (opcional). Adicione também as docstrings da função

def notas(* notas, situacao = False): # não usamos situacao = '' pois não é necessário, não iremos mostrar sim ou não, apenas iremos usar para uma condição
    resultado = dict()

    resultado['total'] = len(notas)
    resultado['maior_nota'] = max(notas)
    resultado['menor_nota'] = min(notas)
    resultado['media'] = sum(notas) / len(notas)

    if situacao: # se for True...
        if (resultado['media'] >= 7):
            resultado['situacao'] = 'APROVADO'
        elif (resultado['media'] >= 5):
            resultado['situacao'] = 'RECUPERAÇÃO'
        else:
            resultado['situacao'] = 'REPROVADO'
    
    return resultado

resp = notas(7.5, 8, 6.5, 9, situacao=True)
print(resp)