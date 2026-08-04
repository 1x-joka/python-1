# ============= FUNÇÕES pt.2 =============
help(input) # fala o que o comando faz (docstring)
print(input.__doc__) # fala outra informação do comando

def contador(inicio, fim, passo):
    cont = inicio
    while (cont <= fim):
        print(f'{cont}', end=' ')
        cont += passo
    print('FIM')

help(contador)

# PARÂMETROS OPCIONAIS

def somar(a = 0, b = 0, c = 0): # igualar a zero torna o parâmetro opcional, ou seja, se eu não digitar quaisquer deles a função entende como zero
    s = a + b + c
    print(f'A soma fica {s}')

somar(1, 2, 3)

# ESCOPO DE VARIÁVEIS

def teste():
    n = 3 # Variável Local, neste caso, criam-se duas variáveis com o mesmo nome porém com valores diferentes
    x = 8 # Variável Local / Escopo Local
    print(f'Na função, x vale {x}')
    print(f'Na função, n vale {n}')

n = 2 # Variável Global / Escopo Global
print(f'No programa principal, n vale {n}')
print(f'No programa principal, x vale {x}')

# RETORNANDO VALORES (RETURN)

def somar2(a2 = 0, b2 = 0, c2 = 0):
    s2 = a2 + b2 + c2
    return s2

resposta = somar2(1, 2, 3) # Temos que criar uma variável resposta pois o return s2 faz o valor ir para uma variável (ou colocar dentro de um print)
print(somar2(1, 2, 3))

r1 = somar2(1, 2, 3)
r2 = somar2(1, 2, 3)
r3 = somar2(1, 2, 3)

print(f'As somas deram {r1}, {r2} e {r3}')

def par(num = 0):
    if (num % 2 == 0):
        return True
    else:
        return False
    
numero = int(input('Digite um número: '))

if (numero % 2 == 0):
    print('É PAR')
else:
    print('É ÍMPAR')