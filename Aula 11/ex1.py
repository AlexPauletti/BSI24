nome = input("Insira seu nome: ")

nome = nome.upper()


for w in reversed(nome):
    print(w, end="")