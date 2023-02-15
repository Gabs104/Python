# estudando análise combinatória e este foi o primeiro conteúdo abordado, "Fatorial"
# Fatorial é usado para indicar o produto entre n números naturais.
# "n!": indicamos com "n" que é qualquer número pertencente ao conjunto dos números naturais (ex: 1,2,3,4...).
# e o "!" é para indicar que é fatorial, que é acrescido de -1 e assim sucessivamente(-1,-2,-3,-4...).
# ex: 5! = 5*4*3*2*1 (o 1 não é necessário ja que qualquer coisa multiplicada por 1 é ela mesma).
# 1° - temos a noção de que: n! --> n*(n-1)! --> n*(n-1)*(n-2)!
# 2° - o valor de n deve ser constante.

num = int(input('Digite um número:> ')) # esse é o nosso n.
fator = num # fator ira receber o valor de n para ser calculado o n! e também para ser printado.
result = num # é o resultado final de toda multiplicação
for i in range(1,num): # i é o nosso "-1".
    print(f'{fator} ',end='') # sera printado o primeiro valor.
    fator = num-i # fator = n - i
    result = result * fator # para sempre multiplicar o resultado.
    if i < num-1: # aqui é para ser printado a quantidade certa de "*"
        print(end='* ')
print(f'\no resultado foi: {result}')
