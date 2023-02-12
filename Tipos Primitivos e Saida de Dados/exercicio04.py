# Faça um programa que leia algo pelo teclado e mostre na tela seu tipo primitivo
# e todas as informações possíveis sobre ele.

dado = input('digite algo: ')
# verificação de caracteristicas da variável
print(f'o tipo primitivo de {dado} é {type(dado)}.')
print(f'o valor é um número?: {dado.isnumeric()}')
print(f'o valor é uma letra?: {dado.isalpha()}')
print(f'o valor é alfanumérico?: {dado.isnumeric()}')
print(f'o valor é decimal?: {dado.isdecimal()}')
print(f'o valor esta em maiúsculo? {dado.isupper()}')
print(f'o valor esta em minúsculo? {dado.islower()}')
