# Crie um programa que leia dois números e mostre a soma entre eles.
trava = True
while trava == True: # condição de loop até que o usupario tenha feito certo oq foi pedido
    num1 = input('digite um número: ')
    num2 = input('digite outro número: ')
    if num1.isnumeric() and num2.isnumeric() == True: # ira checar se os valores de num1 e num2 são numéricos
        num1 = int(num1)
        num2 = int(num2)
        trava = False
    else: # se nao for possivel transformar em número sera printado essa frase para o terminal.
        print('foi digitado um valor inválido')
soma = num1+num2
print(f'a soma entre {num1} + {num2} é: {soma}')