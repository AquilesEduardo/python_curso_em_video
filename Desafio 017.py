'''from math import sqrt
cat_op = int(input('Qual o tamanho do cateto oposto? '))
cat_adj = int(input('Qual o tamanho do cateto adjacente? '))
hipotenusa = sqrt((cat_op**2)+(cat_adj**2))
print(f'O valor da hipotenusa é: {hipotenusa}')'''

'''Ou podemos fazer de outro jeito'''
import math
cat_op = int(input('Qual o tamanho do cateto oposto? '))
cat_adj = int(input('Qual o tamanho do cateto adjacente? '))
hipo = math.hypot(cat_adj, cat_op)
print(f'O valor da hipotenusa é: {hipo}')