import numpy as np

tamanho = 5

vetor = np.zeros(tamanho)


for i in range(tamanho):
    vetor[i] = float(input("Informe o número que queira adicionar à array: "))
    

maior = vetor[0]
menor = vetor[0]    

for a in vetor:
    if a < menor:
     menor = a

    if a > maior:
     maior = a


print(f"O menor número da lista é {menor} e o maior é {maior}")