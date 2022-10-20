nome = input("Digite uma palavra: ")
print(f"O tipo primitivo desse valor é: {type(nome)}")
print(f"Só tem espaços? {nome.isspace()}")
print(f"É alfabético? {nome.isalpha()}")
print(f"É alfanumérico? {nome.isalnum()}")
print(f"Está em maiúsculas? {nome.isupper()}")
print(f"Está em minúsculas? {nome.islower()}")
print(f"Está capitalizada? {nome.istitle()}")

