# Faça um programa que tenha uma função chamada area(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno

def area(largura, comprimento):
    return largura * comprimento

print('\033[1;31;40m============== PROGRAMA ÁREA ==============\033[m')
largura = float(input('Digite a largura do terreno: '))
comprimento = float(input('Digite o comprimento do terreno: '))
resultado = area(largura, comprimento)

print(f'A área do terreno é de {resultado} m²')