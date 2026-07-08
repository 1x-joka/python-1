# ============= OPERADORES ARITMÉTICOS =============
# adição, subtração, multiplicação, divisão, potência, divisão inteira (quociente) e resto da divisão

# ============= ORDEM DE PRECEDÊNCIA =============
# 1. ()
# 2. **
# 3. * / // % (quem aparece primeiro)
# 4. + - (quem aparece primeiro)

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
soma = n1 + n2
multiplicacao = n1 * n2
divisao = n1 / n2
divisao_inteira = n1 // n2
exponencial = n1 ** n2
print(f'''
      A soma é {soma}
      A multiplicação é {multiplicacao}
      A divisão é {divisao}
      A divisão inteira é {divisao_inteira}
      O exponencial é {exponencial}
''')