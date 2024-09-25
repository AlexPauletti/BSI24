import numpy as np

A = np.zeros(10)
B = np.zeros(10)
C = np.zeros(20)

for a in range(10):
    aAdd = int(input("Informe o número que irá adicionar ao primeiro vetor: "))
    A[a] = aAdd

for b in range(10):
    bAdd = int(input("Informe o número que irá adicionar ao segundo vetor: "))
    B[b] = bAdd

cont = 0
contA = 0
contB = 0
for c in range(10):
    C[cont] = A[contA]
    cont += 1
    contA += 1

    C[cont] = B[contB]
    cont += 1
    contB += 1

for d in range(20):
    print(C[d], end=", ")

