import numpy as np

matriz = np.zeros((5,5))
SL = np.zeros(5)
SC = np.zeros(5)
soma = 0

for a in range(5):
    for b in range(5):
        matriz[a][b] = int(input("Informe o valor que queira adicionar à matriz: "))
    
for a in range(5):
    for b in range(5):
        soma = soma + matriz[a][b]
        if b == 4:
            SL[a] = soma
            soma = 0


for a in range(5):
    for b in range(5):
        soma = soma + matriz[b][a]
        if b == 4:
            SC[a] = soma
            soma = 0


for b in range(5):
    print(SL[b], end=' ')

for b in range(5):
    print(SC[b], end=' ')