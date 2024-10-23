import numpy as np

M = 10
matriz = np.zeros((M,M))

for a in range(M):
    for b in range(M):
        matriz[a][b] = input("Informe o valor que queira adicionar à matriz: ")
        
soma = 0
for c in range(M):
    soma = soma + matriz[c][1]

soma2 = 0
for c in range(M):
    soma = soma + matriz[c][c]

print(soma, soma2)