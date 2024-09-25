import numpy as np

tamanho = 10

x = np.zeros(tamanho)

for i in range(tamanho):
    x[i] = float(input(f"Informe o valor que quer adicionar à array [x]: "))

print(x)