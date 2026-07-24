# ============= LISTAS =============
# -> Tuplas (imutáveis)
# -> Listas (mutáveis)

numeros = (2, 5, 9, 1)
print(numeros)
# numeros[2] = 3 #--> não é possível pois tupla é imutável

numeros2 = [2, 5, 9, 1]
numeros2[2] = 10
# numeros[4] = 7 --> não pode adicionar valores assim (FORMA INCORRETA)
numeros2.append(7) # --> FORMA CORRETA
numeros2.sort() # colocando em ordem crescente
numeros2.sort(reverse=True) # colocando em ordem decrescente
numeros2.insert(2, 0) # adicionando o 0 na posição 2 (empurra todos os elementos pra direita/frente)
numeros2.pop() # removendo o último elemento da lista
numeros2.pop(2) # removendo o elemento que está na posição 2 da lista
numeros2.remove(2) # procura, começando do início, a primeira ocorrência do NÚMERO 2 e remove
print(numeros2[2])

if (4 in numeros2):
    numeros2.remove(4)
    print('Número 4 removido')
else:
    print('Não achei o número 4 na lista')
print(f'Essa lista tem {len(numeros2)} elementos')

print('----------------------------------------------')

valores = list() # mesma coisa que valores = []
valores.append(5)
valores.append(9)
valores.append(4)
print(valores)

# deixando mais bonito visualmente
for valor in valores:
    print(f'{valor}')

for indice, valor in enumerate(valores):
    print(f'Na posição {indice + 1} encontrei o valor {valor}')
print('Cheguei no final da lista')

# lendo valores pelo teclado e colocando na lista
for cont in range(0, 5):
    valores.append(int(input(f'Digite o {cont}° valor: ')))
for indice, valor in enumerate(valores):
    print(f'Na posição {indice + 1} encontrei o valor {valor}')
print(f'Lista completa: {valores}')
print('Cheguei no final da lista novamente')

a = [2, 3, 4, 7]
b = a # igualar listas = python cria uma conexão entre elas, qualquer mudança ocorre em ambas. NÃO É CÓPIA
b[2] = 8 # muda as duas listas

print(f'Lista A: {a}')
print(f'Lista B: {b}')

b = a[:] # ISSO É CÓPIA