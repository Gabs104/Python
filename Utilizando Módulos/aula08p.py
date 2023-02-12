# utilização das bibliotecas
from math import sqrt # importações de módulos da biblioteca math, sqrt e truncs
from math import trunc

num = int(input('Digite um Número:> ')) 
raiz = sqrt(num) # utilizando o módulo sqrt()
print(f'a raiz de {num} é: {(raiz):.2f}')

num = float(input('digite outro número:> '))
denominador = float(input(f'deseja dividir {num} por qual número?:> '))
div = num/denominador # divisão
print(f'o resultado da divisão entre {num:.1f}/{denominador:.1f} é {div}\n',f'a parte inteira da divisão é {trunc(div)}')

