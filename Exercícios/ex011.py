# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo

from math import sin, cos, tan, radians

print('============== PROGRAMA ÂNGULOS ==============')
angulo = float(input('Digite o ângulo, em graus: '))
angulo_radiano = radians(angulo) # convertendo para radiano, pois as funções sin, cos e tan só aceitam assim

print(f'''
    sin({angulo}) = {sin(angulo_radiano):.2f}
    cos({angulo}) = {cos(angulo_radiano):.2f}
    tan({angulo}) = {tan(angulo_radiano):.2f}
''')