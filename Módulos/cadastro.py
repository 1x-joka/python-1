from pathlib import Path as pt # para salvar na área de trabalho especificamente

ARQUIVO = pt.home() / 'Desktop' / 'pessoas.txt' # salva na área de trabalho

def cadastrar():
    nome = input('Nome: ').strip()
    idade = input('Idade: ')

    with open(ARQUIVO, 'a') as arquivo: # Abre o arquivo pessoas.txt no modo 'a' (append), permitindo adicionar novos dados sem apagar os anteriores, 'arquivo' é o nome da variável que representa o arquivo.
        arquivo.write(f'{nome};{idade}\n')


def listar():
    with open(ARQUIVO, 'r') as arquivo:
        for linha in arquivo:
            nome, idade = linha.strip().split(';')
            print(f'{nome:<10}{idade} anos')