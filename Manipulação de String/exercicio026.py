# Faça um programa que leia uma frase pelo teclado e mostre:
# Quantas vezes aparece a letra 'A' .count()
# Em que posição ela aparece a primeira vez. .find()
# Em que posição ela aparece a última vez. .find()

nome = str(input('Informe seu Nome:> '))
nome = nome.strip().split()
nome = ''.join(nome)
nome = nome.upper()
print(f'a letra A aparece {nome.count("A")} vezes em seu nome!')
print(f'a letra A aparece a primeira vez na posição {nome.find("A",1)+1}°')
print(f'a letra A aparece a ultima vez na posição {nome.rfind("A")+1}°') # o rfind() ira procurar começando da direta da string. (ao inves de procurar no sentido '>' ele ira procurar no sentido '<')