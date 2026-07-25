# Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção. No final, mostre a lista ordenada na tela

print('\033[1;31;40m============== PROGRAMA ORDENADO ==============\033[m')
numeros = []

for indice in range(1, 6):
    num = float(input(f'Digite o {indice}° valor: '))
    
    if (len(numeros) == 0 or (num > numeros[-1])): # se a lista estiver vazia ou o número digitado for menor que o último elemento da lista..
        numeros.append(num) # entra no final da lista
    else:
        posicao = 0 # verifica a posição do primeiro elemento da lista
        while (posicao < len(numeros)): # enquanto ainda existirem posições a verificar na lista...
            if (num <= numeros[posicao]): # se o número digitado for menor ou igual ao número que está nessa posição da lista...
                numeros.insert(posicao, num) # adiciona esse exato número nessa exata posição
                break
            posicao += 1 # vai para o próximo elemento da lista

print(f'A lista ordenada é: {numeros}')