# crie um programa que leia um número que leia um número Real qualquer
# pelo teclado e mostre na tela sua porção intera.
# ex: digite um número: 6.127
# o número 6.127 tem a parte inteira 6.
from math import trunc

num = float(input('Digite um número decimal:> ')) # ira ler um número decimal
print(f'o valor {num:.3f} tem sua parte inteira sendo {trunc(num)}') # ira printar o número decimal apenas até as 3 primeiras casas decimais e mostrar sua parte inteira.
