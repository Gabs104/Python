n1 = int(input('digite um número: '))
n2 = int(input('digite um número: '))
soma = n1+n2
print(f'a soma vale {soma}') # na verdade os valores são concatenados pois são strings, para evitar isso utiliza de int()

# existem 4 tipos de dados
# int() que são valores inteiros: 5, -7, 2034, -29471
# float() que são valores flutuantes ou decimais: 5.6, 7.9, 4.652, 3.141518...
# bool() que são valores booleanos, só existem 2: True, False
# str() que são valores strings: 'olá', 'como vai?', 'salve!' 

# voltando ao exemplo a cima, e se eu quiser escrever "a soma entre x e y vale z"
# escrevemos assim...

print(f'a soma {n1} + {n2} é: {soma}')

# podemos também verificar se foi atribuido algo para uma variável

valor = bool(input('Digite um valor: '))
print(valor)
# o bool ira verificar se a variável tem um dado inserido
# caso não tenha é retornado False.
# caso contrario é retornado True.
