# ============= TIPOS PRIMITIVOS E SAÍDA DE DADOS =============

n1 = int(input('Digite um número: '))
n2 = int(input('Digite mais um número: '))
print(f'A soma {n1} + {n2} é {n1 + n2}')

# int = número inteiro
# float = número real
# bool = True or False
# str = string = texto (tem que estar entre aspas)

nome = input('Digite seu nome: ')
print(f'O tipo do seu nome é {type(nome)}')
n3 = float(input('Digite um número: '))
print(f'O tipo do número é {type(n3)}')
n4 = bool(input('Digite outro número: '))
print(f'O tipo do outro número é {type(n4)}')
n5 = bool(input('Digite outro outro número: '))
print(f'O outro número é {n5}') # Vazio = False; Preenchido = True

# Concatenação = juntar uma string na outra

n6 = input('Digite um número: ')
print(n6.isnumeric()) # Verificando se o valor digitado dentro de n6 é possível converter em um número do tipo "int"

n7 = input('Digite: ')
print(n7.isalpha()) # Verificando se o valor digitado dentro de n7 é letra

n8 = input('Digite: ')
print(n8.isalnum()) # Verificando se o valor digitado dentro de n8 é alphanumérico (letra e/ou número)

n9 = input('Digite um número: ')
print(n9.isupper()) # Verificando se o valor digitado dentro de n9 está somente em CapsLock