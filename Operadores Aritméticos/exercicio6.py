# Crie um algoritmo que leia um número e mostre seu dobro triplo e raiz quadrada.
num = int(input('digite um número: '))
print(f'o dobro de {num} é {num*2}, seu triplo é {num*3} e sua raiz quadrada é {num**(1/2):2f}')
# para calcuar a raiz quadrada sem a biblioteca do sqrt utiliza de **(1/2)
# a raiz cubica é **(1/3)