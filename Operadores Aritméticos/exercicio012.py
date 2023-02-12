# Faça um programa que leia o preço de um produto
# e mostre seu novo preço, com 5% de desconto.

print('-'*15,'Bem-Vindo a lojinha!','-'*15) # print 

produto = float(input('digite o preço do produto: '))

produto_desc = (produto*5)/100 # calculo de porcentagem. primeiro multiplica pelo numerador depois divide pelo denominador.

print(f'o preço do produto R${produto:.2f} com o desconto de 5%',f'fica por R${produto-produto_desc:.2f}')
