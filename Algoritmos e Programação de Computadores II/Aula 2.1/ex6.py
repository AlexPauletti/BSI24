import numpy as np

M = []
KM = np.zeros(5)

for a in range(5):
    modelo = input("Informe o modelo de carro que vai adicionar: ")
    M.append(modelo)

    km = input("Quantos kilômetros ele faz por litro? ")
    KM[a] = km


maior = 0
for b in range(5):
    if M[b] > maior:
        maior = M[b]
        