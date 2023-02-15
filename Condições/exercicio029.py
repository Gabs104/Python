# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada Km acima do limite.

v = int(input('Qual a velocidade do carro?:> ')) # velocidade do carro
if v > 80: # se a velocidade do carro ultrapassar 80 então:
    multa = (v-80)*7 # multa é a (velocidade-80)*7, aonde 80 é o meu limite, e 7 é a multa.
    print('Esse carro ultrapassou o limite de 80Km/h.')
    print('Sera cobrado uma multa de R$7,00 para cada Km ultrapassado.')
    print(f'Sua multa foi de: R${multa:.2f}')
else:
    print('o carro não ultrapassou o limite de 80Km/h!')