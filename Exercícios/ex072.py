# Faça um programa que tenha um função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.

def escreva(frase):
    tamanho = len(frase) + 4 # mais 4 pra ajustar os '-'
    print('-' * tamanho)
    print(f' {frase}')
    print('-' * tamanho)

print('\033[1;31;40m============== PROGRAMA ESCREVA ==============\033[m')
frase = input('Escreva a frase: ').strip().upper()
escreva(frase)