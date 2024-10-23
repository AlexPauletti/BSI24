import numpy as np
N = 4
matriz = np.zeros((N,N))
vetor = []

for a in range(N):
    for b in range(N):
        matriz[a][b] = int(input("Informe o valor que queira adicionar à matriz: "))

print(matriz)        

a = int(input("Informe um valor para multiplicar pela matriz "))

for c in range(N):
    for d in range(N):
        vetor.append((matriz[c][d]) * a)

for a in range(len(vetor)):
    print(vetor[a])