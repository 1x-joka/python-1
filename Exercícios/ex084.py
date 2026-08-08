# Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome e idade em um arquivo de texto simples. O sistema só vai ter 2 opções: cadastrar uma nova pessoa e listar todas as pessoas cadastradas

from Módulos.cadastro import cadastrar, listar

while True:
    print('\n1 - Cadastrar pessoa')
    print('2 - Listar pessoas')
    print('3 - Sair')

    opcao = input('Escolha: ')

    if opcao == '1':
        cadastrar()
    elif opcao == '2':
        listar()
    elif opcao == '3':
        print('Volte sempre')
        break
    else:
        print('Opção inválida!')