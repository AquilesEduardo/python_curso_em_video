import random

aluno1 = input('Aluno 1')
aluno2 = input('Aluno 2')
aluno3 = input('Aluno 3')
aluno4 = input('Aluno 4')

lista = [aluno1, aluno2, aluno3, aluno4]
emabaralhada = random.shuffle(lista)
print(f'A ordem embaralhada de {lista} é: \n {emabaralhada}')
#Por que a variavel 'embaralhara' retornou None ao invés de uma lista alterada??