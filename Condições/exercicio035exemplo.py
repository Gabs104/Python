r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
# se 2 < 5 + 4 and 5 < 2 + 4 and 4 < 2 + 5, ou seja se a soma de 2 segmentos for maior que o que o segmento indicado por <. é possivel formar um trângulo.
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('é possivel formar um triângulo!')
else:
    print('não é possivel formar um triângulo!')