# Faça um programa que leia o comprimento do cateto oposto e do cateto
# adjacente de um triangulo retangulo, calcule e mostre o comprimento da 
# hipotenusa.

from math import hypot

cat_oposto = float(input('digite o cateto oposto:> '))
cat_adj = float(input('digite o cateto adjacente:> '))

h = hypot(cat_oposto,cat_adj)
print(f'a hipotenusa deste triângulo retângulo é:> {h}')