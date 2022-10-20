import math
num = float(input('Qual o ângulo? '))
radiano = math.radians(num)
print(f'O Seno, Cosseno e Tangente de {num}, respectivamente são {math.sin(radiano)}, {math.cos(radiano)}, {math.tan(radiano):.2f} ')