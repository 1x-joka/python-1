# Melhore o exercício anterior, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando ele disser que quer mostrar 0 termos

print('\033[1;31;40m============== PROGRAMA PA ==============\033[m')

primeiro_termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão da PA: '))

termo = primeiro_termo
contador = 1
total = 10

while contador <= total:
    print(termo, end=' -> ')
    termo += razao
    contador += 1

mais = int(input('\nQuantos termos a mais você quer mostrar? '))

while mais != 0:
    total += mais

    while contador <= total:
        print(termo, end=' -> ')
        termo += razao
        contador += 1

    mais = int(input('\nQuantos termos a mais você quer mostrar? '))

print('\nPrograma encerrado.')