nome:str = input('Qual o seu nome? ')
print('Prazer em te conhecer {:20}!!'.format(nome)) #Deixa 20 espaços após o nome
print('Prazer em te conhecer {:>20}!!'.format(nome))#Deixa o nome alinhado à direita
print('Prazer em te conhecer {:<20}!!'.format(nome))#Deixa o nome alinhado à esquerda
print('Prazer em te conhecer {:^20}!!'.format(nome)) #Deixa o nome centralizado
print('Prazer em te conhecer {:=^20}!!'.format(nome))#Preeche os espaços que sobraram com o caractere à escolha

