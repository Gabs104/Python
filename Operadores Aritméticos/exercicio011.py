# Faça um progarma que leia a largura e a altura de uma parede em metros
# calcule sua área e a quantidade de tinta necessária para pintá-la, sabendo que
# cada litro de tinta pinta uma área de 2m²
# Area = b*a
# b = base
# a = altura

base = float(input('digite o comprimento da base: '))
altura = float(input('digite o comprimento da altura: '))
area = base*altura
print(f'a área dessa parede é:{area}m, e a quantidade de tinta necessária é {area/2}L')