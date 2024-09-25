x = []
y = []
xy = []
tamanhoLista = 5
soma = 0
soma2 = 0

for a in range(tamanhoLista):
    tome = int(input("Informe o valor que queira adicionar à primeira lista: "))
    x.append(tome)

for b in range(tamanhoLista):
    tome2 = int(input("Informe o valor que queira adicionar à segunda lista: "))
    y.append(tome2)

cont = tamanhoLista - 1
for c in range(tamanhoLista):
    xy.append(x[c]*y[cont])
    cont = cont - 1


print(f"A soma dos valores das listas é {xy}")
