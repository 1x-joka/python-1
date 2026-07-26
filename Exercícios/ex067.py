# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar

from datetime import date
ano_atual = date.today().year

print('\033[1;31;40m============== PROGRAMA APOSENTADORIA ==============\033[m')
dados = {}
escolha = ''

while True:
    dados["nome"] = input('Escreva seu nome: ').strip()
    dados["ano_nasc"] = int(input('Digite seu ano de nascimento: '))
    dados["idade"] = ano_atual - dados["ano_nasc"]
    dados["clt"] = int(input('Digite sua carteira de trabalho: '))
    if (dados['clt'] != 0):
        dados["ano_contratacao"] = int(input('Digite o ano de contratação: '))
        dados["salario"] = float(input('Digite seu salário: '))
        dados["aposentadoria"] = (dados["ano_contratacao"] + 35) - dados["ano_nasc"]
        print(f'''
            Você, {dados["nome"]} vai se aposentar aos {dados["aposentadoria"]} anos.
        ''')
    else:
        print(f'''
            Você, {dados["nome"]}, não possui carteira de trabalho cadastrada.
        ''')
    for chave, valor in dados.items():
        print(f'{chave}: {valor}')
    print('-='*50)
    escolha = input('Quer continuar? [S/N]: ').strip().upper()
    if (escolha == 'N'):
        print('Adeus!')
        break