import numpy as np
N = 10
matriz = np.zeros((N,N))
aux = []
aux2 = []

for a in range(N):
    for b in range(N):
        matriz[a][b] = input("Informe o valor que queira adicionar à matriz: ")

for a in range(N):
    aux.append(matriz[2][a])
    aux2.append(matriz[5][a])

for b in range(N):
    matriz[2][b] = matriz[8][b]
    matriz[8][b] = aux[b]

    matriz[5][b] = matriz[9][b]
    matriz[9][b] = aux2[b]


print(matriz)