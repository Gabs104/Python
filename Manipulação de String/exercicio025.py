# Crie um programa que leia o nome de uma pessoa e diga se ela tem 'SILVA' no nome.

nome = str(input('Informe seu Nome:> '))
nome = nome.strip().split()
nome = ''.join(nome)
print('Seu nome tem Silva?:','SILVA' in nome.upper())