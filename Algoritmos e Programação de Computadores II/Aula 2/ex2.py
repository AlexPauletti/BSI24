x = []
tamanhoLista = 10
par = []
impar = []

for a in range(tamanhoLista):
    tome = float(input("Informe o valor que queira adicionar à lista: "))
    x.append(tome)

    if tome%2 == 0:
        x[a] = tome*a

    else:
        x[a] = a

print(x)