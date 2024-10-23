import numpy as np

matriz = np.zeros((2,2))

for a in range(2):
    for b in range(2):
        matriz[a][b] = int(input("Informe o valor que queira adicionar à matriz: "))

determinante = (matriz[0][0] * matriz[1][1]) - (matriz[0][1] * matriz[1][0])
print(determinante)
