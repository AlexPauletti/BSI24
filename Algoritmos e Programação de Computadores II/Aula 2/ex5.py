x = []
y = []
xy = []
tamanhoLista = 5


for a in range(tamanhoLista):
    tome = int(input("Informe o valor que queira adicionar à primeira lista: "))
    x.append(tome)

for b in range(tamanhoLista):
    tome2 = int(input("Informe o valor que queira adicionar à segunda lista: "))
    y.append(tome2)

for c in range(tamanhoLista):
    xy.append(x[c])   
for c in range(tamanhoLista):
    xy.append(y[c])

print(f"A terceira lista é {xy}")
