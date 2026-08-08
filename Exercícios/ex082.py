# Reescreva a função leiaInt() que fizemos, incluindo agora a possibilidade da digitação de um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade

def leiaInt(msg):
    while True:
        try:
            return int(input(msg))
        except (ValueError, TypeError):
            print('ERRO! Digite um número inteiro')

def leiaFloat(msg):
    while True:
        try:
            return float(print(msg))
        except (ValueError, TypeError):
            print('ERRO! Digite um número "flutuante"')


n = leiaInt('Digite um n: ')
print(f'Você digiou {n}')