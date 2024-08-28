#reversor e capitalizador de nome 3000

nome = input("Informe seu nome: ")

nome = nome.upper()

for n in reversed(nome):
    print(n, end="")