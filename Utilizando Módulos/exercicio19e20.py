# Um professor quer sortear um dos seus quatro alunos
# para apagar o quadro. Faça um programa que ajude
# ele, lendo o nome deles e escrevendo o nome
# do escolhido.

from random import choice,shuffle # o choice tem a função de escolher 1 elemento de uma lista
alunos = ['Kamilla','Jordan','Renatão','João'] # criamos uma lista para usar no módulo choice que ira escolher entre os 4 elementos dados (uma lista não é necessária, poderiamos ter colocado as strings dentro do choice())
shuffle(alunos)
print('Kamilla, Jordan, Renatão e João, um de vocês sera escolhido para apagar o quadro!')
print(f'e esse aluno é você: {choice(alunos)}! hahahaha!') # aluno escolhido é printado
print(f'e a ordem de apresentação do trabalho sera 1°:{alunos[0]}, 2°: {alunos[1]}, 3°: {alunos[2]}, 4°: {alunos[3]}')