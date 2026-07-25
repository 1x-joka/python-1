# ============= DICIONÁRIOS =============

pessoas = {
    'nome': 'Gustavo',
    'sexo': 'M',
    'idade': 22
}

print(f'O dicionário é: {pessoas}')
print(f'O nome da primeira pessoa é {pessoas["nome"]}, o sexo é {pessoas["sexo"]} e a idade é {pessoas["idade"]} anos')

print(pessoas.keys()) # mostra nome, sexo e idade (como um describe em SQL)
print(pessoas.values()) # mostra os valores das keys
print(pessoas.items()) # uma lista (primeira pessoa) composta de 3 tuplas (nome, idade e sexo)

for key in pessoas.keys(): # para cada uma das chaves
    print(key)

for valores in pessoas.values(): # para cada um dos valores
    print(valores)

for key, valores in pessoas.items(): # items substitui enumerate (somente em dicionários)
    print(f'{key} = {valores}')

pessoas['nome'] = 'Leandro' # substituindo todos os nomes por Leandro
pessoas['peso'] = 98.5 # adicionando uma key juntamente a um valor da própria = substitui append (somente em dicionários)
del pessoas['sexo'] # apagando a key "sexo"

brasil = []
estado1 = {
    'UF': 'Rio de Janeiro',
    'sigla': 'RJ'
}
estado2 = {
    'UF': 'São Paulo',
    'sigla': 'SP'
}

brasil.append(estado1)
brasil.append(estado2)
print(brasil)
print(brasil[1]) # mostra o segundo dicionário da lista
print(brasil[0]['UF']) # mostra apenas 'Rio de Janeiro'

states = dict()
brazil = list()
for cont in range(0, 3):
    states['UF'] = str(input('Unidade Federativa: '))
    states['sigla'] = str(input('Sigla do Estado: '))
    brazil.append(states.copy()) # não podemos interligar dicionários e listas, apenas cópias para que o valor dentro da lista não seja o mesmo (todos os dicionários com a mesma UF e sigla)
for e in brazil: # for da lista
    for k, v in e.items(): # for do dicionário
        print(f'O campo {k} tem valor {v}')