# Faça um programa que leia a largura e a altura de uma parede retangular em metros, calcule sua área e a quantidade necessária de tinta para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m²

print('================ PROGRAMA PINTURA ================')
l = float(input('Digite a largura da parede, em metros: '))
a = float(input('Digite a altura da parede, em metros: '))
area = (l * a)
qtd_tinta = area / 2

print(f'A quantidade de tinta necessária, em litros, é {qtd_tinta}L')