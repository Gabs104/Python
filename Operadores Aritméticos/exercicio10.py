# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira
# e mostre quantos dólares ela pode comprar
# considere US$ = 1,00 == R$ 5,14

money = float(input('Digite seu saldo: '))
money_us = money/5.14 # para converter reais em doláres é necessário dividir seu saldo pelo valor atual do dolar
print(f'voce pode comprar US${money_us:.2f}!') 
