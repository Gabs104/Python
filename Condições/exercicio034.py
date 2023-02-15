# Escreva um programa que pergunte o salário de um funcionário e calcule
# o valor de seu aumento.
# Para salários superiores a R$1.250,00 calcule um aumento de 10%
# Para os inferiores ou iguais, aumento é de 15%.
# salario <= 1250:
#   aumento = salario + ((salario*15)/100)
# sálario > 1250:
#   aumento = salario + ((salario*10)/100)

salario = float(input('insira seu salário:> '))
if salario > 1250:
    aumento = salario + ((salario*10)/100) 
    print(f'seu salário receberá um aumento de 10%!, ficando com R${aumento:.2f}!')
else:
    aumento = salario + ((salario*15)/100)
    print(f'seu salário receberá um aumento de 15%, ficando com R${aumento:.2f}!')