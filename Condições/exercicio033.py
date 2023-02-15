# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
num1 = int(input('Digite um número:> '))
num2 = int(input('Digite outro número:> '))
num3 = int(input('Digite outro número:> '))
if num1 > num2: # se num1 for maior que num2 então ele é o maior número até agora.
    if num3 > num1 > num2: # se num3 for maior que num1, então num2 é o menor número.
        print(f'o maior número é:{num3}')
        print(f'o menor número é: {num2}')
    else: # se num3 não for maior que num1, então ele é o menor número.
        print(f'o maior número é: {num1}')
        print(f'o menor número é: {num3}')
else: # se num1 não for maior que num2, então ele é o maior número até agora.
    if num3 > num2 > num1: # se num3 for maior que num2, então o menor número é o num1.
        print(f'o maior número é: {num3}')
        print(f'e o menor número é: {num1}')
    else: # se num3 não for maior que num2, então num3 é o menor número.
        print(f'o maior número é: {num2}')
        print(f'o menor número é: {num3}')