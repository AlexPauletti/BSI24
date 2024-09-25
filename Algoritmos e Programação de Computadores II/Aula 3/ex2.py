import numpy as np
np.set_printoptions(legacy='1.25')

tamanhoV = 9
V = np.zeros(9)
primos = []
pos = []

for a in range(tamanhoV):
    V[a] = int(input("Informe o valor que deseja adicionar: "))

cont = 0
for b in V:
    if b == 2:
            primos.append(b)
            pos.append(cont)
            
    if b%2 == 1:
        if b == 1:
            print("Para você que não sabia, 1 não é número primo")

        elif b%3!=0 and b%5!=0 and b%7!=0 and b%9!=0 and b%11!=0:
            primos.append(b)
            pos.append(cont)
    
    cont += 1


print(f"Números primos: {primos}")
print(f"Suas posições: {pos}")


