import numpy as np

tamanho = 10

vetor = np.zeros(tamanho)

pos = 0
pos2 = 0
maior = vetor[0]
menor = vetor[0]    
for i in range(tamanho):
    vetor[i] = float(input("Informe o número que queira adicionar à array: "))
    
    if vetor[i] < menor:
     menor = vetor[i]
     pos = i

    if vetor[i] > maior:
     maior = vetor[i]
     pos2 = i



print(f"O menor número está na posição {pos}, e o maior na posição {pos2}")