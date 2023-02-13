# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome 'SANTO'.

cidade = str(input('Qual cidade você nasceu:> '))
cidade = cidade.strip().split() # aqui sera removidos os espaços desnecessários entre os elementos e as que estão nos cantos.
cidade = ' '.join(cidade) # sera juntado novamente a string.
print(f'você nasceu em {cidade.title()}!') # title() é usado para deixar bonitinho.
print('SANTO' in cidade.upper()) # verificação se tem a palavra 'SANTOS' na cidade em que o usuário nasceu.