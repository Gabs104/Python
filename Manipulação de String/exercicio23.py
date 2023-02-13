# Faça um programa que leia um número de 0 a 9999 e mostra na tela
# cada um dos dígitos separados.
# ex: 10, ele pode ser tratado como uma string então podemos dividir esse número em uma lista
# tive que ver o video, pois não foi usado nenhum método de manipulação de string.
# Método Guanabara

num = int(input('Informe um Valor entre 0 a 9999:> '))
# forma utilizada para as casas.
u = num // 1 % 10 
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print(f'Analisando o número:> {num}')
print(f'Unidade: {u}')
print(f'Dezena: {d}')
print(f'Centena: {c}')
print(f'Milhar: {m}')