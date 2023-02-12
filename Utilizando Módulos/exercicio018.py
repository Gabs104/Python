# Faça um programa que leia um ângulo qualquer e mostre na tela o valor
# do seno, cosseno e tangente desse ângulo.

from math import cos,sin,radians # importação dos módulos seno, cosseno e radianos
ang = float(input('digite um ângulo:> ')) # valor do ângulo
ang_s = sin(radians(ang)) # sera dado o seno do ângulo 'ang' (ângulo é primeiro convertido em radianos pois o módulo 'sin' funciona apenas com radianos)
ang_c = cos(radians(ang)) # sera dado o cosseno do ângulo 'ang'
print(f'o seno e o cosseno deste ângulo de {ang}° é, respectivamente: {ang_s}, {ang_c}')