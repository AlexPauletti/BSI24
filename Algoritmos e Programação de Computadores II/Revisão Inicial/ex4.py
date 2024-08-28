nome = input("Informe seu nome: ")
cont = 1

nome = nome.upper()

for a in range(len(nome)):
    cutelo = slice(cont)
    print(nome[cutelo])
    cont+=1
