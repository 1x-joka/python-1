# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele (use funções ".is")

x = input('Digite algo: ')
print(x.isnumeric())
print(x.isalpha())
print(x.isalnum())
print(x.isdecimal())
print(x.islower())
print(x.isupper())
print(x.isspace()) # Verifica se todos os caracteres estão com espaço (em branco)
print(x.isidentifier()) # Verifica se o x é um nome válido para variáveis, funções ou classes (começa com letra ou "_" e contém apenas alfanuméricos)
print(x.istitle()) # Verifica se é um título, ou seja, a primeira letra de cada palavra está em maiúsculo
print(x.isascii()) # Verifica se tem caracteres especiais na palavra (ç, ã, etc.)