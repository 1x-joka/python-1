# ============= TRATAMENTO DE ERROS E EXCEÇÕES =============
# -> comando que normalmente funcionaria (código "correto" mas sem declaração da variável, etc.) = exceção

# Tipos de Erros (não precisa decorar, são MUITOS, mais do que estão aqui)
# ModuleNotFoundError -> Módulo não encontrado
# SyntaxError -> Erro na sintaxe do código
# NameError -> Variável/função não definida
# ValueError -> Valor inválido para a operação
# ZeroDivisionError -> Divisão por zero
# TypeError -> Tipo de dado incompatível
# IndexError -> Índice inexistente em uma sequência
# KeyError -> Chave inexistente em um dicionário
# EOFError -> Fim inesperado de uma entrada
# KeyboardInterrupt -> Usuário interrompeu o programa (Ctrl+C)
# OSError -> Erro relacionado ao sistema operacional
# ConnectionError -> Erro em uma conexão
# MemoryError -> Memória insuficiente
# RuntimeError -> Erro genérico durante a execução
# TabError -> Indentação usando tabs/espaços de forma inconsistente
# IndentationError -> Indentação incorreta
# AttributeError -> Atributo/método não existe no objeto
# PermissionError -> Permissão insuficiente para realizar uma operação
# OverflowError -> Resultado numérico grande demais
# FloatingPointError -> Erro em operação de ponto flutuante
# UnboundLocalError -> Variável local usada antes de receber valor
# AssertionError -> Uma afirmação (assert) falhou
# ImportError -> Erro ao importar algo
# FileNotFoundError -> Arquivo ou diretório não encontrado

try:
    x = int(input('Digite o numerador: '))
    y = int(input('Digite o denominador: '))
    resultado = x / y
# except Exception as error:
    # print(f'A classe do erro encontrado foi {error.__class__}') = mostra a classe do erro
# except Exception as error:
    # print(f'A causa do erro encontrado foi {error.__cause__}') = mostra a causa do erro
except ZeroDivisionError:
    print('Não é possível dividir por zero')
except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados informados por você')
except KeyboardInterrupt:
    print('O usuario preferiu não informar os dados')
else: # se tudo der certo
    print(f'O resultado é {resultado:.2f}')
finally: # querendo ou não, vai acontecer isso
    print('Obrigado, volte sempre!')