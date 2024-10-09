import numpy as np

M = 5
matriz = np.zeros((M,M))

for a in range(M):
    for b in range(M):
        matriz[a][b] = input("Informe o valor que queira adicionar à matriz: ")
        
for c in range(M):
    print(matriz[c][c])