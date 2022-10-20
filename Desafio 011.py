largura = int(input('Qual a largura da parede? '))
altura = int(input('Qual a altura da parede? '))
metros2 = largura * altura
litros = metros2/2
print(f'Sabendo que cada litro de tinta pinta 2m²\nVocê precisará de {litros} litros de tinta, para pintar os {metros2}m² de parede.')