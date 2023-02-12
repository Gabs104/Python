# Faça um algoritmo que leia o salário de um funcionário e mostre
# seu novo salário com 15% de aumento.
# 5000
salario = int(input('Digite seu salário: '))
salario_aumt = (salario)*15/100 + salario
print(f'seu salário de R${salario:.2f} com um aumento de 15%',f'fica por R${salario_aumt:.2f}')