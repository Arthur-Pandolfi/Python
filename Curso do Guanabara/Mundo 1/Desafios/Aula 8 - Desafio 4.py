from random import choice
a1 = str(input('Qual o nome do 1º aluno? '))
a2 = str(input('Qual o nome do 2º aluno? '))
a3 = str(input('Qual o nome do 3º aluno? '))
a4 = str(input('Qual o nome do 4º aluno? '))
alunos = [a1, a2, a3, a4]
escolhido = choice(alunos)
print(f'Entre os alunos {a1}, {a2}, {a3}, {a4}, o escolhido foi {escolhido}')

