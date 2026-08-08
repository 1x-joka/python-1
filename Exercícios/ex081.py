# Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra 'FIM', o programa se encerrará. Obs.: Use Cores

while True:
    print('\033[1;31;40m=\033[m' * 50)

    comando = input('\033[1;33mFunção ou biblioteca: \033[m').strip()

    if comando.upper() == 'FIM':
        break

    print('\033[1;36;40m')
    help(comando)
    print('\033[m')

print('\033[1;31;40mPROGRAMA ENCERRADO!\033[m')