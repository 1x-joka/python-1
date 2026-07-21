# # ============= CONDIÇÕES pt.2 =============
# -> Estrutura Condicional Aninhada = if, elif e else

from datetime import datetime
agora = datetime.now().hour

nome = input('Digite seu nome: ')

if (nome == 'Gustavo'):
    print('Que belo nome masculino')
elif (nome in ['Ana Cláudia Jéssica Laura Roberta']):
    print('Que belo nome feminino')
elif (nome == 'Dominique' or nome == 'Ariel'):
    print('Que belo nome pra ambos gêneros')
print('Foi bom te conhecer')

if (6 <= agora < 12):
    print('Tenha um bom dia')
elif (12 <= agora < 18):
    print('Tenha uma boa tarde')
elif (18 <= agora <= 23):
    print('Tenha uma boa noite')
elif (0 <= agora < 6):
    print('Tenha uma boa madrugada')