# Escreva um programa que pergunte a quantidade de Km percorridos
# por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$ 60/dia e R$0,15 por Km Rodado.
# a cada dia R$ 60,00 são incluidos + com R$0,15 por cada Km.
# total = 60*D+0.15*Km

D = int(input('por quantos dias o carro foi alugado?:> '))
Km = int(input('Quantos Km foram percorridos?:> '))
total = (60*D) + (0.15*Km)
print(f'o total a ser pago é de R${total:.2f}')