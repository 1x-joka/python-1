# Refaça o exercício de tabuada, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for

print('\033[1;31;40m============== PROGRAMA TABUADA REMAKE ==============\033[m')
numero = int(input('Digite o número que deseja adquirir a tabuada de 1 a 10: '))

for cont in range(1, 11):
    print(f'{numero} x {cont} = {numero * cont}')
print('---FIM---')