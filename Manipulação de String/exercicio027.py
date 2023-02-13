# Faça um programa que leia o primeiro e último nome de uma pessoa.

nome = str(input('Digite seu nome Completo:> ')).strip()
nome = nome.split()
print(f'Seu primeiro nome é: {nome[0]}') # ira ler o primeiro elemento da lista
print(f'seu último nome é: {nome[-1]}') # ira ler o último elemento da lista