# Faça um programa que leia um ano qualquer e diga se ele é bissexto.
# um ano bissexto é aquele em que é possivel dividi-lo por 4. ou seja
# o resto da divisão tem que ser 0.

ano = int(input('Insira algum ano:> '))
if ano%4 == 0:
    print('é um ano bissexto!')
else:
    print('não é um ano bissexto!')