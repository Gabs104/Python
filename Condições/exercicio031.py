# Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens até 200Km.
# e R$0,45 para viagens mais longas.

dist = int(input('Qual a distância do seu destino?:> '))
if dist <= 200:
    custo = dist*0.50
    print(f'o custo da sua viagem sera de R${custo:.2f} seguindo a tarifa de R$0,50 para viagens de até 200Km')
else:
    custo = dist*0.45
    print(f'o custo da sua viagem sera de R${custo:.2f} seguindo a tarifa de R$0,45 para viagens acima de 200Km')