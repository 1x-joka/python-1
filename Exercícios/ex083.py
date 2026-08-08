# Crie um código em Python que testa se o site Pudim está acessível pelo computador usado

import urllib.request

try:
    urllib.request.urlopen('https://www.pudim.com.br')
    print('O site está acessível!')
except:
    print('O site Pudim não está acessível!')
finally:
    print('Teste Realizado')