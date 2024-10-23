import numpy as np

mult = []
for a in range(5):
    mult.append(int(input("Informe os valores que queira multiplicar as linhas da matriz: ")))

matriz = np.zeros((5,5,))

for a in range(5):
    for b in range(5):
        matriz[a][b] = int(input("Informe o valor que queira adicionar à matriz: "))

for a in range(5):
    for b in range(5):
        matriz[a][b] = matriz[a][b] * mult[a]


print(matriz)