# Desenvolva um programa que leia o comprimento de 3 retas
# e diga ao usuário se elas podem ou não formar um trinagulo.

r1 = float(input('Insira a medida da reta:> '))
r2 = float(input('Insira a medida da outra reta:> '))
r3 = float(input('Insira a medida da última reta:> '))

if r1 + r2 > r3 and r2 + r3 > r1 and r1 + r3 > r2:
    print('é possivel formar um triângulo!')
else:
    print('não é possivel formar um triângulo!')