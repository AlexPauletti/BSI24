import numpy as np

M = 5
matriz = np.zeros((M,M))

for a in range(M):
    for b in range(M):
        matriz[b][a] = input("Informe o valor que queira adicionar à matriz: ")
        
print(matriz)