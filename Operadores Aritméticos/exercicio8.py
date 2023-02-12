# Escreva um programa que leia um valor em metros exiba convertido em centímetros e milímetros.
# 1 metro = 100 centímetros
# 1 metro = 1000 milímetros

metro = float(input('digite o comprimento: '))
cent = metro*100
mili = metro*1000
print(f'o comprimento {metro}m, em centímetros é {cent}cm, e em milímetros {mili}mm')