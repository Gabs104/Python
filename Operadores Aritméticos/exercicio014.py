# Escreva um programa que converta uma temperatura digitada 
# em °C e converta para °F
# Formula para calcular °F >: F = C*1.8+32
# Essa formula foi feita da modificação desta >: C = F-32/1.8

cel = float(input('Informe a temperatura em °C: '))
fah = (cel*1.8) + 32
print(f'a temperatura °{cel:.1f}C é: °{(fah):.1f}F')