# ============= CONDIÇÕES pt.1 =============
# -> if e else

tempo = int(input('Quantos anos tem seu carro? '))

if (tempo <= 3):
    print('carro novo')
else:
    print('carro velho')
print('--FIM--')

# maneira simplificada

print('carro novo' if tempo <=3 else 'carro velho')
print('--FIM--')

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2
print(f'A sua média foi {media:.1f}') # :.1f = 1 casa decimal

if (media >= 6):
    print('Boa média! Parabéns')
else:
    print('Média ruim! Estude mais')