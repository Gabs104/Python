frase = 'Curso em Vídeo Python'
print(frase.upper().count('O')) # uma forma de contar se tem determinado elemento em uma string
# fatiamentos
print(frase[9]) # me mostre o elemento da posição 9
print(frase[9:20]) # me mostre os elementos entre 9 e 20, incluindo 9 e excluindo 20
print(frase[:11:2]) # me mostre desde o inicio até o 11° elemento pulando de 2 casas.
print(frase[::3]) # me mostre do inicio até o fim pulando de 3 casas.

print(frase.lower()) # ira colocar toda a string em minúscula.

print(len(frase)) # comprimento da String

frase_1 = '  Curso  em Vídeo Python   '
print(frase_1.strip()) # ira remover espaços desnecessários, (os espaços entre strings adicionais que são desnecessários não foram removidos)

# um método para remover espaços desnecessários que se encontram entre os elementos da string
frase_1 = frase_1.split() # primeiro divide a string em uma lista
frase_1 = ' '.join(frase_1) # depois ela é juntada novamente com .join()
print(frase_1)


frase = frase.replace('Python','Android') # ira trocar 'Python' por 'Android'
print(frase)
frase = frase.replace('Android','Python') # ira trocar 'Android' por 'Python'.

print('Curso'in frase) # ira verificar se 'Python' está em frase, valor retornado é booleano.
print('Android' in frase) # ira verificar se 'Android' está em frase, valor retornado é booleano.

print(frase.lower().find('curso')) #ira deixa toda a frase em minúscula e ira procurar por 'curso' retornando aonde esta o primeiro elemento de 'curso' que é 'c'

div = frase.split() # ira dividir a String em uma lista.

print(div[0] [3]) # pegue o item da posição 0 e me mostre o 3 elemento deste item.