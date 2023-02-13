# Crie um programa que leia o nome completo de uma pessoa e mostre:
# > O nome com todas as letras maiúsculas
# > O nome com todas minúsculas.
# > Quantas letras tem ao todo (sem considerar espaços).
# > Quantas letras tem o primeiro nome.

nome = input('Insira seu nome:> ') # primeiro vem a atribuição do nome do usuário
nome = nome.strip().split() # vai ser usado para o calculo de comprimento e também para a remoção de espaços desnecessários.
nome_div = nome # usado para contar o primeiro nome da pessoa.
nome_m = ' '.join(nome) # juntar a string novamente
nome_len = ''.join(nome) # para usar no calculo de letras sem contar os espaços do meio.

print(f'seu nome com todas as letras maiúsculas é: {nome_m.upper()}')
print(f'seu nome com todas as letras minúsculas é: {nome_m.lower()}')
print(f'seu nome tem {len(nome_len)} letras')
print(f'seu primeiro nome tem {len(nome_div[0])} letras')