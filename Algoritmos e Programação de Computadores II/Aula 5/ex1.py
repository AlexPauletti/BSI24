import numpy as np
N = int(input("Informe o tamanho das matrizes: "))

M1 = np.zeros((N,N))
M2 = np.zeros((N,N))
M3 = np.zeros((N,N))

for a in range(N):
    for b in range(N):
        M1[a][b] = int(input("Informe o valor que queira adicionar à primeira matriz: "))

for c in range(N):
    for d in range(N):
        M2[c][d] = int(input("Informe o valor que queira adicionar à segunda matriz: "))


for e in range(N):
    for f in range(N):
        M3[e][f] = M1[e][f] + M2[e][f]


print(M3)