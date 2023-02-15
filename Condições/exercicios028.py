# Escreva um programa que faça o computador 'Pensar' em um número inteiro
# entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número
# escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

from time import sleep # foi importado o módulo 'sleep' da biblioteca 'time' para fazer parecer que o computador pareça estar 'pensando' em um número
from random import randint # foi importado da biblioteca 'random' o módulo 'randint' que ira gerar um número inteiro entre 0 e 5 (incluindo ambos).

num_comp = randint(0,5) # gerando o número
num_user = int(input('Digite um número e tente adivinhar qual escolhi:> ')) # usuário insere o seu número
print('Escolhendo um número',end='') # aqui é usado o ' end='' ' para fazer com que os pontos da estrutura de repetição for sejam printados nessa frase.

for i in range(0,3): # estrutura de repetição for para não ficar repetindo várias funções prints e sleep (não tinha necessidade da estrutura repetição for, só uma sugestão)
    print('.',end='')
    sleep(0.5)
print(end='\n') # aqui é feito uma quebra de linha para remover o end=''
if num_comp == num_user: # verificação se o usuário acertou o número escolhido pelo computador.
    print(f'Você acertou!, eu escolhi o número: {num_comp}')
else:
    print(f'Você errou!, eu escolhi o número: {num_comp}')

