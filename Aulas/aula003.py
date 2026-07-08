# ============= UTILIZANDO MÓDULOS =============
# -> importar bibliotecas
#   - math: ceil (arredonda pra cima), floor (arredonda pra baixo), trunc (tirando as casas decimais), pow (potencia), sqrt (raiz quadrada), factorial (fatorial)

import random
n = random.random() # o computador gera um número aleatório entre 0 e 1
n2 = random.randint(1, 20) # o computador gera um número inteiro aleatório entre 1 e 20
print(n)
print(n2)

# import emoji: para instalar localmente apenas escreva no terminal pip install [nome da biblioteca]
import math # não aparece "erro" como o emoji pois é uma biblioteca global, do próprio python.org, enquanto a emoji uma pessoa criou e disponibilizou na comunidade PyPI

from math import floor
j = float(input('Digite um número: '))
print(f'A parte inteira de {j} arredondada pra baixo é {floor(j)}')