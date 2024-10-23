import numpy as np
#matriz = [['Brasil', 'Italia', [10, 9]], ['Brasil', 'Espanha', [5, 7]], ['Italia', 'Espanha', [7,8]]]

matriz = np.zeros((3,3))

for a in range(3):
    for b in range(3):
        if b == 2:
            matriz[a][b][0] = int(input("Informe o número de faltas do primeiro time: "))
            matriz[a][b][1] = int(input("Informe o número de faltas do segundo time: "))
        matriz[a][b] = input("Informe o time: ")
