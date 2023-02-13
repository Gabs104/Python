em linguagem de programação existe algo chamado cadeia de caracteres
ou 'String'

ex: 'Curso em Video Python'
O que sera visto na aula 9 sera a manipulação destas strings.
vamos atribuir essa string a uma variável

frase = 'Curso em Vídeo Python'
ao fazer isso o computador grava essa informação em sua memória
e ele divide essa frase fazendo com que cada letra ocupe um bloquinho e receba um index

index é seu posicionamento.
por exemplo: a letra C de 'Curso em Vídeo Python' está na posição 0, e é o 1° elemento desta String.

e o total de caracteres 'presentes em Curso em Vídeo Python' é 21.
e seus index vão de 0 até 20.

com essa informação de que cada letra em uma String tem um posicionamento podemos realizar certas funções em relação a isso.

Fatiamento: é pegar uma parte de uma String.
ex: frase[9] > estamos indicando que queremos o elemento que está na 9° posição da String.
o elemento retornado sera 'V' pois é o elemento que ocupa a 9° posição

outra forma de fatiamento é:
frase[9:13] > ele ira retornar elementos dentro desse intervalo começando da posição 9 até a 13, excluindo o 13° elemento.

sera retornado 'Víde', mas se eu quissese 'Vídeo'?
então usamos frase[9:14].

frase[9:21] > ira retornar elementos dentro deste intervalo.
'mas na frase a posição 21 não existe.' exato, e ela não sera incluida pois o último elemento do fatiamento é excluido.

frase[9:21] > 'Vídeo Python'

temos também frase[9:21:2]
'comece da posição 9, va até 21 e pule de 2 casas.'
o valor retornado sera: 'VdoPto'

frase[:5] > 'começa do 1° e vai até a 5° posição, excluindo o elemento da 5° posição'.
frase[5] > 'Curso'
frase[15:] > 'começa do 15° e vai até o final'
frase[15:] > 'Python'.

frase[9::3] > 'Começa do 9° vai até o final e pule 3 casas'
frase[9::3] > 'VePh'

Agora temos os métodos e funções de análise de String.

-Análise-

a função len() ira retornar a quantidade de caracteres de uma String
len = length = comprimento.
ex: len(frase) > 21.

temos o método .count() que ira contar quantas vezes uma determinada caracter aparece.
frase = 'Curso em Vídeo Python'
ex: frase.count('o') > 3

'frase.count('o',0,13)' os números presentes no método são em qual intervalo sera realizado a procura. comece de 0 e va até 13, excluindo o elemetno da posição 13.

ex: frase.count('o',0,13) > 1

frase.find('deo') ira procurar aonde começou determinada string.
ela ira retornar o valor da primeira letra da frase inserida dentro de .find() que no caso é 'd'.

ex: frase.find('deo') > 11

frase.find('Android') a palavra 'Android' não existe na frase, então o valor retornado sera '-1'. indica que não existe este elemento nesta string.

Temos um verificador também, indicado desta forma > 'Curso' in frase
o valor retornado sera booleano que sera 'True' pois 'Curso' está em frase.

-Transformações-

Temos Transformações de String.

uma delas é o método .replace() que ira substituir um elemento por outro.

ex: frase.replace('Python','Android') primeiro indicamos qual parte da frase iremos substituir depois por qual palavra.

frase.upper() ira transformar aquilo que é minúsculo em uma string para maiúscula
ex: frase.upper() > 'CURSO EM VÍDEO PYTHON'.

frase.upper() mesma coisa que upper só que o contrário.
ex: frase.lower() > 'curso em vídeo python'.

frase.captalize() ira colocar todos os elementos em minúsculo exceto pelo primeiro elemento da string.

ex: frase.captalize() > 'Curso em vídeo python'

frase.title() ira colocar cada segmento da String em maiúscula.
ex: frase.title() > 'Curso Em Vídeo Python'

vamos mudar a frase para '   Aprenda Python  ' note que espaços desnecessários foram adicionados. existem métodos de transformação para remover esses espaçõs.

um deles é o .strip() ele ira remover esses espaços que foram adicionados desnecessariamente.

ex: frase.strip() > 'Aprende Python' o espaço do meio não foi removido pois ele é
um espaço que divide uma palavra da outra.

temos o rstrip() que é a remoção de espaços desnecessário que estão pela direita.
frase.rstrip() > '   Aprenda Python'

e temos o lstrip() que é a remoção de espaços desnecessários que estão pela esquerda.

frase.lstrip() > 'Aprenda Python  '

-Divisão-

mudando a frase novamente para 'Curso em Vídeo Python'
e agora vamos ver as divisões de String.

o método split() ira dividir a string de acordo com os espaços e vai criar uma lista apartir desta string.

ex: frase.split() > ['Curso','em','Vídeo','Python']
seguindo a lógica de uma lista, cada elemento recebe um posicionamento.

se quisermos fazer com que essa lista vire novamente uma String apenas, usamos o método .join()

'-'.join(frase) > 'Curso-em-Vídeo-Python' note que o '-' substitui os espaços.
e cola novamente a string.