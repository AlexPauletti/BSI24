import numpy as np

tamanho = 5

vetor = np.zeros(tamanho)

soma = 0
for i in range(tamanho):
    vetor[i] = float(input("Informe o número que queira adicionar à array: "))
    soma = soma + vetor[i]

print(f"A média dos números dentro da array é: {soma/tamanho}")