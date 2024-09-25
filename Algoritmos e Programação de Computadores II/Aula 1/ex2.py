import numpy as np

tamanho = 5

vetor = np.zeros(tamanho)

for i in range(tamanho):
    vetor[i] = float(input("Informe o número que queira adicionar à array: "))

soma = 0
for s in vetor:
    soma = soma + s

print(f"A soma dos números dentro da array é: {soma}")