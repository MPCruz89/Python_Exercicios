from random import  choice

a1 = input('Informe o nome de um aluno: ')
a2 = input('Informe o nome de um aluno: ')
a3 = input('Informe o nome de um aluno: ')
a4 = input('Informe o nome de um aluno: ')

alunos = [a1, a2, a3, a4]

sorteado = choice(alunos)

print('O aluno sorteado foi {}'.format(sorteado))

